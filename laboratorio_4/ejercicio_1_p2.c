#include <stdint.h>
#include <stdbool.h>
#include "inc/hw_ints.h"
#include "inc/hw_memmap.h"
#include "driverlib/gpio.h"
#include "driverlib/interrupt.h"
#include "driverlib/pin_map.h"
#include "driverlib/sysctl.h"
#include "driverlib/timer.h"

uint32_t FS = 120000000 * 1;
void timer0A_handler(void);
uint8_t switch_state = 0;
uint32_t button = 0;

int main(void)
{
    // Clock Configuration
    SysCtlClockFreqSet((SYSCTL_XTAL_25MHZ | SYSCTL_OSC_MAIN | SYSCTL_USE_PLL | SYSCTL_CFG_VCO_480), 120000000);

    // Enable peripherals
    SysCtlPeripheralEnable(SYSCTL_PERIPH_GPION); // Enable GPIO N
    SysCtlPeripheralEnable(SYSCTL_PERIPH_GPIOF); // Enable GPIO F
    SysCtlPeripheralEnable(SYSCTL_PERIPH_GPIOJ); // Enable GPIO J
    SysCtlPeripheralEnable(SYSCTL_PERIPH_TIMER0); // Enable Timer 0

    // Configure GPIO pins as outputs for LEDs (PN0, PN1, PF0, PF4)
    GPIOPinTypeGPIOOutput(GPIO_PORTN_BASE, GPIO_PIN_0 | GPIO_PIN_1);
    GPIOPinTypeGPIOOutput(GPIO_PORTF_BASE, GPIO_PIN_0 | GPIO_PIN_4);
    
    // Configurar PJ0 como entrada con resistencia pull-up para el botón
    GPIOPinTypeGPIOInput(GPIO_PORTJ_BASE, GPIO_PIN_0);
    GPIOPadConfigSet(GPIO_PORTJ_BASE, GPIO_PIN_0, GPIO_STRENGTH_2MA, GPIO_PIN_TYPE_STD_WPU); // Pull-up interno

    // Set the timer configuration
    TimerConfigure(TIMER0_BASE, TIMER_CFG_PERIODIC);
    TimerLoadSet(TIMER0_BASE, TIMER_A, FS);

    // Register the interrupt handler for Timer 0A
    TimerIntRegister(TIMER0_BASE, TIMER_A, timer0A_handler);

    // Enable processor interrupts
    IntMasterEnable();

    // Enable timer interrupt
    IntEnable(INT_TIMER0A);
    TimerIntEnable(TIMER0_BASE, TIMER_TIMA_TIMEOUT);
    
    // Enable the timer
    TimerEnable(TIMER0_BASE, TIMER_A);

    while(1)
    {
        // Main loop can perform other tasks if needed
    }
}

void timer0A_handler(void)
{
    // Increment switch state
    switch_state++;

    // Check if the button on PJ0 is pressed
    if (GPIOPinRead(GPIO_PORTJ_BASE, GPIO_PIN_0) == 0)
    {
        button++;
    }

    // If the button has been pressed, change the timer delay
    if (button > 0)
    {
        FS = 120000000 * 2;
        TimerLoadSet(TIMER0_BASE, TIMER_A, FS);
    }

    if (button > 1)
    {
        FS = 120000000 * 5;
        TimerLoadSet(TIMER0_BASE, TIMER_A, FS);
    }

    // Clear the timer interrupt
    TimerIntClear(TIMER0_BASE, TIMER_A);

    // Sequence 1: Toggle LEDs
    if (switch_state % 2 != 0)
    {
        GPIOPinWrite(GPIO_PORTN_BASE, 0x03, 0x02);  // Turn on LED PN1
        GPIOPinWrite(GPIO_PORTF_BASE, 0x11, 0x01);  // Turn on LED PF0
    }
    if (switch_state % 2 == 0)
    {
        GPIOPinWrite(GPIO_PORTN_BASE, 0x03, 0x01);  // Turn on LED PN0
    }
}
