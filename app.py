from dash import Dash, html

app = Dash(__name__, assets_folder='front/dist')
app.layout = html.Div(
    [
        html.Div('Hello World', className='title'),
        html.Div('Hello World', className='text-3xl font-semibold m-6'),
    ]
)

if __name__ == "__main__":
    app.run(debug=True)
