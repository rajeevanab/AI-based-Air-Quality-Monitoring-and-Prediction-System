void setup() {

Serial.begin(9600); // setting the board rate
}

void loop() {
 
int sen= analogRead(A0); // reading the analog values from the sensor 
print(sen); //print the sensor values
}
