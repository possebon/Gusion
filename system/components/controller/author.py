# Python Standard Libraries
#
# External Libraries
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
# Components
#   Model
from system.components.model.author import get_author_data_db, get_papers_by_author_db
#   Controller 
from system.components.controller.nlp_tools import topic_modelling
# Get plot author
def get_plot_author(name):
    author = get_author_data_db(name)
    idx = author[0]
    name = author[1]
    affiliation = author[2]
    citedby = author[3]
    cites_by_year = eval(author[4])
    email = author[5]
    url_picture = author[6]
    if url_picture == "URL picture not available":
        url_picture = "./assets/user-empty.png"
    interests = author[7] 
    # Figure cites by year
    x = list(cites_by_year.keys())
    y = list(cites_by_year.values())
    fig = go.Figure(go.Bar(x=x, y=y))
    # Get papers by author
    papers = get_papers_by_author_db(idx)
    abstracts = []
    for paper in papers:
        abstracts.append(paper[2])
    topics = topic_modelling(abstracts)
    # Plot layout
    if author != []:
        plot = html.Div([
                    dcc.Tabs([
                        dcc.Tab(
                            html.Div([
                                html.Div([
                                    html.Img(src=url_picture),
                                ],id="author-picture"),
                                html.Div([
                                    html.H4(name),
                                    html.H5(affiliation),
                                    html.P(email),
                                    html.P(f"Cites: {citedby}"),
                                    html.P(f"Interests: {interests}")
                                ], id="author-data")
                            ], className="row"), label="Data"
                        ),
                        dcc.Tab(
                            html.Div([
                                dcc.Graph(figure=fig, config={ 'displayModeBar': False}, responsive=True)
                            ]), label="Cited by year"
                        ),
                        dcc.Tab(
                            html.Div([
                                html.Iframe(srcDoc=str(topics), id="iframe-topic")
                            ], id="topic-div"), label="Topic Modelling"
                        )
                    ])
        ])
        return plot
    else:
        return None
    
    