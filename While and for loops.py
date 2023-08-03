# While loops condition must be true
i = 1
while i < 5:
    print(i)
    i += 1 # i = i + 1
print("the end")

# for Loops iterate over a sequence
name = ['subscribe', 'to', 'kylie', 'ying']
for x in name:
    print(x)

# Nested For loops
adjs = ['shiny', 'purple', 'clear']
nouns = ['coin', 'speaker', 'iphone']

for adj in adjs:
    for noun in nouns:
        print(adj, noun)

# Control Flow
# break - canceling the entire loop
word_list = ['subscribe', 'to', 'kylie', 'ying']
for name in word_list:
    print(name)
    if name == 'kylie':
        break
print("the end")

i = 1 
while i < 5:
    print(i)
    if i == 3:
        break
    i += 1
print("the end")

# continue - canceling one loop
word_list = ['subscribe', 'to', 'kylie', 'ying']
for name in word_list:
    if name == 'kylie':
        continue
    print(name)
print("the end")



# import turtle
# counter = 1
# while counter <= 4:
#     turtle.forward(100)
#     turtle.right(90)
#     counter += 1
  
   