'''2. Створити клас Person, в якому буде присутнім метод __init__ який буде приймати * аргументів, які зберігатиме в відповідні змінні. Методи, які повинні бути в класі Person - show_age, print_name, show_all_information.
   - Створіть 2 екземпляри класу Person та в кожному з екземплярів створіть атребут profession.'''
   
class Person(object):
    profession = 'No one'
    
    def __init__(self, *args):
            self.name = args[0]
            self.age = args[1]
            self.id = args[2]

    def show_age(self):
        print(f'Age of {self.name} = {self.age}')
    def print_name(self):
        print(f'Name = {self.name}')
    def show_all_information(self):
        print(f'Name = {self.name}')
        print(f'Age = {self.age}')
        print(f'Proffession = {self.profession}')
        print(f'ID number = {self.id}')
    
    
per_1 = Person('Pavel', 24, 134488)
per_1.show_age()
per_1.print_name()
per_1.profession = 'CEO'
print(per_1.profession)
per_1.show_all_information()

per_2 = Person('Jean', 18, 12484)
per_2.print_name()
per_2.profession = 'Junior'
print(per_2.profession)
per_2.show_all_information()
