from turtle import title
import numpy as np
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def page_0():
    # 'https://github.com/alimusac/Trabajo-Grupal'
    cols = st.columns((2,3))
    cols[0].title('El calentamiento global en el mundo')
    cols[0].write('La comunidad internacional se ha puesto de acuerdo para evitar que el aumento **promedio de la temperatura mundial no supere los 2 °C** por encima de los niveles pre-industriales. Para tal fin, todos los países presentan en forma voluntaria un compromiso para disminuir sus emisiones de dióxido de carbono para el 2030.')
    cols[0].write('Sin embargo, distintos tipos de estudios advierten que los estragos de la polución ya están dejando sus huellas en el presente:')
    tabs = cols[1].tabs(['Link1', 'link2', 'link3', 'link4', 'link5'])
    tabs[0].image('diario1.jpg')
    tabs[0].caption('ℹ️ https://www.france24.com/es/minuto-a-minuto/20220810-el-agua-de-lluvia-no-es-potable-debido-a-los-químicos-según-un-estudio')
    tabs[1].image('diario2.jpg')
    tabs[1].caption('ℹ️ https://www.bbc.com/mundo/noticias-61389005')
    tabs[2].image('diario3.jpg')
    tabs[2].caption('ℹ️ https://www.jornada.com.mx/notas/2022/08/18/economia/creciente-necesidad-de-recursos-para-hacer-frente-al-cambio-climatico-fmi/')
    tabs[3].image('diario4.jpg')
    tabs[3].caption('ℹ️ https://www.meteored.mx/noticias/ciencia/la-comunicacion-del-cambio-climatico-y-los-eventos-extremos-en-los-medios.html')
    tabs[4].image('diario5.jpg')
    tabs[4].caption('ℹ️ https://www.dw.com/es/el-mundo-debe-prepararse-para-los-peores-escenarios-de-extinci%C3%B3n-debido-al-cambio-clim%C3%A1tico/a-62689096')
    st.write('----')
    cols = st.columns(2)
    cols[0].title(' LC(Comisión Latinoamericana)')
    cols[0].write('La ONU ha organizado distintas comisiones para corroborar que cada país esté en camino a cumplir con las NDC (Contribuciones Determinadas a Nivel Nacional) del Acuerdo de París.')
    cols[0].write('Debemos realizar un informe sobre la situación en Latinoamérica para la IPCC (Grupo Intergubernamental de Expertos Sobre el Cambio Climático) para que nuclee la información y realice un informe general para la ONU.')
    # cols[0].write('Los puntos a trabajar son:')
    cols[1].title("KPI's")
    tabs2 = cols[1].tabs(['1 - Compromiso','2 - Acceso','3 - Renovable','4 - Eficiencia','5 - Temperatura'])
    tabs2[0].write('Analizar el compromiso que cada país realizó y ver si (a cinco años del mismo) están encaminados en su cumplimiento.')
    with tabs2[0].expander('Imagen'):
        st.image('NDC.jpg')  
    tabs2[1].write('Garantizar el acceso universal a servicios energéticos asequibles, fiables y modernos para el 2030.')
    tabs2[2].write('Aumentar considerablemente la proporción de energía renovable en el conjunto de fuentes energéticas para el 2030.')
    tabs2[3].write('Duplicar la tasa mundial de mejora de la eficiencia energética para el 2030')
    tabs2[4].write('Que la temperatura de Latinoamérica no supere los 1,5°C a las mediciones de la época preindustrial.')
    cols[0].title('Equipo')
    cols[0].write('La LC(Comisión Latinoamericana) ya está trabajando en el análisis exploratorio de datos a través de la información obtenida.')
    cols[0].write('Esta información se presenta en los siguientes archivos que podemos explorar:')
    cols[0].write('- energyco2.csv')
    cols[0].write('- global_power_plant_database.csv')
    cols[0].write('- owid-energy-consumption-source.csv')
    cols[0].write('- GlobalLandTemperaturesByCountry.csv')


def page_1():
    st.write('# energyco2.csv')
    st.write('Fuente: https://www.kaggle.com/datasets/lobosi/c02-emission-by-countrys-grouth-and-population')
    tabla = pd.read_csv('energyco2.csv')
    tabla.drop(columns=['Unnamed: 0'], inplace = True)
    tabs = st.tabs(['Original', 'Sin Datos vacíos'])
    with tabs[0]:
        st.write('## Dataset Original:')
        cols = st.columns((3,1))
        cols[0].dataframe(tabla)
        cols[1].write('----')
        cols[1].info('Número de registros: {}'.format(len(tabla)))
        cols[1].write('----')
        cols[1].info('Número de columnas: {}'.format(len(tabla.columns)))
        cols[1].write('----')
    with tabs[1]:
        st.write('## Dataset sin datos vacíos:')
        cols = st.columns((3,1))
        cols[0].dataframe(tabla.dropna())
        cols[1].write('----')
        cols[1].info('Número de registros: {}'.format(len(tabla.dropna())))
        cols[1].write('----')
        cols[1].info('Número de columnas: {}'.format(len(tabla.columns)))
        cols[1].write('----')
    st.write('----')
    
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
        cols2 = st.columns((1,1,3))
        col_agrup = cols2[0].radio('Agrupar por:', columnas_primordiales)
        cols2[0].write('----')
        tipo_agrup = cols2[0].radio('Tipo agrupación:', ['Promedio', 'Suma', 'Conteo'])
        cols2[0].write('----')
        if tipo_agrup == 'Promedio':
            tabla_agr = tabla[[col_agrup, col]].groupby(col_agrup).mean().reset_index().sort_values(col_agrup)
        elif tipo_agrup == 'Suma':
            tabla_agr = tabla[[col_agrup, col]].groupby(col_agrup).sum().reset_index().sort_values(col_agrup)
        else:
            tabla_agr = tabla[[col_agrup, col]].groupby(col_agrup).count().reset_index().sort_values(col_agrup)
        cols2[1].write(tipo_agrup + ' por la columna "' + col_agrup + '"')
        cols2[1].dataframe(tabla_agr, height=450)
        if len(tabla_agr) < 50: tipo_graph = cols2[0].radio('Tipo de gráfico:', ['Barra', 'Linea', 'Pastel'])
        else: tipo_graph = cols2[0].radio('Tipo de gráfico:', ['Barra', 'Linea'])
        fig = go.Figure()
        if tipo_graph == 'Barra':
            fig.add_trace(go.Bar(x = tabla_agr[col_agrup], y= tabla_agr[col]))
        elif tipo_graph == 'Linea':
            fig.add_trace(go.Scatter(x = tabla_agr[col_agrup], y= tabla_agr[col], mode='lines'))
        elif tipo_graph == 'Pastel':
            fig.add_trace(go.Pie(labels = tabla_agr[col_agrup], values= tabla_agr[col]))
        fig.update_layout(title=col+' agrupado por '+col_agrup)
        cols2[2].plotly_chart(fig)
    st.write('------')
    pass

def page_2():
    st.write('# global_power_plant_database.csv')
    st.write('Fuente: http://datasets.wri.org/dataset/globalpowerplantdatabase')
    tabla = pd.read_csv('global_power_plant_database.csv', dtype={'other_fuel1':str, 'other_fuel2':str, 'other_fuel3':str})
    tabs = st.tabs(['Original', 'Sin Datos vacíos'])
    with tabs[0]:
        st.write('## Dataset Original:')
        cols = st.columns((3,1))
        cols[0].dataframe(tabla)
        cols[1].write('----')
        cols[1].info('Número de registros: {}'.format(len(tabla)))
        cols[1].write('----')
        cols[1].info('Número de columnas: {}'.format(len(tabla.columns)))
        cols[1].write('----')
    with tabs[1]:
        st.write('## Dataset sin datos vacíos:')
        cols = st.columns((3,1))
        cols[0].dataframe(tabla.dropna())
        cols[1].write('----')
        cols[1].info('Número de registros: {}'.format(len(tabla.dropna())))
        cols[1].write('----')
        cols[1].info('Número de columnas: {}'.format(len(tabla.columns)))
        cols[1].write('----')
    st.write('----')
   
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
        cols2 = st.columns((1,1,3))
        col_agrup = cols2[0].radio('Agrupar por:', columnas_primordiales)
        cols2[0].write('----')
        tipo_agrup = cols2[0].radio('Tipo agrupación:', ['Promedio', 'Suma', 'Conteo'])
        cols2[0].write('----')
        if tipo_agrup == 'Promedio':
            tabla_agr = tabla[[col_agrup, col]].groupby(col_agrup).mean().reset_index().sort_values(col_agrup)
        elif tipo_agrup == 'Suma':
            tabla_agr = tabla[[col_agrup, col]].groupby(col_agrup).sum().reset_index().sort_values(col_agrup)
        else:
            tabla_agr = tabla[[col_agrup, col]].groupby(col_agrup).count().reset_index().sort_values(col_agrup)
        cols2[1].write(tipo_agrup + ' por la columna "' + col_agrup + '"')
        cols2[1].dataframe(tabla_agr, height=450)
        if len(tabla_agr) < 50: tipo_graph = cols2[0].radio('Tipo de gráfico:', ['Barra', 'Linea', 'Pastel'])
        else: tipo_graph = cols2[0].radio('Tipo de gráfico:', ['Barra', 'Linea'])
        fig = go.Figure()
        if tipo_graph == 'Barra':
            fig.add_trace(go.Bar(x = tabla_agr[col_agrup], y= tabla_agr[col]))
        elif tipo_graph == 'Linea':
            fig.add_trace(go.Scatter(x = tabla_agr[col_agrup], y= tabla_agr[col], mode='lines'))
        elif tipo_graph == 'Pastel':
            fig.add_trace(go.Pie(labels = tabla_agr[col_agrup], values= tabla_agr[col]))
        fig.update_layout(title=col+' agrupado por '+col_agrup)
        cols2[2].plotly_chart(fig)
    st.write('------')
    pass

def page_3():
    st.write('# owid-energy-consumption-source.csv')
    st.write('https://github.com/owid/energy-data')
    tabla = pd.read_csv('owid-energy-consumption-source.csv')
    tabs = st.tabs(['Original', 'Sin Datos vacíos'])
    with tabs[0]:
        st.write('## Dataset Original:')
        cols = st.columns((3,1))
        cols[0].dataframe(tabla)
        cols[1].write('----')
        cols[1].info('Número de registros: {}'.format(len(tabla)))
        cols[1].write('----')
        cols[1].info('Número de columnas: {}'.format(len(tabla.columns)))
        cols[1].write('----')
    with tabs[1]:
        st.write('## Dataset sin datos vacíos:')
        cols = st.columns((3,1))
        cols[0].dataframe(tabla.dropna())
        cols[1].write('----')
        cols[1].info('Número de registros: {}'.format(len(tabla.dropna())))
        cols[1].write('----')
        cols[1].info('Número de columnas: {}'.format(len(tabla.columns)))
        cols[1].write('----')
    st.write('----')
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
        cols2 = st.columns((1,1,3))
        col_agrup = cols2[0].radio('Agrupar por:', columnas_primordiales)
        cols2[0].write('----')
        tipo_agrup = cols2[0].radio('Tipo agrupación:', ['Promedio', 'Suma', 'Conteo'])
        cols2[0].write('----')
        if tipo_agrup == 'Promedio':
            tabla_agr = tabla[[col_agrup, col]].groupby(col_agrup).mean().reset_index().sort_values(col_agrup)
        elif tipo_agrup == 'Suma':
            tabla_agr = tabla[[col_agrup, col]].groupby(col_agrup).sum().reset_index().sort_values(col_agrup)
        else:
            tabla_agr = tabla[[col_agrup, col]].groupby(col_agrup).count().reset_index().sort_values(col_agrup)
        cols2[1].write(tipo_agrup + ' por la columna "' + col_agrup + '"')
        cols2[1].dataframe(tabla_agr, height=450)
        if len(tabla_agr) < 50: tipo_graph = cols2[0].radio('Tipo de gráfico:', ['Barra', 'Linea', 'Pastel'])
        else: tipo_graph = cols2[0].radio('Tipo de gráfico:', ['Barra', 'Linea'])
        fig = go.Figure()
        if tipo_graph == 'Barra':
            fig.add_trace(go.Bar(x = tabla_agr[col_agrup], y= tabla_agr[col]))
        elif tipo_graph == 'Linea':
            fig.add_trace(go.Scatter(x = tabla_agr[col_agrup], y= tabla_agr[col], mode='lines'))
        elif tipo_graph == 'Pastel':
            fig.add_trace(go.Pie(labels = tabla_agr[col_agrup], values= tabla_agr[col]))
        fig.update_layout(title=col+' agrupado por '+col_agrup)
        cols2[2].plotly_chart(fig)
    st.write('------')
    pass

def page_4():
    st.write('# GlobalLandTemperaturesByCountry.csv')
    st.write('https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data')
    tabla = pd.read_csv('GlobalLandTemperaturesByCountry.csv')
    tabs = st.tabs(['Original', 'Sin Datos vacíos'])
    with tabs[0]:
        st.write('## Dataset Original:')
        cols = st.columns((3,1))
        cols[0].dataframe(tabla)
        cols[1].write('----')
        cols[1].info('Número de registros: {}'.format(len(tabla)))
        cols[1].write('----')
        cols[1].info('Número de columnas: {}'.format(len(tabla.columns)))
        cols[1].write('----')
    with tabs[1]:
        st.write('## Dataset sin datos vacíos:')
        cols = st.columns((3,1))
        cols[0].dataframe(tabla.dropna())
        cols[1].write('----')
        cols[1].info('Número de registros: {}'.format(len(tabla.dropna())))
        cols[1].write('----')
        cols[1].info('Número de columnas: {}'.format(len(tabla.columns)))
        cols[1].write('----')
    st.write('----')
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
        cols2 = st.columns((1,1,3))
        col_agrup = cols2[0].radio('Agrupar por:', columnas_primordiales)
        cols2[0].write('----')
        tipo_agrup = cols2[0].radio('Tipo agrupación:', ['Promedio', 'Suma', 'Conteo'])
        cols2[0].write('----')
        if tipo_agrup == 'Promedio':
            tabla_agr = tabla[[col_agrup, col]].groupby(col_agrup).mean().reset_index().sort_values(col_agrup)
        elif tipo_agrup == 'Suma':
            tabla_agr = tabla[[col_agrup, col]].groupby(col_agrup).sum().reset_index().sort_values(col_agrup)
        else:
            tabla_agr = tabla[[col_agrup, col]].groupby(col_agrup).count().reset_index().sort_values(col_agrup)
        cols2[1].write(tipo_agrup + ' por la columna "' + col_agrup + '"')
        cols2[1].dataframe(tabla_agr, height=450)
        if len(tabla_agr) < 50: tipo_graph = cols2[0].radio('Tipo de gráfico:', ['Barra', 'Linea', 'Pastel'])
        else: tipo_graph = cols2[0].radio('Tipo de gráfico:', ['Barra', 'Linea'])
        fig = go.Figure()
        if tipo_graph == 'Barra':
            fig.add_trace(go.Bar(x = tabla_agr[col_agrup], y= tabla_agr[col]))
        elif tipo_graph == 'Linea':
            fig.add_trace(go.Scatter(x = tabla_agr[col_agrup], y= tabla_agr[col], mode='lines'))
        elif tipo_graph == 'Pastel':
            fig.add_trace(go.Pie(labels = tabla_agr[col_agrup], values= tabla_agr[col]))
        fig.update_layout(title=col+' agrupado por '+col_agrup)
        cols2[2].plotly_chart(fig)
    st.write('------')
    pass

page_names_to_funcs = {
    "0 - Presentacion": page_0,
    "1 - energyco2": page_1,
    "2 - global_power_plant_database": page_2,
    "3 - owid-energy-consumption-source": page_3,
    "4 - GlobalLandTemperaturesByCountry": page_4,
}
st.set_page_config(page_title = 'Presentación', page_icon='Ⓛ', layout='wide', initial_sidebar_state='collapsed')
selected_page = st.sidebar.selectbox("Seleccione página", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()