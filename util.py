"""
This is a collection of shared components, utilities and data

"""

from dash import dcc, html
import plotly.express as px
import dash_bootstrap_components as dbc
import pathlib

# set relative path
PATH = pathlib.Path(__file__).parent
GALLERY_PATH = PATH.joinpath("./gallery").resolve()


# Links
dbc_logo = "https://user-images.githubusercontent.com/72614349/133677816-5ea52424-bfd3-4405-9ccf-8ad0dbd18020.png"
bootstrap_logo = "https://user-images.githubusercontent.com/72614349/133683669-eef08b42-2eff-49df-b0a5-33a7754a2b86.png"
dbc_home_url = "https://dash-bootstrap-components.opensource.faculty.ai/"
cheatsheet_url = "https://dashcheatsheet.pythonanywhere.com/"
theme_explorer_url = "https://hellodash.pythonanywhere.com/theme_explorer"


def get_code_file(filename):
    """
    :param filename: (str) file name of python file in the gallery directory
    :return: a string to display the code with highlighting in dcc.Markdown(code)

    Note: be sure to include a blank line and docstring at start of source file so highlighting
      works correctly
    """
    with open(GALLERY_PATH.joinpath(filename)) as f:
        code = f.read()
    return f"```{code}```"


def make_code_card(code, id=id, height=600, width=None):
    return dbc.Card(
        [
            dcc.Markdown(
                code,
                id=id,
                className="p-2 mt-4",
                style={"maxHeight": height,'maxWidth':width, "overflow": "auto"},
            ),
            dcc.Clipboard(
                target_id=id,
                title="copy snippet",
                className="position-absolute top-0 end-0 fs-5",
            ),
        ],
        className="position-relative",
    )


theme_explorer_header = html.Div(
    dbc.Container(
        [
            html.H1("Dash Bootstrap Theme Explorer", className="display-3 text-dark",),
            html.P(
                "A guide for styling Dash components and figures with a Bootstrap theme",
                className="fst-italic lead",
            ),
            html.Div(
                [
                    html.A(
                        html.Img(src=dbc_logo, height=90, className="m-2"),
                        href=dbc_home_url,
                        target="_blank",
                    ),
                    html.A(
                        html.Img(src=bootstrap_logo, height=90, className="m-2"),
                        href="https://getbootstrap.com/docs/5.1/getting-started/introduction/",
                        target="blank",
                    ),
                ],
            ),
            html.Div(
            [
                dbc.Button(
                    "Theme Explorer",
                    color="primary",
                    outline=True,
                    href="/theme_explorer",
                    className="me-2",
                    size="sm",
                ),
                dbc.Button(
                    "Figure Templates",
                    color="primary",
                    outline=True,
                    href="/figure_templates",
                    className="me-2",
                    size="sm",
                ),
                dbc.Button(
                    "Theme Change Components",
                    id="app_gallery",
                    color="primary",
                    outline=True,
                    href="/theme_change_components",
                    className="me-2",
                    size="sm",
                ),
                dbc.Button(
                    "Bootstrap Cheatsheet",
                    id="cheatsheet",
                    color="primary",
                    outline=True,
                    href="https://dashcheatsheet.pythonanywhere.com/",
                    external_link=True,
                    target="_blank",
                    className="me-2",
                    size="sm",
                ),
            ],
            className="mt-4",
         ),

        ],
        fluid=True,
        className="py-3",
    ),
    className="p-3 bg-light text-dark rounded-3 mb-4  position-relative",
    style={"height": 400},
)


plotly_template = [
    "bootstrap",
    "plotly",
    "ggplot2",
    "seaborn",
    "simple_white",
    "plotly_white",
    "plotly_dark",
    "presentation",
    "xgridoff",
    "ygridoff",
    "gridon",
    "none",
]

continuous_colors = px.colors.named_colorscales()

discrete_colors = {
    "Plotly": px.colors.qualitative.Plotly,
    "D3": px.colors.qualitative.D3,
    "G10": px.colors.qualitative.G10,
    "T10": px.colors.qualitative.T10,
    "Alphabet": px.colors.qualitative.Alphabet,
    "Dark24": px.colors.qualitative.Dark24,
    "Light24": px.colors.qualitative.Light24,
    "Set1": px.colors.qualitative.Set1,
    "Pastel1": px.colors.qualitative.Pastel1,
    "Dark2": px.colors.qualitative.Dark2,
    "Set2": px.colors.qualitative.Set2,
    "Pastel2": px.colors.qualitative.Pastel2,
    "Set3": px.colors.qualitative.Set3,
    "Antique": px.colors.qualitative.Antique,
    "Bold": px.colors.qualitative.Bold,
    "Pastel": px.colors.qualitative.Pastel,
    "Safe": px.colors.qualitative.Safe,
    "Vivid": px.colors.qualitative.Vivid,
    "Prism": px.colors.qualitative.Prism,
}
