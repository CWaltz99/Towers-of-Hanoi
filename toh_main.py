from towers_of_hanoi import TowersOfHanoi
def main():
    print('Towers of Hanoi')
    print('----------------')
    print('----------------')
    for i in range(3, 25):
        toh = TowersOfHanoi(i)
        if i == 4:
            toh.display_towers()
        toh.play()
        print('Moving ' + str(i) + ' in ' + str(toh.get_num_of_moves()) + ' moves!')

main()
