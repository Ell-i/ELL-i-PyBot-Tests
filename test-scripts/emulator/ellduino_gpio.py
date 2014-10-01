from ctypes import *

#-------------------------------------------------------------------------------------------#
# General purpose I/O ports: A,B,C,D & F                                                    #                                                                                                        #
# Each port: 16-bits mapping w.r.t array GPIOPIN[] in ../variants/ellduino/ellduino_gpio.h  #
#-------------------------------------------------------------------------------------------#

#-------------------------------------------------------------------------------------------#
# Port A                                                                                    #
#-------------------------------------------------------------------------------------------#
# DEFINE_GPIO_PIN(A,  0),        GPIOPIN[28]     # 60 PA0        A6
# DEFINE_GPIO_PIN(A,  1),        GPIOPIN[29]     # 61 PA1        A7
# DEFINE_GPIO_PIN(A,  2),        GPIOPIN[7]      #  7 PA2        D7
# DEFINE_GPIO_PIN(A,  3),        GPIOPIN[6]      #  6 PA3        D6
# DEFINE_GPIO_PIN(A,  4),        GPIOPIN[34]     # 66 PA4        DAC0
# DEFINE_GPIO_PIN(A,  5),        GPIOPIN[26]     # 58 PA5        A4
# DEFINE_GPIO_PIN(A,  6),        GPIOPIN[27]     # 59 PA6        A5
# DEFINE_GPIO_PIN(A,  7),        GPIOPIN[5]      #  5 PA7        D5
# DEFINE_GPIO_PIN(A,  8),        GPIOPIN[2]      #  2 PA8        D2
# DEFINE_GPIO_PIN(A,  9),        GPIOPIN[1]      #  1 PA9        D1      TX0
# DEFINE_GPIO_PIN(A, 10),        GPIOPIN[0]      #  0 PA10       D0      RX0
# DEFINE_GPIO_PIN(A, 11),        GPIOPIN[35]     # 67 PA11       DAC1
# DEFINE_GPIO_PIN(A, 12),        GPIOPIN[36]     # 68 PA12       CANRX
# DEFINE_GPIO_PIN(A, 13),        GPIOPIN[37]     # 69 PA13       CANTX   SWDAT
# DEFINE_GPIO_PIN(A, 14),        GPIOPIN[16]     # 16 PA14       TX2     SWCLK
# DEFINE_GPIO_PIN(A, 15),        GPIOPIN[10]     # 10 PA15       D10
ELLDUINO_GPIO_PORT_A = {
        0:  c_uint(28).value,
        1:  c_uint(29).value,
        2:  c_uint(7).value,
        3:  c_uint(6).value,
        4:  c_uint(34).value,
        5:  c_uint(26).value,
        6:  c_uint(27).value,
        7:  c_uint(5).value,
        8:  c_uint(2).value,
        9:  c_uint(1).value,
        10: c_uint(0).value,
        11: c_uint(35).value,
        12: c_uint(36).value,
        13: c_uint(37).value,
        14: c_uint(16).value,
        15: c_uint(10).value
}
#-------------------------------------------------------------------------------------------#

#-------------------------------------------------------------------------------------------#
# Port B                                                                                    #
#-------------------------------------------------------------------------------------------#
# DEFINE_GPIO_PIN(B,  0),        GPIOPIN[32]     # 64 PB0        A10
# DEFINE_GPIO_PIN(B,  1),        GPIOPIN[33]     # 65 PB1        A11
# DEFINE_GPIO_PIN(B,  3),        GPIOPIN[13]     # 13 PB3        Led B3 Amber "L"
# DEFINE_GPIO_PIN(B,  4),        GPIOPIN[12]     # 12 PB4        D12
# DEFINE_GPIO_PIN(B,  5),        GPIOPIN[11]     # 11 PB5        D11
# DEFINE_GPIO_PIN(B,  6),        GPIOPIN[18]     # 18 PB6        TX1
# DEFINE_GPIO_PIN(B,  7),        GPIOPIN[19]     # 19 PB7        RX1
# DEFINE_GPIO_PIN(B,  8),        GPIOPIN[21]     # 21 PB8        SCL
# DEFINE_GPIO_PIN(B,  9),        GPIOPIN[20]     # 20 PB9        SDA
# DEFINE_GPIO_PIN(B, 10),        GPIOPIN[8]      #  8 PB10       D8
# DEFINE_GPIO_PIN(B, 11),        GPIOPIN[9]      #  9 PB11       D9
# DEFINE_GPIO_PIN(B, 12),        GPIOPIN[40]     # 40 PB12       SPI2 NSS
ELLDUINO_GPIO_PORT_B = {
        0:  c_uint(32).value,
        1:  c_uint(33).value,
        3:  c_uint(13).value,
        4:  c_uint(12).value,
        5:  c_uint(11).value,
        6:  c_uint(18).value,
        7:  c_uint(19).value,
        8:  c_uint(21).value,
        9:  c_uint(20).value,
        10: c_uint(8).value,
        11: c_uint(9).value,
        12: c_uint(40).value
}
#-------------------------------------------------------------------------------------------#

#-------------------------------------------------------------------------------------------#
# Port C                                                                                    #
#-------------------------------------------------------------------------------------------#
# DEFINE_GPIO_PIN(C,  0),        GPIOPIN[22]             # 54 PC0        A0
# DEFINE_GPIO_PIN(C,  1),        GPIOPIN[23]             # 55 PC1        A1
# DEFINE_GPIO_PIN(C,  2),        GPIOPIN[24]             # 56 PC2        A2
# DEFINE_GPIO_PIN(C,  3),        GPIOPIN[25]             # 57 PC3        A3
# DEFINE_GPIO_PIN(C,  4),        GPIOPIN[30]             # 62 PC4        A8
# DEFINE_GPIO_PIN(C,  5),        GPIOPIN[31]             # 63 PC5        A9
# DEFINE_GPIO_PIN(C,  6),        GPIOPIN[14]             # 14 PC6        TX3
# DEFINE_GPIO_PIN(C,  7),        GPIOPIN[15]             # 15 PC7        RX3
# DEFINE_GPIO_PIN(C,  8),        GPIOPIN[4]              #  4 PC8        D4
# DEFINE_GPIO_PIN(C,  9),        GPIOPIN[3]              #  3 PC9        D3
ELLDUINO_GPIO_PORT_C = {
        0: c_uint(22).value,
        1: c_uint(23).value,
        2: c_uint(24).value,
        3: c_uint(25).value,
        4: c_uint(30).value,
        5: c_uint(31).value,
        6: c_uint(14).value,
        7: c_uint(15).value,
        8: c_uint(4).value,
        9: c_uint(3).value
}
#-------------------------------------------------------------------------------------------#

#-------------------------------------------------------------------------------------------#
# Port D                                                                                    #
#-------------------------------------------------------------------------------------------#
# DEFINE_GPIO_PIN(D,  2),        GPIOPIN[17]             # 17 PD2        RX2
ELLDUINO_GPIO_PORT_D = {
        2: c_uint(17).value
};
#-------------------------------------------------------------------------------------------#

#-------------------------------------------------------------------------------------------#
# Port F                                                                                    #
#-------------------------------------------------------------------------------------------#
# DEFINE_GPIO_PIN(F,  6),        GPIOPIN[39]             # 71 PF6  SCL1
# DEFINE_GPIO_PIN(F,  7),        GPIOPIN[38]             # 70 PF7  SDA1
ELLDUINO_GPIO_PORT_F = {
        6: c_uint(39).value,
        7: c_uint(38).value
}
#-------------------------------------------------------------------------------------------#

#-------------------------------------------------------------------------------------------#
ELLDUINO_GPIO = {
        'A': ELLDUINO_GPIO_PORT_A,
        'B': ELLDUINO_GPIO_PORT_B,
        'C': ELLDUINO_GPIO_PORT_C,
        'D': ELLDUINO_GPIO_PORT_D,
        'F': ELLDUINO_GPIO_PORT_F,
}
#-------------------------------------------------------------------------------------------#
