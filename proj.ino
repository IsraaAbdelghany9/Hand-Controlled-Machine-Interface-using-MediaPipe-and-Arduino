int pin4 = 4;
int pin7 = 7;
void setup() {
  pinMode(pin7, OUTPUT);  // Set pin 7 as output
  pinMode(pin4, OUTPUT);  // Set pin 4 as output
  Serial.begin(9600);  // Set baud rate to match Python code
}
void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    if (command == 'L') {
      digitalWrite(pin7, HIGH);  // Set pin 7 high
      digitalWrite(pin4, LOW);   // Set pin 4 low
    } else if (command == 'R') {
      digitalWrite(pin7, LOW);   // Set pin 7 low
      digitalWrite(pin4, HIGH);  // Set pin 4 high
    } else if (command == 'B') {
      digitalWrite(pin7, HIGH);  // Set pin 7 high
      digitalWrite(pin4, HIGH);  // Set pin 4 high
    } else if (command == 'N') {
      digitalWrite(pin7, LOW);   // Set pin 7 low
      digitalWrite(pin4, LOW);   // Set pin 4 low
    }
  }
}
