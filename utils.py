import random
import base64
from enum import Enum

NUM1 = random.randint(0, 10)
NUM2 = random.randint(0, 10)
RESP = 0


def get_image(selected_image):
    if not selected_image:
        return
    with open("images/" + selected_image.lower() + ".png", "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()

    return f"data:image/png;base64,{encoded_image}"


def update_numbers():
    global NUM1, NUM2
    NUM1 = random.randint(9, 15)
    NUM2 = random.randint(9, 15)


def get_num1():
    return NUM1


def get_num2():
    return NUM2


class Operation(Enum):
    COUNTING = 0
    ADDITION = 1
    SUBTRACTION = 2
    DIVISION = 3
    MULTIPLICATION = 4


ICONS = ['icon1', 'icon2', 'icon3', 'icon4', 'icon5']


def generate_divisible_numbers(max_num1=10, max_num2=5):
    global NUM1, NUM2
    NUM2 = random.randint(1, max_num2)
    NUM1 = NUM2 * random.randint(1, max_num1 // NUM2)


def get_chosen_operation(operations):
    try:
        current_operation = 0
        if len(operations) > 1:
            current_operation = random.randint(0, len(operations) - 1)
        else:
            current_operation = Operation[operations[0].upper()].value
        if current_operation == 3:
            generate_divisible_numbers(max_num1=10, max_num2=5)
        return current_operation
    except KeyError:
        return None
