answer= input('What is the answer to great question of life, the universe and everything?: ')
answer= answer.lower().strip()
if answer in ['42', 'forty-two', 'forty two']:
   print('Yes')
else:
   print('No')
