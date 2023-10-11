import time

def sudokuSolve(puzzle):
    new_puzzle = []
    for row in puzzle:
        temp_row = []
        for char in row:
            if char == 0:
                temp_row.append(set([1,2,3,4,5,6,7,8,9]))
            else:
                temp_row.append([char])
        new_puzzle.append(temp_row)
    puzzle = new_puzzle
    puzzle = solveCrossHatch(puzzle)
    
    return puzzle
        
def solveCrossHatch(puzzle):
    #rowcheck
    for r in range(0,9):
        for c in range(0,9):
            if len(puzzle[r][c])>1:
                for col in puzzle[r]:
                    if len(col)==1:
                        print("ROWCHECK removing possibility",col,"from",r+1,c+1,"leaving",puzzle[r][c])
                        puzzle[r][c] -= set(col)
                    
                

    #colcheck is broken
    for c in range(0,9):
        for r in range(0,9):
            if len(puzzle[r][c])>1:
                for row in range(0,9):
                    if len(puzzle[row][c])==1:
                        print("COLCHECK removing possibility",puzzle[row][c],"from",r+1,c+1,"leaving",puzzle[r][c])
                        puzzle[r][c] -= set(puzzle[row][c])
            

    # this part is stupid.
    for row in puzzle:
        for col in row:
            if len(col)==1:
                pass
    return puzzle

def printSudoku(puzzle):
    print("_"+"______"*3)
    for row in puzzle:
        temp_row = "|"
        for char in row:
            if len(char)>1:
                temp_row += " |"
            else:
                temp_row += str(char[0]) +"|"
       
        print(temp_row)
        print("_"+"_____|"*3)
        

start = time.time()


file = open('problem96_files/sudoku.txt', 'r')
line_number = 0
cumSum = 0
puzzle = []
for line in file:
    print(line)
    line_number+=1

    if not line_number%10==1:
        line = line.replace('\n','')
        temp_line = []
        for char in line:
            temp_line.append(int(char))
        puzzle.append(temp_line)
    if line_number%10==0:
        puzzle = sudokuSolve(puzzle)
        #cumSum += solved[0][0]*100 + solved[0][1]*100 + solved[0][2]
        break
        puzzle = []

printSudoku(puzzle)
end = time.time()
print("found in",str(end-start),"Answer is",str())
