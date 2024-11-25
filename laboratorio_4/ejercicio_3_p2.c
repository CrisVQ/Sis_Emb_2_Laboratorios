#include <stdint.h>
#include <stdbool.h>
#include "inc/hw_ints.h"
#include "inc/hw_memmap.h"
#include "driverlib/gpio.h"
#include "driverlib/interrupt.h"
#include "driverlib/sysctl.h"
#include "driverlib/timer.h"

// Define timer periods for 1 second and 0.5 seconds
#define TIMER_PERIOD_1S (120000000 * 2)
#define TIMER_PERIOD_0_5S (120000000 * 0.5)

uint32_t timerPeriod = TIMER_PERIOD_1S; // Default timer period (1 second)
uint8_t led_index = 0;  // Index of the current LED to be turned on

void timer0A_handler(void);

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

    // Configure PJ0 as input with pull-up resistor for the switch
    GPIOPinTypeGPIOInput(GPIO_PORTJ_BASE, GPIO_PIN_0);
    GPIOPadConfigSet(GPIO_PORTJ_BASE, GPIO_PIN_0, GPIO_STRENGTH_2MA, GPIO_PIN_TYPE_STD_WPU); // Pull-up internal

    // Set the timer configuration
    TimerConfigure(TIMER0_BASE, TIMER_CFG_PERIODIC);
    TimerLoadSet(TIMER0_BASE, TIMER_A, timerPeriod - 1); // Load the timer with the period

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
        // Main loop does nothing; Timer interrupt handles LED sequence and timer period change
    }
}

void timer0A_handler(void)
{
    // Clear the timer interrupt
    TimerIntClear(TIMER0_BASE, TIMER_A);

    // Check the state of the switch to adjust the timer period
    if (GPIOPinRead(GPIO_PORTJ_BASE, GPIO_PIN_0) == 0) // Switch pressed (active-low)
    {
        timerPeriod = TIMER_PERIOD_0_5S; // Set timer period to 0.5 seconds
    }
    else
    {
        timerPeriod = TIMER_PERIOD_1S; // Set timer period to 1 second
    }

    // Update the timer period
    TimerLoadSet(TIMER0_BASE, TIMER_A, timerPeriod - 1);

    // Turn off all LEDs first
    GPIOPinWrite(GPIO_PORTN_BASE, GPIO_PIN_0 | GPIO_PIN_1, 0x00);  // Turn off PN0 and PN1
    GPIOPinWrite(GPIO_PORTF_BASE, GPIO_PIN_0 | GPIO_PIN_4, 0x00);  // Turn off PF0 and PF4

    // Turn on the current LED
    if (led_index == 0)
    {
        GPIOPinWrite(GPIO_PORTN_BASE, GPIO_PIN_0, GPIO_PIN_0);  // Turn on PN0
    }
    else if (led_index == 1)
    {
        GPIOPinWrite(GPIO_PORTN_BASE, GPIO_PIN_1, GPIO_PIN_1);  // Turn on PN1
    }
    else if (led_index == 2)
    {
        GPIOPinWrite(GPIO_PORTF_BASE, GPIO_PIN_0, GPIO_PIN_0);  // Turn on PF0
    }
    else if (led_index == 3)
    {
        GPIOPinWrite(GPIO_PORTF_BASE, GPIO_PIN_4, GPIO_PIN_4);  // Turn on PF4
    }

    // Update the LED index for the next interrupt
    led_index = (led_index + 1) % 4; // Increment and wrap around if necessary
}
