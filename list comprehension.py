prices = [10, 38, 40, 58, 62]

halved_loop = []
for price in prices:
    half_price = price/2
    halved_loop.append(half_price)

print(halved_loop)

#The list comprehension creating halved_lc is and equivalent, 
# but more compact version of the code creating halved_loop

halved_lc = [price/2 for price in prices ] 
print(halved_lc)


# We can pick the operations we want to apply to each price value in a function like halve(), 
# and use it as an expression.

prices = [10, 22, 30, 40, 58]

def halve(num):
      return num/2

halved = [halve(price) for price in prices] # halve(price) calls out the function halve(num)

print(halved)

# We created the list in high_scores by looping through each score in scores, 
# copying the score only if it's greater than 20.

scores = [12, 47, 30, 29, 19, 35]

high_scores = [score for score in scores if score > 20]

print(high_scores)
