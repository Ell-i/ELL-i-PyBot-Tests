#---------------------------------------------------------------------------------------------#
# ENCX24J600 SFR E Registers                                                                  #
#                                                                                             #
# Author: Asif Sardar <engr.asif.sardar@gmail.com>  2014                                      #
#---------------------------------------------------------------------------------------------#

'''
Create tuple-like objects that have fields accessible by attribute lookup as well as being
indexable and iterable. It can be used synonym to C-type structs.
'''
from collections import namedtuple

MAX_PACKET_SIZE = 1536

ENC_BUFFER_START = 0x0000
ENC_BUFFER_SIZE  = 0x6000
ENC_BUFFER_END   = 0x5FFF

'''
Default value for start of Rx buffer, refer to: ENCX24J600 Datasheet Section 3.5.2
'''
RX_BUFFER_START = 0x5340
RX_BUFFER_END   = ENC_BUFFER_END
TX_BUFFER_LEN   = 0x2000
TX_BUFFER_END   = RX_BUFFER_START
TX_BUFFER_START = TX_BUFFER_END - TX_BUFFER_LEN

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

E_CON1 = {
    'MODEXST'      : 0x8000,
    'HASHEN'       : 0x4000,
    'HASHOP'       : 0x2000,
    'HASHLST'      : 0x1000,
    'AESST'        : 0x0800,
    'AES_DECRYPT'  : 0x0400,
    'AES_ENCRYPT'  : 0x0200,
    'AES_INIT'     : 0x0000,
    'PKT_DEC'      : 0x0100,
    'FC_END'       : 0x00C0,
    'FC_ENABLE'    : 0x0080,
    'FC_PAUSE'     : 0x0040,
    'FC_IDLE'      : 0x0000,
    'DMA_START'    : 0x0020,
    'DMAST'        : 0x0020,
    'DMACPY'       : 0x0010,
    'DMACSSD'      : 0x0008,
    'DMANOCS'      : 0x0004,
    'TX_REQUEST'   : 0x0002,
    'RX_ENABLE'    : 0x0001,
    'RXEN'         : 0x0001,
}

E_CON2 = {
    'ETHEN'        : 0x8000,
    'STRCH'        : 0x4000,
    'TXMAC'        : 0x2000,
    'SHA1MD5'      : 0x1000,
    'COCON_50'     : 0x0F00,
    'COCON_100'    : 0x0E00,
    'COCON_NONE1'  : 0x0D00,
    'COCON_3125'   : 0x0C00,
    'COCON_4000'   : 0x0B00,
    'COCON_5000'   : 0x0A00,
    'COCON_8000'   : 0x0800,
    'COCON_8333'   : 0x0700,
    'COCON_10000'  : 0x0600,
    'COCON_12500'  : 0x0500,
    'COCON_16666'  : 0x0400,
    'COCON_20000'  : 0x0300,
    'COCON_25000'  : 0x0200,
    'COCON_33333'  : 0x0100,
    'COCON_NONE0'  : 0x0000,
    'AUTOFC'       : 0x0080,
    'TX_RESET'     : 0x0040,
    'ENC_RX_STATUS_CARRIER_SEENET'    : 0x0020,
    'ETH_RESET'    : 0x0010,
    'MODLEN_1024'  : 0x0008,
    'MODLEN_768'   : 0x0004,
    'MODLEN_512'   : 0x0000,
    'AESLEN_256'   : 0x0002,
    'AESLEN_192'   : 0x0001,
    'AESLEN_128'   : 0x0000,
}

'''
ESTAT: Ethernet status register.  Page 93
'''
E_STAT = {
    'INT_PEND'     : 0x8000,
    'FC_STAT_IDLE' : 0x4000,
    'RX_BUSY'      : 0x2000,
    'CLOCK_READY'  : 0x1000,
    'PHY_DUPLEX'   : 0x0400,
    'PHY_LINK'     : 0x0100,
    'PKT_CNT_MASK' : 0x00ff,
};

E_RX_FILTER_CON = {
    'HT_EN'        : 0x8000,
    'MP_EN'       : 0x4000,
    'NOT_PM'       : 0x1000,
    'PM_MAGIC'     : 0x0900,
    'PM_HASHTABLE' : 0x0800,
    'PM_NOT_BCAST' : 0x0700,
    'PM_IS_BCAST'  : 0x0600,
    'PM_NOT_MCAST' : 0x0500,
    'PM_IS_MCAST'  : 0x0400,
    'PM_NOT_UCAST' : 0x0300,
    'PM_IS_UCAST'  : 0x0200,
    'PM_ALL'       : 0x0100,
    'PM_DISABLE'   : 0x0000,
    'CRC_E_EN'     : 0x0080,
    'CRC_EN'       : 0x0040,
    'RUNT_E_EN'    : 0x0020,
    'RUNT_EN'      : 0x0010,
    'UC_EN'        : 0x0008,
    'NOT_ME_EN'    : 0x0004,
    'MC_EN'        : 0x0002,
    'BC_EN'        : 0x0001,
};

E_INT_ENA = {
    'INT_ENABLE'   : 0x8000,
    'MODEX_IE'     : 0x4000,
    'HASH_IE'      : 0x2000,
    'AES_IE'       : 0x1000,
    'LINK_IE'      : 0x0800,
    'PKT_IE'       : 0x0040,
    'DMA_IE'       : 0x0020,
    'TX_IE'        : 0x0008,
    'TX_ABT_IE'    : 0x0004,
    'RX_ABT_IE'    : 0x0002,
    'PC_FULL'      : 0x0001,
}

enc_rx_packet_status = {
    'ENC_RX_STATUS_LONG_DROP'      : 0x0001,
    'ENC_RX_STATUS_CARRIER_SEEN'   : 0x0004,
    'ENC_RX_STATUS_CEC_ERROR'      : 0x0010,
    'ENC_RX_STATUS_LENGTH_ERROR'   : 0x0020,
    'ENC_RX_STATUS_LONG_TYPE'      : 0x0040,
    'ENC_RX_STATUS_RECEIVE_OK'     : 0x0080,
    'ENC_RX_STATUS_MULTICAST'      : 0x0100,
    'ENC_RX_STATUS_BROADCAST'      : 0x0200,
    'ENC_RX_STATUS_DRIBBLE'        : 0x0400,
    'ENC_RX_STATUS_CONTROL_FRAME'  : 0x0800,
    'ENC_RX_STATUS_PAUSE_FRAME'    : 0x1000,
    'ENC_RX_STATUS_UNKNOWN_OPCODE' : 0x2000,
    'ENC_RX_STATUS_VLAN_FRAME'     : 0x4000,
}

'''
np.uint16 enc_reg_value;
np.uint8  enc_buf_value;
np.uint64   enc_buf_len;
np.uint16 enc_phy_value;
'''
encX24j600_register_init_static_16bit = namedtuple("encX24j600_register_init_static_16bit", "enc_reg_address enc_reg_value")

# The above synonym to C-type struct can be used as:
# device_register_init_static_8bit_t = encX24j600_register_init_static_16bit(np.uint16(0), np.uint16(0))
# print device_register_init_static_8bit_t











