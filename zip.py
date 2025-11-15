s1 = {6,7,4,1}
s2 = {'f','i','v','e'}
s3 = list(zip(s1, s2))
print(s3,'\n')

l1 = [6,7,4,1]
l2 = ['f','i','v','e']

for x,y in zip(l1,l2[::-1]):
    print(x,y)

stocks = ['Smyth Inc.','Iron Bear','NRI']
prices = [983423,908922,218833]

d1 = {stocks:prices for stocks,prices
      in zip(stocks,prices)}

print(d1)

