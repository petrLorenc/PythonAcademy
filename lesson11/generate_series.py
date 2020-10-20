from lesson11.series.handlers import FileHandler

if __name__ == '__main__':
    fHandler = FileHandler("data/futurama.episodes")
    print(str(fHandler.episodes[0]))
