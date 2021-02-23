void setup() {

Serial.begin(9600);
}

void loop() {
 
int sen= analogRead(A0);
print(sen);
}
