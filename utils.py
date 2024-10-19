import base64


def get_banana_image():
    with open("banana.png", "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()

    return f"data:image/png;base64,{encoded_image}"