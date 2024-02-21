from PIL import Image
import numpy as np
import argparse
import os


# encoding the message by changing the least significant bit
def encode(img_path: str, message: str, delimiter: str, output_file) -> None:
    # load image and transform to RGB
    with Image.open(img_path) as img:
        width, height = img.size
        img = np.array(img)

    # add delimiter and encode message
    full_message = message + delimiter
    message_encoded = ''.join(format(ord(i), '08b') for i in full_message)
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
    new_img.save(f"{output_file}.png")


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


def main(args) -> None:
    delimiter = args.delimiter
    message = args.msg
    img_path = args.image
    output_file_name = args.output_file

    # check if method specified
    if args.method is None:
        print("Method not specified. Use either encode or decode")
        return

    # check if image path specified
    if args.image is None:
        print("Image path not specified")
        return

    # check whether image exists
    if not os.path.exists(args.image):
        print("Image does not exist")
        return

    # check if image is valid
    try:
        img = Image.open(args.image)
        img.verify()  # Verifying the image file
    except Exception as e:
        print(f"This file is not a valid image")
        return

    if args.method.lower() == "encode":
        # check if message was specified
        if message == "" or message is None:
            print("Message not specified")
        else:
            encode(img_path, message, delimiter, output_file_name)
    elif args.method.lower() == "decode":
        message = decode(img_path, delimiter)
        print(f"Your message: {message}")
    else:
        print("Method not recognized. Use either encode or decode")


if __name__ == "__main__":
    argParser = argparse.ArgumentParser()

    argParser.add_argument("--delimiter", type=str, default="###END###", help="Delimiter to know when message "
                                                                              "finishes. Default = '###END###'")
    argParser.add_argument("--msg", type=str, default="", help="Specify your message")
    argParser.add_argument("--method", type=str, help="Specify if you want to decode or encode the image")
    argParser.add_argument("--image", type=str, help="Specify the path of the image")
    argParser.add_argument("--output_file", type=str, default="output", help="Image with encoded message")

    args = argParser.parse_args()

    main(args)
