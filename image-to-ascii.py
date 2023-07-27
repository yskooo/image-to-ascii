from PIL import Image

# Define the ASCII characters used for the conversion
ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / float(width)
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayify(image):
    grayscale_image = image.convert("L")
    return grayscale_image

def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel_value in pixels:
        ascii_str += ASCII_CHARS[pixel_value // 25]  # Map pixel value to corresponding ASCII character
    return ascii_str

def main(image_path, new_width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print("Error:", e)
        return

    image = resize_image(image, new_width)
    image = grayify(image)
    ascii_str = pixels_to_ascii(image)

    # Reshape the ASCII string to match the new width
    pixel_count = len(ascii_str)
    ascii_img = "\n".join([ascii_str[i:i + new_width] for i in range(0, pixel_count, new_width)])

    print(ascii_img)

if __name__ == "__main__":
    image_path = "arzea.jpg"  # Replace this with the path to your image
    new_width = 100  # Adjust the width to control the size of the ASCII art
    main(image_path, new_width)
