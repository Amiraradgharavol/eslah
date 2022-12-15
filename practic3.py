name = input("plz enter your name: ")
famili = input("plz enter your famili: ")

a = float(input("plz enter frist score: "))
b = float(input("plz enter secend score: "))
c = float(input("plz enter third score: "))
avrage = (a + b + c) / 3

if avrage >= 17:
    print(name, famili , " avrage is great")
if avrage < 17 and avrage >= 12:
    print(name, famili, " avrage is normal") 
if avrage < 12:
    print(name , famili , " avrage is failed")       