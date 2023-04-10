import requests
from bs4 import BeautifulSoup

url = 'https://www.linkedin.com/in/[nombre-de-candidato]/'
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

nombre = soup.find('li', {'class': 'inline t-24 t-black t-normal break-words'}).get_text().strip()
titulo = soup.find('h2', {'class': 'mt1 t-18 t-black t-normal break-words'}).get_text().strip()
ubicacion = soup.find('li', {'class': 't-16 t-black t-normal inline-block'}).get_text().strip()
resumen = soup.find('section', {'class': 'pv-about-section'}).find('p').get_text().strip()

experiencias = soup.find_all('li', {'class': 'pv-profile-section__list-item'})
for experiencia in experiencias:
    cargo = experiencia.find('h3').get_text().strip()
    empresa = experiencia.find('p', {'class': 'pv-entity__secondary-title'}).get_text().strip()
    periodo = experiencia.find('h4', {'class': 'pv-entity__date-range'}).find_all('span')[1].get_text().strip()
    descripcion = experiencia.find('p', {'class': 'pv-entity__description'}).get_text().strip()

print(nombre, titulo, ubicacion, resumen)

for experiencia in experiencias:
    print(experiencia)
