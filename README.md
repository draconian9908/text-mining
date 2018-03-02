# Text Mining

This is the homepage for the Olin Spring 2018 Software Design Text Mining project as done by Lydia Hodges.

## Project Overview

I used Project Gutenberg to mine text for the first segment of the project and a combination of online PDFs and pitt.edu for the second segment. Cosine similarity via Python was used on the texts to determine similarity between the different writings.

## Implementation

For the [text mining](text_mining.py) of the first segment, I chose to import the plain text version of several fiction novels from 1894 off Project Gutenberg, save the text from each novel to directly to its own file, and edit the Project Gutenberg header and footer out of each of them manually. For the text mining of the second segment, I copied the text from the online PDFs of several of the original stories behind Disney classics into separate files within Atom and saved them.

I ended up choosing not to pickle the text data I gathered because it was easier for me to directly manipulate the open file objects created by savinf and opening the separate files directly. Pickling added extra steps and complicated the reading process, so I did away with it.

For the text analysis for both segments, I used a combination of dictionaries, lists, and sets to create multidimensional vectors for each piece of writing, and then to compare them using cosine similarity. The equation I used for cosine similarity is:
```∑(Aᵢ * Bᵢ) / (√(∑Aᵢ) * √(∑Bᵢ))```, where `A` and `B` are dictionaries that represent those multidimensional vectors.

## Results

In the [first segment](text_processing.py), when comparing contemporary fiction novels, the similarities between the texts was very low, as shown below. This may be due in part to the differences in lengths, and therefore number of unique words, in the different novels I used.

| [Pan](pan.txt) | [Pembroke](pembroke.txt) | [The Jungle Book](jungle.txt) | [The Last Cruise of the Spitfire](spitfire.txt) | [The Triumph of Death](death.txt) |
| --- | --- | --- | --- | --- |
| 1.0 | 0.181 | 0.166 | 0.173 | 0.157 |
| 0.181 | 1.0 | 0.178 | 0.198 | 0.195 |
| 0.166 | 0.178 | 1.0 | 0.175 | 0.147 |
| 0.173 | 0.198 | 0.175 | 1.0 | 0.151 |
| 0.157 | 0.195 | 0.147 | 0.151 | 1.0 |

In the [second segment](disney_mining/disney_processing.py), when comparing the original stories that Disney abridged and took inspiration from, there was, again, very little similarity. These were closer in length, however, they were almost all written by differnt people and at different times, so the dissimilarities show the differences in styles bewteen people and time. *Note: the titles in the table are the Disney versions. The originals are listed underneath.*

| [Cinderella](disney_mining/cinderella.txt) | [The Little Mermaid](disney_mining/mermaid.txt) | [The Beauty and the Beast](disney_mining/beast.txt) | [Sleeping Beauty](disney_mining/sleep.txt) | [Snow White](disney_mining/snow.txt) |
| --- | --- | --- | --- | --- |
| 1.0 | 0.135 | 0.144 | 0.167 | 0.204 |
| 0.135 | 1.0 | 0.171 | 0.120 | 0.148 |
| 0.144 | 0.171 | 1.0 | 0.146 | 0.169 |
| 0.167 | 0.120 | 0.146 | 1.0 | 0.179 |
| 0.204 | 0.148 | 0.169 | 0.179 | 1.0 |

*Cinderella; The Little Mermaid; La Belle et la Bête; Sun, Moon, and Talia; Little Snow-White*

## Reflection

Overall, my project could have been much better. I experienced quite the setback when I lost all my files and found that I hadn't pushed to GitHub, so I had to start the project over very close to the deadline. This is definitley a good example of why it is important to always push to GitHub, often. Still, I did complete the project, and I did do a little extra by making the additional analysis os the Disney origin stories. I would have liked to have either compared the texts using sentiment or create a good visual of the data I did gather using MSD.
