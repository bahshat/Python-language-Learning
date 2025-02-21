# Tuples can't add remove elements
a_tuple = ('apple', 'banana')
print(a_tuple[1])

# List can add remove elements
a_list = ['Apple', 'Grapes', 'Mango']
print(a_list)



# set can't have duplicate entries
# will not have same order in which elements added
a_set = {'Nano', 'Mobilio', 'i10', 'i10'}
print(a_set)


# subscript notation
a_list[0] = 'Seb' # list can be modified

a_list.append('Pineapple')
print(a_list)

a_list.remove('Pineapple')
print(a_list)

a_tuple[0] = 'Saparchand' # tuple can not be modified once created

a_set.add('Swift')