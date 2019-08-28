""" Static typing implemented """

from typing import Dict

def get_first_name(full_name: str) -> str:
    """ Accepts a string full_name
    returns part of string before first space """
    return full_name.split(" ")[0]

fallback_name: Dict[str, str] = {
    "first_name": "UserFirstName",
    "last_name": "UserLastName"
}

raw_name: str = input("Please enter your name: ")
first_name: str = get_first_name(raw_name)

# If the user didn't type anything in, use the fallback name
if not first_name:
    FIRST_NAME = get_first_name(fallback_name)

print(f"Hi, {FIRST_NAME}!")

# Note: this file is proper and doesnt have any python linting errors
# also note the way the doc string is written explaining about the input and output parameter
# of a function and explains about the open question which a user may have while reading the code.
# Note the variable name is camel_cased and not snakeCased

# Below referenced link is by Adam Geitgey on his GitHub channel.
# Ref : https://gist.github.com/ageitgey/1201167f4f85b2131c71d4a421227f72#file-buggy-with-types-py
