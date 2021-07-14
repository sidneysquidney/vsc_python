import copy, random

def create_grid():
    default = [None, None, None]
    top_row = middle_row = bottom_row = left_column = middle_column = right_column = down_diagonal = up_diagonal = [None, None, None]
    rows = [top_row, middle_row, bottom_row, left_column, middle_column, right_column, down_diagonal, up_diagonal]
    numbers = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [7,5,3]]
    acceptable = [1,2,3,4,5,6,7,8,9]
    return numbers, acceptable

def create_dic():
    acceptable = create_grid()[1]
    dictionary = {}
    for number in acceptable:
        dictionary[number] = None
    return dictionary

def assign(taken, side, grid):
    acceptable = create_grid()[1]
    numbers = grid
    taken = taken
    while True:
        number = input()
        if number.isdigit():
            number = int(number)
            if number in acceptable and number not in taken:
                to_assign = []
                for i in range(len(numbers)):
                    coordinates = [0, 0]
                    if number in numbers[i]:
                        coordinates[0] = i
                        for el in range(len(numbers[i])):
                            if number == numbers[i][el]:
                                coordinates[1] = el
                        to_assign.append(coordinates) 
                break
            else:
                print('cannot play here')
        else:
            print('invalid move')
            continue
    for lst in to_assign:
        x, y = lst[0], lst[1]
        numbers[x][y] = side
    return numbers, number

def computer_assign(side, grid, number):
    to_assign = []
    for i in range(len(grid)):
        coordinates = [0, 0]
        if number in grid[i]:
            coordinates[0] = i
            for el in range(len(grid[i])):
                if number == grid[i][el]:
                    coordinates[1] = el
            to_assign.append(coordinates)   
    for lst in to_assign:
        x, y = lst[0], lst[1]
        grid[x][y] = side

def assign_team():
    teams = ['o', 'x', '0']
    question = ['y', 'n']
    human = ['h', 'c']
    level = None
    levels = ['e', 'm', 'i']
    while True:
        player_1 = str(input('Player 1. would you like to play as naughts or crosses?'))
        if player_1 in teams:
            if player_1 in ['0', 'o']:
                player_1, player_2 = 'o', 'x'
            else:
                player_1, player_2 = 'x', 'o'
            break
        else:
            print('input o/x')
            continue
    while True:
        first_turn = input('would you like to go first y/n?').lower()
        if first_turn in question:
            if first_turn == 'y':
                first_turn = player_1
            else:
                first_turn = player_2
            break
        else:
            print('input y/n')
            continue
    while True:
        second_player = input('do you want to play against a human or a computer - h/c?')
        if second_player in human:
            if second_player == 'c':
                while True:
                    level = input('what level computer would you like to play against? easy, medium, impossible?')
                    if level in levels:
                        if level == 'e':
                            level = 'easy'
                        elif level == 'm':
                            level = 'medium'
                        else:
                            level = 'impossible'
                        break
                    else:
                        print('input e/m/i')
                        continue
                second_player = 'computer'
                break
            else:
                second_player = 'human'
                break
        else:
            print('input c/h')
            continue
    return player_1, player_2, first_turn, second_player, level 
            
def print_grid(grid):
    for lst in grid[:3]:
        print(lst)

def print_grid_2(grid):
    acceptable = create_grid()[1]
    temp_grid = copy.deepcopy(grid)[:3]
    for lst in temp_grid:
        for i in range(len(lst)):
            if lst[i] in acceptable:
                lst[i] = '_'
    for lst in temp_grid:
        print(lst)
    return

def still_playing(grid, side, taken):
    for lst in grid:
        if lst.count(lst[0]) == 3:
            return False
    if len(taken) == 9:
            return False
    return True

def winner(grid):
    for lst in grid:
        if lst.count('x') == 3:
            return 'x'
        elif lst.count('o') == 3:
            return 'o'
    return 'no winner'

def change_side(side):
    if side == 'x':
        return 'o'
    else:
        return 'x'

def available(taken):
    acceptable = create_grid()[1]
    return [num for num in acceptable if num not in taken]

def computer_turn(grid, computer_side, level, taken, dic):
    human_side = change_side(computer_side)
    if level == 'easy':
        number = random.choice(available(taken))
        computer_assign(computer_side, grid, number)
        return grid, number
    elif level == 'medium':
        for row in grid:
            if row.count(computer_side) == 2 and human_side not in row:
                number = [x for x in row if x != computer_side][0]
                computer_assign(computer_side, grid, number)
                return grid, number
        for row in grid:
            if row.count(human_side) == 2 and computer_side not in row:
                number = [x for x in row if x != human_side][0]
                computer_assign(computer_side, grid, number)
                return grid, number
        number = random.choice(available(taken))
        computer_assign(computer_side, grid, number)
        return grid, number
    elif level == 'impossible':
        for row in grid:
            if row.count(computer_side) == 2 and human_side not in row:
                number = [x for x in row if x != computer_side][0]
                computer_assign(computer_side, grid, number)
                return grid, number
        for row in grid:
            if row.count(human_side) == 2 and computer_side not in row:
                number = [x for x in row if x != human_side][0]
                computer_assign(computer_side, grid, number)
                return grid, number
        if len(available(taken)) == 9:
            number = 1
            computer_assign(computer_side, grid, number)
            return grid, number
        if len(available(taken)) == 7:
            if 9 in available(taken):
                number = 9
            else:
                number = 5
            computer_assign(computer_side, grid, number)
            return grid, number
        if len(available(taken)) == 5:
            if 2 in available(taken):
                number = 3
            else:
                number = 7
            computer_assign(computer_side, grid, number)
            return grid, number
        elif len(available(taken)) == 8:
            if 5 in available(taken):
                number = 5
            else:
                number = 1
            computer_assign(computer_side, grid, number)
            return grid, number
        if len(available(taken)) == 6:
            if 5 in taken and 1 in taken and 9 in taken or 7 in taken and 5 in taken and 3 in taken:
                if dic[5] == human_side:
                    if 7 in taken:
                        number = 9
                    else:
                        number = 7
                else:
                    number = 8
                computer_assign(computer_side, grid, number)
                return grid, number
            elif 2 in taken and 4 in taken and 5 in taken or 2 in taken and 5 in taken and 6 in taken or 4 in taken and 5 in taken and 8 in taken or 5 in taken and 6 in taken and 8 in taken:
                if 2 in taken:
                    number = 1
                elif 8 in taken:
                    number = 9
                print('last version')
                computer_assign(computer_side, grid, number)
                return grid, number
            else:
                print('get random')
                number = random.choice(available(taken))
                computer_assign(computer_side, grid, number)
                return grid, number
        number = random.choice(available(taken))
        computer_assign(computer_side, grid, number)
        return grid, number

def play_game():
    player_1, player_2, first_turn, opponent, level = assign_team()
    grid, acceptable = create_grid()
    taken = []
    player = first_turn
    dic = create_dic()
    playing = False
    print('input 1-9 for the grid position')
    for lst in grid[:3]:
        print(lst)
    while still_playing(grid, player, taken):
        if first_turn == player_1 or playing or opponent == 'human':
            print_grid_2(grid)
            print('{} it is your turn'.format(player))
            grid, number = assign(taken, player, grid)
            taken.append(number)
            dic[number] = player
        if len(taken) == 9:
            break
        if opponent == 'human':
            player = change_side(player)
        else:
            grid, number = computer_turn(grid, player_2, level, taken, dic)
            taken.append(number)
            dic[number] = player_2
        playing = True
        if opponent == 'computer':
            player = player_1
    print_grid_2(grid)
    print('the winner is {}'.format(winner(grid)))
    return 

play_game()