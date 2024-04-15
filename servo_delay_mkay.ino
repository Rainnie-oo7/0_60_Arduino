#include <Servo.h>
Servo myServo;

int servoPin = 3;


void setup()
{
  myServo.attach(servoPin);
}

void loop()
{
  for (int i=20;i<=160;i=i+1)
  {
    myServo.write(i);
    delay(20); 
  }

  for (int i=160;i>=20;i=i-1)
  {
    myServo.write(i);
    delay(20);
  }
  
}
