import tkinter
import time 

x = 600
y = 600
Take_peice = 30
King_maker = 20
Core_dominance = 5
In_danger = -10
Is_danger = 15

class CheckersBoard(tkinter.Frame): # A class to hold/represent all the board functions and the GUI
    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent )
        self.parent = parent
        self.Interface()
        self.turn = "yellow"
        self.rules = []
        self.score = 0
    
    def Game_Reset(self): #A function to help resent the game by destroying the current state of the board 
        for wiget in self.winfo_children():
            wiget.destroy()
        # Reset graveyard counters
        self.yellow_graveyard_count = 0
        self.ai_graveyard_count = 0
        self.checker_pos = {}
        self.check_grid_pos = {}
        self.drag_data = {"Y-oval": None, "R-oval": None, "Y-king": None, "R-king": None, "x": 0, "y": 0}
        self.turn = "yellow"
        # Rebuild the interface (board + pieces)
        self.Interface()
        print("Game has been reset.")
        
    def Rule_Guide_window(self): # Rule guide for player reference
        rule_window = tkinter.Toplevel()
        rule_window.title("Guide")
        rule = tkinter.Label(rule_window, text=
                                        "Guide:" # a guide on the over all game 
                                        "\n\nWelcome to the checkers play guide. The aim of checkers is to capture as many of"
                                        "\nyour oponents (an Artifical intelligence using the Minimax algorithem) checkers as "
                                        "\nposible or block as many of the oppoents checkers as posible so that they can no longer move."
                                        "\nTo play take it in turns to move you checkers diagonatly on the black squares and capture peices. "
                                        "\nTo take a pecice you must juump over. If you reach to opposite side you may king a checker"
                                        "\nthis means that this peice may move back and forward diagnonaly."
                                        
                                        "\n\nRules:" # the rule set for checkers
                                        "\n\nRule 1: A checker shall only be moved diagonaly one squar at a time"
                                        "\nRule 2: A checker shall not move backwards"
                                        "\nRule 3: A checker shall become kinged if it reaches the last row opposite to the players stide of the board"
                                        "\nRule 4: A kinged checker shall move forward and backwards diagonaly"
                                        "\nRule 5: Capturing is mandatory, if an opponents checker is diagonaly adjasent and the square diagonaly agasent to that checker is free"
                                        "\nRule 6: Multiple captures are then also mandatory if when rule 3 is applicable recusivly, but if more than"
                                        "\none checker is avalible to capture then there is a free choise as to which checker to capture."
                                        "\nRule 7: A player shall be delcared Champion when all of the oponent checker are captured or of the opponents remaining checkers movments are blocked"
                                        ,justify="left")
        rule.pack(padx=20, pady=20)
        
    def Yellow_Winner(self): #Window containing a congratulatory message for the player if they win.
        Yellow_Win = tkinter.Toplevel()
        Yellow_Win.title("Winner")
        win = tkinter.Label(Yellow_Win, text="CONGRATULATION, YOU DEFEATED THE ARTIFICAL INTELLIGENCE, HUMANITY IS SAVED!!!"
                                        "\nTo play again restart the game"
                                        ,justify="left")
        win.pack(padx=20, pady=20)
        
    def Yellow_Looser(self): #Window containing a message to notify play they have lost the game.
        Yellow_loose = tkinter.Toplevel()
        Yellow_loose.title("Winner")
        lose = tkinter.Label(Yellow_loose, text="NOoooo!!, ARTIFICAL INTELLIGENCE HAS WON, HUMANITY IS DOOMED!!!"
                                        "\nTo play again close this window and restat game"
                                        ,justify="left")
        lose.pack(padx=20, pady=20)
       
    def Interface(self):#GUI functions including lables, buttons the board and checkers
        
        self.parent.title("Welcome to Checkers!" )#Titel for the game window
        self.pack(fill=tkinter.BOTH, expand=1)

        self.canvas = tkinter.Canvas(self,bg="RoyalBlue1", width=x, height=y)# GUI window
        self.canvas.place(x=0,y=0)
        
        self.sidebar = tkinter.Frame(self, width=200, height=600, bg="blue2") #Side bar for tracking/controlling variables
        self.sidebar.place(x=600, y = 2)
        
        self.Difficulty_setting = tkinter.Label(self.sidebar, text="Agent Skill Level", bg = "blue2", fg = "white",font=("Arial", 10, "bold"))#Dificulty slide bar function to controll ai depth.
        self.Difficulty_setting.place(x=43, y=513) 
        self.Difficulty = tkinter.IntVar()
        self.Difficulty.set(2)  
        self.Difficulty_setting = tkinter.Scale(self.sidebar,
                                       from_=1,
                                       to=10,
                                       orient=tkinter.HORIZONTAL,
                                       variable=self.Difficulty,
                                       bg="blue2",
                                       fg="white",
                                       highlightthickness=0,
                                       troughcolor="gray",
                                       length=150)
        self.Difficulty_setting.place(x=30, y=530)
        
        self.rule_button = tkinter.Button(self, text="Rule Guide", command=self.Rule_Guide_window) #Rule button wiget
        self.rule_button.place(x=715,y=30) 
        
        self.Game_reset = tkinter.Button(self, text="Game Reset", command=self.Game_Reset)#Game reset button
        self.Game_reset.place(x=630,y=30) 
        
        self.yellow_graveyard_count = 0 #Initialize yellow grave yard count
        self.yellow_graveyard = tkinter.Canvas(self.sidebar, width=50, height=400, bg="blue4") # Gave yard wiget 
        self.yellow_graveyard.pack(pady=10)
        self.yellow_graveyard.place(x=40, y =85)
        self.yellow_lable = tkinter.Label(self.sidebar, text=f"Captured Yellow: {self.yellow_graveyard_count}", bg="blue2", fg="white") #label for graveyard displaying checker count.
        self.yellow_lable.place(x=10, y =60)
        
        self.ai_graveyard_count = 0 #Initialize ai grave yard count
        self.ai_graveyard = tkinter.Canvas(self.sidebar, width=50, height=400, bg="blue4")
        self.ai_graveyard.pack(pady=10)
        self.ai_graveyard.place(x=120, y =85)
        self.ai_lable = tkinter.Label(self.sidebar, text=f"Captured AI: {self.ai_graveyard_count}", bg="blue2", fg="white") #label for graveyard displaying checker count.
        self.ai_lable.place(x=115, y =60)
            
        self.drag_data = {"item": None, "x": 0, "y": 0} # Drag data dictionary to store vlues for the drag/drop function that the player will use to manipulate board state

        self.canvas.tag_bind("Y-oval", "<ButtonPress-1>", self.PickUp) # Binding player events to canvas for non king checkers
        self.canvas.tag_bind("Y-oval", "<B1-Motion>", self.Drag)
        self.canvas.tag_bind("Y-oval", "<ButtonRelease-1>", self.Drop)
        
        self.canvas.tag_bind("Y-king", "<ButtonPress-1>", self.PickUp) # Binding player events to canvas for non king checkers
        self.canvas.tag_bind("Y-king", "<B1-Motion>", self.Drag)
        self.canvas.tag_bind("Y-king", "<ButtonRelease-1>", self.Drop)
        
        SQA1 = self.canvas.create_rectangle(60, 60,120,120,outline="gold1", fill="gold1", tags= "gold" ) #Place colombs and rows for the tiles to be played on
        SQB1 = self.canvas.create_rectangle(60,120,120,180,outline="black", fill="black", tags= "black")
        SQC1 = self.canvas.create_rectangle(60,180,120,240,outline="gold1", fill="gold1", tags= "gold" )
        SQD1 = self.canvas.create_rectangle(60,240,120,300,outline="black", fill="black", tags= "black")
        SQE1 = self.canvas.create_rectangle(60,300,120,360,outline="gold1", fill="gold1", tags= "gold" )
        SQF1 = self.canvas.create_rectangle(60,360,120,420,outline="black", fill="black", tags= "black")
        SQG1 = self.canvas.create_rectangle(60,420,120,480,outline="gold1", fill="gold1", tags= "gold" )
        SQH1 = self.canvas.create_rectangle(60,480,120,540,outline="black", fill="black", tags= "black")
        
        SQA2 = self.canvas.create_rectangle(120, 60,180,120,outline="black", fill="black", tags= "gold" ) 
        SQB2 = self.canvas.create_rectangle(120,120,180,180,outline="gold1", fill="gold1", tags= "black")
        SQC2 = self.canvas.create_rectangle(120,180,180,240,outline="black", fill="black", tags= "gold" )
        SQD2 = self.canvas.create_rectangle(120,240,180,300,outline="gold1", fill="gold1", tags= "black")
        SQE2 = self.canvas.create_rectangle(120,300,180,360,outline="black", fill="black", tags= "gold" )
        SQF2 = self.canvas.create_rectangle(120,360,180,420,outline="gold1", fill="gold1", tags= "black")
        SQG2 = self.canvas.create_rectangle(120,420,180,480,outline="black", fill="black", tags= "gold" )
        SQH2 = self.canvas.create_rectangle(120,480,180,540,outline="gold1", fill="gold1", tags= "black")
        
        SQA3 = self.canvas.create_rectangle(180, 60,240,120,outline="gold1", fill="gold1", tags= "gold" )
        SQB3 = self.canvas.create_rectangle(180,120,240,180,outline="black", fill="black", tags= "black")
        SQC3 = self.canvas.create_rectangle(180,180,240,240,outline="gold1", fill="gold1", tags= "gold" )
        SQD3 = self.canvas.create_rectangle(180,240,240,300,outline="black", fill="black", tags= "black")
        SQE3 = self.canvas.create_rectangle(180,300,240,360,outline="gold1", fill="gold1", tags= "gold" )
        SQF3 = self.canvas.create_rectangle(180,360,240,420,outline="black", fill="black", tags= "black")
        SQG3 = self.canvas.create_rectangle(180,420,240,480,outline="gold1", fill="gold1", tags= "gold" )
        SQH3 = self.canvas.create_rectangle(180,480,240,540,outline="black", fill="black", tags= "black")
        
        SQA4 = self.canvas.create_rectangle(240, 60,300,120,outline="black", fill="black", tags= "gold" ) 
        SQB4 = self.canvas.create_rectangle(240,120,300,180,outline="gold1", fill="gold1", tags= "black")
        SQC4 = self.canvas.create_rectangle(240,180,300,240,outline="black", fill="black", tags= "gold" )
        SQD4 = self.canvas.create_rectangle(240,240,300,300,outline="gold1", fill="gold1", tags= "black")
        SQE4 = self.canvas.create_rectangle(240,300,300,360,outline="black", fill="black", tags= "gold" )
        SQF4 = self.canvas.create_rectangle(240,360,300,420,outline="gold1", fill="gold1", tags= "black")
        SQG4 = self.canvas.create_rectangle(240,420,300,480,outline="black", fill="black", tags= "gold" )
        SQH4 = self.canvas.create_rectangle(240,480,300,540,outline="gold1", fill="gold1", tags= "black")
        
        SQA5 = self.canvas.create_rectangle(300, 60,360,120,outline="gold1", fill="gold1", tags= "gold" )
        SQB5 = self.canvas.create_rectangle(300,120,360,180,outline="black", fill="black", tags= "black")
        SQC5 = self.canvas.create_rectangle(300,180,360,240,outline="gold1", fill="gold1", tags= "gold" )
        SQD5 = self.canvas.create_rectangle(300,240,360,300,outline="black", fill="black", tags= "black")
        SQE5 = self.canvas.create_rectangle(300,300,360,360,outline="gold1", fill="gold1", tags= "gold" )
        SQF5 = self.canvas.create_rectangle(300,360,360,420,outline="black", fill="black", tags= "black")
        SQG5 = self.canvas.create_rectangle(300,420,360,480,outline="gold1", fill="gold1", tags= "gold" )
        SQH5 = self.canvas.create_rectangle(300,480,360,540,outline="black", fill="black", tags= "black")
        
        SQA6 = self.canvas.create_rectangle(360, 60,420,120,outline="black", fill="black", tags= "gold" ) 
        SQB6 = self.canvas.create_rectangle(360,120,420,180,outline="gold1", fill="gold1", tags= "black")
        SQC6 = self.canvas.create_rectangle(360,180,420,240,outline="black", fill="black", tags= "gold" )
        SQD6 = self.canvas.create_rectangle(360,240,420,300,outline="gold1", fill="gold1", tags= "black")
        SQE6 = self.canvas.create_rectangle(360,300,420,360,outline="black", fill="black", tags= "gold" )
        SQF6 = self.canvas.create_rectangle(360,360,420,420,outline="gold1", fill="gold1", tags= "black")
        SQG6 = self.canvas.create_rectangle(360,420,420,480,outline="black", fill="black", tags= "gold" )
        SQH6 = self.canvas.create_rectangle(360,480,420,540,outline="gold1", fill="gold1", tags= "black")
        
        SQA7 = self.canvas.create_rectangle(420, 60,480,120,outline="gold1", fill="gold1", tags= "gold" )
        SQB7 = self.canvas.create_rectangle(420,120,480,180,outline="black", fill="black", tags= "black")
        SQC7 = self.canvas.create_rectangle(420,180,480,240,outline="gold1", fill="gold1", tags= "gold" )
        SQD7 = self.canvas.create_rectangle(420,240,480,300,outline="black", fill="black", tags= "black")
        SQE7 = self.canvas.create_rectangle(420,300,480,360,outline="gold1", fill="gold1", tags= "gold" )
        SQF7 = self.canvas.create_rectangle(420,360,480,420,outline="black", fill="black", tags= "black")
        SQG7 = self.canvas.create_rectangle(420,420,480,480,outline="gold1", fill="gold1", tags= "gold" )
        SQH7 = self.canvas.create_rectangle(420,480,480,540,outline="black", fill="black", tags= "black")
        
        SQA8 = self.canvas.create_rectangle(480, 60,540,120,outline="black", fill="black", tags= "gold" ) 
        SQB8 = self.canvas.create_rectangle(480,120,540,180,outline="gold1", fill="gold1", tags= "black")
        SQC8 = self.canvas.create_rectangle(480,180,540,240,outline="black", fill="black", tags= "gold" )
        SQD8 = self.canvas.create_rectangle(480,240,540,300,outline="gold1", fill="gold1", tags= "black")
        SQE8 = self.canvas.create_rectangle(480,300,540,360,outline="black", fill="black", tags= "gold" )
        SQF8 = self.canvas.create_rectangle(480,360,540,420,outline="gold1", fill="gold1", tags= "black")
        SQG8 = self.canvas.create_rectangle(480,420,540,480,outline="black", fill="black", tags= "gold" )
        SQH8 = self.canvas.create_rectangle(480,480,540,540,outline="gold1", fill="gold1", tags= "black")
        
        outline = self.canvas.create_rectangle(59, 59, 541, 541, outline = "black" )# visual additive for board aethetics
        self.pos_grid() # initializes the tile/grid positions 
        
        Y1  = self.canvas.create_oval(70 , 490, 110, 530, outline = "red", fill = "yellow", tag ="Y-oval" ) #place player 1 checkers
        Y2  = self.canvas.create_oval(190, 490, 230, 530, outline = "red", fill = "yellow", tag ="Y-oval" ) 
        Y3  = self.canvas.create_oval(310, 490, 350, 530, outline = "red", fill = "yellow", tag ="Y-oval" ) 
        Y4  = self.canvas.create_oval(430, 490, 470, 530, outline = "red", fill = "yellow", tag ="Y-oval" ) 
        
        Y5  = self.canvas.create_oval(130, 430, 170, 470, outline = "red" ,fill = "yellow" ,tag ="Y-oval" ) 
        Y6  = self.canvas.create_oval(250, 430, 290, 470, outline = "red" ,fill = "yellow" ,tag ="Y-oval" ) 
        Y7  = self.canvas.create_oval(370, 430, 410, 470, outline = "red" ,fill = "yellow" ,tag ="Y-oval" ) 
        Y8  = self.canvas.create_oval(490, 430, 530, 470, outline = "red" ,fill = "yellow" ,tag ="Y-oval" ) 

        Y9  = self.canvas.create_oval( 70,  370, 110, 410,outline = "red" ,fill = "yellow" ,tag ="Y-oval" ) 
        Y10 = self.canvas.create_oval( 190, 370, 230, 410,outline = "red" ,fill = "yellow" ,tag ="Y-oval" ) 
        Y11 = self.canvas.create_oval( 310, 370, 350, 410,outline = "red" ,fill = "yellow" ,tag ="Y-oval" ) 
        Y12 = self.canvas.create_oval( 430, 370, 470, 410,outline = "red" ,fill = "yellow" ,tag ="Y-oval" ) 
         
        R1  = self.canvas.create_oval( 490, 70, 530, 110,outline = "darkolivegreen1" ,fill = "brown" ,tag ="R-oval" ) #place AI checkers 
        R2  = self.canvas.create_oval( 370, 70, 410, 110,outline = "darkolivegreen1" ,fill = "brown" ,tag ="R-oval" ) 
        R3  = self.canvas.create_oval( 250, 70, 290, 110,outline = "darkolivegreen1" ,fill = "brown" ,tag ="R-oval" ) 
        R4  = self.canvas.create_oval( 130, 70, 170, 110,outline = "darkolivegreen1" ,fill = "brown" ,tag ="R-oval" ) 
        
        R5  = self.canvas.create_oval( 430, 130, 470, 170,outline = "darkolivegreen1" ,fill = "brown" ,tag ="R-oval" ) 
        R6  = self.canvas.create_oval( 310, 130, 350, 170,outline = "darkolivegreen1" ,fill = "brown" ,tag ="R-oval" ) 
        R7  = self.canvas.create_oval( 190, 130, 230, 170,outline = "darkolivegreen1" ,fill = "brown" ,tag ="R-oval" ) 
        R8  = self.canvas.create_oval(  70, 130, 110, 170,outline = "darkolivegreen1" ,fill = "brown" ,tag ="R-oval" ) 

        R9  = self.canvas.create_oval( 490, 190, 530, 230,outline = "darkolivegreen1" ,fill = "brown" ,tag ="R-oval" ) 
        R10 = self.canvas.create_oval( 370, 190, 410, 230,outline = "darkolivegreen1" ,fill = "brown" ,tag ="R-oval" ) 
        R11 = self.canvas.create_oval( 250, 190, 290, 230,outline = "darkolivegreen1" ,fill = "brown" ,tag ="R-oval" ) 
        R12 = self.canvas.create_oval( 130, 190, 170, 230,outline = "darkolivegreen1" ,fill = "brown" ,tag ="R-oval" ) 
        self.checker_pos = {} #initialize checkers so that they exist on the board
        
        #function to find and store all of the checkers center points (x,y) to use as a reference point later in the code 
        for piese_id in self.canvas.find_withtag("Y-oval") + self.canvas.find_withtag("R-oval") + self.canvas.find_withtag("Y-king") + self.canvas.find_withtag("R-king"): #
            coords = self.canvas.coords(piese_id) 
            coord_x = (coords[0] + coords[2]) //2
            coord_y = (coords[1] + coords[3]) //2
            self.checker_pos[piese_id] = (coord_x, coord_y)
            
    def get_counter_grid_pos(self): #function to retreave the grid position in terms of rows and colombs (row,col)
        self.check_grid_pos= {}
        self.checker_pos = {}
        for piese_id in self.canvas.find_withtag("Y-oval") + self.canvas.find_withtag("R-oval") + self.canvas.find_withtag("Y-king") + self.canvas.find_withtag("R-king"):
            coords = self.canvas.coords(piese_id)
            #convert piece id to x y coords
            center_x = (coords[0] + coords[2]) //2
            center_y = (coords[1] + coords[3]) //2
            self.checker_pos[piese_id] = (center_x, center_y)
            #convert xy coords to (row, col)
            for (row, col), (grid_x, grid_y) in self.grid.items():
                if (center_x, center_y) == (grid_x, grid_y):
                    self.check_grid_pos[piese_id] = (row, col)
                    break
        return self.checker_pos #return the row colomb position       
    
    def pos_grid(self): # function to determin if a psoition on the board is a void square that can not be moved to at any point ie (yellow squares)
        self.grid = {}
        self.not_pos = []
        squ_size = 60
        for row in range(8):
            for col in range(8):
                x = squ_size + col * squ_size 
                y = squ_size + row * squ_size 
                self.grid[(row, col)] = (x + squ_size //2, y + squ_size //2) 
                if (row + col) % 2 == 0:
                    self.not_pos.append(self.grid[(row, col)])
        #print(self.grid)
        #print(self.not_pos)
        return self.grid
    
    def State_rep(self): # Board state representation data set for the use in the board iteration/mutants
        bord_stat = [[None for r in range(8)] for c in range(8)]    
        self.get_counter_grid_pos()
        for piese_id, (row,col) in self.check_grid_pos.items():
            row = int(row)
            col = int(col)
            if not (0 <= row < 8 and 0 <= col < 8):
                continue 
            tag = self.canvas.gettags(piese_id)
            if "Y-oval" in tag:
                bord_stat[row][col] = 'YO'
            elif "Y-king" in tag:
                bord_stat[row][col] = 'YK'
            elif "R-oval" in tag:
                bord_stat[row][col] = 'RO'
            elif "R-king" in tag:
                bord_stat[row][col] = 'RK'
        return bord_stat
        #print(bord_stat)
    def new_board_iterations(self, board, start_pos, end_pos, tag): # function for the new board iterations 
        new_board = [row[:] for row in board]  

        start_row, start_col = start_pos #creates a new set of rows to represent the new board to populate
        end_row, end_col = end_pos
        new_board[end_row][end_col] = tag
        new_board[start_row][start_col] = None
        
        if abs(start_row - end_row) == 2: 
            mid_row = (start_row + end_row) // 2
            mid_col = (start_col + end_col) // 2
            new_board[mid_row][mid_col] = None

        if tag == 'RO' and end_row == 7:
            new_board[end_row][end_col] = 'RK'
        elif tag == 'YO' and end_row == 0:
            new_board[end_row][end_col] = 'YK'

        return new_board
    
    def Check_checker_move_take(self, piese_id): # function to check if there avaible moves and takes. 
        self.get_counter_grid_pos() 
        if piese_id not in self.check_grid_pos:
            return False
        row, col = self.check_grid_pos[piese_id]
        tag = self.canvas.gettags(piese_id)
        
        is_yellow = "Y" in tag
        is_king = "king" in tag
        #based of player colour, moves are set depending of piece type.
        if is_yellow: 
            en_tag = ("R-oval", "R-king")
            directs = [(-1, -1), (-1, 1)]
        else:
            en_tag = ("Y-oval", "Y-king")
            directs = [(1, -1), (1, 1)]
        if is_king: # if its a king add the reversal direction the sucsessors
            directs += [(-d[0], -d[1]) for d in directs]
        
        for dr, dc in directs: #check for valid non capture moves 
            new_row = row + dr
            new_col = col + dc
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                pos = self.grid[(new_row, new_col)]
                if pos not in self.checker_pos.values() and pos not in self.not_pos:
                    return True  # if there are valid non capture moves then return true 
                
        for d_id in self.checker_pos: # check for valid capture moves 
            if any(tag in self.canvas.gettags(d_id) for tag in en_tag):
                if d_id in self.check_grid_pos:
                        d_row, d_col = self.check_grid_pos[d_id]
                        rowbehind = d_row + (d_row - row)
                        colbehind = d_col + (d_col - col)
                            # Check bounds
                        if 0 <= rowbehind < 8 and 0 <= colbehind < 8: 
                            behind_pos = self.grid[(rowbehind, colbehind)]
                            if behind_pos not in self.checker_pos.values()  and behind_pos not in self.not_pos: 
                                return True    # if there are valid capture moves then return true 
        return False #if there are non return false  

    def get_suc(self, tag, board): # the sucsessor function that signifys all the posible moves a piese can take 
        successors = []
        directions = []

        # Set movement directions based on piece type
        if tag == 'RO':
            directions = [(1, -1), (1, 1)]
        elif tag == 'RK':
            directions = [(1, -1), (1, 1), (-1, -1), (-1, 1)]
        elif tag == 'YO':
            directions = [(-1, -1), (-1, 1)]
        elif tag == 'YK':
            directions = [(1, -1), (1, 1), (-1, -1), (-1, 1)]

        for row in range(8): #range checking logic and col row mapping
            for col in range(8):
                if board[row][col] == tag:
                    for dr, dc in directions:
                        new_row = row + dr
                        new_col = col + dc
                        if 0 <= new_row < 8 and 0 <= new_col < 8: # logic for normal moves for ai
                            if board[new_row][new_col] is None:
                                new_board = self.new_board_iterations(board, (row, col), (new_row, new_col), tag)
                                successors.append((new_board, ((row, col), (new_row, new_col))))
                        jump_row = row + 2 * dr # jump/capture logic for ai
                        jump_col = col + 2 * dc
                        mid_row = row + dr
                        mid_col = col + dc
                        if (0 <= jump_row < 8 and 0 <= jump_col < 8 and board[jump_row][jump_col] is None): #checks the capturing conditions and adds sucsessor to list
                            mid_piece = board[mid_row][mid_col]
                            if tag.startswith('R') and mid_piece is not None and mid_piece.startswith('Y'):
                                new_board = self.new_board_iterations(board, (row, col), (jump_row, jump_col), tag)
                                successors.append((new_board, ((row, col), (jump_row, jump_col))))
                            elif tag.startswith('Y') and mid_piece is not None and mid_piece.startswith('R'):
                                new_board = self.new_board_iterations(board, (row, col), (jump_row, jump_col), tag)
                                successors.append((new_board, ((row, col), (jump_row, jump_col))))

        return successors
    
    def Move_eval(self, start_pos, end_pos, can_cap, is_jump=False, is_king=False):
        value = 0 
        row, col = end_pos
        start_row, start_col = start_pos
        
        # 1. Capture evaluation (but not overwhelming)
        if can_cap and is_jump:
            mid_row = (start_row + row) // 2
            mid_col = (start_col + col) // 2
            mid_pos = (mid_row, mid_col)
            mid_grid = self.grid.get(mid_pos)
            
            for piece_id in self.checker_pos:
                if self.checker_pos[piece_id] == mid_grid:
                    tags = self.canvas.gettags(piece_id)
                    if "Y-oval" in tags:
                        value += Take_peice  # +30 for regular piece
                    elif "Y-king" in tags:
                        value += Take_peice * 2  # +60 for king (more valuable)
                    break
        
        # 2. King promotion (fix the row logic)
        if row == 7:  # Red reaches bottom row
            value += King_maker  # +20
        
        # 3. Center control (encourage central positioning)
        if 2 <= row <= 5 and 2 <= col <= 5:
            value += Core_dominance  # +5
        
        # 4. Forward progress for regular pieces
        if start_row > row:  # Moving forward
            value += 2  # Small bonus for advancing
        
        # 5. Edge penalty (discourage edge play)
        if col == 0 or col == 7:
            value -= 3  # Slight penalty for edge positions
        
        # 6. Simple threat evaluation
        # Check if this move puts us in danger
        for piece_id in self.checker_pos:
            if "Y-oval" in self.canvas.gettags(piece_id) or "Y-king" in self.canvas.gettags(piece_id):
                if piece_id in self.check_grid_pos:
                    p_row, p_col = self.check_grid_pos[piece_id]
                    # Check if yellow piece can capture us after this move
                    if abs(p_row - row) == 1 and abs(p_col - col) == 1:
                        # Check if square behind us is free
                        behind_row = row + (row - p_row)
                        behind_col = col + (col - p_col)
                        if 0 <= behind_row < 8 and 0 <= behind_col < 8:
                            behind_pos = self.grid.get((behind_row, behind_col))
                            if behind_pos not in self.checker_pos.values():
                                value += In_danger  # -10 for being in danger
        
        return value

    def minimax(self, board, move, depth, alpha, beta, maximizing_player): # minimax algorithem with alpha beta pruning determins the optimal move based on the branching of a decision tree of posible moves 
        
        start_pos, end_pos = move
        row, col = end_pos
        is_jump = abs(row - start_pos[0]) == 2
        value = self.Move_eval(start_pos, end_pos, can_cap=is_jump, is_jump=is_jump)
        #print(f"Depth: {depth}, Player: {'Max' if maximizing_player else 'Min'}, Value: {value}")
        if depth == 0:
            return value
        if maximizing_player:
            max_eval = -float("inf")
            for tag in ['RO', 'RK']:
                successors = self.get_suc(tag, board)
                for new_board, new_move in successors:
                    eval_val = self.minimax(new_board, new_move, depth - 1, alpha, beta, False)
                    max_eval = max(max_eval, eval_val)
                    alpha = max(alpha, eval_val)
                    if beta <= alpha:
                        break
            return max_eval
        else:
            min_eval = float("inf")
            for tag in ['YO', 'YK']:
                successors = self.get_suc(tag, board)
                for new_board, new_move in successors:
                    eval_val = self.minimax(new_board, new_move, depth - 1, alpha, beta, True)
                    min_eval = min(min_eval, eval_val)
                    beta = min(beta, eval_val)
                    if beta <= alpha:
                        break
            return min_eval

    def has_more_captures(self, piece_id):
        """Check if a piece has more captures available"""
        if piece_id not in self.check_grid_pos:
            return False
            
        row, col = self.check_grid_pos[piece_id]
        tags = self.canvas.gettags(piece_id)
        
        # Define movement directions based on piece type
        if "Y-oval" in tags:
            directions = [(-1, -1), (-1, 1)]  # Yellow moves up
        elif "Y-king" in tags:
            directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # Kings move all directions
        elif "R-oval" in tags:
            directions = [(1, -1), (1, 1)]  # Red moves down
        elif "R-king" in tags:
            directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # Kings move all directions
        else:
            return False
        
        # Check each direction for possible captures
        for dr, dc in directions:
            enemy_row = row + dr
            enemy_col = col + dc
            landing_row = row + 2 * dr
            landing_col = col + 2 * dc
            
            # Check bounds
            if not (0 <= enemy_row < 8 and 0 <= enemy_col < 8 and 
                    0 <= landing_row < 8 and 0 <= landing_col < 8):
                continue
                
            enemy_pos = self.grid[(enemy_row, enemy_col)]
            landing_pos = self.grid[(landing_row, landing_col)]
            
            # Check if there's an enemy piece to capture
            enemy_piece = None
            for pid, pos in self.checker_pos.items():
                if pos == enemy_pos:
                    enemy_tags = self.canvas.gettags(pid)
                    if "R-oval" in tags or "R-king" in tags:  # AI piece checking for yellow enemies
                        if "Y-oval" in enemy_tags or "Y-king" in enemy_tags:
                            enemy_piece = pid
                            break
                    elif "Y-oval" in tags or "Y-king" in tags:  # Yellow piece checking for red enemies
                        if "R-oval" in enemy_tags or "R-king" in enemy_tags:
                            enemy_piece = pid
                            break
            
            # Check if landing square is free
            if (enemy_piece and 
                landing_pos not in self.checker_pos.values() and 
                landing_pos not in self.not_pos):
                return True
                
        return False

    def ai_moving(self, continue_piece=None):
        """Handle AI movements with support for multiple captures"""
        
        board = self.State_rep()
        for row in board:
            print(row)
        
        best_val = float('-inf')
        best_move = None
        best_tag = None
        
        # If continuing captures with specific piece
        if continue_piece is not None:
            piece_tags = self.canvas.gettags(continue_piece)
            if "R-oval" in piece_tags:
                tag = 'RO'
            elif "R-king" in piece_tags:
                tag = 'RK'
            else:
                return
                
            # Get only capture moves for this specific piece
            if continue_piece in self.check_grid_pos:
                piece_row, piece_col = self.check_grid_pos[continue_piece]
                successors = []
                
                # Get directions based on piece type
                if tag == 'RO':
                    directions = [(1, -1), (1, 1)]
                else:  # RK
                    directions = [(1, -1), (1, 1), (-1, -1), (-1, 1)]
                
                # Only look for capture moves
                for dr, dc in directions:
                    jump_row = piece_row + 2 * dr
                    jump_col = piece_col + 2 * dc
                    mid_row = piece_row + dr
                    mid_col = piece_col + dc
                    
                    if (0 <= jump_row < 8 and 0 <= jump_col < 8 and 
                        board[jump_row][jump_col] is None):
                        mid_piece = board[mid_row][mid_col]
                        if mid_piece is not None and mid_piece.startswith('Y'):
                            new_board = self.new_board_iterations(board, (piece_row, piece_col), 
                                                                (jump_row, jump_col), tag)
                            successors.append((new_board, ((piece_row, piece_col), (jump_row, jump_col))))
                
                # Evaluate capture moves
                for new_board, move in successors:
                    eval_val = self.minimax(new_board, move, self.Difficulty.get(), -float('inf'), float('inf'), False)
                    if eval_val > best_val:
                        best_val = eval_val
                        best_move = move
                        best_tag = tag
        
        else:
            # Normal AI move selection
            for tag in ['RO', 'RK']:
                successors = self.get_suc(tag, board)
                print(f"{tag} has {len(successors)} successors")
                for new_board, move in successors:
                    eval_val = self.minimax(new_board, move, self.Difficulty.get(), -float('inf'), float('inf'), False)
                    if eval_val > best_val:
                        best_val = eval_val
                        best_move = move
                        best_tag = tag
        
        if best_move:
            start_pos, end_pos = best_move
            self.get_counter_grid_pos()
            piece_id = None
            
            # Find the piece to move
            if continue_piece is not None:
                piece_id = continue_piece
            else:
                for peice_id, (row, col) in self.check_grid_pos.items():
                    tags = self.canvas.gettags(peice_id)
                    if (row, col) == start_pos and ((best_tag == 'RO' and 'R-oval' in tags) or 
                                                  (best_tag == 'RK' and 'R-king' in tags)):
                        piece_id = peice_id
                        break
            
            if piece_id is None:
                return 
        
            # Execute the move
            grid_target = self.grid[end_pos]
            self.canvas.coords(piece_id, grid_target[0]-20, grid_target[1]-20, 
                              grid_target[0]+20, grid_target[1]+20)
            self.checker_pos[piece_id] = grid_target
            self.update_idletasks()
            self.canvas.update()
            
            # Handle captures
            if abs(start_pos[0] - end_pos[0]) == 2:
                mid_row = (start_pos[0] + end_pos[0]) // 2
                mid_col = (start_pos[1] + end_pos[1]) // 2
                mid_grid = self.grid[(mid_row, mid_col)]
                
                for peice_id, (x, y) in self.checker_pos.items():
                    if (x, y) == mid_grid and ("Y-oval" in self.canvas.gettags(peice_id) or 
                                             "Y-king" in self.canvas.gettags(peice_id)):
                        # Handle regicide
                        if ("Y-king" in self.canvas.gettags(peice_id) and 
                            "R-oval" in self.canvas.gettags(piece_id)):
                            self.canvas.itemconfig(piece_id, fill="OrangeRed2")
                            self.canvas.dtag(piece_id, "R-oval")
                            self.canvas.addtag_withtag("R-king", piece_id)
                            print("AI committed regicide! Red piece has become king.")
                        
                        self.move_to_graveyard(peice_id)
                        self.yellow_graveyard_count += 1
                        self.yellow_lable.config(text=f"Captured Yellow: {self.yellow_graveyard_count}")
                        del self.checker_pos[peice_id]
                        if peice_id in self.check_grid_pos:
                            del self.check_grid_pos[peice_id]
                        break

            self.get_counter_grid_pos()
            self.Kinging(piece_id)
            
            # Check for additional captures
            if abs(start_pos[0] - end_pos[0]) == 2 and self.has_more_captures(piece_id):
                print("AI has multiple capture! Continuing with same piece.")
                self.update()
                time.sleep(0.75)
                self.ai_moving(continue_piece=piece_id)  # Recursive call
            else:
                # No more captures - switch turns
                self.turn = "yellow"
                print(self.turn, 'to move.')
        else:
            # No valid moves - shouldn't happen
            self.turn = "yellow"
            print("AI has no valid moves.")
        
    def Win_Check_checker(self, Yellow_Winner, Yellow_Looser): # function to check wether there is a winning game state present in the board. 
        self.get_counter_grid_pos()
        yellow_remeaining = self.canvas.find_withtag("Y-oval") + self.canvas.find_withtag("Y-king")
        ai_remaining = self.canvas.find_withtag("R-oval") + self.canvas.find_withtag("R-king")
        yellow_move = len(yellow_remeaining)
        ai_move = len(ai_remaining)
        yellow_move = any(self.Check_checker_move_take(pieceid) for pieceid in yellow_remeaining)
        ai_move = any(self.Check_checker_move_take(pieceid) for pieceid in ai_remaining)
        if len(yellow_remeaining) == 0 or yellow_move == False:
            Yellow_Looser() 
        if len(ai_remaining) == 0 or ai_move == False:
            Yellow_Winner()
    
    def Kinging(self, piese_id): # a kinging function baced on the condition that a peice reaches the other side of the board or commis reggiside 
        if "R-oval" in self.canvas.gettags(piese_id):
            self.get_counter_grid_pos()
            if piese_id in self.check_grid_pos:
                row, col = self.check_grid_pos[piese_id]
                if row == 7:  # Reached back row for red (bottom of board)
                    self.canvas.itemconfig(piese_id, fill="OrangeRed2")
                    self.canvas.dtag(piese_id, "R-oval")
                    self.canvas.addtag_withtag("R-king", piese_id)
                    print("Red piece kinged!") 
        elif "Y-oval" in self.canvas.gettags(piese_id):
            self.get_counter_grid_pos()
            if piese_id in self.check_grid_pos:
                    row, col = self.check_grid_pos[piese_id]
                    if row == 0:  # Reached back row for red (bottom of board)
                        self.canvas.itemconfig(piese_id, fill="darkgoldenrod1")
                        self.canvas.dtag(piese_id, "Y-oval")
                        self.canvas.addtag_withtag("Y-king", piese_id)
                        print( "Yellow Checker Kinged!") 
                    
    def move_to_graveyard(self, piese_id): # function to move a checker to the grave yard if it is captured 
        tag = self.canvas.gettags(piese_id)
        if "R-oval" in tag or "R-king" in tag: #loop for graveyarding in the checker is an ai checker
            grid_x = 25
            grid_y = 25 + self.ai_graveyard_count * 4
            canvas = self.ai_graveyard
            

        elif "Y-oval" in tag or "Y-king" in tag: #loop for graveyarding in the checker is an yellow checker
                grid_x = 25
                grid_y = 25 + self.yellow_graveyard_count* 5
                canvas = self.yellow_graveyard
        else:
            return # ensures, absolutly, that a grid square isnt graveyarded  
        coords = (grid_x -15, grid_y -15, grid_x +15, grid_y +15) # Get oval color
        color = self.canvas.itemcget(piese_id, "fill")
        outline = self.canvas.itemcget(piese_id, "outline")
        canvas.create_oval(*coords, fill=color, outline=outline) #places the checker on the graveyard wiget
        self.canvas.delete(piese_id) 
        
    def PickUp(self, event): #pick up function as part of a drag an drop mechanisum using wiget coordinates
        piese_id = self.canvas.find_closest(event.x, event.y)[0]
        ply = self.canvas.gettags(piese_id)
        
        if (self.turn == "yellow" and ("Y-oval" in ply or "Y-king" in ply)):

        # Save piece to drag_data
            for key in ["Y-oval", "Y-king"]:
                if key in ply:
                    self.drag_data[key] = piese_id
                    self.drag_data["Y-oval"] = piese_id
                    self.drag_data["x"] = event.x
                    self.drag_data["y"] = event.y
                    self.drag_data["start_coords"] = self.canvas.coords(piese_id)
                    self.get_counter_grid_pos()
                    if piese_id in self.check_grid_pos:
                        self.drag_data["start_grid"] = self.check_grid_pos[piese_id]
    
    def Drag(self, event):# drag checker function as part of a drag an drop mechanisum using wiget coordinates
        piese_id = self.drag_data.get("Y-oval") or self.drag_data.get("Y-king") 
        if not piese_id:
            return  # Nothing to drag
        delta_x = event.x - self.drag_data["x"]
        delta_y = event.y - self.drag_data["y"]
        # Move the item by the calculated distance
        self.canvas.move(piese_id, delta_x, delta_y)
    # Update the coordinates of the item
        self.drag_data["x"] = event.x
        self.drag_data["y"] = event.y
        
    def Drop(self, event): #drop function as part of a drag an drop mechanisum using wiget coordinates
        piese_id = self.drag_data.get("Y-oval") or self.drag_data.get("R-oval") or self.drag_data.get("Y-king") or self.drag_data.get("R-king")
        if not piese_id:
            return 
        clos_pos = None
        min_distance = float('inf')
        for (row, col), (grid_x, grid_y) in self.grid.items():
            dist = ((event.x - grid_x) **2 + (event.y - grid_y) **2) **0.5
            if dist < min_distance:
                min_distance = dist
                clos_pos = (grid_x, grid_y)
                new_grid = (row,col)
                      
        start_grid = self.drag_data.get("start_grid") # function to prevent lateral movments 
        if "Y-oval" in self.canvas.gettags(piese_id) or "Y-king" in self.canvas.gettags(piese_id):
            if start_grid:
                drow = abs(new_grid[0] - start_grid[0])
                dcol = abs(new_grid[1] - start_grid[1])
                if drow > 1 or dcol > 1: 
                    start_coords = self.drag_data.get("start_coords")
                    self.canvas.coords(piese_id, *start_coords)
                    print("Invalid move: yellow pieces can't move sideways.")
                    self.drag_data = {"Y-oval": None,"Y-king":None, "R-oval": None, "R-king":None, "x": 0, "y": 0}
                    self.Win_Check_checker(Yellow_Winner=self.Yellow_Winner, Yellow_Looser=self.Yellow_Looser)
                    return    
                  
        start_grid = self.drag_data.get("start_grid")# function to prevent backwards movments for non king checkers 
        if "Y-oval" in self.canvas.gettags(piese_id):
            if start_grid and new_grid[0] > start_grid[0]:  
                start_coords = self.drag_data.get("start_coords")
                self.canvas.coords(piese_id, *start_coords)
                print("Invalid move: yellow pieces can't move backwards.")
                self.drag_data = {"Y-oval": None, "R-oval": None, "x": 0, "y": 0}
                self.Win_Check_checker(Yellow_Winner=self.Yellow_Winner, Yellow_Looser=self.Yellow_Looser)
                return  
        
        tag = self.canvas.gettags(piese_id)  # function to restrict movment of more that one squar at a time if peice is a non king checker 
        start_grid = self.drag_data.get("start_grid")
        if "Y-oval" in tag or "Y-king" in tag:
            if start_grid and abs(new_grid[0] - start_grid[0]) > 1 : 
                start_coords = self.drag_data.get("start_coords")
                self.canvas.coords(piese_id, *start_coords)
                print("Invalid move: Pieces can't move more that one square at a time.")
                self.drag_data = {"Y-oval": None, "R-oval": None, "x": 0, "y": 0}  
                self.Win_Check_checker(Yellow_Winner=self.Yellow_Winner, Yellow_Looser=self.Yellow_Looser)
                return
        
        #function to prevent illigal moves and moves to occupied squares 
        piese_id = self.drag_data.get("Y-oval") or self.drag_data.get("R-oval") or self.drag_data.get("Y-king") or self.drag_data.get("R-king")
        self.canvas.coords(piese_id, clos_pos[0]-20, clos_pos[1]-20, clos_pos[0]+20, clos_pos[1]+20)
        occupied = clos_pos in self.checker_pos.values()
        illegal = clos_pos in self.not_pos    
        if occupied or illegal: #conditional for illigal move
            if "Y-oval" in tag or "Y-king" in tag:
                start_coords = self.drag_data.get("start_coords")
                if start_coords:
                    self.canvas.coords(piese_id, *start_coords)
                print("Invalid move:", "occupied position" if occupied else "illegal placed checker!!!")
                self.Win_Check_checker(Yellow_Winner=self.Yellow_Winner, Yellow_Looser=self.Yellow_Looser)
            capture_made = False
            if "Y-oval" in tag or "Y-king" in tag: #start of the capture logic
                for r_piese_id, (rx, ry) in self.checker_pos.items():
                    if "R-oval" in self.canvas.gettags(r_piese_id) or "R-king" in self.canvas.gettags(r_piese_id):
                        if abs(rx - clos_pos[0]) <= 5 and abs(ry - clos_pos[1]) <= 5:
                            self.get_counter_grid_pos()
                            if r_piese_id in self.check_grid_pos and piese_id in self.check_grid_pos:
                                y_row, y_col = self.check_grid_pos[piese_id]
                                r_row, r_col = self.check_grid_pos[r_piese_id]
                                rowbehind = r_row + (r_row - y_row)
                                colbehind = r_col + (r_col - y_col)
                                if 0 <= rowbehind < 8 and 0 <= colbehind < 8:
                                    behind_pos = self.grid[(rowbehind, colbehind)]
                                    if behind_pos not in self.checker_pos.values() and behind_pos not in self.not_pos:
                                        # Execute the capture
                                        r_tags = self.canvas.gettags(r_piese_id)
                                        p_tags = self.canvas.gettags(piese_id)
                                        if "R-king" in r_tags and "Y-oval" in p_tags:
                                            self.canvas.itemconfig(piese_id, fill="darkgoldenrod1")
                                            self.canvas.dtag(piese_id, "Y-oval")
                                            self.canvas.addtag_withtag("Y-king", piese_id)
                                            print("Regicide! Yellow piece has become king.")
                                        
                                        self.move_to_graveyard(r_piese_id)
                                        self.ai_graveyard_count += 1
                                        self.ai_lable.config(text=f"Captured AI: {self.ai_graveyard_count}")
                                        del self.checker_pos[r_piese_id]
                                        if r_piese_id in self.check_grid_pos:
                                            del self.check_grid_pos[r_piese_id]
                                        
                                        self.canvas.coords(piese_id, behind_pos[0]-20, behind_pos[1]-20, 
                                                        behind_pos[0]+20, behind_pos[1]+20)
                                        self.checker_pos[piese_id] = behind_pos
                                        self.get_counter_grid_pos()
                                        self.Kinging(piese_id)
                                        
                                        # Check for additional captures
                                        if self.has_more_captures(piese_id):
                                            print("Multiple capture available! Continue with same piece.")
                                            capture_made = True
                                            # DON'T switch turns - stay with yellow
                                            self.drag_data = {"Y-oval": None,"Y-king": None,"R-oval": None,"R-king": None, "x": 0, "y": 0}
                                            self.Win_Check_checker(Yellow_Winner=self.Yellow_Winner, Yellow_Looser=self.Yellow_Looser)
                                            return
                                        else:
                                            # No more captures - switch turns
                                            capture_made = True
                                            self.turn = "red"
                                            self.update()
                                            time.sleep(0.75)
                                            self.ai_moving()
                                            print("Captured Red piece!")
                                            self.drag_data = {"Y-oval": None,"Y-king": None,"R-oval": None,"R-king": None, "x": 0, "y": 0}
                                            self.Win_Check_checker(Yellow_Winner=self.Yellow_Winner, Yellow_Looser=self.Yellow_Looser)
                                            return
        
        else: # function to snap to grid and update position
            self.checker_pos[piese_id] = clos_pos
            # Change turn
            if clos_pos != start_grid:
                self.turn = "red" if self.turn == "yellow" else "yellow"       
            print(self.turn,'to move.')
            self.Win_Check_checker(Yellow_Winner=self.Yellow_Winner, Yellow_Looser=self.Yellow_Looser)
        self.Kinging(piese_id) #check for any kinging conditions after drop
        # Reset drag data
        self.drag_data = {"Y-oval": None, "R-oval": None,"Y-king": None, "R-king": None, "x": 0, "y": 0}
        self.Win_Check_checker(Yellow_Winner=self.Yellow_Winner, Yellow_Looser=self.Yellow_Looser) # check for winning states 
        self.update ()#finalize any update on the board 
        time.sleep(.750)
        if self.turn == "red":   
            self.ai_moving()
        
if __name__ == "__main__": # initiates the game
    root = tkinter.Tk()
    app = CheckersBoard(root)
    root.geometry("800x600+500+200")
    root.mainloop()