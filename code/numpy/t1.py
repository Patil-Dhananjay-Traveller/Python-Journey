from numpy import array
import numpy as np

'''my_list = [1,2,3,4,5]

my_list = my_list * 2

print(my_list)'''

'''array = np.array([1,2,3,4,5])
array = array * 2
print(array)
print(type(array))'''

#array = np.array('A')

'''array = np.array([
    [
        ['Mumbai', 'Delhi', 'Pune', 'Chennai'],
        ['Kolkata', 'Hyderabad', 'Jaipur', 'Lucknow'],
        ['Surat', 'Nagpur', 'Indore', 'Bhopal'],
        ['Agra', 'Kanpur', 'Patna', 'Ranchi']
    ],
    [
        ['London', 'Paris', 'Berlin', 'Rome'],
        ['Madrid', 'Lisbon', 'Vienna', 'Prague'],
        ['Athens', 'Dublin', 'Oslo', 'Stockholm'],
        ['Helsinki', 'Warsaw', 'Budapest', 'Zurich']
    ],
    [
        ['New York', 'Chicago', 'Boston', 'Seattle'],
        ['Los Angeles', 'Houston', 'Miami', 'Dallas'],
        ['Phoenix', 'Denver', 'Atlanta', 'Detroit'],
        ['Orlando', 'Austin', 'San Diego', 'Portland']
    ],
    [
        ['Tokyo', 'Seoul', 'Beijing', 'Shanghai'],
        ['Bangkok', 'Singapore', 'Kuala Lumpur', 'Jakarta'],
        ['Dubai', 'Doha', 'Muscat', 'Riyadh'],
        ['Sydney', 'Melbourne', 'Perth', 'Brisbane']
    ]
])


word = array[0,0,0]  + array[1,0,0]+ array [2,0,0]
print(word)
print(array[0,0,0]) #Mumbai
print(array[0,0,1]) #Delhi
print(array[0,0,2]) #Pune
print(array[0,1,0]) #Kolkata
print(array[0,1,1]) #Hyderabad
print(array[1,1,1]) #Lisbon
print(array[3,3,3]) #Brisbane'''
#{print(array.shape)
#(4 layers, 4 rows, 4 columns)}

#print(array)
#print(array.ndim)

array = np.array([[1,2,3,4,5],
                 [6,7,8,9,10],
                 [11,12,13,14,15],
                 [16,17,18,19,20]])

# array [start:end:step]
#print(array[0])
#print(array[-1])
#print(array[0:4])
#print(array[0:4:2])
#print(array[::2])

#column
#print(array[:,0])
#print(array[:,1])
#print(array[:,::2])
#print(array[:,1::2])
#print(array[:,::-1])

#print(array[0:2, 0:2])
print(array[0:2 , 2:])
