# leap year
"""
year / 4 == 0 &
year / 100 != 0|
year / 400 == 0
"""


def isleapyear(year):
  if (year / 4 == 0 and year / 100 != 0) or year / 400 == 0:
    return True
  else:
    return False


year = 2020
if isleapyear(year):
  print("2020 is a leapyear")
else:
  print("2020 is not a leapyear")
