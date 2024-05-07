import dash_bootstrap_components as dbc
from dash import html, Input, Output, State, dcc
from app import *
from templates.base import *

layout_dashboard = dbc.Row(
    style={
        'width': '100%'
    },
    children= [
        layout
    ]
)
