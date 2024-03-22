todos = []  # List to store to-do items as dictionaries

def add_todo():
  
  title = input("Enter a new to-do item: ")
  todos.append({"title": title, "completed": False})
  print("To-do item added successfully!")

def view_todos():
  
  if not todos:
    print("There are no to-do items yet.")
    return
  print("-" * 40)
  print("| Title                     | Completed |")
  print("-" * 40)
  for i, todo in enumerate(todos):
    completion_marker = "*" if todo["completed"] else ""
    print(f"| {i+1}. {todo['title']:<30} | {completion_marker} |")
  print("-" * 40)

def mark_todo_done():
  
  if not todos:
    print("There are no to-do items yet.")
    return
  view_todos()
  while True:
    try:
      index = int(input("Enter the number of the completed to-do item (or 0 to cancel): ")) - 1
      if 0 <= index < len(todos):
        todos[index]["completed"] = True
        print("To-do item marked as completed!")
        break
      elif index == -1:
        break
      else:
        print("Invalid input. Please enter a valid number or 0 to cancel.")
    except ValueError:
      print("Invalid input. Please enter a number.")

def delete_todo():
  
  if not todos:
    print("There are no to-do items yet.")
    return
  view_todos()
  while True:
    try:
      index = int(input("Enter the number of the to-do item to delete (or 0 to cancel): ")) - 1
      if 0 <= index < len(todos):
        del todos[index]
        print("To-do item deleted successfully!")
        break
      elif index == -1:
        break
      else:
        print("Invalid input. Please enter a valid number or 0 to cancel.")
    except ValueError:
      print("Invalid input. Please enter a number.")

def main():
  
  while True:
    print("\nTo-Do List App")
    print("1. Add a new to-do item")
    print("2. View all to-do items")
    print("3. Mark a to-do item as completed")
    print("4. Delete a to-do item")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
      add_todo()
    elif choice == "2":
      view_todos()
    elif choice == "3":
      mark_todo_done()
    elif choice == "4":
      delete_todo()
    elif choice == "5":
      print("Exiting To-Do List App...")
      break
    else:
      print("Invalid input. Please enter a number between 1 and 5.")

if __name__ == "__main__":
  main()
