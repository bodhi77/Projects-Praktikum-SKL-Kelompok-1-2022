void setup() {
  Serial.begin(9600);
}

void loop() {
int x = map(analogRead(A1),0,1023,0,30);
Serial.println(x);
delay(100);
}
