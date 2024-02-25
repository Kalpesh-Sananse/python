#oop

class Employee:
    __name = None
    __id = 0            # __ double uderscore means var are private
    __salary = 0

    def __init__(self,name,id,salary):
        self.__name =name;
        self.__id    = id;
        self.__salary = salary;

    def set_name(self,name):
        self.__name=name

    def get_name(self):
        return  self.__name

harry = Employee()
harry.set_name('kalpesh')
print(harry.get_name())