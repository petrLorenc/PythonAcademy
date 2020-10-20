from lesson11.series2.handlers import FileHandler

if __name__ == '__main__':
    fHandler = FileHandler("data/futurama.episodes")
    print(fHandler.episodes)
    fHandler.generate_file_structure("./data")