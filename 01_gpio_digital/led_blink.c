
#define LED 7

int main(void){
    wiringPiSetupGpio();
    pinMode(LED, OUTPUT);
    for (int i=0; i<10; i++){
        digitalWrite(LED,HIGH); delay(1000);
        digitalWrite(LED,LOW); delay(1000);
    }
    return 0;
}