import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import time
import sys

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([dcc.Interval(id='interval1', interval=1 * 500, n_intervals=0),
                       html.Div([html.H1(id='white', children='White time passed : 01:30:00',
                                         style={"position":"absolut", "top":"50%", "transform": "translate(0, 100%)"})],
                                style={'width': '49%', "height":"200px","background-color": "#BCC6CC",
                                       "position":"relative", 'display': 'inline-block'}),
                       html.Div([html.H1(id='black', children='Black time passed : 01:30:00',
                                         style={"position":"absolut", "top":"50%", "transform": "translate(0, 100%)"})],
                                style={'width': '49%', "height":"200px", "background-color": "#E5E4E2",
                                       "position":"relative", 'display': 'inline-block'}),
                       html.Div([html.Button(id='submit-button', n_clicks=0, children='ok',
                                             style={"width":"200px", "height":"100px", "text-align":"center",
                                                    "background-color": "#e7e7e7", "font-size": "30px",
                                                    "border":"2px solid #4CAF50"})],
                                style={"position":"relative",'width': '98%', "height":"100px", "text-align":"center"})],
                      style={"margin":"auto", "text-align":"center"}
                      )


@app.callback(Output('white', 'children'),
              Output('black', 'children'),
              Input('interval1', 'n_intervals'),
              Input('submit-button', "n_clicks"))
def update_interval(n, clicks):
    def timer(total, s, e):
        hours, rem = divmod(total - (e - s), 3600)
        minutes, seconds = divmod(rem, 60)
        ret="{:0>2}:{:0>2}:{:02.0f}".format(int(hours), int(minutes), seconds)
        return int(hours) * 3600 + int(minutes) * 60 + int(seconds)#ret

    def convertTimeToString(t):
        hours, rem = divmod(t, 3600)
        minutes, seconds = divmod(rem, 60)
        ret = "{:0>2}:{:0>2}:{:02.0f}".format(int(hours), int(minutes), seconds)
        return ret

    global totalClicks, whiteRemainTime, blackRemainTime, startTime, WorB

    # The game has not started yet
    if clicks == 0 :
        return 'White time passed : ' + convertTimeToString(whiteRemainTime), \
               'Black time passed : ' + convertTimeToString(blackRemainTime)

    if clicks > totalClicks:
        if WorB == 0:
            end = time.time()
            whiteRemainTime = timer(whiteRemainTime, startTime, end)
            WorB = 1
        elif WorB == 1:
            end = time.time()
            blackRemainTime = timer(blackRemainTime, startTime, end)
            WorB = 0
        else :# WorB == -1 :
            WorB = 0

        totalClicks = clicks
        startTime = time.time()
        return 'White time passed : ' + convertTimeToString(whiteRemainTime), \
               'Black time passed : ' + convertTimeToString(blackRemainTime)
    else :
        end = time.time()
        if WorB == 0 :
            # whiteRemainTime = timer(whiteRemainTime, startTime, end)
            return 'White time passed : ' + convertTimeToString(timer(whiteRemainTime, startTime, end)), \
                   'Black time passed : ' + convertTimeToString(blackRemainTime)
        if WorB == 1 :
            # blackRemainTime = timer(blackRemainTime, startTime, end)
            return 'White time passed : ' + convertTimeToString(whiteRemainTime), \
                   'Black time passed : ' + convertTimeToString(timer(blackRemainTime, startTime, end))
        else :
            return 'White time passed : ' + convertTimeToString(whiteRemainTime), \
                   'Black time passed : ' + convertTimeToString(blackRemainTime)

if __name__ == '__main__':
    whiteRemainTime = 90 * 60
    blackRemainTime = 90 * 60
    startTime = 0
    totalClicks = 0
    WorB = -1
    app.run_server(debug=True)