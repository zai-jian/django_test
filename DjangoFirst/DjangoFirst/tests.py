import random
list1 = ['red','blue','green','orange','yellow','pink','purple']
string = "<table border=1>"
for i in range(1, 10):
    string += '<tr background="purple">'
    for j in range(1, i+1):
        string += '<td> '+ str(j) + '*' +str(i)+ str(i *j)+'</td>'
    string += '</tr>'
string += '</table> '
print(random.choice(list1))

