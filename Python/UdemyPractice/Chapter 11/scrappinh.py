'''
import bs4
import requests

resultado = requests.get('https://www.hollowknight.com/')
soup = bs4.BeautifulSoup(resultado.text, 'html.parser')

imagenes = soup.select('img')[14]['data-src']

print( imagenes)
breakpoint()

image_grim=requests.get(imagenes)


hk= open('new_hk.jpg','wb')
hk.write(image_grim.content)
hk.close()


'''

import bs4
import requests
game='elden ring'
resultado = requests.get(f'https://www.google.com/search?q={game}&tbm=isch&ved=2ahUKEwjsqLjw2uGEAxWc7skDHYYaBBMQ2-cCegQIABAA')
soup = bs4.BeautifulSoup(resultado.text, 'html.parser')
url= soup.select('.DS1iW')[0]['src']
breakpoint()
url_imnage = soup.select('.sqs-image-shape-container-element')[9].select('img')[0]['data-src']
image_grim=requests.get(url_imnage)


hk= open('new_hk.jpg','wb')
hk.write(image_grim.content)
hk.close()
