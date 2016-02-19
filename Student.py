class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print("%s : %s" % (self.__name, self.__score))


lisa = Student("lisa", 100)

# lisa.print_score()
# print(lisa._Student__name)


print(dir(Student("lisa", 100)))
