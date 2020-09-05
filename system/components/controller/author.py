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
from system.components.controller.nlp_tools import topic_modelling, common_words, common_bigrams, common_speech_tagging
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
    fig_cites_year = go.Figure(go.Bar(x=x, y=y))
    fig_cites_year.update_layout(margin=dict(l=0, r=0, t=5, b=0), xaxis_title="Year", yaxis_title="Cites")
    # Get papers by author
    papers = get_papers_by_author_db(idx)
    # Get abstracts
    abstracts = []
    for paper in papers:
        abstracts.append(paper[2])
    # Topic modelling
    topics = topic_modelling(abstracts)
    # Common words
    words, count_words = common_words(abstracts)
    fig_common_words = go.Figure(go.Bar(x=count_words, y=words, orientation="h"))
    fig_common_words.update_layout(margin=dict(l=0, r=0, t=5, b=0), xaxis_title="Count", yaxis_title="Word")
    # Common bigrams
    bigrams, count_bigrams = common_bigrams(abstracts)
    fig_common_bigrams = go.Figure(go.Bar(x=count_bigrams, y=bigrams, orientation="h"))
    fig_common_bigrams.update_layout(margin=dict(l=0, r=0, t=5, b=0), xaxis_title="Count", yaxis_title="Bigram")
    # Common speech tagging
    tags, count_tags = common_speech_tagging(abstracts)
    fig_common_tags = go.Figure(go.Bar(x=count_tags, y=tags, orientation="h"))
    fig_common_tags.update_layout(margin=dict(l=0, r=0, t=5, b=0), xaxis_title="Count", yaxis_title="Tag")

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
                                dcc.Graph(figure=fig_cites_year, config={ 'displayModeBar': False}, responsive=True)
                            ]), label="Cited by year"
                        ),
                        dcc.Tab(
                            html.Div([
                                html.Iframe(srcDoc=str(topics), id="iframe-topic")
                            ], id="topic-div"), label="Topic Modelling"
                        ),
                        dcc.Tab(
                            dcc.Tabs([
                                dcc.Tab(
                                    html.Div([
                                        dcc.Graph(figure=fig_common_words, config={ 'displayModeBar': False}, responsive=True)
                                    ], id="common-words-div"), label="Words"
                                ),
                                dcc.Tab(
                                    html.Div([
                                        dcc.Graph(figure=fig_common_bigrams, config={ 'displayModeBar': False}, responsive=True)
                                    ], id="common-bigrams-div"), label="Bigrams"
                                ),
                                dcc.Tab(
                                    html.Div([
                                        dcc.Graph(figure=fig_common_tags, config={ 'displayModeBar': False}, responsive=True)
                                    ], id="common-tags-div"), label="Speech Tagging"
                                )
                            ]), label="Frequency"
                        )
                    ])
        ])
        return plot
    else:
        return None
    