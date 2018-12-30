int b=13;
int d;
void setup()
{
  Serial.begin(9600);
  pinMode(b,OUTPUT);
}
void loop()
{
  if(Serial.available()>1)
  {  
    d=Serial.read();
    digitalWrite(b,HIGH);
    delay(500);
  }
  else
  {
    digitalWrite(b,LOW);
  }
      
}
