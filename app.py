# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# %% Librerias
import pandas as pd
#import tkinter as tk
import numpy as np

import time
#from datetime import datetime
from datetime import date

import dash

#import dash_core_components as dcc
#import dash_html_components as html
import plotly.graph_objs as go
from dash import dcc
from dash import html
import plotly.express as px
from dash.dependencies import Input, Output
from dash import Dash, html, dcc, Output, Input, callback,  State, dash_table
import dash_bootstrap_components as dbc

from dash import dash_table as dt
from reportlab.pdfgen import canvas
#from PIL import Image
from dash.exceptions import PreventUpdate
from pymongo import MongoClient


# %% Importar datos

# Movimientos de bodegas
url = 'https://drive.google.com/file/d/1J6fxtiLztklxNP1zWiEgHE44FhdS9625/view?usp=sharing'
path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
movbod = pd.read_csv(path)

#movbod = pd.read_csv('movbod.csv')



# Stock total bodegas
url = 'https://drive.google.com/file/d/1f3ayIeyfbkP0CmyAMalQHt9Zs8CBsFVI/view?usp=sharing'
path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
stocktotalbodmas = pd.read_csv(path)

#stocktotalbodmas = pd.read_csv('stocktotalbodmas.csv')

# Imagen

url = 'https://drive.google.com/file/d/1lANWYiQYrPKmVx-8JNGY66mjmhxKKPcr/view?usp=sharing'
path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
ok = (path)
#ok = Image.open('EEQ.png','r')

# PDF

#url = 'https://drive.google.com/file/d/14f0wP0bWuv01nXmUlvBgc_2lC1sPzkJ2/view?usp=sharing'
##path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
#pdf = (path)




# %% PRUEBAS
#consumoprom = movbod

#df_masky=consumoprom['TIPO_x']== 'EGRESO'
#consumoprom2 = consumoprom [df_masky]

#dffq = movbod2. groupby(['Descripcion_cod', 'BODEGA', 'CENTRO_DE_COSTO', 'Tipopersonal', 'ENTREGA_O_RECIBE', 'AUTORIZADOR', 'TIPO_x', 'MMI',
                            #'PRIORIZAR_COMPRA', 'CRITICO', 'Motivo', 'FECHA_', 'FECHA', 'Grupomas50', 'DESC_SDI']).VALOR_TOTAL.sum().sort_values(ascending=False)
#dffq = dffq.to_frame()
#dffq = dffq.reset_index(level='Descripcion_cod')
#dffq = dffq.reset_index(level='BODEGA')
#dffq = dffq.reset_index(level='CENTRO_DE_COSTO')
#dffq = dffq.reset_index(level='Tipopersonal')
#dffq = dffq.reset_index(level='ENTREGA_O_RECIBE')
#dffq = dffq.reset_index(level='AUTORIZADOR')
  #dffq = dffq.reset_index(level='TIPO_x')
    #dffq = dffq.reset_index(level='MMI')
    #dffq = dffq.reset_index(level='PRIORIZAR_COMPRA')


# %% Datos para las cartas informativas
# 1

miles_translator = str.maketrans(".,", ",.")



Total = movbod. groupby(
    ['TIPO_x']).VALOR_TOTAL.sum().sort_values(ascending=False)
Total = Total.to_frame()
Total['mov'] = Total.index
Total = round(Total)
pd.options.display.float_format = '${:,.2f}'.format
# descriocion
dese = Total['mov'].tolist()
dese1 = dese[0]
dese2 = dese[1]
# descriocion
cantu = Total['VALOR_TOTAL'].tolist()
cantu1 = cantu[0]
cantu1 = f"{cantu1:,}".translate(miles_translator)
cantu2 = cantu[1]
cantu2 = f"{cantu2:,}".translate(miles_translator)

#Total = movbod. groupby (['TIPO_x']).VALOR_TOTAL.sum().sort_values(ascending = False)

#Total = movbod['VALOR_TOTAL'].sum()
card = dbc.Card(
    [
        dbc.CardHeader("Valor tipo de movimientos"),
        dbc.CardBody(
            [
                #html.H4("Valor en dólares", className="card-title"),
                html.P(f' {dese1} $ {cantu1}  ', className="card-text"),
                html.P(f' {dese2} $ {cantu2}     ', className="card-text"),



            ]
        ),
        #dbc.CardFooter("This is the footer"),
    ],

)

# 2

df_mask = movbod['TIPO_x'] == "EGRESO"
filtegre = movbod[df_mask]


Total1 = filtegre. groupby(['TIPO_x', 'DESC_SDI']
                           ).VALOR_TOTAL.sum().sort_values(ascending=False)
Total1 = Total1.to_frame()
Total1 = Total1.reset_index(level='TIPO_x')
Total1 = Total1.reset_index(level='DESC_SDI')
Total1 = round(Total1)
# descriocion
dese = Total1['DESC_SDI'].tolist()
dese1 = dese[0]
dese2 = dese[1]
# descriocion
cantu = Total1['VALOR_TOTAL'].tolist()
cantu1 = cantu[0]

cantu1 = f"{cantu1:,}".translate(miles_translator)

cantu2 = cantu[1]

cantu2 = f"{cantu2:,}".translate(miles_translator)


#Total = movbod. groupby (['TIPO_x']).VALOR_TOTAL.sum().sort_values(ascending = False)

#Total = movbod['VALOR_TOTAL'].sum()
card1 = dbc.Card(
    [
        dbc.CardHeader("Valor de egresos"),
        dbc.CardBody(
            [
                #html.H4("Valor en dólares", className="card-title"),
                html.P(f' {dese1} $ {cantu1}  ', className="card-text"),
                html.P(f' {dese2} $ {cantu2}     ', className="card-text"),



            ]
        ),
        #dbc.CardFooter("This is the footer"),
    ],

)

# 3

df_mask = movbod['TIPO_x'] == "REINGRESO"
filtegre = movbod[df_mask]


Total1 = filtegre. groupby(['TIPO_x', 'DESC_SDI']
                           ).VALOR_TOTAL.sum().sort_values(ascending=False)
Total1 = Total1.to_frame()
Total1 = Total1.reset_index(level='TIPO_x')
Total1 = Total1.reset_index(level='DESC_SDI')
Total1 = round(Total1)
# descriocion
dese = Total1['DESC_SDI'].tolist()
dese1 = dese[0]
dese2 = dese[1]
# descriocion
cantu = Total1['VALOR_TOTAL'].tolist()
cantu1 = cantu[0]

cantu1 = f"{cantu1:,}".translate(miles_translator)
cantu2 = cantu[1]

cantu2 = f"{cantu2:,}".translate(miles_translator)
#Total = movbod. groupby (['TIPO_x']).VALOR_TOTAL.sum().sort_values(ascending = False)

#Total = movbod['VALOR_TOTAL'].sum()
card2 = dbc.Card(
    [
        dbc.CardHeader("Valor de reingresos"),
        dbc.CardBody(
            [
                #html.H4("Valor en dólares", className="card-title"),
                html.P(f' {dese1} $ {cantu1}  ', className="card-text"),
                html.P(f' {dese2} $ {cantu2}     ', className="card-text"),



            ]
        ),
        #dbc.CardFooter("This is the footer"),
    ],

)
# %% Cambiar tipo de dato fechas movimientos de bodegas
movbod['FECHA'] = pd.to_datetime(movbod['FECHA'], errors='coerce')
movbod['FECHA'] = movbod['FECHA'].dt.strftime('%d-%m-%Y')
movbod['FECHA'] = pd. to_datetime(movbod['FECHA'])
#df['fecha egreso'] =df['fecha egreso'].dt.strftime('%d-%m-%Y')
mini = movbod['FECHA'].min()
maxi = movbod['FECHA'].max()
# %% DASH CONFIGURACIÓN INICIAL

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server


# styling the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# padding for the page content
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

# %% DASH CONFIGURACIÓN INICIAL IMPORTAR DF PARA TABLA DE PRIORIAD DE COMPRA
dffls = stocktotalbodmas. groupby(['CODIGO','DESCRIPCION', 'STOCKTOTAL', 'CANTIDAD_SUGERIDAD_PARA_COMPRA', 'PRIORIZAR_COMPRA',
                                  'CODIGOCPC', 'FECHA_PROYECCION_FIN_MATERIAL', 'PORCENTAJE_DE_PRIORIDAD','UNIDAD',]).REGISTRO.count().sort_values(ascending=False)
dffls = dffls.to_frame()

dffls = dffls.reset_index(level='PORCENTAJE_DE_PRIORIDAD')

dffls = dffls.reset_index(level='FECHA_PROYECCION_FIN_MATERIAL')
dffls = dffls.reset_index(level='CANTIDAD_SUGERIDAD_PARA_COMPRA')
dffls = dffls.reset_index(level='PRIORIZAR_COMPRA')

dffls = dffls.reset_index(level='UNIDAD')
dffls = dffls.reset_index(level='STOCKTOTAL')
dffls = dffls.reset_index(level='DESCRIPCION')
dffls = dffls.reset_index(level='CODIGO')
dffls = dffls.reset_index(level='CODIGOCPC')
dffls = dffls.drop(['REGISTRO'], axis=1)
df_mask = dffls['PORCENTAJE_DE_PRIORIDAD'] > 49
dffls = dffls[df_mask]
dffls= dffls.drop_duplicates(['DESCRIPCION', 'CODIGO'], keep='last')
dffls = dffls.sort_values('FECHA_PROYECCION_FIN_MATERIAL', ascending=False)


# %% DASH CONFIGURACIÓN INICIAL IMPORTAR DF analisis por material
detal = stocktotalbodmas. groupby(['CODIGO', 'DESCRIPCION', 'NOMBREBODEGA', 'STOCKPORBODEGA',
                                   'Descripcion_cod','UNIDAD','ACTIVIDAD','CONSUMO_PROMEDIO_DIARIO','FECHA_PROYECCION_FIN_MATERIAL']).REGISTRO.count().sort_values(ascending=False)

detal = detal.to_frame()
detal = detal.reset_index(level='FECHA_PROYECCION_FIN_MATERIAL')
#detal = detal.reset_index(level='COBERTURA_MATERIAL_DIAS')
detal = detal.reset_index(level='CONSUMO_PROMEDIO_DIARIO')
detal = detal.reset_index(level='UNIDAD')  
detal = detal.reset_index(level='STOCKPORBODEGA')
detal = detal.reset_index(level='NOMBREBODEGA')
detal = detal.reset_index(level='Descripcion_cod')
detal = detal.reset_index(level='ACTIVIDAD')
detal = detal.reset_index(level='DESCRIPCION')
detal = detal.reset_index(level='CODIGO')
#detal = detal.reset_index(level='BODEGA')
detal=detal.drop(['Descripcion_cod'], axis=1)
detal=detal.drop(['REGISTRO'], axis=1)
#detal = detal.sort_values('BODEGA', ascending=True)



# %% DASH CONFIGURACIÓN barra lateral con opciones

sidebar = html.Div(
    [
        html.H2(html.Img(src=ok, style={'width': '100%', 'display': 'inline-block'
                                        }),),




        html.Hr(),
        html.P(
            "Seleccione opción:", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Detalle de materiales",
                            href="/", active="exact"),
                
                dbc.NavLink("Materiales con prioridad de compra",
                            href="/mats", active="exact"),



                dbc.NavLink("Egresos y reingresos cantidades",
                            href="/page-1", active="exact"),

                dbc.NavLink("Egresos y reingresos valorados",
                            href="/page-2", active="exact"),
                #dbc.NavLink("Generar informe movimiento de bodegas", href="/page-2", active="exact"),
                #dbc.NavLink("Generar informe por areas", href="/page-3", active="exact"),
                #dbc.Row([dbc.Col([card],),],style={'width': '100%', 'display': 'inline-block'}),

                html.P(
                    "Importancia de materiales:", className="lead"),

                html.Div(children=[
                    html.Label('Mat. mayor importancia'),
                    dcc.Dropdown(
                        id='dropdownmmi',
                        #options=[{'label': i, 'value': i} for i in options],
                        options=[{'label': c, 'value': c}
                                 for c in movbod['MMI'].unique()],
                        value='NA',
                        multi=True
                    )], style={'width': '100%', 'display': 'inline-block'}),


                html.Div(children=[
                    html.Label('Materiales con proridad de compra'),
                    dcc.Dropdown(
                        id='dropdownmcp',
                        #options=[{'label': i, 'value': i} for i in options],
                        options=[{'label': c, 'value': c}
                                 for c in movbod['PRIORIZAR_COMPRA'].unique()],
                        value='NA',
                        multi=True
                    )], style={'width': '100%', 'display': 'inline-block'}),


                html.Div(children=[
                    html.Label('Materiales criticos'),
                    dcc.Dropdown(
                        id='dropdownprio',
                        #options=[{'label': i, 'value': i} for i in options],
                        options=[{'label': c, 'value': c}
                                 for c in movbod['CRITICO'].unique()],
                        value='NA',
                        multi=True
                    )], style={'width': '100%', 'display': 'inline-block'}),


                #html.Div([

                    
                #html.Button("Descargar informe general ", id="infor_"),
                #dcc.Download(id="doinfor_"),

                # 'local' or 'session'
                #dcc.Store(id='store-data6', data=[], storage_type='memory')

                #], style={'width': '100%'}),
                





                # html.H1(children='Material mas reingresado',style={
                # 'color': 'Black','width': '5%', 'display': 'inline-block', 'font-size': 20
                # }),




            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

app.layout = html.Div(children=[

    # html.Img(src=okb,style={'width': '50%', 'display': 'inline-block'
    # }),


    dcc.Location(id="url"),
    sidebar,
    content,

])
    #html.Div(dcc.Graph(id='bod'),style={'width': '50%', 'display': 'inline-block'}),




# %% DASH DETALLE MATERIALES


@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def render_page_content(pathname):

    if pathname == "/":
        return [




            html.H1('Detalle de materiales',
                    style={'textAlign': 'center'}),
            
            
            
            
            
            

            html.Div(children=[
                html.Label('Seleccione material'),
                dcc.Dropdown(
                    id='dropdownmatok',
                    #options=[{'label': i, 'value': i} for i in options],
                    options=[{'label': c, 'value': c}
                             for c in stocktotalbodmas['Descripcion_cod'].unique()],
                    value='NA',
                    #virtualization=True,
                    #maxHeight=50,
                    multi=True)
                

                ], style={'width': '50%', 'display': 'inline-block'}),
            
            
            
            
            

            html.Div(children=[
                html.Label('Seleccione bodega'),
                dcc.Dropdown(
                    id='dropdownmatokbod',
                    #options=[{'label': i, 'value': i} for i in options],
                    options=[{'label': c, 'value': c}
                             for c in stocktotalbodmas['NOMBREBODEGA'].unique()],
                    value='NA',
                    multi=True
                )], style={'width': '35%', 'display': 'inline-block'}),



            html.Div(children=[
                html.Label('Material con actividad'),
                dcc.Dropdown(
                    id='dropdownmatokac',
                    #options=[{'label': i, 'value': i} for i in options],
                    options=[{'label': c, 'value': c}
                             for c in stocktotalbodmas['ACTIVIDAD'].unique()],
                    value='NA',
                    multi=True
                )], style={'width': '15%', 'display': 'inline-block'}),





            html.Div([
                html.Button("Descargar     Excel", id="btn_xlsxokzz"),
                dcc.Download(id="download-dataframe-xlsxokzz"),

                # 'local' or 'session'
                dcc.Store(id='store-dataokzz', data=[], storage_type='memory')

            ], style={'width': '100%'}),



            # CARTAS INFORMATIVAS

            
                    html.Div([
            #html.H4('Simple interactive table'),
            html.P(id='table_out'),
            dash_table.DataTable(
                id='table-container_',
                columns=[{"name": i, "id": i} 
                         for i in detal.columns],
                data=detal.to_dict('records'),
                style_cell=dict(textAlign='left'),
                style_header=dict(backgroundColor="paleturquoise"),
                style_data=dict(backgroundColor="lavender"),
                page_size=40,

            ), 
            ])
                    
                    
            
            #html.Div(children=[
                #html.Label('Material con actividad'),
                #dt.DataTable(
                    #id='table-container_',
                    #columns=[{"name": i, "id": i} for i in detal.columns],
                    #data = detal.to_dict("records"),
                    #options=[{'label': i, 'value': i} for i in options],
                #)]),





        ]








# %% DASH MATERIALES CON PRIORIDAD DE COMPRA 


    elif pathname == "/mats":
        return [

            html.H1('Materiales con prioridad de compra',
                    style={'textAlign': 'center'}),

            html.Div([
                html.Button("Descargar Excel ", id="btn_xlsx_"),
                dcc.Download(id="download-dataframe-xlsx_"),

                # 'local' or 'session'
                dcc.Store(id='store-data_', data=[], storage_type='memory')

            ], style={'width': '100%'}),


            #html.Div(dcc.Graph(id='tabla'),style={'width': '100%', 'display': 'inline-block'}),




            html.Div(children=[
                #html.Label('Material con actividad'),
                dt.DataTable(
                    id='table-container',
                    columns=[{"name": i, "id": i} for i in dffls.columns],
                    data = dffls.to_dict("records"),
                    #options=[{'label': i, 'value': i} for i in options],
                    style_cell=dict(textAlign='left'),
                )]),



            #html.Div(dcc.Graph(id='priocomprak'),style={'width': '100%', 'display': 'inline-block'}),





        ]




# %% DASH Análisis de transacciones

    elif pathname == "/page-1":
        return [




            html.H1('Análisis de transacciones',
                    style={'textAlign': 'center'}),

            html.Div(children=[
                html.Label('Seleccione material'),
                dcc.Dropdown(
                    id='dropdownmat',
                    #options=[{'label': i, 'value': i} for i in options],
                    options=[{'label': c, 'value': c}
                             for c in movbod['Descripcion_cod'].unique()],
                    value='NA',
                    multi=True
                )], style={'width': '80%', 'display': 'inline-block'}),


            html.Div(children=[
                html.Label('Tipo'),
                dcc.Dropdown(
                    id='dropdowntipogoi',
                    #options=[{'label': i, 'value': i} for i in options],
                    options=[{'label': c, 'value': c}
                             for c in movbod['DESC_SDI'].unique()],
                    value='NA',
                    multi=True
                )], style={'width': '10%', 'display': 'inline-block'}),







            html.Div(children=[
                html.Label('Tipo de personal'),
                dcc.Dropdown(
                    id='dropdowntipo',
                    #options=[{'label': i, 'value': i} for i in options],
                    options=[{'label': c, 'value': c}
                             for c in movbod['Tipopersonal'].unique()],
                    value='NA',
                    multi=True
                )], style={'width': '10%', 'display': 'inline-block'}),




            html.Div(children=[
                html.Label('Seleccione centro de costo'),
                dcc.Dropdown(
                    id='dropdowncc',
                    #options=[{'label': i, 'value': i} for i in options],
                    options=[{'label': c, 'value': c}
                             for c in movbod['CENTRO_DE_COSTO'].unique()],
                    value='NA',
                    multi=True
                )], style={'width': '50%', 'display': 'inline-block'}),







            html.Div(children=[
                html.Label('Seleccione personal'),
                dcc.Dropdown(
                    id='dropdownsonal',
                    #options=[{'label': i, 'value': i} for i in options],
                    options=[{'label': c, 'value': c}
                             for c in movbod['ENTREGA_O_RECIBE'].unique()],
                    value='NA',
                    multi=True
                )], style={'width': '50%', 'display': 'inline-block'}),


            html.Div(children=[
                html.Label('Seleccione autorizador'),
                dcc.Dropdown(
                    id='dropdownautor',
                    #options=[{'label': i, 'value': i} for i in options],
                    options=[{'label': c, 'value': c}
                             for c in movbod['AUTORIZADOR'].unique()],
                    value='NA',
                    multi=True
                )], style={'width': '50%', 'display': 'inline-block'}),


            html.Div(children=[
                html.Label('Seleccione bodega'),
                dcc.Dropdown(
                    id='dropdownboder',
                    #options=[{'label': i, 'value': i} for i in options],
                    options=[{'label': c, 'value': c}
                             for c in movbod['BODEGA'].unique()],
                    value='NA',
                    multi=True
                )], style={'width': '50%', 'display': 'inline-block'}),







            #html.Div(children=[
                #html.Label('Motivos de reingresos mayor al 50%'),
                #dcc.Dropdown(
                    #id='dropdownmas50',
                    #options=[{'label': i, 'value': i} for i in options],
                    #options=[{'label': c, 'value': c}
                             #for c in movbod['Motivo'].unique()],
                    #value='NA',
                    #multi=True
                #)], style={'width': '15%', 'display': 'inline-block'}),

            #html.Div(children=[
                #html.Label('Porcentaje de reingreso'),
                #dcc.Dropdown(
                    #id='dropdowngrmas50',
                    #options=[{'label': i, 'value': i} for i in options],
                    #options=[{'label': c, 'value': c}
                             #for c in movbod['Grupomas50'].unique()],
                    #value='NA',
                    #multi=True
                #)], style={'width': '10%', 'display': 'inline-block'}),











            html.Div(children=[
                html.Label('Seleccione fecha'),
                dcc.DatePickerRange(
                    id='my-date-picker-range',
                    min_date_allowed=movbod['FECHA'].min(),
                    max_date_allowed=movbod['FECHA'].max(),
                    initial_visible_month=date(2022, 6, 1),
                    # end_date=movbod['FECHA'].max(),
                    clearable=True,  # whether or not the user can clear the dropdo
                ),
                html.Div(id='output-container-date-picker-range'),
            ], style={'width': '50%', 'display': 'inline-block'}),



            html.Div([
                html.Button("Descargar     Excel", id="btn_xlsx"),
                dcc.Download(id="download-dataframe-xlsx"),

                # 'local' or 'session'
                dcc.Store(id='store-data', data=[], storage_type='memory')

            ], style={'width': '100%'}),






            # INFORMACIONES

            # html.Div([
            # dbc.Row([dbc.Col(card, width=3),
            #dbc.Col(card1, width=3),
            # dbc.Col(card2, width=3)], justify="center")]),  # justify="start", "center", "end", "between", "around"









            #html.Div(dcc.Graph(id='mate'),style={'width': '65%', 'display': 'inline-block'}),
            html.H5('Materiales y bodegas',
                    style={'textAlign': 'left'}),

            html.Div(dcc.Graph(id='mate'), style={
                     'width': '75%', 'display': 'inline-block'}),
            html.Div(dcc.Graph(id='bode'), style={
                     'width': '25%', 'display': 'inline-block'}),

            html.H5('Centros de costos y contratistas',
                    style={'textAlign': 'left'}),

            html.Div(dcc.Graph(id='centrocos'), style={
                     'width': '100%', 'display': 'inline-block'}),

            html.H5('Materiales  por linea de tiempo ',
                    style={'textAlign': 'left'}),


            html.Div(dcc.Graph(id='movmat'), style={
                     'width': '100%', 'display': 'inline-block'}),
            #html.Div(dcc.Graph(id='auto'), style={
                     #'width': '100%', 'display': 'inline-block'}),


            html.H5('Movimientos de materiales por gasto e inversión ',
                    style={'textAlign': 'left'}),


            html.Div(dcc.Graph(id='fini'), style={
                     'width': '100%', 'display': 'inline-block'}),

            # ANIMACIÓNXXXXXXXXXXXXXXXXXXXXX



            # html.Div(dcc.Graph(id='video',figure=px.scatter(dffc, x="CANTIDAD", y="BODEGA", animation_frame="FECHA", animation_group="AUTORIZADOR",size="VALOR_TOTAL",
            # color="CENTRO_DE_COSTO", hover_name="AUTORIZADOR",)),style={'width': '100%', 'display': 'inline-block'}),









        ]


# ESTUDIO ECONOMICO

# %% DASH Análisis de transacciones valorizadas

    elif pathname == "/page-2":
        return [




            html.H1('Análisis de transacciones valoradas',
                    style={'textAlign': 'center'}),

            html.Div(children=[
                html.Label('Seleccione material'),
                dcc.Dropdown(
                    id='dropdownmat3',
                    #options=[{'label': i, 'value': i} for i in options],
                    options=[{'label': c, 'value': c}
                             for c in movbod['Descripcion_cod'].unique()],
                    value='NA',
                    multi=True
                )], style={'width': '80%', 'display': 'inline-block'}),


            html.Div(children=[
                html.Label('Tipo'),
                dcc.Dropdown(
                    id='dropdowntipogoi3',
                    #options=[{'label': i, 'value': i} for i in options],
                    options=[{'label': c, 'value': c}
                             for c in movbod['DESC_SDI'].unique()],
                    value='NA',
                    multi=True
                )], style={'width': '10%', 'display': 'inline-block'}),







            html.Div(children=[
                html.Label('Tipo de personal'),
                dcc.Dropdown(
                    id='dropdowntipo3',
                    #options=[{'label': i, 'value': i} for i in options],
                    options=[{'label': c, 'value': c}
                             for c in movbod['Tipopersonal'].unique()],
                    value='NA',
                    multi=True
                )], style={'width': '10%', 'display': 'inline-block'}),




            html.Div(children=[
                html.Label('Seleccione centro de costo'),
                dcc.Dropdown(
                    id='dropdowncc3',
                    #options=[{'label': i, 'value': i} for i in options],
                    options=[{'label': c, 'value': c}
                             for c in movbod['CENTRO_DE_COSTO'].unique()],
                    value='NA',
                    multi=True
                )], style={'width': '50%', 'display': 'inline-block'}),







            html.Div(children=[
                html.Label('Seleccione personal'),
                dcc.Dropdown(
                    id='dropdownsonal3',
                    #options=[{'label': i, 'value': i} for i in options],
                    options=[{'label': c, 'value': c}
                             for c in movbod['ENTREGA_O_RECIBE'].unique()],
                    value='NA',
                    multi=True
                )], style={'width': '50%', 'display': 'inline-block'}),


            html.Div(children=[
                html.Label('Seleccione autorizador'),
                dcc.Dropdown(
                    id='dropdownautor3',
                    #options=[{'label': i, 'value': i} for i in options],
                    options=[{'label': c, 'value': c}
                             for c in movbod['AUTORIZADOR'].unique()],
                    value='NA',
                    multi=True
                )], style={'width': '50%', 'display': 'inline-block'}),







            html.Div(children=[
                html.Label('Motivos de reingresos mayor al 50%'),
                dcc.Dropdown(
                    id='dropdownmas503',
                    #options=[{'label': i, 'value': i} for i in options],
                    options=[{'label': c, 'value': c}
                             for c in movbod['Motivo'].unique()],
                    value='NA',
                    multi=True
                )], style={'width': '25%', 'display': 'inline-block'}),

            html.Div(children=[
                html.Label('Porcentaje de reingreso'),
                dcc.Dropdown(
                    id='dropdowngrmas503',
                    #options=[{'label': i, 'value': i} for i in options],
                    options=[{'label': c, 'value': c}
                             for c in movbod['Grupomas50'].unique()],
                    value='NA',
                    multi=True
                )], style={'width': '25%', 'display': 'inline-block'}),











            html.Div(children=[
                html.Label('Seleccione fecha'),
                dcc.DatePickerRange(
                    id='my-date-picker-range3',
                    min_date_allowed=movbod['FECHA'].min(),
                    max_date_allowed=movbod['FECHA'].max(),
                    initial_visible_month=date(2022, 6, 1),
                    # end_date=movbod['FECHA'].max(),
                    clearable=True,  # whether or not the user can clear the dropdo
                ),


                html.Div(id='output-container-date-picker-range3'),
            ], style={'width': '45%', 'display': 'inline-block'}),



            html.Div([
                html.Button("Descargar     Excel", id="btn_xls_o"),
                dcc.Download(id="download-dataframe-xls_o"),

                # 'local' or 'session'
                dcc.Store(id='store_o', data=[], storage_type='memory')

            ], style={'width': '100%'}),






            # CARTAS INFORMATIVAS

            html.Div([
                dbc.Row([dbc.Col(card, width=3),
                         dbc.Col(card1, width=3),
                         dbc.Col(card2, width=3)], justify="center")]),  # justify="start", "center", "end", "between", "around"









            #html.Div(dcc.Graph(id='mate'),style={'width': '65%', 'display': 'inline-block'}),
            html.H5('Materiales y bodegas valorados',
                    style={'textAlign': 'left'}),

            html.Div(dcc.Graph(id='mate3'), style={
                     'width': '75%', 'display': 'inline-block'}),
            html.Div(dcc.Graph(id='bode3'), style={
                     'width': '25%', 'display': 'inline-block'}),
            html.Div(dcc.Graph(id='mate23'), style={
                     'width': '75%', 'display': 'inline-block'}),
            html.Div(dcc.Graph(id='bode23'), style={
                     'width': '25%', 'display': 'inline-block'}),


            html.H5('Centros de costos y contratistas valorados',
                    style={'textAlign': 'left'}),

            html.Div(dcc.Graph(id='centrocos3'), style={
                     'width': '100%', 'display': 'inline-block'}),
            html.Div(dcc.Graph(id='centrocos23'), style={
                     'width': '100%', 'display': 'inline-block'}),

            html.H5('Egresos de materiales autorizados por linea de tiempo ',
                    style={'textAlign': 'left'}),


            html.Div(dcc.Graph(id='movmat3'), style={
                     'width': '100%', 'display': 'inline-block'}),




            html.H5('Movimientos de materiales por gasto e inversión ',
                    style={'textAlign': 'left'}),


            html.Div(dcc.Graph(id='fini23'), style={
                     'width': '50%', 'display': 'inline-block'}),
            html.Div(dcc.Graph(id='fini3'), style={
                     'width': '50%', 'display': 'inline-block'}),


            # ANIMACIÓNXXXXXXXXXXXXXXXXXXXXX



            # html.Div(dcc.Graph(id='video',figure=px.scatter(dffc, x="CANTIDAD", y="BODEGA", animation_frame="FECHA", animation_group="AUTORIZADOR",size="VALOR_TOTAL",
            # color="CENTRO_DE_COSTO", hover_name="AUTORIZADOR",)),style={'width': '100%', 'display': 'inline-block'}),









        ]


# %% DASH error si no encuentra la pagina

    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


# PAGINA 3

# %% DASH DROPDOWN Análisis de transacciones valorizadasXXXXX

# grafico materiales
@app.callback(
    Output('mate3', 'figure'),
    Input('dropdownmat3', 'value'),
    Input('dropdowncc3', 'value'),
    Input('dropdownautor3', 'value'),
    Input('dropdowntipo3', 'value'),
    Input('dropdownmmi', 'value'),
    Input('dropdownmcp', 'value'),
    Input('dropdownprio', 'value'),
    Input('dropdownmas503', 'value'),
    Input('my-date-picker-range3', 'start_date'),
    Input('my-date-picker-range3', 'end_date'),
    Input('dropdowngrmas503', 'value'),
    Input('dropdownsonal3', 'value'),
    Input('dropdowntipogoi3', 'value'),


)
def update_graph(dropdownmat3, dropdowncc3, dropdownautor3, dropdowntipo3, dropdownmmi, dropdownmcp, dropdownprio, dropdownmas503, start_date, end_date, dropdowngrmas503, dropdownsonal3, dropdowntipogoi3):
    #dff = movbod.copy()
    #movibodmasxn['CANTIDAD'] = movibodmasxn['CANTIDAD'].astype(str)
   #movibodmasxn["CANTIDAD2"] = movibodmasxn["CANTIDAD"] + " " + movibodmasxn["UNIDAD"]
    # SUMA

    movbod2 = movbod
    movbod2[['FECHA_']] = movbod2[['FECHA']]

    dffq = movbod2. groupby(['Descripcion_cod', 'BODEGA', 'CENTRO_DE_COSTO', 'Tipopersonal', 'ENTREGA_O_RECIBE', 'AUTORIZADOR', 'TIPO_x', 'MMI',
                            'PRIORIZAR_COMPRA', 'CRITICO', 'Motivo', 'FECHA_', 'FECHA', 'Grupomas50', 'DESC_SDI']).VALOR_TOTAL.sum().sort_values(ascending=False)
    dffq = dffq.to_frame()
    dffq = dffq.reset_index(level='Descripcion_cod')
    dffq = dffq.reset_index(level='BODEGA')
    dffq = dffq.reset_index(level='CENTRO_DE_COSTO')
    dffq = dffq.reset_index(level='Tipopersonal')
    dffq = dffq.reset_index(level='ENTREGA_O_RECIBE')
    dffq = dffq.reset_index(level='AUTORIZADOR')
    dffq = dffq.reset_index(level='TIPO_x')
    dffq = dffq.reset_index(level='MMI')
    dffq = dffq.reset_index(level='PRIORIZAR_COMPRA')
    dffq = dffq.reset_index(level='CRITICO')
    dffq = dffq.reset_index(level='Motivo')
    dffq = dffq.reset_index(level='Grupomas50')
    dffq = dffq.reset_index(level='DESC_SDI')
    dffq = dffq.reset_index(level='FECHA_')
    #dffq = dffq.reset_index(level='VALOR_TOTAL')

    # material
    if not dropdownmat3 or 'NA' in dropdownmat3:
        dffq = dffq
    else:
        if dropdownmat3 != "NA":
            dffq = dffq[dffq['Descripcion_cod'].isin(dropdownmat3)]
    # cc
    if not dropdowncc3 or 'NA' in dropdowncc3:
        dffq = dffq
    else:
        if dropdowncc3 != "NA":
            dffq = dffq[dffq['CENTRO_DE_COSTO'].isin(dropdowncc3)]
    # personal
    if not dropdownsonal3 or 'NA' in dropdownsonal3:
        dffq = dffq
    else:
        if dropdownsonal3 != "NA":
            dffq = dffq[dffq['ENTREGA_O_RECIBE'].isin(dropdownsonal3)]
    # autorizados
    if not dropdownautor3 or 'NA' in dropdownautor3:
        dffq = dffq
    else:
        if dropdownautor3 != "NA":
            dffq = dffq[dffq['AUTORIZADOR'].isin(dropdownautor3)]
    # mmi
    if not dropdownmmi or 'NA' in dropdownmmi:
        dffq = dffq
    else:
        if dropdownmmi != "NA":
            dffq = dffq[dffq['MMI'].isin(dropdownmmi)]
    # priorizar
    if not dropdownmcp or 'NA' in dropdownmcp:
        dffq = dffq
    else:
        if dropdownmcp != "NA":
            dffq = dffq[dffq['PRIORIZAR_COMPRA'].isin(dropdownmcp)]
    # criticos
    if not dropdownprio or 'NA' in dropdownprio:
        dffq = dffq
    else:
        if dropdownprio != "NA":
            dffq = dffq[dffq['CRITICO'].isin(dropdownprio)]
            # motivo
    if not dropdownmas503 or 'NA' in dropdownmas503:
        dffq = dffq
    else:
        if dropdownmas503 != "NA":
            dffq = dffq[dffq['Motivo'].isin(dropdownmas503)]
    # TIPO PERSONAL
    if not dropdowntipo3 or 'NA' in dropdowntipo3:
        dffq = dffq
    else:
        if dropdowntipo3 != "NA":
            dffq = dffq[dffq['Tipopersonal'].isin(dropdowntipo3)]
    # FECHA
    if not start_date or 'NA' in start_date or not end_date or 'NA' in end_date:
        dffq = dffq
    else:
        if start_date != "NA":
            #dff = dff[dff['FECHA'].isin(start_date)]
            dffq = dffq.loc[start_date:end_date]
            # grupo 50%
    if not dropdowngrmas503 or 'NA' in dropdowngrmas503:
        dffq = dffq
    else:
        if dropdowngrmas503 != "NA":
            dffq = dffq[dffq['Grupomas50'].isin(dropdowngrmas503)]

            # GASTO O INVERSION
    if not dropdowntipogoi3 or 'NA' in dropdowntipogoi3:
        dffq = dffq
    else:
        if dropdowntipogoi3 != "NA":
            dffq = dffq[dffq['DESC_SDI'].isin(dropdowntipogoi3)]

    #dffxs = dffxs.to_frame()

    df_mask = dffq['TIPO_x'] == "EGRESO"
    egresosx2 = dffq[df_mask]

    egresosx2 = egresosx2.sort_values('VALOR_TOTAL', ascending=False)
    egresosx2 = egresosx2.head(25)
    figure222ww = px.pie(egresosx2, values='VALOR_TOTAL', names='Descripcion_cod',
                         title='Mayor valoración de materiales egresados')
    return figure222ww


# grafico materiales reingresos
@app.callback(
    Output('mate23', 'figure'),
    Input('dropdownmat3', 'value'),
    Input('dropdowncc3', 'value'),
    Input('dropdownautor3', 'value'),
    Input('dropdowntipo3', 'value'),
    Input('dropdownmmi', 'value'),
    Input('dropdownmcp', 'value'),
    Input('dropdownprio', 'value'),
    Input('dropdownmas503', 'value'),
    Input('my-date-picker-range3', 'start_date'),
    Input('my-date-picker-range3', 'end_date'),
    Input('dropdowngrmas503', 'value'),
    Input('dropdownsonal3', 'value'),
    Input('dropdowntipogoi3', 'value'),


)
def update_graph(dropdownmat3, dropdowncc3, dropdownautor3, dropdowntipo3, dropdownmmi, dropdownmcp, dropdownprio, dropdownmas503, start_date, end_date, dropdowngrmas503, dropdownsonal3, dropdowntipogoi3):
    #dff = movbod.copy()
    #movibodmasxn['CANTIDAD'] = movibodmasxn['CANTIDAD'].astype(str)
   #movibodmasxn["CANTIDAD2"] = movibodmasxn["CANTIDAD"] + " " + movibodmasxn["UNIDAD"]
    # SUMA

    movbod2 = movbod
    movbod2[['FECHA_']] = movbod2[['FECHA']]

    dffq = movbod2. groupby(['Descripcion_cod', 'BODEGA', 'CENTRO_DE_COSTO', 'Tipopersonal', 'ENTREGA_O_RECIBE', 'AUTORIZADOR', 'TIPO_x', 'MMI',
                            'PRIORIZAR_COMPRA', 'CRITICO', 'Motivo', 'FECHA_', 'FECHA', 'Grupomas50', 'DESC_SDI']).VALOR_TOTAL.sum().sort_values(ascending=False)
    dffq = dffq.to_frame()
    dffq = dffq.reset_index(level='Descripcion_cod')
    dffq = dffq.reset_index(level='BODEGA')
    dffq = dffq.reset_index(level='CENTRO_DE_COSTO')
    dffq = dffq.reset_index(level='Tipopersonal')
    dffq = dffq.reset_index(level='ENTREGA_O_RECIBE')
    dffq = dffq.reset_index(level='AUTORIZADOR')
    dffq = dffq.reset_index(level='TIPO_x')
    dffq = dffq.reset_index(level='MMI')
    dffq = dffq.reset_index(level='PRIORIZAR_COMPRA')
    dffq = dffq.reset_index(level='CRITICO')
    dffq = dffq.reset_index(level='Motivo')
    dffq = dffq.reset_index(level='FECHA_')
    dffq = dffq.reset_index(level='Grupomas50')
    dffq = dffq.reset_index(level='DESC_SDI')

    #dffq = dffq.reset_index(level='VALOR_TOTAL')

    # material
    if not dropdownmat3 or 'NA' in dropdownmat3:
        dffq = dffq
    else:
        if dropdownmat3 != "NA":
            dffq = dffq[dffq['Descripcion_cod'].isin(dropdownmat3)]
    # cc
    if not dropdowncc3 or 'NA' in dropdowncc3:
        dffq = dffq
    else:
        if dropdowncc3 != "NA":
            dffq = dffq[dffq['CENTRO_DE_COSTO'].isin(dropdowncc3)]
    # personal
    if not dropdownsonal3 or 'NA' in dropdownsonal3:
        dffq = dffq
    else:
        if dropdownsonal3 != "NA":
            dffq = dffq[dffq['ENTREGA_O_RECIBE'].isin(dropdownsonal3)]
    # autorizados
    if not dropdownautor3 or 'NA' in dropdownautor3:
        dffq = dffq
    else:
        if dropdownautor3 != "NA":
            dffq = dffq[dffq['AUTORIZADOR'].isin(dropdownautor3)]
    # mmi
    if not dropdownmmi or 'NA' in dropdownmmi:
        dffq = dffq
    else:
        if dropdownmmi != "NA":
            dffq = dffq[dffq['MMI'].isin(dropdownmmi)]
    # priorizar
    if not dropdownmcp or 'NA' in dropdownmcp:
        dffq = dffq
    else:
        if dropdownmcp != "NA":
            dffq = dffq[dffq['PRIORIZAR_COMPRA'].isin(dropdownmcp)]
    # criticos
    if not dropdownprio or 'NA' in dropdownprio:
        dffq = dffq
    else:
        if dropdownprio != "NA":
            dffq = dffq[dffq['CRITICO'].isin(dropdownprio)]
            # motivo
    if not dropdownmas503 or 'NA' in dropdownmas503:
        dffq = dffq
    else:
        if dropdownmas503 != "NA":
            dffq = dffq[dffq['Motivo'].isin(dropdownmas503)]
    # TIPO PERSONAL
    if not dropdowntipo3 or 'NA' in dropdowntipo3:
        dffq = dffq
    else:
        if dropdowntipo3 != "NA":
            dffq = dffq[dffq['Tipopersonal'].isin(dropdowntipo3)]
    # FECHA
    if not start_date or 'NA' in start_date or not end_date or 'NA' in end_date:
        dffq = dffq
    else:
        if start_date != "NA":
            #dff = dff[dff['FECHA'].isin(start_date)]
            dffq = dffq.loc[start_date:end_date]
            # grupo 50%
    if not dropdowngrmas503 or 'NA' in dropdowngrmas503:
        dffq = dffq
    else:
        if dropdowngrmas503 != "NA":
            dffq = dffq[dffq['Grupomas50'].isin(dropdowngrmas503)]

            # GASTO O INVERSION
    if not dropdowntipogoi3 or 'NA' in dropdowntipogoi3:
        dffq = dffq
    else:
        if dropdowntipogoi3 != "NA":
            dffq = dffq[dffq['DESC_SDI'].isin(dropdowntipogoi3)]

    #dffxs = dffxs.to_frame()

    df_mask = dffq['TIPO_x'] == "REINGRESO"
    reingresosqx = dffq[df_mask]

    reingresosqx = reingresosqx.sort_values('VALOR_TOTAL', ascending=False)
    reingresosqx = reingresosqx.head(25)
    figure222oq = px.pie(reingresosqx, values='VALOR_TOTAL', names='Descripcion_cod',
                         title='Mayor valoración de materiales ingresados')
    return figure222oq


# grafico bodegas
@app.callback(
    Output('bode3', 'figure'),
    Input('dropdownmat3', 'value'),
    Input('dropdowncc3', 'value'),
    Input('dropdownautor3', 'value'),
    Input('dropdowntipo3', 'value'),
    Input('dropdownmmi', 'value'),
    Input('dropdownmcp', 'value'),
    Input('dropdownprio', 'value'),
    Input('dropdownmas503', 'value'),
    Input('my-date-picker-range3', 'start_date'),
    Input('my-date-picker-range3', 'end_date'),
    Input('dropdowngrmas503', 'value'),
    Input('dropdownsonal3', 'value'),
    Input('dropdowntipogoi3', 'value'),


)
def update_graph(dropdownmat3, dropdowncc3, dropdownautor3, dropdowntipo3, dropdownmmi, dropdownmcp, dropdownprio, dropdownmas503, start_date, end_date, dropdowngrmas503, dropdownsonal3, dropdowntipogoi3):
    #dff = movbod.copy()
    #movibodmasxn['CANTIDAD'] = movibodmasxn['CANTIDAD'].astype(str)
   #movibodmasxn["CANTIDAD2"] = movibodmasxn["CANTIDAD"] + " " + movibodmasxn["UNIDAD"]
    # SUMA

    movbod2 = movbod
    movbod2[['FECHA_']] = movbod2[['FECHA']]

    dffq = movbod2. groupby(['Descripcion_cod', 'BODEGA', 'CENTRO_DE_COSTO', 'Tipopersonal', 'ENTREGA_O_RECIBE', 'AUTORIZADOR', 'TIPO_x', 'MMI',
                            'PRIORIZAR_COMPRA', 'CRITICO', 'Motivo', 'FECHA_', 'FECHA', 'Grupomas50', 'DESC_SDI']).VALOR_TOTAL.sum().sort_values(ascending=False)
    dffq = dffq.to_frame()
    dffq = dffq.reset_index(level='Descripcion_cod')
    dffq = dffq.reset_index(level='BODEGA')
    dffq = dffq.reset_index(level='CENTRO_DE_COSTO')
    dffq = dffq.reset_index(level='Tipopersonal')
    dffq = dffq.reset_index(level='ENTREGA_O_RECIBE')
    dffq = dffq.reset_index(level='AUTORIZADOR')
    dffq = dffq.reset_index(level='TIPO_x')
    dffq = dffq.reset_index(level='MMI')
    dffq = dffq.reset_index(level='PRIORIZAR_COMPRA')
    dffq = dffq.reset_index(level='CRITICO')
    dffq = dffq.reset_index(level='Motivo')
    dffq = dffq.reset_index(level='FECHA_')
    dffq = dffq.reset_index(level='Grupomas50')
    dffq = dffq.reset_index(level='DESC_SDI')

    #dffq = dffq.reset_index(level='VALOR_TOTAL')

    # material
    if not dropdownmat3 or 'NA' in dropdownmat3:
        dffq = dffq
    else:
        if dropdownmat3 != "NA":
            dffq = dffq[dffq['Descripcion_cod'].isin(dropdownmat3)]
    # cc
    if not dropdowncc3 or 'NA' in dropdowncc3:
        dffq = dffq
    else:
        if dropdowncc3 != "NA":
            dffq = dffq[dffq['CENTRO_DE_COSTO'].isin(dropdowncc3)]
    # personal
    if not dropdownsonal3 or 'NA' in dropdownsonal3:
        dffq = dffq
    else:
        if dropdownsonal3 != "NA":
            dffq = dffq[dffq['ENTREGA_O_RECIBE'].isin(dropdownsonal3)]
    # autorizados
    if not dropdownautor3 or 'NA' in dropdownautor3:
        dffq = dffq
    else:
        if dropdownautor3 != "NA":
            dffq = dffq[dffq['AUTORIZADOR'].isin(dropdownautor3)]
    # mmi
    if not dropdownmmi or 'NA' in dropdownmmi:
        dffq = dffq
    else:
        if dropdownmmi != "NA":
            dffq = dffq[dffq['MMI'].isin(dropdownmmi)]
    # priorizar
    if not dropdownmcp or 'NA' in dropdownmcp:
        dffq = dffq
    else:
        if dropdownmcp != "NA":
            dffq = dffq[dffq['PRIORIZAR_COMPRA'].isin(dropdownmcp)]
    # criticos
    if not dropdownprio or 'NA' in dropdownprio:
        dffq = dffq
    else:
        if dropdownprio != "NA":
            dffq = dffq[dffq['CRITICO'].isin(dropdownprio)]
            # motivo
    if not dropdownmas503 or 'NA' in dropdownmas503:
        dffq = dffq
    else:
        if dropdownmas503 != "NA":
            dffq = dffq[dffq['Motivo'].isin(dropdownmas503)]
    # TIPO PERSONAL
    if not dropdowntipo3 or 'NA' in dropdowntipo3:
        dffq = dffq
    else:
        if dropdowntipo3 != "NA":
            dffq = dffq[dffq['Tipopersonal'].isin(dropdowntipo3)]
    # FECHA
    if not start_date or 'NA' in start_date or not end_date or 'NA' in end_date:
        dffq = dffq
    else:
        if start_date != "NA":
            #dff = dff[dff['FECHA'].isin(start_date)]
            dffq = dffq.loc[start_date:end_date]
            # grupo 50%
    if not dropdowngrmas503 or 'NA' in dropdowngrmas503:
        dffq = dffq
    else:
        if dropdowngrmas503 != "NA":
            dffq = dffq[dffq['Grupomas50'].isin(dropdowngrmas503)]

            # GASTO O INVERSION
    if not dropdowntipogoi3 or 'NA' in dropdowntipogoi3:
        dffq = dffq
    else:
        if dropdowntipogoi3 != "NA":
            dffq = dffq[dffq['DESC_SDI'].isin(dropdowntipogoi3)]

    dffq = dffq. groupby(['BODEGA', 'TIPO_x']
                         ).VALOR_TOTAL.sum().sort_values(ascending=False)
    dffq = dffq.to_frame()
    dffq = dffq.reset_index(level='BODEGA')
    dffq = dffq.reset_index(level='TIPO_x')

    df_mask = dffq['TIPO_x'] == "EGRESO"
    egresosxx = dffq[df_mask]

    egresosxx = egresosxx.sort_values('VALOR_TOTAL', ascending=False)
    egresosxx = egresosxx.head(10)

    figure2223hh = px.bar(egresosxx, x="BODEGA", y="VALOR_TOTAL",
                          color="TIPO_x", title="Recursos económicos en egresos")
    return figure2223hh


# grafico bodegas
@app.callback(
    Output('bode23', 'figure'),
    Input('dropdownmat3', 'value'),
    Input('dropdowncc3', 'value'),
    Input('dropdownautor3', 'value'),
    Input('dropdowntipo3', 'value'),
    Input('dropdownmmi', 'value'),
    Input('dropdownmcp', 'value'),
    Input('dropdownprio', 'value'),
    Input('dropdownmas503', 'value'),
    Input('my-date-picker-range3', 'start_date'),
    Input('my-date-picker-range3', 'end_date'),
    Input('dropdowngrmas503', 'value'),
    Input('dropdownsonal3', 'value'),
    Input('dropdowntipogoi3', 'value'),


)
def update_graph(dropdownmat3, dropdowncc3, dropdownautor3, dropdowntipo3, dropdownmmi, dropdownmcp, dropdownprio, dropdownmas503, start_date, end_date, dropdowngrmas503, dropdownsonal3, dropdowntipogoi3):
    #dff = movbod.copy()
    #movibodmasxn['CANTIDAD'] = movibodmasxn['CANTIDAD'].astype(str)
   #movibodmasxn["CANTIDAD2"] = movibodmasxn["CANTIDAD"] + " " + movibodmasxn["UNIDAD"]
    # SUMA

    movbod2 = movbod
    movbod2[['FECHA_']] = movbod2[['FECHA']]

    dffq = movbod2. groupby(['Descripcion_cod', 'BODEGA', 'CENTRO_DE_COSTO', 'Tipopersonal', 'ENTREGA_O_RECIBE', 'AUTORIZADOR', 'TIPO_x', 'MMI',
                            'PRIORIZAR_COMPRA', 'CRITICO', 'Motivo', 'FECHA_', 'FECHA', 'Grupomas50', 'DESC_SDI']).VALOR_TOTAL.sum().sort_values(ascending=False)
    dffq = dffq.to_frame()
    dffq = dffq.reset_index(level='Descripcion_cod')
    dffq = dffq.reset_index(level='BODEGA')
    dffq = dffq.reset_index(level='CENTRO_DE_COSTO')
    dffq = dffq.reset_index(level='Tipopersonal')
    dffq = dffq.reset_index(level='ENTREGA_O_RECIBE')
    dffq = dffq.reset_index(level='AUTORIZADOR')
    dffq = dffq.reset_index(level='TIPO_x')
    dffq = dffq.reset_index(level='MMI')
    dffq = dffq.reset_index(level='PRIORIZAR_COMPRA')
    dffq = dffq.reset_index(level='CRITICO')
    dffq = dffq.reset_index(level='Motivo')
    dffq = dffq.reset_index(level='FECHA_')
    dffq = dffq.reset_index(level='Grupomas50')
    dffq = dffq.reset_index(level='DESC_SDI')

    #dffq = dffq.reset_index(level='VALOR_TOTAL')

    # material
    if not dropdownmat3 or 'NA' in dropdownmat3:
        dffq = dffq
    else:
        if dropdownmat3 != "NA":
            dffq = dffq[dffq['Descripcion_cod'].isin(dropdownmat3)]
    # cc
    if not dropdowncc3 or 'NA' in dropdowncc3:
        dffq = dffq
    else:
        if dropdowncc3 != "NA":
            dffq = dffq[dffq['CENTRO_DE_COSTO'].isin(dropdowncc3)]
    # personal
    if not dropdownsonal3 or 'NA' in dropdownsonal3:
        dffq = dffq
    else:
        if dropdownsonal3 != "NA":
            dffq = dffq[dffq['ENTREGA_O_RECIBE'].isin(dropdownsonal3)]
    # autorizados
    if not dropdownautor3 or 'NA' in dropdownautor3:
        dffq = dffq
    else:
        if dropdownautor3 != "NA":
            dffq = dffq[dffq['AUTORIZADOR'].isin(dropdownautor3)]
    # mmi
    if not dropdownmmi or 'NA' in dropdownmmi:
        dffq = dffq
    else:
        if dropdownmmi != "NA":
            dffq = dffq[dffq['MMI'].isin(dropdownmmi)]
    # priorizar
    if not dropdownmcp or 'NA' in dropdownmcp:
        dffq = dffq
    else:
        if dropdownmcp != "NA":
            dffq = dffq[dffq['PRIORIZAR_COMPRA'].isin(dropdownmcp)]
    # criticos
    if not dropdownprio or 'NA' in dropdownprio:
        dffq = dffq
    else:
        if dropdownprio != "NA":
            dffq = dffq[dffq['CRITICO'].isin(dropdownprio)]
            # motivo
    if not dropdownmas503 or 'NA' in dropdownmas503:
        dffq = dffq
    else:
        if dropdownmas503 != "NA":
            dffq = dffq[dffq['Motivo'].isin(dropdownmas503)]
    # TIPO PERSONAL
    if not dropdowntipo3 or 'NA' in dropdowntipo3:
        dffq = dffq
    else:
        if dropdowntipo3 != "NA":
            dffq = dffq[dffq['Tipopersonal'].isin(dropdowntipo3)]
    # FECHA
    if not start_date or 'NA' in start_date or not end_date or 'NA' in end_date:
        dffq = dffq
    else:
        if start_date != "NA":
            #dff = dff[dff['FECHA'].isin(start_date)]
            dffq = dffq.loc[start_date:end_date]
            # grupo 50%
    if not dropdowngrmas503 or 'NA' in dropdowngrmas503:
        dffq = dffq
    else:
        if dropdowngrmas503 != "NA":
            dffq = dffq[dffq['Grupomas50'].isin(dropdowngrmas503)]

            # GASTO O INVERSION
    if not dropdowntipogoi3 or 'NA' in dropdowntipogoi3:
        dffq = dffq
    else:
        if dropdowntipogoi3 != "NA":
            dffq = dffq[dffq['DESC_SDI'].isin(dropdowntipogoi3)]

    dffq = dffq. groupby(['BODEGA', 'TIPO_x']
                         ).VALOR_TOTAL.sum().sort_values(ascending=False)
    dffq = dffq.to_frame()
    dffq = dffq.reset_index(level='BODEGA')
    dffq = dffq.reset_index(level='TIPO_x')

    df_mask = dffq['TIPO_x'] == "REINGRESO"
    egresosxx = dffq[df_mask]

    egresosxx = egresosxx.sort_values('VALOR_TOTAL', ascending=False)
    egresosxx = egresosxx.head(10)

    figure2223hh = px.bar(egresosxx, x="BODEGA", y="VALOR_TOTAL",
                          color="TIPO_x", title="Recursos económicos en ingresos")
    return figure2223hh


@app.callback(
    Output('centrocos3', 'figure'),
    Input('dropdownmat3', 'value'),
    Input('dropdowncc3', 'value'),
    Input('dropdownautor3', 'value'),
    Input('dropdowntipo3', 'value'),
    Input('dropdownmmi', 'value'),
    Input('dropdownmcp', 'value'),
    Input('dropdownprio', 'value'),
    Input('dropdownmas503', 'value'),
    Input('my-date-picker-range3', 'start_date'),
    Input('my-date-picker-range3', 'end_date'),
    Input('dropdowngrmas503', 'value'),
    Input('dropdownsonal3', 'value'),
    Input('dropdowntipogoi3', 'value'),


)
def update_graph(dropdownmat3, dropdowncc3, dropdownautor3, dropdowntipo3, dropdownmmi, dropdownmcp, dropdownprio, dropdownmas503, start_date, end_date, dropdowngrmas503, dropdownsonal3, dropdowntipogoi3):
    #dff = movbod.copy()
    #movibodmasxn['CANTIDAD'] = movibodmasxn['CANTIDAD'].astype(str)
   #movibodmasxn["CANTIDAD2"] = movibodmasxn["CANTIDAD"] + " " + movibodmasxn["UNIDAD"]
    # SUMA

    movbod2 = movbod
    movbod2[['FECHA_']] = movbod2[['FECHA']]

    dffq = movbod2. groupby(['Descripcion_cod', 'BODEGA', 'CENTRO_DE_COSTO', 'Tipopersonal', 'ENTREGA_O_RECIBE', 'AUTORIZADOR', 'TIPO_x', 'MMI',
                            'PRIORIZAR_COMPRA', 'CRITICO', 'Motivo', 'FECHA_', 'FECHA', 'Grupomas50', 'DESC_SDI']).VALOR_TOTAL.sum().sort_values(ascending=False)
    dffq = dffq.to_frame()
    dffq = dffq.reset_index(level='Descripcion_cod')
    dffq = dffq.reset_index(level='BODEGA')
    dffq = dffq.reset_index(level='CENTRO_DE_COSTO')
    dffq = dffq.reset_index(level='Tipopersonal')
    dffq = dffq.reset_index(level='ENTREGA_O_RECIBE')
    dffq = dffq.reset_index(level='AUTORIZADOR')
    dffq = dffq.reset_index(level='TIPO_x')
    dffq = dffq.reset_index(level='MMI')
    dffq = dffq.reset_index(level='PRIORIZAR_COMPRA')
    dffq = dffq.reset_index(level='CRITICO')
    dffq = dffq.reset_index(level='Motivo')
    dffq = dffq.reset_index(level='FECHA_')
    dffq = dffq.reset_index(level='Grupomas50')
    dffq = dffq.reset_index(level='DESC_SDI')

    #dffq = dffq.reset_index(level='VALOR_TOTAL')

    # material
    if not dropdownmat3 or 'NA' in dropdownmat3:
        dffq = dffq
    else:
        if dropdownmat3 != "NA":
            dffq = dffq[dffq['Descripcion_cod'].isin(dropdownmat3)]
    # cc
    if not dropdowncc3 or 'NA' in dropdowncc3:
        dffq = dffq
    else:
        if dropdowncc3 != "NA":
            dffq = dffq[dffq['CENTRO_DE_COSTO'].isin(dropdowncc3)]
    # personal
    if not dropdownsonal3 or 'NA' in dropdownsonal3:
        dffq = dffq
    else:
        if dropdownsonal3 != "NA":
            dffq = dffq[dffq['ENTREGA_O_RECIBE'].isin(dropdownsonal3)]
    # autorizados
    if not dropdownautor3 or 'NA' in dropdownautor3:
        dffq = dffq
    else:
        if dropdownautor3 != "NA":
            dffq = dffq[dffq['AUTORIZADOR'].isin(dropdownautor3)]
    # mmi
    if not dropdownmmi or 'NA' in dropdownmmi:
        dffq = dffq
    else:
        if dropdownmmi != "NA":
            dffq = dffq[dffq['MMI'].isin(dropdownmmi)]
    # priorizar
    if not dropdownmcp or 'NA' in dropdownmcp:
        dffq = dffq
    else:
        if dropdownmcp != "NA":
            dffq = dffq[dffq['PRIORIZAR_COMPRA'].isin(dropdownmcp)]
    # criticos
    if not dropdownprio or 'NA' in dropdownprio:
        dffq = dffq
    else:
        if dropdownprio != "NA":
            dffq = dffq[dffq['CRITICO'].isin(dropdownprio)]
            # motivo
    if not dropdownmas503 or 'NA' in dropdownmas503:
        dffq = dffq
    else:
        if dropdownmas503 != "NA":
            dffq = dffq[dffq['Motivo'].isin(dropdownmas503)]
    # TIPO PERSONAL
    if not dropdowntipo3 or 'NA' in dropdowntipo3:
        dffq = dffq
    else:
        if dropdowntipo3 != "NA":
            dffq = dffq[dffq['Tipopersonal'].isin(dropdowntipo3)]
    # FECHA
    if not start_date or 'NA' in start_date or not end_date or 'NA' in end_date:
        dffq = dffq
    else:
        if start_date != "NA":
            #dff = dff[dff['FECHA'].isin(start_date)]
            dffq = dffq.loc[start_date:end_date]
            # grupo 50%
    if not dropdowngrmas503 or 'NA' in dropdowngrmas503:
        dffq = dffq
    else:
        if dropdowngrmas503 != "NA":
            dffq = dffq[dffq['Grupomas50'].isin(dropdowngrmas503)]

            # GASTO O INVERSION
    if not dropdowntipogoi3 or 'NA' in dropdowntipogoi3:
        dffq = dffq
    else:
        if dropdowntipogoi3 != "NA":
            dffq = dffq[dffq['DESC_SDI'].isin(dropdowntipogoi3)]

    dffxs = dffq. groupby(['CENTRO_DE_COSTO', 'ENTREGA_O_RECIBE', 'Descripcion_cod',
                          'TIPO_x']).VALOR_TOTAL.sum().sort_values(ascending=False)
    dffxs = dffxs.to_frame()
    dffxs = dffxs.reset_index(level='CENTRO_DE_COSTO')
    dffxs = dffxs.reset_index(level='ENTREGA_O_RECIBE')
    dffxs = dffxs.reset_index(level='Descripcion_cod')
    dffxs = dffxs.reset_index(level='TIPO_x')

    df_mask = dffxs['TIPO_x'] == "EGRESO"
    egresosxxx1 = dffxs[df_mask]

    egresosxxx1 = egresosxxx1.sort_values('VALOR_TOTAL', ascending=False)
    egresosxxx1 = egresosxxx1.head(40)

    figure2224oo = px.bar(egresosxxx1, x="VALOR_TOTAL", y="CENTRO_DE_COSTO", color="ENTREGA_O_RECIBE", pattern_shape="Descripcion_cod",
                          pattern_shape_sequence=[".", "x", "+"], title="Contratistas-Personal qué más valores egresan", orientation='h')

    return figure2224oo


# grafico centro de costo mas contratistas egresos
@app.callback(
    Output('centrocos23', 'figure'),
    Input('dropdownmat3', 'value'),
    Input('dropdowncc3', 'value'),
    Input('dropdownautor3', 'value'),
    Input('dropdowntipo3', 'value'),
    Input('dropdownmmi', 'value'),
    Input('dropdownmcp', 'value'),
    Input('dropdownprio', 'value'),
    Input('dropdownmas503', 'value'),
    Input('my-date-picker-range3', 'start_date'),
    Input('my-date-picker-range3', 'end_date'),
    Input('dropdowngrmas503', 'value'),
    Input('dropdownsonal3', 'value'),
    Input('dropdowntipogoi3', 'value'),


)
def update_graph(dropdownmat3, dropdowncc3, dropdownautor3, dropdowntipo3, dropdownmmi, dropdownmcp, dropdownprio, dropdownmas503, start_date, end_date, dropdowngrmas503, dropdownsonal3, dropdowntipogoi3):
    #dff = movbod.copy()
    #movibodmasxn['CANTIDAD'] = movibodmasxn['CANTIDAD'].astype(str)
   #movibodmasxn["CANTIDAD2"] = movibodmasxn["CANTIDAD"] + " " + movibodmasxn["UNIDAD"]
    # SUMA

    movbod2 = movbod
    movbod2[['FECHA_']] = movbod2[['FECHA']]

    dffq = movbod2. groupby(['Descripcion_cod', 'BODEGA', 'CENTRO_DE_COSTO', 'Tipopersonal', 'ENTREGA_O_RECIBE', 'AUTORIZADOR', 'TIPO_x', 'MMI',
                            'PRIORIZAR_COMPRA', 'CRITICO', 'Motivo', 'FECHA_', 'FECHA', 'Grupomas50', 'DESC_SDI']).VALOR_TOTAL.sum().sort_values(ascending=False)
    dffq = dffq.to_frame()
    dffq = dffq.reset_index(level='Descripcion_cod')
    dffq = dffq.reset_index(level='BODEGA')
    dffq = dffq.reset_index(level='CENTRO_DE_COSTO')
    dffq = dffq.reset_index(level='Tipopersonal')
    dffq = dffq.reset_index(level='ENTREGA_O_RECIBE')
    dffq = dffq.reset_index(level='AUTORIZADOR')
    dffq = dffq.reset_index(level='TIPO_x')
    dffq = dffq.reset_index(level='MMI')
    dffq = dffq.reset_index(level='PRIORIZAR_COMPRA')
    dffq = dffq.reset_index(level='CRITICO')
    dffq = dffq.reset_index(level='Motivo')
    dffq = dffq.reset_index(level='FECHA_')
    dffq = dffq.reset_index(level='Grupomas50')
    dffq = dffq.reset_index(level='DESC_SDI')

    #dffq = dffq.reset_index(level='VALOR_TOTAL')

    # material
    if not dropdownmat3 or 'NA' in dropdownmat3:
        dffq = dffq
    else:
        if dropdownmat3 != "NA":
            dffq = dffq[dffq['Descripcion_cod'].isin(dropdownmat3)]
    # cc
    if not dropdowncc3 or 'NA' in dropdowncc3:
        dffq = dffq
    else:
        if dropdowncc3 != "NA":
            dffq = dffq[dffq['CENTRO_DE_COSTO'].isin(dropdowncc3)]
    # personal
    if not dropdownsonal3 or 'NA' in dropdownsonal3:
        dffq = dffq
    else:
        if dropdownsonal3 != "NA":
            dffq = dffq[dffq['ENTREGA_O_RECIBE'].isin(dropdownsonal3)]
    # autorizados
    if not dropdownautor3 or 'NA' in dropdownautor3:
        dffq = dffq
    else:
        if dropdownautor3 != "NA":
            dffq = dffq[dffq['AUTORIZADOR'].isin(dropdownautor3)]
    # mmi
    if not dropdownmmi or 'NA' in dropdownmmi:
        dffq = dffq
    else:
        if dropdownmmi != "NA":
            dffq = dffq[dffq['MMI'].isin(dropdownmmi)]
    # priorizar
    if not dropdownmcp or 'NA' in dropdownmcp:
        dffq = dffq
    else:
        if dropdownmcp != "NA":
            dffq = dffq[dffq['PRIORIZAR_COMPRA'].isin(dropdownmcp)]
    # criticos
    if not dropdownprio or 'NA' in dropdownprio:
        dffq = dffq
    else:
        if dropdownprio != "NA":
            dffq = dffq[dffq['CRITICO'].isin(dropdownprio)]
            # motivo
    if not dropdownmas503 or 'NA' in dropdownmas503:
        dffq = dffq
    else:
        if dropdownmas503 != "NA":
            dffq = dffq[dffq['Motivo'].isin(dropdownmas503)]
    # TIPO PERSONAL
    if not dropdowntipo3 or 'NA' in dropdowntipo3:
        dffq = dffq
    else:
        if dropdowntipo3 != "NA":
            dffq = dffq[dffq['Tipopersonal'].isin(dropdowntipo3)]
    # FECHA
    if not start_date or 'NA' in start_date or not end_date or 'NA' in end_date:
        dffq = dffq
    else:
        if start_date != "NA":
            #dff = dff[dff['FECHA'].isin(start_date)]
            dffq = dffq.loc[start_date:end_date]
            # grupo 50%
    if not dropdowngrmas503 or 'NA' in dropdowngrmas503:
        dffq = dffq
    else:
        if dropdowngrmas503 != "NA":
            dffq = dffq[dffq['Grupomas50'].isin(dropdowngrmas503)]

            # GASTO O INVERSION
    if not dropdowntipogoi3 or 'NA' in dropdowntipogoi3:
        dffq = dffq
    else:
        if dropdowntipogoi3 != "NA":
            dffq = dffq[dffq['DESC_SDI'].isin(dropdowntipogoi3)]

    dffxs = dffq. groupby(['CENTRO_DE_COSTO', 'ENTREGA_O_RECIBE', 'Descripcion_cod',
                          'TIPO_x']).VALOR_TOTAL.sum().sort_values(ascending=False)
    dffxs = dffxs.to_frame()
    dffxs = dffxs.reset_index(level='CENTRO_DE_COSTO')
    dffxs = dffxs.reset_index(level='ENTREGA_O_RECIBE')
    dffxs = dffxs.reset_index(level='Descripcion_cod')
    dffxs = dffxs.reset_index(level='TIPO_x')

    df_mask = dffxs['TIPO_x'] == "REINGRESO"
    egresosxxx1 = dffxs[df_mask]

    egresosxxx1 = egresosxxx1.sort_values('VALOR_TOTAL', ascending=False)
    egresosxxx1 = egresosxxx1.head(40)

    figure2224oo = px.bar(egresosxxx1, x="VALOR_TOTAL", y="CENTRO_DE_COSTO", color="ENTREGA_O_RECIBE", pattern_shape="Descripcion_cod",
                          pattern_shape_sequence=[".", "x", "+"], title="Contratistas-Personal qué más valores ingresan", orientation='h')

    return figure2224oo


# AUTORIZADORES MAS DINERO
@app.callback(
    Output('auto3', 'figure'),
    Input('dropdownmat3', 'value'),
    Input('dropdowncc3', 'value'),
    Input('dropdownautor3', 'value'),
    Input('dropdowntipo3', 'value'),
    Input('dropdownmmi', 'value'),
    Input('dropdownmcp', 'value'),
    Input('dropdownprio', 'value'),
    Input('dropdownmas503', 'value'),
    Input('my-date-picker-range3', 'start_date'),
    Input('my-date-picker-range3', 'end_date'),
    Input('dropdowngrmas503', 'value'),
    Input('dropdownsonal3', 'value'),
    Input('dropdowntipogoi3', 'value'),


)
def update_graph(dropdownmat3, dropdowncc3, dropdownautor3, dropdowntipo3, dropdownmmi, dropdownmcp, dropdownprio, dropdownmas503, start_date, end_date, dropdowngrmas503, dropdownsonal3, dropdowntipogoi3):
    #dff = movbod.copy()
    #movibodmasxn['CANTIDAD'] = movibodmasxn['CANTIDAD'].astype(str)
   #movibodmasxn["CANTIDAD2"] = movibodmasxn["CANTIDAD"] + " " + movibodmasxn["UNIDAD"]
    # SUMA

    movbod2 = movbod
    movbod2[['FECHA_']] = movbod2[['FECHA']]

    dffq = movbod2. groupby(['Descripcion_cod', 'BODEGA', 'CENTRO_DE_COSTO', 'Tipopersonal', 'ENTREGA_O_RECIBE', 'AUTORIZADOR', 'TIPO_x', 'MMI',
                            'PRIORIZAR_COMPRA', 'CRITICO', 'Motivo', 'FECHA_', 'FECHA', 'Grupomas50', 'DESC_SDI']).VALOR_TOTAL.sum().sort_values(ascending=False)
    dffq = dffq.to_frame()
    dffq = dffq.reset_index(level='Descripcion_cod')
    dffq = dffq.reset_index(level='BODEGA')
    dffq = dffq.reset_index(level='CENTRO_DE_COSTO')
    dffq = dffq.reset_index(level='Tipopersonal')
    dffq = dffq.reset_index(level='ENTREGA_O_RECIBE')
    dffq = dffq.reset_index(level='AUTORIZADOR')
    dffq = dffq.reset_index(level='TIPO_x')
    dffq = dffq.reset_index(level='MMI')
    dffq = dffq.reset_index(level='PRIORIZAR_COMPRA')
    dffq = dffq.reset_index(level='CRITICO')
    dffq = dffq.reset_index(level='Motivo')
    dffq = dffq.reset_index(level='FECHA_')
    dffq = dffq.reset_index(level='Grupomas50')
    dffq = dffq.reset_index(level='DESC_SDI')

    #dffq = dffq.reset_index(level='VALOR_TOTAL')

    # material
    if not dropdownmat3 or 'NA' in dropdownmat3:
        dffq = dffq
    else:
        if dropdownmat3 != "NA":
            dffq = dffq[dffq['Descripcion_cod'].isin(dropdownmat3)]
    # cc
    if not dropdowncc3 or 'NA' in dropdowncc3:
        dffq = dffq
    else:
        if dropdowncc3 != "NA":
            dffq = dffq[dffq['CENTRO_DE_COSTO'].isin(dropdowncc3)]
    # personal
    if not dropdownsonal3 or 'NA' in dropdownsonal3:
        dffq = dffq
    else:
        if dropdownsonal3 != "NA":
            dffq = dffq[dffq['ENTREGA_O_RECIBE'].isin(dropdownsonal3)]
    # autorizados
    if not dropdownautor3 or 'NA' in dropdownautor3:
        dffq = dffq
    else:
        if dropdownautor3 != "NA":
            dffq = dffq[dffq['AUTORIZADOR'].isin(dropdownautor3)]
    # mmi
    if not dropdownmmi or 'NA' in dropdownmmi:
        dffq = dffq
    else:
        if dropdownmmi != "NA":
            dffq = dffq[dffq['MMI'].isin(dropdownmmi)]
    # priorizar
    if not dropdownmcp or 'NA' in dropdownmcp:
        dffq = dffq
    else:
        if dropdownmcp != "NA":
            dffq = dffq[dffq['PRIORIZAR_COMPRA'].isin(dropdownmcp)]
    # criticos
    if not dropdownprio or 'NA' in dropdownprio:
        dffq = dffq
    else:
        if dropdownprio != "NA":
            dffq = dffq[dffq['CRITICO'].isin(dropdownprio)]
            # motivo
    if not dropdownmas503 or 'NA' in dropdownmas503:
        dffq = dffq
    else:
        if dropdownmas503 != "NA":
            dffq = dffq[dffq['Motivo'].isin(dropdownmas503)]
    # TIPO PERSONAL
    if not dropdowntipo3 or 'NA' in dropdowntipo3:
        dffq = dffq
    else:
        if dropdowntipo3 != "NA":
            dffq = dffq[dffq['Tipopersonal'].isin(dropdowntipo3)]
    # FECHA
    if not start_date or 'NA' in start_date or not end_date or 'NA' in end_date:
        dffq = dffq
    else:
        if start_date != "NA":
            #dff = dff[dff['FECHA'].isin(start_date)]
            dffq = dffq.loc[start_date:end_date]
            # grupo 50%
    if not dropdowngrmas503 or 'NA' in dropdowngrmas503:
        dffq = dffq
    else:
        if dropdowngrmas503 != "NA":
            dffq = dffq[dffq['Grupomas50'].isin(dropdowngrmas503)]

            # GASTO O INVERSION
    if not dropdowntipogoi3 or 'NA' in dropdowntipogoi3:
        dffq = dffq
    else:
        if dropdowntipogoi3 != "NA":
            dffq = dffq[dffq['DESC_SDI'].isin(dropdowntipogoi3)]

    dffxss = dffq. groupby(['AUTORIZADOR', 'FECHA_', 'TIPO_x']
                           ).VALOR_TOTAL.sum().sort_values(ascending=False)
    # dffxs = dffxs.to_frame()AUTORIZADOR
    dffxss = dffxss.reset_index(level='AUTORIZADOR')
    dffxss = dffxss.reset_index(level='FECHA_')
    dffxss = dffxss.reset_index(level='TIPO_x')

    df_mask = dffxss['TIPO_x'] == "EGRESO"
    dffxss = dffxss[df_mask]

    dffxss = dffxss.sort_values('FECHA_', ascending=False)

    figure2224s = px.line(dffxss, x="FECHA_", y="VALOR_TOTAL", color='AUTORIZADOR',
                          title="Valorización de movimientos de egresos autorizados")

    return figure2224s


@app.callback(
    Output('auto23', 'figure'),
    Input('dropdownmat3', 'value'),
    Input('dropdowncc3', 'value'),
    Input('dropdownautor3', 'value'),
    Input('dropdowntipo3', 'value'),
    Input('dropdownmmi', 'value'),
    Input('dropdownmcp', 'value'),
    Input('dropdownprio', 'value'),
    Input('dropdownmas503', 'value'),
    Input('my-date-picker-range3', 'start_date'),
    Input('my-date-picker-range3', 'end_date'),
    Input('dropdowngrmas503', 'value'),
    Input('dropdownsonal3', 'value'),
    Input('dropdowntipogoi3', 'value'),


)
def update_graph(dropdownmat3, dropdowncc3, dropdownautor3, dropdowntipo3, dropdownmmi, dropdownmcp, dropdownprio, dropdownmas503, start_date, end_date, dropdowngrmas503, dropdownsonal3, dropdowntipogoi3):
    #dff = movbod.copy()
    #movibodmasxn['CANTIDAD'] = movibodmasxn['CANTIDAD'].astype(str)
   #movibodmasxn["CANTIDAD2"] = movibodmasxn["CANTIDAD"] + " " + movibodmasxn["UNIDAD"]
    # SUMA

    movbod2 = movbod
    movbod2[['FECHA_']] = movbod2[['FECHA']]

    dffq = movbod2. groupby(['Descripcion_cod', 'BODEGA', 'CENTRO_DE_COSTO', 'Tipopersonal', 'ENTREGA_O_RECIBE', 'AUTORIZADOR', 'TIPO_x', 'MMI',
                            'PRIORIZAR_COMPRA', 'CRITICO', 'Motivo', 'FECHA_', 'FECHA', 'Grupomas50', 'DESC_SDI']).VALOR_TOTAL.sum().sort_values(ascending=False)
    dffq = dffq.to_frame()
    dffq = dffq.reset_index(level='Descripcion_cod')
    dffq = dffq.reset_index(level='BODEGA')
    dffq = dffq.reset_index(level='CENTRO_DE_COSTO')
    dffq = dffq.reset_index(level='Tipopersonal')
    dffq = dffq.reset_index(level='ENTREGA_O_RECIBE')
    dffq = dffq.reset_index(level='AUTORIZADOR')
    dffq = dffq.reset_index(level='TIPO_x')
    dffq = dffq.reset_index(level='MMI')
    dffq = dffq.reset_index(level='PRIORIZAR_COMPRA')
    dffq = dffq.reset_index(level='CRITICO')
    dffq = dffq.reset_index(level='Motivo')
    dffq = dffq.reset_index(level='FECHA_')
    dffq = dffq.reset_index(level='Grupomas50')
    dffq = dffq.reset_index(level='DESC_SDI')

    #dffq = dffq.reset_index(level='VALOR_TOTAL')

    # material
    if not dropdownmat3 or 'NA' in dropdownmat3:
        dffq = dffq
    else:
        if dropdownmat3 != "NA":
            dffq = dffq[dffq['Descripcion_cod'].isin(dropdownmat3)]
    # cc
    if not dropdowncc3 or 'NA' in dropdowncc3:
        dffq = dffq
    else:
        if dropdowncc3 != "NA":
            dffq = dffq[dffq['CENTRO_DE_COSTO'].isin(dropdowncc3)]
    # personal
    if not dropdownsonal3 or 'NA' in dropdownsonal3:
        dffq = dffq
    else:
        if dropdownsonal3 != "NA":
            dffq = dffq[dffq['ENTREGA_O_RECIBE'].isin(dropdownsonal3)]
    # autorizados
    if not dropdownautor3 or 'NA' in dropdownautor3:
        dffq = dffq
    else:
        if dropdownautor3 != "NA":
            dffq = dffq[dffq['AUTORIZADOR'].isin(dropdownautor3)]
    # mmi
    if not dropdownmmi or 'NA' in dropdownmmi:
        dffq = dffq
    else:
        if dropdownmmi != "NA":
            dffq = dffq[dffq['MMI'].isin(dropdownmmi)]
    # priorizar
    if not dropdownmcp or 'NA' in dropdownmcp:
        dffq = dffq
    else:
        if dropdownmcp != "NA":
            dffq = dffq[dffq['PRIORIZAR_COMPRA'].isin(dropdownmcp)]
    # criticos
    if not dropdownprio or 'NA' in dropdownprio:
        dffq = dffq
    else:
        if dropdownprio != "NA":
            dffq = dffq[dffq['CRITICO'].isin(dropdownprio)]
            # motivo
    if not dropdownmas503 or 'NA' in dropdownmas503:
        dffq = dffq
    else:
        if dropdownmas503 != "NA":
            dffq = dffq[dffq['Motivo'].isin(dropdownmas503)]
    # TIPO PERSONAL
    if not dropdowntipo3 or 'NA' in dropdowntipo3:
        dffq = dffq
    else:
        if dropdowntipo3 != "NA":
            dffq = dffq[dffq['Tipopersonal'].isin(dropdowntipo3)]
    # FECHA
    if not start_date or 'NA' in start_date or not end_date or 'NA' in end_date:
        dffq = dffq
    else:
        if start_date != "NA":
            #dff = dff[dff['FECHA'].isin(start_date)]
            dffq = dffq.loc[start_date:end_date]
            # grupo 50%
    if not dropdowngrmas503 or 'NA' in dropdowngrmas503:
        dffq = dffq
    else:
        if dropdowngrmas503 != "NA":
            dffq = dffq[dffq['Grupomas50'].isin(dropdowngrmas503)]

            # GASTO O INVERSION
    if not dropdowntipogoi3 or 'NA' in dropdowntipogoi3:
        dffq = dffq
    else:
        if dropdowntipogoi3 != "NA":
            dffq = dffq[dffq['DESC_SDI'].isin(dropdowntipogoi3)]

    dffxss = dffq. groupby(['AUTORIZADOR', 'FECHA_', 'TIPO_x']
                           ).VALOR_TOTAL.sum().sort_values(ascending=False)
    # dffxs = dffxs.to_frame()AUTORIZADOR
    dffxss = dffxss.reset_index(level='AUTORIZADOR')
    dffxss = dffxss.reset_index(level='FECHA_')
    dffxss = dffxss.reset_index(level='TIPO_x')

    df_mask = dffxss['TIPO_x'] == "REINGRESO"
    dffxss = dffxss[df_mask]

    dffxss = dffxss.sort_values('FECHA_', ascending=False)

    figure2224s = px.line(dffxss, x="FECHA_", y="VALOR_TOTAL", color='AUTORIZADOR',
                          title="Valorización de movimientos de ingresos autorizados")

    return figure2224s


# AUTORIZADORES inversion o gasto y dinero en total
@app.callback(
    Output('fini3', 'figure'),
    Input('dropdownmat3', 'value'),
    Input('dropdowncc3', 'value'),
    Input('dropdownautor3', 'value'),
    Input('dropdowntipo3', 'value'),
    Input('dropdownmmi', 'value'),
    Input('dropdownmcp', 'value'),
    Input('dropdownprio', 'value'),
    Input('dropdownmas503', 'value'),
    Input('my-date-picker-range3', 'start_date'),
    Input('my-date-picker-range3', 'end_date'),
    Input('dropdowngrmas503', 'value'),
    Input('dropdownsonal3', 'value'),
    Input('dropdowntipogoi3', 'value'),


)
def update_graph(dropdownmat3, dropdowncc3, dropdownautor3, dropdowntipo3, dropdownmmi, dropdownmcp, dropdownprio, dropdownmas503, start_date, end_date, dropdowngrmas503, dropdownsonal3, dropdowntipogoi3):
    #dff = movbod.copy()
    #movibodmasxn['CANTIDAD'] = movibodmasxn['CANTIDAD'].astype(str)
   #movibodmasxn["CANTIDAD2"] = movibodmasxn["CANTIDAD"] + " " + movibodmasxn["UNIDAD"]
    # SUMA

    movbod2 = movbod
    movbod2[['FECHA_']] = movbod2[['FECHA']]

    dffq = movbod2. groupby(['Descripcion_cod', 'BODEGA', 'CENTRO_DE_COSTO', 'Tipopersonal', 'ENTREGA_O_RECIBE', 'AUTORIZADOR', 'TIPO_x', 'MMI',
                            'PRIORIZAR_COMPRA', 'CRITICO', 'Motivo', 'FECHA_', 'FECHA', 'Grupomas50', 'DESC_SDI']).VALOR_TOTAL.sum().sort_values(ascending=False)
    dffq = dffq.to_frame()
    dffq = dffq.reset_index(level='Descripcion_cod')
    dffq = dffq.reset_index(level='BODEGA')
    dffq = dffq.reset_index(level='CENTRO_DE_COSTO')
    dffq = dffq.reset_index(level='Tipopersonal')
    dffq = dffq.reset_index(level='ENTREGA_O_RECIBE')
    dffq = dffq.reset_index(level='AUTORIZADOR')
    dffq = dffq.reset_index(level='TIPO_x')
    dffq = dffq.reset_index(level='MMI')
    dffq = dffq.reset_index(level='PRIORIZAR_COMPRA')
    dffq = dffq.reset_index(level='CRITICO')
    dffq = dffq.reset_index(level='Motivo')
    dffq = dffq.reset_index(level='FECHA_')
    dffq = dffq.reset_index(level='Grupomas50')
    dffq = dffq.reset_index(level='DESC_SDI')

    #dffq = dffq.reset_index(level='VALOR_TOTAL')

    # material
    if not dropdownmat3 or 'NA' in dropdownmat3:
        dffq = dffq
    else:
        if dropdownmat3 != "NA":
            dffq = dffq[dffq['Descripcion_cod'].isin(dropdownmat3)]
    # cc
    if not dropdowncc3 or 'NA' in dropdowncc3:
        dffq = dffq
    else:
        if dropdowncc3 != "NA":
            dffq = dffq[dffq['CENTRO_DE_COSTO'].isin(dropdowncc3)]
    # personal
    if not dropdownsonal3 or 'NA' in dropdownsonal3:
        dffq = dffq
    else:
        if dropdownsonal3 != "NA":
            dffq = dffq[dffq['ENTREGA_O_RECIBE'].isin(dropdownsonal3)]
    # autorizados
    if not dropdownautor3 or 'NA' in dropdownautor3:
        dffq = dffq
    else:
        if dropdownautor3 != "NA":
            dffq = dffq[dffq['AUTORIZADOR'].isin(dropdownautor3)]
    # mmi
    if not dropdownmmi or 'NA' in dropdownmmi:
        dffq = dffq
    else:
        if dropdownmmi != "NA":
            dffq = dffq[dffq['MMI'].isin(dropdownmmi)]
    # priorizar
    if not dropdownmcp or 'NA' in dropdownmcp:
        dffq = dffq
    else:
        if dropdownmcp != "NA":
            dffq = dffq[dffq['PRIORIZAR_COMPRA'].isin(dropdownmcp)]
    # criticos
    if not dropdownprio or 'NA' in dropdownprio:
        dffq = dffq
    else:
        if dropdownprio != "NA":
            dffq = dffq[dffq['CRITICO'].isin(dropdownprio)]
            # motivo
    if not dropdownmas503 or 'NA' in dropdownmas503:
        dffq = dffq
    else:
        if dropdownmas503 != "NA":
            dffq = dffq[dffq['Motivo'].isin(dropdownmas503)]
    # TIPO PERSONAL
    if not dropdowntipo3 or 'NA' in dropdowntipo3:
        dffq = dffq
    else:
        if dropdowntipo3 != "NA":
            dffq = dffq[dffq['Tipopersonal'].isin(dropdowntipo3)]
    # FECHA
    if not start_date or 'NA' in start_date or not end_date or 'NA' in end_date:
        dffq = dffq
    else:
        if start_date != "NA":
            #dff = dff[dff['FECHA'].isin(start_date)]
            dffq = dffq.loc[start_date:end_date]
            # grupo 50%
    if not dropdowngrmas503 or 'NA' in dropdowngrmas503:
        dffq = dffq
    else:
        if dropdowngrmas503 != "NA":
            dffq = dffq[dffq['Grupomas50'].isin(dropdowngrmas503)]

            # GASTO O INVERSION
    if not dropdowntipogoi3 or 'NA' in dropdowntipogoi3:
        dffq = dffq
    else:
        if dropdowntipogoi3 != "NA":
            dffq = dffq[dffq['DESC_SDI'].isin(dropdowntipogoi3)]

    dffxss = dffq. groupby(['AUTORIZADOR', 'DESC_SDI', 'TIPO_x']
                           ).VALOR_TOTAL.sum().sort_values(ascending=False)
    #dffxs = dffxs.to_frame()
    dffxss = dffxss.reset_index(level='AUTORIZADOR')
    dffxss = dffxss.reset_index(level='DESC_SDI')
    dffxss = dffxss.reset_index(level='TIPO_x')

    df_mask = dffxss['TIPO_x'] == "EGRESO"
    dffxss = dffxss[df_mask]

    dffxss = dffxss.sort_values('VALOR_TOTAL', ascending=False)
    dffxss = dffxss.head(20)
    figure2224sf = px.sunburst(dffxss, path=[
                               'DESC_SDI', 'AUTORIZADOR'], values='VALOR_TOTAL', title="Recursos en egresos")

    return figure2224sf





# AUTORIZADORES inversion o gasto y dinero en total
@app.callback(
    Output('fini23', 'figure'),
    Input('dropdownmat3', 'value'),
    Input('dropdowncc3', 'value'),
    Input('dropdownautor3', 'value'),
    Input('dropdowntipo3', 'value'),
    Input('dropdownmmi', 'value'),
    Input('dropdownmcp', 'value'),
    Input('dropdownprio', 'value'),
    Input('dropdownmas503', 'value'),
    Input('my-date-picker-range3', 'start_date'),
    Input('my-date-picker-range3', 'end_date'),
    Input('dropdowngrmas503', 'value'),
    Input('dropdownsonal3', 'value'),
    Input('dropdowntipogoi3', 'value'),


)
def update_graph(dropdownmat3, dropdowncc3, dropdownautor3, dropdowntipo3, dropdownmmi, dropdownmcp, dropdownprio, dropdownmas503, start_date, end_date, dropdowngrmas503, dropdownsonal3, dropdowntipogoi3):
    #dff = movbod.copy()
    #movibodmasxn['CANTIDAD'] = movibodmasxn['CANTIDAD'].astype(str)
   #movibodmasxn["CANTIDAD2"] = movibodmasxn["CANTIDAD"] + " " + movibodmasxn["UNIDAD"]
    # SUMA

    movbod2 = movbod
    movbod2[['FECHA_']] = movbod2[['FECHA']]

    dffq = movbod2. groupby(['Descripcion_cod', 'BODEGA', 'CENTRO_DE_COSTO', 'Tipopersonal', 'ENTREGA_O_RECIBE', 'AUTORIZADOR', 'TIPO_x', 'MMI',
                            'PRIORIZAR_COMPRA', 'CRITICO', 'Motivo', 'FECHA_', 'FECHA', 'Grupomas50', 'DESC_SDI']).VALOR_TOTAL.sum().sort_values(ascending=False)
    dffq = dffq.to_frame()
    dffq = dffq.reset_index(level='Descripcion_cod')
    dffq = dffq.reset_index(level='BODEGA')
    dffq = dffq.reset_index(level='CENTRO_DE_COSTO')
    dffq = dffq.reset_index(level='Tipopersonal')
    dffq = dffq.reset_index(level='ENTREGA_O_RECIBE')
    dffq = dffq.reset_index(level='AUTORIZADOR')
    dffq = dffq.reset_index(level='TIPO_x')
    dffq = dffq.reset_index(level='MMI')
    dffq = dffq.reset_index(level='PRIORIZAR_COMPRA')
    dffq = dffq.reset_index(level='CRITICO')
    dffq = dffq.reset_index(level='Motivo')
    dffq = dffq.reset_index(level='FECHA_')
    dffq = dffq.reset_index(level='Grupomas50')
    dffq = dffq.reset_index(level='DESC_SDI')

    #dffq = dffq.reset_index(level='VALOR_TOTAL')

    # material
    if not dropdownmat3 or 'NA' in dropdownmat3:
        dffq = dffq
    else:
        if dropdownmat3 != "NA":
            dffq = dffq[dffq['Descripcion_cod'].isin(dropdownmat3)]
    # cc
    if not dropdowncc3 or 'NA' in dropdowncc3:
        dffq = dffq
    else:
        if dropdowncc3 != "NA":
            dffq = dffq[dffq['CENTRO_DE_COSTO'].isin(dropdowncc3)]
    # personal
    if not dropdownsonal3 or 'NA' in dropdownsonal3:
        dffq = dffq
    else:
        if dropdownsonal3 != "NA":
            dffq = dffq[dffq['ENTREGA_O_RECIBE'].isin(dropdownsonal3)]
    # autorizados
    if not dropdownautor3 or 'NA' in dropdownautor3:
        dffq = dffq
    else:
        if dropdownautor3 != "NA":
            dffq = dffq[dffq['AUTORIZADOR'].isin(dropdownautor3)]
    # mmi
    if not dropdownmmi or 'NA' in dropdownmmi:
        dffq = dffq
    else:
        if dropdownmmi != "NA":
            dffq = dffq[dffq['MMI'].isin(dropdownmmi)]
    # priorizar
    if not dropdownmcp or 'NA' in dropdownmcp:
        dffq = dffq
    else:
        if dropdownmcp != "NA":
            dffq = dffq[dffq['PRIORIZAR_COMPRA'].isin(dropdownmcp)]
    # criticos
    if not dropdownprio or 'NA' in dropdownprio:
        dffq = dffq
    else:
        if dropdownprio != "NA":
            dffq = dffq[dffq['CRITICO'].isin(dropdownprio)]
            # motivo
    if not dropdownmas503 or 'NA' in dropdownmas503:
        dffq = dffq
    else:
        if dropdownmas503 != "NA":
            dffq = dffq[dffq['Motivo'].isin(dropdownmas503)]
    # TIPO PERSONAL
    if not dropdowntipo3 or 'NA' in dropdowntipo3:
        dffq = dffq
    else:
        if dropdowntipo3 != "NA":
            dffq = dffq[dffq['Tipopersonal'].isin(dropdowntipo3)]
    # FECHA
    if not start_date or 'NA' in start_date or not end_date or 'NA' in end_date:
        dffq = dffq
    else:
        if start_date != "NA":
            #dff = dff[dff['FECHA'].isin(start_date)]
            dffq = dffq.loc[start_date:end_date]
            # grupo 50%
    if not dropdowngrmas503 or 'NA' in dropdowngrmas503:
        dffq = dffq
    else:
        if dropdowngrmas503 != "NA":
            dffq = dffq[dffq['Grupomas50'].isin(dropdowngrmas503)]

            # GASTO O INVERSION
    if not dropdowntipogoi3 or 'NA' in dropdowntipogoi3:
        dffq = dffq
    else:
        if dropdowntipogoi3 != "NA":
            dffq = dffq[dffq['DESC_SDI'].isin(dropdowntipogoi3)]

    dffxss = dffq. groupby(['AUTORIZADOR', 'DESC_SDI', 'TIPO_x']
                           ).VALOR_TOTAL.sum().sort_values(ascending=False)
    #dffxs = dffxs.to_frame()
    dffxss = dffxss.reset_index(level='AUTORIZADOR')
    dffxss = dffxss.reset_index(level='DESC_SDI')
    dffxss = dffxss.reset_index(level='TIPO_x')

    df_mask = dffxss['TIPO_x'] == "REINGRESO"
    dffxss = dffxss[df_mask]

    dffxss = dffxss.sort_values('VALOR_TOTAL', ascending=False)
    dffxss = dffxss.head(20)
    figure2224sf = px.sunburst(dffxss, path=[
                               'DESC_SDI', 'AUTORIZADOR'], values='VALOR_TOTAL', title="Recursos en ingresos")

    return figure2224sf


# mat en linea de tiempo egresos
@app.callback(
    Output('movmat3', 'figure'),
    Input('dropdownmat3', 'value'),
    Input('dropdowncc3', 'value'),
    Input('dropdownautor3', 'value'),
    Input('dropdowntipo3', 'value'),
    Input('dropdownmmi', 'value'),
    Input('dropdownmcp', 'value'),
    Input('dropdownprio', 'value'),
    Input('dropdownmas503', 'value'),
    Input('my-date-picker-range3', 'start_date'),
    Input('my-date-picker-range3', 'end_date'),
    Input('dropdowngrmas503', 'value'),
    Input('dropdownsonal3', 'value'),
    Input('dropdowntipogoi3', 'value'),


)
def update_graph(dropdownmat3, dropdowncc3, dropdownautor3, dropdowntipo3, dropdownmmi, dropdownmcp, dropdownprio, dropdownmas503, start_date, end_date, dropdowngrmas503, dropdownsonal3, dropdowntipogoi3):
    #dff = movbod.copy()
    #movibodmasxn['CANTIDAD'] = movibodmasxn['CANTIDAD'].astype(str)
   #movibodmasxn["CANTIDAD2"] = movibodmasxn["CANTIDAD"] + " " + movibodmasxn["UNIDAD"]
    # SUMA

    movbod2 = movbod
    movbod2[['FECHA_']] = movbod2[['FECHA']]

    dffq = movbod2. groupby(['Descripcion_cod', 'BODEGA', 'CENTRO_DE_COSTO', 'Tipopersonal', 'ENTREGA_O_RECIBE', 'AUTORIZADOR', 'TIPO_x', 'MMI',
                            'PRIORIZAR_COMPRA', 'CRITICO', 'Motivo', 'FECHA_', 'FECHA', 'Grupomas50', 'DESC_SDI']).VALOR_TOTAL.sum().sort_values(ascending=False)
    dffq = dffq.to_frame()
    dffq = dffq.reset_index(level='Descripcion_cod')
    dffq = dffq.reset_index(level='BODEGA')
    dffq = dffq.reset_index(level='CENTRO_DE_COSTO')
    dffq = dffq.reset_index(level='Tipopersonal')
    dffq = dffq.reset_index(level='ENTREGA_O_RECIBE')
    dffq = dffq.reset_index(level='AUTORIZADOR')
    dffq = dffq.reset_index(level='TIPO_x')
    dffq = dffq.reset_index(level='MMI')
    dffq = dffq.reset_index(level='PRIORIZAR_COMPRA')
    dffq = dffq.reset_index(level='CRITICO')
    dffq = dffq.reset_index(level='Motivo')
    dffq = dffq.reset_index(level='FECHA_')
    dffq = dffq.reset_index(level='Grupomas50')
    dffq = dffq.reset_index(level='DESC_SDI')

    #dffq = dffq.reset_index(level='VALOR_TOTAL')

    # material
    if not dropdownmat3 or 'NA' in dropdownmat3:
        dffq = dffq
    else:
        if dropdownmat3 != "NA":
            dffq = dffq[dffq['Descripcion_cod'].isin(dropdownmat3)]
    # cc
    if not dropdowncc3 or 'NA' in dropdowncc3:
        dffq = dffq
    else:
        if dropdowncc3 != "NA":
            dffq = dffq[dffq['CENTRO_DE_COSTO'].isin(dropdowncc3)]
    # personal
    if not dropdownsonal3 or 'NA' in dropdownsonal3:
        dffq = dffq
    else:
        if dropdownsonal3 != "NA":
            dffq = dffq[dffq['ENTREGA_O_RECIBE'].isin(dropdownsonal3)]
    # autorizados
    if not dropdownautor3 or 'NA' in dropdownautor3:
        dffq = dffq
    else:
        if dropdownautor3 != "NA":
            dffq = dffq[dffq['AUTORIZADOR'].isin(dropdownautor3)]
    # mmi
    if not dropdownmmi or 'NA' in dropdownmmi:
        dffq = dffq
    else:
        if dropdownmmi != "NA":
            dffq = dffq[dffq['MMI'].isin(dropdownmmi)]
    # priorizar
    if not dropdownmcp or 'NA' in dropdownmcp:
        dffq = dffq
    else:
        if dropdownmcp != "NA":
            dffq = dffq[dffq['PRIORIZAR_COMPRA'].isin(dropdownmcp)]
    # criticos
    if not dropdownprio or 'NA' in dropdownprio:
        dffq = dffq
    else:
        if dropdownprio != "NA":
            dffq = dffq[dffq['CRITICO'].isin(dropdownprio)]
            # motivo
    if not dropdownmas503 or 'NA' in dropdownmas503:
        dffq = dffq
    else:
        if dropdownmas503 != "NA":
            dffq = dffq[dffq['Motivo'].isin(dropdownmas503)]
    # TIPO PERSONAL
    if not dropdowntipo3 or 'NA' in dropdowntipo3:
        dffq = dffq
    else:
        if dropdowntipo3 != "NA":
            dffq = dffq[dffq['Tipopersonal'].isin(dropdowntipo3)]
    # FECHA
    if not start_date or 'NA' in start_date or not end_date or 'NA' in end_date:
        dffq = dffq
    else:
        if start_date != "NA":
            #dff = dff[dff['FECHA'].isin(start_date)]
            dffq = dffq.loc[start_date:end_date]
            # grupo 50%
    if not dropdowngrmas503 or 'NA' in dropdowngrmas503:
        dffq = dffq
    else:
        if dropdowngrmas503 != "NA":
            dffq = dffq[dffq['Grupomas50'].isin(dropdowngrmas503)]

            # GASTO O INVERSION
    if not dropdowntipogoi3 or 'NA' in dropdowntipogoi3:
        dffq = dffq
    else:
        if dropdowntipogoi3 != "NA":
            dffq = dffq[dffq['DESC_SDI'].isin(dropdowntipogoi3)]

    dffxss = dffq. groupby(['Descripcion_cod', 'FECHA_', 'TIPO_x']
                           ).VALOR_TOTAL.sum().sort_values(ascending=False)
    #dffxs = dffxs.to_frame()
    dffxss = dffxss.reset_index(level='Descripcion_cod')
    dffxss = dffxss.reset_index(level='FECHA_')
    dffxss = dffxss.reset_index(level='TIPO_x')
    df_mask = dffxss['TIPO_x'] == "EGRESO"
    egresos = dffxss[df_mask]

    egresos = egresos.head(80)
    egresos = egresos.sort_values('FECHA_', ascending=False)

    figure2224sww = px.line(egresos, x="FECHA_", y="VALOR_TOTAL",
                            color='Descripcion_cod', title="Movimientos de egresos")

    return figure2224sww


# mat en linea de tiempo
@app.callback(
    Output('movmat23', 'figure'),
    Input('dropdownmat3', 'value'),
    Input('dropdowncc3', 'value'),
    Input('dropdownautor3', 'value'),
    Input('dropdowntipo3', 'value'),
    Input('dropdownmmi', 'value'),
    Input('dropdownmcp', 'value'),
    Input('dropdownprio', 'value'),
    Input('dropdownmas503', 'value'),
    Input('my-date-picker-range3', 'start_date'),
    Input('my-date-picker-range3', 'end_date'),
    Input('dropdowngrmas503', 'value'),
    Input('dropdownsonal3', 'value'),
    Input('dropdowntipogoi3', 'value'),


)
def update_graph(dropdownmat3, dropdowncc3, dropdownautor3, dropdowntipo3, dropdownmmi, dropdownmcp, dropdownprio, dropdownmas503, start_date, end_date, dropdowngrmas503, dropdownsonal3, dropdowntipogoi3):
    #dff = movbod.copy()
    #movibodmasxn['CANTIDAD'] = movibodmasxn['CANTIDAD'].astype(str)
   #movibodmasxn["CANTIDAD2"] = movibodmasxn["CANTIDAD"] + " " + movibodmasxn["UNIDAD"]
    # SUMA

    movbod2 = movbod
    movbod2[['FECHA_']] = movbod2[['FECHA']]

    dffq = movbod2. groupby(['Descripcion_cod', 'BODEGA', 'CENTRO_DE_COSTO', 'Tipopersonal', 'ENTREGA_O_RECIBE', 'AUTORIZADOR', 'TIPO_x', 'MMI',
                            'PRIORIZAR_COMPRA', 'CRITICO', 'Motivo', 'FECHA_', 'FECHA', 'Grupomas50', 'DESC_SDI']).VALOR_TOTAL.sum().sort_values(ascending=False)
    dffq = dffq.to_frame()
    dffq = dffq.reset_index(level='Descripcion_cod')
    dffq = dffq.reset_index(level='BODEGA')
    dffq = dffq.reset_index(level='CENTRO_DE_COSTO')
    dffq = dffq.reset_index(level='Tipopersonal')
    dffq = dffq.reset_index(level='ENTREGA_O_RECIBE')
    dffq = dffq.reset_index(level='AUTORIZADOR')
    dffq = dffq.reset_index(level='TIPO_x')
    dffq = dffq.reset_index(level='MMI')
    dffq = dffq.reset_index(level='PRIORIZAR_COMPRA')
    dffq = dffq.reset_index(level='CRITICO')
    dffq = dffq.reset_index(level='Motivo')
    dffq = dffq.reset_index(level='FECHA_')
    dffq = dffq.reset_index(level='Grupomas50')
    dffq = dffq.reset_index(level='DESC_SDI')

    #dffq = dffq.reset_index(level='VALOR_TOTAL')

    # material
    if not dropdownmat3 or 'NA' in dropdownmat3:
        dffq = dffq
    else:
        if dropdownmat3 != "NA":
            dffq = dffq[dffq['Descripcion_cod'].isin(dropdownmat3)]
    # cc
    if not dropdowncc3 or 'NA' in dropdowncc3:
        dffq = dffq
    else:
        if dropdowncc3 != "NA":
            dffq = dffq[dffq['CENTRO_DE_COSTO'].isin(dropdowncc3)]
    # personal
    if not dropdownsonal3 or 'NA' in dropdownsonal3:
        dffq = dffq
    else:
        if dropdownsonal3 != "NA":
            dffq = dffq[dffq['ENTREGA_O_RECIBE'].isin(dropdownsonal3)]
    # autorizados
    if not dropdownautor3 or 'NA' in dropdownautor3:
        dffq = dffq
    else:
        if dropdownautor3 != "NA":
            dffq = dffq[dffq['AUTORIZADOR'].isin(dropdownautor3)]
    # mmi
    if not dropdownmmi or 'NA' in dropdownmmi:
        dffq = dffq
    else:
        if dropdownmmi != "NA":
            dffq = dffq[dffq['MMI'].isin(dropdownmmi)]
    # priorizar
    if not dropdownmcp or 'NA' in dropdownmcp:
        dffq = dffq
    else:
        if dropdownmcp != "NA":
            dffq = dffq[dffq['PRIORIZAR_COMPRA'].isin(dropdownmcp)]
    # criticos
    if not dropdownprio or 'NA' in dropdownprio:
        dffq = dffq
    else:
        if dropdownprio != "NA":
            dffq = dffq[dffq['CRITICO'].isin(dropdownprio)]
            # motivo
    if not dropdownmas503 or 'NA' in dropdownmas503:
        dffq = dffq
    else:
        if dropdownmas503 != "NA":
            dffq = dffq[dffq['Motivo'].isin(dropdownmas503)]
    # TIPO PERSONAL
    if not dropdowntipo3 or 'NA' in dropdowntipo3:
        dffq = dffq
    else:
        if dropdowntipo3 != "NA":
            dffq = dffq[dffq['Tipopersonal'].isin(dropdowntipo3)]
    # FECHA
    if not start_date or 'NA' in start_date or not end_date or 'NA' in end_date:
        dffq = dffq
    else:
        if start_date != "NA":
            #dff = dff[dff['FECHA'].isin(start_date)]
            dffq = dffq.loc[start_date:end_date]
            # grupo 50%
    if not dropdowngrmas503 or 'NA' in dropdowngrmas503:
        dffq = dffq
    else:
        if dropdowngrmas503 != "NA":
            dffq = dffq[dffq['Grupomas50'].isin(dropdowngrmas503)]

            # GASTO O INVERSION
    if not dropdowntipogoi3 or 'NA' in dropdowntipogoi3:
        dffq = dffq
    else:
        if dropdowntipogoi3 != "NA":
            dffq = dffq[dffq['DESC_SDI'].isin(dropdowntipogoi3)]

    dffxss = dffq. groupby(['Descripcion_cod', 'FECHA_', 'TIPO_x']
                           ).VALOR_TOTAL.sum().sort_values(ascending=False)
    #dffxs = dffxs.to_frame()
    dffxss = dffxss.reset_index(level='Descripcion_cod')
    dffxss = dffxss.reset_index(level='FECHA_')
    dffxss = dffxss.reset_index(level='TIPO_x')
    df_mask = dffxss['TIPO_x'] == "REINGRESO"
    egresos = dffxss[df_mask]

    egresos = egresos.head(80)
    egresos = egresos.sort_values('FECHA_', ascending=False)

    figure2224sww = px.line(egresos, x="FECHA_", y="VALOR_TOTAL",
                            color='Descripcion_cod', title="Movimientos de ingresos")

    return figure2224sww


@app.callback(
    Output('output-container-date-picker-range3', 'children'),
    Input('my-date-picker-range3', 'start_date'),
    Input('my-date-picker-range3', 'end_date'))
def update_output(start_date, end_date):
    string_prefix = 'Fecha analisis: '
    if start_date is not None:
        start_date_object = date.fromisoformat(start_date)
        start_date_string = start_date_object.strftime('%B %d, %Y')
        string_prefix = string_prefix + 'Fecha inicio: ' + start_date_string + ' | '
    if end_date is not None:
        end_date_object = date.fromisoformat(end_date)
        end_date_string = end_date_object.strftime('%B %d, %Y')
        string_prefix = string_prefix + 'Fecha fin: ' + end_date_string
    if len(string_prefix) == len('Fecha analisis: '):
        #mini = date.fromisoformat(mini)
        #mini = mini.strftime('%B %d, %Y')
        return f'Fecha analisis: Fecha inicio: {mini} | Fecha fin: {maxi}'

    else:
        return string_prefix


@app.callback(
    Output('store_o', 'data'),
    Input('dropdownmat3', 'value'),
    Input('dropdowncc3', 'value'),
    Input('dropdownautor3', 'value'),
    Input('dropdowntipo3', 'value'),
    Input('dropdownmmi', 'value'),
    Input('dropdownmcp', 'value'),
    Input('dropdownprio', 'value'),
    Input('dropdownmas503', 'value'),
    Input('my-date-picker-range3', 'start_date'),
    Input('my-date-picker-range3', 'end_date'),
    Input('dropdowngrmas503', 'value'),
    Input('dropdownsonal3', 'value'),
    Input('dropdowntipogoi3', 'value'),


)
def store_data(dropdownmat3, dropdowncc3, dropdownautor3, dropdowntipo3, dropdownmmi, dropdownmcp, dropdownprio, dropdownmas503, start_date, end_date, dropdowngrmas503, dropdownsonal3, dropdowntipogoi3):

    movbod2 = movbod
    movbod2[['FECHA_']] = movbod2[['FECHA']]

    ak = movbod2. groupby(['CODIGO', 'DOCUMENTO', 'CANTIDAD', 'Descripcion', 'Descripcion_cod', 'BODEGA', 'CENTRO_DE_COSTO', 'Tipopersonal', 'ENTREGA_O_RECIBE', 'AUTORIZADOR',
                          'TIPO_x', 'MMI', 'PRIORIZAR_COMPRA', 'CRITICO', 'Motivo', 'FECHA_', 'FECHA', 'Grupomas50', 'DESC_SDI']).VALOR_TOTAL.sum().sort_values(ascending=False)
    ak = ak.to_frame()
    ak = ak.reset_index(level='Descripcion_cod')
    ak = ak.reset_index(level='BODEGA')
    ak = ak.reset_index(level='CENTRO_DE_COSTO')
    ak = ak.reset_index(level='Tipopersonal')
    ak = ak.reset_index(level='ENTREGA_O_RECIBE')
    ak = ak.reset_index(level='AUTORIZADOR')
    ak = ak.reset_index(level='TIPO_x')
    ak = ak.reset_index(level='MMI')
    ak = ak.reset_index(level='PRIORIZAR_COMPRA')
    ak = ak.reset_index(level='CRITICO')
    ak = ak.reset_index(level='Motivo')
    ak = ak.reset_index(level='FECHA_')
    ak = ak.reset_index(level='Grupomas50')
    ak = ak.reset_index(level='DESC_SDI')
    ak = ak.reset_index(level='CANTIDAD')
    ak = ak.reset_index(level='DOCUMENTO')
    ak = ak.reset_index(level='Descripcion')
    ak = ak.reset_index(level='CODIGO')

    #dffq = dffq.reset_index(level='VALOR_TOTAL')

    # material
    if not dropdownmat3 or 'NA' in dropdownmat3:
        ak = ak
    else:
        if dropdownmat3 != "NA":
            ak = ak[ak['Descripcion_cod'].isin(dropdownmat3)]
    # cc
    if not dropdowncc3 or 'NA' in dropdowncc3:
        ak = ak
    else:
        if dropdowncc3 != "NA":
            ak = ak[ak['CENTRO_DE_COSTO'].isin(dropdowncc3)]
    # personal
    if not dropdownsonal3 or 'NA' in dropdownsonal3:
        ak = ak
    else:
        if dropdownsonal3 != "NA":
            ak = ak[ak['ENTREGA_O_RECIBE'].isin(dropdownsonal3)]
    # autorizados
    if not dropdownautor3 or 'NA' in dropdownautor3:
        ak = ak
    else:
        if dropdownautor3 != "NA":
            ak = ak[ak['AUTORIZADOR'].isin(dropdownautor3)]
    # mmi
    if not dropdownmmi or 'NA' in dropdownmmi:
        ak = ak
    else:
        if dropdownmmi != "NA":
            ak = ak[ak['MMI'].isin(dropdownmmi)]
    # priorizar
    if not dropdownmcp or 'NA' in dropdownmcp:
        ak = ak
    else:
        if dropdownmcp != "NA":
            ak = ak[ak['PRIORIZAR_COMPRA'].isin(dropdownmcp)]
    # criticos
    if not dropdownprio or 'NA' in dropdownprio:
        ak = ak
    else:
        if dropdownprio != "NA":
            ak = ak[ak['CRITICO'].isin(dropdownprio)]
            # motivo
    if not dropdownmas503 or 'NA' in dropdownmas503:
        ak = ak
    else:
        if dropdownmas503 != "NA":
            ak = ak[ak['Motivo'].isin(dropdownmas503)]
    # TIPO PERSONAL
    if not dropdowntipo3 or 'NA' in dropdowntipo3:
        ak = ak
    else:
        if dropdowntipo3 != "NA":
            ak = ak[ak['Tipopersonal'].isin(dropdowntipo3)]
    # FECHA
    if not start_date or 'NA' in start_date or not end_date or 'NA' in end_date:
        ak = ak
    else:
        if start_date != "NA":
            #dff = dff[dff['FECHA'].isin(start_date)]
            ak = ak.loc[start_date:end_date]
            # grupo 50%
    if not dropdowngrmas503 or 'NA' in dropdowngrmas503:
        ak = ak
    else:
        if dropdowngrmas503 != "NA":
            ak = ak[ak['Grupomas50'].isin(dropdowngrmas503)]

            # GASTO O INVERSION
    if not dropdowntipogoi3 or 'NA' in dropdowntipogoi3:
        ak = ak
    else:
        if dropdowntipogoi3 != "NA":
            ak = ak[ak['DESC_SDI'].isin(dropdowntipogoi3)]

    ak = ak.sort_values('CANTIDAD', ascending=False)

    ak['FECHA_'] = ak['FECHA_'].apply(lambda a: pd.to_datetime(a).date())

    return ak.to_json(date_format='iso', orient='split')
    # return print (ak)


@app.callback(
    Output("download-dataframe-xls_o", "data"),
    Input("btn_xls_o", "n_clicks"),
    State('store_o', 'data'),




    prevent_initial_call=False,
)
def func(n_clicks, jsonified_cleaned_data):
    if n_clicks > 0:
        movbod2 = pd.read_json(jsonified_cleaned_data, orient='split')

        ak = movbod2. groupby(['CODIGO', 'DOCUMENTO', 'CANTIDAD', 'Descripcion', 'Descripcion_cod', 'BODEGA', 'CENTRO_DE_COSTO', 'Tipopersonal', 'ENTREGA_O_RECIBE',
                              'AUTORIZADOR', 'TIPO_x', 'MMI', 'PRIORIZAR_COMPRA', 'CRITICO', 'Motivo', 'FECHA_', 'Grupomas50', 'DESC_SDI']).VALOR_TOTAL.sum().sort_values(ascending=False)
        ak = ak.to_frame()
        ak = ak.reset_index(level='Descripcion_cod')
        ak = ak.reset_index(level='Grupomas50')
        ak = ak.reset_index(level='MMI')
        ak = ak.reset_index(level='PRIORIZAR_COMPRA')
        ak = ak.reset_index(level='CRITICO')
        ak = ak.reset_index(level='Motivo')
        ak = ak.reset_index(level='CENTRO_DE_COSTO')
        ak = ak.reset_index(level='Tipopersonal')
        ak = ak.reset_index(level='ENTREGA_O_RECIBE')
        ak = ak.reset_index(level='AUTORIZADOR')
        ak = ak.reset_index(level='FECHA_')
        ak = ak.reset_index(level='DESC_SDI')
        ak = ak.reset_index(level='BODEGA')
        ak = ak.reset_index(level='CANTIDAD')
        ak = ak.reset_index(level='TIPO_x')
        ak = ak.reset_index(level='DOCUMENTO')
        ak = ak.reset_index(level='Descripcion')
        ak = ak.reset_index(level='CODIGO')
        ak = ak.sort_values('VALOR_TOTAL', ascending=False)

        #dff = dff[dff['Grupomas50'].isin(dropdowngrmas50)]
        #dff3['FECHA'] = dff3['FECHA'].apply(lambda a: pd.to_datetime(a).date())
        ak = ak.drop(['Descripcion_cod'], axis=1)
        
        
        return dcc.send_data_frame(ak.to_excel, "Movimientos_bodegas_valorizadasDPCE.xlsx", sheet_name="DPCE", index = False)


# %% DASH DROPDOWN ANALISIS DE TRANSACCIONES este si

# PAGINA 4

# grafico materiales
@app.callback(
    Output('mate', 'figure'),
    Input('dropdownmat', 'value'),
    Input('dropdowncc', 'value'),
    Input('dropdownautor', 'value'),
    Input('dropdowntipo', 'value'),
    Input('dropdownmmi', 'value'),
    Input('dropdownmcp', 'value'),
    Input('dropdownprio', 'value'),
    Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'),
    Input('dropdownsonal', 'value'),
    Input('dropdowntipogoi', 'value'),
    Input('dropdownboder', 'value'),
    


)
def update_graph(dropdownmat, dropdowncc, dropdownautor, dropdowntipo, dropdownmmi, dropdownmcp, dropdownprio, start_date, end_date,  dropdownsonal, dropdowntipogoi, dropdownboder):
    #dff = movbod.copy()
    #movibodmasxn['CANTIDAD'] = movibodmasxn['CANTIDAD'].astype(str)
   #movibodmasxn["CANTIDAD2"] = movibodmasxn["CANTIDAD"] + " " + movibodmasxn["UNIDAD"]
    # SUMA
    dff = movbod. groupby(['Descripcion_cod', 'BODEGA', 'CENTRO_DE_COSTO', 'Tipopersonal', 'ENTREGA_O_RECIBE', 'AUTORIZADOR', 'TIPO_x',
                          'MMI', 'PRIORIZAR_COMPRA', 'CRITICO', 'Motivo', 'FECHA', 'Grupomas50', 'DESC_SDI']).CANTIDAD.sum().sort_values(ascending=False)
    dff = dff.to_frame()
    dff = dff.reset_index(level='Descripcion_cod')
    dff = dff.reset_index(level='BODEGA')
    dff = dff.reset_index(level='CENTRO_DE_COSTO')
    dff = dff.reset_index(level='Tipopersonal')
    dff = dff.reset_index(level='ENTREGA_O_RECIBE')
    dff = dff.reset_index(level='AUTORIZADOR')
    dff = dff.reset_index(level='TIPO_x')
    dff = dff.reset_index(level='MMI')
    dff = dff.reset_index(level='PRIORIZAR_COMPRA')
    dff = dff.reset_index(level='CRITICO')
    dff = dff.reset_index(level='Motivo')
    dff = dff.reset_index(level='Grupomas50')
    dff = dff.reset_index(level='DESC_SDI')

    # material
    if not dropdownmat or 'NA' in dropdownmat:
        dff = dff
    else:
        if dropdownmat != "NA":
            dff = dff[dff['Descripcion_cod'].isin(dropdownmat)]
    # cc
    if not dropdowncc or 'NA' in dropdowncc:
        dff = dff
    else:
        if dropdowncc != "NA":
            dff = dff[dff['CENTRO_DE_COSTO'].isin(dropdowncc)]
    # personal
    if not dropdownsonal or 'NA' in dropdownsonal:
        dff = dff
    else:
        if dropdownsonal != "NA":
            dff = dff[dff['ENTREGA_O_RECIBE'].isin(dropdownsonal)]
    # autorizados
    if not dropdownautor or 'NA' in dropdownautor:
        dff = dff
    else:
        if dropdownautor != "NA":
            dff = dff[dff['AUTORIZADOR'].isin(dropdownautor)]
    # mmi
    if not dropdownmmi or 'NA' in dropdownmmi:
        dff = dff
    else:
        if dropdownmmi != "NA":
            dff = dff[dff['MMI'].isin(dropdownmmi)]
    # priorizar
    if not dropdownmcp or 'NA' in dropdownmcp:
        dff = dff
    else:
        if dropdownmcp != "NA":
            dff = dff[dff['PRIORIZAR_COMPRA'].isin(dropdownmcp)]
    # criticos
    if not dropdownprio or 'NA' in dropdownprio:
        dff = dff
    else:
        if dropdownprio != "NA":
            dff = dff[dff['CRITICO'].isin(dropdownprio)]

    # TIPO PERSONAL
    if not dropdowntipo or 'NA' in dropdowntipo:
        dff = dff
    else:
        if dropdowntipo != "NA":
            dff = dff[dff['Tipopersonal'].isin(dropdowntipo)]
    # FECHA
    if not start_date or 'NA' in start_date or not end_date or 'NA' in end_date:
        dff = dff
    else:
        if start_date != "NA":
            #dff = dff[dff['FECHA'].isin(start_date)]
            dff = dff.loc[start_date:end_date]


            # GASTO O INVERSION
    if not dropdowntipogoi or 'NA' in dropdowntipogoi:
        dff = dff
    else:
        if dropdowntipogoi != "NA":
            dff = dff[dff['DESC_SDI'].isin(dropdowntipogoi)]
            
            # BODEGA
    if not dropdownboder or 'NA' in dropdownboder:
        dff = dff
    else:
        if dropdownboder != "NA":
            dff = dff[dff['BODEGA'].isin(dropdownboder)]
            
             
            
            
            
            
            
            

    #dffxs = dffxs.to_frame()

    df_mask = dff['TIPO_x'] == "EGRESO"
    egresosx = dff[df_mask]

    egresosx = egresosx.sort_values('CANTIDAD', ascending=False)
    egresosx = egresosx.head(25)
    figure222 = px.pie(egresosx, values='CANTIDAD',
                       names='Descripcion_cod', title='Materiales mas egresados')
    return figure222


# grafico bodegas
@app.callback(
    Output('bode', 'figure'),
    Input('dropdownmat', 'value'),
    Input('dropdowncc', 'value'),
    Input('dropdownautor', 'value'),
    Input('dropdowntipo', 'value'),
    Input('dropdownmmi', 'value'),
    Input('dropdownmcp', 'value'),
    Input('dropdownprio', 'value'),
    Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'),
    Input('dropdownsonal', 'value'),
    Input('dropdowntipogoi', 'value'),
    Input('dropdownboder', 'value'),
    
)
def update_graph(dropdownmat, dropdowncc, dropdownautor, dropdowntipo, dropdownmmi, dropdownmcp, dropdownprio,  start_date, end_date, dropdownsonal, dropdowntipogoi, dropdownboder):
    #dff = movbod.copy()
    #movibodmasxn['CANTIDAD'] = movibodmasxn['CANTIDAD'].astype(str)
   #movibodmasxn["CANTIDAD2"] = movibodmasxn["CANTIDAD"] + " " + movibodmasxn["UNIDAD"]
    # SUMA
    dff = movbod. groupby(['Descripcion_cod', 'BODEGA', 'CENTRO_DE_COSTO', 'Tipopersonal', 'ENTREGA_O_RECIBE', 'AUTORIZADOR', 'TIPO_x',
                          'MMI', 'PRIORIZAR_COMPRA', 'CRITICO', 'Motivo', 'FECHA', 'Grupomas50', 'DESC_SDI']).CANTIDAD.sum().sort_values(ascending=False)
    dff = dff.to_frame()
    dff = dff.reset_index(level='Descripcion_cod')
    dff = dff.reset_index(level='BODEGA')
    dff = dff.reset_index(level='CENTRO_DE_COSTO')
    dff = dff.reset_index(level='Tipopersonal')
    dff = dff.reset_index(level='ENTREGA_O_RECIBE')
    dff = dff.reset_index(level='AUTORIZADOR')
    dff = dff.reset_index(level='TIPO_x')
    dff = dff.reset_index(level='MMI')
    dff = dff.reset_index(level='PRIORIZAR_COMPRA')
    dff = dff.reset_index(level='CRITICO')
    dff = dff.reset_index(level='Motivo')
    dff = dff.reset_index(level='Grupomas50')
    dff = dff.reset_index(level='DESC_SDI')

    # material
    if not dropdownmat or 'NA' in dropdownmat:
        dff = dff
    else:
        if dropdownmat != "NA":
            dff = dff[dff['Descripcion_cod'].isin(dropdownmat)]
    # cc
    if not dropdowncc or 'NA' in dropdowncc:
        dff = dff
    else:
        if dropdowncc != "NA":
            dff = dff[dff['CENTRO_DE_COSTO'].isin(dropdowncc)]
    # personal
    if not dropdownsonal or 'NA' in dropdownsonal:
        dff = dff
    else:
        if dropdownsonal != "NA":
            dff = dff[dff['ENTREGA_O_RECIBE'].isin(dropdownsonal)]
    # autorizados
    if not dropdownautor or 'NA' in dropdownautor:
        dff = dff
    else:
        if dropdownautor != "NA":
            dff = dff[dff['AUTORIZADOR'].isin(dropdownautor)]
    # mmi
    if not dropdownmmi or 'NA' in dropdownmmi:
        dff = dff
    else:
        if dropdownmmi != "NA":
            dff = dff[dff['MMI'].isin(dropdownmmi)]
    # priorizar
    if not dropdownmcp or 'NA' in dropdownmcp:
        dff = dff
    else:
        if dropdownmcp != "NA":
            dff = dff[dff['PRIORIZAR_COMPRA'].isin(dropdownmcp)]
    # criticos
    if not dropdownprio or 'NA' in dropdownprio:
        dff = dff
    else:
        if dropdownprio != "NA":
            dff = dff[dff['CRITICO'].isin(dropdownprio)]

    # TIPO PERSONAL
    if not dropdowntipo or 'NA' in dropdowntipo:
        dff = dff
    else:
        if dropdowntipo != "NA":
            dff = dff[dff['Tipopersonal'].isin(dropdowntipo)]
    # FECHA
    if not start_date or 'NA' in start_date or not end_date or 'NA' in end_date:
        dff = dff
    else:
        if start_date != "NA":
            #dff = dff[dff['FECHA'].isin(start_date)]
            dff = dff.loc[start_date:end_date]


    # GASTO O INVERSION
    if not dropdowntipogoi or 'NA' in dropdowntipogoi:
        dff = dff
    else:
        if dropdowntipogoi != "NA":
            dff = dff[dff['DESC_SDI'].isin(dropdowntipogoi)]
 
            
    # BODEGAS
    if not dropdownboder or 'NA' in dropdownboder:
        dff = dff
    else:
        if dropdownboder != "NA":
            dff = dff[dff['BODEGA'].isin(dropdownboder)]
 
            
            
            
            

    dffx = dff. groupby(['BODEGA', 'TIPO_x']
                        ).CANTIDAD.sum().sort_values(ascending=False)
    dffx = dffx.to_frame()
    dffx = dffx.reset_index(level='BODEGA')
    dffx = dffx.reset_index(level='TIPO_x')

    df_mask = dffx['TIPO_x'] == "EGRESO"
    egresosxx = dffx[df_mask]

    egresosxx = egresosxx.sort_values('CANTIDAD', ascending=False)
    egresosxx = egresosxx.head(10)

    figure2223 = px.bar(egresosxx, x="BODEGA", y="CANTIDAD",
                        color="TIPO_x", title="Bodegas con mas egresos")
    return figure2223



# grafico centro de costo mas contratistas reingresos
@app.callback(
    Output('centrocos', 'figure'),
    Input('dropdownmat', 'value'),
    Input('dropdowncc', 'value'),
    Input('dropdownautor', 'value'),
    Input('dropdowntipo', 'value'),
    Input('dropdownmmi', 'value'),
    Input('dropdownmcp', 'value'),
    Input('dropdownprio', 'value'),
    Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'),
    Input('dropdownsonal', 'value'),
    Input('dropdowntipogoi', 'value'),
    Input('dropdownboder', 'value'),
    
)
def update_graph(dropdownmat, dropdowncc, dropdownautor, dropdowntipo, dropdownmmi, dropdownmcp, dropdownprio,  start_date, end_date, dropdownsonal, dropdowntipogoi, dropdownboder):
    #dff = movbod.copy()
    #movibodmasxn['CANTIDAD'] = movibodmasxn['CANTIDAD'].astype(str)
   #movibodmasxn["CANTIDAD2"] = movibodmasxn["CANTIDAD"] + " " + movibodmasxn["UNIDAD"]
    # SUMA
    dff = movbod. groupby(['Descripcion_cod', 'BODEGA', 'CENTRO_DE_COSTO', 'Tipopersonal', 'ENTREGA_O_RECIBE', 'AUTORIZADOR', 'TIPO_x',
                          'MMI', 'PRIORIZAR_COMPRA', 'CRITICO', 'Motivo', 'FECHA', 'Grupomas50', 'DESC_SDI']).CANTIDAD.sum().sort_values(ascending=False)
    dff = dff.to_frame()
    dff = dff.reset_index(level='Descripcion_cod')
    dff = dff.reset_index(level='BODEGA')
    dff = dff.reset_index(level='CENTRO_DE_COSTO')
    dff = dff.reset_index(level='Tipopersonal')
    dff = dff.reset_index(level='ENTREGA_O_RECIBE')
    dff = dff.reset_index(level='AUTORIZADOR')
    dff = dff.reset_index(level='TIPO_x')
    dff = dff.reset_index(level='MMI')
    dff = dff.reset_index(level='PRIORIZAR_COMPRA')
    dff = dff.reset_index(level='CRITICO')
    dff = dff.reset_index(level='Motivo')
    dff = dff.reset_index(level='Grupomas50')
    dff = dff.reset_index(level='DESC_SDI')

    # material
    if not dropdownmat or 'NA' in dropdownmat:
        dff = dff
    else:
        if dropdownmat != "NA":
            dff = dff[dff['Descripcion_cod'].isin(dropdownmat)]
    # cc
    if not dropdowncc or 'NA' in dropdowncc:
        dff = dff
    else:
        if dropdowncc != "NA":
            dff = dff[dff['CENTRO_DE_COSTO'].isin(dropdowncc)]
    # personal
    if not dropdownsonal or 'NA' in dropdownsonal:
        dff = dff
    else:
        if dropdownsonal != "NA":
            dff = dff[dff['ENTREGA_O_RECIBE'].isin(dropdownsonal)]
    # autorizados
    if not dropdownautor or 'NA' in dropdownautor:
        dff = dff
    else:
        if dropdownautor != "NA":
            dff = dff[dff['AUTORIZADOR'].isin(dropdownautor)]
    # mmi
    if not dropdownmmi or 'NA' in dropdownmmi:
        dff = dff
    else:
        if dropdownmmi != "NA":
            dff = dff[dff['MMI'].isin(dropdownmmi)]
    # priorizar
    if not dropdownmcp or 'NA' in dropdownmcp:
        dff = dff
    else:
        if dropdownmcp != "NA":
            dff = dff[dff['PRIORIZAR_COMPRA'].isin(dropdownmcp)]
    # criticos
    if not dropdownprio or 'NA' in dropdownprio:
        dff = dff
    else:
        if dropdownprio != "NA":
            dff = dff[dff['CRITICO'].isin(dropdownprio)]

    # TIPO PERSONAL
    if not dropdowntipo or 'NA' in dropdowntipo:
        dff = dff
    else:
        if dropdowntipo != "NA":
            dff = dff[dff['Tipopersonal'].isin(dropdowntipo)]
    # FECHA
    if not start_date or 'NA' in start_date or not end_date or 'NA' in end_date:
        dff = dff
    else:
        if start_date != "NA":
            #dff = dff[dff['FECHA'].isin(start_date)]
            dff = dff.loc[start_date:end_date]

            # GASTO O INVERSION
    if not dropdowntipogoi or 'NA' in dropdowntipogoi:
        dff = dff
    else:
        if dropdowntipogoi != "NA":
            dff = dff[dff['DESC_SDI'].isin(dropdowntipogoi)]
            
            
            
            #BODEGAS
    if not dropdownboder or 'NA' in dropdownboder:
        dff = dff
    else:
        if dropdownboder != "NA":
            dff = dff[dff['BODEGA'].isin(dropdownboder)]




    dff = dff.sort_values('CANTIDAD', ascending=False)

    # dff=dff.head(50)

    # aqui deben empezar las listas o la reagrupación

    dffxs = dff. groupby(['CENTRO_DE_COSTO', 'ENTREGA_O_RECIBE', 'Descripcion_cod',
                         'TIPO_x']).CANTIDAD.sum().sort_values(ascending=False)
    dffxs = dffxs.to_frame()
    dffxs = dffxs.reset_index(level='CENTRO_DE_COSTO')
    dffxs = dffxs.reset_index(level='ENTREGA_O_RECIBE')
    dffxs = dffxs.reset_index(level='Descripcion_cod')
    dffxs = dffxs.reset_index(level='TIPO_x')

    df_mask = dffxs['TIPO_x'] == "EGRESO"
    egresosxxx = dffxs[df_mask]

    egresosxxx = egresosxxx.sort_values('CANTIDAD', ascending=False)
    egresosxxx = egresosxxx.head(40)

    figure2224 = px.bar(egresosxxx, x="CANTIDAD", y="CENTRO_DE_COSTO", color="ENTREGA_O_RECIBE", pattern_shape="Descripcion_cod",
                        pattern_shape_sequence=[".", "x", "+"], title="Contratistas-Personal qué más egresan materiales", orientation='h')

    return figure2224




# AUTORIZADORES inversion o gasto y dinero en total
@app.callback(
    Output('fini', 'figure'),
    Input('dropdownmat', 'value'),
    Input('dropdowncc', 'value'),
    Input('dropdownautor', 'value'),
    Input('dropdowntipo', 'value'),
    Input('dropdownmmi', 'value'),
    Input('dropdownmcp', 'value'),
    Input('dropdownprio', 'value'),
    Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'),
    Input('dropdownsonal', 'value'),
    Input('dropdowntipogoi', 'value'),
    Input('dropdownboder', 'value'),
    
    
)
def update_graph(dropdownmat, dropdowncc, dropdownautor, dropdowntipo, dropdownmmi, dropdownmcp, dropdownprio, start_date, end_date, dropdownsonal, dropdowntipogoi, dropdownboder):
    #dff = movbod.copy()
    #movibodmasxn['CANTIDAD'] = movibodmasxn['CANTIDAD'].astype(str)
   #movibodmasxn["CANTIDAD2"] = movibodmasxn["CANTIDAD"] + " " + movibodmasxn["UNIDAD"]

    movbod2 = movbod
    movbod2[['FECHA_']] = movbod2[['FECHA']]

    dff = movbod2. groupby(['Descripcion_cod', 'BODEGA', 'CENTRO_DE_COSTO', 'Tipopersonal', 'ENTREGA_O_RECIBE', 'AUTORIZADOR', 'TIPO_x', 'MMI',
                           'PRIORIZAR_COMPRA', 'CRITICO', 'Motivo', 'FECHA_', 'FECHA', 'Grupomas50', 'DESC_SDI', 'VALOR_TOTAL']).CANTIDAD.sum().sort_values(ascending=False)
    dff = dff.to_frame()
    dff = dff.reset_index(level='Descripcion_cod')
    dff = dff.reset_index(level='BODEGA')
    dff = dff.reset_index(level='CENTRO_DE_COSTO')
    dff = dff.reset_index(level='Tipopersonal')
    dff = dff.reset_index(level='ENTREGA_O_RECIBE')
    dff = dff.reset_index(level='AUTORIZADOR')
    dff = dff.reset_index(level='TIPO_x')
    dff = dff.reset_index(level='MMI')
    dff = dff.reset_index(level='PRIORIZAR_COMPRA')
    dff = dff.reset_index(level='CRITICO')
    dff = dff.reset_index(level='Motivo')
    dff = dff.reset_index(level='Grupomas50')
    dff = dff.reset_index(level='DESC_SDI')
    dff = dff.reset_index(level='FECHA_')
    dff = dff.reset_index(level='VALOR_TOTAL')

    # material
    if not dropdownmat or 'NA' in dropdownmat:
        dff = dff
    else:
        if dropdownmat != "NA":
            dff = dff[dff['Descripcion_cod'].isin(dropdownmat)]
    # cc
    if not dropdowncc or 'NA' in dropdowncc:
        dff = dff
    else:
        if dropdowncc != "NA":
            dff = dff[dff['CENTRO_DE_COSTO'].isin(dropdowncc)]
    # personal
    if not dropdownsonal or 'NA' in dropdownsonal:
        dff = dff
    else:
        if dropdownsonal != "NA":
            dff = dff[dff['ENTREGA_O_RECIBE'].isin(dropdownsonal)]
    # autorizados
    if not dropdownautor or 'NA' in dropdownautor:
        dff = dff
    else:
        if dropdownautor != "NA":
            dff = dff[dff['AUTORIZADOR'].isin(dropdownautor)]
    # mmi
    if not dropdownmmi or 'NA' in dropdownmmi:
        dff = dff
    else:
        if dropdownmmi != "NA":
            dff = dff[dff['MMI'].isin(dropdownmmi)]
    # priorizar
    if not dropdownmcp or 'NA' in dropdownmcp:
        dff = dff
    else:
        if dropdownmcp != "NA":
            dff = dff[dff['PRIORIZAR_COMPRA'].isin(dropdownmcp)]
    # criticos
    if not dropdownprio or 'NA' in dropdownprio:
        dff = dff
    else:
        if dropdownprio != "NA":
            dff = dff[dff['CRITICO'].isin(dropdownprio)]

    # TIPO PERSONAL
    if not dropdowntipo or 'NA' in dropdowntipo:
        dff = dff
    else:
        if dropdowntipo != "NA":
            dff = dff[dff['Tipopersonal'].isin(dropdowntipo)]
    # FECHA
    if not start_date or 'NA' in start_date or not end_date or 'NA' in end_date:
        dff = dff
    else:
        if start_date != "NA":
            #dff = dff[dff['FECHA'].isin(start_date)]
            dff = dff.loc[start_date:end_date]
 
            # GASTO O INVERSION
    if not dropdowntipogoi or 'NA' in dropdowntipogoi:
        dff = dff
    else:
        if dropdowntipogoi != "NA":
            dff = dff[dff['DESC_SDI'].isin(dropdowntipogoi)]

    dff = dff.sort_values('CANTIDAD', ascending=False)
    
    
            # BODEGAS
    if not dropdownboder or 'NA' in dropdownboder:
        dff = dff
    else:
        if dropdownboder != "NA":
            dff = dff[dff['DESC_SDI'].isin(dropdownboder)]

    dff = dff.sort_values('BODEGA', ascending=False)
    
    
    
    

    # dff=dff.head(5000)

    # aqui deben empezar las listas o la reagrupación
    #dff = dff.reset_index(level='FECHA')

    dffxss = dff. groupby(['AUTORIZADOR', 'DESC_SDI', 'TIPO_x']
                          ).CANTIDAD.sum().sort_values(ascending=False)
    #dffxs = dffxs.to_frame()
    dffxss = dffxss.reset_index(level='AUTORIZADOR')
    dffxss = dffxss.reset_index(level='DESC_SDI')
    dffxss = dffxss.reset_index(level='TIPO_x')

    df_mask = dffxss['TIPO_x'] == "EGRESO"
    dffxss = dffxss[df_mask]

    dffxss = dffxss.sort_values('CANTIDAD', ascending=False)
    dffxss = dffxss.head(20)
    figure2224sf = px.sunburst(dffxss, path=[
                               'DESC_SDI', 'AUTORIZADOR'], values='CANTIDAD', title="Recursos en egresos")

    return figure2224sf




# mat en linea de tiempo egresos
@app.callback(
    Output('movmat', 'figure'),
    Input('dropdownmat', 'value'),
    Input('dropdowncc', 'value'),
    Input('dropdownautor', 'value'),
    Input('dropdowntipo', 'value'),
    Input('dropdownmmi', 'value'),
    Input('dropdownmcp', 'value'),
    Input('dropdownprio', 'value'),
    Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'),
    Input('dropdownsonal', 'value'),
    Input('dropdowntipogoi', 'value'),
    Input('dropdownboder', 'value'),
    
    
)
def update_graph(dropdownmat, dropdowncc, dropdownautor, dropdowntipo, dropdownmmi, dropdownmcp, dropdownprio,  start_date, end_date, dropdownsonal, dropdowntipogoi, dropdownboder):
    #dff = movbod.copy()
    #movibodmasxn['CANTIDAD'] = movibodmasxn['CANTIDAD'].astype(str)
   #movibodmasxn["CANTIDAD2"] = movibodmasxn["CANTIDAD"] + " " + movibodmasxn["UNIDAD"]

    movbod2 = movbod
    movbod2[['FECHA_']] = movbod2[['FECHA']]

    dff = movbod2. groupby(['Descripcion_cod', 'BODEGA', 'CENTRO_DE_COSTO', 'Tipopersonal', 'ENTREGA_O_RECIBE', 'AUTORIZADOR', 'TIPO_x', 'MMI',
                           'PRIORIZAR_COMPRA', 'CRITICO', 'Motivo', 'FECHA_', 'FECHA', 'Grupomas50', 'DESC_SDI', 'VALOR_TOTAL']).CANTIDAD.sum().sort_values(ascending=False)
    dff = dff.to_frame()
    dff = dff.reset_index(level='Descripcion_cod')
    dff = dff.reset_index(level='BODEGA')
    dff = dff.reset_index(level='CENTRO_DE_COSTO')
    dff = dff.reset_index(level='Tipopersonal')
    dff = dff.reset_index(level='ENTREGA_O_RECIBE')
    dff = dff.reset_index(level='AUTORIZADOR')
    dff = dff.reset_index(level='TIPO_x')
    dff = dff.reset_index(level='MMI')
    dff = dff.reset_index(level='PRIORIZAR_COMPRA')
    dff = dff.reset_index(level='CRITICO')
    dff = dff.reset_index(level='Motivo')
    dff = dff.reset_index(level='Grupomas50')
    dff = dff.reset_index(level='DESC_SDI')
    dff = dff.reset_index(level='FECHA_')
    dff = dff.reset_index(level='VALOR_TOTAL')

    # material
    if not dropdownmat or 'NA' in dropdownmat:
        dff = dff
    else:
        if dropdownmat != "NA":
            dff = dff[dff['Descripcion_cod'].isin(dropdownmat)]
    # cc
    if not dropdowncc or 'NA' in dropdowncc:
        dff = dff
    else:
        if dropdowncc != "NA":
            dff = dff[dff['CENTRO_DE_COSTO'].isin(dropdowncc)]
    # personal
    if not dropdownsonal or 'NA' in dropdownsonal:
        dff = dff
    else:
        if dropdownsonal != "NA":
            dff = dff[dff['ENTREGA_O_RECIBE'].isin(dropdownsonal)]
    # autorizados
    if not dropdownautor or 'NA' in dropdownautor:
        dff = dff
    else:
        if dropdownautor != "NA":
            dff = dff[dff['AUTORIZADOR'].isin(dropdownautor)]
    # mmi
    if not dropdownmmi or 'NA' in dropdownmmi:
        dff = dff
    else:
        if dropdownmmi != "NA":
            dff = dff[dff['MMI'].isin(dropdownmmi)]
    # priorizar
    if not dropdownmcp or 'NA' in dropdownmcp:
        dff = dff
    else:
        if dropdownmcp != "NA":
            dff = dff[dff['PRIORIZAR_COMPRA'].isin(dropdownmcp)]
    # criticos
    if not dropdownprio or 'NA' in dropdownprio:
        dff = dff
    else:
        if dropdownprio != "NA":
            dff = dff[dff['CRITICO'].isin(dropdownprio)]

    # TIPO PERSONAL
    if not dropdowntipo or 'NA' in dropdowntipo:
        dff = dff
    else:
        if dropdowntipo != "NA":
            dff = dff[dff['Tipopersonal'].isin(dropdowntipo)]
    # FECHA
    if not start_date or 'NA' in start_date or not end_date or 'NA' in end_date:
        dff = dff
    else:
        if start_date != "NA":
            #dff = dff[dff['FECHA'].isin(start_date)]
            dff = dff.loc[start_date:end_date]

            # GASTO O INVERSION
    if not dropdowntipogoi or 'NA' in dropdowntipogoi:
        dff = dff
    else:
        if dropdowntipogoi != "NA":
            dff = dff[dff['DESC_SDI'].isin(dropdowntipogoi)]
            
            # BODEGAS
    if not dropdownboder or 'NA' in dropdownboder:
        dff = dff
    else:
        if dropdownboder != "NA":
            dff = dff[dff['BODEGA'].isin(dropdownboder)]
            
             
            
            

    dff = dff.sort_values('CANTIDAD', ascending=False)

    # dff=dff.head(50)

    # aqui deben empezar las listas o la reagrupación
    #dff = dff.reset_index(level='FECHA')

    # dffxss=dffxss.head(400)

    # dffxss=dffxss.head(15)

    dffxss = dff. groupby(['Descripcion_cod', 'FECHA_', 'TIPO_x']
                          ).CANTIDAD.sum().sort_values(ascending=False)
    #dffxs = dffxs.to_frame()
    dffxss = dffxss.reset_index(level='Descripcion_cod')
    dffxss = dffxss.reset_index(level='FECHA_')
    dffxss = dffxss.reset_index(level='TIPO_x')
    df_mask = dffxss['TIPO_x'] == "EGRESO"
    egresos = dffxss[df_mask]

    egresos = egresos.head(80)
    egresos = egresos.sort_values('FECHA_', ascending=False)

    figure2224sww = px.line(egresos, x="FECHA_", y="CANTIDAD",
                            color='Descripcion_cod', title="Movimientos de egresos")

    return figure2224sww



@app.callback(
    Output('output-container-date-picker-range', 'children'),
    Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'))
def update_output(start_date, end_date):
    string_prefix = 'Fecha analisis: '
    if start_date is not None:
        start_date_object = date.fromisoformat(start_date)
        start_date_string = start_date_object.strftime('%B %d, %Y')
        string_prefix = string_prefix + 'Fecha inicio: ' + start_date_string + ' | '
    if end_date is not None:
        end_date_object = date.fromisoformat(end_date)
        end_date_string = end_date_object.strftime('%B %d, %Y')
        string_prefix = string_prefix + 'Fecha fin: ' + end_date_string
    if len(string_prefix) == len('Fecha analisis: '):
        #mini = date.fromisoformat(mini)
        #mini = mini.strftime('%B %d, %Y')
        return f'Fecha analisis: Fecha inicio: {mini} | Fecha fin: {maxi}'

    else:
        return string_prefix


@app.callback(
    Output('store-data', 'data'),
    Input('dropdownmat', 'value'),
    Input('dropdowncc', 'value'),
    Input('dropdownautor', 'value'),
    Input('dropdowntipo', 'value'),
    Input('dropdownmmi', 'value'),
    Input('dropdownmcp', 'value'),
    Input('dropdownprio', 'value'),
    Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'),
    Input('dropdownsonal', 'value'),
    Input('dropdowntipogoi', 'value'),
    Input('dropdownboder', 'value'),

)
def store_data(dropdownmat, dropdowncc, dropdownautor, dropdowntipo, dropdownmmi, dropdownmcp, dropdownprio, start_date, end_date,  dropdownsonal, dropdowntipogoi,dropdownboder):
    # hypothetical enormous dataset with millions of rows

    movbod2 = movbod
    movbod2[['FECHA_']] = movbod2[['FECHA']]

    dffr = movbod2. groupby(['UNIDAD','CODIGO', 'Descripcion', 'DOCUMENTO', 'Descripcion_cod', 'BODEGA', 'CENTRO_DE_COSTO', 'Tipopersonal', 'ENTREGA_O_RECIBE', 'AUTORIZADOR',
                            'TIPO_x', 'MMI', 'PRIORIZAR_COMPRA', 'CRITICO', 'Motivo', 'FECHA_', 'FECHA', 'Grupomas50', 'DESC_SDI', 'VALOR_TOTAL']).CANTIDAD.sum().sort_values(ascending=False)
    dffr = dffr.to_frame()
    dffr = dffr.reset_index(level='Descripcion_cod')
    dffr = dffr.reset_index(level='BODEGA')
    dffr = dffr.reset_index(level='CENTRO_DE_COSTO')
    dffr = dffr.reset_index(level='Tipopersonal')
    dffr = dffr.reset_index(level='ENTREGA_O_RECIBE')
    dffr = dffr.reset_index(level='AUTORIZADOR')
    dffr = dffr.reset_index(level='TIPO_x')
    dffr = dffr.reset_index(level='MMI')
    dffr = dffr.reset_index(level='PRIORIZAR_COMPRA')
    dffr = dffr.reset_index(level='CRITICO')
    dffr = dffr.reset_index(level='Motivo')
    dffr = dffr.reset_index(level='Grupomas50')
    dffr = dffr.reset_index(level='DESC_SDI')
    dffr = dffr.reset_index(level='FECHA_')
    dffr = dffr.reset_index(level='VALOR_TOTAL')
    dffr = dffr.reset_index(level='DOCUMENTO')
    dffr = dffr.reset_index(level='Descripcion')
    dffr = dffr.reset_index(level='CODIGO')
    dffr = dffr.reset_index(level='UNIDAD')
    # material
    if not dropdownmat or 'NA' in dropdownmat:
        dffr = dffr
    else:
        if dropdownmat != "NA":
            dffr = dffr[dffr['Descripcion_cod'].isin(dropdownmat)]
    # cc
    if not dropdowncc or 'NA' in dropdowncc:
        dffr = dffr
    else:
        if dropdowncc != "NA":
            dffr = dffr[dffr['CENTRO_DE_COSTO'].isin(dropdowncc)]
    # personal
    if not dropdownsonal or 'NA' in dropdownsonal:
        dffr = dffr
    else:
        if dropdownsonal != "NA":
            dffr = dffr[dffr['ENTREGA_O_RECIBE'].isin(dropdownsonal)]
    # autorizados
    if not dropdownautor or 'NA' in dropdownautor:
        dffr = dffr
    else:
        if dropdownautor != "NA":
            dffr = dffr[dffr['AUTORIZADOR'].isin(dropdownautor)]
    # mmi
    if not dropdownmmi or 'NA' in dropdownmmi:
        dffr = dffr
    else:
        if dropdownmmi != "NA":
            dffr = dffr[dffr['MMI'].isin(dropdownmmi)]
    # priorizar
    if not dropdownmcp or 'NA' in dropdownmcp:
        dffr = dffr
    else:
        if dropdownmcp != "NA":
            dffr = dffr[dffr['PRIORIZAR_COMPRA'].isin(dropdownmcp)]
    # criticos
    if not dropdownprio or 'NA' in dropdownprio:
        dffr = dffr
    else:
        if dropdownprio != "NA":
            dffr = dffr[dffr['CRITICO'].isin(dropdownprio)]

    # TIPO PERSONAL
    if not dropdowntipo or 'NA' in dropdowntipo:
        dffr = dffr
    else:
        if dropdowntipo != "NA":
            dffr = dffr[dffr['Tipopersonal'].isin(dropdowntipo)]
    # FECHA
    if not start_date or 'NA' in start_date or not end_date or 'NA' in end_date:
        dffr = dffr
    else:
        if start_date != "NA":
            #dff = dff[dff['FECHA'].isin(start_date)]
            dffr = dffr.loc[start_date:end_date]

            # GASTO O INVERSION
    if not dropdowntipogoi or 'NA' in dropdowntipogoi:
        dffr = dffr
    else:
        if dropdowntipogoi != "NA":
            dffr = dffr[dffr['DESC_SDI'].isin(dropdowntipogoi)]

    dffr = dffr.sort_values('CANTIDAD', ascending=False)
    
            # BODEGAS
    if not dropdownboder or 'NA' in dropdownboder:
        dffr = dffr
    else:
        if dropdownboder != "NA":
            dffr = dffr[dffr['BODEGA'].isin(dropdownboder)]

    dffr = dffr.sort_values('CANTIDAD', ascending=False)
    
    

    # return dff.to_dict('records')

    # 2. or save as string like JSON
    # return no_update
    return dffr.to_json(date_format='iso', orient='split')


@app.callback(
    Output("download-dataframe-xlsx", "data"),
    Input("btn_xlsx", "n_clicks"),
    State('store-data', 'data'),



    prevent_initial_call=False,
)
def func(n_clicks, jsonified_cleaned_data):
    if n_clicks > 0:

        dff2 = pd.read_json(jsonified_cleaned_data, orient='split')
        #dff = dff[dff['Grupomas50'].isin(dropdowngrmas50)]
        dff2 = dff2. groupby(['CODIGO','UNIDAD', 'Descripcion', 'MMI', 'PRIORIZAR_COMPRA', 'Grupomas50', 'CRITICO', 'Descripcion_cod', 'BODEGA', 'ENTREGA_O_RECIBE',
                             'TIPO_x', 'DOCUMENTO', 'CENTRO_DE_COSTO', 'AUTORIZADOR', 'VALOR_TOTAL', 'DESC_SDI', 'FECHA_']).CANTIDAD.sum().sort_values(ascending=False)

        dff2 = dff2.to_frame()
        dff2 = dff2.reset_index(level='UNIDAD')
        dff2 = dff2.reset_index(level='Descripcion_cod')
        dff2 = dff2.reset_index(level='BODEGA')
        dff2 = dff2.reset_index(level='ENTREGA_O_RECIBE')
        dff2 = dff2.reset_index(level='TIPO_x')
        dff2 = dff2.reset_index(level='DOCUMENTO')
        dff2 = dff2.reset_index(level='CENTRO_DE_COSTO')
        dff2 = dff2.reset_index(level='AUTORIZADOR')
        dff2 = dff2.reset_index(level='VALOR_TOTAL')
        dff2 = dff2.reset_index(level='DESC_SDI')
        dff2 = dff2.reset_index(level='FECHA_')
        dff2 = dff2.reset_index(level='CRITICO')
        dff2 = dff2.reset_index(level='Grupomas50')
        dff2 = dff2.reset_index(level='PRIORIZAR_COMPRA')
        dff2 = dff2.reset_index(level='MMI')
        dff2 = dff2.reset_index(level='Descripcion')
        dff2 = dff2.reset_index(level='CODIGO')
        dff2 = dff2.drop(['Descripcion_cod'], axis=1)
    return dcc.send_data_frame(dff2.to_excel, "Movimientos_bodegas_DPCE.xlsx", sheet_name="DPCE", index = False)


# %% DASH DROPDOWN DETALLE DE MATERIALES


@app.callback(
    Output('table-container_', 'data'),
    Input('dropdownmatok', 'value'),
    Input('dropdownprio', 'value'),
    Input('dropdownmmi', 'value'),
    Input('dropdownmcp', 'value'),
    Input('dropdownmatokbod', 'value'),
    Input('dropdownmatokac', 'value'),


)
def data(dropdownmatok,dropdownprio,dropdownmmi,dropdownmcp,dropdownmatokbod,dropdownmatokac):


    dffl = stocktotalbodmas. groupby(['CONSUMO_PROMEDIO_DIARIO',
                                      'LIMITE_MINIMO_STOCK_PARA_INICIAR_PROCESO_CONTRATACION',
                                      'STOCKTOTAL','FECHA_ULTIMOEGRESO','FECHA_PROYECCION_FIN_MATERIAL',
                                      'CRITICO','PRIORIZAR_COMPRA','MMI','CODIGO', 
                                      'DESCRIPCION', 'NOMBREBODEGA', 'STOCKPORBODEGA',
                                      'Descripcion_cod','UNIDAD','ACTIVIDAD', ]).REGISTRO.count().sort_values(ascending=False)

    dffl = dffl.to_frame()
    dffl = dffl.reset_index(level='CONSUMO_PROMEDIO_DIARIO')
    dffl = dffl.reset_index(level='UNIDAD')
    dffl = dffl.reset_index(level='STOCKPORBODEGA')
    dffl = dffl.reset_index(level='NOMBREBODEGA')
    dffl = dffl.reset_index(level='Descripcion_cod')
    dffl = dffl.reset_index(level='DESCRIPCION')
    dffl = dffl.reset_index(level='CODIGO')
    dffl = dffl.reset_index(level='CRITICO')
    dffl = dffl.reset_index(level='PRIORIZAR_COMPRA')
    dffl = dffl.reset_index(level='MMI')
    dffl = dffl.reset_index(level='ACTIVIDAD')
    dffl = dffl.reset_index(level='LIMITE_MINIMO_STOCK_PARA_INICIAR_PROCESO_CONTRATACION')
    dffl = dffl.reset_index(level='STOCKTOTAL')
    dffl = dffl.reset_index(level='FECHA_ULTIMOEGRESO')
    dffl = dffl.reset_index(level='FECHA_PROYECCION_FIN_MATERIAL')
    
    
    
    # crtico
    if not dropdownmatok or 'NA' in dropdownmatok:
        dffl = dffl
    else:
        if dropdownmatok != "NA":
            dffl = dffl[dffl['Descripcion_cod'].isin(dropdownmatok)]
            
    # crtico
    if not dropdownprio or 'NA' in dropdownprio:
        dffl = dffl
    else:
        if dropdownprio != "NA":
            dffl = dffl[dffl['CRITICO'].isin(dropdownprio)]

        # priorizar
    if not dropdownmcp or 'NA' in dropdownmcp:
        dffl = dffl
    else:
        if dropdownmcp != "NA":
            dffl = dffl[dffl['PRIORIZAR_COMPRA'].isin(dropdownmcp)]

        # MMI
    if not dropdownmmi or 'NA' in dropdownmmi:
        dffl = dffl
    else:
        if dropdownmmi != "NA":
            dffl = dffl[dffl['MMI'].isin(dropdownmmi)]
            
           # bodega
    if not dropdownmatokbod or 'NA' in dropdownmatokbod:
        dffl = dffl
    else:
        if dropdownmatokbod != "NA":
            dffl = dffl[dffl['NOMBREBODEGA'].isin(dropdownmatokbod)]
            
            
            # actividad
    if not dropdownmatokac or 'NA' in dropdownmatokac:
        dffl = dffl
    else:
        if dropdownmatokac != "NA":
            dffl = dffl[dffl['ACTIVIDAD'].isin(dropdownmatokac)]
            
            
            
    



    dffl = dffl.sort_values('CODIGO', ascending=False)
             
    return dffl.to_dict("records")





@app.callback(
    Output('store-dataokzz', 'data'),
    Input('dropdownmatok', 'value'),
    Input('dropdownprio', 'value'),
    Input('dropdownmmi', 'value'),
    Input('dropdownmcp', 'value'),
    Input('dropdownmatokbod', 'value'),
    Input('dropdownmatokac', 'value'),



)
def store_data_zz(dropdownmatok, dropdownprio,  dropdownmmi, dropdownmcp, dropdownmatokbod, dropdownmatokac  ):




    dffl = stocktotalbodmas. groupby(['LIMITE_MINIMO_STOCK_PARA_INICIAR_PROCESO_CONTRATACION',
                                      'STOCKTOTAL','FECHA_PROYECCION_FIN_MATERIAL',
                                      'CRITICO','PRIORIZAR_COMPRA','MMI','CODIGO', 
                                      'DESCRIPCION', 'NOMBREBODEGA', 'STOCKPORBODEGA',
                                      'Descripcion_cod','UNIDAD','ACTIVIDAD', ]).REGISTRO.count().sort_values(ascending=False)

    dffl = dffl.to_frame()
    dffl = dffl.reset_index(level='UNIDAD')
    dffl = dffl.reset_index(level='STOCKPORBODEGA')
    dffl = dffl.reset_index(level='NOMBREBODEGA')
    dffl = dffl.reset_index(level='Descripcion_cod')
    dffl = dffl.reset_index(level='DESCRIPCION')
    dffl = dffl.reset_index(level='CODIGO')
    dffl = dffl.reset_index(level='CRITICO')
    dffl = dffl.reset_index(level='PRIORIZAR_COMPRA')
    dffl = dffl.reset_index(level='MMI')
    dffl = dffl.reset_index(level='ACTIVIDAD')
    dffl = dffl.reset_index(level='LIMITE_MINIMO_STOCK_PARA_INICIAR_PROCESO_CONTRATACION')
    dffl = dffl.reset_index(level='STOCKTOTAL')
    #dffl = dffl.reset_index(level='FECHA_ULTIMOEGRESO')
    dffl = dffl.reset_index(level='FECHA_PROYECCION_FIN_MATERIAL')

    #dffl['CONSUMO_PROMEDIO_DIARIO'] = dffl['CONSUMO_PROMEDIO_DIARIO'].apply(lambda x: round(x))
    #dffl=dffl.assign(guion="-")
    

     
    # crtico
    if not dropdownmatok or 'NA' in dropdownmatok:
        dffl = dffl
    else:
        if dropdownmatok != "NA":
            dffl = dffl[dffl['Descripcion_cod'].isin(dropdownmatok)]
            
    # crtico
    if not dropdownprio or 'NA' in dropdownprio:
        dffl = dffl
    else:
        if dropdownprio != "NA":
            dffl = dffl[dffl['CRITICO'].isin(dropdownprio)]

        # priorizar
    if not dropdownmcp or 'NA' in dropdownmcp:
        dffl = dffl
    else:
        if dropdownmcp != "NA":
            dffl = dffl[dffl['PRIORIZAR_COMPRA'].isin(dropdownmcp)]

        # MMI
    if not dropdownmmi or 'NA' in dropdownmmi:
        dffl = dffl
    else:
        if dropdownmmi != "NA":
            dffl = dffl[dffl['MMI'].isin(dropdownmmi)]
            
           # bodega
    if not dropdownmatokbod or 'NA' in dropdownmatokbod:
        dffl = dffl
    else:
        if dropdownmatokbod != "NA":
            dffl = dffl[dffl['NOMBREBODEGA'].isin(dropdownmatokbod)]
            
            
            # actividad
    if not dropdownmatokac or 'NA' in dropdownmatokac:
        dffl = dffl
    else:
        if dropdownmatokac != "NA":
            dffl = dffl[dffl['ACTIVIDAD'].isin(dropdownmatokac)]
            

    dfflzz=dffl


    return dfflzz.to_json(date_format='iso', orient='split')
    #return dfflzz

# DESCARGA MATERIALES


@app.callback(
    Output("download-dataframe-xlsxokzz", "data"),
    Input("btn_xlsxokzz", "n_clicks"),
    State('store-dataokzz', 'data'),



    prevent_initial_call=False,
)
def func(n_clicks, jsonified_cleaned_data):
    if n_clicks > 0:
        #dffl=dffls
        dfflzz = pd.read_json(jsonified_cleaned_data, orient='split')
        
        #dffl=dfflzz
        dffl = dfflzz. groupby(['LIMITE_MINIMO_STOCK_PARA_INICIAR_PROCESO_CONTRATACION',
                                          'STOCKTOTAL','FECHA_PROYECCION_FIN_MATERIAL',
                                          'CRITICO','PRIORIZAR_COMPRA','MMI','CODIGO', 
                                          'DESCRIPCION', 'NOMBREBODEGA', 'STOCKPORBODEGA',
                                          'Descripcion_cod','UNIDAD','ACTIVIDAD'
                                    ]).REGISTRO.count().sort_values(ascending=False)
    
        #dffl = dffl.to_frame()
       
        dffl = dffl.reset_index(level='UNIDAD')


        dffl = dffl.reset_index(level='Descripcion_cod')


        dffl = dffl.reset_index(level='CRITICO')
        
        dffl = dffl.reset_index(level='STOCKTOTAL')
        dffl = dffl.reset_index(level='LIMITE_MINIMO_STOCK_PARA_INICIAR_PROCESO_CONTRATACION')
        dffl = dffl.reset_index(level='FECHA_PROYECCION_FIN_MATERIAL')
        dffl = dffl.reset_index(level='MMI')
        dffl = dffl.reset_index(level='ACTIVIDAD')
        dffl = dffl.reset_index(level='STOCKPORBODEGA')
        dffl = dffl.reset_index(level='NOMBREBODEGA')
        dffl = dffl.reset_index(level='DESCRIPCION')
        dffl = dffl.reset_index(level='CODIGO')
        dffl = dffl.reset_index(level='PRIORIZAR_COMPRA')
        
        
        dffl = dffl.rename( columns = {'MMI':'MATERIAL MAYOR IMPORTANCIA'})
        dffl=dffl.drop(["LIMITE_MINIMO_STOCK_PARA_INICIAR_PROCESO_CONTRATACION","CRITICO","Descripcion_cod","REGISTRO"],axis=1)
        dffl4=dffl
        
        
        
    return dcc.send_data_frame(dffl4.to_excel, "Materiales_DPCE.xlsx", sheet_name="DPCE", index=False)







# %% DASH DROPDOWN DESCARGA DE INFORMES

@app.callback(
    Output('store-data6', 'data'),
    Input('dropdownprio', 'value'),
    Input('dropdownmmi', 'value'),
    Input('dropdownmcp', 'value'),
)
def store_data_(dropdownprio, dropdownmmi, dropdownmcp):

    dffl = stocktotalbodmas
    

    
    return dffl.to_json(date_format='iso', orient='split')
    #return c.to_json(date_format='iso', orient='split')
                
                #html.Button("Descargar informe general ", id="infor_"),
                #dcc.Download(id="doinfor_"),
                #dcc.Store(id='store-data6'






@app.callback(
    Output("doinfor_", "data"),
    Input("infor_", "n_clicks"),
    State('store-data6', 'data'),



    prevent_initial_call=False,
)
def func(n_clicks, jsonified_cleaned_data):
    if n_clicks > 0:
        
        def hello(c):
            c.drawString(100,100,"Hello World")
            
            
        c = canvas.Canvas("okokok.pdf")
        hello(c)
        c.showPage()
        c.save()



        #dffl=dffls
        dffl = pd.read_json(jsonified_cleaned_data, orient='split')
        #dffl = dff[dff['Grupomas50'].isin(dropdowngrmas50)]

    return dcc.send_data_frame(dffl.to_excel, "Materiales_DPCE.xlsx", sheet_name="DPCE")


# pagina 2
           

# %% DASH DROPDOWN  MATERIALES CON PRIORIDAD DE COMPRA

# PAGINA 1


# descarga MATERIALES


@app.callback(
    Output('store-data_', 'data'),
    Input('dropdownprio', 'value'),
    Input('dropdownmmi', 'value'),
    Input('dropdownmcp', 'value'),







)
def store_data_(dropdownprio, dropdownmmi, dropdownmcp):

    dffl = stocktotalbodmas. groupby(['CODIGO', 'DESCRIPCION_', 'Descripcion_cod', 'STOCKTOTAL', 'ACTIVIDAD', 'STOCK_MAXIMO', 'STOCK_MINIMO', 'CANTIDAD_SUGERIDAD_PARA_COMPRA', 'PRIORIZAR_COMPRA', 'CRITICO', 'CODIGOCPC', 'FECHAULTIMA_COMPRA',
                                     'FECHA_ULTIMOEGRESO', 'MMI', 'FECHA_PROYECCION_FIN_MATERIAL', 'PORCENTAJE_DE_PRIORIDAD', 'PREC_UNITARIO', 'ESTIMADO_VALOR_DE_COMPRA', 'VALOR_MATERIALES', ]).REGISTRO.count().sort_values(ascending=False)

    dffl = dffl.to_frame()

    dffl = dffl.reset_index(level='PORCENTAJE_DE_PRIORIDAD')
    dffl = dffl.reset_index(level='ACTIVIDAD')
    dffl = dffl.reset_index(level='STOCK_MAXIMO')
    dffl = dffl.reset_index(level='STOCK_MINIMO')
    dffl = dffl.reset_index(level='CANTIDAD_SUGERIDAD_PARA_COMPRA')
    dffl = dffl.reset_index(level='PRIORIZAR_COMPRA')
    dffl = dffl.reset_index(level='CRITICO')
    dffl = dffl.reset_index(level='CODIGOCPC')
    dffl = dffl.reset_index(level='FECHAULTIMA_COMPRA')
    dffl = dffl.reset_index(level='FECHA_ULTIMOEGRESO')
    dffl = dffl.reset_index(level='MMI')
    dffl = dffl.reset_index(level='FECHA_PROYECCION_FIN_MATERIAL')
    dffl = dffl.reset_index(level='STOCKTOTAL')
    dffl = dffl.reset_index(level='PREC_UNITARIO')
    dffl = dffl.reset_index(level='ESTIMADO_VALOR_DE_COMPRA')
    dffl = dffl.reset_index(level='VALOR_MATERIALES')
    dffl = dffl.reset_index(level='Descripcion_cod')
    dffl = dffl.reset_index(level='DESCRIPCION_')
    dffl = dffl.reset_index(level='CODIGO')

    # crtico
    if not dropdownprio or 'NA' in dropdownprio:
        dffl = dffl
    else:
        if dropdownprio != "NA":
            dffl = dffl[dffl['CRITICO'].isin(dropdownprio)]

        # priorizar
    if not dropdownmcp or 'NA' in dropdownmcp:
        dffl = dffl
    else:
        if dropdownmcp != "NA":
            dffl = dffl[dffl['PRIORIZAR_COMPRA'].isin(dropdownmcp)]

        # MMI
    if not dropdownmmi or 'NA' in dropdownmmi:
        dffl = dffl
    else:
        if dropdownmmi != "NA":
            dffl = dffl[dffl['MMI'].isin(dropdownmmi)]

    df_mask = dffl['PORCENTAJE_DE_PRIORIDAD'] > 49
    dffl = dffl[df_mask]

    dffl = dffl.sort_values('PORCENTAJE_DE_PRIORIDAD', ascending=False)

    return dffl.to_json(date_format='iso', orient='split')


# DESCARGA MATERIALES


@app.callback(
    Output("download-dataframe-xlsx_", "data"),
    Input("btn_xlsx_", "n_clicks"),
    State('store-data_', 'data'),



    prevent_initial_call=False,
)
def func(n_clicks, jsonified_cleaned_data):
    if n_clicks > 0:
        #dffl=dffls
        dffl = pd.read_json(jsonified_cleaned_data, orient='split')
        
        dffl2 = dffl. groupby(['CODIGO', 'DESCRIPCION_', 'Descripcion_cod', 'STOCKTOTAL', 'ACTIVIDAD', 'STOCK_MAXIMO', 'STOCK_MINIMO', 'CANTIDAD_SUGERIDAD_PARA_COMPRA', 'PRIORIZAR_COMPRA', 'CRITICO', 'CODIGOCPC', 'FECHAULTIMA_COMPRA',
                                         'FECHA_ULTIMOEGRESO', 'MMI', 'FECHA_PROYECCION_FIN_MATERIAL', 'PORCENTAJE_DE_PRIORIDAD', 'PREC_UNITARIO', 'ESTIMADO_VALOR_DE_COMPRA', 'VALOR_MATERIALES', ]).REGISTRO.count().sort_values(ascending=False)

        dffl2 = dffl2.to_frame()

        dffl2 = dffl2.reset_index(level='PORCENTAJE_DE_PRIORIDAD')
        dffl2 = dffl2.reset_index(level='ACTIVIDAD')
        dffl2 = dffl2.reset_index(level='STOCK_MAXIMO')
        
        dffl2 = dffl2.reset_index(level='CANTIDAD_SUGERIDAD_PARA_COMPRA')
        dffl2 = dffl2.reset_index(level='PRIORIZAR_COMPRA')
        dffl2 = dffl2.reset_index(level='CRITICO')
        
        dffl2 = dffl2.reset_index(level='FECHAULTIMA_COMPRA')
        dffl2 = dffl2.reset_index(level='FECHA_ULTIMOEGRESO')
        dffl2 = dffl2.reset_index(level='MMI')
        dffl2 = dffl2.reset_index(level='FECHA_PROYECCION_FIN_MATERIAL')
        dffl2 = dffl2.reset_index(level='STOCK_MINIMO')
        dffl2 = dffl2.reset_index(level='STOCKTOTAL')
        dffl2 = dffl2.reset_index(level='PREC_UNITARIO')
        dffl2 = dffl2.reset_index(level='ESTIMADO_VALOR_DE_COMPRA')
        dffl2 = dffl2.reset_index(level='VALOR_MATERIALES')
        dffl2 = dffl2.reset_index(level='Descripcion_cod')
        dffl2 = dffl2.reset_index(level='DESCRIPCION_')
        dffl2 = dffl2.reset_index(level='CODIGO')
        dffl2 = dffl2.reset_index(level='CODIGOCPC')
        dffl2= dffl2.drop_duplicates(['DESCRIPCION_', 'CODIGO'], keep='last')
        dffl2=dffl2.drop(['Descripcion_cod'], axis=1)
        dffl2=dffl2.drop(['REGISTRO'], axis=1)
        dffl2=dffl2.drop(["VALOR_MATERIALES","ESTIMADO_VALOR_DE_COMPRA","CRITICO","CANTIDAD_SUGERIDAD_PARA_COMPRA","STOCK_MAXIMO"],axis=1)
        dffl2 = dffl2.sort_values('FECHA_PROYECCION_FIN_MATERIAL', ascending=True)
        
        #dffl = dff[dff['Grupomas50'].isin(dropdowngrmas50)]

    return dcc.send_data_frame(dffl2.to_excel, "Materiales_DPCE.xlsx", sheet_name="DPCE", index=False)


# pagina 2




@app.callback(
    Output('table-container', 'data'),
    Input('dropdownprio', 'value'),
    Input('dropdownmmi', 'value'),
    Input('dropdownmcp', 'value'),


)
def data(dropdownprio, dropdownmmi, dropdownmcp):

    dffl = stocktotalbodmas. groupby(['CODIGO', 'DESCRIPCION', 'Descripcion_cod', 'STOCKTOTAL', 'ACTIVIDAD', 'STOCK_MAXIMO', 'STOCK_MINIMO', 'CANTIDAD_SUGERIDAD_PARA_COMPRA', 'PRIORIZAR_COMPRA', 'CRITICO', 'CODIGOCPC', 'FECHAULTIMA_COMPRA',
                                     'FECHA_ULTIMOEGRESO', 'MMI', 'FECHA_PROYECCION_FIN_MATERIAL', 'PORCENTAJE_DE_PRIORIDAD', 'PREC_UNITARIO', 'ESTIMADO_VALOR_DE_COMPRA', 'VALOR_MATERIALES','UNIDAD', ]).REGISTRO.count().sort_values(ascending=False)

    dffl = dffl.to_frame()

    dffl = dffl.reset_index(level='PORCENTAJE_DE_PRIORIDAD')
    dffl = dffl.reset_index(level='ACTIVIDAD')
    dffl = dffl.reset_index(level='STOCK_MAXIMO')
    dffl = dffl.reset_index(level='STOCK_MINIMO')
    dffl = dffl.reset_index(level='CANTIDAD_SUGERIDAD_PARA_COMPRA')
    dffl = dffl.reset_index(level='PRIORIZAR_COMPRA')
    dffl = dffl.reset_index(level='CRITICO')
    dffl = dffl.reset_index(level='CODIGOCPC')
    dffl = dffl.reset_index(level='FECHAULTIMA_COMPRA')
    dffl = dffl.reset_index(level='FECHA_ULTIMOEGRESO')
    dffl = dffl.reset_index(level='MMI')
    dffl = dffl.reset_index(level='FECHA_PROYECCION_FIN_MATERIAL')
    dffl = dffl.reset_index(level='UNIDAD')
    dffl = dffl.reset_index(level='STOCKTOTAL')
    dffl = dffl.reset_index(level='PREC_UNITARIO')
    dffl = dffl.reset_index(level='ESTIMADO_VALOR_DE_COMPRA')
    dffl = dffl.reset_index(level='VALOR_MATERIALES')
    dffl = dffl.reset_index(level='Descripcion_cod')
    dffl = dffl.reset_index(level='DESCRIPCION')
    dffl = dffl.reset_index(level='CODIGO')

    # crtico
    if not dropdownprio or 'NA' in dropdownprio:
        dffl = dffl
    else:
        if dropdownprio != "NA":
            dffl = dffl[dffl['CRITICO'].isin(dropdownprio)]

        # priorizar
    if not dropdownmcp or 'NA' in dropdownmcp:
        dffl = dffl
    else:
        if dropdownmcp != "NA":
            dffl = dffl[dffl['PRIORIZAR_COMPRA'].isin(dropdownmcp)]

        # MMI
    if not dropdownmmi or 'NA' in dropdownmmi:
        dffl = dffl
    else:
        if dropdownmmi != "NA":
            dffl = dffl[dffl['MMI'].isin(dropdownmmi)]

    df_mask = dffl['PORCENTAJE_DE_PRIORIDAD'] > 49
    dffl = dffl[df_mask]
    
    dffl= dffl.drop_duplicates(['DESCRIPCION', 'CODIGO'], keep='last')

    dffl = dffl.sort_values('FECHA_PROYECCION_FIN_MATERIAL', ascending=True)

    return dffl.to_dict("records")










                    
                   
                    

                    
                    



if __name__ == '__main__':
    app.run_server(debug=False,port=8051)
