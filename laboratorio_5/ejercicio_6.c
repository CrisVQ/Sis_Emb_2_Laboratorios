#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>
#include <string.h>
#include "inc/hw_memmap.h"
#include "driverlib/debug.h"
#include "driverlib/gpio.h"
#include "driverlib/sysctl.h"
#include "driverlib/pin_map.h"
#include "driverlib/uart.h"
#include "utils/uartstdio.c"

void ConfigurarSistema(void);
void ConfigurarUART(void);
void ConfigurarGPIO(void);

int main(void)
{
    char receivedChar;

    ConfigurarSistema();
    ConfigurarGPIO();
    ConfigurarUART();

    while(1)
    {
        if(UARTCharsAvail(UART0_BASE))
        {
            receivedChar = UARTCharGet(UART0_BASE);
            if(receivedChar == '5')
            {
                GPIOPinWrite(GPIO_PORTN_BASE, GPIO_PIN_1, GPIO_PIN_1);
                SysCtlDelay((SysCtlClockGet() / 3) * 2);
                GPIOPinWrite(GPIO_PORTN_BASE, GPIO_PIN_1, 0);
            }
        }
    }
}

void ConfigurarSistema(void)
{
    SysCtlClockFreqSet((SYSCTL_XTAL_25MHZ | SYSCTL_OSC_MAIN | SYSCTL_USE_PLL | SYSCTL_CFG_VCO_480), 120000000);
}

void ConfigurarUART(void)
{
    SysCtlPeripheralEnable(SYSCTL_PERIPH_UART0);
    SysCtlPeripheralEnable(SYSCTL_PERIPH_GPIOA);
    GPIOPinConfigure(GPIO_PA0_U0RX);
    GPIOPinConfigure(GPIO_PA1_U0TX);
    GPIOPinTypeUART(GPIO_PORTA_BASE, GPIO_PIN_0 | GPIO_PIN_1);
    UARTStdioConfig(0, 9600, 120000000);
}

void ConfigurarGPIO(void)
{
    SysCtlPeripheralEnable(SYSCTL_PERIPH_GPION);
    GPIOPinTypeGPIOOutput(GPIO_PORTN_BASE, GPIO_PIN_1);
}
