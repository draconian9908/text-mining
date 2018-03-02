""" Text Mining
    Lydia Hodges
    Collecting Texts for Analysis"""

import requests

last_cruise_spitfire_full_text = requests.get('https://www.gutenberg.org/ebooks/34367.txt.utf-8').text
pan_full_text = requests.get('https://www.gutenberg.org/files/7214/7214-0.txt').text
jungle_book_full_text = requests.get('https://www.gutenberg.org/ebooks/35997.txt.utf-8').text
pembroke_full_text = requests.get('https://www.gutenberg.org/ebooks/17428.txt.utf-8').text
death_triumph_full_text = requests.get('https://www.gutenberg.org/files/54272/54272-0.txt').text

print(death_triumph_full_text)
