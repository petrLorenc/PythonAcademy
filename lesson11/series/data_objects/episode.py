import os
import numpy
from PIL import Image

class Episode:

    def __init__(self, episode_name, title, image_name, season):
        self.episode_name = episode_name
        self.title = title
        self.image_name = image_name
        self.season = season

    def make_folder(self, root):
        season_path = os.path.join(root, self.season)
        if not os.path.exists(season_path):
            os.mkdir(season_path)
        episode_path = os.path.join(season_path, self.episode_name)
        if not os.path.exists(episode_path):
            os.mkdir(episode_path)

        with open(os.path.join(episode_path, self.title + ".txt"), "w") as f:
            f.write(self.title)
        self.generate_random_image(os.path.join(episode_path, self.image_name))

    def generate_random_image(self, path):
        imarray = numpy.random.rand(100, 100, 3) * 255
        im = Image.fromarray(imarray.astype('uint8')).convert('RGBA')
        im.save(path)

    def __str__(self):
        return f""

    def __repr__(self):
        return f"{self.season}-{self.title}"
