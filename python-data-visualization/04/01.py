import dash
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
    html.P("first paragraph"),
    html.P("second paragraph")
])

if __name__ == "__main__":
    app.run_server(debug=True)