#include "Fw_global_config.h"   // This defines application specific charactersitics

#include <stdio.h>
#include "FreeRTOS.h"
#include "task.h"
#include "semphr.h"
#include "timers.h"
#include "RtosTask.h"

/*    Include the generic headers required for QORC */
#include "eoss3_hal_gpio.h"
#include "eoss3_hal_rtc.h"
#include "eoss3_hal_timer.h"
#include "eoss3_hal_fpga_usbserial.h"
#include "ql_time.h"
#include "s3x_clock_hal.h"
#include "s3x_clock.h"
#include "s3x_pi.h"
#include "dbg_uart.h"

#include "cli.h"


extern const struct cli_cmd_entry my_main_menu[];


const char *SOFTWARE_VERSION_STR;


/*
 * Global 
variable definition
 */


extern void qf_hardwareSetup();
static void nvic_init(void);
#define GPIO_OUTPUT_MODE (1)
#define GPIO_INPUT_MODE (0)
void PyHal_GPIO_SetDir(uint8_t gpionum,uint8_t iomode);
int PyHal_GPIO_GetDir(uint8_t gpionum);
int PyHal_GPIO_Set(uint8_t gpionum, uint8_t gpioval);
int PyHal_GPIO_Get(uint8_t gpionum);
#define A_PIN  4
#define Q_PIN  5  
#define d_PIN  22  //red led

int main(void)
{
    uint32_t A=0,Q=0;   //from ic 7474 pin  5  to vaman board 5 th  
    uint32_t d;    
    SOFTWARE_VERSION_STR = "qorc-onion-apps/qf_hello-fpga-gpio-ctlr";
    
    qf_hardwareSetup();
    nvic_init();

    dbg_str("\n\n");
    dbg_str( "##########################\n");
    dbg_str( "Quicklogic QuickFeather FPGA GPIO CONTROLLER EXAMPLE\n");
    dbg_str( "SW Version: ");
    dbg_str( SOFTWARE_VERSION_STR );
    dbg_str( "\n" );
    dbg_str(_DATE_ " "_TIME_ "\n" );
    dbg_str( "##########################\n\n");

    dbg_str( "\n\nHello GPIO!!\n\n");  // <<<<<<<<<<<<<<<<<<<<<  Change me!
    
    CLI_start_task( my_main_menu );
        HAL_Delay_Init();

    //LED pins Output
    PyHal_GPIO_SetDir(18,1);

    while(1)
    {
        //Test GPIO Code
        PyHal_GPIO_Set(18,1);//blue
        HAL_DelayUSec(2000000);
        PyHal_GPIO_Set(18,0);
        HAL_DelayUSec(2000000);
    }
    /* Start the tasks and timer running. */
    vTaskStartScheduler();
    dbg_str("\n");

    while(1);                               }

    CLI_start_task( my_main_menu );
  HAL_Delay_Init();
/***************START FLASH IMPL***********************/
PyHal_GPIO_SetDir(A_PIN,0); //Input
PyHal_GPIO_SetDir(Q_PIN,0); //Input

PyHal_GPIO_SetDir(d_PIN,1); //Output
while(1)
{
    d=(!A&&Q) || (!Q&&A);
     //Digital write 
     PyHal_GPIO_Set(d_PIN, d);
     //Digital Read
     A = PyHal_GPIO_Get(A_PIN);
     Q = PyHal_GPIO_Get(Q_PIN);
   

}
/***********************END flash IMPL********************************/
//     disp(7);  //display the number

    /* Start the tasks and timer running. */
    vTaskStartScheduler();
    dbg_str("\n");

    while(1);
}

static void nvic_init(void)
 {
    // To initialize system, this interrupt should be triggered at main.
    // So, we will set its priority just before calling vTaskStartScheduler(), not the time of enabling each irq.
    NVIC_SetPriority(Ffe0_IRQn, configLIBRARY_MAX_SYSCALL_INTERRUPT_PRIORITY);
    NVIC_SetPriority(SpiMs_IRQn, configLIBRARY_MAX_SYSCALL_INTERRUPT_PRIORITY);
    NVIC_SetPriority(CfgDma_IRQn, configLIBRARY_MAX_SYSCALL_INTERRUPT_PRIORITY);
    NVIC_SetPriority(Uart_IRQn, configLIBRARY_MAX_SYSCALL_INTERRUPT_PRIORITY);
    NVIC_SetPriority(FbMsg_IRQn, configLIBRARY_MAX_SYSCALL_INTERRUPT_PRIORITY);
 }
