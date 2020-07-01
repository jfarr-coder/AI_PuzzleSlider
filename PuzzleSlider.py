# Was Meant to include Puzzle Class and be Used for BFS, DFS, and Heuristics Search
class state:
    def __init__(self,present):
        self.present=present
        self.next=None

class puzzle:
    def __init__(self, rows, columns,elems, numTiles, Table, GTable):
        self.rows=rows
        self.columns=columns
        self.elems=elems
        self.numTiles=numTiles
        self.Table=[]
        self.GTable=[]
    
    def displayStats(self):
        print("Number of Rows: {}".format(self.rows))
        print("Number of Columns: {}".format(self.columns))
        print("Number of Tiles: {}".format(self.numTiles))
        print("Number of Elements: {}".format(self.elems))
    
    def fillTable(self, Table):
        temp=0
        self.Table=[]
        #instantiating Beginning state as a variable
        errM2=("This value does not fit within  the range of 1 and {}".format(self.elems))
        errM3=("The Values in the puzzle repeat themselves")
        while(temp!=self.numTiles):
            inp=int(input("Enter either a 0 for blank tile or a Number in the range between 1 and {}:".format(self.elems)))
            if inp>elems or inp<0:
                while (inp>self.elems or inp<0):
                    print(errM2)
                    inp=int(input("Enter either a 0 for blank tile or a Number in the range between 1 and {}:".format(self.elems)))
            else:
                self.Table.append(inp)
            temp+=1
    
    def findBlank(self):
        for slide in self.Table:
            if self.Table[slide]==0:
                b=blankTile(slide)
                b.display()

    def getGoalState(self, GTable):
        # Creating Goal State as a string variable
        GTable = []
        num=1
        while(num<=self.elems):
            numS=str(num)
            GTable.append(numS)
            num+=1
        GTable.append('0')

        Gstate='|'
        for slide in GTable:
            temp=slide+'|'
            Gstate+=temp
 
        print("Goal State: {}".format(Gstate))
    
    # Was Meant to find the Number of Misplaced Tiles by Comparing the Beginning State and the Goal State
    def compTables(self, Table, GTable):
        numMis=0
        for slide in self.Table:
            if self.Table[slide]!=self.GTable[slide]:
                numMis+=1
        print("The Number of Misplaced Tiles is: {}".format(numMis))

    def displayTable(self): 
        # Creating Beginning State as a string variable
        Bstate='|'
        for slide in self.Table:
            temp=str(slide)+'|'
            Bstate+=temp
        print("Beginning State: {}".format(Bstate))

class blankTile:
    value=0
    blank=True
    def __init__(self, index):
        self.index=index

    def display(self):
        print("Index of Tile: {}".format(self.index))
        print("Value of Tile: {}".format(self.value))
        print("Blank: {}".format(self.blank))

#Getting the Number of Rows and Columns in the Puzzle
r= int(input("How Many Rows:"))
c= int(input("How Many Colums:"))

# Implementing a Condition in Which The Number of Rows and Columns are less than 3
errM="This Program Can't Move Forward Because There's Not Enough Rows and Columns"
if r<3 or c<3:
    while(r<3 or c<3):
        print(errM)
        r= int(input("How Many Rows:"))
        c= int(input("How Many Colums:"))

# Setting both the number of Tiles and Elements in the puzzle
numTiles= r*c
elems=numTiles-1
bTable=[]
gTable=[]
p = puzzle(r,c,elems,numTiles,bTable,gTable)
p.displayStats()
p.fillTable(bTable)
p.displayTable()
p.getGoalState(gTable)
p.findBlank()
#p.compTables(bTable, gTable)