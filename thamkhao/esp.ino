#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include "MAX30100_PulseOximeter.h"
#include "Adafruit_MLX90614.h"

const char* ssid = "your_SSID";
const char* password = "your_PASSWORD";

ESP8266WebServer server(80);

PulseOximeter pox;
Adafruit_MLX90614 mlx = Adafruit_MLX90614();

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  
  Serial.println("Connected to WiFi");
  
  if (!pox.begin()) {
    Serial.println("Failed to initialize MAX30100");
    while (1);
  }
  
  mlx.begin();
  
  server.on("/measure", HTTP_GET,  {
    pox.update();
    float temp = mlx.readObjectTempC();
    float heartRate = pox.getHeartRate();
    
    String jsonData = "{\"temperature\":" + String(temp) + ",\"heartRate\":" + String(heartRate) + "}";
    server.send(200, "application/json", jsonData);
  });
  
  server.begin();
}

void loop() {
  server.handleClient();
}
