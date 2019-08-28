""" We generally declare constants as 0s or 1s but this can be unclear if we have more than 2 values
such values which makes reader of our code ask questions is called magic numbers. """

def day_of_year(month: int, day_of_month: int):
    """ Accepts month (1-12) and date (1-31) as integer values"""
    if month == 2:
        day_of_month += 31
    elif month == 3:
        day_of_month += 59
    elif month == 4:
        day_of_month += 90
    elif month == 5:
        day_of_month += 31 + 28 + 31 + 30
    elif month == 6:
        day_of_month += 31 + 28 + 31 + 30 + 31
    elif month == 7:
        day_of_month += 31 + 28 + 31 + 30 + 31 + 30
    elif month == 8:
        day_of_month += 31 + 28 + 31 + 30 + 31 + 30 + 31
    elif month == 9:
        day_of_month += 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31
    elif month == 10:
        day_of_month += 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30
    elif month == 11:
        day_of_month += 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31
    elif month == 12:
        day_of_month += 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 31

    return day_of_month

# day_of_year is full of magic numbers:

# The months 2, …, 12 would be far more readable as FEBRUARY, …, DECEMBER.
# The days-of-months 30, 31, 28 would be more readable(and eliminate duplicate code)
# if they were in a data structure like an array, list, or map, e.g. MONTH_LENGTH[month].
# The mysterious numbers 59 and 90 are particularly pernicious examples of magic numbers.
# Not only are they uncommented and undocumented, but they are also the result of a
# computation done by hand by the programmer. Don't hardcode constants that you've computed
# by hand. Java is better at arithmetic than you are. Explicit computations like 31 + 28
# make the provenance of these mysterious numbers much clearer. MONTH_LENGTH[JANUARY] +
# MONTH_LENGTH[FEBRUARY] would be clearer still.

# Note: DRY - Dont Repeat yourself is not repeated properly.

# Ref : [MITx: 6.005.1x edx](https://courses.edx.org/courses/course-v1:MITx+6.005.1x+3T2016/\
# course/#block-v1:MITx+6.005.1x+3T2016+type@sequential+block@02-Code-Review)
