from PIL import Image

def bwimage(image_path, brightness_threshold):
    image = Image.open(image_path)
    img1 = image.convert("L")
    black_white = Image.new("L", img1.size)
    for y in range(img1.height):
        for x in range(img1.width):
            brightness = img1.getpixel((x, y))

            if brightness > brightness_threshold:
                black_white.putpixel((x, y), 0)
            else:
                black_white.putpixel((x, y), 255)

    black_white.show()

image_path = imgpath
brightness_threshold = 12
bwimage(image_path, brightness_threshold)
