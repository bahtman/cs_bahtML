import geopandas as gpd
import pandas as pd
from shapely.geometry import Polygon, Point


def point_in_polygon(point:tuple, polygon: Polygon):
    point = Point(point)
    b_contain = polygon.contains(point)
    return b_contain

def build_polygon(points):
    polygon = Polygon(points)
    return polygon