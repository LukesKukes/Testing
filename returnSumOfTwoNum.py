"""Board game where u can roll a dice and if you land on the enemy piece u take them out or wth"""

a = 1
b = 8
def posBon(x,y):
    if abs(x-y) <= 6:
        return True
    else:
        return False
#print(posBon(a,b))


