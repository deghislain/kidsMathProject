import random
import base64

NUM1 = random.randint(0, 9)
NUM2 = random.randint(0, 9)
RESP = 0

with open("banana.png", "rb") as image_file:
    ENCODED_IMAGE = base64.b64encode(image_file.read()).decode()

BANANA_IMAGE = f"data:image/png;base64,{ENCODED_IMAGE}"


def update_numbers():
    global NUM1, NUM2
    NUM1 = random.randint(0, 9)
    NUM2 = random.randint(0, 9)


def get_num1():
    return NUM1


def get_num2():
    return NUM2
