#include <Adafruit_NeoPixel.h>

#define PIN            6
#define NUMPIXELS      34
Adafruit_NeoPixel pixels = Adafruit_NeoPixel(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);

char buff[2*NUMPIXELS*3];


void setup() {
  pinMode(13,OUTPUT);
  Serial.begin(115200);
  pixels.begin();
  pixels.setPixelColor(0, 100,00,00); 
  pixels.show();


  digitalWrite(13,HIGH);
  delay(500);
  digitalWrite(13,LOW);
  delay(500);
  digitalWrite(13,HIGH);
  delay(500);
  digitalWrite(13,LOW);
  
}


void loop() {
// $FF,FF,FF ->> 6 byte
Serial.println(sizeof(buff));

  while (Serial.available() == 0);
  do
  {
      Serial.readBytes(buff, sizeof(buff)); 
  }
  while(buff[0] != '$');

  int i=0;
  int j=0;
  for (i = 0; i<sizeof(buff); i++)
  pixels.setPixelColor(i,   pixels.Color(buff[1+(i*6)], buff[3+(i*6)], buff[5+(i*6)]));
  
  pixels.show(); 
}



