# LeftwichP4
# Logan Leftwich
# Email: lleftwich1@student.cnm.edu
# Purpose: Demonstrate the use of Python dictionaries.

# Create dictionaries
Dictionary = {
'Greetings' : {
    'Hello': 'Hola',
    'Good morning': 'Buenos días',
    'Good afternoon': 'Buenas tardes',
    'Good evening': 'Buenas noches',
    'How are you?': '¿Cómo estás?',
    'Nice to meet you': 'Mucho gusto',
    'What is your name?': '¿Cómo te llamas?',
    'My name is': 'Me llamo',
    'How is it going?': '¿Qué tal?',
    'Welcome': 'Bienvenido'
},

'Common phrases' : {
    'Please': 'Por favor',
    'Thank you': 'Gracias',
    'You are welcome': 'De nada',
    'Yes': 'Sí',
    'No': 'No',
    'Excuse me': 'Disculpe',
    'I am sorry': 'Lo siento',
    'I do not understand': 'No entiendo',
    'Can you help me?': '¿Puedes ayudarme?',
    'Where is the bathroom?': '¿Dónde está el baño?',
    'How much does it cost?': '¿Cuánto cuesta?',
    'I would like': 'Me gustaría',
    'What time is it?': '¿Qué hora es?',
    'I am hungry': 'Tengo hambre',
    'I am thirsty': 'Tengo sed'
},

'Goodbyes' : {
    'Goodbye': 'Adiós',
    'See you later': 'Hasta luego',
    'See you tomorrow': 'Hasta mañana',
    'See you soon': 'Hasta pronto',
    'Take care': 'Cuídate',
    'Have a good day': 'Que tengas un buen día',
    'Good night': 'Buenas noches',
    'Farewell': 'Hasta la vista',
    'It was nice seeing you': 'Fue un placer verte',
    'Until next time': 'Hasta la próxima'
},

'Numbers' : {
    'One': 'Uno',
    'Two': 'Dos',
    'Three': 'Tres',
    'Four': 'Cuatro',
    'Five': 'Cinco',
    'Six': 'Seis',
    'Seven': 'Siete',
    'Eight': 'Ocho',
    'Nine': 'Nueve',
    'Ten': 'Diez'
},

'Food/Drink' : {
    'Water': 'Agua',
    'Coffee': 'Café',
    'Bread': 'Pan',
    'Rice': 'Arroz',
    'Chicken': 'Pollo',
    'Fish': 'Pescado',
    'Fruit': 'Fruta',
    'Vegetables': 'Verduras',
    'Breakfast': 'Desayuno',
    'Dinner': 'Cena'
}
}
# Greet
print("\nThis program will allow you to select a category of words/phrases. Then it will allow you to find a word/phrase to translate from English to Spanish. ")

# Display category options
categories = (', '.join(Dictionary.keys()))
print()
print('Categories:',categories)

# Ask user for category and display word/senteces
User_category = input('\nPlease enter category of words/sentences: ')
print()
word_keys = '", "'.join(Dictionary[User_category].keys())
print('"' + word_keys + '"')

# Ask user which word/sentence for translation
User_word = input('\nPlease enter word/sentence to translate: ')
print()
User_category = Dictionary[User_category]
translated_word = User_category[User_word]
print(f'The word/phrase "{User_word}" in spanish is "{translated_word}"')
print()
print("Thank you for using my translator!")
print()