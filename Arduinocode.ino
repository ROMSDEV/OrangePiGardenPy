const int VAL_PROBE = 0; // Analog pin 0
const int MOISTURE_LEVEL = 900; // the value after the pump goes on
int opipin = 8; //recieves the sinal from orangepi
int OPIsignal = 0; //
void setup() {
    Serial.begin(9600);
    pinMode(opipin, INPUT);
    pinMode(7, OUTPUT); //sends the signal to orange pi
    digitalWrite(7, LOW);
}
 
void loop() {
    int moisture = analogRead(VAL_PROBE);
    OPIsignal = digitalRead(opipin);
    Serial.println(moisture);
if (OPIsignal == HIGH)  //if there is signal from opi
    if(moisture > MOISTURE_LEVEL) {
        digitalWrite(7, HIGH); //starts sending the signal
        delay(8000);
        digitalWrite(7, LOW); //turns the signal off
    } else   {
        digitalWrite(7, LOW);
    }
else {
  digitalWrite(7, LOW);
  }
 }

