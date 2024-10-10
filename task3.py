import re

try:
  with open(file='.\text_file.txt', 'r', encoding='utf-8') as info_f:
    count=0
    for line in info_f:
      a=line.strip().split()
      for x in a:
        if re.search(r'[a-z,A-Z,а-я,А-Я,0-9]',x):
          count=count+1

except FileNotFoundError:
  print()
