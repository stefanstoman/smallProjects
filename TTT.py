#This is my attempt to create a tick-tack-toe game

print('Welcome to Stefan-Tick-Tack-Toe!')
print('How to play the game:')
print('Select the block to place your mark with numbers 1 - 3.')
print('The first number is the vertical index, the second the horizontal index.')
print('Enter d to quit the game.')
print('Have fun!')

#Create the playing board with lists

first_row = [' ', ' ', ' ',]
sec_row = [' ', ' ', ' ',]
third_row = [' ', ' ', ' ',]

#Display the playing board using print statement

print('|', first_row[0],'|', first_row[1], '|', first_row[2], '|')
print('|', sec_row[0],'|', sec_row[1], '|', sec_row[2], '|')
print('|', third_row[0],'|', third_row[1], '|', third_row[2], '|')

#While loop to loop through the game

player = 1 #initialise the player

while True:
    if player == 0: #Player set to 0 will end the loop
        break
    while player ==1:
        pos1 = input('Player1, please select the position of the mark: ') #This part to add elements to the board
        if pos1 == 'd': 
            player = 0  #Input of d will set player to 0 causing the loop to end
            break
        if pos1[0] == '1':
            if pos1[1] == '1':
                first_row[0] = 'X'
            if pos1[1] == '2':
                first_row[1] = 'X'
            if pos1[1] == '3':
                first_row[2] = 'X'
        if pos1[0] == '2':
            if pos1[1] == '1':
                sec_row[0] = 'X'
            if pos1[1] == '2':
                sec_row[1] = 'X'
            if pos1[1] == '3':
                sec_row[2] = 'X'
        if pos1[0] == '3':
            if pos1[1] == '1':
                third_row[0] = 'X'
            if pos1[1] == '2':
                third_row[1] = 'X'
            if pos1[1] == '3':
                third_row[2] = 'X'    
            
        print('|', first_row[0],'|', first_row[1], '|', first_row[2], '|')
        print('|', sec_row[0],'|', sec_row[1], '|', sec_row[2], '|')
        print('|', third_row[0],'|', third_row[1], '|', third_row[2], '|')
        
        #Check for winning conditions and if there is a win, reset the board
        
        if first_row[0] == 'X' and sec_row[0] == 'X' and third_row[0] == 'X':
            print('Player 1 wins!')
            first_row = [' ', ' ', ' ',]
            sec_row = [' ', ' ', ' ',]
            third_row = [' ', ' ', ' ',]
            break
            
        if first_row[1] == 'X' and sec_row[1] == 'X' and third_row[1] == 'X':
            print('Player 1 wins!')
            first_row = [' ', ' ', ' ',]
            sec_row = [' ', ' ', ' ',]
            third_row = [' ', ' ', ' ',]
            break
            
        if first_row[2] == 'X' and sec_row[2] == 'X' and third_row[2] == 'X':
            print('Player 1 wins!')
            first_row = [' ', ' ', ' ',]
            sec_row = [' ', ' ', ' ',]
            third_row = [' ', ' ', ' ',]
            break
            
        if first_row[0] == 'X' and first_row[1] == 'X' and first_row[2] == 'X':
            print('Player 1 wins!')
            first_row = [' ', ' ', ' ',]
            sec_row = [' ', ' ', ' ',]
            third_row = [' ', ' ', ' ',]
            break
            
        if sec_row[0] == 'X' and sec_row[1] == 'X' and sec_row[2] == 'X':
            print('Player 1 wins!')
            first_row = [' ', ' ', ' ',]
            sec_row = [' ', ' ', ' ',]
            third_row = [' ', ' ', ' ',]
            break     
            
        if third_row[0] == 'X' and third_row[1] == 'X' and third_row[2] == 'X':
            print('Player 1 wins!')
            first_row = [' ', ' ', ' ',]
            sec_row = [' ', ' ', ' ',]
            third_row = [' ', ' ', ' ',]
            break
        
        player = 2
        
    while player == 2:
        pos2 = input('Player2, please select the position of the mark: ') #This part to add elements to the board
        if pos2 == 'd': 
            player = 0
            break
        if pos2[0] == '1':
            if pos2[1] == '1':
                first_row[0] = 'O'
            if pos2[1] == '2':
                first_row[1] = 'O'
            if pos2[1] == '3':
                first_row[2] = 'O'
        if pos2[0] == '2':
            if pos2[1] == '1':
                sec_row[0] = 'O'
            if pos2[1] == '2':
                sec_row[1] = 'O'
            if pos2[1] == '3':
                sec_row[2] = 'O'
        if pos2[0] == '3':
            if pos2[1] == '1':
                third_row[0] = 'O'
            if pos2[1] == '2':
                third_row[1] = 'O'
            if pos2[1] == '3':
                third_row[2] = 'O'    
            
        print('|', first_row[0],'|', first_row[1], '|', first_row[2], '|')
        print('|', sec_row[0],'|', sec_row[1], '|', sec_row[2], '|')
        print('|', third_row[0],'|', third_row[1], '|', third_row[2], '|')
        
        #Check for winning conditions and if there is a win, reset the board
        
        if first_row[0] == 'O' and sec_row[0] == 'O' and third_row[0] == 'O':
            print('Player 2 wins!')
            first_row = [' ', ' ', ' ',]
            sec_row = [' ', ' ', ' ',]
            third_row = [' ', ' ', ' ',]
            break
            
        if first_row[1] == 'O' and sec_row[1] == 'O' and third_row[1] == 'O':
            print('Player 2 wins!')
            first_row = [' ', ' ', ' ',]
            sec_row = [' ', ' ', ' ',]
            third_row = [' ', ' ', ' ',]
            break
            
        if first_row[2] == 'O' and sec_row[2] == 'O' and third_row[2] == 'O':
            print('Player 2 wins!')
            first_row = [' ', ' ', ' ',]
            sec_row = [' ', ' ', ' ',]
            third_row = [' ', ' ', ' ',]
            break
            
        if first_row[0] == 'O' and first_row[1] == 'O' and first_row[2] == 'O':
            print('Player 2 wins!')
            first_row = [' ', ' ', ' ',]
            sec_row = [' ', ' ', ' ',]
            third_row = [' ', ' ', ' ',]
            break
            
        if sec_row[0] == 'O' and sec_row[1] == 'O' and sec_row[2] == 'O':
            print('Player 2 wins!')
            first_row = [' ', ' ', ' ',]
            sec_row = [' ', ' ', ' ',]
            third_row = [' ', ' ', ' ',]
            break     
            
        if third_row[0] == 'O' and third_row[1] == 'O' and third_row[2] == 'O':
            print('Player 2 wins!')
            first_row = [' ', ' ', ' ',]
            sec_row = [' ', ' ', ' ',]
            third_row = [' ', ' ', ' ',]
            break
        
        player = 1
