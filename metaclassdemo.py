# 请记住，'type'实际上是一个类，就像'str'和'int'一样
# 所以，你可以从type继承
class UpperAttrMetaClass(type):
    __

    # __new__ 是在__init__之前被调用的特殊方法

    # __new__是用来创建对象并返回之的方法

    # 而__init__只是用来将传入的参数初始化给对象

    # 你很少用到__new__，除非你希望能够控制对象的创建

    # 这里，创建的对象是类，我们希望能够自定义它，所以我们这里改写__new__

    # 如果你希望的话，你也可以在__init__中做些事情

    # 还有一些高级的用法会涉及到改写__call__特殊方法，但是我们这里不用
    def __new__(self, future_class_name, future_class_parents, future_class_attr):
        attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
        return type(future_class_name, future_class_parents, uppercase_attr)


class UpperAttrMetaclass(type):
    def __new__(self, future_class_name, future_class_parents, future_class_attr):
        attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)

        # 复用type.__new__方法

        # 这就是基本的OOP编程，没什么魔法
        return type.__new__(self, future_class_name, future_class_parents, uppercase_attr)
