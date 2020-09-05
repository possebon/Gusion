# Python Standard Libraries
#
# External Libraries
import numpy as np
import igraph as ig
import chart_studio.plotly as py
import plotly.graph_objs as go
import dash_core_components as dcc
# Components
#   Model
from system.components.model.graph import get_graph_db
# Graph
def graph():
    nodes, links = get_graph_db()  
    N=len(nodes)
    L=len(links)
    Edges=[(links[k]['source'], links[k]['target']) for k in range(L)]
    # Graph
    G=ig.Graph(Edges, directed=True)
    # Getting name and group
    labels=[]
    group=[]
    for node in nodes:
        labels.append(node['name'])
        group.append(node['group'])
    # Layout style
    layt=G.layout_fruchterman_reingold(grid=True,dim=3)
    # Getting coordinates
    Xn=[layt[k][0] for k in range(N)]# x-coordinates of nodes
    Yn=[layt[k][1] for k in range(N)]# y-coordinates
    Zn=[layt[k][2] for k in range(N)]# z-coordinates 
    Xe=[]
    Ye=[]
    Ze=[]
    for e in Edges:
        Xe+=[layt[e[0]][0],layt[e[1]][0], None]
        Ye+=[layt[e[0]][1],layt[e[1]][1], None]
        Ze+=[layt[e[0]][2],layt[e[1]][2], None]
    # Traces
    trace1=go.Scatter3d(x=Xe,
                y=Ye,
                z=Ze,
                mode='lines',
                line=dict(color='rgb(125,125,125)', width=1),
                hoverinfo='skip',
                )
    trace2=go.Scatter3d(x=Xn,
                y=Yn,
                z=Zn,
                mode='markers',
                name='actors',
                opacity=1,
                marker=dict(symbol='circle',
                                size=4,
                                color=group,
                                colorscale='haline',
                                line=dict(color='rgb(50,50,50)', width=0.5)
                                ),
                text= labels,
                hoverinfo='text'
                )
    # Layout figure
    axis=dict(showbackground=False,
            showline=False,
            zeroline=False,
            showgrid=False,
            showticklabels=False,
            title=''
            )
    layout = go.Layout(
            title="Authors",
            showlegend=False,
            scene=dict(
                xaxis=dict(axis),
                yaxis=dict(axis),
                zaxis=dict(axis),
            ),
        margin=dict(l=0, r=0, t=0, b=0),
        hovermode='closest',  
        hoverlabel = dict(
            bgcolor = 'white'
        )
    )
    data=[trace1, trace2]
    fig=go.Figure(data=data, layout=layout)
    fig.update_layout(
        title={
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    autosize=True)
    
    config = {'responsive': True, "displaylogo": False, \
        'modeBarButtonsToRemove': ['pan3d', 'lasso3d', 'zoom3d', 'orbitRotation', 'tableRotation', \
            'resetCameraDefault3d', 'hoverClosest3d', 'resetCameraLastSave3d']}
    graph = dcc.Graph(figure=fig, id="graph", config = config, style={"height": "92vh", "width": "100%"})
    return graph