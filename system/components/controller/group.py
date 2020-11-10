# Python Standard Libraries
#
# External Libraries
import dash_table
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import pandas as pd
# Components
#   Model
from system.components.model.author import get_author_data_db, get_papers_by_author_db
#   Controller 
from system.components.controller.nlp_tools import topic_modelling, common_words, common_bigrams, common_speech_tagging
# Get plot group
def get_plot_group(names):
    print("heey")
    authors = []
    for author in names:
        data = get_author_data_db(author)
        authors.append(data)
        
    idx = [author[0] for author in authors]
    name = [author[1]+"\n" for author in authors]
    affiliation = [author[2]+"\n" for author in authors]
    citedby = sum([author[3] for author in authors])
    cites_by_year = [eval(author[4]) for author in authors]
    email = [author[5]+"\n" for author in authors]
    url_picture = [author[6] for author in authors]
    if url_picture == "URL picture not available":
        url_picture = "./assets/user-empty.png"
    interests = [author[7]+"\n" for author in authors]
    # Figure cites by year
    x = [list(cite_by_year.keys()) for cite_by_year in cites_by_year]
    y = [list(cite_by_year.values()) for cite_by_year in cites_by_year]
    fig_cites_year = go.Figure(go.Bar(x=x, y=y))
    fig_cites_year.update_layout(margin=dict(l=0, r=0, t=5, b=0), xaxis_title="Year", yaxis_title="Cites")
    # Get papers by author
    papers = []
    papers_ = [get_papers_by_author_db(idx_) for idx_ in idx]
    for i in range(len(idx)):
        papers.extend(papers_[i])
    # Papers datatable
    df_papers = pd.DataFrame.from_records(papers)
    df_papers.columns = ["ID", "Title", "Abstract", "Authors", "Year", "Cites", "Journal", "Publisher", "j", "z"]
    df_papers = df_papers.drop(["j", "z"], axis=1)
    table = dash_table.DataTable(
            id="table",
            style_table={
                'overflowY': 'auto',
                'overflowX': 'auto',
                'height': "75vh"
            },
            tooltip_data=[
                {
                    column: {'value': str(value)}
                    for column, value in row.items()
                } for row in df_papers.to_dict('rows')
            ],
            tooltip_duration=None,
            style_cell={
                'whiteSpace': 'normal',
                "word-break": "break-word",
                'height': 'auto',
                'minWidth': '10px', 'width': '90px', 'maxWidth': '200px',
            },
            data=df_papers.to_dict("rows"),
            columns=[{"name": i, "id": i} for i in df_papers.columns],
            
            style_data_conditional=[  
                {
                    'if': {'row_index': 'odd'},
                    'backgroundColor': 'rgb(248, 248, 248)'
                }
            ],
            
            style_cell_conditional=[
                {
                    'if': {'column_id': 'Abstract'},
                    'width': '30%'
                },
                {
                    'if': {'column_id': 'ID'},
                    'width': '5%'
                },
                {
                    'if': {'column_id': 'Title'},
                    'width': '10%'
                },
                {
                    'if': {'column_id': 'Year'},
                    'width': '5%'
                },
                {
                    'if': {'column_id': 'Cites'},
                    'width': '5%'
                }
            ],
            
            style_header={
                'backgroundColor': 'rgb(230, 230, 230)',
                'fontWeight': 'bold'
            },
            # To edit elements
            #columns=[{"name": i, "id": i, "editable": False if i == "id" else True} for i in df.columns],
            editable=False,
            row_deletable=False,
            page_size= 10,
        )
    # N papers
    n_papers = len(papers)
    print(n_papers)
    # Get years
    years = []
    for paper in papers:
        years.append(paper[4])
    fig_papers_year = go.Figure(go.Histogram(x=years, xbins=dict(start=1950, end=2021, size=1)))
    fig_papers_year.update_layout(margin=dict(l=0, r=0, t=5, b=0), xaxis_title="Year published", yaxis_title="Papers")
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

    images = [html.Img(src=url_picture_) for url_picture_ in url_picture] 

    # Plot layout
    if author != []:
        plot = html.Div([
                    dcc.Tabs([
                        dcc.Tab(
                            html.Div([
                                html.Br(),
                                html.Div([
                                    html.Div(
                                        images,id="author-picture"
                                    ),
                                    html.Div([
                                        html.H4(name),
                                        html.H5(affiliation),
                                        html.P(email),
                                        html.P(f"Cites: {citedby}"),
                                        html.P(f"Papers published: {n_papers}"),
                                        html.P(f"Cites/Papers: {citedby/n_papers:.3f}"),
                                        html.P(f"Interests: {interests}")
                                    ], id="author-data")
                                ], className="row")
                            ]), label="Description"
                        ),
                        dcc.Tab(
                            html.Div(table),label="Papers"
                        ),
                        dcc.Tab(
                            dcc.Tabs([
                                dcc.Tab(
                                    html.Div([
                                        dcc.Graph(figure=fig_cites_year, config={ 'displayModeBar': False}, responsive=True)
                                    ]), label="Cited by year"
                                ),
                                dcc.Tab(
                                    html.Div([
                                        dcc.Graph(figure=fig_papers_year, config={ 'displayModeBar': False}, responsive=True)
                                    ]), label="Papers by year"
                                ),
                            ]), label = "Year"
                        ),
                        dcc.Tab(
                            html.Div([
                                html.Iframe(srcDoc=str(topics), id="iframe-topic")
                            ], id="topic-div"), label="Topic"
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