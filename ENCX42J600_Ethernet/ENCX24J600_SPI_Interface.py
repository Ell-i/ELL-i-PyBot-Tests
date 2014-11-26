#---------------------------------------------------------------------------------------------#
# ENCX24J600 SPI OpCodes                                                                      #
#                                                                                             #
# Author: Asif Sardar <engr.asif.sardar@gmail.com>  2014                                      #
#---------------------------------------------------------------------------------------------#

from ENCX24J600_Memory import *

#
# TO DO:
#

ENC_SPI_Opcodes = {
    'ENC_SPI_READ_REG'      : 0x00, # 0x00 - 0x1F
    'ENC_SPI_READ_REG_UB'   : 0x20,
    'ENC_SPI_WRITE_REG_UB'  : 0x22,
    'ENC_SPI_SET_BF_UB'     : 0x24,
    'ENC_SPI_CLR_BF_UB'     : 0x26,
    'ENC_SPI_READ_MEM'      : 0x28, # Through GP
    'ENC_SPI_WRITE_MEM'     : 0x2A, # Through GP
    'ENC_SPI_READ_RX'       : 0x2C,
    'ENC_SPI_WRITE_RX'      : 0x2E,
    'ENC_SPI_READ_UDA'      : 0x30,
    'ENC_SPI_WRITE_UDA'     : 0x32,
    'ENC_SPI_WRITE_REG'     : 0x40, # 0x40 - 0x5F
    'ENC_SPI_WRITE_GP_RDP'  : 0x60,
    'ENC_SPI_READ_GP_RDP'   : 0x62,

    'ENC_SPI_WRITE_RX_RDP'  : 0x64,
    'ENC_SPI_READ_RX_RDP'   : 0x66,
    'ENC_SPI_WRITE_UDA_RPT' : 0x68,
    'ENC_SPI_READ_UDA_RPT'  : 0x6A,
    'ENC_SPI_WRITE_GP_WRP'  : 0x6C,
    'ENC_SPI_READ_GP_WRP'   : 0x6E,
    'ENC_SPI_WRITE_RX_WRP'  : 0x70,
    'ENC_SPI_READ_RX_WRP'   : 0x72,
    'ENC_SPI_WRITE_UDA_WRP' : 0x74,
    'ENC_SPI_READ_UPDA_WRP' : 0x76,
    'ENC_SPI_SET_BF'        : 0x80, # 0x80-0x9F
    'ENC_SPI_CLR_BF'        : 0xA0, # 0xA0-0xBF
    'ENC_SPI_BANK0_SELECT'  : 0xC0,
    'ENC_SPI_BANK1_SELECT'  : 0xC2,
    'ENC_SPI_BANK2_SELECT'  : 0xC4,
    'ENC_SPI_BANK3_SELECT'  : 0xC6,
    'ENC_SPI_BANK_READ'     : 0xC8,
    'ENC_SPI_RESET'         : 0xCA,
    'ENC_SPI_SET_PKT_DEC'   : 0xCC,

    'ENC_SPI_DMA_STOP'      : 0xD2,
    'ENC_SPI_TX_REQUEST'    : 0xD4,
    'ENC_SPI_DMA_CKSUM'     : 0xD8,
    'ENC_SPI_DMA_CKSUM_S'   : 0xDA,
    'ENC_SPI_DMA_COPY'      : 0xDC,
    'ENC_SPI_DMA_COPY_S'    : 0xDE,
    'ENC_SPI_FC_DISABLE'    : 0xE0,
    'ENC_SPI_FC_SINGLE'     : 0xE2,
    'ENC_SPI_FC_MULTIPLE'   : 0xE4,
    'ENC_SPI_FC_CLEAR'      : 0xE6,
    'ENC_SPI_ENABLE_RX'     : 0xE8,
    'ENC_SPI_DISABLE_RX'    : 0xEA,
    'ENC_SPI_SET_EIE'       : 0xEC,
    'ENC_SPI_CLR_EIE'       : 0xEE,
}
