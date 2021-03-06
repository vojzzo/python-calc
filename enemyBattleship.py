import random
enemyBoard={'a0':'_','a1':'_','a2':'_','a3':'_','a4':'_','a5':'_', 'a6':'_','a7':'_', 'a8':'_','a9':'_',
            'b0':'_','b1':'_','b2':'_','b3':'_','b4':'_','b5':'_', 'b6':'_','b7':'_', 'b8':'_','b9':'_',
            'c0':'_','c1':'_','c2':'_','c3':'_','c4':'_','c5':'_', 'c6':'_','c7':'_', 'c8':'_','c9':'_',
            'd0':'_','d1':'_','d2':'_','d3':'_','d4':'_','d5':'_', 'd6':'_','d7':'_', 'd8':'_','d9':'_',
            'e0':'_','e1':'_','e2':'_','e3':'_','e4':'_','e5':'_', 'e6':'_','e7':'_', 'e8':'_','e9':'_',
            'f0':'_','f1':'_','f2':'_','f3':'_','f4':'_','f5':'_', 'f6':'_','f7':'_', 'f8':'_','f9':'_',
            'g0':'_','g1':'_','g2':'_','g3':'_','g4':'_','g5':'_', 'g6':'_','g7':'_', 'g8':'_','g9':'_',
            'h0':'_','h1':'_','h2':'_','h3':'_','h4':'_','h5':'_', 'h6':'_','h7':'_', 'h8':'_','h9':'_',
            'i0':'_','i1':'_','i2':'_','i3':'_','i4':'_','i5':'_', 'i6':'_','i7':'_', 'i8':'_','i9':'_',
            'j0':'_','j1':'_','j2':'_','j3':'_','j4':'_','j5':'_', 'j6':'_','j7':'_', 'j8':'_','j9':'_'}

enemyPlaces =  ['a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9',
                'b0', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9',
                'c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9',
                'd0', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9',
                'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9',
                'f0', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
                'g0', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'g9',
                'h0', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9',
                'i0', 'i1', 'i2', 'i3', 'i4', 'i5', 'i6', 'i7', 'i8', 'i9',
                'j0', 'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'j8', 'j9']

def printBoard(board):
    print('  0 1 2 3 4 5 6 7 8 9')
    print('A'+ ' ' + board['a0'] + ' ' + board['a1'] + ' ' + board['a2'] + ' ' + board['a3'] + ' ' + board['a4'] + ' ' + board['a5'] + ' ' + board['a6'] + ' ' + board['a7'] + ' ' + board['a8']  + ' ' + board['a9'])
    
    print('B'+ ' ' + board['b0'] + ' ' + board['b1'] + ' ' + board['b2'] + ' ' + board['b3'] + ' ' + board['b4'] + ' ' + board['b5'] + ' ' + board['b6'] + ' ' + board['b7'] + ' ' + board['b8']  + ' ' + board['b9'])

    print('C'+ ' ' + board['c0'] + ' ' + board['c1'] + ' ' + board['c2'] + ' ' + board['c3'] + ' ' + board['c4'] + ' ' + board['c5'] + ' ' + board['c6'] + ' ' + board['c7'] + ' ' + board['c8']  + ' ' + board['c9'])

    print('D'+ ' ' + board['d0'] + ' ' + board['d1'] + ' ' + board['d2'] + ' ' + board['d3'] + ' ' + board['d4'] + ' ' + board['d5'] + ' ' + board['d6'] + ' ' + board['d7'] + ' ' + board['d8']  + ' ' + board['d9'])
    
    print('E'+ ' ' + board['e0'] + ' ' + board['e1'] + ' ' + board['e2'] + ' ' + board['e3'] + ' ' + board['e4'] + ' ' + board['e5'] + ' ' + board['e6'] + ' ' + board['e7'] + ' ' + board['e8']  + ' ' + board['e9'])
    
    print('F'+ ' ' + board['f0'] + ' ' + board['f1'] + ' ' + board['f2'] + ' ' + board['f3'] + ' ' + board['f4'] + ' ' + board['f5'] + ' ' + board['f6'] + ' ' + board['f7'] + ' ' + board['f8']  + ' ' + board['f9'])

    print('G'+ ' ' + board['g0'] + ' ' + board['g1'] + ' ' + board['g2'] + ' ' + board['g3'] + ' ' + board['g4'] + ' ' + board['g5'] + ' ' + board['g6'] + ' ' + board['g7'] + ' ' + board['g8']  + ' ' + board['g9'])

    print('H'+ ' ' + board['h0'] + ' ' + board['h1'] + ' ' + board['h2'] + ' ' + board['h3'] + ' ' + board['h4'] + ' ' + board['h5'] + ' ' + board['h6'] + ' ' + board['h7'] + ' ' + board['h8']  + ' ' + board['h9'])
    
    print('I'+ ' ' + board['i0'] + ' ' + board['i1'] + ' ' + board['i2'] + ' ' + board['i3'] + ' ' + board['i4'] + ' ' + board['i5'] + ' ' + board['i6'] + ' ' + board['i7'] + ' ' + board['i8']  + ' ' + board['i9'])

    print('J'+ ' ' + board['j0'] + ' ' + board['j1'] + ' ' + board['j2'] + ' ' + board['j3'] + ' ' + board['j4'] + ' ' + board['j5'] + ' ' + board['j6'] + ' ' + board['j7'] + ' ' + board['j8']  + ' ' + board['j9'])
    print('')
    
def enemyShip(length):
    global enemyBoard
    global emptyPlaces
    alphabet = 'abcdefghij'
    possibleDirs = []
    place = random.choice(enemyPlaces)
    letterIndex = alphabet.index(place[0])

    if int(place[1]) <= 9 - length + 1:
        for i in range(length):
            if enemyBoard[place[0] + str(int(place[1]) + i)] == '_':
                if 'r' not in possibleDirs:
                    possibleDirs.append('r')
        
                if letterIndex >=  length - 1:
                    secLetterIndex = letterIndex - i
                    if enemyBoard[alphabet[secLetterIndex] + place[1]] == '_':
                        if 'u' not in possibleDirs:
                            possibleDirs.append('u')
                    
                if letterIndex <= 9 - length + 1:
                    secLetterIndex = letterIndex + i
                    if enemyBoard[alphabet[secLetterIndex] + place[1]] == '_':
                        if 'd' not in possibleDirs:
                            possibleDirs.append('d')
            
    if int(place[1]) >= length - 1:
        for i in range(length):
                if enemyBoard[place[0] + str(int(place[1]) - i)] == '_':
                    if 'l' not in possibleDirs:
                        possibleDirs.append('l')
                
                if letterIndex >=  length - 1:
                    secLetterIndex = letterIndex - i
                    if enemyBoard[alphabet[secLetterIndex] + place[1]] == '_':
                        if 'u' not in possibleDirs:
                            possibleDirs.append('u')
                        
                if letterIndex <= 9 - length + 1:
                    secLetterIndex = letterIndex + i
                    if enemyBoard[alphabet[secLetterIndex] + place[1]] == '_':
                        if 'd' not in possibleDirs:
                            possibleDirs.append('d')
    direc = random.choice(possibleDirs)
    if direc == 'r':
        for i in range(length):
            if int(place[1]) + i <= 9:            
                if enemyBoard[place[0] + str(int(place[1]) + i)] == '_':
                    enemyBoard[place[0] + str(int(place[1]) + i)] = 'o'
                    if place[0] + str(int(place[1]) + i) in enemyPlaces:
                        enemyPlaces.remove(place[0] + str(int(place[1]) + i))
                else:
                   enemyBoard = dict.fromkeys(enemyBoard, '_')
                   print('END')
                   break
            else:
                enemyBoard = dict.fromkeys(enemyBoard, '_')
                print('END')
                break
                
    elif direc == 'l':
        for i in range(length):
            if int(place[1]) - i >= 0:
                if enemyBoard[place[0] + str(int(place[1]) - i)] == '_':
                    enemyBoard[place[0] + str(int(place[1]) - i)] = 'o'
                    if place[0] + str(int(place[1]) - i) in enemyPlaces:
                        enemyPlaces.remove(place[0] + str(int(place[1]) - i))
                else:
                   enemyBoard = dict.fromkeys(enemyBoard, '_')
                   print('END')
                   break
            else:
                enemyBoard = dict.fromkeys(enemyBoard, '_')
                print('END')
                break
                
    elif direc == 'u':
        for i in range(length):
            secLetterIndex = letterIndex - i
            if secLetterIndex >= 0:
                if enemyBoard[alphabet[secLetterIndex] + place[1]] == '_':
                    enemyBoard[alphabet[secLetterIndex] + place[1]] = 'o'
                    if alphabet[secLetterIndex] + place[1] in enemyPlaces:
                        enemyPlaces.remove(alphabet[secLetterIndex] + place[1])
                else:
                    enemyBoard = dict.fromkeys(enemyBoard, '_')
                    print('END')
                    break
            else:
                enemyBoard = dict.fromkeys(enemyBoard, '_')
                print('END')
                break
                
    elif direc == 'd':
        for i in range(length):
            secLetterIndex = letterIndex + i
            if secLetterIndex <= 9:
                if enemyBoard[alphabet[secLetterIndex] + place[1]] == '_':
                    enemyBoard[alphabet[secLetterIndex] + place[1]] = 'o'
                    if alphabet[secLetterIndex] + place[1] in enemyPlaces:
                        enemyPlaces.remove(alphabet[secLetterIndex] + place[1])
                else:
                    enemyBoard = dict.fromkeys(enemyBoard, '_')
                    print('END')
                    break
            else:
                enemyBoard = dict.fromkeys(enemyBoard, '_')
                print('END')
                break

while len(enemyPlaces) != 83:
    enemyBoard = dict.fromkeys(enemyBoard, '_')
    enemyPlaces =  ['a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9',
                    'b0', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9',
                    'c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9',
                    'd0', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9',
                    'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9',
                    'f0', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
                    'g0', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'g9',
                    'h0', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9',
                    'i0', 'i1', 'i2', 'i3', 'i4', 'i5', 'i6', 'i7', 'i8', 'i9',
                    'j0', 'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'j8', 'j9']
    enemyShip(5)
    enemyShip(4)
    enemyShip(3)
    enemyShip(3)
    enemyShip(2)

printBoard(enemyBoard)
print(len(enemyPlaces))
input('Press ENTER to exit')


    
    