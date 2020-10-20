import os
import numpy
from PIL import Image

class Episode:
    episode_name = ""
    title = ""
    image_name = ""

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

    def generate_random_image(self, path: str):
        imarray = numpy.random.rand(100, 100, 3) * 255
        im = Image.fromarray(imarray.astype('uint8')).convert('RGBA')
        im.save(path)

    def __str__(self):
        return f"{self.season} - {self.episode_name} - {self.title}"


    """The goal of __repr__ is to be unambiguous. Plus, whenerver possible, you should define repr so that(in your case)
     eval(repr(instance)) == instance
    On the other hand, the goal of __str__ is to be redeable; so it matter if you have to print the instance on screen 
    (for the user, probably), if you don't need to do it, then do not implement it (and again, if str in not implemented 
    will be called repr)"""
    def __repr__(self):
        return str(self)


