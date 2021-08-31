import pandas as pd
import folium
from folium import plugins
from flask import Flask

############################################## Hotspot Data ############################################################

unrest = pd.read_csv(r'unrest_towns.csv')
print(unrest.head())

app = Flask(__name__)

@app.route('/')
def index():

    KZN = folium.Map(location=[-28.503833,
                            30.8875009],
                            zoom_start=7,
                            control_scale=True)

    Unrest_marker_cluster = plugins.marker_cluster.MarkerCluster(name='Hotspot Towns', show=False).add_to(KZN)

    for lat, lon, Town in zip(unrest["Latitude"].values.tolist(),
                              unrest["Longitude"].values.tolist(),
                              unrest["Town"].values.tolist()):
                              folium.Marker(location=[lat, lon],
                                            popup=folium.Popup('Hotspot Town: ' + Town,
                                            min_width=300, max_width=300, height=300),
                                            icon=folium.Icon(color="red", icon="fire", prefix="fa"),
                                            ).add_to(Unrest_marker_cluster)

    KZN.save("trial.html")


    return KZN._repr_html_()


    if __name__ == '__main__':
        app.run()





