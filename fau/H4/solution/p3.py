# Python Programming.
# Homework 4, problem 3
# Instructor: Dr. Ionut Cardei
# Do not distribute.

class Employee:
    def __init__(self, name, base_sal, phone):
        self.__name, self.__base_sal, self.__phone = name, base_sal, phone

    def name(self):
        return self.__name

    def phone(self):
        return self.__phone

    def total_salary(self):
        return self.__base_sal

    def set_base_salary(self, newsal):
        """Set new base salary.
        precondition: newsal >= 0"""
        self.__base_sal = newsal

    def __str__(self):
        return "{}({}, {}, {})".format(type(self).__name__, self.name(), self.phone(), self.total_salary())     # OK if base salary is used instead

    def __repr__(self):
        return str(self)


class Engineer(Employee):
    pass
    # Engineer inherits __init__ from superclass. No need to override it.
    


class Manager(Employee):
    def __init__(self,  name, base_sal, phone, bonus):
        super().__init__(name, base_sal, phone)     # must call superclass constructor to initialize superclass properties
        self.__bonus = bonus

    # override to add the bonus
    def total_salary(self):
        return super().total_salary() + self.__bonus

    

class CEO(Manager):
    def __init__(self,  name, base_sal, phone, bonus, stocks):
        super().__init__(name, base_sal, phone, bonus)     # must call superclass constructor to initialize superclass properties
        self.__stocks = stocks

    # override to add the bonus
    def total_salary(self):
        # use the total salary of Manager. This will return the base_sal+bonus. We add stocks and return the sum.
        return super().total_salary() + self.__stocks


# b)
def print_staff(emp_iterable):
    """Prints a collection of Employee objects.
    precondition: emp_iterable is an iterable sequence of Employee object references."""
    for emp in emp_iterable:
        print(emp)

        
def main():
    e = Employee("Eva Porator ", 100000, "555-43321")
    f = Engineer("Fuzz Darkyear", 50000, "555-1232")
    m = Manager("Moon Pie", 100000, "555-3030", 1000)
    c = CEO("Care Lessing", 100000, "225-5732", 2000, 2000000)

    staff_lst = [e, f, m, c]
    print_staff(staff_lst)

    print("\n\nEngineer after promotion:")
    f.set_base_salary(100000)
    print(f)

if __name__ == "__main__":
    main()

