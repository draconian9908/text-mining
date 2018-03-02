""" Text Mining
    Lydia Hodges
    Collecting Texts for Analysis"""

import requests
import pickle

all_texts = []
last_cruise_spitfire_full_text = requests.get('https://www.gutenberg.org/ebooks/34367.txt.utf-8').text
pan_full_text = requests.get('https://www.gutenberg.org/files/7214/7214-0.txt').text
jungle_book_full_text = requests.get('https://www.gutenberg.org/ebooks/35997.txt.utf-8').text
pembroke_full_text = requests.get('https://www.gutenberg.org/ebooks/17428.txt.utf-8').text
death_triumph_full_text = requests.get('https://www.gutenberg.org/files/54272/54272-0.txt').text

print(death_triumph_full_text)


"""all_texts.append(last_cruise_spitfire_full_text)
all_texts.append(pan_full_text)
all_texts.append(jungle_book_full_text)
all_texts.append(pembroke_full_text)

f1 = open('spitfire.pickle', 'wb')
pickle.dump(last_cruise_spitfire_full_text, f1)
f1.close()

f2 = open('pan.pickle', 'wb')
pickle.dump(pan_full_text, f2)
f2.close()

f3 = open('jungle.pickle', 'wb')
pickle.dump(jungle_book_full_text, f3)
f3.close()

f4 = open('pembroke.pickle', 'wb')
pickle.dump(pembroke_full_text, f4)
f4.close()
"""
