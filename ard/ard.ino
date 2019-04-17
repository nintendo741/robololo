void func() {
  randomSeed(analogRead(A0));
  delay(random(1000, 4000));
  Serial.println("Done");
}
void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
  //func();
}
void loop() {
  while (!Serial.available());
  char x = Serial.read();
  switch (x) {
    case ('M'):
      func();
      break;
    //default:
      //Serial.println(x);
      // ololo ololo tralala
  }
}
