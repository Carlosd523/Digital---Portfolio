print("Hello, welcome to Battlehip")
name_player = input('Please write your name: ')
print("Hello {name}, now we're gonna start playing as 'Player1'".format(name = name_player))
class Player:
    def __init__(self, name,):
        self.name = name

    def guess(self):
        guess = input('Please write your guess: ')
        return guess
    
    def place_ships(self):
        pass
    
    def chech_guess(self):
        pass

class Ships:
    def __init__(self, size):
        self.size = size
        self.hit = []
        self.coordinates = []
    
    def place_ship(self):
        coords = []
        while len(coords) < self.size:
            coord = input('Please write the coordinates of your ship: ')
            if self.validate_coord(coord):
                if coord not in coords:
                    coords.append(coord)
                else:
                    print("You've already placed a ship in these coordinates")
            else:
                print('Invalid coordinates, please try again')
        self.coordinates = coords
        print('You placed your ship in the following coordinates: {coords}'.format(coords = coords))
        return coords
    
    def validate_coord(self, coord):
        if len(coord) < 2 or len(coord) > 3:
            return False
        if coord[0] not in 'ABCDEFGHIJ':
            return False
        if coord[1:] not in[str(i) for i in range(1, 11)]:
            return False
        return True