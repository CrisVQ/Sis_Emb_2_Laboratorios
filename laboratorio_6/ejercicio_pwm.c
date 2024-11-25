#include <stdint.h>
#include <stdbool.h>
#include "inc/hw_ints.h"
#include "inc/hw_memmap.h"
#include "inc/hw_types.h"
#include "driverlib/debug.h"
#include "driverlib/gpio.h"
#include "driverlib/pin_map.h"
#include "driverlib/sysctl.h"
#include "driverlib/pwm.h"

uint32_t clockFreq;
volatile uint32_t width;

void setDutyCycle(uint32_t dutyCyclePercentage) {
    uint32_t period = PWMGenPeriodGet(PWM0_BASE, PWM_GEN_0);
    uint32_t pulseWidth = (dutyCyclePercentage * period) / 100;
    PWMPulseWidthSet(PWM0_BASE, PWM_OUT_1, pulseWidth);
}

int main(void)
{
    // Configuración del reloj del sistema
    clockFreq = SysCtlClockFreqSet((SYSCTL_OSC_MAIN | SYSCTL_USE_PLL | SYSCTL_XTAL_16MHZ | SYSCTL_CFG_VCO_480), 120000000);

    // Habilitar periféricos PWM0 y GPIOF
    SysCtlPeripheralEnable(SYSCTL_PERIPH_PWM0);
    SysCtlPeripheralEnable(SYSCTL_PERIPH_GPIOF);

    // Esperar hasta que los periféricos estén listos
    while (!SysCtlPeripheralReady(SYSCTL_PERIPH_PWM0)) {}
    while (!SysCtlPeripheralReady(SYSCTL_PERIPH_GPIOF)) {}

    // Configurar GPIOF para PWM y salida digital
    GPIOPinConfigure(GPIO_PF1_M0PWM1); // PF1 configurado como salida PWM
    GPIOPinTypePWM(GPIO_PORTF_BASE, GPIO_PIN_1); // Configurar PF1 como salida PWM
    GPIOPinTypeGPIOOutput(GPIO_PORTF_BASE, GPIO_PIN_2); // PF2 como salida GPIO

    // Configurar el generador de PWM
    PWMGenConfigure(PWM0_BASE, PWM_GEN_0, PWM_GEN_MODE_DOWN | PWM_GEN_MODE_NO_SYNC);
    PWMGenPeriodSet(PWM0_BASE, PWM_GEN_0, 400); // Periodo de PWM (400 ciclos)

    // Habilitar el generador de PWM y la salida PWM
    PWMGenEnable(PWM0_BASE, PWM_GEN_0);
    PWMOutputState(PWM0_BASE, PWM_OUT_1_BIT, true);

    // Duty cycles a probar
    uint32_t dutyCycles[] = {25, 45, 50, 75};
    uint32_t numCycles = sizeof(dutyCycles) / sizeof(dutyCycles[0]);

    // Bucle principal: cambiar duty cycle
    for (uint32_t i = 0; i < numCycles; i++) {
        setDutyCycle(dutyCycles[i]); // Configurar el duty cycle
        GPIOPinWrite(GPIO_PORTF_BASE, GPIO_PIN_2, GPIO_PIN_2); // Encender indicador
        SysCtlDelay(120000000); // Esperar 1 segundo (ajustar según necesidad)
        GPIOPinWrite(GPIO_PORTF_BASE, GPIO_PIN_2, 0); // Apagar indicador
    }

    // Finalizar el programa
    while (1) {
        GPIOPinWrite(GPIO_PORTF_BASE, GPIO_PIN_2, 0); // Asegurarse de que el indicador esté apagado
    }
}
