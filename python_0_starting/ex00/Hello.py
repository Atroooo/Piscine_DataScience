ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}


ft_list[1] = "World!"

temp = list(ft_tuple)
temp[1] = "France!"
ft_tuple = tuple(temp)


# ft_set.remove("tutu!")
# ft_set.add("Lyon!")

class CustomHashObject:
    def __init__(self, value):
        self.value = value

    def __hash__(self):
        if self.value == "Hello":
            return 0
        return 1

    def __eq__(self, other):
        if isinstance(other, CustomHashObject):
            return self.value == other.value
        return False

    def __repr__(self):
        return f"{self.value!r}"


obj1 = CustomHashObject("Hello")
obj2 = CustomHashObject("Lyon!")
ft_set = {obj1, obj2}

ft_dict["Hello"] = "42Lyon!"


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
