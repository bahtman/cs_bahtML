from awpy.data import NAV, MAP_DATA
import plotly.graph_objects as go
import plotly.express as px
from PIL import Image, ImageDraw
import os
from awpy.visualization.plot import position_transform

def fill_area(fig,mapname=None,areaId=None):
    if areaId:
        fig = go.Figure(fig)
        area = NAV[mapname][areaId]
        fig.add_shape(type="rect",
            x0=area["southEastX"], 
            y0=area["southEastY"], 
            x1=area["northWestX"], 
            y1=area["northWestY"],
            fillcolor="LightSkyBlue"
        )
    return fig

def load_map(path, mapname):
    img = Image.open(os.path.join(path,f"{mapname}_dark.png"))
    #for a in NAV[mapname]:
    #    area = NAV[mapname][a]
    #    row,col = draw.rectangle_perimeter(end=(area["southEastY"],area["southEastX"]), start=(area["northWestY"],area["northWestX"]))
    #    img[row, col, :] = [255, 255, 0,200] #RGB -Black
    return img






def generate_contour(fig,dff,mapname,type="contour"):

    x = dff.opponentArea_rotated_x.apply(lambda x: position_transform(mapname, x, "x"))
    y = dff.opponentArea_rotated_y.apply(lambda x: position_transform(mapname, x, "y"))

    fig.data = [fig.data[0]]

    if type=="contour" or type=="both":
        fig.add_trace(go.Histogram2dContour(
        x = x,
        y = y,
        opacity = .25,
        ncontours=10,
        histnorm= "probability",
        xbins= dict(start=0, end = 1024, size=32),
        ybins= dict(start=0, end = 1024, size=32),
        colorscale=[[1, 'rgba(214, 39, 40, 1)'],   
                [0, 'rgba(128, 128, 128, 1)']],
        xaxis = 'x',
        line = dict(smoothing=0.5),
        yaxis = 'y',
        showscale=False,
        hoverinfo='skip'
        ))
    if type=="scatter" or type=="both":
        fig.add_trace(go.Scatter(
        x = x,
        y = y,
        opacity = .50,
        #histnorm="probability density",
        #ncontours=30,
        #colorscale=[[1, 'rgba(214, 39, 40, 0.85)'],   
        #        [0.1, 'rgba(128, 128, 128, 0)']],
        xaxis = 'x',
        yaxis = 'y',
        mode='markers',
        #showscale=False,
        hoverinfo='skip'
        ))



    return fig

def add_smoke_wall(fig,smokes, mapname):
    smoke_rad = position_transform(mapname, 144, "x") - position_transform(mapname, 0, "x")
    for x,y in smokes:
        x = position_transform(mapname, x, 'x')
        y = position_transform(mapname, y, 'y')
        fig = add_smoke(fig,x, y, smoke_rad)
    return fig

def add_smoke(fig, x, y, smoke_rad):
    draw = ImageDraw.Draw(fig)
    draw.ellipse(
        xy= [(x-smoke_rad,y-smoke_rad), (x+smoke_rad,y+smoke_rad)],
                outline='rgb(12,15,18)',
                fill= 'rgb(128,128,128)'
    )

    return fig

def add_player(fig,x,y, player_rad, side):
    linecol = 'rgb(12,15,18)'
    if side == "CT":
        fillcol = 'rgb(93,121,174)'
    elif side == "T":
        fillcol = 'rgb(204,186,124)'

    fig.ellipse(
        xy= [(x-player_rad,y-player_rad), (x+player_rad,y+player_rad)],
                outline=linecol,
                fill= fillcol
    )
    return fig