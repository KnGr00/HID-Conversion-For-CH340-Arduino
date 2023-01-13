int y = 0;
void setup() {
//the setup routine runs once when you press reset

Serial.begin(115200); //initialize serial communication at 9600 bits per second
}

void loop() {
//the loop routine runs over and over again forever

int sensorValue = analogRead(A0); //read the input on analog pin 0

y = map(sensorValue, 0, 1023, -32768, 32767);

Serial.println(y); //print out the value you read

delay(10); //delay in between reads for stability
}