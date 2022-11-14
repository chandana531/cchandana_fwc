#include <WiFi.h>
#include <WiFiUdp.h>
#include <ArduinoOTA.h>
#include<Arduino.h>
//    Can be client or even host   //
#ifndef STASSID
#define STASSID "chand"  // Replace with your network credentials
#define STAPSK  "9502530594"
#endif

const char* ssid = STASSID;
const char* password = STAPSK;


void OTAsetup() {
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  while (WiFi.waitForConnectResult() != WL_CONNECTED) {
    delay(5000);
    ESP.restart();
  }
  ArduinoOTA.begin();
}

void OTAloop() {
  ArduinoOTA.handle();
}
int T,Q,D;
//Code released under GNU GPL.  Free to use for anything.
// the setup function runs once when you press reset or power the board
void setup() {
	OTAsetup();
        pinMode(13,OUTPUT);
	pinMode(7,OUTPUT);
	pinMode(2,INPUT);
	pinMode(4,INPUT);
}

// the loop function runs over and over again forever
void loop ()
{
	OTAloop();
        digitalWrite(13,HIGH);
	delay(1000);
	Q=digitalRead(4);
	T=digitalRead(2);
	D=T&&!Q || !T&&Q;
	digitalWrite(7,D);
	digitalWrite(13,LOW);
	delay(1000);
}
