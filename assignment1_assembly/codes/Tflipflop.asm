include "/home/chandana/m328Pdef.inc"

.def led1 = r20
.def mask=r21

ldi r17,0b00000100         ;2spins outputs
out DDRD,r17

sbi DDRB, 5 ;set pin 13 as output pin (DDRB pin 5)
ldi r16, 0b00000101 ;the last 3 bits define the prescaler, 101 => division by 1024
out TCCR0B, r16 

ldi r26,0b11111110             ;T
out DDRB,r26
;ldi r26,0b11111110
;out PORTB,r26
in r26,PINB

ldi r27,0b00000000             ;Qn
ldi r28,0b00000000             ;Q3

clr led1
ldi mask,0b00100000

start:
     ;eor led1,mask
     ;out PORTB,led1
     call loop2
;     rcall clk1
loop2:
;ldi r17,0b00000000
       eor r27,r26         ;T xor Qn
      mov r20, r27             ; D
      mov r17,r20              ;Qn1  
       lsl r17
       lsl r17
       out PORTD,r17
       mov r27,r20             ;Qn
       rcall clk1
       cp led1,mask
       brne loop2
clk1:
w0:	sbi DDRB,5
     ldi r18,0b01000000	;this is delay (function)
         rcall PAUSE
         cbi DDRB,5
     ldi r18,0b01000000	;this is delay (function)
          rcall PAUSE
          ret

PAUSE:;this is delay (function)
lp2:	;loop runs 64 times
		IN r16, TIFR0 ;tifr is timer interupt flag (8 bit timer runs 256 times)
		ldi r17, 0b00000010
		AND r16, r17 ;need second bit
		BREQ PAUSE 
		OUT TIFR0, r17	;set tifr flag high
	dec r18
	brne lp2
	ret

