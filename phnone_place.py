import folium

m = folium.Map(location=[42.68410,23.31743])
result = 'base_map.html'
m.save(result)