#include <Adafruit_NeoPixel.h>
#include <avr/power.h>
#define PIN            6
#define NUMPIXELS      16
Adafruit_NeoPixel pixels = Adafruit_NeoPixel(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);
int delayval = 2000;
void setup() {
  pixels.begin();
}
void loop() {
  for(int i=0;i<NUMPIXELS;i++){
    pixels.setPixelColor(i, pixels.Color(0,0,0)); // Moderately bright green color.
    pixels.show(); // This sends the updated pixel color to the hardware.
    delay(delayval); // Delay for a period of time (in milliseconds).
  }
}

//Jetzt kann man einfach NUMPIXELS auf die Menge der LEDs einstellen, wie man verwenden will. Über den Befehl
//pixels.setPixelColor(ledNumber, pixels.Color(255,255,255));
