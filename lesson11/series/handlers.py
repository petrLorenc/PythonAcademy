from lesson11.series.data_objects.episode import Episode


class FileHandler:
    def __init__(self, path):
        data = self.get_data(path)
        parsed_data = self.process_files(data)
        self.episodes = self.generate_episodes(parsed_data)

    def get_data(self, path):
        try:
            with open(path, "r", encoding="utf8") as f:
                data = f.readlines()
        # can we use only try/finally without except?
        except FileNotFoundError:
            print("The file does not exists")
        # can we use only try/except without finally?
        finally:
            print("File was loaded into memory")
        return data

    def process_files(self, data):
        parsed_data = {}
        label = None
        for line in data:
            splitted_line = line.split("\t")
            if len(splitted_line) == 1:
                label = splitted_line[0].strip()
                parsed_data[label] = []
            else:
                parsed_data[label].append(tuple(map(lambda x: x.strip("\"\n"), splitted_line)))
        return parsed_data

    def generate_episodes(self, parsed_data):
        return [Episode(*episode_info, key) for key, values in parsed_data.items() for episode_info in values]
