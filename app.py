from dash import Dash, html, dcc, callback, Output, Input, dash_table
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

df = pd.read_excel("final2_data2.xlsx")

app = Dash(__name__)

app.layout = html.Div([
    dcc.Tabs([
        dcc.Tab(label='Итоговый балл', children=[
            html.Div(children=[
                html.H2(['Фильтр по типу участия']),
                dcc.RadioItems(['Все','Команда','Одиночка'], id = "status", value = 'Все'),
                html.H2(['Фильтр по полу']),
                dcc.RadioItems(['Все','Мужской','Женский'], id = 'sex', value = 'Все'),
                html.H2(['Интервал по возрасту']),
                dcc.RangeSlider(1, 9, 1, count=1, value=[1, 9], id = 'age')
            ],style={'width':'25%','position':'fixed'}),
            html.Div([
                dcc.Dropdown(df['Категория'].unique(), id = 'categories', value = ['Студент', 'Инженер'], multi=True),
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
                    dcc.RadioItems(['Все','Мужской','Женский'], id = 'sex2', value = 'Все'),
                    html.H2(['Интервал по возрасту']),
                    dcc.RangeSlider(1, 9, 1, count=1, value=[1, 9], id = 'age2')
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
        ]),
        dcc.Tab(label="Интервал по возрасту", children=[
            html.Div(children=[
                    html.H2(['Фильтр по типу участия']),
                    dcc.RadioItems(['Все','Команда','Одиночка'], id = "status3", value = 'Все'),
                    html.H2(['Фильтр по полу']),
                    dcc.RadioItems(['Все','Мужской','Женский'], id = 'sex3', value = 'Все'),
                    html.H2(['Интервал по возрасту']),
                    dcc.RangeSlider(1, 9, 1, count=1, value=[1, 9], id = 'age3')
            ],style={'width':'25%','position':'fixed'}),
            html.Div([
                dcc.Dropdown(df['Категория'].unique(),id = 'categories3', value = ['Студент', 'Инженер'], multi=True),
                dcc.Graph(id='category_graph3'),
                dcc.Dropdown(df['Список компетенций'].unique(), id = "competence3", value = ['Сварочные технологии; ','Инженер-конструктор; '], multi=True),
                dcc.Graph(id='comp_graph3'),     
                dcc.Dropdown(df['Образование'].unique(), id = "education3", value = ['Бакалавриат','Специалитет'], multi=True),
                dcc.Graph(id='edu_graph3'),        
                dcc.Dropdown(df['Профессия'].unique(), id = "prof3", value = ['Промышленная автоматика','Управление качеством'], multi=True),
                dcc.Graph(id='prof_graph3'),
            ], style={'width':'75%', 'marginLeft':'25%'})
        ])
    ])
])

#===================================================================================================================================================
# mean #############################################################################################################################################
#===================================================================================================================================================

@callback(
    Output('category_graph', 'figure'),
    Input('categories', 'value'),
    Input('status','value'),
    Input('sex','value'),
    Input('age', 'value')
)
def update_category(value, status, sex, age):
    dff = pd.DataFrame()
    fig = go.Figure()
    dff = df
    if (status == 'Команда'):
        dff = df[df['comp_stat']=='t']
        if (sex == 'Мужской'):
            dff = dff[dff['Пол']==0]
        elif (sex == 'Женский'):
            dff = dff[dff['Пол']==1]
    elif (status == 'Одиночка'):
        dff = df[df['comp_stat']=='s']
        if (sex == 'Мужской'):
            dff = dff[dff['Пол']==0]
        elif (sex == 'Женский'):
            dff = dff[dff['Пол']==1]
    else:
        if (sex == 'Мужской'):
            dff = df[df['Пол']==0]
        elif (sex == 'Женский'):
            dff = df[df['Пол']==1]
    for s in value:
        dfff = dff[dff['Категория']==s]
        dfff = dfff[(dfff['Интервал по возрасту']>=age[0])&(dfff['Интервал по возрасту']<=age[1])]
        fig.add_trace(go.Histogram(x=dfff['Категория'], y=dfff['summary_rez'], name=s, texttemplate="%{y}", histfunc='avg'))
        fig.update_layout(xaxis_title = "Категория", yaxis_title='Средний балл', title='Гистограмма распределения среднего балла по категориям')
        # dff = dff.append(df[df.country==s], ignore_index=True)
    return fig

@callback(
    Output('comp_graph','figure'),
    Input('competence','value'),    
    Input('status','value'),
    Input('sex','value'),
    Input('age', 'value')
)
def update_comp(value, status, sex, age):
    dff = pd.DataFrame()
    fig = go.Figure()
    dff = df
    if (status == 'Команда'):
        dff = df[df['comp_stat']=='t']
        if (sex == 'Мужской'):
            dff = dff[dff['Пол']==0]
        elif (sex == 'Женский'):
            dff = dff[dff['Пол']==1]
    elif (status == 'Одиночка'):
        dff = df[df['comp_stat']=='s']
        if (sex == 'Мужской'):
            dff = dff[dff['Пол']==0]
        elif (sex == 'Женский'):
            dff = dff[dff['Пол']==1]
    else:
        if (sex == 'Мужской'):
            dff = df[df['Пол']==0]
        elif (sex == 'Женский'):
            dff = df[df['Пол']==1]
    for s in value:
        dfff = dff[dff['Список компетенций']==s]
        dfff = dfff[(dfff['Интервал по возрасту']>=age[0])&(dfff['Интервал по возрасту']<=age[1])]
        fig.add_trace(go.Histogram(x=dfff['Список компетенций'], y=dfff['summary_rez'], name=s, texttemplate="%{y}", histfunc='avg'))
        fig.update_layout(xaxis_title = "Компетенция", yaxis_title='Средний балл', title='Гистограмма распределения среднего балла по компетенциям')
    return fig

@callback(
    Output('edu_graph', 'figure'),
    Input('education', 'value'),
    Input('status','value'),
    Input('sex','value'),
    Input('age', 'value')
)
def update_edu(value, status, sex, age):
    dff = pd.DataFrame()
    fig = go.Figure()
    dff = df
    if (status == 'Команда'):
        dff = df[df['comp_stat']=='t']
        if (sex == 'Мужской'):
            dff = dff[dff['Пол']==0]
        elif (sex == 'Женский'):
            dff = dff[dff['Пол']==1]
    elif (status == 'Одиночка'):
        dff = df[df['comp_stat']=='s']
        if (sex == 'Мужской'):
            dff = dff[dff['Пол']==0]
        elif (sex == 'Женский'):
            dff = dff[dff['Пол']==1]
    else:
        if (sex == 'Мужской'):
            dff = df[df['Пол']==0]
        elif (sex == 'Женский'):
            dff = df[df['Пол']==1]
    for s in value:
        dfff = dff[dff['Образование']==s]
        dfff = dfff[(dfff['Интервал по возрасту']>=age[0])&(dfff['Интервал по возрасту']<=age[1])]
        fig.add_trace(go.Histogram(x=dfff['Образование'], y=dfff['summary_rez'], name=s, texttemplate="%{y}", histfunc='avg'))
        fig.update_layout(xaxis_title = "Образование", yaxis_title='Средний  балл', title='Гистограмма распределения среднего балла по образованию')
    return fig

@callback(
    Output('prof_graph', 'figure'),
    Input('prof', 'value'),
    Input('status','value'),
    Input('sex','value'),
    Input('age', 'value')

)
def update_prof(value, status, sex, age):
    dff = pd.DataFrame()
    fig = go.Figure()
    dff = df
    if (status == 'Команда'):
        dff = df[df['comp_stat']=='t']
        if (sex == 'Мужской'):
            dff = dff[dff['Пол']==0]
        elif (sex == 'Женский'):
            dff = dff[dff['Пол']==1]
    elif (status == 'Одиночка'):
        dff = df[df['comp_stat']=='s']
        if (sex == 'Мужской'):
            dff = dff[dff['Пол']==0]
        elif (sex == 'Женский'):
            dff = dff[dff['Пол']==1]
    else:
        if (sex == 'Мужской'):
            dff = df[df['Пол']==0]
        elif (sex == 'Женский'):
            dff = df[df['Пол']==1]
    for s in value:
        dfff = dff[dff['Профессия']==s]
        dfff = dfff[(dfff['Интервал по возрасту']>=age[0])&(dfff['Интервал по возрасту']<=age[1])]
        fig.add_trace(go.Histogram(x=dfff['Профессия'], y=dfff['summary_rez'], name=s, texttemplate="%{y}", histfunc='avg'))
        fig.update_layout(xaxis_title = "Профессия", yaxis_title='Средний балл', title='Гистограмма распределения среднего балла по профессиям')
    return fig

#===================================================================================================================================================
# count ############################################################################################################################################
#===================================================================================================================================================

@callback(
    Output('category_graph2', 'figure'),
    Input('categories2', 'value'),
    Input('status2','value'),
    Input('sex2','value'),
    Input('age2', 'value')
)
def update_category(value, status, sex, age):
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
            df_test.loc[len(df_test.index)] = [s, df[(df['Категория']==s) & (df['Интервал по возрасту']>=age[0])&(df['Интервал по возрасту']<=age[1])].shape[0]]
        fig = go.Figure()
        fig = px.pie(df_test, values='Sum', names='Name', title='Количество участников по категориям', hole=0.3)
        fig.update_traces(textinfo='value', hoverinfo='percent')
        return fig
    if (stat != 'All'):
        if (gender == 'All'):
            for s in value:
                df_test.loc[len(df_test.index)] = [s, df[(df['Категория']==s)&(df['comp_stat']==stat) & (df['Интервал по возрасту']>=age[0])&(df['Интервал по возрасту']<=age[1])].shape[0]]
            fig = go.Figure()
            fig = px.pie(df_test, values='Sum', names='Name', title='Количество участников по категориям', hole=0.3)
            fig.update_traces(textinfo='value', hoverinfo='percent')
            return fig
        else:
            for s in value:
                df_test.loc[len(df_test.index)] = [s, df[(df['Категория']==s)&(df['comp_stat']==stat)&(df['Пол']==gender) & (df['Интервал по возрасту']>=age[0])&(df['Интервал по возрасту']<=age[1])].shape[0]]
            fig = go.Figure()
            fig = px.pie(df_test, values='Sum', names='Name', title='Количество участников по категориям', hole=0.3)
            fig.update_traces(textinfo='value', hoverinfo='percent')
        return fig
    if (gender != 'All'):
        if (stat == 'All'):
            for s in value:
                df_test.loc[len(df_test.index)] = [s, df[(df['Категория']==s)&(df['Пол']==gender) & (df['Интервал по возрасту']>=age[0])&(df['Интервал по возрасту']<=age[1])].shape[0]]
            fig = go.Figure()
            fig = px.pie(df_test, values='Sum', names='Name', title='Количество участников по категориям', hole=0.3)
            fig.update_traces(textinfo='value', hoverinfo='percent')
            return fig
        else:
            for s in value:
                df_test.loc[len(df_test.index)] = [s, df[(df['Категория']==s)&(df['comp_stat']==stat)&(df['Пол']==gender) & (df['Интервал по возрасту']>=age[0])&(df['Интервал по возрасту']<=age[1])].shape[0]]
            fig = go.Figure()
            fig = px.pie(df_test, values='Sum', names='Name', title='Количество участников по категориям', hole=0.3)
            fig.update_traces(textinfo='value', hoverinfo='percent')
            return fig

@callback(
    Output('comp_graph2','figure'),
    Input('competence2','value'),    
    Input('status2','value'),
    Input('sex2','value'),
    Input('age2', 'value')
)
def update_comp(value, status, sex, age):
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
            df_test.loc[len(df_test.index)] = [s, df[(df['Список компетенций']==s) & (df['Интервал по возрасту']>=age[0])&(df['Интервал по возрасту']<=age[1])].shape[0]]
        fig = go.Figure()
        fig = px.pie(df_test, values='Sum', names='Name', title='Количество участников по компетенциям', hole=0.3)
        fig.update_traces(textinfo='value', hoverinfo='percent')
        return fig
    if (stat != 'All'):
        if (gender == 'All'):
            for s in value:
                df_test.loc[len(df_test.index)] = [s, df[(df['Список компетенций']==s)&(df['comp_stat']==stat) & (df['Интервал по возрасту']>=age[0])&(df['Интервал по возрасту']<=age[1])].shape[0]]
            fig = go.Figure()
            fig = px.pie(df_test, values='Sum', names='Name', title='Количество участников по компетенциям', hole=0.3)
            fig.update_traces(textinfo='value', hoverinfo='percent')
            return fig
        else:
            for s in value:
                df_test.loc[len(df_test.index)] = [s, df[(df['Список компетенций']==s)&(df['comp_stat']==stat)&(df['Пол']==gender) & (df['Интервал по возрасту']>=age[0])&(df['Интервал по возрасту']<=age[1])].shape[0]]
            fig = go.Figure()
            fig = px.pie(df_test, values='Sum', names='Name', title='Количество участников по компетенциям', hole=0.3)
            fig.update_traces(textinfo='value', hoverinfo='percent')
        return fig
    if (gender != 'All'):
        if (stat == 'All'):
            for s in value:
                df_test.loc[len(df_test.index)] = [s, df[(df['Список компетенций']==s)&(df['Пол']==gender) & (df['Интервал по возрасту']>=age[0])&(df['Интервал по возрасту']<=age[1])].shape[0]]
            fig = go.Figure()
            fig = px.pie(df_test, values='Sum', names='Name', title='Количество участников по компетенциям', hole=0.3)
            fig.update_traces(textinfo='value', hoverinfo='percent')
            return fig
        else:
            for s in value:
                df_test.loc[len(df_test.index)] = [s, df[(df['Список компетенций']==s)&(df['comp_stat']==stat)&(df['Пол']==gender) & (df['Интервал по возрасту']>=age[0])&(df['Интервал по возрасту']<=age[1])].shape[0]]
            fig = go.Figure()
            fig = px.pie(df_test, values='Sum', names='Name', title='Количество участников по компетенциям', hole=0.3)
            fig.update_traces(textinfo='value', hoverinfo='percent')
            return fig

@callback(
    Output('edu_graph2', 'figure'),
    Input('education2', 'value'),
    Input('status2','value'),
    Input('sex2','value'),
    Input('age2', 'value')
)
def update_edu(value, status, sex, age):
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
            df_test.loc[len(df_test.index)] = [s, df[(df['Образование']==s) & (df['Интервал по возрасту']>=age[0])&(df['Интервал по возрасту']<=age[1])].shape[0]]
        fig = go.Figure()
        fig = px.pie(df_test, values='Sum', names='Name', title='Количество участников по образованию', hole=0.3)
        fig.update_traces(textinfo='value', hoverinfo='percent')
        return fig
    if (stat != 'All'):
        if (gender == 'All'):
            for s in value:
                df_test.loc[len(df_test.index)] = [s, df[(df['Образование']==s)&(df['comp_stat']==stat) & (df['Интервал по возрасту']>=age[0])&(df['Интервал по возрасту']<=age[1])].shape[0]]
            fig = go.Figure()
            fig = px.pie(df_test, values='Sum', names='Name', title='Количество участников по образованию', hole=0.3)
            fig.update_traces(textinfo='value', hoverinfo='percent')
            return fig
        else:
            for s in value:
                df_test.loc[len(df_test.index)] = [s, df[(df['Образование']==s)&(df['comp_stat']==stat)&(df['Пол']==gender) & (df['Интервал по возрасту']>=age[0])&(df['Интервал по возрасту']<=age[1])].shape[0]]
            fig = go.Figure()
            fig = px.pie(df_test, values='Sum', names='Name', title='Количество участников по образованию', hole=0.3)
            fig.update_traces(textinfo='value', hoverinfo='percent')
        return fig
    if (gender != 'All'):
        if (stat == 'All'):
            for s in value:
                df_test.loc[len(df_test.index)] = [s, df[(df['Образование']==s)&(df['Пол']==gender) & (df['Интервал по возрасту']>=age[0])&(df['Интервал по возрасту']<=age[1])].shape[0]]
            fig = go.Figure()
            fig = px.pie(df_test, values='Sum', names='Name', title='Количество участников по образованию', hole=0.3)
            fig.update_traces(textinfo='value', hoverinfo='percent')
            return fig
        else:
            for s in value:
                df_test.loc[len(df_test.index)] = [s, df[(df['Образование']==s)&(df['comp_stat']==stat)&(df['Пол']==gender) & (df['Интервал по возрасту']>=age[0])&(df['Интервал по возрасту']<=age[1])].shape[0]]
            fig = go.Figure()
            fig = px.pie(df_test, values='Sum', names='Name', title='Количество участников по образованию', hole=0.3)
            fig.update_traces(textinfo='value', hoverinfo='percent')
            return fig

@callback(
    Output('prof_graph2', 'figure'),
    Input('prof2', 'value'),
    Input('status2','value'),
    Input('sex2','value'),
    Input('age2', 'value')

)
def update_prof(value, status, sex, age):
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
            df_test.loc[len(df_test.index)] = [s, df[(df['Профессия']==s) & (df['Интервал по возрасту']>=age[0])&(df['Интервал по возрасту']<=age[1])].shape[0]]
        fig = go.Figure()
        fig = px.pie(df_test, values='Sum', names='Name', title='Количество участников по профессии', hole=0.3)
        fig.update_traces(textinfo='value', hoverinfo='percent')
        return fig
    if (stat != 'All'):
        if (gender == 'All'):
            for s in value:
                df_test.loc[len(df_test.index)] = [s, df[(df['Профессия']==s)&(df['comp_stat']==stat) & (df['Интервал по возрасту']>=age[0])&(df['Интервал по возрасту']<=age[1])].shape[0]]
            fig = go.Figure()
            fig = px.pie(df_test, values='Sum', names='Name', title='Количество участников по профессии', hole=0.3)
            fig.update_traces(textinfo='value', hoverinfo='percent')
            return fig
        else:
            for s in value:
                df_test.loc[len(df_test.index)] = [s, df[(df['Профессия']==s)&(df['comp_stat']==stat)&(df['Пол']==gender) & (df['Интервал по возрасту']>=age[0])&(df['Интервал по возрасту']<=age[1])].shape[0]]
            fig = go.Figure()
            fig = px.pie(df_test, values='Sum', names='Name', title='Количество участников по профессии', hole=0.3)
            fig.update_traces(textinfo='value', hoverinfo='percent')
        return fig
    if (gender != 'All'):
        if (stat == 'All'):
            for s in value:
                df_test.loc[len(df_test.index)] = [s, df[(df['Профессия']==s)&(df['Пол']==gender) & (df['Интервал по возрасту']>=age[0])&(df['Интервал по возрасту']<=age[1])].shape[0]]
            fig = go.Figure()
            fig = px.pie(df_test, values='Sum', names='Name', title='Количество участников по профессии', hole=0.3)
            fig.update_traces(textinfo='value', hoverinfo='percent')
            return fig
        else:
            for s in value:
                df_test.loc[len(df_test.index)] = [s, df[(df['Профессия']==s)&(df['comp_stat']==stat)&(df['Пол']==gender) & (df['Интервал по возрасту']>=age[0])&(df['Интервал по возрасту']<=age[1])].shape[0]]
            fig = go.Figure()
            fig = px.pie(df_test, values='Sum', names='Name', title='Количество участников по профессии', hole=0.3)
            fig.update_traces(textinfo='value', hoverinfo='percent')
            return fig

#===================================================================================================================================================
# age_group ########################################################################################################################################
#===================================================================================================================================================

@callback(
    Output('comp_graph3', 'figure'),
    Input('competence3', 'value'),
    Input('status3','value'),
    Input('sex3','value'),
    Input('age3', 'value')
)

def age_cat(value, status, sex, age):
    df_test = df[(df['Интервал по возрасту']>=age[0])&(df['Интервал по возрасту']<=age[1])]
    dff = df[(df['Интервал по возрасту']>=age[0])&(df['Интервал по возрасту']<=age[1])]
    fig = go.Figure()
    if (status == 'Команда'):
        dff = df[df['comp_stat']=='t']
        if (sex == 'Мужской'):
            dff = dff[dff['Пол']==0]
        elif (sex == 'Женский'):
            dff = dff[dff['Пол']==1]
    elif (status == 'Одиночка'):
        dff = df[df['comp_stat']=='s']
        if (sex == 'Мужской'):
            dff = dff[dff['Пол']==0]
        elif (sex == 'Женский'):
            dff = dff[dff['Пол']==1]
    else:
        if (sex == 'Мужской'):
            dff = df[df['Пол']==0]
        elif (sex == 'Женский'):
            dff = df[df['Пол']==1]
    for s in value:
        dfff = dff[dff['Список компетенций']==s]
        new_df = dfff.groupby('Интервал по возрасту')['ФИО'].count()
        new_df2 = dfff.groupby('Интервал по возрасту')['summary_rez'].mean()
        fig.add_trace(go.Histogram(x=dfff['Текущий возраст'], y=dfff['summary_rez'], name=(s  + " ср. балл"), texttemplate="Ср. балл: %{x}"))
        # fig.add_trace(go.Histogram(x=new_df.index.values, y=new_df.values.tolist(), name=(s + " кол."), texttemplate="Участники: %{y}"))
    fig.update_layout(xaxis_title = "Номер интервала", yaxis_title='Показатели', title='Гистограмма распределения показателей участников по возрасту')
    return fig

@callback(
    Output('edu_graph3', 'figure'),
    Input('education3', 'value'),
    Input('status3','value'),
    Input('sex3','value'),
    Input('age3', 'value')
)

def age_cat(value, status, sex, age):
    df_test = df[(df['Интервал по возрасту']>=age[0])&(df['Интервал по возрасту']<=age[1])]
    dff = df[(df['Интервал по возрасту']>=age[0])&(df['Интервал по возрасту']<=age[1])]
    fig = go.Figure()
    if (status == 'Команда'):
        dff = df[df['comp_stat']=='t']
        if (sex == 'Мужской'):
            dff = dff[dff['Пол']==0]
        elif (sex == 'Женский'):
            dff = dff[dff['Пол']==1]
    elif (status == 'Одиночка'):
        dff = df[df['comp_stat']=='s']
        if (sex == 'Мужской'):
            dff = dff[dff['Пол']==0]
        elif (sex == 'Женский'):
            dff = dff[dff['Пол']==1]
    else:
        if (sex == 'Мужской'):
            dff = df[df['Пол']==0]
        elif (sex == 'Женский'):
            dff = df[df['Пол']==1]
    for s in value:
        dfff = dff[dff['Образование']==s]
        new_df = dfff.groupby('Интервал по возрасту')['ФИО'].count()
        new_df2 = dfff.groupby('Интервал по возрасту')['summary_rez'].mean()
        fig.add_trace(go.Histogram(x=dfff['Текущий возраст'], y=dfff['summary_rez'], name=(s  + " ср. балл"), texttemplate="Ср. балл: %{x}"))
        # fig.add_trace(go.Histogram(x=new_df.index.values, y=new_df.values.tolist(), name=(s + " кол."), texttemplate="Участники: %{y}"))
    fig.update_layout(xaxis_title = "Номер интервала", yaxis_title='Показатели', title='Гистограмма распределения показателей участников по возрасту')
    return fig

@callback(
    Output('prof_graph3', 'figure'),
    Input('prof3', 'value'),
    Input('status3','value'),
    Input('sex3','value'),
    Input('age3', 'value')
)

def age_cat(value, status, sex, age):
    df_test = df[(df['Интервал по возрасту']>=age[0])&(df['Интервал по возрасту']<=age[1])]
    dff = df[(df['Интервал по возрасту']>=age[0])&(df['Интервал по возрасту']<=age[1])]
    fig = go.Figure()
    if (status == 'Команда'):
        dff = df[df['comp_stat']=='t']
        if (sex == 'Мужской'):
            dff = dff[dff['Пол']==0]
        elif (sex == 'Женский'):
            dff = dff[dff['Пол']==1]
    elif (status == 'Одиночка'):
        dff = df[df['comp_stat']=='s']
        if (sex == 'Мужской'):
            dff = dff[dff['Пол']==0]
        elif (sex == 'Женский'):
            dff = dff[dff['Пол']==1]
    else:
        if (sex == 'Мужской'):
            dff = df[df['Пол']==0]
        elif (sex == 'Женский'):
            dff = df[df['Пол']==1]
    for s in value:
        dfff = dff[dff['Профессия']==s]
        new_df = dfff.groupby('Интервал по возрасту')['ФИО'].count()
        new_df2 = dfff.groupby('Интервал по возрасту')['summary_rez'].mean()
        fig.add_trace(go.Histogram(x=dfff['Текущий возраст'], y=dfff['summary_rez'], name=(s  + " ср. балл"), texttemplate="Ср. балл: %{x}"))
        # fig.add_trace(go.Histogram(x=new_df.index.values, y=new_df.values.tolist(), name=(s + " кол."), texttemplate="Участники: %{y}"))
    fig.update_layout(xaxis_title = "Номер интервала", yaxis_title='Показатели', title='Гистограмма распределения показателей участников по возрасту')
    return fig

@callback(
    Output('category_graph3', 'figure'),
    Input('categories3', 'value'),
    Input('status3','value'),
    Input('sex3','value'),
    Input('age3', 'value')
)

def age_cat(value, status, sex, age):
    df_test = df[(df['Интервал по возрасту']>=age[0])&(df['Интервал по возрасту']<=age[1])]
    dff = df[(df['Интервал по возрасту']>=age[0])&(df['Интервал по возрасту']<=age[1])]
    fig = go.Figure()
    if (status == 'Команда'):
        dff = df[df['comp_stat']=='t']
        if (sex == 'Мужской'):
            dff = dff[dff['Пол']==0]
        elif (sex == 'Женский'):
            dff = dff[dff['Пол']==1]
    elif (status == 'Одиночка'):
        dff = df[df['comp_stat']=='s']
        if (sex == 'Мужской'):
            dff = dff[dff['Пол']==0]
        elif (sex == 'Женский'):
            dff = dff[dff['Пол']==1]
    else:
        if (sex == 'Мужской'):
            dff = df[df['Пол']==0]
        elif (sex == 'Женский'):
            dff = df[df['Пол']==1]
    for s in value:
        dfff = dff[dff['Категория']==s]
        new_df = dfff.groupby('Интервал по возрасту')['ФИО'].count()
        new_df2 = dfff.groupby('Интервал по возрасту')['summary_rez'].mean()
        fig.add_trace(go.Histogram(x=dfff['Текущий возраст'], y=dfff['summary_rez'], name=(s  + " ср. балл"), texttemplate="Ср. балл: %{x}"))
        # fig.add_trace(go.Histogram(x=new_df.index.values, y=new_df.values.tolist(), name=(s + " кол."), texttemplate="Участники: %{y}"))
    fig.update_layout(xaxis_title = "Номер интервала", yaxis_title='Показатели', title='Гистограмма распределения показателей участников по возрасту')
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)