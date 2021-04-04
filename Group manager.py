import math

print('The possible answers are : Yes,yes,YES,+')

band={'Jenny':
      {'name':'Jennie','age':25,'job':'main raper and vocalist'},
      'Lisa':
      {'name':'Pranpriya','age':24,'job':'main dancer and raper'},
      'Rose':
      {'name':'Rosie','age':24,'job':'main vocalist'}}

concert_spendings=[]

concerts_data={'Seoul':
               {'spendings':'10000 $','budget':'65000 $','date':'23.03.2021'},
               'Ankara':
               {'spendings':'55555 $','budget':'65000 $','date':'07.01.2021'},
               'Tokyo':
               {'spendings':'50000 $','budget':'65000 $','date':'22.03.2020'},
               'Chicago':
               {'spendings':'14000 $','budget':'65000 $','date':'12.06.2020'},
               'NY':
               {'spendings':'52000 $','budget':'65000 $','date':'30.03.2021'}
               }

li=[]

#  Создаем отдельный лист для утвердительных ответов
affirmations=['yes','Yes','YES','+']

#  Удаляем участника из списка
def band_cancel(idol,band):
  del band[idol]
  return band
 
#  Добавляем нового участника
def new_participant(idol,idol_name,idol_age,idol_job,band):
  band[idol]={}
  band[idol]['name']=idol_name
  band[idol]['age']=idol_age
  band[idol]['job']=idol_job
  return band


#   Подчитываем общую сумму затрат за концерт

def spendings(ll):    # У меня не получилось назначать аргументы по отдельности : я их храню в списке (заранее)
  total_spendings=str(sum(ll))+' $'
  return total_spendings


#   Записываем все полученные данные о предстоящем концерте в словарь с данными о концертах
def new_concert(concerts_data,city,concert_spendings,date1):
  concerts_data[city]={}
  concerts_data[city]['spendings']=spendings(concert_spendings)
  concerts_data[city]['date']=date1
  concerts_data[city]['budget']='65000 $'

def profit(x):
  general_income=65000-x
  print()
  print('The profit from this concert will be approximately',general_income,'$')
  return general_income

#   Выводим имена участников , чтобы пользователь имел информацию о составе группы
band_list=['Jenny','Lisa','Rose']
for i in range(len(band_list)):
  if i==0:
    print('The list of group\'s participants : ')
  if i+1==len(band_list):
    print(band_list[i])
  else:
    print(band_list[i],end=' , ')
print()
#   Спрашиваем , нужно ли убрать участника из группы
data=input('Do you want to cancel a group participant ? : ')
if data in affirmations:
  cancel_idol=input('Who you\'d like to cancel ? : ')
  band_cancel(cancel_idol,band)
  print(cancel_idol,'was removed from the band\'s list')

#   Спрашиваем , нужно ли добавить нового участника
data1=input('Do you want to add a new idol ? : ')
if data1 in affirmations:
  new_idol=input('Who you\'d like to add ? : ')
  idol_name=input('Idol\'s name : ')
  idol_age=int(input('Idol\'s age : '))
  idol_job=input('Idol\'s job : ')
  new_participant(new_idol,idol_name,idol_age,idol_job,band)
  print(new_idol,'was addded to band\'s list')

#   Спрашиваем , запланированы ли концерты
data2=input('Do you want to add a new concert ? : ')
if data2 in affirmations:
  city=input('Where the concert will take place ? : ')
  concert_spendings=input('Write the spendings down \n (One by one) : ').split()
  for i in range(len(concert_spendings)):
    concert_spendings[i]=int(concert_spendings[i])
  date1=input('When the concert will be ? : ')
  new_concert(concerts_data,city,concert_spendings,date1)
  li.append(profit(int(str(concerts_data[city]['spendings'])[:-2])))
  print('New concert\'s data is added to the list )))')
  
def total_money(concerts_data,x):
  for i in concerts_data:
    spend=int(str(concerts_data[i]['spendings'])[:-2])
    prof=65000-spend
    x+=prof
  return x
total_profit=0
print('The total profit of concerts is :',total_money(concerts_data,total_profit))

  
#   Выводим данные об уастниках группы и списке концертов , чтобы не запутаться
print()
print()
print(band)
print()
print()
print(concerts_data)
