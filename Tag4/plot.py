import plotly.graph_objects as go

graph = go.Figure(data=go.Bar(y=[5, 4, 2, 8, 9]))  # bar => balkendiagramm
graph.write_html("test.html", auto_open=True)
