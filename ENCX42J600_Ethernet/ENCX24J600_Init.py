#---------------------------------------------------------------------------------------------#
# ENCX24J600 Initialization                                                                   #
#                                                                                             #
# Author: Asif Sardar <engr.asif.sardar@gmail.com>  2014                                      #
#---------------------------------------------------------------------------------------------#

from ENCX24J600_SFR_Adress_MAP import *
from ENCX24J600_SFR_EREG import *
from ENCX24J600_SFR_MACREG import *
#from ENCX42J600 import *

'''
NumPy is the fundamental package for scientific computing in Python.
Numpy supports a much greater variety of numerical types than Python does.
Refer to: http://docs.scipy.org/doc/numpy/user/index.html#user
'''
import numpy as np

'''
Initializing the SFR values according to the requirements
These values are then mapped/written to the ENCX24J600 Memory Organization
'''

encX24j600_init = [

	#
    # ENCX24J600 Datasheet Sestions 8.4 and 8.5: RX and TX buffers
    #
    # TX buffer -- not really needed, but we use for backwards compatibility
    encX24j600_register_init_static_16bit(np.uint8(ENC_Reg['E_TX_START']), np.uint16(TX_BUFFER_START)),
    encX24j600_register_init_static_16bit(np.uint8(ENC_Reg['E_TX_LEN']), np.uint16(TX_BUFFER_LEN)),

    # RX buffer
    encX24j600_register_init_static_16bit(np.uint8(ENC_Reg['E_RX_START']), np.uint16(RX_BUFFER_START)),
    # In E_RX_TAIL Register: Clear low-order bit for an even address
    encX24j600_register_init_static_16bit(np.uint8(ENC_Reg['E_RX_TAIL']), np.uint16(RX_BUFFER_END & ~0x01)),
    encX24j600_register_init_static_16bit(np.uint8(ENC_Reg['E_RX_HEAD']), np.uint16(RX_BUFFER_START)),
    encX24j600_register_init_static_16bit(np.uint8(ENC_Reg['E_RX_RD_PT']), np.uint16(RX_BUFFER_START)),


    #
    # ENCX24J600 Datasheet Section 8.5: Packet filtering
    #

    #
    # Hash-table not used
    #

    #
    # Filtering configuration.
    #
    encX24j600_register_init_static_16bit(np.uint8(ENC_Reg['E_RX_FCOND']),
    	np.uint16(
    		0
        	| ~ E_RX_FILTER_CON['HT_EN']	   # 0: Hash-table filter disabled
        	| ~ E_RX_FILTER_CON['MP_EN']       # 0: Magic packet filter disabled
        	| ~ E_RX_FILTER_CON['NOT_PM']      # 0: Patterh match checksum match required for a match
        	|   E_RX_FILTER_CON['PM_DISABLE']  # 0: Pattern matching filter disabled
        	| ~ E_RX_FILTER_CON['CRC_E_EN']    # 0: Filter disabled
        	|   E_RX_FILTER_CON['CRC_EN']      # 1: Packets with an invalid CRC will be discarded
        	| ~ E_RX_FILTER_CON['RUNT_E_EN']   # 0: Filter disabled
        	| ~ E_RX_FILTER_CON['RUNT_EN']     # 0: Discard packets that are 64 bytes or smaller
        	|   E_RX_FILTER_CON['UC_EN']       # 1: Unicast with my MAC received
        	| ~ E_RX_FILTER_CON['NOT_ME_EN']   # 0: Unicast without my MAC discarded
        	| ~ E_RX_FILTER_CON['MC_EN']       # 0: Multicast disabled
        	|   E_RX_FILTER_CON['BC_EN']       # 1: Broadcast enabled
        )
    ),

	#
    # ENCX24J600 Datasheet Section 8.6 MAC
    #
    encX24j600_register_init_static_16bit(np.uint8(ENC_Reg['MAC_CON1']),
    	np.uint16(
			0
			| ~ MAC_CON1['LOOP_BACK']   # 0: No loopback
			|   MAC_CON1['TX_PAUSE']    # 1: Allow sending pause control frames
			|   MAC_CON1['RX_PAUSE']    # 1: Adhere received pause control frames
			| ~ MAC_CON1['PASS_ALL']    # 0: Don't pass control frames to host
			|   MAC_CON1['RX_EN']       # 1: Enable the MAC
        )
    ),

	encX24j600_register_init_static_16bit(np.uint8(ENC_Reg['MAC_CON2']),
		np.uint16(
   			0
			| ~ MAC_CON2['DEFER']       # 0: Abort after excessive wait
			| ~ MAC_CON2['BP_EN']       # 0: Use binary backoff algorithm
			| ~ MAC_CON2['NO_BKOFF']    # 0: Use binary backoff algorithm
				# res  | ! LONG_PRE         # 0: Long preambles allowed
				# res  | ! PURE_PRE         # 0: Don't check preable contents
			|   MAC_CON2['PAD_VLAN']    # 101: Pad according to VLAN settings and add CRC
			|   MAC_CON2['TX_CRC_EN']   # 1: Enable CRC for Transmit
			| ~ MAC_CON2['P_HDR_EN']    # 0: No proprietary header
			| ~ MAC_CON2['HUGE_FRM_EN'] # 0: No huge frames
			|   MAC_CON2['FR_LEN_CHK']  # 1: Check frame lengths
			| ~ MAC_CON2['FULL_DUPLEX'] # 0: No full duplex (yet) XXX
		)
	),



	#
    # Control registers
    #
    encX24j600_register_init_static_16bit(np.uint8(ENC_Reg['E_CON2']),
    	np.uint16(
    		0
    		|   E_CON2['ETHEN']             # 1: Enable Ethernet
    		|   E_CON2['STRCH']             # 1: Stretch events on LEDs to 50 ms
    		| ~ E_CON2['TXMAC']             # 0: Do not insert source MAC address to outgoing packets
    		| ~ E_CON2['SHA1MD5']           # 1: Use SHA1 in the hashing engine
    		|   E_CON2['COCON_4000']        # 1011: 4 MHz
        		#
        		# NOTE!  Automatic flow control will not work, at least not with
        		#        some more configuration somewhere else.
        		#
        		#        Pekka tried to enable AUTOFC bit back in September 2014,
        		#        and ended up hunting for the resulting bug for several
        		#        days.  The symptom is that the activity LED flashes quickly
        		#        and the packet count in E_STAT does not get updated.
        		#
        	| ~ E_CON2['AUTOFC']            # 0: Enable automatic flow control
        	| ~ E_CON2['TX_RESET']          # 0: Normal operation
        	| ~ E_CON2['ENC_RX_STATUS_CARRIER_SEENET']          # 0: Normal operation
        	| ~ E_CON2['ETH_RESET']         # 0: Normal operation
        	|   E_CON2['MODLEN_512']        # 00: 512-bit exponential modulus and operands
        	|   E_CON2['AESLEN_128']        # 10: 128-bit AES
        )
	),

	encX24j600_register_init_static_16bit(np.uint8(ENC_Reg['E_INT_ENA']),
		np.uint16(
			0
			|   E_INT_ENA['INT_ENABLE']       # 1: Enable INT pin
			|   E_INT_ENA['PKT_IE']           # 1: Interrupt on pending packets
			| ~ E_INT_ENA['DMA_IE']           # 0: Disable DMA interrupt
			|   E_INT_ENA['LINK_IE']          # 1: Interrupt on link status change
			|   E_INT_ENA['TX_IE']            # 1: Interrupt on transmit ready
				# XXX  |   E_INT_ENA_WOL      # 1: Enable WOL pin
			| ~ E_INT_ENA['TX_ABT_IE']        # 0: Disable transmit error interrupts
			| ~ E_INT_ENA['RX_ABT_IE']        # 0: Disable receive error interrupts
		)
	),

	encX24j600_register_init_static_16bit(np.uint8(ENC_Reg['E_CON1']),
		np.uint16(
			0
			| ~ E_CON1['DMA_START']    # 0: Don't use DMA now
			| ~ E_CON1['TX_REQUEST']   # 0: Don't transmit yet
			|   E_CON1['RX_ENABLE']    # 1: Enable Receiving
		)
	),

]

#print encX24j600_init[6][0]
#print encX24j600_init[6][1]