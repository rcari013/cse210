from importlib.machinery import WindowsRegistryFinder
from colored import fg

#color variables for erron messaging
white = fg('white')
red = fg('red')

#list of arrays are below
line123 = []
line456 = []
line789 = []
line147 = []
line258 = []
line369 = []
line159 = []
line357 = []

board = "\n1|2|3\n-+-+-\n4|5|6\n-+-+-\n7|8|9"

#for scanning the lines
all_line_list = []

#array to scan each time an entry is done
numbers_taken = []

turn = ""

program_on = 1

o = "o"
x = "x"

def main():
    
    while True:
        enter_turn = str(input('Who will be the first?  "x" or "o" player?\n'))
        entered_turn = enter_turn.lower()
        if entered_turn in ('x', 'o'):
            break
        # in case you want to display error messages in red
        print(red + "I don't recognize that input. Please only enter \"x\" or \"o\"" + white + "\n")
    if entered_turn == 'x':
        turn = 'x'
    if entered_turn == 'o':
        turn = 'o'
    
    print(board)
    running = True
    
    first_number = int(input("\nPlayer " + turn + ". Enter the first number on the board:\n"))
    rewritten_board = rewrite_board(first_number, entered_turn, board)
    print(rewritten_board)
    numbers_taken.append(first_number)
    append_one_or_negative_one_number_to_corresponding_line_list(first_number, turn, line123, line456, line789, line147, line258, line369, line159, line357)
    append_all_lines_to_all_list(all_line_list, line123, line456, line789, line147, line258, line369, line159, line357)

    winner = append_all_line_list_to_all_line_list_and_verify_winner(all_line_list, line123, line456, line789, line147, line258, line369, line159, line357)
    
    number_of_turns = 1
    number = first_number
    
    while winner < 1 or (winner == 0 and number_of_turns !=9):
        turn = change_turn(turn)
        number = int(input("\nPlayer " + turn + ". Enter the desired number on the board:\n"))
        checking_the_number_if_taken = verify_if_number_on_board_is_already_taken(numbers_taken, number)
        checking_the_number_if_one_to_nine = verify_if_number_on_board_is_from_one_to_nine(number)
        
        if checking_the_number_if_taken == 1:
            print("\nThe number is already taken by " + str(change_turn(turn)) + " or the number is invalid. \nPlease select another number.")
            turn = change_turn(turn)
            rewritten_board = rewrite_board(number, turn, rewritten_board)
            print(rewritten_board)
        elif checking_the_number_if_one_to_nine == 0:
            print("\nThe number is not within the range 1 to 9. \nPlease select another number.")
            turn = change_turn(turn)
            rewritten_board = rewrite_board(number, turn, rewritten_board)
            print(rewritten_board)
        else:
            rewritten_board = rewrite_board(number, turn, rewritten_board)
            print(rewritten_board)
            numbers_taken.append(number)
            append_one_or_negative_one_number_to_corresponding_line_list(number, turn, line123, line456, line789, line147, line258, line369, line159, line357)
            winner = append_all_line_list_to_all_line_list_and_verify_winner(all_line_list, line123, line456, line789, line147, line258, line369, line159, line357)
            #print(winner)
            #print(all_line_list)
            number_of_turns += 1
            if winner == 1:
                print("\nWe have a winner! Congratulations Player \"" + turn + "\". You are the winner of this game.")

            elif winner == 0 and number_of_turns == 9:
                print("We don't have a winner. This is draw!")

            elif winner == 0 and number_of_turns == 8:
                print("You two are just going to block each other's lines at the end or no lines for 3 anymore. This is considered draw!")

def verify_if_number_on_board_is_from_one_to_nine(entered_number):
    one_to_nine = [1,2,3,4,5,6,7,8,9]
    indication = 0
    for i in one_to_nine:
        if i == entered_number:
            indication += 1
        else:
            indication += 0
    return indication



def verify_if_number_on_board_is_already_taken(numbers_taken, entered_number):
    sum = 0
    indicator_num = 0
    for i in numbers_taken:
        if i == entered_number:
            sum += 1
        else:
            sum += 0
    if sum > 0:
        indicator_num = 1
    elif sum == 0:
        indicator_num = 0
    return indicator_num
    
def rewrite_board(entered_number, turn, board):
    entered_number_str = str(entered_number)
    if turn == "x":
        new_text = board.replace(entered_number_str,"x")
    else:
        new_text = board.replace(entered_number_str,"o")
    return new_text

def change_turn(turn):
    if turn == "o":
        turn = "x"
    elif turn == "x":
        turn = "o"
    return turn

def append_one_or_negative_one_number_to_corresponding_line_list(entered_number, turn, line123, line456, line789, line147, line258, line369, line159, line357):
    if entered_number == 1 and turn =='x':
        line123.append(-1)
        line147.append(-1)
        line159.append(-1)

    elif entered_number == 2 and turn =='x':
        line123.append(-1)
        line258.append(-1)

    elif entered_number == 3 and turn =='x':
        line123.append(-1)
        line369.append(-1)
        line357.append(-1)

    elif entered_number == 4 and turn =='x':
        line456.append(-1)
        line147.append(-1)

    elif entered_number == 5 and turn =='x':
        line456.append(-1)
        line258.append(-1)
        line159.append(-1)
        line357.append(-1)

    elif entered_number == 6 and turn =='x':
        line456.append(-1)
        line369.append(-1)

    elif entered_number == 7 and turn =='x':
        line789.append(-1)
        line147.append(-1)
        line357.append(-1)

    elif entered_number == 8 and turn =='x':
        line258.append(-1)
        line789.append(-1)

    elif entered_number == 9 and turn =='x':
        line789.append(-1)
        line369.append(-1)
        line159.append(-1)
    
    elif entered_number == 1 and turn =='o':
        line123.append(1)
        line147.append(1)
        line159.append(1)

    elif entered_number == 2 and turn =='o':
        line123.append(1)
        line258.append(1)

    elif entered_number == 3 and turn =='o':
        line123.append(1)
        line369.append(1)
        line357.append(1)

    elif entered_number == 4 and turn =='o':
        line456.append(1)
        line147.append(1)

    elif entered_number == 5 and turn =='o':
        line456.append(1)
        line258.append(1)
        line159.append(1)
        line357.append(1)

    elif entered_number == 6 and turn =='o':
        line456.append(1)
        line369.append(1)

    elif entered_number == 7 and turn =='o':
        line789.append(1)
        line147.append(1)
        line357.append(1)

    elif entered_number == 8 and turn =='o':
        line258.append(1)
        line789.append(1)

    elif entered_number == 9 and turn =='o':
        line789.append(1)
        line369.append(1)
        line159.append(1)

def append_all_line_list_to_all_line_list_and_verify_winner(all_line_list, line123, line456, line789, line147, line258, line369, line159, line357):
    all_line_list.append(line123)
    all_line_list.append(line456)
    all_line_list.append(line789)
    all_line_list.append(line147)
    all_line_list.append(line258)
    all_line_list.append(line369)
    all_line_list.append(line159)
    all_line_list.append(line357)
    n = 0
    winner = 0
    for i in all_line_list:
        sum = 0
        #print(all_line_list[n])
        for n_inside in all_line_list[n]:
            sum = sum + n_inside
            #print(sum)
        if sum == 3 or sum == -3:
            winner = 1
        else:
            winner += 0
        n += 1
    all_line_list.remove(line123)
    all_line_list.remove(line456)
    all_line_list.remove(line789)
    all_line_list.remove(line147)
    all_line_list.remove(line258)
    all_line_list.remove(line369)
    all_line_list.remove(line159)
    all_line_list.remove(line357)
    return winner
            
def append_all_lines_to_all_list(all_line_list, line123, line456, line789, line147, line258, line369, line159, line357):
    all_line_list.append(line123)
    all_line_list.append(line456)
    all_line_list.append(line789)
    all_line_list.append(line147)
    all_line_list.append(line258)
    all_line_list.append(line369)
    all_line_list.append(line159)
    all_line_list.append(line357)            
if __name__ == "__main__":
    main()