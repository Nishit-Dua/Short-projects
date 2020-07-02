import PIL.Image as Image

image_path = 'Full path to your Image file'
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]


def resize(image):
    new_width = 100
    width, height = image.size
    aspect_ratio = height/width
    new_height = int(aspect_ratio*new_width)
    return image.resize((new_width, new_height))


def Grey(image):
    return image.convert(mode="L")


def image_to_ascii(image):
    data = image.getdata()
    return ''.join(ASCII_CHARS[val//25] for val in data)


def main():
    try:
        image = Image.open(image_path)
    except:
        print('Not a valid image path')
        return

    new_img = Grey(resize(image))
    text = image_to_ascii(new_img)
    pix_count = len(text)

    final_ascii = '\n'.join(text[i:i+100] for i in range(0, pix_count, 100))

    with open('Ascii-Image.txt', 'w') as f:
        f.write(final_ascii)


main()
