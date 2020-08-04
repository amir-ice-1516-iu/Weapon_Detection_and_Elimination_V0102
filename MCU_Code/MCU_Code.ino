#include<Servo.h>
#define MAX_ANGLE_X 120
#define MIN_ANGLE_X 60
#define MAX_ANGLE_Y 120
#define MIN_ANGLE_Y 60
#define CAN_CONTROLLER_CS 12
#define SERVO_X 2
#define SERVO_Y 10
int next_angle_x=90,next_angle_y=90;
int current_angle_x,current_angle_y;
Servo angleX,angleY;
void setup() {
  // put your setup code here, to run once:
  pinMode(SERVO_X,OUTPUT);
  pinMode(SERVO_Y,OUTPUT);
  pinMode(CAN_CONTROLLER_CS,OUTPUT);
  digitalWrite(CAN_CONTROLLER_CS,HIGH);
  Serial.begin(115200);
  angleX.attach(SERVO_X);
  delay(2000);
  angleY.attach(SERVO_Y);
  delay(2000);
  Aim();
}
void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()>0){
    String Data = Serial.readString();
    if (strlen(Data.c_str())==8){
      if (Data[0]=='X' && Data[4]=='Y'){
        next_angle_x = Data.substring(1,4).toInt();
        next_angle_y = Data.substring(5,9).toInt();
        Aim();
      }
    }
    else if (Data=="XI"){
      ++next_angle_x;
      Serial.write('O');
      Serial.write('K');
      Serial.write('\n');
//      Serial.write('\r');
//      Aim();
    }
    else if (Data=="XD"){
      --next_angle_x;
      Serial.write('O');
      Serial.write('K');
      Serial.write('\n');
//      Serial.write('\r');
//      Aim();
    }
    else if (Data=="YI"){
      ++next_angle_y;
      Serial.write('O');
      Serial.write('K');
      Serial.write('\n');
//      Serial.write('\r');
      //      Aim();
    }
    else if (Data=="YD"){
      --next_angle_y;
      Serial.write('O');
      Serial.write('K');
      Serial.write('\n');
//      Serial.write('\r');
//      Aim();
    } 
  }
}
void Aim(void){
  
  current_angle_x = angleX.read();
  current_angle_y = angleY.read();
  int i=current_angle_x,j=current_angle_y;
  while(true){
    if (i+5<next_angle_x){
      
      i += 5;
    }
    else if(i-5>next_angle_x){
      i -= 5;
    }
    else if(i<next_angle_x){
      ++i;
    }
    else if(i>next_angle_x){
      --i;
    }
    if (i>=MIN_ANGLE_X && i<=MAX_ANGLE_X){
      angleX.write(i);
      delay(20);
    }
      
    if (j+5 < next_angle_y){
      j+=5;   
    }
    else if(j-5 > next_angle_y){
      j-=5;
    }
    else if(j<next_angle_y){
      ++j;      
    }
    else if(j>next_angle_y){
      --j;
    }
    if (j>=MIN_ANGLE_Y && j<=MAX_ANGLE_Y){
      angleY.write(j);
      delay(20);
    }
    if( i==next_angle_x && j==next_angle_y)
      {
        next_angle_x = i;
        next_angle_y = j;
        Serial.write('O');
        Serial.write('K');
        Serial.write('\n');
        break;
      }
  }
}
