import dash
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
    html.Table([
        html.Tr([
            html.Th("종목코드"), html.Th("종목명")
        ]),
        html.Tr([
            html.Td("000020"), html.Td("동화약품")
        ]),
    ])
])

if __name__ == "__main__":
    app.run_server(debug=True)