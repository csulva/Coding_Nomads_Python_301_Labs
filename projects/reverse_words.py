# Complete the solution so that it reverses all of the words within the string passed in.

# Example:
# "The greatest victory is that which requires no battle" --> "battle no requires which that is victory greatest The"

test = "The greatest victory is that which requires no battle"
new_list = test.split()
another_list = []
for words in new_list:
    another_list.insert(0, words)

list_the_third = ' '.join(x for x in another_list)
print(list_the_third)