import pandas as pd
aa = { 'imy': ['Настя', 'коля', 'Вика' , 'Борис', 'Анна' , 'Андрей', 'Оля', 'Витя', 'Маша', 'Миша',],
'matematik': [4,5,3,4,5,5,3,4,4,3],
'istori': [4,4,4,3,3,5,5,3,3, 5],
'biolog': [5,5,5,5,5,5,5,5,5,5],
'fizik': [5,4,3,5,4,3,5,4,3,5],
'literat': [3,3,5,5,4,5,4,3,5,4]}
tt = pd.DataFrame(aa)
print(tt.head())
print("Средние значения по каждому предмету ")
print(tt['matematik'].mean())
print(tt['istori'].mean())
print(tt['biolog'].mean())
print(tt['fizik'].mean())
print(tt['literat'].mean())

print("Медианные значения по каждому предмету ")
print(tt['matematik'].median())
print(tt['istori'].median())
print(tt['biolog'].median())
print(tt['fizik'].median())
print(tt['literat'].median())
print("Первый и третий квартиль")

Q1 = tt['matematik'].quantile(0.25)
Q3 = tt['matematik'].quantile(0.75)
print(Q1)
print(Q3)

print('Межквартальный размах')
IQR = Q3 - Q1
print(IQR)

print("стандартное отклонение для предмета matematik ")
print(tt['matematik'].std() )
































