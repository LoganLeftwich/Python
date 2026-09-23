# LeftwichP3
# Programmer: Logan Leftwich
# Email: lleftwich1@student.cnm.edu
# Purpose: Provides user capability to find fruit in a string

# set up the variables
fruits = [ 'Apricot', 'Apple',	'Asian Pear',	'Avocado',	'Banana',	'Blackberries',
	'Blueberries',	'Boysenberries',	'Cactus Pear',	'Cantaloupe',	'Cherries',
    'Coconut',	'Cranberries',	'Figs',	'Gooseberries',	'Grapefruit',	'Grapes',
    'Honeydew Melon',	'Kiwifruit',	'Limes',	'Longan',	'Loquat', 'Lychee',	
    'Madarins',	'Malanga',	'Mandarin Oranges',	'Mangos',	'Mulberries',	
    'Nectarines',	'Oranges',	'Papayas',	'Passion Fruit',	'Peaches',	'Pears',
    'Persimmons',	'Pineapple',	'Plums',	'Pomegranate',	'Prunes',	'Quince',
    'Raisins',	'Raspberries',	'Rhubarb',	'Strawberries',	'Tangelo',	'Tangerines',
    'Tomato',	'Ugli Fruit',	'Watermelon'
]

# Build lower case list with singular and plural versions of every fruit
# Spaces in two word fruits become underscores so each fruit is one item
fruits_joined = '|'.join(fruits).lower().replace(' ', '_') + '|'
singular = fruits_joined.replace('s|', '|')
plural = fruits_joined.replace('|', 's|')
irregular = fruits_joined.replace('ies|', 'y|').replace('ches|', 'ch|')
fruits_lower = (fruits_joined + singular + plural + irregular).split('|')

# Ask user for sentence
print()
fruit_sentence = input('Please enter a sentence with fruit in it: ')

# Lower case copy of the sentence, with punctuation turned into spaces
sentence_lower = fruit_sentence.lower()
sentence_clean = sentence_lower.replace(',', ' ').replace('.', ' ').replace('!', ' ').replace('?', ' ').replace(':', ' ').replace(';', ' ')

# Join each two word fruit with an underscore so it stays together as one word
sentence_clean = sentence_clean.replace('asian pear', 'asian_pear')
sentence_clean = sentence_clean.replace('cactus pear', 'cactus_pear')
sentence_clean = sentence_clean.replace('honeydew melon', 'honeydew_melon')
sentence_clean = sentence_clean.replace('mandarin orange', 'mandarin_orange')
sentence_clean = sentence_clean.replace('passion fruit', 'passion_fruit')
sentence_clean = sentence_clean.replace('ugli fruit', 'ugli_fruit')

# Split the cleaned sentence into individual words
sentence_words = sentence_clean.split()

# Find fruits that appear in both the list and the user's sentence
intersecList = list(set(sentence_words) & set(fruits_lower))

if len(intersecList) > 0:
    # Put the spaces back into two word fruits for display
    shown_fruits = '|'.join(intersecList).replace('_', ' ').split('|')
    print('\nI found %d fruits in your sentence.' % len(intersecList))
    print('Your fruits are: %s' % shown_fruits)

    # Replace one fruit with Brussel Sprouts
    match = intersecList[0]
    padded = ' ' + sentence_clean + ' '
    start = padded.find(' ' + match + ' ')
    end = start + len(match)
    new_sentence = fruit_sentence[:start] + 'Brussel Sprouts' + fruit_sentence[end:]
    print('Your sentence with some brussel sprouts: "%s"' % new_sentence)
    print()
else:
    print('\nI did not find any fruits in your sentence')
    print()
