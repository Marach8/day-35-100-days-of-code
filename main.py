import time, os

list = []
def menu():
  r = '\033[4mMY TODO LIST📝\033[0m'
  print(f'\033[1m{r:^50}')
  time.sleep(0.5)
  print()
  print('\033[0mEnter:')
  print()
  time.sleep(0.5)
  print('\033[1;33m"\033[32m1\033[1;33m" to view Todo List')
  print()
  time.sleep(0.5)
  print('"\033[32m2\033[1;33m" to edit Todo List')
  print()
  time.sleep(0.5)
  print('"\033[32m3\033[1;33m" to add a Todo to your List.')
  print()
  time.sleep(0.5)
  print('"\033[32m4\033[1;33m" to remove Todo List')
  print()
  a = input('\033[34m>> ')
  return a

def view():
  os.system('clear')
  global list
  if len(list) != 0:
    Printer(list)
    time.sleep(20)
  else:
    print('\033[31mYou have no items in your Todo List! Please, add items before you can view them!👿👿\033[0m')
    time.sleep(8)
  os.system('clear')

def edit():
  os.system('clear')
  global list
  if len(list) != 0:
    time.sleep(2)
    print()
    Printer(list)
    print()
    ask = input('\033[36mWhich item do you want to edit in the list above?: ')
    if ask in list:
      print()
      time.sleep(2)
      ask2 = input(f'Type in the correct word for {ask} here: ')
      list.replace(ask, ask2)
      print(f'\033[32m{ask} succesfully edited!😎')
      print()
      Printer(list)
    else:
      print('\033[31mThis item is not in your Todo List!')
  else:
    print('\033[31mYou have no items in your Todo List! Please, add items before you can edit them!👿👿\033[0m')
  time.sleep(10)
  os.system('clear')


def add():
  os.system('clear')
  time.sleep(2)
  global list
  while True:
    ask = input('Enter the item you want to add to your Todo List: ')
    if ask not in list:
      list.append(ask)
    else:
      print()
      print('\033[0mYou already have that item in your list!!😎')
    time.sleep(0.5)
    print()
    ask1 = input('\033[35mWant to add again? y/n: \033[34m')
    print()
    if ask1 == 'y':
      continue
    else:
      break
  print()
  print('\033[32mItems added Succesfully!😊')
  time.sleep(4)
  os.system('clear')


def remove():
  global list
  os.system('clear')
  time.sleep(1)
  while len(list) != 0:
    ask = input('\033[31mEnter: \n1 to remove all.\n2 to remove one\n>> ')
    if ask == '1':
      time.sleep(2)
      querry = input('Are you sure you want to erase the list? This action cannot be reversed!!!!\ny/n >> ')
      if querry == 'y':
        time.sleep(2)
        for i in list:
          list.remove(i)
        print()
        print('\033[32mTodo list erased Succesfully😎')
    elif ask == '2':
      time.sleep(1)
      print()
      Printer(list)
      time.sleep(1)
      print()
      ask2 = input('\033[1;33mEnter the Todo that you want to remove from the list above: ')
      if ask2 in list:
        print()
        time.sleep(2)
        ask3 = input(f'''\033[31mAre you sure you want to remove {ask2}? This action cannot be reversed!!!!''')
        if ask3 == 'y':
          time.sleep(1)
          print()
          list.remove(ask2)
          print(f'\033[32m{ask2} removed Successfully😊')
      else:
        time.sleep(1)
        print()
        print(f'\033[31m{ask2} is not in the Todo List!')
    break
  else:
    print('\033[31mThere are no items in the Todo List! Please enter 3 to add items!!')
  time.sleep(4)
  os.system('clear')


def Printer(a):
  os.system('clear')
  time.sleep(2)
  for j in range(len(a)):
    print()
    print(f'\033[32m({j+1}) : {a[j]}')
    time.sleep(2)
    os.system('clear')
    
  b = '\033[4mMy Todo List\033[0m'
  print(f'\033[35m{b:^55}')
  print()
  
  for i in a:
    print(f'\033[32m{i} ', end='\033[0m|| ')
    time.sleep(1)
  print()


while True:
  b = menu()
  if b == '1':
    view()
  elif b == '2':
    edit()
  elif b == '3':
    add()
  elif b == '4':
    remove()
  else:
    print()
    print('\033[31mPlease, choose 1, 2 or 3 from the menu!')
    time.sleep(4)
    os.system('clear')
    continue
  