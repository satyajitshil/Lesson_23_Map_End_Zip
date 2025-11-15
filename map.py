set1 = [1,2,3,4,5,6,7,8,9,10]
def sq(n):
    return n**2
x = list(map(sq, set1))
print(x)

set2 = [1,2,3]
set3 = [4,5,6]
result = map(lambda x,y : x + y, set2, set3)
print(list(result))