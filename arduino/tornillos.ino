#include <Servo.h>

Servo myservo;  // create servo object to control a servo

#define dir1 8
#define dir2 9

void setup() {
  pinMode(dir1, OUTPUT);
  pinMode(dir2, OUTPUT);
  
  myservo.attach(10);
  Serial.begin(9600);

}

void abrir(){
  digitalWrite(dir1,0);
  digitalWrite(dir2,1);
  Serial.println("abriendo");
}

void cerrar(){
  digitalWrite(dir1,1);
  digitalWrite(dir2,0);
  Serial.println("cerrando");
}

void detener(){
  digitalWrite(dir1,0);
  digitalWrite(dir2,0);
  Serial.println("deteniendo");
}

void move_servo(int a){
  myservo.write(a);                  // sets the servo position according to the scaled value
  delay(1000);   
  Serial.print("moviendo el servo a: ");
  Serial.println(a);
}

void loop() {
  cerrar();
  delay(5000);
  move_servo(80);
  detener();
  delay(10000);
  //tomar foto
  move_servo(5);
  abrir();
  delay(5000);
  
}
