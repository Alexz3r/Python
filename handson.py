class MatchsticksGame:
    matchsticks = 23

    
    def __is_valid_input(self, player):
        return 1 <= player <= 3
            

    def __show_matchsticks(self):
        return '||||| '*(self.matchsticks//5) + '|'*(self.matchsticks%5)


    def __game_finish(self):
        return self.matchsticks <= 0
        

    def play(self):
        player2 = False
        print('Game starts')
        print(self.__show_matchsticks())

        while True:
            try:
                player = int(input(f'The player {player2+1} remove: '))

                if not self.__is_valid_input(player):
                    print('You can delete only between 1 and 3 matchsticks.')
                    continue

                self.matchsticks -= player
                print(self.__show_matchsticks())

                if self.__game_finish():
                    print(f'The player {player2+1} is eliminated.')
                    break

                player2 = not player2
            except:
                print('You can only enter numeric values.')


if __name__ == '__main__':
    game = MatchsticksGame()
    game.play()