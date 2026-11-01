const int trigPin1 = 2; const int echoPin1 = 3;
const int trigPin2 = 4; const int echoPin2 = 5;
const int trigPin3 = 6; const int echoPin3 = 7;
const int buzzerPin = 8;

const int UMBRAL_DISTANCIA = 80; 

bool ocupado1 = false;
bool ocupado2 = false;
bool ocupado3 = false;

long medirDistancia(int trigPin, int echoPin) {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  long duracion = pulseIn(echoPin, HIGH, 25000); 
  if (duracion == 0) return 999;
  return duracion * 0.034 / 2;
}

void sonarBip() {
  tone(buzzerPin, 1500, 100);
}

void setup() {
  Serial.begin(9600);
  pinMode(trigPin1, OUTPUT); pinMode(echoPin1, INPUT);
  pinMode(trigPin2, OUTPUT); pinMode(echoPin2, INPUT);
  pinMode(trigPin3, OUTPUT); pinMode(echoPin3, INPUT);
  pinMode(buzzerPin, OUTPUT);
}

void loop() {
  // Sensor 1
  long d1 = medirDistancia(trigPin1, echoPin1);
  if (d1 < UMBRAL_DISTANCIA && !ocupado1) {
    sonarBip();
    Serial.println("SENSOR_1");
    ocupado1 = true;
  } else if (d1 >= UMBRAL_DISTANCIA && ocupado1) {
    ocupado1 = false;
  }
  delay(30);

  // Sensor 2
  long d2 = medirDistancia(trigPin2, echoPin2);
  if (d2 < UMBRAL_DISTANCIA && !ocupado2) {
    sonarBip();
    Serial.println("SENSOR_2");
    ocupado2 = true;
  } else if (d2 >= UMBRAL_DISTANCIA && ocupado2) {
    ocupado2 = false;
  }
  delay(30);

  // Sensor 3
  long d3 = medirDistancia(trigPin3, echoPin3);
  if (d3 < UMBRAL_DISTANCIA && !ocupado3) {
    sonarBip();
    Serial.println("SENSOR_3");
    ocupado3 = true;
  } else if (d3 >= UMBRAL_DISTANCIA && ocupado3) {
    ocupado3 = false;
  }
  delay(30);
}