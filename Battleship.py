print("Hello, welcome to Battleship")
class Player:
    def __init__(self, name):
        self.name = name
        self.shots = []
        self.ships = []

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
        print(f"{self.name}, place your ships:")
        for ship in self.ships:
            ship.place_ship()
    
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
    
    def take_damage(self, shot):
        if shot in self.coordinates:
            if shot not in self.hit:
                self.hit.append(shot)
                print('You hit a ship at {}'.format(shot))
                if self.is_sunk():
                    print('You sank a ship!')
            else:
                print('You already hit this coordinate before!')
        else:
            print('You missed at {}'.format(shot))
            
    def is_sunk(self):
        for coord in self.coordinates:
            if coord not in self.hit:
                return False
        return True

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.player1.ships = [Ships(2), Ships(3), Ships(3), Ships(4), Ships(5)]
        self.player2.ships = [Ships(2), Ships(3), Ships(3), Ships(4), Ships(5)]
        self.current_player = player1
        self.other_player = player2
    
    def place_ships(self):
            self.player1.place_ships()
            self.player2.place_ships()
    
    def play(self):
        self.place_ships()

        while True:
            shot = self.current_player.shot()

            hit = False

            for ship in self.other_player.ships:
                if shot in ship.coordinates:
                    ship.take_damage(shot)
                    hit = True
                    break
                
            if not hit:
                print('You missed at {}'.format(shot))
            
            if all(ship.is_sunk() for ship in self.other_player.ships):
                print('{} won!'.format(self.current_player.name))
                break

            self.switch_turn()
    
    def switch_turn(self):
        self.current_player, self.other_player = self.other_player, self.current_player

if __name__ == "__main__":
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    
    game = Game(player1, player2)
    game.play()
