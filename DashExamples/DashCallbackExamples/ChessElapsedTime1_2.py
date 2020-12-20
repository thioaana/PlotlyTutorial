import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import time
import sys

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([dcc.Interval(id='interval1', interval=1 * 500, n_intervals=0),
                       html.Div([html.H1(id='white', children='',
                                         style={"color": "red", "position": "absolut", "top":"50%", "transform": "translate(0, 100%)"})],
                                style={'width': '49%', "height":"200px","background-color": "#BCC6CC",
                                       "position":"relative", 'display': 'inline-block'}),
                       html.Div([html.H1(id='black', children='',
                                         style={"position":"absolut", "top":"50%", "transform": "translate(0, 100%)"})],
                                style={'width': '49%', "height":"200px", "background-color": "#E5E4E2",
                                       "position":"relative", 'display': 'inline-block'}),
                       html.Div([html.Button(id='submit-button', n_clicks=0, children='ok',
                                             style={"width":"200px", "height":"100px", "text-align":"center",
                                                    "background-color": "#e7e7e7", "font-size": "30px",
                                                    "border":"2px solid"}),
                                 html.Button(id='reset-button', n_clicks=0, children='Reset',
                                             style={"width": "200px", "height": "100px", "text-align": "center",
                                                    "background-color": "#e7e7e7", "font-size": "30px",
                                                    "border": "2px solid"})],
                                style={"position":"relative", 'display': 'inline-block',
                                       'width': '68%', "height":"100px", "text-align":"center"})],
                      style={"margin":"auto", "text-align":"center"}
                      )


@app.callback(Output('white', 'children'),
              Output('black', 'children'),
              Input('interval1', 'n_intervals'))
def update_interval(n):
    # Update Remaining time for White and Black during time
    def convertTimeToString(t):
        hours, rem = divmod(t, 3600)
        minutes, seconds = divmod(rem, 60)
        ret = "{:0>2}:{:0>2}:{:02.0f}".format(int(hours), int(minutes), seconds)
        return ret

    global whiteRemainTime, blackRemainTime, startTime, WorB

    end = time.time()
    if WorB == 0:
        w = 'White Remaining time : ' + convertTimeToString(timer(whiteRemainTime, startTime, end))
        b = 'Black Remaining time : ' + convertTimeToString(blackRemainTime)
    elif WorB == 1:
        w = 'White Remaining time : ' + convertTimeToString(whiteRemainTime)
        b = 'Black Remaining time : ' + convertTimeToString(timer(blackRemainTime, startTime, end))
    else:
        w = 'White Remaining time : ' + convertTimeToString(whiteRemainTime)
        b = 'Black Remaining time : ' + convertTimeToString(blackRemainTime)
    return w, b


@app.callback(Output('white', 'style'),
              Output('black', 'style'),
              Input('submit-button', "n_clicks"),
              Input('reset-button', "n_clicks"))
def update_click(clicks, rclicks):
    global whiteRemainTime, blackRemainTime, startTime, WorB
    wStyle = {"color":"black", "position":"absolut", "top":"50%", "transform": "translate(0, 100%)"}
    bStyle = {"color": "black", "position": "absolut", "top": "50%", "transform": "translate(0, 100%)"}

    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'submit-button' in changed_id:
        if WorB == 0:
            end = time.time()
            whiteRemainTime = timer(whiteRemainTime, startTime, end)
            WorB = 1
            bStyle = {"color": "red", "position": "absolut", "top": "50%", "transform": "translate(0, 100%)"}
        elif WorB == 1:
            end = time.time()
            blackRemainTime = timer(blackRemainTime, startTime, end)
            WorB = 0
            wStyle = {"color": "red", "position": "absolut", "top": "50%", "transform": "translate(0, 100%)"}
        else :# WorB == -1 :
            WorB = 0
            wStyle = {"color": "red", "position": "absolut", "top": "50%", "transform": "translate(0, 100%)"}
        startTime = time.time()
    else:
        whiteRemainTime = period
        blackRemainTime = period
        startTime = 0
        WorB = -1
        wStyle = {"color": "red", "position": "absolut", "top": "50%", "transform": "translate(0, 100%)"}
    return wStyle, bStyle

def timer(total, s, e):
    hours, rem = divmod(total - (e - s), 3600)
    minutes, seconds = divmod(rem, 60)
    ret="{:0>2}:{:0>2}:{:02.0f}".format(int(hours), int(minutes), seconds)
    return int(hours) * 3600 + int(minutes) * 60 + int(seconds)#ret

if __name__ == '__main__':
    period = 5 * 60
    whiteRemainTime = period
    blackRemainTime = period
    startTime = 0
    WorB = -1
    app.run_server(debug=True)