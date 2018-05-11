
# the answer is when you say it literally
def get_next(num):
    result = ""
    strNum = str(num) # expect num to be number change it to a str
   
    relpos = 0 # relative number position
    order = [] 
    freq = {} 
    for char in strNum:
        if len(order) == 0:
            order.append(char) 
        elif order[-1] != char:
            relpos += 1
            order.append(char) 
        freq[(relpos, char)] = freq.get((relpos, char), 0) + 1
    
    for inx, ind in enumerate(order):
        result += str(freq[(inx, ind)])
        result += ind

    return result

a = []
a.append(1)

for index in range(30):
    a.append(get_next(a[index]))


print(str(len(a[30])))

