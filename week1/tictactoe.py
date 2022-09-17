import os
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
turn = ""

#for scanning the lines
all_line_list = []

#array to scan each time an entry is done
numbers_taken = []


def program():
    clear_all_array()
    first_phase = 1
    second_phase = 1
    turn = ""


    board = "\n1|2|3\n-+-+-\n4|5|6\n-+-+-\n7|8|9"
    
    
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
    
    while first_phase == 1:
        try:
            first_number = int(input("\nPlayer " + turn + ". Enter the first number on the board:\n"))
            first_entry_checking_the_number_if_one_to_nine = verify_if_number_on_board_is_from_one_to_nine(first_number)
            while first_entry_checking_the_number_if_one_to_nine == 0:
                print("\nThe number is not within the range 1 to 9. \nPlease select another number.")
                print(board)
                break
                
            else:
                board = rewrite_board(first_number, entered_turn, board)
                print(board)
                numbers_taken.append(first_number)
                append_one_or_negative_one_number_to_corresponding_line_list(first_number, turn, line123, line456, line789, line147, line258, line369, line159, line357)
                append_all_lines_to_all_list(all_line_list, line123, line456, line789, line147, line258, line369, line159, line357)

                winner = append_all_line_list_to_all_line_list_and_verify_winner(all_line_list, line123, line456, line789, line147, line258, line369, line159, line357)
                
                number_of_turns = 1
                number = first_number
                first_phase = 0
        except ValueError:
            print("\nOops!  That was no valid number.  Try again...\n")
            print(board)
    
    while winner < 1 or (winner == 0 and number_of_turns !=9):
        turn = change_turn(turn)
        
        while second_phase == 1:
            try:
                number = int(input("\nPlayer " + turn + ". Enter the desired number on the board:\n"))
                checking_the_number_if_taken = verify_if_number_on_board_is_already_taken(numbers_taken, number)
                checking_the_number_if_one_to_nine = verify_if_number_on_board_is_from_one_to_nine(number)
                if checking_the_number_if_taken == 1:
                    
                    print("\nThe number is already taken. Check the board. \nPlease select another number.")
                    board = rewrite_board(number, turn, board)
                    print(board)
                elif checking_the_number_if_one_to_nine == 0:
                    
                    print("\nThe number is not within the range 1 to 9. \nPlease select another number.")
                    
                    board = rewrite_board(number, turn, board)
                    print(board)
                else:
                    
                    board = rewrite_board(number, turn, board)
                    print(board)
                    numbers_taken.append(number)
                    append_one_or_negative_one_number_to_corresponding_line_list(number, turn, line123, line456, line789, line147, line258, line369, line159, line357)
                    winner = append_all_line_list_to_all_line_list_and_verify_winner(all_line_list, line123, line456, line789, line147, line258, line369, line159, line357)
                    #print(winner)
                    #print(all_line_list)
                    turn = change_turn(turn)
                    number_of_turns += 1
                    if winner == 1:
                        print("\nWe have a winner! Congratulations Player \"" + str(change_turn(turn)) + "\". You are the winner of this game.")
                        second_phase = 0
                    elif winner == 0 and number_of_turns == 8:
                        print("You two are just going to block each other's lines so there's no need to continue this game. This is draw. Game over!")
                        winner = 1
                        second_phase = 0
                        
                        
                
            except ValueError:
                print("\nOops!  That was no valid number.  Try again...")
                print(board)

def main():
    while True:
        program()
        while True:
            answer = str(input('\nDo you want to restart the program? (y/n): ')).lower()
            if answer in ('y', 'n'):

                break
            # in case you want to display error messages in red

            print(red + "I don't recognize that input." + white)
        if answer == 'y':
            os.system('cls')
            
            continue


        if answer == 'n':
            print("\nProgram is now closed")
            input("\nPress enter to exit the program")
            break

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

def clear_all_array():
    all_line_list.clear()
    line123.clear()
    line456.clear()
    line789.clear()
    line147.clear()
    line258.clear()
    line369.clear()
    line159.clear()
    line357.clear()
    numbers_taken.clear()    


if __name__ == "__main__":
    main()
        