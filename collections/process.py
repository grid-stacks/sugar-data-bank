from os import path, mkdir
import csv
from sanitize_filename import sanitize
from pathvalidate import sanitize_filename

# E:/---WorkFiles/Computational Chemistry/Drug Discovery/Sugar Bank/collections/fructose/PubChem_compound_text_fructose_summary.csv
csv_file = input("Give csv file location: ")
# E:/---WorkFiles/Computational Chemistry/Drug Discovery/Sugar Bank/collections/fructose/PubChem_compound_text_fructose_records.sdf
sdf_file = input("Give sdf file location: ")

info_dict = {}

if csv_file:
    file_extension = csv_file[-4:]

    if file_extension == ".csv":
        try:
            with open(csv_file, "r") as f_content:
                for line in csv.DictReader(f_content):
                    # print(sanitize(line[1].replace(" ", "-")))
                    # print(line)
                    # print("")
                    info_dict[line["cid"]] = {
                        "name": sanitize_filename(line["cmpdname"].replace(" ", "-").replace(";", "-")),
                        "mw": line["mw"]
                    }

        except IOError:
            print("CSV file not exists! Try again.")

    else:
        print("Please provide a csv file! Try again.")

else:
    print("You didn't provided any csv file name! Try again.")


if sdf_file:
    file_extension = sdf_file[-4:]

    if file_extension == ".sdf":
        folder_name = path.dirname(sdf_file)
        path_name = path.join(folder_name, "files")

        if not path.exists(path_name):
            mkdir(path_name)

        try:
            with open(sdf_file, "r") as f_content:
                contents = f_content.read()

                splitted_parts = contents.split("$$$$")
                total_parts = len(splitted_parts)
                splitted_parts = splitted_parts[:total_parts-1]

                for content in splitted_parts:
                    stripped_content = content.lstrip().rstrip()

                    name = "___" + info_dict[stripped_content.split(
                        "\n", 1)[0]]["name"] if info_dict[stripped_content.split(
                            "\n", 1)[0]]["name"] else ""
                    mw = "___" + info_dict[stripped_content.split(
                        "\n", 1)[0]]["mw"] if info_dict[stripped_content.split(
                            "\n", 1)[0]]["mw"] else ""

                    file_name = stripped_content.split(
                        "\n", 1)[0] + name + mw + ".sdf"
                    complete_name = path.join(path_name, file_name)

                    file = open(complete_name, "w")
                    file.write(stripped_content)
                    file.close()

                print("Report:")
                print("Total files: " + str(total_parts))
                print("Output folder: " + path_name)

        except IOError:
            print("SDF File not exists! Try again.")

    else:
        print("Please provide a sdf file! Try again.")

else:
    print("You didn't provided any sdf file name! Try again.")
