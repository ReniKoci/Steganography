from PIL import Image
import numpy as np


# encoding the message by changing the least significant bit
def encode(img_path: str, message: str, delimiter: str) -> None:
    # load image and transform to RGB
    with Image.open(img_path) as img:
        width, height = img.size
        img = np.array(img)

    # add delimiter and encode message
    full_message = message + delimiter
    message_encoded = ''.join(format(ord(i), '08b') for i in full_message)
    print(message_encoded)
    # convert values to integers
    message_encoded = [int(x) for x in message_encoded]
    message_encoded_length = len(message_encoded)

    # check whether image can include the whole message
    # if image size is smaller than the message, than its impossible to fully transfer the message
    if len(message_encoded) > width * height:
        print("Message cannot be fully hidden in this image")
        return

    # Flatten the pixel arrays
    img = np.reshape(img, width * height * 3)

    # Overwrite pixel LSB
    img[:message_encoded_length] = img[:message_encoded_length] & ~1 | message_encoded

    # Reshape back to an image pixel array
    img = np.reshape(img, (height, width, 3))

    new_img = Image.fromarray(img)
    new_img.save("out.png")


def decode(encoded_image_path: str, delimiter: str) -> str:
    with Image.open(encoded_image_path) as img:
        width, height = img.size
        data = np.array(img)

    data = np.reshape(data, width * height * 3)
    # extract lsb
    data = data & 1
    # Packs binary-valued array into 8-bits array.
    data = np.packbits(data)
    # Read and convert integer to Unicode characters until hitting a non-printable character
    message = ""
    for x in data:
        letter = chr(x)
        if letter.isprintable():
            message += letter
        # check if delimiter found
        if message[-len(delimiter):] == delimiter:
            break

    return message.split(delimiter)[0]


delimiter = "###END###"
# encode("test_img.png", "Hello", delimiter)
print(decode("out.png", delimiter))
