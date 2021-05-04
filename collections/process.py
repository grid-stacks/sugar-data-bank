from os import path

sdf_file = input("Give sdf file location: ")

if sdf_file:
    file_extension = sdf_file[-4:]

    if file_extension == ".sdf":
        folder_name = path.dirname(sdf_file)

        try:
            with open(sdf_file, "r") as f_content:
                contents = f_content.read()

                splitted_parts = contents.split("$$$$")
                total_parts = len(splitted_parts)
                splitted_parts = splitted_parts[:total_parts-1]

                for content in splitted_parts:
                    stripped_content = content.lstrip().rstrip()

                    file_name = stripped_content.split("\n", 1)[0] + ".sdf"
                    complete_name = path.join(folder_name, file_name)

                    file = open(complete_name, "w")
                    file.write(stripped_content)
                    file.close()

                print("Report:")
                print("Total files: " + str(total_parts))
                print("Output folder: " + folder_name)

        except IOError:
            print("File not exists! Try again.")

    else:
        print("Please provide a sdf file! Try again.")

else:
    print("You didn't provided any file name! Try again.")
