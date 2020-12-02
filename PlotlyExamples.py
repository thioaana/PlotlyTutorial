import plotly.graph_objects as go
import numpy as np
import math #needed for definition of pi

def plotLegents():
    xpoints = np.arange(0, math.pi*2, 0.05)
    ypoints = np.sin(xpoints)
    zpoints = np.cos(xpoints)

    trace0 = go.Scatter(x = xpoints,
                        y = ypoints,
                        name = "Sin")

    trace1 = go.Scatter(x = xpoints,
                        y = zpoints,
                        name = "Cos")

    layout = go.Layout(title="Sine and Cos Functions",
                       xaxis={"title":"Angle in pi"},
                       yaxis ={"title":"Value"})

    data = [trace0, trace1]
    fig = go.Figure(data=data, layout=layout)
    fig.write_html('first_figure.html', auto_open=True)

def plotAxisAndTicks():
    xpoints = np.arange(0, math.pi * 2, 0.05)
    ypoints = np.sin(xpoints)
    zpoints = np.cos(xpoints)

    trace0 = go.Scatter(x = xpoints,
                        y = ypoints,
                        name = "Sin")

    trace1 = go.Scatter(x = xpoints,
                        y = zpoints,
                        name = "Cos")


    layout = go.Layout(title="Sine and cos",
                       xaxis=dict(
                           title='angle',
                           showgrid=True,
                           gridcolor='#bdbdbd',
                           zeroline=True,
                           showline=True,
                           showticklabels=True,
                           gridwidth=1),
                       yaxis=dict(showgrid=True,
                                  zeroline=True,
                                  showline=True,
                                  gridcolor='#bdbdbd',
                                  gridwidth=2,
                                  zerolinecolor='#969696',
                                  zerolinewidth=2,
                                  linecolor='#636363',
                                  linewidth=2,
                                  title='VALUE',
                                  titlefont=dict(family='Arial, sans-serif',
                                                 size=18,
                                                 color='lightgrey'),
                                  showticklabels=True,
                                  tickangle=45,
                                  tickfont=dict(family='Old Standard TT, serif',
                                                size=14,
                                                color='black'),
                                  tickmode='linear',
                                  tick0=0.0,
                                  dtick=0.25)
                       )

    data = [trace0, trace1]
    fig = go.Figure(data=data, layout=layout)
    fig.write_html('first_figure.html', auto_open=True)

def plotMultipleAxes():
    x = np.arange(1, 11)
    y1 = np.exp(x)
    y2 = np.log(x)

    trace1 = go.Scatter(x=x, y=y1, name='exp')
    trace2 = go.Scatter(x=x, y=y2, name='log', yaxis='y2')
    data = [trace1, trace2]

    layout = go.Layout(title='Double Y Axis Example',
                       yaxis=dict(title='exp',
                                  zeroline=True,
                                  showline=True),
                       yaxis2=dict(title='log',
                                   zeroline=True,
                                   showline=True,
                                   overlaying='y',
                                   side='right')
                       )

    fig = go.Figure(data=data, layout=layout)
    fig.write_html('first_figure.html', auto_open=True)

def plotSubplots():
    from plotly import tools
    x = np.arange(1, 11)
    y1 = np.exp(x)
    y2 = np.log(x)

    trace1 = go.Scatter(x=x, y=y1, name='exp')
    trace2 = go.Scatter(x=x, y=y2, name='log', yaxis='y2')

    fig = tools.make_subplots(rows=1, cols=2)
    fig.append_trace(trace1, 1, 1)
    fig.append_trace(trace2, 1, 2)
    fig['layout'].update(height=600, width=800, title='subplot')
    fig.write_html('first_figure.html', auto_open=True)

def plotInsetPlots():
    x = np.arange(1, 11)
    y1 = np.exp(x)
    y2 = np.log(x)

    trace1 = go.Scatter(x=x, y=y1, name='exp')
    trace2 = go.Scatter(x=x, y=y2, name='log',
                        xaxis="x2", yaxis='y2')
    data = [trace1, trace2]

    layout = go.Layout(yaxis=dict(showline=True),
                       xaxis2=dict(domain=[0.1, 0.5],anchor='y2'),
                       yaxis2=dict(showline=True, domain=[0.5, 0.9], anchor='x2')
                       )

    fig = go.Figure(data=data, layout=layout)
    fig.write_html('first_figure.html', auto_open=True)

def plotBarCharts():

    # Bar Chart 1
    langs = ['C', 'C++', 'Java', 'Python', 'PHP']
    students = [23, 17, 35, 29, 12]
    data = [go.Bar(x=langs, y=students)]
    fig = go.Figure(data=data)
    fig.write_html('first_figure.html', auto_open=True)

    # Bar Chart 2
    branches = ['CSE', 'Mech', 'Electronics']
    fy = [23, 17, 35]
    sy = [20, 23, 30]
    ty = [30, 20, 15]
    trace1 = go.Bar(x=branches, y=fy, name='FY')
    trace2 = go.Bar(x=branches, y=sy, name='SY')
    trace3 = go.Bar(x=branches, y=ty, name='TY')
    data = [trace1, trace2, trace3]

    layout = go.Layout(barmode='group')
    fig = go.Figure(data=data, layout=layout)
    fig.write_html('2nd_figure.html', auto_open=True)

    # Bar Chart 3
    layout = go.Layout(barmode="stack")
    fig = go.Figure(data=data, layout=layout)
    fig.write_html('3rd_figure.html', auto_open=True)

def plotPie():
    # Pie Chart 1
    langs = ['C', 'C++', 'Java', 'Python', 'PHP']
    students = [23, 17, 35, 29, 12]
    trace = go.Pie(labels=langs, values=students)
    data = [trace]
    fig = go.Figure(data=data)
    fig.write_html('first_figure.html', auto_open=True)

    # Pie Chart 2
    parties = ['BJP', 'CONGRESS', 'DMK', 'TMC', 'YSRC', 'SS', 'JDU', 'BJD', 'BSP', 'OTH']
    seats = [303, 52, 23, 22, 22, 18, 16, 12, 10, 65]
    percent = [37.36, 19.49, 2.26, 4.07, 2.53, 2.10, 1.46, 1.66, 3.63, 25.44]

    data1 = {"values": seats, "labels": parties,
             "domain": {"column": 0},
             "name": "seats",
             "hoverinfo": "label+percent+name",
             "hole": .4,
             "type": "pie"}
    data2 = {"values": percent, "labels": parties,
             "domain": {"column": 1},
             "name": "vote share",
             "hoverinfo": "label+percent+name",
             "hole": .4,
             "type": "pie"}
    data = [data1, data2]
    layout = go.Layout({"title": "Parliamentary Election 2019",
                        "grid": {"rows": 1, "columns": 2},
                        "annotations": [{"font": {"size": 20},
                                         "showarrow": False,
                                         "text": "seats",
                                         "x": 0.20, "y": 0.5},
                                        {"font": {"size": 20},
                                         "showarrow": False,
                                         "text": "votes",
                                         "x": 0.8, "y": 0.5}]
                        })
    fig = go.Figure(data=data, layout=layout)
    fig.write_html('2nd_figure.html', auto_open=True)

if __name__ == "__main__":
    # plotLegents()
    # plotAxisAndTicks()
    # plotMultipleAxes()
    # plotSubplots()
    # plotInsetPlots()
    # plotBarCharts()
    plotPie()