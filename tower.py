class Tower(list):
    def __init__(self, name):
        super().__init__()
        self.__name = name

    def get_name(self):
        return self.__name

    def move(self, dest_tower):
        dest_tower.append(self.pop())
        return dest_tower

    def __str__(self):
        tow_str = 'Tower' + self.__name + ': ['
        for i in range(len(self)):
            if i == 0:
                tow_str += str(self[i])
            else:
                tow_str += ', ' + str(self[i])
        tow_str = tow_str + ']'
        return tow_str
