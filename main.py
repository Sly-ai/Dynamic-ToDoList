import os

title = "\033[31m=\033[0m=\033[34m=\033[33m To Do List Manager \033[31m=\033[0m=\033[34m="

def printList():
  os.system("clear")
  print(f"{title:^80}\n")
  menu_options = {
      1: viewList,
      2: addItem,
      3: removeItem,
      4: changeItem,
  }
  menu = int(input(
      "ToDoList Manager\n\n What do you want to do?\n 1:view\n 2:add\n 3:remove\n 4:change\n\n enter no.:> "
  ))
  if menu in menu_options:
      menu_options[menu]()

def viewList():
  counter = 0
  for idx, item in enumerate(ToDoList, start=1):
      print(f"{idx}:{item}")
  input("Press Enter to continue...")

def addItem():
  item = input("What do you wanna add?: ")
  ToDoList.append(item)

def removeItem():
  viewList()
  item_idx = int(input("Which item would you like to remove (enter index no.): "))

  if 1 <= item_idx <= len(ToDoList):
      removed_item = ToDoList[item_idx - 1]
      confirm = input(f"Are you sure you want to remove '{removed_item}'? (yes/no): ").lower()

      if confirm == "yes":
          ToDoList.pop(item_idx - 1)
          print(f"'{removed_item}' has been removed.")
      else:
          print(f"'{removed_item}' was not removed.")
  else:
      print("Invalid index. Item not removed.")

  input("Press Enter to continue...")

def changeItem():
  item_idx = int(input("Which item would you like to change (enter index no.): "))
  if 1 <= item_idx <= len(ToDoList):
      change = input("To what would you like to change it to: ")
      ToDoList[item_idx - 1] = change
      print("Item changed successfully.")
  else:
      print("Invalid index. Item not changed.")
  input("Press Enter to continue...")

ToDoList = []

while True:
  printList()
