"""
CV Data Manager

GitHub Repository:
https://github.com/nordentesla/cv-data-manager

CV Data Manager for flexible management of relevant 
skills and experiences for target job applications.
"""


import sys
import datetime
import re


# Constants
CV_FIRST_NAME = "Jose Nichole"
CV_MIDDLE_NAME = "Canlas"
CV_LAST_NAME = "Galenzoga"
CV_CONTACT_NUMBERS = {
    "mobile": "+63 917 138 0264",
    "landline": "+63 42 784 3616"
}
CV_EMAIL = "nicogalenzoga@gmail.com"


def main():
    WIP()


def input_data_manager(input_name: str, prompt: str, 
                       data_type: object, input_format: str):
    while True:
        # Input Prompt
        print("Input Format for %s: %s", input_name, input_format)
        user_input = input(prompt)

        # Data Conversion
        try:
            # For Numbers / Quantity
            if data_type == int:
                user_input = int(user_input)
            # For Dates
            elif data_type == datetime.date:
                if matches := re.search(r"^([1-2][0-9]){3}-(0[1-9]|1[0-2])-([0-2][0-9]|3[0-1])$", 
                                        user_input):
                    yyyy = matches.group(1)
                    mm = matches.group(2)
                    dd = matches.group(3)
                    user_input = datetime.date(yyyy, mm, dd)
        except ValueError:
            print("invalid %s, please type a valid %s\n".capitalize(), input_format, input_name)
            continue

        # Return of data
        if user_input is data_type:
            return user_input
        else:
            continue

def error_notice(*notices: str):
    WIP()

def WIP():
    sys.exit("---\nunder construction, exiting program...\n---".upper())

if __name__ == "__main__":
    main()
