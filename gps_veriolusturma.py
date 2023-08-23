import json
import random

# Rastgele GPS koordinatları oluşturmak için sınırlar belirliyoruz
min_lat, max_lat = 36, 42  # Enlem sınırları
min_lon, max_lon = 26, 45  # Boylam sınırları

# Rakip Takımların GPS koordinatlarını rastgele oluşturuyoruz
teams = []
for i in range(15):
    team = {
        'Takim_adi': f'Takim {i+1}',
        'gpsX': round(random.uniform(min_lat, max_lat), 6),
        'gpsY': round(random.uniform(min_lon, max_lon), 6)
    }
    teams.append(team)

# Bizim takımın GPS koordinatlarını rastgele oluşturuyoruz
my_team = {
    'Takim_adi': 'Takimim',
    'gpsX': round(random.uniform(min_lat, max_lat), 6),
    'gpsY': round(random.uniform(min_lon, max_lon), 6)
}

# Tüm GPS koordinatlarını bir sözlük nesnesinde topluyoruz
data = {'Bizim Takim': my_team, 'Takimlar': teams}

# JSON formatında dosyaya yazıyoruz
with open('gps_data.json', 'w') as f:
    f.writelines(json.dumps(data,indent=0))
