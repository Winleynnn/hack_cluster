from dash import Dash, html, dcc, callback, Output, Input, dash_table
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("C://Users/Dmitriy/Desktop/out_final.csv")
df_out = pd.read_csv("C://Users/Dmitriy/Desktop/out2.csv")
df['number_of_teammates'] = df_out['4']

app = Dash(__name__)

app.layout = html.Div([
    dcc.Tabs([
        dcc.Tab(label='Итоговый балл', children=[
            html.Div(children=[
                html.H2(['Фильтр по типу участия']),
                dcc.RadioItems(['Все','Команда','Одиночка'], id = "status", value = 'Все'),
                html.H2(['Фильтр по полу']),
                dcc.RadioItems(['Все','Мужской','Женский'], id = 'sex', value = 'Все')
            ],style={'width':'25%','position':'fixed'}),
            html.Div([
                dcc.Dropdown(df['Категория'].unique().delete('null'), id = 'categories', value = ['Студент', 'Инженер'], multi=True),
                dcc.Graph(id='category_graph'),            
                dcc.Dropdown(df['Список компетенций'].unique(), id = "competence", value = ['Сварочные технологии; ','Инженер-конструктор; '], multi=True),
                dcc.Graph(id='comp_graph'),
                dcc.Dropdown(df['Образование'].unique(), id = "education", value = ['Бакалавриат','Специалитет'], multi=True),
                dcc.Graph(id='edu_graph'),
                dcc.Dropdown(df['Профессия'].unique(), id = "prof", value = ['Промышленная автоматика','Управление качеством'], multi=True),
                dcc.Graph(id='prof_graph')
            ], style={'width':'75%', 'marginLeft':'25%'}),
        ]),
        dcc.Tab(label="Количество участников", children=[
            html.Div(children=[
                    html.H2(['Фильтр по типу участия']),
                    dcc.RadioItems(['Все','Команда','Одиночка'], id = "status2", value = 'Все'),
                    html.H2(['Фильтр по полу']),
                    dcc.RadioItems(['Все','Мужской','Женский'], id = 'sex2', value = 'Все')
            ],style={'width':'25%','position':'fixed'}),
            html.Div([
                dcc.Dropdown(df['Категория'].unique(),id = 'categories2', value = ['Студент', 'Инженер'], multi=True),
                dcc.Graph(id='category_graph2'),      
                dcc.Dropdown(df['Список компетенций'].unique(), id = "competence2", value = ['Сварочные технологии; ','Инженер-конструктор; '], multi=True),
                dcc.Graph(id='comp_graph2'),     
                dcc.Dropdown(df['Образование'].unique(), id = "education2", value = ['Бакалавриат','Специалитет'], multi=True),
                dcc.Graph(id='edu_graph2'),        
                dcc.Dropdown(df['Профессия'].unique(), id = "prof2", value = ['Промышленная автоматика','Управление качеством'], multi=True),
                dcc.Graph(id='prof_graph2'),
            ], style={'width':'75%', 'marginLeft':'25%'})
        ])
    ])
])

@callback(
    Output('category_graph', 'figure'),
    Input('categories', 'value'),
    Input('status','value'),
    Input('sex','value')
)
def update_category(value, status, sex):
    dff = pd.DataFrame()
    fig = go.Figure()
    dff = df
    if (status == 'Команда'):
        dff = df[df['status']=='t']
    elif (status == 'Одиночка'):
        dff = df[df['status']=='s']
    if (sex == 'Мужской'):
        dff = df[df['Пол']==0]
    elif (sex == 'Женский'):
        dff = df[df['Пол']==1]
    for s in value:
        dfff = dff[dff['Категория']==s]
        fig.add_trace(go.Histogram(x=dfff['Категория'], y=dfff['Results'], name=s))
        fig.update_layout(legend=dict(yanchor="top", y=1.3, xanchor="center", x=0.5), yaxis_title='Итоговый балл')
        # dff = dff.append(df[df.country==s], ignore_index=True)
    return fig

@callback(
    Output('comp_graph','figure'),
    Input('competence','value'),    
    Input('status','value'),
    Input('sex','value')
)
def update_comp(value, status, sex):
    dff = pd.DataFrame()
    fig = go.Figure()
    dff = df
    if (status == 'Команда'):
        dff = df[df['status']=='t']
    elif (status == 'Одиночка'):
        dff = df[df['status']=='s']
    if (sex == 'Мужской'):
        dff = df[df['Пол']==0]
    elif (sex == 'Женский'):
        dff = df[df['Пол']==1]
    for s in value:
        dfff = dff[dff['Список компетенций']==s]
        fig.add_trace(go.Histogram(x=dfff['Список компетенций'], y=dfff['Results'], name=s))
        fig.update_layout(legend=dict(yanchor="top", y=1.3, xanchor="center", x=0.5), yaxis_title='Итоговый балл')
    return fig

@callback(
    Output('edu_graph', 'figure'),
    Input('education', 'value'),
    Input('status','value'),
    Input('sex','value')
)
def update_edu(value, status, sex):
    dff = pd.DataFrame()
    fig = go.Figure()
    dff = df
    if (status == 'Команда'):
        dff = df[df['status']=='t']
    elif (status == 'Одиночка'):
        dff = df[df['status']=='s']
    if (sex == 'Мужской'):
        dff = df[df['Пол']==0]
    elif (sex == 'Женский'):
        dff = df[df['Пол']==1]
    for s in value:
        dfff = dff[dff['Образование']==s]
        fig.add_trace(go.Histogram(x=dfff['Образование'], y=dfff['Results'], name=s))
        fig.update_layout(legend=dict(yanchor="top", y=1.3, xanchor="center", x=0.5), yaxis_title='Итоговый балл')
    return fig

@callback(
    Output('prof_graph', 'figure'),
    Input('prof', 'value'),
    Input('status','value'),
    Input('sex','value')

)
def update_prof(value, status, sex):
    dff = pd.DataFrame()
    fig = go.Figure()
    dff = df
    if (status == 'Команда'):
        dff = df[df['status']=='t']
    elif (status == 'Одиночка'):
        dff = df[df['status']=='s']
    if (sex == 'Мужской'):
        dff = df[df['Пол']==0]
    elif (sex == 'Женский'):
        dff = df[df['Пол']==1]
    for s in value:
        dfff = dff[dff['Профессия']==s]
        fig.add_trace(go.Histogram(x=dfff['Профессия'], y=dfff['Results'], name=s))
        fig.update_layout(legend=dict(yanchor="top", y=1.3, xanchor="center", x=0.5), yaxis_title='Итоговый балл')
    return fig

#--------------------------------------------

@callback(
    Output('category_graph2', 'figure'),
    Input('categories2', 'value'),
    Input('status2','value'),
    Input('sex2','value')
)
def update_category(value, status, sex):
    df_test = pd.DataFrame(columns=['Name','Sum'])
    # df[Категория==Студент] <- пол, тип участия
    stat = 'All'
    gender = 'All'
    if (status != 'Все'):
        if (status == 'Команда'):
            stat = 't'
        elif (status == 'Одиночка'):
            stat = 's'
    if (sex != 'Все'):
        if (sex == 'Мужской'):
            gender = 0
        elif (sex == 'Женский'):
            gender = 1
    if ((stat == 'All') & (gender == 'All')):
        for s in value:
            df_test.loc[len(df_test.index)] = [s, df[df['Категория']==s].shape[0]]
    if (stat != 'All'):
        if (gender == 'All'):
            for s in value:
                df_test.loc[len(df_test.index)] = [s, df[(df['Категория']==s)&(df['status']==stat)].shape[0]]
        else:
            for s in value:
                df_test.loc[len(df_test.index)] = [s, df[(df['Категория']==s)&(df['status']==stat)&(df['Пол']==gender)].shape[0]]
    if (gender != 'All'):
        if (stat == 'All'):
            for s in value:
                df_test.loc[len(df_test.index)] = [s, df[(df['Категория']==s)&(df['Пол']==gender)].shape[0]]
        else:
            for s in value:
                df_test.loc[len(df_test.index)] = [s, df[(df['Категория']==s)&(df['status']==stat)&(df['Пол']==gender)].shape[0]]
    # if ((status != 'All') & (gender != 'All')):
    #     for s in value:
    #         df_test.loc[len(df_test.index)] = [s, df[(df['Категория']==s)&(df['Пол']==gender)&(df['status']==stat)].shape[0]]
    fig = go.Figure()
    fig = px.pie(df_test, values='Sum', names='Name', title='Количество участников по категориям', hole=0.3)
    fig.update_traces(textinfo='value', hoverinfo='percent')
    return fig

@callback(
    Output('comp_graph2','figure'),
    Input('competence2','value'),    
    Input('status2','value'),
    Input('sex2','value')
)
def update_comp(value, status, sex):
    df_test = pd.DataFrame(columns=['Name','Sum'])
    stat = 'All'
    gender = 'All'
    if (status != 'Все'):
        if (status == 'Команда'):
            stat = 't'
        elif (status == 'Одиночка'):
            stat = 's'
    if (sex != 'Все'):
        if (sex == 'Мужской'):
            gender = 0
        elif (sex == 'Женский'):
            gender = 1
    if ((stat == 'All') & (gender == 'All')):
        for s in value:
            df_test.loc[len(df_test.index)] = [s, df[df['Список компетенций']==s].shape[0]]
    if (stat != 'All'):
        if (gender == 'All'):
            for s in value:
                df_test.loc[len(df_test.index)] = [s, df[(df['Список компетенций']==s)&(df['status']==stat)].shape[0]]
        else:
            for s in value:
                df_test.loc[len(df_test.index)] = [s, df[(df['Список компетенций']==s)&(df['status']==stat)&(df['Пол']==gender)].shape[0]]
    if (gender != 'All'):
        if (stat == 'All'):
            for s in value:
                df_test.loc[len(df_test.index)] = [s, df[(df['Список компетенций']==s)&(df['Пол']==gender)].shape[0]]
        else:
            for s in value:
                df_test.loc[len(df_test.index)] = [s, df[(df['Список компетенций']==s)&(df['status']==stat)&(df['Пол']==gender)].shape[0]]
    fig = go.Figure()
    fig = px.pie(df_test, values='Sum', names='Name', title='Количество участников по компетенциям', hole=0.3)
    fig.update_traces(textinfo='value')
    return fig

@callback(
    Output('edu_graph2', 'figure'),
    Input('education2', 'value'),
    Input('status2','value'),
    Input('sex2','value')
)
def update_edu(value, status, sex):
    df_test = pd.DataFrame(columns=['Name','Sum'])
    stat = 'All'
    gender = 'All'
    if (status != 'Все'):
        if (status == 'Команда'):
            stat = 't'
        elif (status == 'Одиночка'):
            stat = 's'
    if (sex != 'Все'):
        if (sex == 'Мужской'):
            gender = 0
        elif (sex == 'Женский'):
            gender = 1
    if ((stat == 'All') & (gender == 'All')):
        for s in value:
            df_test.loc[len(df_test.index)] = [s, df[df['Образование']==s].shape[0]]
    if (stat != 'All'):
        if (gender == 'All'):
            for s in value:
                df_test.loc[len(df_test.index)] = [s, df[(df['Образование']==s)&(df['status']==stat)].shape[0]]
        else:
            for s in value:
                df_test.loc[len(df_test.index)] = [s, df[(df['Образование']==s)&(df['status']==stat)&(df['Пол']==gender)].shape[0]]
    if (gender != 'All'):
        if (stat == 'All'):
            for s in value:
                df_test.loc[len(df_test.index)] = [s, df[(df['Образование']==s)&(df['Пол']==gender)].shape[0]]
        else:
            for s in value:
                df_test.loc[len(df_test.index)] = [s, df[(df['Образование']==s)&(df['status']==stat)&(df['Пол']==gender)].shape[0]]
    fig = go.Figure()
    fig = px.pie(df_test, values='Sum', names='Name', title='Количество участников по образованию', hole=0.3)
    fig.update_traces(textinfo='value')
    return fig

@callback(
    Output('prof_graph2', 'figure'),
    Input('prof2', 'value'),
    Input('status2','value'),
    Input('sex2','value')

)
def update_prof(value, status, sex):
    df_test = pd.DataFrame(columns=['Name','Sum'])
    stat = 'All'
    gender = 'All'
    if (status != 'Все'):
        if (status == 'Команда'):
            stat = 't'
        elif (status == 'Одиночка'):
            stat = 's'
    if (sex != 'Все'):
        if (sex == 'Мужской'):
            gender = 0
        elif (sex == 'Женский'):
            gender = 1
    if ((stat == 'All') & (gender == 'All')):
        for s in value:
            df_test.loc[len(df_test.index)] = [s, df[df['Профессия']==s].shape[0]]
    if (stat != 'All'):
        if (gender == 'All'):
            for s in value:
                df_test.loc[len(df_test.index)] = [s, df[(df['Профессия']==s)&(df['status']==stat)].shape[0]]
        else:
            for s in value:
                df_test.loc[len(df_test.index)] = [s, df[(df['Профессия']==s)&(df['status']==stat)&(df['Пол']==gender)].shape[0]]
    if (gender != 'All'):
        if (stat == 'All'):
            for s in value:
                df_test.loc[len(df_test.index)] = [s, df[(df['Профессия']==s)&(df['Пол']==gender)].shape[0]]
        else:
            for s in value:
                df_test.loc[len(df_test.index)] = [s, df[(df['Профессия']==s)&(df['status']==stat)&(df['Пол']==gender)].shape[0]]
    fig = go.Figure()
    fig = px.pie(df_test, values='Sum', names='Name', title='Количество участников по профессии', hole=0.3)
    fig.update_traces(textinfo='value')
    return fig

# @callback(
#     Output('asd', 'children'),
#     Input('dropdown-selection', 'value')
# )
# def generate_table(value, max_rows=1000):
#     dff = pd.DataFrame()
#     for s in value:
#         dff = dff.append([df[df.country==s]['country'], df[df.country==s]['year'], df[df.country==s]['pop']], ignore_index=True)
#     dff = dff.T
#     return html.Table([
#         html.Thead(
#             html.Tr([html.Th(col) for col in dff.columns])
#         ),
#         html.Tbody([
#             html.Tr([
#                 html.Td(dff.iloc[i][col]) for col in dff.columns
#             ]) for i in range(min(len(dff), max_rows))
#         ])
#     ])

if __name__ == '__main__':
    app.run_server(debug=True)