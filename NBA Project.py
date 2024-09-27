#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import required libraries
import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px
import matplotlib.pyplot as plt

#Read the data into pandas dataframe
first_df = pd.read_csv("/Users/maggie/championsdata.csv")

max_court_home = first_df['Home'].max()
min_court_away = first_df['Home'].min()


# In[2]:


# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('NBA Finals Home Game Advantage Dashboard: 2010 - 2018',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable year selection
                                # The default select value is for ALL teams
                                dcc.Dropdown(
                                    id='team-dropdown',
                                    options=[
                                        {'label': 'All Champion Teams', 'value': 'ALL'},
                                        {'label': 'Lakers', 'value': 'Lakers'},
                                        {'label': 'Mavericks', 'value': 'Mavericks'},
                                        {'label': 'Heat', 'value': 'Heat'},
                                        {'label': 'Spurs', 'value': 'Spurs'},
                                        {'label': 'Warriors', 'value': 'Warriors'},
                                        {'label': 'Cavaliers', 'value': 'Cavaliers'},
                                    ],
                                    value='ALL',
                                    placeholder='Select a champion team here',
                                    searchable=True
                                    ),
                                html.Br(),

                                # TASK 2: Add a pie chart to show the total home court wins count for all teams
                                # If a specific team was selected, show the Win vs. Loss counts for the team at home
                                html.Div(dcc.Graph(id='at-home-win-pie-chart')),
                                html.Br(),
                                
                                # TASK 3: Add a pie chart to show the total away court wins count for all teams
                                # If a specific team was selected, show the Win vs. Loss counts for the team at away
                                html.Div(dcc.Graph(id='at-away-win-pie-chart')),
                                html.Br(),

                                ])

# TASK 2:
# Add a callback function for `team-dropdown` as input, `at-home-win-pie-chart` as output

@app.callback( Output(component_id='at-home-win-pie-chart', component_property='figure'),
               Input(component_id='team-dropdown', component_property='value'))

def get_pie_chart(entered_team):
    filtered_df = first_df
    if entered_team == 'ALL':
        fig = px.pie(first_df, values='Win At Home', names='Team', title='Total Home Court Wins By Team')
        return fig
    else:
        # return the outcomes piechart for a selected team
        filtered_df = first_df[first_df['Team'] == entered_team]
        filtered_df = filtered_df.groupby(['Team', 'Win At Home']).size().reset_index(name='win_count')
        fig = px.pie(filtered_df, values='win_count', names='Win At Home', title=f"Total Home Game Wins for Team {entered_team}")
        return fig

# TASK 3:
# Add a callback function for `team-dropdown` as input, `at-away-win-pie-chart` as output

@app.callback( Output(component_id='at-away-win-pie-chart', component_property='figure'),
               Input(component_id='team-dropdown', component_property='value'))

def get_pie_chart(entered_team):
    filtered_df = first_df
    if entered_team == 'ALL':
        fig = px.pie(first_df, values='Win At Away', names='Team', title='Total Away Court Wins By Team')
        return fig
    else:
        # return the outcomes piechart for a selected team
        filtered_df = first_df[first_df['Team'] == entered_team]
        filtered_df = filtered_df.groupby(['Team', 'Win At Away']).size().reset_index(name='win_count')
        fig = px.pie(filtered_df, values='win_count', names='Win At Away', title=f"Total Away Game Wins for Team {entered_team}")
        return fig

    
# Run the app
if __name__ == '__main__':
    app.run_server()


# In[3]:


second_df = pd.read_csv("/Users/maggie/final_data.csv")
new_df = second_df[second_df['year']>1999]
new_df = new_df[['first','last','year','pts','reb','ast','stl','blk','turnover','fg_pct']]


# In[4]:


new_df.head()


# In[5]:


print(new_df.dtypes)


# In[6]:


stats_df = pd.DataFrame()

for column in new_df:
    if column != 'first' and column != 'last' and column != 'year':
        new_column = new_df.groupby('year')[column].mean()
        if column == 'fg_pct':
            new_column = new_column * 100
        stats_df[f'avg_{column}'] = new_column
        
stats_df.head()


# In[7]:


plt.figure(figsize = (10, 10))
stats_df.plot(kind = 'line', title = 'Stats For All Star Selections')
plt.xlabel = 'Year'
plt.legend(title = 'Statistics', loc = 'center left', bbox_to_anchor = (1, 0.5), fontsize = 'small')
plt.minorticks_on()
plt.grid(which = 'both', axis='both')
plt.grid(which = 'minor', linestyle = ':', linewidth = 0.5)
plt.show()


# In[ ]:




