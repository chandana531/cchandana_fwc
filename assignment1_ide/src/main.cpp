#include<Arduino.h>
int T,Q,D;
void setup()
{
	pinMode(13,OUTPUT);
	pinMode(7,OUTPUT);
	pinMode(2,INPUT);
	pinMode(4,INPUT);
}
void loop()
{
	digitalWrite(13,HIGH);
	delay(1000);
	Q=digitalRead(4);
	T=digitalRead(2);
	D=T&&!Q || !T&&Q;
	digitalWrite(7,D);
	digitalWrite(13,LOW);
	delay(1000);
}
