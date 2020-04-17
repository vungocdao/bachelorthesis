import requests
import csv
from bs4 import BeautifulSoup

r = requests.get('https://www.repustate.com/sentiment-analysis-api-demo/').text

# scrape information out of website
# soup = BeautifulSoup(r, 'lxml')
# sentimentScore = soup.select('strong')
# inputText = soup.find('textarea', class_='ctrl').decode_contents()

# Create csv file
# csv_file = open('repustate.csv', 'w')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['sentimentScore', 'inputText'])
# csv_file.close()

# print(dir(r)) gives all methods and attributes, help
# <textarea name='text' class='ctrl' id='id_text'> Insert Reviews into this
# <button class='btn btn--primary' type='submit'> button
# in <td>, <strong> sentiment value
