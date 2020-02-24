class Disk:
    def __init__(self, size):
        self.__size = size

    def get_size(self):
        return self.__size

    def __str__(self):
        return str(self.__size)
