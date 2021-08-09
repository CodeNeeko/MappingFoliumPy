import folium
import pandas
data = pandas.read_csv("volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list (data["ELEV"])
name = list(data["NAME"])

def color_producer(elevation):
    if elevation < 1500:
        return 'green'
    elif 1500 < elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location = [19.27463731321326, 72.8737635364547], zoom_start=5, tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el,name in zip(lat, lon, elev, name):
    fgv.add_child(folium.CircleMarker(location =[lt, ln], radius = 8, popup=str(name)+"\n"+str(el)+"m",fill_color=color_producer(el), color='grey', fill_opacity = 0.9 ))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data = open('world.json', 'r', encoding = 'utf-8-sig').read(), 
style_function = lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())

map.save("Map1.html")