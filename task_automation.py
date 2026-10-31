
import os
import shutil
import csv
from pathlib import Path
from datetime import datetime

# 1. FILE ORGANIZER
def organize_files():

    folder_path = input("\nEnter folder path to organize: ")
    folder = Path(folder_path)

    if not folder.is_dir():
        print("Invalid folder path!")
        return

    print("\nOrganizing files...")

    for file in folder.iterdir():

        if file.is_file():

            extension = file.suffix.lower().replace(".", "")

            if not extension:
                extension = "Others"

            destination_folder = folder / extension.upper()
            destination_folder.mkdir(exist_ok=True)

            destination = destination_folder / file.name

            # Avoid overwriting existing files
            count = 1
            while destination.exists():
                destination = destination_folder / (
                    f"{file.stem}_{count}{file.suffix}"
                )
                count += 1

            shutil.move(str(file), str(destination))

    print("Files organized successfully!")


# 2. FILE BACKUP
def create_backup():

    source_path = Path(input("\nEnter folder path to backup: "))

    if not source_path.is_dir():
        print("Source folder not found!")
        return

    backup_path = Path(input("Enter backup destination folder: "))

    try:
        source = source_path.resolve()
        backup = backup_path.resolve()

        if backup == source or source in backup.parents:
            print("Backup destination cannot be inside source folder!")
            return

        backup.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        destination = backup / f"Backup_{timestamp}"

        shutil.copytree(source, destination)

        print("\nBackup created successfully!")
        print("Location:", destination)

    except OSError as error:
        print("Backup error:", error)


# 3. GENERATE FOLDER REPORT
def generate_report():

    folder_path = Path(input("\nEnter folder path: "))

    if not folder_path.is_dir():
        print("Invalid folder path!")
        return

    report_name = "folder_report.csv"
    report_path = folder_path / report_name

    try:
        with open(report_path, "w", newline="", encoding="utf-8") as file:

            writer = csv.writer(file)

            writer.writerow([
                "File Name",
                "File Type",
                "File Size (KB)"
            ])

            for item in folder_path.iterdir():

                if item.is_file() and item != report_path:

                    file_type = item.suffix or "No Extension"
                    file_size = round(item.stat().st_size / 1024, 2)

                    writer.writerow([
                        item.name,
                        file_type,
                        file_size
                    ])

        print("\nFolder report generated successfully!")
        print("Saved as:", report_path)

    except OSError as error:
        print("Report error:", error)


# 4. DISPLAY DATE AND TIME
def show_datetime():

    current_time = datetime.now()

    print("\n===== CURRENT DATE & TIME =====")
    print("Date:", current_time.strftime("%d-%m-%Y"))
    print("Time:", current_time.strftime("%I:%M:%S %p"))


# MAIN MENU
while True:

    print("\n====================================")
    print("       PYTHON TASK AUTOMATION")
    print("====================================")

    print("1. Organize Files")
    print("2. Create Folder Backup")
    print("3. Generate Folder Report")
    print("4. Show Date and Time")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":

        organize_files()

    elif choice == "2":

        create_backup()

    elif choice == "3":

        generate_report()

    elif choice == "4":

        show_datetime()

    elif choice == "5":

        print("\nThank you for using Task Automation!")
        break

    else:

        print("\nInvalid choice! Please try again.")
