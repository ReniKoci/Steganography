# Steganography Encoder/Decoder

This Python project allows users to encode and decode messages using steganography techniques. Steganography is the practice of concealing a message within another non-secret data, such as hiding a message within an image.

I used this as a password manager but it obviously has many other uses.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Methods](#methods)
- [Examples](#examples)

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/steganography.git
2. Navigate to the project directory:
   ```bash
   cd steganography
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

## Usage

### Command Line Interface (CLI)

To use the command line interface:

```bash
python main.py --method [encode/decode] --image [path_to_image] --msg [message] --output_file [output_file_name]
```

- method: Specify whether you want to encode or decode the image.
- image: Path to the image file.
- msg: Message to encode (for encoding only).
- output_file: Name of the output file (for encoding only).

### Command Line Interface (CLI)

To use the graphical user interface (GUI):
```bash
python ui.py
```

## Methods

### Encode
The encode method embeds a message within an image using the least significant bit (LSB) technique. It changes the least significant bit of each pixel's RGB values to encode the message.
### Decode
The decode method extracts a message from an encoded image. It reads the least significant bit of each pixel's RGB values to reconstruct the encoded message.

## Examples

### CLI
Encoding
  ```bash
  python steganography.py --method encode --image test_img.png --msg "Secret message" --output_file encoded_image
  ```
Decoding 
  ```bash
  python steganography.py --method decode --image encoded_image.png
  ```
## GUI
1. Run the GUI application:
  ```bash
  python steganography_gui.py
  ```
2. Choose the mode (Encode/Decode).
3. Enter the message (for encoding).
4. Select an image.
5. Click on the "Proceed" button.

## 🤝 Contributing

### Submit a pull request

If you'd like to contribute, please fork the repository and open a pull request to the `main` branch.

