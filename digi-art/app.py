from PIL import Image, ImageDraw
import random

# Create a blank image with a white background
width, height = 800, 600
img = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(img)

# Generate colorful circles
for _ in range(100):
    x = random.randint(0, width)
    y = random.randint(0, height)
    radius = random.randint(10, 50)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    draw.ellipse([(x - radius, y - radius), (x + radius, y + radius)], fill=color)

# Save the image
img.save('digital_art.png')
