const int VAL_PROBE = 0; // Analog pin 0
const int MOISTURE_LEVEL = 900; // the value after the LED goes ON
int opipin = 8;
int OPIsignal = 0;
void setup() {
    Serial.begin(9600);
    pinMode(opipin, INPUT);
    pinMode(7, OUTPUT);
    digitalWrite(7, LOW);
}
 
void loop() {
    int moisture = analogRead(VAL_PROBE);
    OPIsignal = digitalRead(opipin);
    Serial.println(moisture);
if (OPIsignal == HIGH) 
    if(moisture > MOISTURE_LEVEL) {
        digitalWrite(7, HIGH);
        delay(8000);
        digitalWrite(7, LOW);
    } else   {
        digitalWrite(7, LOW);
    }
else {
  digitalWrite(7, LOW);
  }
 }

