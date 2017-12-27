#include <Wire.h>

#define slave_addr 0x48
#define conversion_reg 0x00
#define config_reg 0x01


void setup() {
  Wire.begin();                // join i2c bus (address optional for master)
  Serial.begin(115200);          // start serial communication at 115200bps
  
  // set up ADS1115
  Wire.beginTransmission(slave_addr);
  Wire.write(byte(config_reg));
  Wire.write(byte(0xC2)); // continuous mode, AIN1&AIN0, FSR ±4.096V
  Wire.write(byte(0x83)); // 128SPS, disable comparator
  Wire.endTransmission();

  delay(50);
  
  // Instruct ADS115 pointer to point to conversion register
  Wire.beginTransmission(slave_addr);
  Wire.write(byte(conversion_reg)); //pointer to conversion register
  Wire.endTransmission();      // stop transmitting

  delay(50);
}

byte Low = 0;
byte High = 0;
//float filtered;

void loop() {
  // step 4: request reading from sensor
  Wire.requestFrom(slave_addr, 2);    // request 2 bytes from slave device 

  // step 5: receive reading from sensor
  if (2 <= Wire.available()) { // if two bytes were received
    High = Wire.read();  // receive high byte (overwrites previous reading)
    Low = Wire.read(); // receive low byte as lower 8 bits
    Serial.write(High);
    Serial.write(Low);
  }
  delay(10);                  // wait a bit since people have to read the output :)
}

