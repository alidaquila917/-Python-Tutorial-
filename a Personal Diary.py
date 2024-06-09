import os
from datetime import datetime

DIARY_FILE = "diary.txt"

def create_diary_entry(entry, add_timestamp=False):
    try:
        with open(DIARY_FILE, 'a') as file:
            if add_timestamp:
                timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S] ")
                file.write(timestamp)
            file.write(entry + '\n')
        print("Diary entry created successfully.")
    except IOError as e:
        print("Error creating diary entry:", e)

def view_previous_entries():
    try:
        with open(DIARY_FILE, 'r') as file:
            entries = file.readlines()
            if entries:
                print("Previous Diary Entries:")
                for entry in entries:
                    print(entry.strip())
            else:
                print("No previous entries found.")
    except IOError as e:
        print("Error viewing previous entries:", e)

def main():
    while True:
        print("\n1. Create a new diary entry")
        print("2. View previous diary entries")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            entry = input("Enter your diary entry: ")
            add_timestamp = input("Add timestamp to the entry? (yes/no): ").lower() == 'yes'
            create_diary_entry(entry, add_timestamp)
        elif choice == '2':
            view_previous_entries()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
