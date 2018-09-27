#include <Servo.h>
#include <SoftwareSerial.h>


SoftwareSerial BTcomm(3,4);                 //This sets up the communication ports to be used by the module
Servo servoL;                               //Declares the Left servo
Servo servoR;                               //Declares the Right servo
  char input;                               //Declares a variable to hold the input character
  char r_speed_val, l_speed_val;            //Declares two characters to use for right and left servo setting assignment

void setup() {
  servoL.attach(11, 1000, 2000);            //This sets the pinout for the servo on the board as well as the min and max values it can receive
  servoR.attach(12, 1000, 2000);            //This sets the pinout for the servo on the board as well as the min and max values it can receive
  servoL.writeMicroseconds(1500);           //This starts the servo in the stopped position
  servoR.writeMicroseconds(1500);           //This starts the servo in the stopped position
  BTcomm.begin(9600);
  Serial.begin(9600);
  pinMode(2, OUTPUT);
  
}
void loop() { 
  if(BTcomm.available())                    //if there's data available to be read then we will enter this control structure
  {
    input = BTcomm.read();                  //set the input variable to the incoming character
    
    Serial.println("Value Received: ");     //A test print to check the control structure
    Serial.println(input);

    if(input == 'L'){                       //if the input character is selecting the left servo then we enter this control structure to set the state of the motor
      l_speed_val = BTcomm.read();          //read the next character from the GUI
      if(l_speed_val == 'F'){               //set the motor to go forward at 80% speed
        servoL.writeMicroseconds(1800);
      }
      if(l_speed_val == 'S'){               //set the motor to stop
        servoL.writeMicroseconds(1500);  
      }
      if(l_speed_val == 'R'){               //set the motor to go backward at 80% speed
        servoL.writeMicroseconds(1200);  
      }
    }

    if(input == 'R'){                       //if the input character is selecting the right servo then we enter this control structure to set the state of the motor
      r_speed_val = BTcomm.read();          //read the next character from the GUI
      if(r_speed_val == 'F'){               //set the motor to go forward at 80% speed
        servoR.writeMicroseconds(1800);
      }
      if(r_speed_val == 'S'){               //set the motor to stop
        servoR.writeMicroseconds(1500);  
      }
      if(r_speed_val == 'R'){               //set the motor to go backward at 80% speed
        servoR.writeMicroseconds(1200);  
      }
    }
  }
}
