import folium
import json
import pandas as pd

def mapa(DF,columna):
    df_mapa_dict = DF.set_index("comunidad")["columna"].to_dict()

    mapa_espana = folium.Map(location=[40.4637, -3.7492], zoom_start=6)

    with open('data/comunidades.geojson') as f:
        geojson_data = json.load(f)

    def estilo(feature):
        comunidad_nombre = feature['properties']['acom_name']
        valor = df_mapa_dict.get(comunidad_nombre, 0)  
        fill_color = (
            'green' if valor < 5 else
            'yellow' if valor < 10 else
            'red' if valor >= 10 else
            "pink"
        )
        return {
            'fillColor': fill_color,
            'color': 'black',
            'weight': 1,
            'fillOpacity': 0.5,
        }

    folium.GeoJson(
        geojson_data,
        style_function=estilo,
        acom_name='geojson'
    ).add_to(mapa_espana)

    folium.LayerControl().add_to(mapa_espana)

    mapa_espana

