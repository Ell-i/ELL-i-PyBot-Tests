#---------------------------------------------------------------------------------------------#
# ENCX24J600 SFR MAC Registers                                                                #
#                                                                                             #
# Author: Asif Sardar <engr.asif.sardar@gmail.com>  2014                                      #
#---------------------------------------------------------------------------------------------#

MAC_CON1 = {
    'LOOPBK'       : 0x10,
    'LOOP_BACK'    : 0x10,
    'TX_PAUSE'     : 0x08, # Marked as reserved, write as '1' in the data sheet
    'RXPAU'        : 0x04,
    'RX_PAUSE'     : 0x04,
    'PASSALL'      : 0x02,
    'PASS_ALL'     : 0x02,
    'RX_EN'        : 0x01, # Marked as reserved, write as '1' in the data sheet
}

MAC_CON2 = {
	'DEFER'        : 0x4000,
    'BPEN'         : 0x2000,
    'BP_EN'        : 0x2000,
    'NOBKOFF'      : 0x1000,
    'NO_BKOFF'     : 0x1000,
#  LONG_PRE       0x0200 reserved
#  PURE_PRE       0x0100 reserved

    'PAD_64'       : 0x00E0,
    'PAD_VLAN'     : 0x00A0,
    #             0x0060 is redunant
    'PAD_60'       : 0x0020,
    'PAD_NONE'     : 0x0000,
    'PADCFG_EN'    : 0x0020,

    'TXCRCEN'      : 0x0010,
    'TX_CRC_EN'    : 0x0010,
    'PHDREN'       : 0x0008,
    'P_HDR_EN'     : 0x0008,
    'HFRMEN'       : 0x0004,
    'HUGE_FRM_EN'  : 0x0004,
    'FR_LEN_CHK'   : 0x0002, # Reserved, must be written as '1'
    'FULDPX'       : 0x0001,
    'FULL_DUPLEX'  : 0x0001,
}

MII_CMD_SCAN = 0x02
MII_CMD_READ = 0x01



























