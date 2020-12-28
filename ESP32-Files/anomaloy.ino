#include <EloquentTinyML.h>
#include "TPH_Anomaly_Predictor.h"
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>

#define BME_SCK 18
#define BME_MISO 19
#define BME_MOSI 23
#define BME_CS 5*/
Adafruit_BME280 bme;

#define NUMBER_OF_INPUTS 3
#define NUMBER_OF_OUTPUTS 1
#define TENSOR_ARENA_SIZE 3*1024


Eloquent::TinyML::TfLite<NUMBER_OF_INPUTS, NUMBER_OF_OUTPUTS, TENSOR_ARENA_SIZE> ml(TPH_Anomaly_Predictor_tflite);


void setup() {
  Serial.begin(9600);
}

void loop() {
  float h = bme.readHumidity();
  float p = bme.readPressure();
  float t = bme.readTemperature();
  Serial.print("Humidity:");
  Serial.println(h);
  Serial.print("Pressure:");;
  Serial.println(p);
  Serial.print("Temperature:");
  Serial.println(t);
  float input[3] = { h, p, t };
  float predicted = ml.predict(input);

  if (predicted <= 0.5)
  {
    Serial.println("NO Anomaly Detected");

  }
  else {
    Serial.println(" Anomaly Detected");
    Serial.println();
  }
  delay(1000);
}
