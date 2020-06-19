tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(List):
    colWidths = [0]*len(tableData) #create a list containing the same number of 0 values as the number of inner lists in tableData

    for i in range(len(List)):
        for j in range(len(List[i])):
            if len(List[i][j]) > colWidths[i]:
                colWidths[i] = len(List[i][j]) # store the width of Longest value

    for n in range(len(List[0])):
        for m in range(len(List)):
            print(List[m][n].rjust(colWidths[m]), end= ' ')
        print()

print(printTable(tableData))