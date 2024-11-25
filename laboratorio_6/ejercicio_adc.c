#include <stdint.h>
#include <stdbool.h>
#include "inc/tm4c1294ncpdt.h"
#include "inc/hw_memmap.h"
#include "driverlib/sysctl.h"
#include "driverlib/gpio.h"
#include "driverlib/uart.h"
#include "driverlib/pin_map.h"

void UART0_Config(void)
{
    // Habilitar periféricos UART0 y GPIOA
    SysCtlPeripheralEnable(SYSCTL_PERIPH_UART0);
    SysCtlPeripheralEnable(SYSCTL_PERIPH_GPIOA);

    // Configurar los pines PA0 y PA1 como UART
    GPIOPinConfigure(GPIO_PA0_U0RX);
    GPIOPinConfigure(GPIO_PA1_U0TX);
    GPIOPinTypeUART(GPIO_PORTA_BASE, GPIO_PIN_0 | GPIO_PIN_1);

    // Configurar UART: 9600 baud, 8 bits, sin paridad, 1 bit de parada
    UARTConfigSetExpClk(UART0_BASE, SysCtlClockGet(), 9600,
                        (UART_CONFIG_WLEN_8 | UART_CONFIG_STOP_ONE | UART_CONFIG_PAR_NONE));
}

int main(void)
{
    char buffer[4];
    uint32_t distance;

    // Configurar el reloj del sistema
    SysCtlClockFreqSet((SYSCTL_XTAL_25MHZ | SYSCTL_OSC_MAIN | SYSCTL_USE_PLL | SYSCTL_CFG_VCO_480), 120000000);

    // Configurar GPIO para los LEDs
    SysCtlPeripheralEnable(SYSCTL_PERIPH_GPION);
    SysCtlPeripheralEnable(SYSCTL_PERIPH_GPIOF);
    GPIOPinTypeGPIOOutput(GPIO_PORTN_BASE, 0x03); // PN0 y PN1
    GPIOPinTypeGPIOOutput(GPIO_PORTF_BASE, 0x10); // PF4

    // Configurar UART
    UART0_Config();

    while (1)
    {
        int index = 0;

        // Leer distancia desde UART
        while (UARTCharsAvail(UART0_BASE))
        {
            char c = UARTCharGet(UART0_BASE);

            if (c == '\n') // Fin del dato
            {
                buffer[index] = '\0';
                distance = atoi(buffer);
                break;
            }
            else
            {
                buffer[index++] = c;
            }
        }

        // Controlar los LEDs según la distancia
        if (distance > 10)
        {
            GPIOPinWrite(GPIO_PORTN_BASE, 0x03, 0x00);
            GPIOPinWrite(GPIO_PORTF_BASE, 0x10, 0x00);
        }
        else if (distance > 8)
        {
            GPIOPinWrite(GPIO_PORTN_BASE, 0x03, 0x02); // Enciende PN1
            GPIOPinWrite(GPIO_PORTF_BASE, 0x10, 0x00);
        }
        else if (distance > 6)
        {
            GPIOPinWrite(GPIO_PORTN_BASE, 0x03, 0x03); // Enciende PN1 y PN0
            GPIOPinWrite(GPIO_PORTF_BASE, 0x10, 0x00);
        }
        else if (distance > 4)
        {
            GPIOPinWrite(GPIO_PORTN_BASE, 0x03, 0x03); // Enciende PN1 y PN0
            GPIOPinWrite(GPIO_PORTF_BASE, 0x10, 0x10); // Enciende PF4
        }
        else
        {
            GPIOPinWrite(GPIO_PORTN_BASE, 0x03, 0x03); // Enciende PN1 y PN0
            GPIOPinWrite(GPIO_PORTF_BASE, 0x10, 0x10); // Enciende PF4
        }
    }
}
