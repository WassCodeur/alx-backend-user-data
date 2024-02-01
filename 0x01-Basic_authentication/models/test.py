from base import Base
from models.user import User

base = Base(email="wass@was.com", _password="12345", first_name="Wasiu", last_name='ibrahim')

# base.to_json()

user = User(email="wass@was.com", _password="12345", first_name="Wasiu", last_name='ibrahim')
# user.save()
user.load_from_file()
resul = user.search({'email': "wass@was.com", '_password': "12345", 'first_name': "Wasiu", 'last_name': 'ibrahim'})
# print(resul)
# print(user.display_name())

class MyClass:
    class_variable = 0  # Variable de classe

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable  # Variable d'instance
        self.name = MyClass.__name__

    @classmethod
    def class_method(cls, x):
        cls.class_variable += x
        print(f"Class method called. Class variable is now {cls.class_variable}")
        print(cls.__name__)

# Création d'instances de la classe
obj1 = MyClass(10)
obj2 = MyClass(20)

print(obj1.class_variable)
print(obj1.name)

# Appel de la méthode de classe
MyClass.class_method(5)
# Output: Class method called. Class variable is now 5

# Accès à la variable de classe à partir d'une instance
print(obj1.class_variable)
# Output: 5

print(obj2.class_variable)
# Output: 5
