class salary:
  def __init__(self, Hours, Rate):
    self.hours = Hours
    self.rate = Rate

  def myfunc(self):
    if Hours < 40:
      money = Rate * Hours
    else:
      overtime = Hours - 40
      money = (Rate * 40.0) + (1.5 * Rate * overtime)
    print('salary : ',money)

inth = input("enter Hours : ")
intr = input("enter Rate : ")
Hours = int(inth)
Rate = int(intr)
salarys = salary(Hours, Rate)
salarys.myfunc()