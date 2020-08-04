#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WiFiMulti.h> 
#include <ESP8266mDNS.h>
#include <ESP8266WebServer.h>
#include<Servo.h>
#define MAX_ANGLE_X 120
#define MIN_ANGLE_X 60
#define MAX_ANGLE_Y 120
#define MIN_ANGLE_Y 60
#define CAN_CONTROLLER_CS 12
#define SERVO_X D4
#define SERVO_Y D7
int next_angle_x=90,next_angle_y=90;
int current_angle_x=90,current_angle_y=90;
Servo angleX,angleY;

#ifndef STASSID
#define STASSID "Tp-Link"
#define STAPSK  "01787232425*#"
#endif

const char* ssid     = STASSID;
const char* password = STAPSK;

ESP8266WiFiMulti WiFiMulti;

ESP8266WebServer server(80);    // Create a webserver object that listens for HTTP request on port 80

void handleRoot();              // function prototypes for HTTP handlers
void handleLogin();
void handleNotFound();

void setup(void){
  Serial.begin(115200);         // Start the Serial communication to send messages to the computer
  delay(10);
  WiFi.mode(WIFI_STA);
  WiFiMulti.addAP(ssid, password);
  Serial.println();
  Serial.println();
  Serial.print("Wait for WiFi... ");

  while (WiFiMulti.run() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

  delay(500);
  
  pinMode(SERVO_X,OUTPUT);
  pinMode(SERVO_Y,OUTPUT); 
  
  
  Serial.println('\n');  
  server.on("/", HTTP_GET, handleRoot);        // Call the 'handleRoot' function when a client requests URI "/"
  server.on("/request", HTTP_POST, handleRequest); // Call the 'handleLogin' function when a POST request is made to URI "/login"
  server.onNotFound(handleNotFound);           // When a client requests an unknown URI (i.e. something other than "/"), call function "handleNotFound"

  server.begin();                            // Actually start the server
  Serial.println("HTTP server started");
  angleX.attach(SERVO_X);
  delay(2000);
  angleY.attach(SERVO_Y);
  delay(2000);
  Aim();
}

void loop(void){
  server.handleClient();                     // Listen for HTTP requests from clients
}

void handleRoot() {                          // When URI / is requested, send a web page with a button to toggle the LED
  server.send(200, "text/html", "unit test");
}

void handleRequest() {                         // If a POST request is made to URI /login
  String Data = "";
    if (server.hasArg("target") && server.hasArg("X") && server.hasArg("Y")){
    Data = "X"+server.arg("X")+"Y"+server.arg("Y");
  }
  else if (server.hasArg("command")){
    Data = server.arg("command");  
  }
  else {
    Data = "invalid";
  }
  if (Data != "invalid"){
    if (strlen(Data.c_str())==8){
      if (Data[0]=='X' && Data[4]=='Y'){
        next_angle_x = Data.substring(1,4).toInt();
        next_angle_y = Data.substring(5,9).toInt();
        Aim();
        server.send(200, "text/html", "X="+server.arg("X")+"Y="+server.arg("Y")+"-->OK");
        return;
      }
      else{
        server.send(200, "text/html", "!!invalid!!");
        return;}
    }
    else if (Data=="XI"){
      ++next_angle_x;
      Aim();
    }
    else if (Data=="XD"){
      --next_angle_x;
      Aim();
    }
    else if (Data=="YI"){
      ++next_angle_y;
            Aim();
    }
    else if (Data=="YD"){
      --next_angle_y;
      Aim();
    }
    server.send(200, "text/html", "X="+String(next_angle_x)+"Y="+String(next_angle_y)+"-->OK");
  }
  else
    server.send(200, "text/html", "!!invalid_request!!"); 
}

void handleNotFound(){
  server.send(404, "text/plain", "404: Not found"); // Send HTTP status 404 (Not Found) when there's no handler for the URI in the request
}
void Aim(void){
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
        current_angle_x = i;
        current_angle_y = j;
        break;
      }
  }
}
