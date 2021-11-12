import random
from tkinter import *
import time
from PIL import Image,ImageTk

class Player():
    def __init__(self):

        self.position = [-50, 550];
        self.block = 0;
        self.player_name = "Player";
    

class Dice():
    def roll():
        dice = random.randrange(1, 7, 1);
        return dice;
    


class Snakes_Ladders():
    def __init__(self):
        
        # meet snakes, move from top to bottom
        self.snakes = {25: 5, 34: 1, 47: 19, 65: 52, 
                  87: 57, 91: 61, 99: 69};
    
        # meet ladders, move from bottom to top
        self.ladders = {3: 51, 6: 27, 20: 70, 36: 55, 
                   63: 95, 68: 98};
    
    def jump(self,current_block):
        
        # a snake or ladder?
        self.meet_type = 0;
        
        if current_block in self.snakes:
            final_block = self.snakes.get(current_block);
            self.meet_type = 1;

        elif current_block in self.ladders:
            final_block = self.ladders.get(current_block);
            self.meet_type = 2;

        else:
            final_block = current_block;
            
        return final_block, self.meet_type;



class GUI():
    def __init__(self, root, img):

        # Create a game board
        self.color = ["#0FF", "#F00", "#0F0", "#F0F"];
        self.canvas = Canvas(root, width = 900, height = 600, bg = "white");
        self.canvas.grid(padx = 0, pady = 0);
        self.canvas.create_image(300, 300, anchor = CENTER, image = img);

        # the number of players
        self.num_player = "Player";
        # a list to save player
        self.player_list = [];
        # count rolling times
        self.i = 0;
        # a list to save counter
        self.counter = [];
        # player's turn
        self.turn = 0;
        self.computer_player = 0;
        # play another game?
        self.replay = 0;
        
        # the list to save players' names
        self.entry_list = [];
        self.labelText = [];
        
        # a label to indicate snake or ladder
        self.meet = StringVar();
        self.SL = Label(self.canvas, textvariable = self.meet, bg = "white",font = ('calibri',(12)));
        
        
        # Choose the number of players
        OPTIONS = ["Player", "1", "2", "3", "4"];
        variable = StringVar();
        variable.set(OPTIONS[0]);
        
        self.op = OptionMenu(self.canvas, variable, *OPTIONS, command = self.choose_num);
        self.op.pack();
        self.op.place(x = 725, y = 250);
        self.op.config(font = ('calibri',(12)), bg = 'white', width = 5);
        
        
        # input names
        self.input = Button(self.canvas, text = "Let's begin!", background = 'white', 
                            command = self.input_name, font = ("Helvetica",(11)));
        self.input.pack();
        self.input.place(x = 725, y = 450);
        
    def choose_num(self, value):
        self.num_player = value;

    def input_name(self):
        
        # if they play games agian, everything has to be initialized
        if (self.replay != 0):
            
            self.label_2.destroy();
            for i in range(self.replay):
                self.canvas.delete(self.counter[i]);
                self.canvas.update();

            self.counter = [];
            self.player_list = [];
            self.i = 0;
            self.turn = 0;
            self.computer_player = 0;
            self.num_player = self.replay;
            
            for i in range(self.num_player):
                self.entry_list[i][1].destroy();
            
            self.entry_list = [];
            self.labelText = [];
            
            self.op.place(x = 725, y = 250);
            self.replay = 0;
            
        # if it is the first time to play
        else:
            
            # choose the number of player
            if( self.num_player == "Player"):
                pass;
            
            else:
                # hide this button
                self.op.place(x = -740, y = 225);
                
                # one player, play with computer
                if(self.num_player == "1"):
                    self.computer_player = 1;
                    self.num_player = 2;
                else:
                    self.num_player = int(self.num_player);
                
                for i in range(self.num_player):
                    
                    # a box to input players' names
                    self.name_1 = Entry(self.canvas);
                    # the list to save players' names
                    self.labelText.append(StringVar());
                    # the label to show players' names
                    self.label_1 = Label(self.canvas, textvariable = self.labelText[i], 
                                         bg = self.color[i],font = ('calibri',(12)));
                        
                    
                    if(self.computer_player == 1 and i == 1):
                        self.labelText[i].set('(Computer)');
                    else:
                        self.labelText[i].set('(Player %s)'%(i + 1));
                    
                    # save the boxes and labels in a list
                    self.entry_list.append([self.name_1,self.label_1]);
                    
                    # display
                    self.entry_list[i][0].pack();
                    self.entry_list[i][0].place(x = 700, y = 250 + i*30);
                        
                    self.entry_list[i][1].pack()
                    self.entry_list[i][1].place(x = 625, y = 250 + i*30);
            
                # hide this button
                self.input.place(x = -770, y = -400);
                
                # a button to get names inputted
                self.name = Button(self.canvas, text = "Submit name", background = 'white', 
                                  command = self.get_name, font = ("Helvetica",(12)));
                self.name.place(x = 725, y = 450);


    def get_name(self):
    
        for i in range(self.num_player):
            # save names
            self.labelText[i].set('(Player %s)  '%(i+1) + self.entry_list[i][0].get());
            
            if(self.computer_player == 1 and i == 1 ):
                self.labelText[i].set('(Computer)  ' + self.entry_list[i][0].get());
            
            # destroy the input box
            self.entry_list[i][0].destroy();

        # hide this button
        self.name.place(x = -700, y = 500);
        
        # button to start this game
        self.start = Button(self.canvas, text="Let's play!", background ='white', 
                            command = self.startGame, font = ("Helvetica",(11)));
        self.start.pack();
        self.start.place(x = 725, y = 450);
        
    
    def startGame(self):
        
        # show a dice on board
        self.canvas.create_rectangle(825, 150, 750, 75, fill = 'white', outline = 'black');
        self.canvas.pack(fill = BOTH, expand = 1);
        # Button to roll dice and move counters
        self.diceRoll = Button(self.canvas, text = "Roll Dice",background = 'white',
                                       command = self.gamePlay, font = ("Helvetica",11));
    
        self.diceRoll.place(x = 750, y = 175);
        
        self.create_counter();
        # hide this button
        self.start.place(x = -100, y = -100);

    def create_counter(self):
        
        # show it is whose turn to roll dice
        self.turn_str = StringVar();
        self.label_2 = Label(self.canvas, textvariable = self.turn_str, 
                             bg = "white",font = ('calibri',(12)))
        self.turn_str.set(self.labelText[(self.i) % self.num_player].get() + "'s turn");
        self.label_2.pack();
        self.label_2.place(x = 625, y = 225);

        
        for i in range(int(self.num_player)):
            # create players
            self.player_list.append(Player());
            turn = self.turn;
            # create counters
            self.counter.append(self.canvas.create_oval(self.player_list[turn].position[0] - 10, 
                                                        self.player_list[turn].position[1] - 10, 
                                                        self.player_list[turn].position[0] + 10, 
                                                        self.player_list[turn].position[1] + 10,
                                                        fill = self.color[turn], outline = "black"));
    
    
    # get dice value and move counters on board
    def diceMove(self, block):
        
        # roll dice
        move = Dice.roll();
        
        # show dice value
        dice_value = Label(self.canvas, text = str(move),
                           background = 'white', font = ("calibri", 35));
        dice_value.pack();
        dice_value.place(x = 775, y = 80);

        turn = self.turn;
        
        # unseen label when there is no snake or ladder
        self.SL.destroy();
        
        if(move + self.player_list[turn].block > 100):
            move = 0;
        
        if(move > 0):
            for i in range(move, 0, -1):
                # block change
                self.player_list[turn].block = self.player_list[turn].block + 1;
                
                self.player_list[turn].position =  self.block_to_position(self.player_list[turn].block, turn);
                # counter change
                self.canvas.delete(self.counter[turn]);
                self.counter[turn] = self.canvas.create_oval(self.player_list[turn].position[0] - 10, 
                            self.player_list[turn].position[1] - 10, 
                            self.player_list[turn].position[0] + 10, 
                            self.player_list[turn].position[1] + 10,
                            fill = self.color[turn], outline = "black");
                self.canvas.update();
                time.sleep(0.3);
                
            # meet a snake or ladder?
            meetSL = 0;
            self.player_list[turn].block, meetSL = Snakes_Ladders().jump(self.player_list[turn].block);

            if(meetSL != 0):
                # indicate snake or ladder
                self.meet = StringVar();
                self.SL = Label(self.canvas, textvariable = self.meet, bg = "white",font = ('calibri',(14)));
                if(meetSL == 1):
                    self.meet.set("Snake!!!");
                    self.SL.pack();
                    self.SL.place(x = 650, y = 175);
                else:
                    self.meet.set("Ladder!!!");
                    self.SL.pack();
                    self.SL.place(x = 650, y = 175);
                    

            self.canvas.delete(self.counter[turn]);
            
            self.player_list[turn].position =  self.block_to_position(self.player_list[turn].block, turn);
            
            self.counter[turn] = self.canvas.create_oval(self.player_list[turn].position[0] - 10, 
                        self.player_list[turn].position[1] - 10, 
                        self.player_list[turn].position[0] + 10, 
                        self.player_list[turn].position[1] + 10,
                        fill = self.color[turn], outline = "black");
            self.canvas.update();
            time.sleep(0.3);


    # convert to specific position on board
    def block_to_position(self, block, turn):
        
        # gap between counters
        gap = 20;
        block_width = 60;
        gap_x = gap + gap * (turn >= 2);
        gap_y = gap + (turn % 2)*gap;
        x = gap_x + ( (block - 1) % 10) * block_width;
        y = gap_y + (9 - int((block - 1) / 10) ) * block_width;
        
        
        if (block == 0) :
            x = gap_x + ( -1) * block_width;

        return [x, y];
    

    def gamePlay(self):
        
        # hide this button
        self.diceRoll.place(x = -770, y = -165);
        # get turn
        turn = self.i % self.num_player;
        self.i += 1;
        self.turn = turn;
        
        
        self.diceMove(self.player_list[turn].block);
        
        if (self.computer_player == 1 and self.player_list[turn].block < 100):
            
            turn = self.i % self.num_player;
            self.i += 1;
            self.turn = turn;
            
            time.sleep(1);
            self.turn_str.set(self.labelText[turn].get() + "'s turn");
            self.diceMove(self.player_list[turn].block);

            
        self.turn_str.set(self.labelText[self.i % self.num_player].get() + "'s turn");

        
        self.diceRoll.place(x = 750, y = 175);
        
        # someone wins
        if(self.player_list[turn].block >= 100 ):
            
            # hide button
            self.diceRoll.place(x = -30, y = -30);
            
            
            
            self.turn_str.set(self.labelText[turn].get() + " Won! Play again or qiut?");
            
            # hide this button
            self.diceRoll.place(x = -770, y = -165);
            
            # wanna play again?
            self.replay = self.num_player;
            self.input.place(x = 725, y = 450);
            



from PIL import Image,ImageTk
def main():
    root = Tk();
    root.title("Snakes and Ladders");
    root.geometry("900x600");
    img1 = Image.open('Game_image.jpg');
    img=ImageTk.PhotoImage(img1);
    x = GUI(root, img);
    root.mainloop();

main()