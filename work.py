class Person():
    def __init__(self):
        self.male_dict = {}
        self.female_dict = {}

    def get_full_name(self):
        first_name = input("Enter the first name of user: ")
        self.first_name = first_name

        last_name = input("Enter the second name of user: ")
        self.last_name = last_name

        age = input("Enter the age of user: ")
        self.age = age

        self.gender = input("Enter the gender of user. Enter 'male' or 'female': ")
        while(not (self.gender == 'male' or self.gender == 'female')):
            self.gender = input("Wrong input. Please enter 'male' or 'female': ")

        if self.gender == 'male':
            self.male_dict[self.first_name] = self.first_name
        elif self.gender == 'female':
            self.female_dict[self.first_name] = self.first_name

        contact_num = input("Enter the contact number of user: ")
        self.contact_num = contact_num

        self.fullname = self.first_name + ' ' + self.last_name
        print(f'\nyour full name is {self.fullname}\n')
        print(f'your gender is {self.gender}')

    def get_gender_list(self):
        print(f'The data is:\nmale data: {self.male_dict}, female data: {self.female_dict}')  
    
per = Person()
for _ in range(0,2):
    per.get_full_name()

per.get_gender_list()