# Examples from https://www.tutorialspoint.com/plotly

import plotly.graph_objects as go
import numpy as np
import math #needed for definition of pi
import pandas as pd

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

def PlotScatter():
    # go.Scatter
    N = 100
    x_vals = np.linspace(0, 1, N)
    y1 = np.random.randn(N) + 5
    y2 = np.random.randn(N)
    y3 = np.random.randn(N) - 5

    trace0 = go.Scatter(x=x_vals, y=y1, mode='markers', name='markers')
    trace1 = go.Scatter(x=x_vals, y=y2, mode='lines+markers', name='line+markers')
    trace2 = go.Scatter(x=x_vals, y=y3, mode='lines', name='line')
    data = [trace0, trace1, trace2]
    fig = go.Figure(data=data)
    fig.write_html('1st_figure.html', auto_open=True)

    # go.Scattergl
    # Allows Graphics Processing Unit (GPU) accelerated usage of image processing
    # For increased speed, improved interactivity, and the ability to plot even more data
    N = 100000
    x = np.random.randn(N)
    y = np.random.randn(N)
    trace0 = go.Scattergl(x=x, y=y, mode='markers')

    data = [trace0]
    layout = go.Layout(title="scattergl plot ")
    fig = go.Figure(data=data, layout=layout)
    fig.write_html('2nd_figure.html', auto_open=True)

    # Bubble charts - Variation of Scatter Plot
    company = ['A', 'B', 'C']
    products = [13, 6, 23]
    sale = [2354, 5423, 4251]
    share = [23, 47, 30]
    fig = go.Figure(data=[go.Scatter(x=products, y=sale,
                                     text=['company:' + c + ' share:' + str(s) + '%'
                                           for c in company for s in share if company.index(c) == share.index(s)],
                                     mode='markers',
                                     marker_size=share,
                                     marker_color=['blue', 'red', 'yellow'])
                          ])
    fig.write_html('3rd_figure.html', auto_open=True)

def PlotDotAndTables():
    # Dot Plots
    # For a small amount of data
    # Shows changes between two (or more) points in time or between two (or more) conditions.
    # Similar to horizontal bar chart
    census = [1951, 1961, 1971, 1981, 1991, 2001, 2011]
    x1 = [8.86, 15.35, 21.97, 29.76, 39.29, 53.67, 64.63]
    x2 = [27.15, 40.40, 45.96, 56.38, 64.13, 75.26, 80.88]
    traceA = go.Scatter(x=x1, y=census,
                        marker=dict(color="crimson", size=12),
                        mode="markers",name="Women")
    traceB = go.Scatter(x=x2, y=census, marker=dict(color="gold", size=12),
                        mode="markers", name="Men")
    data = [traceA, traceB]
    layout = go.Layout(title="Trend in Literacy rate in Post independent India",
                       xaxis_title="percentage", yaxis_title="census")
    fig = go.Figure(data=data, layout=layout)
    fig.write_html('1st_figure.html', auto_open=True)

    # go.Table
    trace = go.Table(header=dict(values=['Teams', 'Mat', 'Won', 'Lost', 'Tied', 'NR', 'Pts', 'NRR'],
                                 line_color='gray', fill_color='lightskyblue', align='left'),
                     cells=dict(values=[['India','Australia','England','New Zealand','Pakistan',
                                         'Sri Lanka','South Africa','Bangladesh','West Indies','Afghanistan'],
                                        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
                                        [7, 7, 6, 5, 5, 3, 3, 3, 2, 0],
                                        [1, 2, 3, 3, 3, 4, 5, 5, 6, 9],
                                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                        [1, 0, 0, 1, 1, 2, 1, 1, 1, 0],
                                        [15, 14, 12, 11, 11, 8, 7, 7, 5, 0],
                                        [0.809, 0.868, 1.152, 0.175, -0.43, -0.919, -0.03, -0.41, -0.225, -1.322]
                                        ],
                                line_color='gray', fill_color='lightcyan', align='left')
                     )
    data = [trace]
    fig = go.Figure(data=data)
    fig.write_html('2nd_figure.html', auto_open=True)

    # go.Table can be used with pandas
    df = pd.read_csv('point-table.csv')
    trace = go.Table(header=dict(values=list(df.columns)),
                     cells=dict(values=[df.Teams, df.Matches, df.Won, df.Lost, df.Tie, df.NR, df.Points, df.NRR]))
    data = [trace]
    fig = go.Figure(data=data)
    fig.write_html("3rd_figure.html", auto_open=True)

def PlotHistogram():
    x1 = np.array([22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27])
    data = [go.Histogram(x=x1)]
    fig = go.Figure(data)
    fig.write_html("1st_figure.html", auto_open=True)

def PlotBoxPlot():
    trace1 = go.Box(y=[1140, 1460, 489, 594, 502, 508, 370, 200])
    data = [trace1]
    fig = go.Figure(data)
    fig.write_html("1st_figure.html", auto_open=True)

    trc = go.Box(y=[0.75, 5.25, 5.5, 6, 6.2, 6.6, 6.80, 7.0, 7.2, 7.5, 7.5, 7.75, 8.15,
                    8.15, 8.65, 8.93, 9.2, 9.5, 10, 10.25, 11.5, 12, 16, 20.90, 22.3, 23.25],
                 boxpoints='suspectedoutliers', boxmean='sd')
    data = [trc]
    fig = go.Figure(data)
    fig.write_html("2nd_figure.html", auto_open=True)

    # Violin Plot
    np.random.seed(10)
    c1 = np.random.normal(100, 10, 200)
    c2 = np.random.normal(80, 30, 200)
    trace1 = go.Violin(y=c1, meanline_visible=True)
    trace2 = go.Violin(y=c2, box_visible=True)
    data = [trace1, trace2]
    fig = go.Figure(data=data)
    fig.write_html("3rd_figure.html", auto_open=True)

    # Contour Plot
    xlist = np.linspace(-3.0, 3.0, 100)
    ylist = np.linspace(-3.0, 3.0, 100)
    X, Y = np.meshgrid(xlist, ylist)
    Z = np.sqrt(X ** 2 + Y ** 2)
    trace = go.Contour(x=xlist, y=ylist, z=Z)
    data = [trace]
    fig = go.Figure(data)
    fig.write_html("4th_figure.html", auto_open=True)

    # Quiver plot
    x, y = np.meshgrid(np.arange(-2, 2, .2), np.arange(-2, 2, .25))
    z = x * np.exp(-x ** 2 - y ** 2)
    v, u = np.gradient(z, .2, .2)

    # Create quiver figure
    import plotly.figure_factory as ff
    fig = ff.create_quiver(x, y, u, v,
                           scale=.25, arrow_scale=.4,
                           name='quiver', line=dict(width=1))
    fig.write_html("5th_figure.html", auto_open=True)

if __name__ == "__main__":
    plotLegents()
    # plotAxisAndTicks()
    # plotMultipleAxes()
    # plotSubplots()
    # plotInsetPlots()
    # plotBarCharts()
    # plotPie()
    # PlotScatter()
    # PlotDotAndTables()
    # PlotHistogram()
    # PlotBoxPlot()