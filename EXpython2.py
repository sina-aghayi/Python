a = int(input("enter a number :"))
if a > 3 :
    print('Bigger than 3')
    print('Still bigger')
print('Done with 3')

for i in range(a) :
    print(i)
    if i > 3 : 
        print('Bigger than 3')
    print('Done with i', i)
print('All Done')
