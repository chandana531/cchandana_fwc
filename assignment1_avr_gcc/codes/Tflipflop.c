#include<avr/io.h>
#include<stdbool.h>
#include <util/delay.h> 

void clk1(){
PORTB=((1<<PB5));
_delay_ms(1000);
PORTB=((0<<PB5));
_delay_ms(1000);
}
int main(){
bool D,Q,T;
Q = (PIND & (1<<PIND3)) == (1<<PIND3);
//DDRD = 0b11110000;
//DDRD |= (1<<DDD3);
//DDRD |=~(1<<DDD6)
//DDRD |=(1<<DDD0)

while(1)
   {
	   T = (PIND & (1<<PIND0)) == (1<<PIND0);	
	  
	   
	   D = ((!Q)&&T) ||((Q)&&(!T));
	
	PORTD = (D<<PD6);
	
    clk1();

   }


}

