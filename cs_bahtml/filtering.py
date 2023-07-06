import geopandas as gpd
import pandas as pd
from shapely.geometry import Polygon


def points_in_polygon(df: pd.DataFrame, polygon: gpd.GeoDataFrame, join: str = "inner"):
    gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.x, df.y))
    gdf = gdf.sjoin(polygon,how = join, predicate = "within")
    df_out = pd.DataFrame(gdf.drop(columns='geometry'))
    return df_out

def build_polygon(points):
    polygon = Polygon(points)
    gdf = gpd.GeoDataFrame()
    gdf['geometry'] = None
    gdf.loc[0,'geometry'] = polygon
    return gdf