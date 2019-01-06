def human_age(age):
    if age < 18:
        return "Human is child"
    elif age < 60:
        return "Human is adult"
    else:
        return "Human is old."

def area(side):
    are = side ** 2
    return f'Area of square is {are}'