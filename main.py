import os
from pathlib import Path

directory_path = os.getcwd()
print("SELECT YOUR FILE")
file_choice = int(input("Enter 0 to select an existing file or 1 to create a new file: ").strip())

match(file_choice):
    case 0:
        while True:
            file_name = input("Enter existing file name: ").strip()
            full_file_name = file_name + ".txt"
            file_path = Path(directory_path) / full_file_name

            if file_path.exists():           
                print_choice = input("Would you like to print the file contents before appending to it (Y/N): ")

                with open(full_file_name, 'r') as file:
                    match(print_choice):
                        case 'Y':
                            file_contents = file.read()
                            print(file_contents)
                        case 'N':
                            print("No problem!")
                        case _:
                            print("Invalid input.")
                
                break
            else:
                print(f"File {full_file_name} was not found. Please try again.")
    case 1:
        file_name = input("Enter new file name: ").strip()
        full_file_name = file_name + ".txt"
    case _:
        print("Invalid input.")

print("Enter your text now. Enter \"end\" to terminate.")
n = 0
with open(full_file_name, 'a', encoding='utf-8') as file:
    while True:
        try: 
            s = input()
            if s.strip() != "end":
                file.write(s + "\n") 
                n += 1
            else:
                break
        except:
            print("Invalid input.")

    print(f"Input reading complete. You entered {n} lines.")

