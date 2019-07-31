class Person:
    def __init__(self, first_name, last_name, age, gender, contact_num):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name  = self.first_name + ' ' + self.last_name
        print("Person Created")
        print("Full name is: " + self.full_name)
        self.age = age
        print(f"Age is: {self.age}")
        self.gender = gender
        print("Gender is: " + self.gender)
        self.contact_num = contact_num
        print(f"Contact Number is: {self.contact_num}")
    
    def get_all_male(self):
        if self.gender == 'Male':
            print(self.full_name)
        else:
            print("Gender is not male")
    
    def get_all_female(self):
        if self.gender == 'Female':
            print(self.full_name)
        else:
            print("Gender is not female")

    def get_under_18(self):
        if self.age <= 18:
            print(self.full_name)
        else:
            print("Age should be under 18")

    def detail(self):
        try:
            print("This is the person's detail.")
            full_name = self.first_name + ' '+ self.last_name
            print(full_name)
            age = self.age
            print(age)
            gender = self.gender
            print(gender)
            contact_num = self.contact_num
            print(contact_num)

        except:
            print("Person does not exist.")

#     def create(self):
#         full_name  = self.first_name + '' + self.last_name
#         print(full_name)
#         age = self.age
#         print(age)
#         gender = self.gender
#         print("The gender is" + ' ' + gender)
#         contact = self.contact_num
#         print(contact)

    def update(self, first_name=None, last_name=None, age=None, gender=None, contact_num=None):
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name     
        self.full_name  = self.first_name + ' ' + self.last_name
        print("Person Updated")
        print("Full name is: " + self.full_name)
        if age:
            self.age = age
        print(f"Age is: {self.age}")
        
        if gender:
            self.gender = gender
        print("Gender is: " + self.gender)
        
        if contact_num:
            self.contact_num = contact_num
        print(f"Contact Number is: {self.contact_num}")

    def delete(self):
        del self.first_name
        del self.last_name
        del self.full_name
        del self.age
        del self.gender
        del self.contact_num
        print('Deleted')

per = Person("Ram", "Karki", 15, "Male", 981221132)
per.get_all_male()
per.get_all_female()
per.get_under_18()
per.detail()
per.update('Bhuwan')
per.delete()
per.detail()

per1 = Person("Sita", "Basnet", 25, "Female", 981871781)
per1.get_all_male()
per1.get_all_female()
per1.get_under_18()
per1.detail()
per1.update('Gita')
per1.delete()
per1.detail()