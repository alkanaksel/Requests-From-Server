import json
from math import radians, cos, sin, asin, sqrt
import requests

# JSON dosyalarından tüm takımların GPS koordinatlarını okuyoruz
with open('gps_data.json') as f:
    data = json.load(f)

# Sizin takımınızın GPS koordinatları
team_lat = data['Bizim Takim']['gpsX']
team_lon = data['Bizim Takim']['gpsY']

# En yakın takımın başlangıçta yok sayılabilecek bir uzaklığı belirliyoruz
min_distance = float('inf')
nearest_team = None

# Tüm takımların GPS koordinatlarını kontrol ediyoruz
for team in data['Takimlar']:
    lat = team['gpsX']
    lon = team['gpsY']
    
    # Haversine formülü ile takım ve diğer takımlar arasındaki mesafeyi hesaplıyoruz
    R = 6372.8  # Dünya'nın yarıçapı (km)
    dLat = radians(lat - team_lat)
    dLon = radians(lon - team_lon)
    lat1 = radians(team_lat)
    lat2 = radians(lat)
    a = sin(dLat/2)**2 + cos(lat1)*cos(lat2)*sin(dLon/2)**2
    c = 2*asin(sqrt(a))
    distance = R * c
    
    # En yakın takımın GPS koordinatlarını güncelliyoruz
    if distance < min_distance:
        min_distance = distance
        nearest_team = team

# En yakın takımın bilgilerini yazdırıyoruz
print(f"En yakin takim: {nearest_team['Takim_adi']}")
print(f"Uzaklik: {min_distance} km")