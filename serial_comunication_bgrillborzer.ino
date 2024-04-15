
#include <Wire.h>
#include <LiquidCrystal_I2C.h> //LiquidCrystal_I2C library

LiquidCrystal_I2C lcd(0x27, 16, 2); //0x27 is the i2c address of the LCM1602 IIC v1 module (might differ) (0x27, 2, 1, 0, 4, 5, 6, 7, 3, positive)

void setup() {
  // put your setup code here, to run once:
  /*lcd.begin(16, 2);
  lcd.backlight();*/
  lcd.clear();
  
  /*Serial.begin(9600);
  while(!Serial) {
    ;
  }
  lcd.setCursor(0,0);   //where to print something, we set on first  column first row)
  lcd.print("Init done");*/
}

void loop() {
  // put your main code here, to run repeatedly:

    lcd.setCursor(0,0);   //where to print something, we set on first  column first row)
  lcd.print("Init done");

  /*
  if (Serial.available() > 0) {
    byte incomingByte = Serial.read();
    if (incomingByte != -1) {
      
      Serial.print("I received: ");
      Serial.println(incomingByte);
      
    lcd.setCursor(0,0);
    lcd.print("I received");
    lcd.setCursor(0,1);
    lcd.print(incomingByte); 
    }
  }
}
*/
}
