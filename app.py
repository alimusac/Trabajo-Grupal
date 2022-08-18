import enum
import numpy as np
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def page_0():
    st.write('# energyco2.csv')
    st.write('Fuente: https://www.kaggle.com/datasets/lobosi/c02-emission-by-countrys-grouth-and-population')
    tabla = pd.read_csv('energyco2.csv')
    tabla.drop(columns=['Unnamed: 0'], inplace = True)
    tabs = st.tabs(['Original', 'Sin Datos vacíos'])
    with tabs[0]:
        st.write('## Dataset Original:')
        st.dataframe(tabla)
        cols = st.columns(2)
        cols[0].info('Número de registros: {}'.format(len(tabla)))
        cols[1].info('Número de columnas: {}'.format(len(tabla.columns)))
    with tabs[1]:
        st.write('## Dataset sin datos vacíos:')

        st.dataframe(tabla.dropna())
        cols = st.columns(2)
        cols[0].info('Número de registros: {}'.format(len(tabla.dropna())))
        cols[1].info('Número de columnas: {}'.format(len(tabla.columns)))
    
    descriptions = {
        'Country': 'País en cuestión',
        'Energy_type': 'Tipo de fuente de energía',
        'Year': 'Año en que la información fue guardada',
        'Energy_consumption': 'Cantidad de consumo de energía medida (Quad BTU)',
        'Energy_production': 'Cantidad de producción de energía medida (Quad BTU)',
        'GDP': 'PIB de los paídes en paridad de poder adquisitivo (Miles de millones de 2015$ PPP)',
        'Population': 'Población medida en Miles de personas',
        'Energy_intensity_per_capita': 'Medida de la ineficiencia energética de una economía. (MMBTU/person)',
        'Energy_intensity_by_GDP': 'Medida de la ineficiencia energética de una economía. (Miles de BTU/2015GDP PPP)',
        'CO2_emission': 'Cantidad emitida de CO2 (Miles de millones de toneladas)',
    }
    columnas_primordiales = ['Country', 'Energy_type', 'Year']
    col = st.selectbox('Seleccione la columna analizar:', tabla.columns)
    st.write('### {}'.format(col))
    cols = st.columns(2)
    cols[0].write('Descripción: **{}**'.format(descriptions[col]))
    cols[0].write('Número de datos vacíos: **{}**'.format(len(tabla[col]) - len(tabla[col].dropna())))
    cols[0].write('Porcentaje de vacíos en DS: **{:.2f}%**'.format((len(tabla[col]) - len(tabla[col].dropna()))/len(tabla)*100))
    dato = tabla.loc[0,col]
    cols[0].write('Tipo de dato: **{}**'.format(type(dato)))
    if type(dato) == str or type(dato)==float:
        cols[0].write('Cantidad de valores únicos: **{}**'.format(len(tabla[col].dropna().unique())))
        cols[1].dataframe(pd.Series(tabla[col].unique(), name=col), height=200)
    elif type(dato) == np.int64:
        min = tabla[col].min()
        max = tabla[col].max()
        cols[0].write('Valor mínimo: **{}**'.format(min))
        cols[0].write('Valor máximo: **{}**'.format(max))
        cols[1].dataframe(pd.Series(tabla[col].unique(), name=col), height=310)
    elif type(tabla.loc[0,col]) == np.float64:
        cols[1].write('Valor mínimo: **{:.2f}**'.format(tabla[col].min()))
        cols[1].write('Valor máximo: **{:.2f}**'.format(tabla[col].max()))
        cols[1].write('Promedio en dataset: **{:.2f}**'.format(tabla[col].mean()))
        cols[1].write('Desviación estándar: **{:.2f}**'.format(tabla[col].std()))
        st.write('----')
        # Agrupación
        cols2 = st.columns(2)
        col_agrup = cols2[0].radio('Agrupar por:', columnas_primordiales)
        cols2[0].write('----')
        tipo_agrup = cols2[0].radio('Tipo agrupación:', ['Promedio', 'Suma', 'Conteo'])
        if tipo_agrup == 'Promedio':
            tabla_agr = tabla[[col_agrup, col]].groupby(col_agrup).mean().reset_index().sort_values(col_agrup)
        elif tipo_agrup == 'Suma':
            tabla_agr = tabla[[col_agrup, col]].groupby(col_agrup).sum().reset_index().sort_values(col_agrup)
        else:
            tabla_agr = tabla[[col_agrup, col]].groupby(col_agrup).count().reset_index().sort_values(col_agrup)
        cols2[1].write(tipo_agrup + ' por la columna "' + col_agrup + '"')
        cols2[1].dataframe(tabla_agr, height=250)
    st.write('------')

def page_1():
    st.write('# global_power_plant_database.csv')
    st.write('Fuente: http://datasets.wri.org/dataset/globalpowerplantdatabase')
    tabla = pd.read_csv('global_power_plant_database.csv', dtype={'other_fuel1':str, 'other_fuel2':str, 'other_fuel3':str})
    tabs = st.tabs(['Original', 'Sin Datos vacíos'])
    with tabs[0]:
        st.write('## Dataset Original:')
        st.dataframe(tabla)
        cols = st.columns(2)
        cols[0].info('Número de registros: {}'.format(len(tabla)))
        cols[1].info('Número de columnas: {}'.format(len(tabla.columns)))
    with tabs[1]:
        st.write('## Dataset sin datos vacíos:')

        st.dataframe(tabla.dropna())
        cols = st.columns(2)
        cols[0].info('Número de registros: {}'.format(len(tabla.dropna())))
        cols[1].info('Número de columnas: {}'.format(len(tabla.columns)))
   
    descriptions = {'country':'Cod pais', 'country_long':'Pais', 'name':'Nombre', 
                    'gppd_idnr':'Identificador de la planta de energia', 'capacity_mw': 'capacidad de generación eléctrica en mw',
                    'latitude':'Latitud', 'longitude':'Longitud', 'primary_fuel':'Fuente de energia primaria', 'other_fuel1':'Otras fuentes 1', 
                    'other_fuel2':'Otras fuentes 2','other_fuel3':'Otras fuentes 3', 'commissioning_year':'Fecha de puesta en operacion',
                    'owner':'Dueño', 'source':'Fuente', 'url':'Pagina web',
                    'geolocation_source':'Fuente de geolocalizacion', 'wepp_id':'Identificador unico de planta', 
                    'year_of_capacity_data':'Fecha de la informacion',
                    'generation_gwh_2013':'Generacion de electricidad en el 2013', 'generation_gwh_2014':'Generacion de electricidad en el 2014', 
                    'generation_gwh_2015':'Generacion de electricidad en el 2015','generation_gwh_2016':'Generacion de electricidad en el 2016', 
                    'generation_gwh_2017':'Generacion de electricidad en el 2017', 'generation_gwh_2018':'Generacion de electricidad en el 2018',
                    'generation_gwh_2019':'Generacion de electricidad en el 2019', 'generation_data_source':'Fuente de generacion de datos',
                    'estimated_generation_gwh_2013':'Generacion electrica estimada en el 2013', 
                    'estimated_generation_gwh_2014':'Generacion electrica estimada en el 2014',
                    'estimated_generation_gwh_2015':'Generacion electrica estimada en el 2015', 
                    'estimated_generation_gwh_2016':'Generacion electrica estimada en el 2016',
                    'estimated_generation_gwh_2017':'Generacion electrica estimada en el 2017', 
                    'estimated_generation_note_2013':'Etiqueta del modelo/metodo utilizado para estimar la generación electrica en el 2013',
                    'estimated_generation_note_2014':'Etiqueta del modelo/metodo utilizado para estimar la generación electrica en el 2014', 
                    'estimated_generation_note_2015':'Etiqueta del modelo/metodo utilizado para estimar la generación electrica en el 2015',
                    'estimated_generation_note_2016':'Etiqueta del modelo/metodo utilizado para estimar la generación electrica en el 2016', 
                    'estimated_generation_note_2017':'Etiqueta del modelo/metodo utilizado para estimar la generación electrica en el 2017',
                }

    columnas_primordiales = ['country_long']
    col = st.selectbox('Seleccione la columna analizar:', tabla.columns)
    st.write('### {}'.format(col))
    cols = st.columns(2)
    cols[0].write('Descripción: **{}**'.format(descriptions[col]))
    cols[0].write('Número de datos vacíos: **{}**'.format(len(tabla[col]) - len(tabla[col].dropna())))
    cols[0].write('Porcentaje de vacíos en DS: **{:.2f}%**'.format((len(tabla[col]) - len(tabla[col].dropna()))/len(tabla)*100))
    dato = tabla.loc[0,col]
    cols[0].write('Tipo de dato: **{}**'.format(type(dato)))
    if type(dato) == str or type(dato)==float:
        cols[0].write('Cantidad de valores únicos: **{}**'.format(len(tabla[col].dropna().unique())))
        cols[1].dataframe(pd.Series(tabla[col].unique(), name=col), height=200)
    elif type(dato) == np.int64:
        min = tabla[col].min()
        max = tabla[col].max()
        cols[0].write('Valor mínimo: **{}**'.format(min))
        cols[0].write('Valor máximo: **{}**'.format(max))
        cols[1].dataframe(pd.Series(tabla[col].unique(), name=col), height=310)
    elif type(tabla.loc[0,col]) == np.float64:
        cols[1].write('Valor mínimo: **{:.2f}**'.format(tabla[col].min()))
        cols[1].write('Valor máximo: **{:.2f}**'.format(tabla[col].max()))
        cols[1].write('Promedio en dataset: **{:.2f}**'.format(tabla[col].mean()))
        cols[1].write('Desviación estándar: **{:.2f}**'.format(tabla[col].std()))
        st.write('----')
        # Agrupación
        cols2 = st.columns(2)
        col_agrup = cols2[0].radio('Agrupar por:', columnas_primordiales)
        cols2[0].write('----')
        tipo_agrup = cols2[0].radio('Tipo agrupación:', ['Promedio', 'Suma', 'Conteo'])
        if tipo_agrup == 'Promedio':
            tabla_agr = tabla[[col_agrup, col]].groupby(col_agrup).mean().reset_index().sort_values(col_agrup)
        elif tipo_agrup == 'Suma':
            tabla_agr = tabla[[col_agrup, col]].groupby(col_agrup).sum().reset_index().sort_values(col_agrup)
        else:
            tabla_agr = tabla[[col_agrup, col]].groupby(col_agrup).count().reset_index().sort_values(col_agrup)
        cols2[1].write(tipo_agrup + ' por la columna "' + col_agrup + '"')
        cols2[1].dataframe(tabla_agr, height=250)
    st.write('------')

def page_2():
    st.write('# owid-energy-consumption-source.csv')
    st.write('https://github.com/owid/energy-data')
    tabla = pd.read_csv('owid-energy-consumption-source.csv')
    tabs = st.tabs(['Original', 'Sin Datos vacíos'])
    with tabs[0]:
        st.write('## Dataset Original:')
        st.dataframe(tabla)
        cols = st.columns(2)
        cols[0].info('Número de registros: {}'.format(len(tabla)))
        cols[1].info('Número de columnas: {}'.format(len(tabla.columns)))
    with tabs[1]:
        st.write('## Dataset sin datos vacíos:')

        st.dataframe(tabla.dropna())
        cols = st.columns(2)
        cols[0].info('Número de registros: {}'.format(len(tabla.dropna())))
        cols[1].info('Número de columnas: {}'.format(len(tabla.columns)))
    df_dicc = pd.read_csv('owid_diccionario_traduccion.csv')
    descriptions = df_dicc[['Nombre_col_en', 'Descripcion']].set_index('Nombre_col_en').T.to_dict('records')[0]
    columnas_primordiales = ['country', 'year']
    col = st.selectbox('Seleccione la columna analizar:', tabla.columns)
    st.write('### {}'.format(col))
    cols = st.columns(2)
    cols[0].write('Descripción: **{}**'.format(descriptions[col]))
    cols[0].write('Número de datos vacíos: **{}**'.format(len(tabla[col]) - len(tabla[col].dropna())))
    cols[0].write('Porcentaje de vacíos en DS: **{:.2f}%**'.format((len(tabla[col]) - len(tabla[col].dropna()))/len(tabla)*100))
    dato = tabla.loc[0,col]
    cols[0].write('Tipo de dato: **{}**'.format(type(dato)))
    if type(dato) == str or type(dato)==float:
        cols[0].write('Cantidad de valores únicos: **{}**'.format(len(tabla[col].dropna().unique())))
        cols[1].dataframe(pd.Series(tabla[col].unique(), name=col), height=200)
    elif type(dato) == np.int64:
        min = tabla[col].min()
        max = tabla[col].max()
        cols[0].write('Valor mínimo: **{}**'.format(min))
        cols[0].write('Valor máximo: **{}**'.format(max))
        cols[1].dataframe(pd.Series(tabla[col].unique(), name=col), height=310)
    elif type(tabla.loc[0,col]) == np.float64:
        cols[1].write('Valor mínimo: **{:.2f}**'.format(tabla[col].min()))
        cols[1].write('Valor máximo: **{:.2f}**'.format(tabla[col].max()))
        cols[1].write('Promedio en dataset: **{:.2f}**'.format(tabla[col].mean()))
        cols[1].write('Desviación estándar: **{:.2f}**'.format(tabla[col].std()))
        st.write('----')
        # Agrupación
        cols2 = st.columns(2)
        col_agrup = cols2[0].radio('Agrupar por:', columnas_primordiales)
        cols2[0].write('----')
        tipo_agrup = cols2[0].radio('Tipo agrupación:', ['Promedio', 'Suma', 'Conteo'])
        if tipo_agrup == 'Promedio':
            tabla_agr = tabla[[col_agrup, col]].groupby(col_agrup).mean().reset_index().sort_values(col_agrup)
        elif tipo_agrup == 'Suma':
            tabla_agr = tabla[[col_agrup, col]].groupby(col_agrup).sum().reset_index().sort_values(col_agrup)
        else:
            tabla_agr = tabla[[col_agrup, col]].groupby(col_agrup).count().reset_index().sort_values(col_agrup)
        cols2[1].write(tipo_agrup + ' por la columna "' + col_agrup + '"')
        cols2[1].dataframe(tabla_agr, height=250)
    st.write('------')

def page_3():
    st.write('# GlobalLandTemperaturesByCountry.csv')
    st.write('https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data')
    tabla = pd.read_csv('GlobalLandTemperaturesByCountry.csv')
    tabs = st.tabs(['Original', 'Sin Datos vacíos'])
    with tabs[0]:
        st.write('## Dataset Original:')
        st.dataframe(tabla)
        cols = st.columns(2)
        cols[0].info('Número de registros: {}'.format(len(tabla)))
        cols[1].info('Número de columnas: {}'.format(len(tabla.columns)))
    with tabs[1]:
        st.write('## Dataset sin datos vacíos:')

        st.dataframe(tabla.dropna())
        cols = st.columns(2)
        cols[0].info('Número de registros: {}'.format(len(tabla.dropna())))
        cols[1].info('Número de columnas: {}'.format(len(tabla.columns)))
    descriptions = {
        'dt': 'Fecha',
        'AverageTemperature': 'Temperatura promedio en grados centígrados',
        'AverageTemperatureUncertainty': 'Incertidumbre de la temperatura en grados centígrados',
        'Country': 'Pais de registro'
    }
    columnas_primordiales = ['dt', 'Country']
    col = st.selectbox('Seleccione la columna analizar:', tabla.columns)
    st.write('### {}'.format(col))
    cols = st.columns(2)
    cols[0].write('Descripción: **{}**'.format(descriptions[col]))
    cols[0].write('Número de datos vacíos: **{}**'.format(len(tabla[col]) - len(tabla[col].dropna())))
    cols[0].write('Porcentaje de vacíos en DS: **{:.2f}%**'.format((len(tabla[col]) - len(tabla[col].dropna()))/len(tabla)*100))
    dato = tabla.loc[0,col]
    cols[0].write('Tipo de dato: **{}**'.format(type(dato)))
    if type(dato) == str or type(dato)==float:
        cols[0].write('Cantidad de valores únicos: **{}**'.format(len(tabla[col].dropna().unique())))
        cols[1].dataframe(pd.Series(tabla[col].unique(), name=col), height=200)
    elif type(dato) == np.int64:
        min = tabla[col].min()
        max = tabla[col].max()
        cols[0].write('Valor mínimo: **{}**'.format(min))
        cols[0].write('Valor máximo: **{}**'.format(max))
        cols[1].dataframe(pd.Series(tabla[col].unique(), name=col), height=310)
    elif type(tabla.loc[0,col]) == np.float64:
        cols[1].write('Valor mínimo: **{:.2f}**'.format(tabla[col].min()))
        cols[1].write('Valor máximo: **{:.2f}**'.format(tabla[col].max()))
        cols[1].write('Promedio en dataset: **{:.2f}**'.format(tabla[col].mean()))
        cols[1].write('Desviación estándar: **{:.2f}**'.format(tabla[col].std()))
        st.write('----')
        # Agrupación
        cols2 = st.columns(2)
        col_agrup = cols2[0].radio('Agrupar por:', columnas_primordiales)
        cols2[0].write('----')
        tipo_agrup = cols2[0].radio('Tipo agrupación:', ['Promedio', 'Suma', 'Conteo'])
        if tipo_agrup == 'Promedio':
            tabla_agr = tabla[[col_agrup, col]].groupby(col_agrup).mean().reset_index().sort_values(col_agrup)
        elif tipo_agrup == 'Suma':
            tabla_agr = tabla[[col_agrup, col]].groupby(col_agrup).sum().reset_index().sort_values(col_agrup)
        else:
            tabla_agr = tabla[[col_agrup, col]].groupby(col_agrup).count().reset_index().sort_values(col_agrup)
        cols2[1].write(tipo_agrup + ' por la columna "' + col_agrup + '"')
        cols2[1].dataframe(tabla_agr, height=250)
    st.write('------')
    pass


def page_4():
    repo_path = 'https://github.com/alimusac/Trabajo-Grupal'
    st.title('El calentamiento global en el mundo')
    st.write('La comunidad internacional se ha puesto de acuerdo para evitar que el aumento promedio de la temperatura mundial no supere los 2 °C por encima de los niveles pre-industriales. Para tal fin, todos los países presentan en forma voluntaria un compromiso para disminuir sus emisiones de dióxido de carbono para el 2030.')
    st.write('Sin embargo, distintos tipos de estudios advierten que los estragos de la polución ya están dejando sus huellas en el presente.')
    st.image('diario1.jpg')
    st.image('diario2.jpg')
    st.write('A tal fin la ONU ha organizado distintas comisiones, una por un continente, para corroborar que cada país esté en camino a cumplir con las NDC (Contribuciones Determinadas a Nivel Nacional) del Acuerdo de París.')
    st.title(' AC(Comisión Americana)')
    st.write('Debemos realizar un informe sobre la situación en América para la IPCC (Grupo Intergubernamental de Expertos Sobre el Cambio Climático) para que nuclee la información y realice un informe general para la ONU.')
    st.title('KPI')
    st.title('Equipo')
    st.title('Organización')
      
    st.write('------')

page_names_to_funcs = {
    "1 - energyco2": page_0,
    "2 - global_power_plant_database": page_1,
    "3 - owid-energy-consumption-source": page_2,
    "4 - GlobalLandTemperaturesByCountry": page_3,
    "5 - Presentacion": page_4
}

selected_page = st.sidebar.selectbox("Seleccione página", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()