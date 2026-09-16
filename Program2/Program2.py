#LeftwichP2
#Programmer: Logan Leftwich
#Email: lleftwich1@student.cnm.edu
#Purpose: Look up US state information

#Initialize the four lists
states = ('Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware',
'Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana',
'Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska',
'Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio',
'Oklahoma','Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee','Texas',
'Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming')

capitals = ('Montgomery','Juneau','Phoenix','Little Rock','Sacramento','Denver','Hartford','Dover',
'Tallahassee','Atlanta','Honolulu','Boise','Springfield','Indianapolis','Des Moines','Topeka',
'Frankfort','Baton Rouge','Augusta','Annapolis','Boston','Lansing','Saint Paul','Jackson',
'Jefferson City','Helena','Lincoln','Carson City','Concord ','Trenton','Santa Fe','Albany','Raleigh',
'Bismarck','Columbus','Oklahoma City','Salem','Harrisburg','Providence','Columbia','Pierre','Nashville',
'Austin','Salt Lake City','Montpelier','Richmond','Olympia','Charleston','Madison','Cheyenne')

districs = (7,1,9,4,52,8,5,1,28,14,2,2,17,9,4,4,6,6,2,8,9,13,8,4,8,
2,3,4,2,12,3,26,14,1,15,5,6,17,2,7,1,9,38,4,1,11,10,2,8,1)

order = (22,49,48,25,31,38,5,1,27,4,50,43,21,19,29,34,15,18,23,7,6,
26,32,20,24,41,37,36,9,3,47,11,39,12,17,46,33,2,13,40,8,16,28,45,14,10,42,35,30,44)

#Greet
print()
print('Welcome to State Info Search')
print('This program will provide you the capital, number of congresional districts, and order in which the state joined the union of a given state.')

#Ask user to enter a name of state
print()
state_name = input('Please enter state name: ')

#Find index of name
state_index = states.index(state_name)

#Assign variable for index
states_capital = capitals[state_index]
states_district = districs[state_index]
states_order = order[state_index]

#Display results
print(f'The capital of {state_name} is {states_capital}. It has {states_district} congressional districts and it is state number {states_order} in the union.')

#Thank
print() 
print('Thank you for using State Info Finder!')