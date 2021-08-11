import random
default_regret_profile = [.33,.33,.33]
import time

def action(regret_profile):
  random_num = random.uniform(0,1) 
  if random_num < regret_profile[0]:
    choice = 'r'
  elif random_num < (regret_profile[0]+regret_profile[1]):
    choice = 'p'
  else:
    choice = 's'
  return choice


def u(a1,a2):
  if a1 == 'r':
    if a2 == 'r':
      return 0
    elif a2 == 'p':
      return -1
    elif a2 == 's':
      return 1
  elif a1 == 'p':
    if a2 == 'r':
      return 1
    elif a2 == 'p':
      return 0
    elif a2 == 's':
      return -1
  elif a1 == 's':
    if a2=='r':
      return -1
    elif a2 == 'p':
      return 1
    elif a2 == 's': 
      return 0


def regret(a1,a2):
  regret_profile = [0,0,0]

  regret_profile[0] = u('r',a2) - u(a1,a2)
  regret_profile[1] = u('p',a2) - u(a1,a2)
  regret_profile[2] = u('s',a2) - u(a1,a2)

  #use zero for negative regret
  for x in range(3):
    if regret_profile[x] < 0:
      regret_profile[x]=0
  return regret_profile  

trained_regret_profile = [0,1,0]
total_regrets = [0,1,0]
total_actions = 1
print( 'First Strategy:')
print('rock: '+str(round(trained_regret_profile[0]*100,4))+'%, '+'paper: '\
        +str(round(trained_regret_profile[1]*100,4))+'%, '+'scissors: '\
        +str(round(trained_regret_profile[2]*100,4))+'%')
print('')
for y in range(9):
  a1 = action(trained_regret_profile)
  a2 = action(trained_regret_profile)
  if a1 == 'r':
    aa1 = 'rock'
  elif a1 == 'p':
    aa1 = 'paper'
  elif a1 == 's':
    aa1 = 'scissors'
  if a2 == 'r':
    aa2 = 'rock'
  elif a2 == 'p':
    aa2 = 'paper'
  elif a2 == 's':
    aa2 = 'scissors'
  print('you: '+aa1,'opponent: '+aa2)
  current_regrets = regret(a1,a2)
  current_actions=0
  #print(current_regrets)
  for x in range(3):
    current_actions+=current_regrets[x]
  #print(current_actions)
  total_actions += current_actions
  current_actions=0
  #compute new regret profile
  for x in range(3):  
    total_regrets[x] += current_regrets[x]
    #print(total_regrets)
    if total_actions > 0:
      trained_regret_profile[x]=round(total_regrets[x]/total_actions,3)
    else:
      trained_regret_profile[x]=0
  #print (trained_regret_profile)
  print('rock: '+str(round(trained_regret_profile[0]*100,4))+'%, '+'paper: '\
        +str(round(trained_regret_profile[1]*100,4))+'%, '+'scissors: '\
        +str(round(trained_regret_profile[2]*100,4))+'%')
  print('')

for y in range(1000000):
  a1 = action(trained_regret_profile)
  a2 = action(trained_regret_profile)
  #print(a1,a2)
  current_regrets = regret(a1,a2)
  #print(current_regrets)
  for x in range(3):
    current_actions+=current_regrets[x]
  #print(current_actions)
  total_actions += current_actions
  current_actions=0
  #compute new regret profile
  for x in range(3):  
    total_regrets[x] += current_regrets[x]
    #print(total_regrets)
    if total_actions > 0:
      trained_regret_profile[x]=total_regrets[x]/total_actions
    else:
      trained_regret_profile[x]=0
  #print (trained_regret_profile)

#print (trained_regret_profile)
print('After many iterations:')
print('rock: '+str(round(trained_regret_profile[0]*100,2))+'%, '+'paper: '\
        +str(round(trained_regret_profile[1]*100,2))+'%, '+'scissors: '\
        +str(round(trained_regret_profile[2]*100,2))+'%')
