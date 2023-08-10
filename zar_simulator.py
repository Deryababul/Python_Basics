import random

def zarYuzey(zar):
    zar1= """-------------
|           |
|           |
|     0     |
|           |
|           |
-------------"""
    zar2= """-------------
|           |
| 0         |
|           |
|       0   |
|           |
-------------"""
    zar3= """-------------
| 0         |
|           |
|     0     |
|           |
|         0 |
-------------"""
    zar4= """-------------
| 0       0 |
|           |
|           |
|           |
| 0       0 |
-------------"""
    zar5= """-------------
| 0       0 |
|           |
|     0     |
|           |
| 0       0 |
-------------"""
    zar6= """-------------
| 0       0 |
|           |
| 0       0 |
|           |
| 0       0 |
-------------"""
 

    if zar==1:
        print(zar1)
    elif zar==2:
        print(zar2)
    elif zar==3:
        print(zar3)
    elif zar==4:
        print(zar4)
    elif zar==5:
        print(zar5)
    elif zar==6:
        print(zar6)
   
zar = random.randint(1,7)

zarYuzey(zar)
