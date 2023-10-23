"""
CV Data Manager\n
\n
GitHub Repository:\n
https://github.com/nordentesla/cv-data-manager \n
\n
CV Data Manager for flexible management of relevant\n
skills and experiences for target job applications.\n
"""


import sys
from datetime import date
from fpdf import FPDF
import re


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

class Education:
    ...

class Certification:
    ...

class Training:
    ...


def main():
    try:
        print("CV Data Manager")
    except KeyboardInterrupt:
        sys.exit("program force closed".title())


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
        print(f"Input Format for {input_name}: {input_format}")
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
            print(f'invalid {input_format}, please type a valid {input_name}\n'.capitalize())
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
    Placeholder function for functions and objects currently in development phase\n
    """
    sys.exit("---\nunder construction, exiting program...\n---".upper())

if __name__ == "__main__":
    main()
