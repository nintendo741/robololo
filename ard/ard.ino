void func() {
	randomSeed(analogRead(A0));
	delay(random(100, 400));
	Serial.println("Done");
}
void func2() {
	randomSeed(analogRead(A0));
	delay(random(100, 400));
	int x = random(100, 400);
	Serial.println(x);
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
	case ('X'):
		func2();
		break;
	default:
		Serial.println(x);
		break;
	}
}
