#("PROGRAM BILANGAN TERBESAR DARI 3 BUAH BILANGAN YANG DIINPUTKAN")
a=int(input("Masukan Bilangan A: "))
b=int(input("Masukan bilangan B: "))
c=int(input("Masukan bilangan C: "))
if (a > b) and (a > c):
 print("Bilangan terbesar adalah :",a,)
elif (b > a) and (b > c):
 print("Bilangan terbesar adalah :",b,)
else:
 print("Bilangan terbesar adalah :",c,)
