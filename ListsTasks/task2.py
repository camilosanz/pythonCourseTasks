# The Flying Python Circus wants to create a program to keep track of their performances and daily schedule. 
# Let's start by creating a list to store all of the names of the performances.
performances_names = ['Ventriloquism', 'Amazing Acrobatics', 'Snake Charmer', 'Bearded Lady', 'Tiniest Man']
# Start by creating a list called performances with two performances in it: 'Ventriloquism' and 'Amazing Acrobatics'.
performances = ['Ventriloquism', 'Amazing Acrobatics']
# Let's add 'Snake Charmer' to our performances list.
performances.append('Snake Charmer')
# Let's add 'Bearded Lady' and the 'Tiniest Man' to our performances list.
[ performances.append(performance) for performance in ['Bearded Lady', 'Tiniest Man'] ]
# Let's see our updated list by printing it to the screen
print(performances)
# Our list of performances has grown, but the 'Bearded Lady' and the 'Tiniest Man' have moved on, so let's remove them both from our performances list.

# Remove 'Bearded Lady' from the list 
performances.remove('Bearded Lady')
# Remove 'Tiniest Man' from the list 
performances.remove('Tiniest Man')
# Let's see our updated list by printing it to the screen.
print(performances)