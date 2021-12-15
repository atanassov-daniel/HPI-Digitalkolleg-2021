import plotly.graph_objects as go

all = [
    ("Elena Stoyanova", 11788),
    ("Мартин Ганчев", 7861),
    ("Hristo Petrov", 7688),
    ("Daniel Atanassov", 5120),
    ("Йово Маков", 5070),
    ("Kalina Krusteva", 4979),
    ("Александър Станков", 4780),
    ("Alexandra Tsvetanska", 4298),
    ("Димитър Колев", 3985),
    ("Yoana Monova", 3729),
    ("Veliqn Taslev", 3495),
    ("Viktor Angelov", 3245),
    ("Nikola Plakunov", 2903),
    ("Eliza Assenova", 1889),
    ("Miya Simova", 1349),
    ("Janet Tablova", 1232),
    ("Ивайло М.", 1137),
    ("Te Di", 882),
    ("Teodora Todorova", 831),
    ("Сияна Люцканова", 528),
    ("Калия Николова", 526),
    ("Ivana Pojarska", 223),
    ("Краси Деянова", 220),
    ("Вероника С.", 158),
    ("Slav Ivanov", 144),
    ("Selma Borislavova", 130),
    ("Elitsa Inkova", 120),
    ("Katya Ovsyannikova", 38),
    ("Александра Цветанска", 38),
    ("Niki Gospodinov", 2),
    ("Минко Минков", 2),
    ("Ч. Нелия", 1),
]

x, y1, hovertext1, y2, hovertext2 = [], [], [], [], []
for name, messages_count in all:
    x.append((name))
    y1.append((messages_count))
    hovertext1.append(f"{name} wrote {messages_count} messages")

    # percent_of_messages = f"{'%.2f' % (messages_count / 78391 * 100)}%"
    percent_of_messages = float("%.2f" % (messages_count / 78391 * 100))
    y2.append(percent_of_messages)
    hovertext2.append(
        f"{name} wrote {percent_of_messages}% of all the messages in the chat"
    )

# Use textposition='auto' for direct text
fig1 = go.Figure(
    data=[
        go.Bar(
            x=x,
            y=y1,
            hovertext=hovertext1,
            text=y1,
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
            values=y2,
            textinfo='label+value',
            # text=y2,
            hovertemplate="<b>%{label}</b> wrote <b>%{value}%</b> of all the messages in the chat"
        )
    ]
)
fig2.show()
# fig2.update_traces(hoverinfo='label+percent')
# * write the graphs to a single html file
html_name = "p_graph7.html"
with open(html_name, "a") as f:
    f.write(fig1.to_html(full_html=False, include_plotlyjs="cdn"))
    f.write(fig2.to_html(full_html=False, include_plotlyjs="cdn"))

# * open the newly generated html in the browser
import webbrowser

webbrowser.open_new_tab(html_name)
