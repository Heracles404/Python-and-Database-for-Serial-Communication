#define signal A0

void setup() {
  Serial.begin(9600);
  pinMode(signal, INPUT);
}

void loop() {
  int swtch = digitalRead(signal);

  switch (swtch) {
    case HIGH:
      Serial.println("ON");
      break;
    case LOW:
      Serial.println("OFF");
      break;
    default:
      Serial.println("Cannot be determined!");
      break;
  }

  delay(500);
}
