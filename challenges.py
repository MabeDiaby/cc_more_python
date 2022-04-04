# Shortest Word

def shortest_word(s): 
    # your lovely code here!
    return 'hello world'
 # when word < the previous -> moves on to the list of short words len(word)
def shortest_word(s):
    shortest = min(s.split(), key=len)
    return len(shortest)

print(shortest_word("I don't think that word means what you think it means"))
# should return: 1

# Sum of Minimums

def sum_of_minimums(list):
    # your lovely code goes here!
    return 'hello world'

def sum_of_minimums(list):
    sum = 0
    for nums in list:
        sum += min(nums)
    return sum

# or


my_list = [
    [1,2,3,4,5], # minimum value of row is 1
    [5,6,7,8,9], # minimum value of row is 5
    [20,21,34,56,100] # minimum value of row is 20
    ]

result = sum(map(min, my_list))
print(result)

print(sum_of_minimums(my_list))
    # should return 26
  
# Split Strings

def split_strings(s):
    # your lovely code goes here
    list = []
    if len(s) % 2 != 0:
        s += "_"
    for let in range(0, len(s), 2):
        list.append(s[let : let + 2])
    return list

print(split_strings('abc'))
# should return ['ab', 'c_']

print(split_strings('abcdef'))
# should return ['ab', 'cd', 'ef']
