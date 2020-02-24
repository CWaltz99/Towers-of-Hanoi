from tower import Tower
from disk import Disk
class TowersOfHanoi():
    def __init__(self, num_disks):
        self.__num_of_disks = num_disks
        self.__num_of_moves = 0
        towA = Tower('A')
        for size in range(num_disks, 0, -1):
            disk = Disk(size)
            towA.append(disk)
        towB = Tower('B')
        towC = Tower('C')
        self.__towers = [towA, towB, towC]

    def get_num_of_moves(self):
        return self.__num_of_moves

    def move_disks(self, num_disks_to_move, source, helper, target):
        if num_disks_to_move == 1:
            source.move(target)
            self.__num_of_moves += 1
            if self.__num_of_disks == 4:
                self.display_towers()
        else:
            self.move_disks(num_disks_to_move - 1, source, target, helper)
            self.move_disks(1, source, helper, target)
            self.move_disks(num_disks_to_move - 1, helper, source, target)


    def play(self):
        self.move_disks(self.__num_of_disks, self.__towers[0], self.__towers[1], self.__towers[2])

    def display_towers(self):
        for tower in self.__towers:
            print(tower)
