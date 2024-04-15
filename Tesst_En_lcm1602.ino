//Ich weiß nicht, was ich falsch mache, es funktioniert nicht.
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
/**********************************************************/
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup()
{
  lcd.begin(16,2),
  lcd.setCursor(0,0);
  lcd.print("hallo juuunGe");
  lcd.setCursor(0,1);
  
  /*lcd.init();  //initialize the lcd
  lcd.backlight();*/  //open the backlight
}
/*********************************************************/
void loop()
{

}
