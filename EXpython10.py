x = input('enter a number :')
try: 
    int1 = int(x)
except: 
    int1 = -1

if int1 > 0 :  
    print('Well done ')
else:  
    print('Not a number')
