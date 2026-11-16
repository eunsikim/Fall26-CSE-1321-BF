class todo_item:
    def __init__(self, title, category = ""):
        self.title = title
        self.is_done = False
        self.category

        print("LOG: Finished defining object attributes")

    def print_todo_item(self):
        if self.is_done == True:
            return f"[x] {self.title}"
        else:
            return f"[ ] {self.title}"

    def set_done(self):
        if self.is_done == True:
            print("This To Do item is already completed")
        else:
            self.is_done = True
            print(f"LOG: To Do Item {self.title} has been set as done.")

def main():
    todo_list = []

    while True:
        print("1. Add a To Do Item")
        print("2. Set To Do Item as done")
        print("3. Print To Do List")
        print("4. Exit")

        option = int(input("> "))
        
        print()

        if option == 1:
            title = input("Enter title: ")

            new_todo_item = todo_item(title)

            todo_list.append(new_todo_item)
            print("LOG: Finished appending `todo_item` into the To Do List")

        elif option == 2:
            print("Select a To Do Item:")
            for index in range(len(todo_list)):
                print(f"{index} - {todo_list[index].title}")

            todo_sel = int(input("> "))

            todo_list[todo_sel].set_done()
            
        elif option == 3:
            for item in todo_list:
                print(item.print_todo_item())

        elif option == 4:
            print("Terminating Programs...")
            break

        print()

if __name__ == "__main__":
    main()