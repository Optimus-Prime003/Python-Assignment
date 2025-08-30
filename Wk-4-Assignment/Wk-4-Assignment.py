def file_read_write():
    # Ask user for the input file name
    filename = input("Enter the filename to read: ")

    try:
        # Open file for reading
        with open(filename, "r") as file:
            lines = file.readlines()

        # Modify content: Add line numbers and uppercase
        modified_lines = [f"{i+1}: {line.strip().upper()}\n" for i, line in enumerate(lines)]

        # Write modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.writelines(modified_lines)

        print(f"✅ File processed successfully! Modified content saved in '{new_filename}'.")

    except FileNotFoundError:
        print("❌ Error: The file you entered does not exist.")
    except PermissionError:
        print("❌ Error: You don't have permission to read this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


# Run the program
file_read_write()
