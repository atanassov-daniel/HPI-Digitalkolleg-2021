import plotly.graph_objects as go

def gen_graphs(people_messages_count_desc, total_messages, path):
    x, y, hovertext1 = [], [], []
    for name, messages_count in people_messages_count_desc:
        x.append((name))
        y.append((messages_count))
        hovertext1.append(f"{name} wrote {messages_count} out of {total_messages} messages")

    # Use textposition='auto' for direct text
    fig1 = go.Figure(
        data=[
            go.Bar(
                x=x,
                y=y,
                hovertext=hovertext1,
                text=y,
                textposition="auto",
            )
        ],
        layout=go.Layout(
            title=go.layout.Title(text="Wie viele Nachrichten hat jede Person geschrieben?")
        ),
    )

    # Customize aspect
    """ fig1.update_traces(
        marker_color="rgb(158,202,225)",
        marker_line_color="rgb(8,48,107)",
        marker_line_width=1.5,
        opacity=0.6,
    ) """
    # fig1.update_layout(title_text="Wie viele Nachrichten hat jede Person geschrieben?")
    # fig1.update_yaxes(hoverformat=",d")

    # print(y2)
    # * name="" is needed so that there isn't a text "trace 0" next to every hover box
    # fig2 = go.Figure(data=[go.Pie(name="", labels=x, values=y2, hovertemplate=hovertext2)])
    fig2 = go.Figure(
        data=[
            go.Pie(
                name="",
                labels=x,
                values=y,
                textinfo='label+percent',
                # text=y2,
                hovertemplate="<b>%{label}</b> wrote <br><b>%{percent}</b> of the messages</br> (%{value} out of 78391)"
            )
        ],layout=go.Layout(
            title=go.layout.Title(text="Wie hoch liegt der prozentuale Anteil der Nachrichten, die jede Person geschrieben hat?")
        ),
    )
    fig1.show()
    fig2.show()
    """ 
    #! this one gets pretty ugly too 
    fig1.write_html(f"{path}/graph1.html")
    fig2.write_html(f"{path}/graph2.html") """

    #! the pie starts looking extremely ugly, I have to find a way to fix it probably 
    # * write the graphs to a single html file
    """ html_name = f"{path}/graphs.html"
    with open(html_name, "a") as f:
        f.write(fig1.to_html(full_html=False, include_plotlyjs="cdn"))
        f.write(fig2.to_html(full_html=False, include_plotlyjs="cdn"))
       

    # * open the newly generated html in the browser
    import webbrowser
    webbrowser.open_new_tab(html_name) """#!end of ugly reuslting code