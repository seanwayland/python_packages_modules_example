todays_day = "fri"
yesterday = "thus"

def print_todays_day():
    print("today is : ", todays_day)

class Person:
    # init is a constructor 
  def __init__(self, name, age):
    self.name = name
    self.age = age

  # this functions adds years to the person it is "called on"
  def make_older(self, years ):
      self.age = self.age + years 

