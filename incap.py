class Person:

        
    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname

        self.name = f'{self.__name} {self.__surname}'


