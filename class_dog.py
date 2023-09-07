class Dog:
    #This is the constructor for the class.
    # It is called whenever a Dog object is created.
    #takes 5 parameters
    def __init__(self, name, month, day,year, sound):
        #assign the attributes to the instance of the class using 'self'
        self.name = name
        self.month = month
        self.year = year
        self.day = day
        self.sound = sound

    def speak(self):
        return f"{self.name} says {self.sound}"
    
    # Here is an accessor method to get the name
    def get_name(self):
        return self.name
    
    def birth_date(self):
        return str(self.month) + "/" + str(self.day) + "/" + str(self.year)
    
    def change_bark(self, new_sound):
        self.sound = new_sound

    #a special method that allows you to use the + operator to combine two Dog objects.
    def __add__(self, other_dog):
        return Dog("Puppy of "  + self.name + " and " + other_dog.name, \
                   self.month, self.day, self.year + 1, \
                    self.sound + other_dog.sound)
    
def main():#function is the entry point of the program
#instances of the Dog class
    boyDog = Dog("Mesa",5, 12, 2004, "WOOF")
    girlDog = Dog("Mary", 5, 6, 2004, " barkbark ")
    print(boyDog.speak())
    print(girlDog.speak())
    # Access the birth_day attribute
    print(boyDog.birth_date())
    print(girlDog.birth_date())

    boyDog.change_bark("woofywoofy")
   

    print(boyDog.speak())
    puppy = boyDog + girlDog
    print(puppy.speak())
    print(puppy.get_name())
    print(puppy.birth_date())

if __name__=="__main__":
    main()
#this block ensures that the main function is only executed if the script
#  is run directly (not imported as a module).

#Output
#Mesa says WOOF
#Mary says  barkbark 
#5/12/2004
#5/6/2004
#Mesa says woofywoofy
#Puppy of Mesa and Mary says woofywoofy barkbark 
#Puppy of Mesa and Mary
#5/12/2005