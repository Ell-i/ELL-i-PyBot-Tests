#---------------------------------------------------------------------------------------------#
# ENCX24J600 Memory Organization                                                              #
#                                                                                             #
# Author: Asif Sardar <engr.asif.sardar@gmail.com>  2014                                      #
#---------------------------------------------------------------------------------------------#

'''
When SPI interface is used or selected ENCX24J600 Memory is organized into three areas:
1- Special Function Registers (SFR) Memory Address Space
2- Main Memory Address Space
3- Physical Registers (PHY) Memory Address Space

Refer to: ENCX24J600 Datasheet Section 3.0
'''

#---------------------------------SFR Memory Address Space------------------------------------#
'''
The linear 160 bytes SFR memory area is directly accessible to the user through banked
or unbanked SPI opcodes. The SFRs can be addressed as 4 banks of 32 bytes each directly
accessible through banked SPI opcodes, with an additional unbanked area of 32 bytes at
the end of the SFR memory. The SFRs can be directly accessible through 8-bit unbanked
addresses using unbanked SPI opcodes.
'''

#---------------------------------------------------------------------------------------------#

#---------------------------------Main Memory Address Space-----------------------------------#
'''
Main Memory Address Space:

'''
#---------------------------------------------------------------------------------------------#

#---------------------------------PHY Memory Address Space------------------------------------#
'''
PHY Memory Address Space:
'''
#---------------------------------------------------------------------------------------------#