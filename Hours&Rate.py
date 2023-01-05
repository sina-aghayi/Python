interH = input('Hours :')
interR = input('Rate :')
hour = int(interH)
rate = int(interR)

if hour > 40 :
    times = float(hour) - 40
else :
    times = 0

pay1 = 0.5 * float(rate) * times
pay2 = float(hour) * float(rate) + pay1
print(pay2)        