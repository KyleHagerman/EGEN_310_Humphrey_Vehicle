#
# Kyle Hagerman
# EGEN 310
# Humphrey's GUI - Hooey
#
# This code should run a GUI on a Raspberry Pi Zero W to communicate
# via Bluetooth with an Arduino to control a car. The controller will have
# a Left and Right joystick and a small 360x480 pixel screen. So here goes nothing!


from tkinter import *
from tkinter import ttk
import time


class Hooey:
    def __init__(self, master):

#Frame declarations
        self.frame_stopwatch = ttk.LabelFrame(master, height = 800, width = 250, text = "Stopwatch")
        self.frame_graphics = ttk.LabelFrame(master, height = 400, width = 500, text = "Graphical Data")
        self.frame_systeminfo = ttk.LabelFrame(master, height = 400, width = 500, text = "System Information")
        self.frame_direction = ttk.LabelFrame(master, height = 800, width = 500, text = "Directional Control")

    #Frame packed in with grid
        self.frame_stopwatch.grid(row = 0, column = 0)
##        self.frame_graphics.grid(row = 0, column = 1)
##        self.frame_systeminfo.grid(row = 1, column = 1)
        self.frame_direction.grid(row = 0, column = 1)

#Stopwatch Frame Layout
    #Widget declarations
        start = ttk.Button(self.frame_stopwatch, text = "Start")
        stop = ttk.Button(self.frame_stopwatch, text = "Stop")
        split = ttk.Button(self.frame_stopwatch, text = "Split")
        reset = ttk.Button(self.frame_stopwatch, text = "Reset")

        label_1 = ttk.Label(self.frame_stopwatch, text = "Runtime: ")
        run_time = ttk.Label(self.frame_stopwatch, text = "00:00:000")

        splits = ttk.Treeview(self.frame_stopwatch)

    #Add widgets to stopwatch frame with grid geo manager
        label_1.grid(row = 0, column = 0, columnspan = 2)
        run_time.grid(row = 0, column = 2, columnspan = 2)
        start.grid(row = 1, column = 0)
        stop.grid(row = 1, column = 1)
        split.grid(row = 1, column = 2)
        reset.grid(row = 1, column = 3)
        splits.grid(row = 2, column = 0, columnspan = 4)

    #Initialize splits Treeview
        splits.config(columns = "Splits") #2nd column for splits
        splits.insert('', '0', 'split_1', text = 'Element 1')
        splits.insert('', '1', 'split_2', text = 'Element 2')
        splits.insert('', '2', 'split_3', text = 'Element 3')
        splits.insert('', '3', 'split_4', text = 'Element 4')
        splits.insert('', '4', 'split_5', text = 'Element 5')
        splits.insert('', '5', 'split_6', text = 'Element 6')
        splits.insert('', '6', 'split_7', text = 'Element 7')
        splits.insert('', '7', 'split_8', text = 'Element 8')
        splits.insert('', '8', 'split_9', text = 'Total Time')

        split_list = ["00:00:00", "00:00:00", "00:00:00", "00:00:00", "00:00:00",
                      "00:00:00", "00:00:00", "00:00:00", "00:00:00"]

        counter = 1
        counter_string = str(counter)
        for x in range (0, 9):
            splits.set("split_" + counter_string, 'Splits', split_list[x])
            counter = counter + 1
            counter_string = str(counter)


#Graphical Data Frame Layout
    #Widget declarations
        velocity = ttk.Label(self.frame_graphics, text = "Velocity")
        acceleration = ttk.Label(self.frame_graphics, text = "Acceleration")
        graph_1 = ttk.Label(self.frame_graphics, text = "Graph_1")
        graph_2 = ttk.Label(self.frame_graphics, text = "Graph_2")
        
    #graphs???

    #Add widgets to graphics frame with grid geo manager
##        velocity.grid(row = 1, column = 0)
##        acceleration.grid(row = 1, column = 1)
##        graph_1.grid(row = 0, column = 0)
##        graph_2.grid(row = 0, column = 1)

#System Information Frame Layout
    #Widget declarations
        label_2 = ttk.Label(self.frame_systeminfo, text = "Circuit Temperature: ")
        label_3 = ttk.Label(self.frame_systeminfo, text = "Amperage: ")
        label_4 = ttk.Label(self.frame_systeminfo, text = "Voltage: ")
        amps = ttk.Label(self.frame_systeminfo, text = "0.0mA")

        temp = ttk.Button(self.frame_systeminfo, text = "0.0 F")

        graph_3 = ttk.Label(self.frame_systeminfo, text = "Graph_3")

    #Grid geo manager for systeminfo frame
##        label_2.grid(row = 0, column = 0)
##        temp.grid(row = 0, column = 1)
##        label_3.grid(row = 0, column = 2)
##        amps.grid(row = 0, column = 3)
##        label_4.grid(row = 2, column = 0)
##        graph_3.grid(row = 3, column = 0, columnspan = 4)

        #Menubar declaration
        menubar = Menu(master)

        #Adding menubar to window
        master.config(menu = menubar)

        #Add cascading menu titles to menubar
        file = Menu(menubar)
        stopwatch = Menu(menubar)
        graphs = Menu(menubar)
        temperature = Menu(menubar)
        about = Menu(menubar)
        
#Directional Control Frame Layout
        #Directional Arrow Buttons
        self.n_img = PhotoImage(file = 'C:\\Users\\hager\\Desktop\\Hooey\\up-chevron.gif')
        self.n_img_small = self.n_img.subsample(5,5)
        north = ttk.Button(self.frame_direction, image = self.n_img_small)
        
        self.e_img = PhotoImage(file = 'C:\\Users\\hager\\Desktop\\Hooey\\right-arrow.gif')
        self.e_img_small = self.e_img.subsample(5,5)
        east = ttk.Button(self.frame_direction, image = self.e_img_small)
        
        self.s_img = PhotoImage(file = 'C:\\Users\hager\\Desktop\\Hooey\\down-chevron.gif')
        self.s_img_small = self.s_img.subsample(5,5)
        south = ttk.Button(self.frame_direction, image = self.s_img_small)
        
        self.w_img = PhotoImage(file = 'C:\\Users\\hager\\Desktop\\Hooey\\left-arrow.gif')
        self.w_img_small = self.w_img.subsample(5,5)
        west = ttk.Button(self.frame_direction, image = self.w_img_small)

        #Add arrows to frame with grid
        north.grid(row = 0, column = 1)
        east.grid(row = 1, column = 2)
        south.grid(row = 2, column = 1)
        west.grid(row = 1, column = 0)

    #File
        menubar.add_cascade(menu = file, label = "File")

        def export_data():
            print('Exported data...') #replace with text file generation with all current system data

        def exit_():
            print('Exiting program...') #replace with function that kills program
        
##        file.add_command(label = 'Export Data', command = export_data) #define export_data
        file.add_command(label = 'Exit Program', command = exit_) #define exit_


    #Stopwatch
        menubar.add_cascade(menu = stopwatch, label = "Stopwatch")

        def format_time(value):
            '''From seconds to Days;Hours:Minutes;Seconds'''

            valueD = (((value/365.0)/24.0)/60.0)
            D = int(valueD)
            Days = str(D)

            valueH = (valueD-D)*365.0
            H = int(valueH)
            Hours = str(H)

            valueM = (valueH - H)*24.0
            M = int(valueM)
            Minutes = str(M)

            valueS = (valueM - M)*60.0
            S = int(valueS)
            Seconds = str(S)

            if H < 10:
                if M < 10:
                    if S < 10:
                        return ("0" + Hours + ":0" + Minutes + ":0" + Seconds)
                    else:
                        return ("0" + Hours + ":0" + Minutes + ":" + Seconds)
                else:
                    return ("0" + Hours + ":" + Minutes + ":" + Seconds)
            else:
                return (Hours + ":" + Minutes + ":" + Seconds)




##        start = time.time() # What in other posts is described is
##
##        #***your code HERE***
##
##        end = time.time()         
##        stopWatch(end-start) #Use then my code

        start_time = DoubleVar()
        stop_time = DoubleVar()
        stopped_time = DoubleVar()
        split_time = DoubleVar()
        total_time = DoubleVar()
        
        def get_time(number):
            if number == 0:
                if stop_time.get() == 0.0:
                    start_time.set(time.time())
                    run_time.config(text = "Started")
                else:
                    stopped_time.set(stopped_time.get() + (time.time() - stop_time.get()))
                    stop_time.set(0.0)
                    run_time.config(text = "Started")
            elif number == 1:
                stop_time.set(time.time())
                run_time.config(text = "Time Paused")
            elif number == 2:

                if stop_time.get() == 0.0:
                    split_time.set(time.time() - (stopped_time.get() + start_time.get()))
                else:
                    split_time.set(time.time() - (stop_time.get() + start_time.get()))

                counter = 1
                counter_string = str(counter)
                for x in range (0,7):
                    if split_list[x] == "00:00:00":
                        split_list[x] = format_time(split_time.get())
                        total_time.set(total_time.get() + split_time.get())
                        split_list[8] = format_time(total_time.get())
                        break
                    counter = counter + 1
                    counter_string = str(counter)
                    splits.set("split_" + counter_string, 'Splits', split_list[x])
                
##                temp = DoubleVar()
##                temp.set(time.time())
##                print("1 ",format_time(temp.get()))
##                stopped_time.set((temp.get() - stop_time.get()))
##                print("2 ",format_time(stopped_time.get()))
##                counter = 1
##                counter_string = str(counter)
##                for x in range (0, 7):
##                    if split_list[x] == "00:00:00":
##                        if split_time.get() == 0.0:
##                            split_time.set(temp.get() - (start_time.get() + stopped_time.get()))
##                            print("3 ",format_time(split_time.get()))
##                            total_time.set(split_time.get() + total_time.get())
##                            print("4 ",format_time(total_time.get()))
##                            formatted_total_time = format_time(total_time.get())
##                            splits.set("split_9", 'Splits', formatted_total_time)
##                            split_list[x] = format_time(split_time.get())
##                            break
##                        else:
##                            split_time.set(temp.get() - split_time.get())
##                            split_list[x] = format_time(split_time.get())
##                            total_time.set(split_time.get() + total_time.get())
##                            formatted_total_time = format_time(total_time.get())
##                            splits.set("split_9", 'Splits', formatted_total_time)
##                            break
##                    splits.set("split_" + counter_string, 'Splits', split_list[x])
##                    counter = counter + 1
##                    counter_string = str(counter)
##                splits.set("split_" + counter_string, 'Splits', split_list[x])
            elif number == 3:
                start_time.set(0.0)
                stop_time.set(0.0)
                stopped_time.set(0.0)
                split_time.set(0.0)
                run_time.config(text = "00:00:00")
                
                counter = 1
                counter_string = str(counter)
                for x in range (0, 9):
                    splits.set("split_" + counter_string, 'Splits', "00:00:00")
                    counter = counter + 1
                    counter_string = str(counter)
        
        stopwatch.add_command(label = 'Start', command = lambda : get_time(0)) #define watch, 0 to start watch
        stopwatch.add_command(label = 'Stop', command = lambda: get_time(1)) #1 to stop watch
        stopwatch.add_command(label = 'Split', command = lambda: get_time(2)) #2 to record split
        stopwatch.add_command(label = 'Reset', command = lambda: get_time(3)) #3 to clear watch
        
##    #Graphs
##        menubar.add_cascade(menu = graphs, label = "Graphs")
##
##        def export_graph_data():
##            print('Exported graph data...') #export just graph data
##
##        def mps_to_kms():
##            print('Converet from meters per second to kilometers per second') #simple unit conversion, needs to go both ways
##
##        def clear_graph():
##            print('Cleared graphs...') #erase graphs
##        
##        graphs.add_command(label = 'Export...', command = export_graph_data) #define export_graph_data
##        graphs.add_command(label = 'Units', command = mps_to_kms) #define mps_to_kms
##        graphs.add_command(label = 'Clear Graphs', command = clear_graph) #define clear_graph
##
##    #Temperature
##        menubar.add_cascade(menu = temperature, label = "Temperature")
##
##        def change_units():
##            print('Changed units...') #switch from C to F and vice versa
##        
##        temperature.add_command(label = 'Change Units', command = change_units) #define change_units

    #About
        menubar.add_cascade(menu = about, label = "About")

        def open_readme():
            print('Opening README...') #this needs to open a README.txt file about Hooey and Humphrey
        
        about.add_command(label = 'README', command = open_readme) #define open_readme to display full documentation in basic text file        

    #Method Declarations

    #Add commands to buttons, graphs, and treeview by frame
        #Stopwatch
        start.config(command = lambda: get_time(0))
        stop.config(command = lambda: get_time(1))
        split.config(command = lambda: get_time(2))
        reset.config(command = lambda: get_time(3))

        #Graphical Data

        #System Info
        

def main():

    root = Tk()
    root.title("Hooey")
    root.option_add('*tearOff', False)
    hooey = Hooey(root)
    root.mainloop()

if __name__ == "__main__": main()
