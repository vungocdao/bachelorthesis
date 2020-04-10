import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.repustate.com/sentiment-analysis-api-demo/')

# soup = bs4.BeautifulSoup(request.text, 'lxml')
# sentiment = soup.select('strong')

# <textarea id="id_text" class="ctrl" name="text"> Insert Reviews into this
# <button class="btn btn--primary"> button
# in <td>, <strong> sentiment value
