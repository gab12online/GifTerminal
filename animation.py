import os
import time
from PIL import Image, ImageSequence

class AsciiGifPlayer:
    def __init__(self, gif_path, width=80, frame_delay=0.05, loop=2):
        self.gif_path = gif_path
        self.width = width
        self.frame_delay = frame_delay
        self.loop = loop
        self.frames = []

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def resize_image(self, image):
        width, height = image.size
        ratio = height / width / 1.85
        new_height = int(self.width * ratio)
        return image.resize((self.width, new_height))

    def rgb_to_ansi(self, r, g, b):
        return f"\033[38;2;{r};{g};{b}m█"

    def convert_frame_to_ascii_rgb(self, image):
        image = image.convert("RGBA")
        pixels = list(image.getdata())
        ascii_img = ""

        width = image.width
        for i, pixel in enumerate(pixels):
            r, g, b, a = pixel
            if a < 128:
                ascii_img += " "
            else:
                ascii_img += self.rgb_to_ansi(r, g, b)
            if (i + 1) % width == 0:
                ascii_img += "\033[0m\n"
        return ascii_img

    def load_frames(self):
        try:
            img = Image.open(self.gif_path)
            self.frames.clear()
            for frame in ImageSequence.Iterator(img):
                resized = self.resize_image(frame)
                ascii_frame = self.convert_frame_to_ascii_rgb(resized)
                self.frames.append(ascii_frame)
        except Exception as e:
            print(f"\033[91m❌ Erreur lors du chargement des frames : {e}")

    def play(self):
        if not self.frames:
            self.load_frames()

        for _ in range(self.loop):
            for frame in self.frames:
                self.clear()
                print(frame, end="")
                time.sleep(self.frame_delay)

        print("\033[0m")  # Reset couleur terminal
