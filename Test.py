
# importing required libraries
from flask import Flask
import datetime
import yfinance as yf
from dash import dash, html, dcc
from dash.dependencies import Input, Output
import webbrowser as web



app = dash.Dash()
app.title = "Stock Visualisation"

app.layout = html.Div(children=[
	html.H1("Stock Visualisation Dashboard"),
	html.H4("Please enter the stock name"),
	dcc.Input(id='input', value='AAPL', type='text'),
	html.Div(id='output-graph')
])

# callback Decorator 
@app.callback(
	Output(component_id='output-graph', component_property='children'),
	[Input(component_id='input', component_property='value')]
)
def update_graph(input_data):
	start = datetime.datetime(2010, 1, 1)
	end = datetime.datetime.now()

	try:
		df = web.DataReader(input_data, 'yahoo', start, end)

		graph = dcc.Graph(id ="example", figure ={
			'data':[{'x':df.index, 'y':df.Close, 'type':'line', 'name':input_data}],
			'layout':{
				'title':input_data
			}
		})

	except:
		graph = html.Div("Error retrieving stock data.")

	return graph

if __name__ == '__main__':
	app.run_server()
