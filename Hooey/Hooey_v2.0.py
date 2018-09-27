#
# Kyle Hagerman
# Montana State University - Spring 2018
# EGEN 310 - E.10
# Humphrey's GUI - Hooey
#
# This code should run a GUI on a Windows based operating system via Bluetooth with an Arduino to control a car.
# The car is controlled with the arrow keys and press 's' to stop.
# Humphrey has never felt more alive!


from tkinter import *
from tkinter import ttk
import time
import bluetooth

#Bluetooth Initialization
nearby_devices = bluetooth.discover_devices()
num = 0

#for all the nearby devices, print them out to the user
for i in nearby_devices:
    print (num, ": ", bluetooth.lookup_name(i))
    num+=1

#the user selects a bluetooth device
selection = input("> ")
#print the confirmation for the bluetooth device
print ("You have selected", bluetooth.lookup_name(nearby_devices[int(selection)]))
#set the bluetooth address
bd_addr = nearby_devices[int(selection)]
#set the port the bluetooth connection will use
port = 1

class Hooey:
    def __init__(self, master):

        

#Frame declarations
        self.frame_stopwatch = ttk.LabelFrame(master, height = 800, width = 250, text = "Stopwatch")
        self.frame_direction = ttk.LabelFrame(master, height = 800, width = 500, text = "Directional Control")

    #Frame packed in with grid
        self.frame_stopwatch.grid(row = 0, column = 0)
        self.frame_direction.grid(row = 0, column = 1)

#Stopwatch Frame Layout
    #Widget declarations
        start = ttk.Button(self.frame_stopwatch, text = "Start")
        stop = ttk.Button(self.frame_stopwatch, text = "Stop")
        display = ttk.Button(self.frame_stopwatch, text = "Display")
        reset = ttk.Button(self.frame_stopwatch, text = "Reset")

        label_1 = ttk.Label(self.frame_stopwatch, text = "Runtime: ")
        run_time = ttk.Label(self.frame_stopwatch, text = "00:00:00")

        label_2 = ttk.Label(self.frame_stopwatch, text = "Status: ")
        status = ttk.Label(self.frame_stopwatch, text = "Ready")

    #Add widgets to stopwatch frame with grid geo manager
        label_1.grid(row = 0, column = 0, columnspan = 2)
        run_time.grid(row = 0, column = 2, columnspan = 2)
        label_2.grid(row = 1, column = 0, columnspan = 2)
        status.grid(row = 1, column = 2, columnspan = 2)
        start.grid(row = 2, column = 0)
        stop.grid(row = 2, column = 1)
        display.grid(row = 2, column = 2)
        reset.grid(row = 2, column = 3)

    #Format Labels
        label_1.config(font = ('', 24, ''))
        run_time.config(font = ('', 24, ''))
        label_2.config(font = ('', 24, ''))
        status.config(font = ('', 24, ''))

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

        #Add a cascading menu

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

    #File
        menubar.add_cascade(menu = file, label = "File")

        file.add_command(label = 'Exit Program', command = master.destroy)

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

        #declare variables to store time values for the stopwatch methods
        start_time = DoubleVar()
        stop_time = DoubleVar()
        stopped_time = DoubleVar()
        total_time = DoubleVar()

        #initialize above time variables
        start_time.set(0.0)
        stop_time.set(0.0)
        stopped_time.set(0.0)
        total_time.set(0.0)

        #this method will start the watch
        #it checks to see if time has been stopped or if time has already been started before setting the start time
        def start_watch():
            if (stop_time.get() == 0.0) & (start_time.get() == 0.0):
                start_time.set(time.time())
            else:
                stopped_time.set(stopped_time.get() + (time.time() - stop_time.get()))
                stop_time.set(0.0)
            status.config(text = "Running")

        #this method will stop the watch
        #if time has been stopped then it won't reassign the stop time
        def stop_watch():
            if stop_time.get() == 0.0:
                stop_time.set(time.time())
                status.config(text = "Paused")

        #this method displays the watch
        #the display doesn't auto update so the button has to be clicked in Hooey to display the current run time
        #time has to have been started and the amount of stopped time has to be subtracted from the total time since time started
        def display_watch():
            if start_time.get() > 0.0:
                if stop_time.get() == 0.0:
                    total_time.set((time.time() - start_time.get()) - stopped_time.get())
                else:
                    total_time.set(stop_time.get() - start_time.get())
                run_time.config(text = format_time(total_time.get()))

        #this method resets the watch and all variables to point zero
        def reset_watch():
            start_time.set(0.0)
            stop_time.set(0.0)
            stopped_time.set(0.0)
            run_time.config(text = "00:00:00")
            status.config(text = "Reset, Ready")

        #adds the watch methods to their respective buttons
        stopwatch.add_command(label = 'Start', command = lambda: start_watch()) #define watch, 0 to start watch
        stopwatch.add_command(label = 'Stop', command = lambda: stop_watch()) #1 to stop watch
        stopwatch.add_command(label = 'Display Current Time', command = lambda: display_watch()) #update current display time
        stopwatch.add_command(label = 'Reset', command = lambda: reset_watch()) #3 to clear watch

    #About
    #this menu bar option contains a place for me to link a README file, there's no file there right now
        menubar.add_cascade(menu = about, label = "About")

        def open_readme():
            print('Opening README...') #this needs to open a README.txt file about Hooey and Humphrey
        
        about.add_command(label = 'README', command = open_readme) #define open_readme to display full documentation in basic text file        

#Method Declarations

    #Add commands to buttons, graphs, and treeview by frame
        #Stopwatch
        start.config(command = lambda: start_watch())
        stop.config(command = lambda: stop_watch())
        display.config(command = lambda: display_watch())
        reset.config(command = lambda: reset_watch())

        #Directional Controls
        #Bluetooth methods would theoretically go here
        


#Main Method        
def main():

    #initialize Tkinter window
    root = Tk()
    #make the program title Hooey
    root.title("Hooey")
    #apparently this is legacy code, don't know what it does but it's necessary
    root.option_add('*tearOff', False)
    #instantiate the Hooey class and assign it to the program window
    hooey = Hooey(root)
    
    #initialize the socket to connect via bluetooth
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    #connect to the bluetooth address
    sock.connect((bd_addr,port))

    #To send multiple data packets at once I coded 5 methods to be called by the various keybindings
    #This results in there being a slight delay when the keys are pressed but its a splitsecond delay between servos responding
    #Turns are still very fluid and Humphrey spins in place perfectly
    #Just make sure to hold down the key for 1 second so that the arduino receives the whole command

    #this method selects the right servo
    def bt_right():
        data = 'R'
        sock.send(data)

    #this method selects the left servo
    def bt_left():
        data = 'L'
        sock.send(data)

    #this method sets the direction of the servo to forward
    def bt_forward():
        data = 'F'
        sock.send(data)

    #this method sets the direction of the servo to reverse
    def bt_reverse():
        data = 'R'
        sock.send(data)

    #this method sets the servo to stop
    def bt_s():
        data = 'S'
        sock.send(data)

    #this method makes the vehicle go backwards
    def bt_d(event):
        bt_right()
        bt_forward()
        bt_left()
        bt_reverse()

    #this method makes the vehicle spin in place to the left
    def bt_l(event):
        bt_right()
        bt_forward()
        bt_left()
        bt_forward()

    #this method makes the vehicle go forwards
    def bt_u(event):
        bt_right()
        bt_reverse()
        bt_left()
        bt_forward()

    #this method makes the vehicle spin in place to the right
    def bt_r(event):
        bt_right()
        bt_reverse()
        bt_left()
        bt_reverse()

    #this method stops the vehicle
    def bt_stop(event):
        bt_right()
        bt_s()
        bt_left()
        bt_s()

    #the key bindings for the various methods
    root.bind('<KeyPress-Up>', bt_u)
    root.bind('<KeyPress-Right>', bt_r)
    root.bind('<KeyPress-Down>', bt_d)
    root.bind('<KeyPress-Left>', bt_l)
    
    root.bind('<KeyPress-s>', bt_stop)
    #loops the code to send data after bluetooth connection has been established
    root.mainloop()

if __name__ == "__main__": main()
