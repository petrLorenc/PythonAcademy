import os
import numpy
from PIL import Image

with open("data/futurama.episodes", "r", encoding="utf8") as f:
    data = f.readlines()


def generate_random_image(path: str):
    imarray = numpy.random.rand(100,100,3) * 255
    im = Image.fromarray(imarray.astype('uint8')).convert('RGBA')
    im.save(path)


parsed_data = {}

for line in data:
    splitted_line = line.split("\t")
    if len(splitted_line) == 1:
        label = splitted_line[0].strip()
        parsed_data[label] = []
    else:
        parsed_data[label].append(tuple(map(lambda x: x.strip("\"\n"), splitted_line)))


root = "./data/"
for season, tupled_names in parsed_data.items():
    for episode_name, title, image_name in tupled_names:
        season_path = os.path.join(root, season)
        if not os.path.exists(season_path):
            os.mkdir(season_path)
        episode_path = os.path.join(season_path, episode_name)
        if not os.path.exists(episode_path):
            os.mkdir(episode_path)

        with open(os.path.join(episode_path, title + ".txt"), "w") as f:
            f.write(title)
        generate_random_image(os.path.join(episode_path, image_name))