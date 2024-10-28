import random
import base64
from enum import Enum

NUM1 = random.randint(9, 15)
NUM2 = random.randint(9, 15)
RESP = 0


def get_image(fruit_selector):
    if not fruit_selector:
        return
    with open("images/" + fruit_selector.lower() + ".png", "rb") as image_file:
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
    MULTIPLICATION = 3
    DIVISION = 4


def get_chosen_operation(operations):
    try:
        return Operation[operations[0].upper()].value
    except KeyError:
        return None
