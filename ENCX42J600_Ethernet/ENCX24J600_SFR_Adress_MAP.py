#---------------------------------------------------------------------------------------------#
# ENCX24J600 Special Function Register (SFR) Memory Address Map                               #
#                                                                                             #
# Author: Asif Sardar <engr.asif.sardar@gmail.com>  2014                                      #
#---------------------------------------------------------------------------------------------#

'''
Calling this function for the sake of clarity and documentation for ENCX42J600 SFR registers
'''
# Offset added to physical register addresses to fold them into the same address space
ENC_PHY_OFFSET = 0xA0 # See Table 3-1 on page 20.  0x9F is the last SPI SFR

def ENC_SFR_REG(number):
	return number
def ENC_PHY_REG(number):
	return (number +  ENC_PHY_OFFSET)
def ENC_IS_PHY_REG(number):
	return (number >= ENC_PHY_OFFSET)

# Macros for MII_STAT Register
def MII_STAT_NVALID():
	return 0x04
def MII_STAT_SCAN():
	return 0x02
def MII_STAT_BUSY():
	return 0x01
def PHY_CON1_PRST():
	return 0x8000
def PHY_CON1_PLOOPBK():
	return 0x4000
def PHY_CON1_PPWRSV():
	return 0x0800
def PHY_CON1_PDPXMD():
	return 0x0100
def PHY_STAT1_PFDPX():
	return 0x1000
def PHY_STAT1_PHDPX():
	return 0x0800
def PHY_STAT1_LLSTAT():
	return 0x0004
def PHY_STAT1_JBSTAT():
	return 0x0002
def PHY_CON2_FRCLINK():
	return 0x4000
def PHY_CON2_TXDIS():
	return 0x2000
def PHY_CON2_JABBER():
	return 0x0400
def PHY_CON2_HDLDIS():
	return 0x0100
'''
ENCX42J600 SFR register memory map addresses
'''
ENC_Reg = {
	'E_TX_START'  : ENC_SFR_REG(0x00),
    'E_TX_LEN'    : ENC_SFR_REG(0x02),
    'E_RX_START'  : ENC_SFR_REG(0x04),
    'E_RX_TAIL'   : ENC_SFR_REG(0x06),
    'E_RX_HEAD'   : ENC_SFR_REG(0x08),
    'E_DMA_START' : ENC_SFR_REG(0x0A),
    'E_DMA_LEN'   : ENC_SFR_REG(0x0C),
    'E_DMA_DST'   : ENC_SFR_REG(0x0E),
    'E_DMA_CS'    : ENC_SFR_REG(0x10),
    'E_TX_STAT'   : ENC_SFR_REG(0x12),
    'E_TX_WIRE'   : ENC_SFR_REG(0x14),
    'E_UDA_START' : ENC_SFR_REG(0x16),
    'E_UDA_END'   : ENC_SFR_REG(0x18),
    'E_STAT'      : ENC_SFR_REG(0x1A),
    'E_IR'        : ENC_SFR_REG(0x1C),
    'E_CON1'      : ENC_SFR_REG(0x1E),

    'E_HT1'       : ENC_SFR_REG(0x20),
    'E_HT2'       : ENC_SFR_REG(0x22),
    'E_HT3'       : ENC_SFR_REG(0x24),
    'E_HT4'       : ENC_SFR_REG(0x26),
    'E_PM_M1'     : ENC_SFR_REG(0x28),
    'E_PM_M2'     : ENC_SFR_REG(0x2A),
    'E_PM_M3'     : ENC_SFR_REG(0x2C),
    'E_PM_M4'     : ENC_SFR_REG(0x2E),
    'E_PM_CKSUM'  : ENC_SFR_REG(0x30),
    'E_PM_OFF'    : ENC_SFR_REG(0x32),
    'E_RX_FCOND'  : ENC_SFR_REG(0x34),

    'MAC_CON1'    : ENC_SFR_REG(0x40),
    'MAC_CON2'    : ENC_SFR_REG(0x42),
    'MAC_BBIPG'   : ENC_SFR_REG(0x44),
    'MAC_IPG'     : ENC_SFR_REG(0x46),
    'MAC_CL_CON'  : ENC_SFR_REG(0x48),
    'MAC_MAX_FL'  : ENC_SFR_REG(0x4A),

    'MII_CMD'     : ENC_SFR_REG(0x52),
    'MII_REG_ADR' : ENC_SFR_REG(0x54),

    'MAC_ADDR3'   : ENC_SFR_REG(0x60),
    'MAC_ADDR2'   : ENC_SFR_REG(0x62),
    'MAC_ADDR1'   : ENC_SFR_REG(0x64),
    'MII_WR'      : ENC_SFR_REG(0x66),
    'MII_RD'      : ENC_SFR_REG(0x68),
    'MII_STAT'    : ENC_SFR_REG(0x6A),

    'E_PAUSE'     : ENC_SFR_REG(0x6C),
    'E_CON2'      : ENC_SFR_REG(0x6E),
    'E_RX_WM'     : ENC_SFR_REG(0x70),
    'E_INT_ENA'   : ENC_SFR_REG(0x72),
    'E_ID_LED'    : ENC_SFR_REG(0x74),

    'E_GP_DATA'   : ENC_SFR_REG(0x80), # 8-bit register, ok to access as 16 bits
    'E_RX_DATA'   : ENC_SFR_REG(0x82), # 8-bit register, ok to access as 16 bits
    'E_UDA_DATA'  : ENC_SFR_REG(0x84), # 8-bit register, ok to access as 16 bits
    'E_GP_RD_PT'  : ENC_SFR_REG(0x86),
    'E_GP_WR_PT'  : ENC_SFR_REG(0x88),
    'E_RX_RD_PT'  : ENC_SFR_REG(0x8A),
    'E_RX_WR_PT'  : ENC_SFR_REG(0x8C),
    'E_UDA_RD_PT' : ENC_SFR_REG(0x8E),
    'E_UDA_WR_PT' : ENC_SFR_REG(0x90),

    'PHY_CON1 '   : ENC_PHY_REG(0x00),

    'PHY_STAT1'   : ENC_PHY_REG(0x01),

    'PHY_AN_A'    : ENC_PHY_REG(0x04),
    'PHY_AN_LPA'  : ENC_PHY_REG(0x05),
    'PHY_AN_E'    : ENC_PHY_REG(0x06),
    'PHY_CON2'    : ENC_PHY_REG(0x11),

    'PHY_STAT2'   : ENC_PHY_REG(0x1B),
    'PHY_STAT3'   : ENC_PHY_REG(0x1F),
}
