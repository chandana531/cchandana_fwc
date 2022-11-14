*/                                           
//declaring the blink module
 module helloworldfpga(                        
      output wire redled,
   output wire greenled,                    
        output wire blueled                      
         );                                           
              wire clk;                                
                                                           
                qlal4s3b_cell_macro u_qlal4s3b_cell_macr    o (                                          
                 .Sys_Clk0 (clk),                     
 );
 
reg[26:0] delay;
 reg        led;            
 always@(posedge clk) begin          
 delay = delay+1; //incrementing the counter. 
                              
 //counts from 0 to 20000000 in 1 second      
                               
 //if(delay==27'b1001100010010110100000000) /    / blink delay in bits                        
  if(delay > 20000000) //blink delay in decima    l
  begin                                        
   delay=27'b0;
 led=!led; //reset the led                    
  end                                          
  end                                          
  //    assign blueled = led;     //If you wan    t to change led colour to blue,              
   assign redled = led; //If you want to change     led colour to red,
   
   //end of the module
     end module
     module flash(     
     input A,
    input B,
    output wire r,
);
    reg r.g;
    always@(A,B)
        begin
            r=(!A&&B) || (!B&&A);
            
    
    end
    endmodule
