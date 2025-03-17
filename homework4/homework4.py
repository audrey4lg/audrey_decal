#1 continue to explain debugging throughout the entire homework set

#2.1 Making a List Variable
countingnumbers = list(range(21))
print(countingnumbers)

#2.2 Working with List Elements
countingnumbers = list(range(21))
def squarelist(countingnumbers):
    return [num ** 2 for num in countingnumbers]
countingsquares = squarelist(countingnumbers)
print(countingsquares)

#2.3 Slicing
# numberssquared = countingsquares(countingnumbers) #"list object is uncallable" and also unnecessary so removed it
def numberssquared(countingsquares):
    return countingsquares[:15] #put pranthesis instead of brackets
# numberssquared = countingsquares(squarelist) #list object is not callable so i did the line below instead
firstfifteen = numberssquared(countingsquares)
print(firstfifteen)

#2.4 Striding
def fifthelement(countingsquares):
    return countingsquares[4::5]
everyfifthelement = fifthelement(countingsquares)
print(everyfifthelement)

#2.5 Slicing and Striding
def fancy_function(countingsquares):
    return countingsquares[-3::-3]
back3fromback = fancy_function(countingsquares)
print(back3fromback)

#3
#3.1 Creating a 5x5 2D list
def create_2d_list():
    matrix = []
    count = 1
    for i in range(5): #syntaxerror: expected ':' so added it in
        row = []
        for j in range(5):
            row.append(count)
            count += 1
        matrix.append(row)
    return matrix
matrix = create_2d_list()
print(matrix)

#3.2 Replacing 2D list with multiples of 3
matrix = create_2d_list()
def modified_2d_list(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] % 3 == 0 : #typeerror:not all arguments conversted during string formatting, unsure how to fix, simply retyped and somehow it worked
                matrix[i][j] = '?'
    return(matrix)
modified = modified_2d_list(matrix)
print(modified)

#3.3 Summing Non-'?' Elements
def sum_non_question_elements(matrix):
    total = 0  
    for row in matrix: 
        for num in row:  
            if num != '?':  
                total += num  
    return total
# new_matrix = modified_2d_list(matrix) #already put this as modified so just removed it and simplified what im printing
answer = sum_non_question_elements(modified)
print(answer)