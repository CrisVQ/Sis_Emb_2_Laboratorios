//*****************************************************************************
//
// blinky_binary_counter.c - Binary counter using LEDs and buttons.
//
//*****************************************************************************

#include <stdint.h>
#include <stdbool.h>
#include "inc/hw_memmap.h"
#include "driverlib/sysctl.h"
#include "driverlib/gpio.h"

//*****************************************************************************
//
// Function to update LEDs based on the binary value of the counter.
//
//*****************************************************************************
void updateLEDs(int counter)
{
    // Control LEDs según el bit correspondiente del contador
    GPIOPinWrite(GPIO_PORTN_BASE, GPIO_PIN_1, (counter & 0x1) ? GPIO_PIN_1 : 0);  // LED 1 on PN1 (LSB)
    GPIOPinWrite(GPIO_PORTN_BASE, GPIO_PIN_0, (counter & 0x2) ? GPIO_PIN_0 : 0);  // LED 2 on PN0
    GPIOPinWrite(GPIO_PORTF_BASE, GPIO_PIN_4, (counter & 0x4) ? GPIO_PIN_4 : 0);  // LED 3 on PF4
    GPIOPinWrite(GPIO_PORTF_BASE, GPIO_PIN_0, (counter & 0x8) ? GPIO_PIN_0 : 0);  // LED 4 on PF0 (MSB)
}

//*****************************************************************************
//
// Main entry point for binary counter with LEDs.
//
//*****************************************************************************
int main(void)
{
    uint32_t delay = (120000000 / 3) * 0.3; // Delay similar to debounce
    int counter = 0;

    // Configure the system clock to 120 MHz
    SysCtlClockFreqSet((SYSCTL_XTAL_25MHZ | SYSCTL_OSC_MAIN | SYSCTL_USE_PLL | SYSCTL_CFG_VCO_480), 120000000);

    // Enable the GPIO ports for LEDs and buttons
    SysCtlPeripheralEnable(SYSCTL_PERIPH_GPION); // LEDs on port N (PN0, PN1)
    SysCtlPeripheralEnable(SYSCTL_PERIPH_GPIOF); // LEDs on port F (PF0, PF4)
    SysCtlPeripheralEnable(SYSCTL_PERIPH_GPIOJ); // Buttons on port J (PJ0, PJ1)

    // Wait until peripherals are ready
    while (!SysCtlPeripheralReady(SYSCTL_PERIPH_GPION)) {}
    while (!SysCtlPeripheralReady(SYSCTL_PERIPH_GPIOF)) {}
    while (!SysCtlPeripheralReady(SYSCTL_PERIPH_GPIOJ)) {}

    // Set LED pins as output
    GPIOPinTypeGPIOOutput(GPIO_PORTN_BASE, GPIO_PIN_0 | GPIO_PIN_1); // LEDs PN0, PN1
    GPIOPinTypeGPIOOutput(GPIO_PORTF_BASE, GPIO_PIN_0 | GPIO_PIN_4); // LEDs PF0, PF4

    // Set button pins as input with pull-up resistors
    GPIOPinTypeGPIOInput(GPIO_PORTJ_BASE, GPIO_PIN_0 | GPIO_PIN_1);
    GPIOPadConfigSet(GPIO_PORTJ_BASE, GPIO_PIN_0 | GPIO_PIN_1, GPIO_STRENGTH_2MA, GPIO_PIN_TYPE_STD_WPU);

    // Initialize LEDs to current counter state
    updateLEDs(counter);

    // Main loop
    while (1)
    {
        // Button to increment (PJ0)
        if (GPIOPinRead(GPIO_PORTJ_BASE, GPIO_PIN_0) == 0)
        {
            if (counter < 15) // Counter max is 15 (4 bits)
            {
                counter++;
                updateLEDs(counter);
                SysCtlDelay(delay); // Debounce delay
            }
        }

        // Button to decrement (PJ1)
        if (GPIOPinRead(GPIO_PORTJ_BASE, GPIO_PIN_1) == 0)
        {
            if (counter > 0)
            {
                counter--;
                updateLEDs(counter);
                SysCtlDelay(delay); // Debounce delay
            }
        }

        SysCtlDelay(delay); // General delay between reads
    }
}
