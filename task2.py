import re

sum=0
try
  with open(file='.prices.txt', 'r', encoding='utf-8') as info_f
    i=0
    for line in info_f:
      i=i+1
      list=re.split(r'\s+', line.strip())
      try:
        ql=int(list[1])
        pr=int(list[2])
        sum=sum+ql*pr
      except FileNotFoundError:
        print('файл не обнаружен')

print('Общая стоимость заказа', sum)
