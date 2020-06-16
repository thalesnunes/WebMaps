import folium
import pandas as pd


def color_generator_elev(elev):
    if elev < 1000:
        return 'green'
    elif 1000 <= elev < 3000:
        return 'orange'
    else:
        return 'red'

def color_generator_pop(pop):
    
    if pop < 10000000:
        return 'green' 
    elif 10000000 <= pop < 30000000:
        return 'orange'
    else:
        return 'red'


map1 = folium.Map(location=[0, 0], zoom_start=2)

points = pd.read_csv('Volcanoes.txt')

fg1 = folium.FeatureGroup(name='Volcanoes')

for _, item in points.iterrows():
    fg1.add_child(folium.Marker(location=[item.LAT, item.LON],
                               popup=f'{item.NAME}: {item.ELEV}m',
                               icon=folium.Icon(color=color_generator_elev(item.ELEV))))

fg2 = folium.FeatureGroup(name='Population')
fg2.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                            style_function=lambda x: {'fillColor': color_generator_pop(x['properties']['POP2005'])}))

map1.add_child(fg1)
map1.add_child(fg2)

map1.add_child(folium.LayerControl())

map1.save('Map1.html')