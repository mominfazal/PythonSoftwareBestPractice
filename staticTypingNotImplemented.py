""" Static typing not implemented, name of file should be camelcased and not snake cased """

def get_first_name(full_name):
    """ Accepts a variable full_name (Type unknown)
    returns part of string before first space """
    return full_name.split(" ")[0] # Here we assumed its string and used split function

# I suggest running this file through a python linter https://pypi.org/project/pylint/
# You will find more suggestion which are improper in this file.

fallbackName = {
    "first_name": "UserFirstName",
    "last_name": "UserLastName"
}

rawName = input("Please enter your name: ")
firstName = get_first_name(rawName)

# If the user didn't type anything in, use the fallback name
if not firstName:
    firstName = get_first_name(fallbackName)

print(f"Hi, {firstName}!")

# Below referenced link is by Adam Geitgey on his GitHub channel.
# Reference : https://gist.github.com/ageitgey/a84a0651cd34464f3f8555f22f27e7f8#file-buggy-py
