from PIL import Image, ImageDraw

# Create bird image
bird = Image.new('RGBA', (34, 24), (255, 255, 0, 255))  # Yellow bird
draw = ImageDraw.Draw(bird)
draw.ellipse([4, 4, 30, 20], fill=(255, 0, 0, 255))  # Red ellipse to simulate a bird
bird.save('bird.png')

# Create pipe image
pipe = Image.new('RGBA', (70, 400), (0, 255, 0, 255))  # Green pipe
draw = ImageDraw.Draw(pipe)
draw.rectangle([0, 0, 70, 400], fill=(0, 128, 0, 255))  # Darker green bands
pipe.save('pipe.png')

# Create background image
background = Image.new('RGBA', (400, 600), (135, 206, 235, 255))  # Sky blue background
draw = ImageDraw.Draw(background)
draw.ellipse([50, 50, 100, 100], fill=(255, 255, 255, 255))  # White cloud
draw.ellipse([300, 80, 350, 130], fill=(255, 255, 255, 255))  # Another white cloud
background.save('background.png')
