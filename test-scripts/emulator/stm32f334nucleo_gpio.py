from ctypes import *

#-------------------------------------------------------------------------------------------#
# General purpose I/O ports: A,B & C                                                        #                                                                                                        #
# Each port: 16-bits mapping w.r.t array GPIOPIN[] in 										#
# ../variants/stm32f334nucleo/stm32f334nucleo_gpio.h  									    #
#-------------------------------------------------------------------------------------------#

#-------------------------------------------------------------------------------------------#
# Port A -> stm32f334nucleo_gpio.h                                                          #
#-------------------------------------------------------------------------------------------#
# DEFINE_GPIO_PIN(A,  0),   /* 54 PA0  A0  ADC1_1 */
# DEFINE_GPIO_PIN(A,  1),   /* 55 PA1  A1  ADC1_2 */
# DEFINE_GPIO_PIN(A,  2),   /*  1 PA2  D1 TX2 */
# DEFINE_GPIO_PIN(A,  3),   /*  0 PA3  D0 RX2 */
# DEFINE_GPIO_PIN(A,  4),   /* 56 PA4  A2  ADC2_1 */
# DEFINE_GPIO_PIN(A,  5),   /* 13 PA5                  SPI1_SCK */
# DEFINE_GPIO_PIN(A,  6),   /* 12 PA6  D12             SPI1_MISO */
# DEFINE_GPIO_PIN(A,  7),   /* 11 PA7  D11 TIM17_CH1 / SPI1_MOSI */
# DEFINE_GPIO_PIN(A,  8),   /*  7 PA8  D7 */
# DEFINE_GPIO_PIN(A,  9),   /*  8 PA9  D8 */
# DEFINE_GPIO_PIN(A,  10),  /*  2 PA10 D2 */
STM32F334NUCLEO_GPIO_PORT_A = {
		0:  c_uint(54).value,
        1:  c_uint(55).value,
        2:  c_uint(1).value,
        3:  c_uint(0).value,
        4:  c_uint(56).value,
        5:  c_uint(13).value,
        6:  c_uint(12).value,
        7:  c_uint(11).value,
        8:  c_uint(7).value,
        9:  c_uint(8).value,
        10: c_uint(2).value
}
#-------------------------------------------------------------------------------------------#

#-------------------------------------------------------------------------------------------#
# Port B -> stm32f334nucleo_gpio.h                                                          #
#-------------------------------------------------------------------------------------------#
# DEFINE_GPIO_PIN(B,  0),   /* 57 PB0  A3  ADC1_11 */
# DEFINE_GPIO_PIN(B,  3),   /*  3 PB3  D3 TIM2_CH2 */
# DEFINE_GPIO_PIN(B,  4),   /*  5 PB3  D5 TIM3_CH1 */
# DEFINE_GPIO_PIN(B,  5),   /*  4 PB5  D4 */
# DEFINE_GPIO_PIN(B,  6),   /* 10 PB6  D10 TIM16_CH1n  / SPI1_CS */
# DEFINE_GPIO_PIN(B,  8),   /* 15 PB8  D15 I2C1_SCL */
# DEFINE_GPIO_PIN(B,  9),   /* 14 PB9  D14 I2C1_SDA */
# DEFINE_GPIO_PIN(B, 10),   /*  6 PB10 D6 TIM2_CH3 */
#ifdef FEATURE_NUCLEO_ANALOG45_I2C
# DEFINE_GPIO_PIN(B,  8),   /* 59 PB8  A5  I2C1_SCL */
# DEFINE_GPIO_PIN(B,  9),   /* 58 PB9  A4  I2C1_SDA */
STM32F334NUCLEO_GPIO_PORT_B = {
		0:  c_uint(57).value,
        3:  c_uint(3).value,
        4:  c_uint(5).value,
        5:  c_uint(4).value,
        6:  c_uint(10).value,
        8:  c_uint(15).value,
        9:  c_uint(14).value,
        #8:  c_uint(59).value,
        #9:  c_uint(58).value,
        10: c_uint(6).value
}
#-------------------------------------------------------------------------------------------#

#-------------------------------------------------------------------------------------------#
# Port C -> stm32f334nucleo_gpio.h                                                          #
#-------------------------------------------------------------------------------------------#
#else
# DEFINE_GPIO_PIN(C,  0),   /* 59 PC0  A5  ADC1_6 */
# DEFINE_GPIO_PIN(C,  1),   /* 58 PC1  A4  ADC1_7*/
#endif
# DEFINE_GPIO_PIN(C,  7),   /*  9 PC7  D9 TIM3_CH2 */
STM32F334NUCLEO_GPIO_PORT_C = {
		0:  c_uint(59).value,
        1:  c_uint(58).value,
        7:  c_uint(9).value
}
#-------------------------------------------------------------------------------------------#

#-------------------------------------------------------------------------------------------#
STM32F334NUCLEO_GPIO = {
        'A': STM32F334NUCLEO_GPIO_PORT_A,
        'B': STM32F334NUCLEO_GPIO_PORT_B,
        'C': STM32F334NUCLEO_GPIO_PORT_C
}
#-------------------------------------------------------------------------------------------#
