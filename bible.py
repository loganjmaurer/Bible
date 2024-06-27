import re
import pandas as pd
import markovify
import random

# Define the regular expression pattern to match the verse format
pattern = r'(\w{3})\|(\d+)\|(\d+)\|(.*)'

# Read the KJV file
with open('kjvdat.txt', 'r') as f:
    kjv_data = f.readlines()

# Read the Apocrypha file
with open('apodat.txt', 'r') as f:
    apocrypha_data = f.readlines()

# Combine the two datasets
all_data = kjv_data + apocrypha_data

# Create an empty list to store the verse data
verses = []

# Loop through each line and extract the verse information
for line in all_data:
    match = re.match(pattern, line.strip())
    if match:
        book, chapter, verse, content = match.groups()
        verses.append({'Book': book, 'Chapter': int(chapter), 'Verse': int(verse), 'Content': content})

# Create the DataFrame
df = pd.DataFrame(verses)

# Display the first few rows
print(df.head())

# Create the Markov chain model
text_model = markovify.Text('\n'.join(df['Content']), state_size=5)

# Generate a new "Bible" text
new_bible_text = []
for i in range(100):
    new_verse = text_model.make_short_sentence(max_chars=500, max_overlap_total=400, tries=150)
    if new_verse:
        new_bible_text.append(new_verse)

print('\n'.join(new_bible_text))
