#include <EloquentTinyML.h>
#include "TPH_Anomaly_Predictor.h"
#define NUMBER_OF_INPUTS 3
#define NUMBER_OF_OUTPUTS 1
#define TENSOR_ARENA_SIZE 3*1024

Eloquent::TinyML::TfLite<NUMBER_OF_INPUTS, NUMBER_OF_OUTPUTS, TENSOR_ARENA_SIZE> ml(TPH_Anomaly_Predictor_tflite);


void setup() {
  Serial.begin(115200);
}

void loop() {
  // pick up a random x and predict its sine
  float x = 100;
  float y = 18.6;
  float z = 6529;
  Serial.print("Humidity:");
  Serial.println(x);
  Serial.print("Pressure:");;
  Serial.println(y);
  Serial.print("Temperature:");
  Serial.println(z);
  float input[3] = { x, y, z };
  float predicted = ml.predict(input);

  if (predicted <= 0.5)
  {
    Serial.println("NO Anomaly Detected");

  }
  else {
    Serial.println(" Anomaly Detected");
    Serial.println("Call prediction function");
    Serial.println();
  }
  delay(1000);
}
