"""
CV Data Manager

GitHub Repository:
https://github.com/nordentesla/cv-data-manager

CV Data Manager for flexible management of relevant 
skills and experiences for target job applications.
"""


import sys
from datetime import date
from fpdf import FPDF
import re


# Constants
CV_FIRST_NAME = "Jose Nichole"
CV_MIDDLE_NAME = "Canlas"
CV_LAST_NAME = "Galenzoga"
CV_GENDER = "Male"
CV_CONTACT_NUMBERS = {
    "mobile": "+63 917 138 0264",
    "landline": "+63 42 784 3616"
}
CV_ADDRESS = {
    "line_1": "135 Faustin Flora Ville",
    "line_2": "Masalukot 1",
    "city": "Candelaria",
    "region": "Quezon",
    "country": "Philippines",
    "postal_code": "4323"
}
CV_EMAIL_ADDRESS = "nicogalenzoga@gmail.com"
CV_SKILLS = {'general', 
            'hvac-r', 'mechanical-engineer', 'power-plant', 'utilities',
            'python-language', 'web-development', 'artificial-intelligence'}


class Event:
    def __init__(self, start_date: date, end_date: date, *skills: str):
        self.start_date = start_date
        self.end_date = end_date
        self.duration = end_date - start_date
        self.skills = set(*skills)

    def role_handler(self):
        WIP()
class Job:
    ...

class Certification:
    ...

class Education:
    ...

class Seminar:
    ...


def main():
    WIP()


def input_data_manager(input_name: str, prompt: str, 
                       data_type: object, input_format: str):
    """
    Input handler for all user inputs for CV data\n
    Usage:\n
    input_name - name of data entry\n
    prompt - prompt for user input\n
    data_type - data type of user input for proper validation\n
    input_format - notice for proper format of the specific data entry\n
    """
    while True:
        # Input Prompt
        print("Input Format for %s: %s", input_name, input_format)
        user_input = input(prompt)

        # Data Conversion and Validation
        try:
            # For Numbers / Quantity
            if data_type == int:
                user_input = int(user_input)
            # For Dates
            elif data_type == date:
                if matches := re.search(r"^([1-2][0-9]){3}-(0[1-9]|1[0-2])-([0-2][0-9]|3[0-1])$", 
                                        user_input):
                    yyyy = matches.group(1)
                    mm = matches.group(2)
                    dd = matches.group(3)
                    user_input = date(yyyy, mm, dd)
                else:
                    raise ValueError
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
    """
    Placeholder function for functions and objects currently in development phase
    """
    sys.exit("---\nunder construction, exiting program...\n---".upper())

if __name__ == "__main__":
    main()
