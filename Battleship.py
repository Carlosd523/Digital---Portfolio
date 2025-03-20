print("Hello, welcome to Battleship")
name_player = input('Please write your name: ')
print("Hello {name}, now we're gonna start playing as 'Player1'".format(name = name_player))
class Player:
    def __init__(self, name):
        self.name = name
        self.shots = []

    def shot(self):
        shot = input('Please write the coordinate of your shot:')
        while True:
            is_valid = self.validate_shot(shot)

            if not is_valid:
                print('Your shot {shot} isn\'t valid, please try again'.format(shot = shot))

            elif shot in self.shots:
                print('You already shot at {shot}'.format(shot = shot))

            else:
                break

            shot = input('Please try to shoot at another coordinate:')
        
        self.shots.append(shot)
        print('Your shot at {shot} is valid'.format(shot = shot))
        return shot
    
    def place_ships(self):
        pass
    
    def validate_shot(self, shot):
        if len(shot) < 2 or len(shot) > 3:
            return False
        if shot[0] not in 'ABCDEFGHIJ':
            return False
        if shot[1:] not in [str(i) for i in range(1, 11)]:
            return False
        return True

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
                    continue
            else:
                print('Invalid coordinates, please try again')
                continue
        self.coordinates = coords
        print('You placed your ship in the following coordinates: {}'.format(self.coordinates))
        return self.coordinates
    
    def validate_coord(self, coord):
        if len(coord) < 2 or len(coord) > 3:
            return False
        if coord[0] not in 'ABCDEFGHIJ':
            return False
        if coord[1:] not in [str(i) for i in range(1, 11)]:
            return False
        return True