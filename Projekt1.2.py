a=float(input())          #объем бензина в галлонах
l=a*4                     #объем бензина в литрах
l=round(l,2)
b=l/19.5                  #баррели нефти для такого объма бензина
b=round(b,0)
c=b*20                    #объем углекислого газа при сжигании этого бензина в фунтах
c=round(c,2)
e=(a*115000)/75700        #относительный объем этанола в галлонах
e=round(e,2)
p=a*3                     #стоимость в доллорах
p=round(p,2)
#Средний расход бензина для человека из России в год. Без учета дизеля и ГАЗа.
#Статистика России 2015 года.
# x-численность населения России в млн.;
# y-общий объем потребляемого бензина за год в млн кг.
# z-количество потребляемого бензина на человека в год.
x=144
y=38600
z=y/x
#n-численность Новосибирска млн.
#f-потребление бензина за год в млн. кг.
#d-среднее потребление бензина в день.
n=1.567
f=650
d=f/(n*365)
print("Литров бензина:",l)
print("Баррелей нефти:",b)
print("Объем углекислого газа при сжигании:",c)
print("Эквивалентный объем этанола:",e)
print("Стоимость в долларах:",p)
print("Среднее потребление бензина на человека в России за год:",z)
print("Среднее потребление бензина на человека из Новосибирска за день:",d)

