from PIL import Image

def percentage(image_path, threshold):
    image = Image.open(filepath)
    image = image.convert("RGB")
    typeA_count = 0
    typeB_count = 0

    for i in range(image.height):
        for j in range(image.width):
            pixel = image.getpixel((j, i))

            if all(value > threshold[i] for i, value in enumerate(pixel)):
                typeA_count += 1
            else:
                typeB_count += 1

    total_pixels = image.height * image.width
    percentage_typeA = (typeA_count / total_pixels) * 100
    percentage_typeB = (typeB_count / total_pixels) * 100

    return percentage_typeA, percentage_typeB


image_path = filepath
threshold = (104, 104, 104)
threshold = (104, 104, 104)

percentage_typeA, percentage_typeB = percentage(image_path, threshold)

print(f"Percentage of typeA pixels: {percentage_typeA:.2f}%")
print(f"Percentage of typeB pixels: {percentage_typeB:.2f}%")
