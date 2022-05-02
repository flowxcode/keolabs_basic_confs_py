# This code and associated information is provided to guide KEOLABS'
# customers in their use of KEOLABS' testing tools. KEOLABS shall not be
# liable for any direct, indirect or consequential damages with respect
# to claims arising from the content and/or its use by the KEOLABS' customers.
# For more information, refer to KEOLABS Sales Conditions at www.keolabs.com.

"""
Collection of functions ans constants to use ProxiLAB automation model
This file has been generated with ProxiLAB software version 4.42.19.0111
"""

import win32com.client
import pythoncom

def CreateObject():
    # Create ProxiLAB COM object
    return win32com.client.Dispatch("KEOLABS.ProxiLAB")

def StartSpy(tool):
    # ProxiLAB Start Spy
    tool.Spy.Start()

def StopSpy(tool):
    # ProxiLAB Stop Spy
    tool.Spy.Stop()
    tool.Spy.Analyzer.Start()

def CreateVARIANT():
    return win32com.client.VARIANT(pythoncom.VT_BYREF|pythoncom.VT_ARRAY|pythoncom.VT_I1,[0]*4096)

def CreateVARIANT_LONG():
    return win32com.client.VARIANT(pythoncom.VT_BYREF|pythoncom.VT_ARRAY|pythoncom.VT_I4,[0]*4096)

def CreateVARIANT_ULONG():
    return win32com.client.VARIANT(pythoncom.VT_BYREF|pythoncom.VT_ARRAY|pythoncom.VT_UI4,[0]*4096)

def CreateVARIANT_DOUBLE():
    return win32com.client.VARIANT(pythoncom.VT_BYREF|pythoncom.VT_ARRAY|pythoncom.VT_R8,[0]*4096)

class Constants:


    #ProxiLAB error codes
    #TAG_ERR_CODE_START (tag used by MissingErrorCode.js)
    
    ERR_SUCCESSFUL                      = 0x0000 #0	#
    NO_ERR                              = 0x0000 #0
    
    #== Reader errors ===========================================================
    XSMRDR_ERR_RF                        = 0x0001 #!< Error 001 : An error occured during RF field setup.	##ERROR : An error occured during RF field setup.
    XSMRDR_ERR_BREAK                     = 0x0002 #!< Error 002 : An error occured during PICC frame reception.	##ERROR : An error occured during PICC frame reception.
    XSMRDR_ERR_CRC                       = 0x0003 #!< Error 003 : Wrong frame checksum received.	##ERROR : Wrong frame checksum received.
    XSMRDR_ERR_PARITY                    = 0x0004 #!< Error 004 : Wrong frame parity bit received.	##ERROR : Wrong frame parity bit received.
    XSMRDR_ERR_TIMEOUT                   = 0x0005 #!< Error 005 : PICC response timed out.	##ERROR : PICC response timed out.
    XSMRDR_ERR_PCSC_INTERFACE_ENABLED    = 0x0006 #!< Error 006 : PCSC interface already active.	##ERROR : PC/SC interface enabled.
    XSMRDR_ERR_TIMEOUT_PICC_SOF_DETECTED = 0x0007 #!< Error 007 : PICC SOF detected but no response.	##ERROR : PICC SOF detected but no response.
    XSMRDR_ERR_PICC_EOF                  = 0x0008 #!< Error 008 : PICC is transmitting.	#
    XSMRDR_ERR_RF_ON_FDET                = 0x0009 #!< Error 009 : ISO18092: Impossible to turn field on: another field was detected.	##ERROR : ISO18092: Impossible to turn field on: another field was detected.
    XSMRDR_ERR_SOFT_TIMEOUT              = 0x000A #!< Error 00A : No PICC response EOF detected (soft time out).	##ERROR : No PICC response EOF detected (soft time out).
    
    #== XSmart driver errors ====================================================
    XSMLIB_ERR_TIMEOUT                = 100  #!< Error 100 : No PCD response.	##ERROR : No PCD response.
    XSMLIB_ERR_CONNEXION              = 101  #!< Error 101 : An error occured during PCD connexion.	##ERROR : An error occured during PCD connexion.
    XSMLIB_ERR_READ_REG               = 102  #!< Error 102 : The read of a PCD register failed.	##ERROR : PCD register read failed.
    XSMLIB_ERR_UPDATE_REG             = 103  #!< Error 103 : The update of a PCD register failed.	##ERROR : PCD register update failed.
    XSMLIB_ERR_READ_FIFO              = 104  #!< Error 104 : The read of a PCD FIFO memory failed.	##ERROR : PCD FIFO memory read failed.
    XSMLIB_ERR_UPDATE_FIFO            = 105  #!< Error 105 : The update of a PCD FIFO memory failed.	##ERROR : PCD FIFO memory upadte failed.
    
    XSMLIB_ERR_PICC_NOT_ISO           = 106  #!< Error 106 : PICC is not compliant with ISO14443 standard.	##ERROR : PICC is not compliant with ISO14443 standard.
    XSMLIB_ERR_NOT_ENOUGH_POWER       = 107  #!< Error 107 : PICC needs more power to process command.	##ERROR : PICC needs more power to process command.
    XSMLIB_ERR_PROTOCOL               = 108  #!< Error 108 : A protocol error occured during frame exchange.	##ERROR : A protocol error occured during frame exchange.
    XSMLIB_ERR_NO_CID_AVAILABLE       = 109  #!< Error 109 : No more card identifier is available.	##ERROR : No more card identifier is available.
    XSMLIB_ERR_BAUDRATE_NOT_AVAILABLE = 110  #!< Error 110 : PCD or PICC do not support specified baud rates.	##ERROR : PCD or PICC do not support specified baud rates.
    XSMLIB_ERR_ATS_ERRONOUS           = 111  #!< Error 111 : Received PICC Answer to Select is erronous.	##ERROR : Received PICC Answer to Select is incorrect.
    XSMLIB_ERR_BLOCK_RECEPTION        = 112  #!< Error 112 : An error occured during a T=CL block exchange.	##ERROR : An error occured during T=CL block exchange.
    XSMLIB_ERR_PROXI_SECU             = 113  #!< Error 113 : This functionnality is only available on security profil.	##ERROR : This functionnality is only available on security profil.
    XSMLIB_ERR_PICC_TEST_SERIES       = 114  #!< Error 114 : This functionnality is only available with the option AnaTestSeries.	##ERROR : This functionnality is only available with the option AnaTestSeries.
    
    XSMLIB_ERR_READ_EEPROM            = 115  #!< Error 115 : The read of the EEPROM failed.	##ERROR : EEPROM read failed.
    XSMLIB_ERR_UPDATE_EEPROM          = 116  #!< Error 116 : The update of the EEPROM failed.	##ERROR : EEPROM update failed.
    
    #== Library parameters errors ===============================================
    XSMLIB_ERR_READER_NOT_INSTANTIATED     = 200 #!< Error 200 : Reader object not instantiated.	##ERROR : Reader object not instantiated.
    XSMLIB_ERR_BAD_PARAM                   = 201 #!< Error 201 : Bad parameter transmitted.	##ERROR : Bad parameter transmitted.
    XSMLIB_ERR_BUFFER_LENGTH               = 202 #!< Error 202 : Buffer length not supported.	##ERROR : Buffer length not supported.
    XSMLIB_ERR_REG_RDWR_MODE_NOT_SUPPORTED = 203 #!< Error 203 : PCD register Read	##ERROR : PCD register Read/Write mode not supported.
    XSMLIB_ERR_RF_POWER_ON_OFF             = 204 #!< Error 204 : RF power switch mode not supported.	##ERROR : RF power switch mode not supported.
    XSMLIB_ERR_RF_POWER_NOT_SUPPORTED      = 205 #!< Error 205 : RF field strength not supported.	##ERROR : RF field strength not supported.
    XSMLIB_ERR_RF_RATE_NOT_SUPPORTED       = 206 #!< Error 206 : RF modulation rate not supported.	##ERROR : RF modulation rate not supported.
    XSMLIB_ERR_CARD_TYPE_ERRONOUS          = 207 #!< Error 207 : Card protocol type not supported.	##ERROR : Card protocol type not supported.
    XSMLIB_ERR_FRAME_TYPE_ERRONOUS         = 208 #!< Error 208 : Frame type not supported.	##ERROR : Frame type not supported.
    XSMLIB_ERR_NB_BIT_NOT_SUPPORTED        = 209 #!< Error 209 : Number of bits not supported.	##ERROR : Number of bits not supported.
    XSMLIB_ERR_NB_SLOTS_NOT_SUPPORTED      = 210 #!< Error 210 : Number of anti-collision slots not supported.	##ERROR : Number of anti-collision slots not supported.
    XSMLIB_ERR_SLOT_NOT_SUPPORTED          = 211 #!< Error 211 : Anti-collision slot number not supported.	##ERROR : Anti-collision slot number not supported.
    XSMLIB_ERR_CID_ERRONOUS                = 212 #!< Error 212 : Card identifier value not supported.	##ERROR : Card identifier value not supported.
    XSMLIB_ERR_CID_ALREADY_AFFECTED        = 213 #!< Error 213 : Card identifier already affected.	##ERROR : Card identifier already affected.
    XSMLIB_ERR_BAUDRATE_NOT_SUPPORTED      = 214 #!< Error 214 : Protocol baud rate not supported.	##ERROR : Protocol baud rate not supported.
    XSMLIB_ERR_CMD_LENGTH_NOT_SUPPORTED    = 215 #!< Error 215 : PICC do not support INF field length.	##ERROR : PICC do not support INF field length.
    XSMLIB_ERR_FSDI_NOT_SUPPORTED          = 216 #!< Error 216 : PCD do not support frame size.	##ERROR : PCD do not support frame size.
    XSMLIB_ERR_STACK_OVERFLOW              = 217 #!< Error 217 : A sequencer stack overflow occured.	##ERROR : A sequencer stack overflow occured.
    XSMLIB_CHAINING_MODE_NOT_SUPPORTED     = 218 #!< Error 218 : Chaining mode not supported.	##ERROR : Chaining mode not supported.
    XSMLIB_CHAINING_MODE_NOT_ALLOWED       = 219 #!< Error 219 : This functionnality do not support chaining mode.	##ERROR : This functionnality do not support chaining mode.
    XSMLIB_INTER_CMD_MODE_NOT_SUPPORTED    = 220 #!< Error 220 : Inter-command mode not supported.	##ERROR : Inter-command mode not supported.
    XSMLIB_INTER_CMD_MODE_NOT_ALLOWED      = 221 #!< Error 221 : This functionnality do not support inter-command mode.	##ERROR : This functionnality do not support inter-command mode.
    XSMLIB_INTER_CMD_MODE_MANDATORY        = 222 #!< Error 222 : This functionnality requires inter-command mode enabled.	##ERROR : This functionnality requires inter-command mode enabled.
    XSMLIB_ERR_TRIGGER_ID_NOT_SUPPORTED    = 223 #!< Error 223 : Trigger identifier not supported.	##ERROR : Trigger identifier not supported.
    XSMLIB_ERR_I2C_NAK                     = 224 #!< Error 224 : I2C device does not answer	##ERROR : No I2C device answer.
    XSMLIB_CHAINING_RESP_NOT_AVAILABLE     = 225 #!< Error 225 : In chaining mode the response buffer is not available.	##Warning : In chaining mode, the response buffer is not available.
    XSMLIB_ISO18092_MODE_NOT_SUPPORTED     = 226 #!< Error 226 : ISO18092 mode not supported.	##ERROR : ISO18092 mode not supported.
    XSMLIB_ERR_RF_POWER_OFF                = 227 #!< Error 227 : RF power is off.	##ERROR : RF power is off.
    
    #PLL Synthesizer
    ERR_CLK_PLL_WARNING                 = 0x1100 #4352	#: /TODO
    ERR_CLK_PLL_ERROR                   = 0x1101 #4353	#: 
    
    ERR_FAILURE                         = 0x1501 #5377	##ERROR : Undefined error code.
    ERR_DEVICE_NOT_CONNECTED            = 0x1502 #5378	##ERROR : ProxiLAB is not connected.
    ERR_I2C_NAK                         = 0x1503 #5379	##ERROR : I2C NAK.
    ERR_TIMEOUT                         = 0x1504 #5380	##ERROR : Timeout.
    ERR_TOOL_PATH_NOT_FOUND             = 0x1506 #5382	##ERROR : Tool path not found.
    ERR_FILE_NOT_FOUND                  = 0x1507 #5383	##ERROR : File not found.
    ERR_UNABLE_TO_CREATE_FILE           = 0x1508 #5384	##ERROR : Unable to create file.
    ERR_VHDL_READ_FAILED                = 0x150A #5386	##ERROR : Failed to read register.
    ERR_VHDL_WRITE_FAILED               = 0x150B #5387	##ERROR : Failed to write register.
    ERR_DIV_0                           = 0x150C #5388	##ERROR : Division by zero.
    ERR_OBJECT_NOT_CREATED              = 0x150D #5389	##ERROR : Object not created.
    ERR_FPGA_BITSTREAM_NOT_FOUND        = 0x150E #5390	##ERROR : FPGA bitstream not found.
    ERR_XSC_FILE_NOT_FOUND              = 0x150F #5391	##ERROR : Configuration file not found.
    ERR_NB_READ_TOO_BIG                 = 0x1510 #5392	#: /TODO
    ERR_RGPA_IS_NOT_RUNNING             = 0x1511 #5393	##ERROR : RGPA is not running.
    ERR_ANALYZER_IS_RUNNING             = 0x1512 #5394	##ERROR : Analyzer is already running.
    ERR_PROPERTY_NOT_FOUND              = 0x1513 #5395	##ERROR : Property not found.
    ERR_BAD_PARAMETER                   = 0x1514 #5396	##ERROR : Wrong parameter.
    ERR_NOT_IMPLEMENTED                 = 0x1515 #5397	##ERROR : SOFT: Function to be implemented.
    ERR_SENT_BUFFER_TOO_SHORT           = 0x1516 #5398	##ERROR : The sent buffer is too short.
    ERR_SENT_BUFFER_TOO_LONG            = 0x1517 #5399	##ERROR : The sent buffer is too long.
    ERR_BUFFER_SIZE_IS_ZERO             = 0x1518 #5400	##ERROR : Buffer size is null.
    ERR_BUFFER_TOO_SHORT                = 0x1519 #5401	##ERROR : Buffer too short.
    ERR_BAD_FILE_FORMAT                 = 0x151A #5402	##ERROR : Wrong file format.
    ERR_INVALID_FILE                    = 0x151B #5403	##ERROR : Wrong file contents.
    ERR_LOADING_FPGA                    = 0x151C #5404	#
    ERR_BAD_PROXILAB_VERSION            = 0x151D #5405	##ERROR : Function not supported with this ProxiLAB version.
    ERR_EEPROM_NOT_PROGRAMMED           = 0x151E #5406	##ERROR : EEPROM not programmed.
    ERR_EEPROM_CONTENT_NOT_VALID        = 0x151F #5407	##ERROR : EEPROM content not valid.
    ERR_CHAINING_FAILED					= 0x1520 #5408	#
    
    #Reader
    ERR_NO_FRAME_AVAILABLE              = 0x2001 #8193	##ERROR : No frame available.
    ERR_WRONG_SIZE_DECLARED             = 0x2002 #8194	##ERROR : Size declared in frame does not correspond to frame size.
    ERR_WRONG_FRAME_SIZE_RECEIVED       = 0x2003 #8195	##ERROR : Received frame size is incorrect.
    ERR_NEED_TO_COMPUTE_WF              = 0x2004 #8196	##ERROR : Waveform tables need to be recomputed.
    ERR_WRONG_UID_SIZE                  = 0x2005 #8197	##ERROR : UID size is wrong (must be 8 bytes).
    
    #Reader.ISO18092
    ERR_RDR_ISO18092_DISABLED           = 0x2101 #8449	##ERROR : Reader.ISO18092: initiator is disabled (Please set ProxiLAB.Reader.ISO18092.Enable = 1).
    ERR_RDR_ISO18092_FRAME_FORMAT       = 0x2102 #8450	##ERROR : Reader.ISO18092: wrong initiator frame format.
    
    #Reader.JISX6319
    ERR_READ_JISX6319_FAILED            = 0x2201 #8705	##ERROR : Reader.JISX6319: failed to read.
    ERR_WRITE_JISX6319_FAILED           = 0x2202 #8706	##ERROR : Reader.JISX6319: failed to write.
    
    #Reader.ISO15693
    ERR_ISO15693_DATA_TOO_LONG          = 0x2250 #8784	##ERROR : Data to write is too long (%d bytes maximum).
    
    #SPY
    ERR_SPY_BAD_OUTPUT_FILE             = 0x3001 #12289	##ERROR : SPY: No output file specified or bad file.
    ERR_ANALYZER_BAD_INPUT_FILE         = 0x3003 #12291	##ERROR : Could not open analyzer input file.
    ERR_ANALYZER_BAD_OUTPUT_FILE        = 0x3004 #12292	##ERROR : Could not open analyzer output file.
    ERR_GENERIC_ANALYZER_NOT_FOUND      = 0x300a #12298	##ERROR : Generic Analyzer not found.
    ERR_ISO14443_ANALYZER_NOT_FOUND     = 0x300b #12299	##ERROR : ISO14443 Analyzer not found.
    ERR_FELICA_ANALYZER_NOT_FOUND       = 0x300c #12300	##ERROR : JISX6319 Analyzer not found.
    ERR_ISO15693_ANALYZER_NOT_FOUND     = 0x300d #12301	##ERROR : ISO15693 Analyzer not found.
    ERR_ISO18092_ANALYZER_NOT_FOUND     = 0x300e #12302	##ERROR : ISO18092 Analyzer not found.
    ERR_MARKER_ANALYZER_NOT_FOUND       = 0x300f #12303	##ERROR : Marker Analyzer not found.
    
    ERR_ANALOG_SPY_RUNNING              = 0x3010 #12304	##ERROR : Analog spy is running.
    ERR_ANALOG_SPY_STOPPED              = 0x3011 #12305	##ERROR : Analog spy is not running.
    ERR_ANALOG_SPY_FILE_GENERATED       = 0x3012 #12306	##Info : Analog spy file was successfully generated.
    
    ERR_SPY_RUNNING                     = 0x3013 #12307	##ERROR : Spy is running.
    ERR_SPY_THREAD_START_FAILED         = 0x3014 #12308	##ERROR : Unable to start the trace.
    ERR_SPY_TIMING_NOT_ACCURATE         = 0x3015 #12309	##Warning : PICC Frame timing not accurate.
    ERR_SPY_OVERFLOW_OCCURED            = 0x3016 #12310	##ERROR : Trace stopped: overflow occured.
    ERR_SPY_MONITOR_CLOCK               = 0x3017 #12311	##Warning : To avoid overflow, clocks are not recorded in digital trace.
    
    #LOG
    ERR_LOG_NO_FRAME_AVAILABLE          = 0x3801 #14337	##ERROR : Logger: no frame available.
    ERR_LOG_FRAME_AVAILABLE             = 0x3802 #14338	##Info : Logger: a frame is available.
    ERR_LOG_INVALID_HEADER_BYTE         = 0x3803 #14339	##ERROR : Logger: invalid header byte.
    ERR_LOG_ALREADY_STARTED             = 0x3804 #14340	##ERROR : Logger: already started.
    ERR_LOG_ERROR_WHILE_STOPPING        = 0x3805 #14341	##ERROR : Logger: error while stopping.
    ERR_LOG_FIFO_FULL                   = 0x3806 #14342	##ERROR : Logger: FIFO is full.
    ERR_LOG_RUNNING                     = 0x3807 #14343	##ERROR : Logger is running.
    ERR_LOG_INVALID_FRAME_SIZE          = 0x3808 #14344	##ERROR : Logger: Invalid frame size found in log file.
    
    ERR_ANALYZER_FILES_MERGE_FAILED     = 0x3809 #14345	##ERROR : Could not merge analyzer output files.
    ERR_ANALYZER_CANNOT_EXTRACT_TRC     = 0x380A #14346	##ERROR : Could not extract .trc file from analyzer input file.
    
    #SEQUENCER
    ERR_SEQ_PROGRAM_TOO_LONG            = 0x4000 #16384	##ERROR : Sequencer: sequence is too long to be loaded.
    ERR_SEQ_CHAINING_OFF                = 0x4001 #16385	##ERROR : Sequencer: chaining is off.
    ERR_SEQ_OVER                        = 0x4002 #16386	##Info : Sequencer: sequencer is over.
    
    #License
    ERR_SPY_LICENSE_NOT_AVAI            = 0x4500 #17664	##ERROR : SPY license not available on this product, please contact your reseller to upgrade it.
    ERR_READER_LICENSE_NOT_AVAILABLE    = 0x4501 #17664	##ERROR : Settings: Specified reader license not available. Please contact your reseller.
    ERR_EMULATOR_LICENSE_NOT_AVAILABLE  = 0x4502 #17664	##ERROR : Settings: Specified emulator license not available. Please contact your reseller.
    
    
    #Analog
    ERR_CALIB_DATE_FORMAT               = 0x5000 #20480	##ERROR : EEPROM: Calibration date format is wrong. Your ProxiLAB may not be calibrated. Please contact your reseller.
    
    #PicoBlaze
    ERR_PICO_FIRM_NOT_FOUND             = 0x5500 #21760	##ERROR : Pico: could not find firmware.
    ERR_PICO_FIRM_TOO_BIG               = 0x5501 #21761	##ERROR : Pico: firmware file too large.
    ERR_PICO_STACK_OVERFLOW             = 0x5502 #21762	##ERROR : Sequencer stack overflow.
    
    #Emulator
    ERR_EMU_NO_FRAME_AVAILABLE          = 0x6000 #24576	##ERROR : Emulator: no frame received.
    ERR_EMU_FRAME_AVAILABLE             = 0x6001 #24577	##ERROR : Emulator: another frame is available in the reception buffer.
    ERR_EMU_IBLOCK_TOO_SHORT            = 0x6002 #24578	##ERROR : Emulator: IBlock is too short.
    ERR_EMU_UNFILTERED_CID_ISSUE        = 0x6003 #24579	##ERROR : Emulator: CID error detected by software.
    ERR_EMU_UNFILTERED_NAD_ISSUE        = 0x6004 #24580	##ERROR : Emulator: NAD error detected by software.
    ERR_EMU_UNEXPECTED_BLOCK            = 0x6005 #24581	##ERROR : Emulator: Unexpected type of block.
    ERR_EMU_WRONG_NAD                   = 0x6006 #24582	##ERROR : Emulator: wrong NAD.
    ERR_EMU_DISABLED                    = 0x6007 #24583	##ERROR : Emulator is not enabled.
    ERR_EMU_WRONG_SIZE_DECLARED         = 0x6008 #24584	##ERROR : Emulator: Size declared in frame does not conform to frame size.
    ERR_EMU_MFS_TOO_SMALL               = 0x6009 #24585	##ERROR : Emulator: Maximum Frame Size is too small for the frames to contain header, information and prolog.
    ERR_EMU_SOFT_CRCA_ERROR             = 0x600A #24586	##ERROR : Emulator: CRC (A) error detected at software.
    ERR_EMU_SOFT_CRCB_ERROR             = 0x600B #24587	##ERROR : Emulator: CRC (B) error detected at software.
    ERR_EMU_ANA_PROBE_NOT_CONNECTED     = 0x600C #24588	##ERROR : Emulator: PICC-Probe+ must be connected.
    ERR_EMU_RF_RESET_OCCURED            = 0x600D #24589	##ERROR : Emulator: an RF reset occured before the end of a chained IBlock.
    ERR_EMU_DESELECTED                  = 0x600E #24590	##ERROR : Emulator: the emulator was deselected before the end of a chained IBlock.
    
    #Emulator.TypeA
    ERR_EMU_A_WRONG_UID                 = 0x6018 #24600	##ERROR : Emulator TypeA: UIDSize should be 5, 10 or 15 bytes.
    ERR_EMU_A_WRONG_UID_ISO_COMPLIANT   = 0x6019 #24601	##ERROR : Emulator TypeA: ISO/IEC 14443 compliant mode is enabled, UIDSize should be 4, 7 or 10 bytes without CT or BCC.
    
    #Emulator.PatternFilter
    ERR_EMU_PATTERN_MAX_NB              = 0x6100 #24832	##ERROR : PatternFilter: cannot store more than 8 pattern filters.
    ERR_EMU_PATTERN_OVERFLOW            = 0x6101 #24833	##ERROR : PatternFilter: too many data bytes.
    ERR_EMU_PATTERN_LEN                 = 0x6102 #24834	##ERROR : PatternFilter: pattern is too long.
    ERR_EMU_PATTERN_RESP_LEN            = 0x6103 #24835	##ERROR : PatternFilter: response is too long.
    
    #Emulator.JISX6319
    ERR_EMU_C_FORMAT_TOO_SHORT          = 0x6200 #25088	##ERROR : JISX6319: wrong frame format: frame is too short.
    ERR_EMU_C_FORMAT_PREAMBLE           = 0x6201 #25089	##ERROR : JISX6319: wrong frame format: preamble is not B2 4D.
    ERR_EMU_C_FORMAT_SIZE               = 0x6202 #25090	##ERROR : JISX6319: wrong frame format: size does not match size byte.
    ERR_EMU_C_FORMAT_CRC                = 0x6203 #25091	##ERROR : JISX6319: wrong frame format: CRC error.
    
    #Timer
    ERR_TIMER_MEAS_NOT_OVER             = 0x6500 #25856	##ERROR : Timer: measuremement is not over yet.
    ERR_TIMER_MEAS_OVERFLOW             = 0x6501 #25857	##ERROR : Timer: measuremement overflow.
    
    #Settings
    ERR_MODE_READER_NOT_SELECTED        = 0x6600 #26112	##ERROR : Settings: Reader mode not selected.
    ERR_MODE_READER_AB_NOT_SELECTED     = 0x6601 #26113	##ERROR : Settings: Reader AB mode not selected.
    ERR_MODE_READER_15693_NOT_SELECTED  = 0x6602 #26114	##ERROR : Settings: Reader ISO15693 mode not selected.
    ERR_MODE_READER_JISX_NOT_SELECTED   = 0x6603 #26115	##ERROR : Settings: Reader JISX6319 mode not selected.
    ERR_MODE_EMU_NOT_SELECTED           = 0x6604 #26116	##ERROR : Settings: Emulator mode not selected.
    
    #Emulator.LoadEventResponse
    ERR_EMU_EVENT_RESP_BYTE_NB          = 0x6605 #26117	#
    
    #Emulator.LoadSpulse
    ERR_EMU_SPULSE_BYTE_NB              = 0x6606 #26118	##ERROR : Too many bytes are already loaded.
    ERR_EMU_SPULSE_NO_DATA_FOUND        = 0x6607 #26119	##ERROR : No data found in the specified file.
    ERR_EMU_SPULSE_DATA_TAG_NOT_FOUND   = 0x6608 #26120	##ERROR : [%s] section not found in the specified file
    
    ERR_OBSOLETE_METHOD                 = 0x6609 #26121	##ERROR : Obsolete method.
    
    ERR_CONDITIONS_NOT_MET              = 0x660A #26122	##ERROR : Conditions to apply this parameter are not met.
    ERR_WRONG_BRIDGE_VERSION            = 0x660B #26123	##ERROR : Bridge V7.0 or higher should be connected to activate this mode..
    ERR_BRIDGE_DEMOD_NOT_SELECTED       = 0x660C #26124	##ERROR : Bridge demodulator input must be selected to activate this mode.
    ERR_READER_AB_MODE_NOT_SELECTED     = 0x660D #26125	##ERROR : READER_AB configuration must be selected to activate this mode.
    ERR_NOT_PROXILAB_V3                 = 0x660E #26126	##ERROR : this mode is not compatible with your ProxiLAB version.
    
    ERR_NOT_CALIBRATED                  = 0x660F #26127	##ERROR : ProxiLAB has not been calibrated.
    ERR_NOT_ANALOG_MODE                 = 0x6610 #26128	##ERROR : ProxiLAB SMA4 is not in Analog mode.
    
    ERR_VNA_MODE_POWER_PARAM_DISABLED   = 0x6611 #26129	##ERROR : Power parameters are disabled in VNA mode.
    
    ERR_NOT_FOUND_TIMING                = 0x6612 #26130	##ERROR : Specified timing not found.
    ERR_BITS_NUMBER                     = 0x6613 #26131	##ERROR : The number of bits is not multiples of 9.
    ERR_BITS_VALUE                      = 0x6614 #26132	##ERROR : Bits value must be 0 or 1.
    ERR_BAD_FLAGS                       = 0x6615 #26133	##ERROR : Select_flag and Address_flag can not be 1 at the same time.
    ERR_UID_NOT_AVAILABLE               = 0x6616 #26134	##ERROR : UID is not available. Please send INVENTORY first.
    
    #TAG_ERR_CODE_END (tag used by MissingErrorCode.js)


    #ProxiLAB.ADCInput
    SINGLE_CHANNEL = 1
    DUAL_CHANNEL = 2
    QUAD_CHANNEL = 3


    #ProxiLAB.Settings.IO4Direction
    DIRECTION_OUTPUT    = 0x0000 #0
    DIRECTION_INPUT     = 0x0001 #1


    #ProxiLAB.Settings.Input4Mode
    MODE_DIGITAL        = 0x0000
    MODE_ANALOG         = 0x0001


    #ProxiLAB.unlinked
    LICENSE_SPY           = 0x0001
    LICENSE_READER        = 0x0002
    LICENSE_READER_NFC    = 0x0004
    LICENSE_EMU           = 0x0008
    LICENSE_EMU_NFC       = 0x0010


    #ProxiLAB.Settings.License
    LICENSE_PCD_AB          = 0x0001
    LICENSE_PCD_ANA         = 0x0002
    LICENSE_PCD_NFC         = 0x0004
    LICENSE_PICC_AB         = 0x0008
    LICENSE_PICC_ANA        = 0x0010
    LICENSE_PICC_NFC        = 0x0020
    LICENSE_PCD_VHBR_ASK    = 0x0040
    LICENSE_PCD_VHBR_PSK    = 0x0080
    LICENSE_EMD             = 0x0100
    LICENSE_ALM             = 0x0200


    #ProxiLAB.Reader.StartPolling.dwType
    TYPE_A             = 0
    TYPE_B             = 1
    
    PROTOCOL_ISO14443A = 2     #to match ISO14443A_STANDARD
    PROTOCOL_ISO14443B = 3     #to match ISO14443B_STANDARD
    PROTOCOL_ISO15693  = 4     #to match ISO15693_STANDARD
    PROTOCOL_INNOVATRON= 5
    PROTOCOL_ISO18092  = 6     #to match ISO18092_STANDARD
    PROTOCOL_JISX6319  = 7     #to match JISX6319_STANDARD
    PROTOCOL_VHDR      = 8     #to match VHDR_STANDARD
    PROTOCOL_VHBR      = 8     #to match VHBR_STANDARD
    
    PROTOCOL_UNKNOWN   = 7777


    #ProxiLAB.Settings.DemodulatorInput
    DEMODULATOR_RF_OUT          = 0x00#v2 and upper when mode Reader
    
    DEMODULATOR_RF_IN           = 0x01
    DEMODULATOR_RF_IN_PROBE     = 0x01
    
    DEMODULATOR_BRIDGE          = 0x03
    DEMODULATOR_PICC_HDMI       = 0x03#v3.1 and v3.2 when mode Emulator
    DEMODULATOR_EXT_HDMI        = 0x03#v3.3 and upper when mode Emulator
    
    DEMODULATOR_SMA2            = 0x04
    DEMODULATOR_AWG_OUT         = 0x05
    DEMODULATOR_RF_OUT_DUAL     = 0x06
    


    #ProxiLAB.Settings.DemodulatorAttenuation
    ATT_0dB     = 0x00
    ATT_10dB    = 0x01
    ATT_20dB    = 0x02
    ATT_30dB    = 0x03


    #ProxiLAB.Settings.ModulatorOutput
    MODULATOR_RF_OUT                = 0
    MODULATOR_AWG_OUT               = 1
    MODULATOR_RF_OUT_DUAL           = 2
    MODULATOR_AWG_CARRIER_RF_OUT    = 3
    


    #ProxiLAB.Settings.ClockSource
    CLOCK_SOURCE_INT        = 0x00
    CLOCK_SOURCE_EXT_DIG    = 0x01
    CLOCK_SOURCE_EXT_ANA    = 0x02


    #ProxiLAB.Emulator.ISO14443.TypeA.UIDType
    UID_SINGLE            = 0x00
    UID_DOUBLE            = 0x01
    UID_TRIPLE            = 0x02


    #ProxiLAB.Emulator.ISO14443.State
    STATE_OFF                 = 0x00000001 #PICC is in state OFF/IDLE
    STATE_POLLING             = 0x00000002 #PICC is subject to polling but not yet selected
    STATE_SELECTED            = 0x00000004 #PICC is selected by PCD
    STATE_HALT                = 0x00000008 #PICC is in halt state
    #STATE_FRAME_RXD           = 0x00000010, #Complete PCD I-Block available
    STATE_DESELECTED          = 0x00000020 #PICC was deselected (note 1)
    #STATE_RST_B4_DESEL        = 0x00000040, #RF reset occurred before PICC was deselected (note 1)
    #STATE_RST_ERR_1           = 0x00000080, #RF reset occurred before PC had sent its last I-Block answer (note 1)
    #STATE_RST_ERR_2           = 0x00000100, #RF reset occurred before PICC could transmit last I-Block (note 1)
    STATE_PICC_CHAIN          = 0x00000200 #PICC is sending a chained frame
    #STATE_PCD_CHAIN           = 0x00000400, #PCD is sending a chained frame
    STATE_FIELD_ON            = 0x00000800 #Field is detected
    
    STATE_POLLING_B_IDLE      = 0x00001000
    STATE_POLLING_B_READY_REQ = 0x00002000
    STATE_POLLING_B_READY_DEC = 0x00004000
    
    STATE_HALT_A              = 0x00010000
    STATE_HALT_B              = 0x00020000


    #ProxiLAB.Emulator.Analog.SelectLoad
    #0bxx00xx00
    PICC_LOAD_NONE	          = 0x00
    NFC_2_0_LOAD_NONE         = 0x00
    EMV_3_0_LOAD_NONE		  = 0x00
    #0bxx00xx01
    PICC_LOAD_1			      = 0x01
    NFC_2_0_LOAD_1            = 0x01
    EMV_3_0_LOAD_LLZ          = 0x01
    #0bxx00xx10
    PICC_LOAD_2				  = 0x02
    NFC_2_0_LOAD_2            = 0x02
    EMV_3_0_LOAD_DCO          = 0x02
    #0bxx01xx00
    PICC_LOAD_3				  = 0x10
    NFC_2_0_LOAD_3            = 0x10
    EMV_3_0_LOAD_NLZ          = 0x10
    #0bxx10xx00
    PICC_LOAD_4               = 0x20
    NFC_2_0_LOAD_4            = 0x20
    EMV_3_0_LOAD_HLZ          = 0x20
    


    #ProxiLAB.Emulator.ISO14443.TypeB.DisableStateMachine.dwCommand
    POWER_OFF           = 0x00 # POWER_OFF    : No Answer
    IDLE                = 0x40 # IDLE for all the types    : wait for the first command
    
    #Type B states
    B_IDLE              = 0x21 # IDLE         : Wait ReqB or WupB
    B_READY_REQ         = 0x22 # READY_REQ    : Wait Slot Markers
    B_READY_DEC         = 0x24 # READY_DEC    : Wait Attrib
    B_HALT              = 0x28 # HALT         : Wait WupB
    B_MAX               = 0x29 # not a state  : just B_HALT + 1
    
    ACTIVE              = 0x80
    
    #Type A states
    A_HALT              = 0x11 # A_HALT        : 0x11 : Wait WupA                       x
    A_IDLE              = 0x12 # A_IDLE        : 0x12 : Wait ReqA or WupA        x      x
    A_READY_HLT_AC1     = 0x13 # A_READY_HLT   : 0x13 : Wait SELECT                              x
    A_READY_AC1         = 0x14 # A_READY       : 0x14 : Wait SELECT                              x
    A_READY_HLT_AC2     = 0x15 # A_READY_HLT   : 0x15 : Wait SELECT                              x
    A_READY_AC2         = 0x16 # A_READY       : 0x16 : Wait SELECT                              x
    A_READY_HLT_AC3     = 0x17 # A_READY_HLT   : 0x17 : Wait SELECT                              x
    A_READY_AC3         = 0x18 # A_READY       : 0x18 : Wait SELECT                              x
    A_ACTIVE_HLT        = 0x19 # A_ACTIVE_HLT  : 0x19 : Wait layer-4 Block                              x        x
    A_ACTIVE            = 0x1A # A_ACTIVE      : 0x1A : Wait layer-4 Block                              x        x
    A_ATS               = 0x1B # A_RATS        : 0x1B
    A_PPS               = 0x1C # A_PPS         : 0x1C
    
    #FeliCa states
    FELICA_IDLE         = 0x51
    FELICA_READY_REQ    = 0x52
    FELICA_READY_DEC    = 0x53
    FELICA_ACTIVE       = 0x54
    
    #15693 states
    ISO15693_READY      = 0x31
    ISO15693_QUIET      = 0x32
    ISO15693_SELECTED   = 0x33
    ISO15693_INVENTORY  = 0x36 # temporary state : valid when inventory completed...
    


    #ProxiLAB.Trigger.State
    TRIGGER_EVENT_0   = 0
    TRIGGER_EVENT_1   = 1
    TRIGGER_PATTERN_0 = 2
    TRIGGER_PATTERN_1 = 3
    TRIGGER_ADVANCED_EVENT_0 = 4


    #ProxiLAB.Trigger.Timer0.StartSource
    TIMER_START_RF_POWER_ON_SYNC     = 0
    TIMER_START_RF_POWER_OFF_SYNC    = 1
    TIMER_START_TX_SOF_SYNC          = 2
    TIMER_START_TX_EOF_SYNC          = 3
    TIMER_START_RX_SOF_SYNC          = 4
    TIMER_START_RX_EOF_SYNC          = 5
    TIMER_START_TRIGGER              = 6
    TIMER_START_SMA1                 = 7
    TIMER_START_SMA2                 = 8
    TIMER_START_SMA3                 = 9
    TIMER_START_SMA4                 = 10
    TIMER_START_TIMER0_TIMEOUT       = 11
    TIMER_START_NOT_CONFIGURED       = 0xFF
    TIMER_STOP_RF_POWER_ON_SYNC     = 0
    TIMER_STOP_RF_POWER_OFF_SYNC    = 1
    TIMER_STOP_TX_SOF_SYNC          = 2
    TIMER_STOP_TX_EOF_SYNC          = 3
    TIMER_STOP_RX_SOF_SYNC          = 4
    TIMER_STOP_RX_EOF_SYNC          = 5
    TIMER_STOP_TRIGGER              = 6
    TIMER_STOP_SMA1                 = 7
    TIMER_STOP_SMA2                 = 8
    TIMER_STOP_SMA3                 = 9
    TIMER_STOP_SMA4                 = 10
    TIMER_STOP_TIMER0_TIMEOUT       = 11
    TIMER_STOP_NOT_CONFIGURED       = 0xFF


    #ProxiLAB.Trigger.Pattern1.Flow
    TRIGGER_FLOW_READER = 0
    TRIGGER_FLOW_PCD    = 0
    TRIGGER_FLOW_CARD   = 1
    TRIGGER_FLOW_PICC   = 1
    TRIGGER_FLOW_BOTH   = 2


    #ProxiLAB.Trigger.Event0.EnEvents, ProxiLAB.Trigger.Event1.EnEvents
    EVENT_OFF                  = 0x0000
    EVENT_READER_SOF           = 0x0001
    EVENT_PCD_SOF              = 0x0001
    EVENT_READER_EOF           = 0x0002
    EVENT_PCD_EOF              = 0x0002
    EVENT_READER_BIT_SYNC      = 0x0004
    EVENT_PCD_BIT_SYNC         = 0x0004
    EVENT_READER_BYTE_SYNC     = 0x0008
    EVENT_PCD_BYTE_SYNC        = 0x0008
    EVENT_READER_ERROR_PARITY  = 0x0010
    EVENT_PCD_ERROR_PARITY     = 0x0010
    EVENT_READER_ERROR_CRC     = 0x0020
    EVENT_PCD_ERROR_CRC        = 0x0020
    EVENT_PICC_SOF             = 0x0040
    EVENT_PICC_EOF             = 0x0080
    EVENT_PICC_BIT_SYNC        = 0x0100
    EVENT_PICC_BYTE_SYNC       = 0x0200
    EVENT_PICC_ERROR_COLLISION = 0x0400
    EVENT_PICC_ERROR_PARITY    = 0x0800
    EVENT_PICC_ERROR_CRC       = 0x1000
    EVENT_PICC_FFT_SYNC        = 0x2000
    EVENT_RF_POWER_ON_SYNC     = 0x4000
    EVENT_SMA3                 = 0x8000


    #ProxiLAB.Trigger1.AdvancedEvent0.PulseWidth.Source
    ADV_EVENT_CONSTANT_0			= 0
    ADV_EVENT_CONSTANT_1			= 1
    ADV_EVENT_RF_POWER				= 3
    ADV_EVENT_TX_IO					= 6
    ADV_EVENT_TX_FRAME				= 7
    ADV_EVENT_RX_IO					= 14
    ADV_EVENT_RX_FRAME				= 15
    ADV_EVENT_TX_FRAME_TYPEA		= 32
    ADV_EVENT_TX_FRAME_TYPEB		= 33
    ADV_EVENT_TX_FRAME_TYPEF		= 34
    ADV_EVENT_TX_FRAME_TYPE15		= 35
    
    ADV_EVENT_PULSE_WIDTH				= 68
    ADV_EVENT_LOGICAL					= 69
    ADV_EVENT_PULSE_TRAIN				= 70
    


    #ProxiLAB.Trigger1.AdvancedEvent0.Logical.Type
    LOGICAL_AND				= 1
    LOGICAL_NAND			= 2
    LOGICAL_OR				= 3
    LOGICAL_NOR				= 4


    #ProxiLAB.Spy.Analog.OutputFileFormat
    ANA_FORMAT_NONE  = 0
    ANA_FORMAT_CSV   = 1
    ANA_FORMAT_TXT   = 2
    ANA_FORMAT_MFILE = 4
    ANA_FORMAT_FACIL = 8
    ANA_FORMAT_BINARY = 16


    #ProxiLAB.Spy.Analog.StartSource
    SOURCE_TRIGGER_0  = 0
    SOURCE_TRIGGER_1   = 1


    # ProxiLAB.Spulse.LoadSpulse.dwType, ProxiLAB.Spulse.LoadSpulseCsvFile.dwType
    FRAME_TYPE_PCD_A   = 0 #b0000
    FRAME_TYPE_PCD_B   = 1 #b0001
    FRAME_TYPE_PICC_A  = 2 #b0010
    FRAME_TYPE_PICC_B  = 3 #b0011
    FRAME_TYPE_PCD_15  = 4 #b0100
    FRAME_TYPE_PICC_15 = 5 #b0101
    FRAME_TYPE_PCD_C   = 6 #b0110
    FRAME_TYPE_PICC_C  = 7 #b0111
    FRAME_TYPE_SPULSE  = 14


    #ProxiLAB.Reader.ISO14443.SendData.frameType
    SHORT_FRAME    = 0
    ANTICOL_FRAME  = 1
    STANDARD_FRAME = 2


    #ProxiLAB.Emulator.ISO14443.SupportedBitratesPICC
    BAUDRATE_106K = 1
    BAUDRATE_212K = 2
    BAUDRATE_424K = 4
    BAUDRATE_847K = 8
    BAUDRATE_1_6M = 16
    BAUDRATE_3_4M = 32
    BAUDRATE_6_8M = 64
    BAUDRATE_10_17M = 66#3fc/4
    BAUDRATE_13_56M = 68#fc
    BAUDRATE_20_34M = 70#3fc/2
    BAUDRATE_27_12M = 72#2fc


    #ProxiLAB.Reader.ISO14443.PCSC.CommunicationStandard
    PCSC_AUTOMATIC = 0
    PCSC_TYPE_A    = 1
    PCSC_TYPE_B    = 2


    #ProxiLAB.Sequencer.DelayCycle.ClockDomain
    CLOCK_DOMAIN_48M        = 0
    CLOCK_DOMAIN_1356       = 1
    CLOCK_DOMAIN_13M        = 1
    CLOCK_DOMAIN_EXTRACTED  = 2
    #CLOCK_DOMAIN_2712       = 1,
    CLOCK_DOMAIN_27M        = 3


    #ProxiLAB.Settings.Output1, ProxiLAB.Settings.Output2, ProxiLAB.Settings.Output3, ProxiLAB.Settings.Output4
    OUTPUT_CONSTANT_LOW         = 0
    OUTPUT_CONSTANT_HIGH        = 1
    OUTPUT_HIGH_IMPEDANCE       = 2
    OUTPUT_TRIGGER              = 8
    OUTPUT_TRIGGER1             = 256 + 61
    OUTPUT_PCD_PICC_IO          = 256 + 29
    OUTPUT_PCD_PICC_FRAME       = 256 + 30
    OUTPUT_RF_POWER             = 16
    OUTPUT_RF_POWER_ON_SYNC     = 17
    OUTPUT_RF_POWER_OFF_SYNC    = 18
    OUTPUT_EXTRACT_CLK          = 31
    OUTPUT_INTERNAL_CLK         = 43
    OUTPUT_SHIFTED_EXTRACT_CLK  = 42
    OUTPUT_PCD_IO               = 32
    OUTPUT_PCD_FRAME            = 33
    OUTPUT_PCD_SOF              = 34
    OUTPUT_PCD_EOF              = 35
    OUTPUT_PCD_BIT_SYNC         = 36
    OUTPUT_PCD_BYTE_SYNC        = 37
    OUTPUT_PCD_PARITY_ERROR     = 38
    OUTPUT_PCD_CRC_ERROR        = 39
    OUTPUT_PCD_A_FRAME          = 256 + 32
    OUTPUT_PCD_B_FRAME          = 256 + 33
    OUTPUT_PCD_FELICA_FRAME     = 256 + 34
    OUTPUT_PCD_ISO15693_FRAME   = 256 + 35
    OUTPUT_PCD_PHASE_SHIFT      = 41
    OUTPUT_PICC_IO              = 48
    OUTPUT_PICC_FRAME           = 49
    OUTPUT_PICC_MANCHESTER      = 50
    OUTPUT_PICC_SUBCARRIER      = 51
    OUTPUT_PICC_PHASE           = 52
    OUTPUT_PICC_SOF             = 53
    OUTPUT_PICC_EOF             = 54
    OUTPUT_PICC_BIT_SYNC        = 55
    OUTPUT_PICC_BYTE_SYNC       = 56
    OUTPUT_PICC_COLLISION_ERROR = 57
    OUTPUT_PICC_PARITY_ERROR    = 58
    OUTPUT_PICC_CRC_ERROR       = 59
    OUTPUT_PICC_TIMEOUT_ERROR   = 60
    OUTPUT_PICC_FFT_SYNC        = 61
    OUTPUT_PICC_CRC_A           = 62
    OUTPUT_PICC_CRC_B           = 63
    OUTPUT_SECURITY_PULSE       = 256 + 36
    OUTPUT_PICC_MODULATOR_IO    = 256 + 37
    OUTPUT_PCD_FELICA_FRAME_212 = 256 + 38
    OUTPUT_PCD_FELICA_FRAME_424 = 256 + 39
    OUTPUT_TRACE_RUN            = 256 + 40
    OUTPUT_VNA_START_SWEEP      = 44
    
    #Min/max values
    OUTPUT_MIN_VALUE            = OUTPUT_CONSTANT_LOW
    OUTPUT_MAX_VALUE            = OUTPUT_TRACE_RUN + 25


    #ProxiLAB.Settings.Antenna
    ANTENNA_INT = 0
    ANTENNA_EXT = 1


    #ProxiLAB.unlinked
    ISO14443_STANDARD  = 1
    ISO14443A_STANDARD = 2
    ISO14443B_STANDARD = 3
    ISO15693_STANDARD  = 4
    ISO18092_STANDARD  = 5
    FELICA_STANDARD    = 6
    JISX6319_STANDARD  = 7
    VHDR_STANDARD      = 8
    VHBR_STANDARD      = 8


    #ProxiLAB.unlinked
    NO_PROPRIETARY_PROTOCOL    = 0
    INNOVATRON_PROTOCOL        = 1
    INSIDE_PICOPASS_PROTOCOL   = 2
    MIFARE_ULTRALIGHT_PROTOCOL = 3
    STMICRO_SRI_PROTOCOL       = 4
    STMICRO_SR176_PROTOCOL     = 5


    #ProxiLAB.Settings.Mode
    MODE_READER             = 0#ProxiLAB V2
    MODE_EMULATOR           = 1
    MODE_EMULATOR_A_B       = 1
    MODE_READER_15693       = 2# Compatibility for old script, but this mode supports only AB, please use MODE_READER_ISO15693 for ISO15693
    MODE_READER_AB          = 2
    MODE_READER_JISX        = 3
    MODE_READER_JISX6319    = 3
    MODE_EMULATOR_F_15      = 4
    MODE_READER_ISO15693    = 5
    MODE_VNA                = 20


    #ProxiLAB.Settings.Submode
    MODE_DEFAULT             = 0
    MODE_SSB                 = 1


    #ProxiLAB.unlinked
    VHDL_EMU_TYPE_A         = 1
    VHDL_EMU_TYPE_B         = 2
    VHDL_EMU_VHDR           = 4
    VHDL_EMU_VHBR           = 4
    VHDL_EMU_ISO15693       = 8
    VHDL_EMU_JISX6319       = 16
    VHDL_EMU_TYPE_Bprime    = 32
    VHDL_EMU_TOPAZ          = 64


    #ProxiLAB.unlinked
    VHDL_READER_TYPE_A      = 0
    VHDL_READER_TYPE_B      = 1
    VHDL_READER_JISX6319    = 2
    VHDL_READER_VHDR        = 3
    VHDL_READER_VHBR        = 3
    VHDL_READER_ISO15693    = 4
    VHDL_READER_TYPE_Bprime = 5
    VHDL_READER_SPULSE      = 7


    #ProxiLAB.Reader.SendBytes.dwType
    READER_TYPE_A      = 0
    READER_TYPE_B      = 1
    READER_JISX6319    = 2
    READER_VHDR        = 3
    READER_VHBR        = 3
    READER_ISO15693    = 4
    READER_TYPE_Bprime = 5
    READER_SPULSE      = 7


    #ProxiLAB.Reader.ISO15693.SendTransparentCommand.dwModulationType
    ISO15693_1_TO_256    = 0
    ISO15693_1_TO_4      = 1


    #ProxiLAB.unlinked
    SUB_SARRIER_FLAG            = 0x01
    DATA_RATE_FLAG              = 0x02
    INVENTORY_FLAG              = 0x04
    PROTOCOL_EXTENSION_FLAG     = 0x08
    AFI_FLAG                    = 0x10
    NB_SLOTS_FLAG               = 0x20
    OPTION_FLAG                 = 0x40
    SELECT_FLAG                 = 0x10
    ADRESS_FLAG                 = 0x20


    #ProxiLAB.Reader.ISO15693.SendCommand
    ISO15_CMD_INVENTORY = 0x01
    ISO15_CMD_STAY_QUIET = 0x02
    ISO15_CMD_READ_SINGLE_BLOCK = 0x20
    ISO15_CMD_WRITE_SINGLE_BLOCK = 0x21
    ISO15_CMD_LOCK_BLOCK = 0x22
    ISO15_CMD_READ_MULTIPLE_BLOCKS = 0x23
    ISO15_CMD_WRITE_MULTIPLE_BLOCKS = 0x24
    ISO15_CMD_SELECT = 0x25
    ISO15_CMD_RESET_TO_READY = 0x26
    ISO15_CMD_WRITE_AFI = 0x27
    ISO15_CMD_LOCK_AFI = 0x28
    ISO15_CMD_WRITE_DSFID = 0x29
    ISO15_CMD_LOCK_DSFID = 0x2A
    ISO15_CMD_GET_SYSTEM_INFORMATION = 0x2B
    ISO15_CMD_GET_MULTIPLE_BLOCK_SECURITY_STATUS = 0x2C


    #ProxiLAB.unlinked
    ERROR_FLAG                  = 0x01


    #ProxiLAB.Emulator.ISO15693.DataRate, ProxiLAB.Reader.ISO15693.DataRateFlag
    FLAG_LOW_DATA_RATE    = 0
    FLAG_HIGH_DATA_RATE   = 1


    #ProxiLAB.Reader.ISO15693.SubCarrierFlag
    FLAG_SINGLE_SUBCARRIER    = 0
    FLAG_DOUBLE_SUBCARRIER    = 1


    #ProxiLAB.Emulator.ISO15693.ModulationType
    SINGLE_SUBCARRIER    = 0
    DOUBLE_SUBCARRIER    = 1


    #ProxiLAB.Emulator.NFC_DEP.Mode
    MODE_PASSIVE = 0
    MODE_ACTIVE  = 1


    #ProxiLAB.Reader.ISO18092.PSL_REQ.dwLR
    LR_00 = 0
    LR_01 = 1
    LR_10 = 2
    LR_11 = 3


    #ProxiLAB.Emulator.Analog.ActivateSubcarrier
    NO_EMU_SUBCARRIER       = 0
    EMU_SUBCARRIER_13_56M   = 1
    EMU_SUBCARRIER_6_8M     = 2
    EMU_SUBCARRIER_3_4M     = 3
    EMU_SUBCARRIER_1_7M     = 4
    EMU_SUBCARRIER_848K     = 5
    EMU_SUBCARRIER_424K     = 6
    EMU_SUBCARRIER_212K     = 7


    #ProxiLAB.Emulator.PatternFilter.Timing
    TIMING_0     = 2
    TIMING_1     = 3
    TIMING_2     = 4
    TIMING_3     = 5
    TIMING_4     = 6
    TIMING_5     = 7


    #ProxiLAB.unlinked
    TOGGLE_BN        = 8
    NO_TOGGLE_BN     = 0


    #ProxiLAB.Emulator.JISX6319.LoadFrameResponse.dwResponseCode
    EMU_JISX6319_ReadResponse               = 0x07
    EMU_JISX6319_WriteResponse              = 0x09
    EMU_JISX6319_Authentication1Response    = 0x11
    EMU_JISX6319_Authentication2Response    = 0x13
    EMU_JISX6319_ReadSecureFileResponse     = 0x15
    EMU_JISX6319_WriteSecureFileResponse    = 0x17


    #ProxiLAB.Emulator.EnableEventResponse
    MODE_DISABLE    = 0
    MODE_TRIGGER    = 1
    MODE_EOF        = 2
    MODE_EOF_TOPAZ  = 3


    #ProxiLAB.Spulse.EnableSpulse.dwEvent
    SP_COMPLEX_TRIGGER = 1
    SP_PCD_EOF         = 2
    SP_PICC_EOF        = 3
    SP_PICC_CRC        = 4


    #ProxiLAB.Spulse.EnableSpulse.dwOutput
    SP_X_MOD_PICC      = 1
    SP_X_MOD_PCD       = 1
    SP_X_LOAD          = 2
    SP_RF_POWER        = 3
    SP_X_MOD_PCD_EMU   = 4


    #ProxiLAB.Spulse.LoadSpulse.dwOpMode
    AND_LOGIC          = 0
    STAND_ALONE        = 1


    #ProxiLAB.Emulator.ModulatorOutput.dwModSrc
    LOGIC_LOW   = 0
    LOGIC_HIGH  = 1
    STANDARD    = 2
    SMA3        = 3


    #ProxiLAB.Emulator.DEPMode
    ISO_DEP   = 0
    NFC_DEP   = 1


    #ProxiLAB.Reader.ISO14443.TypeBPrime.SendTransparentCommand.dwParam
    NO_EVENT           = 0x01  #The frame is sent immediately
    SEND_FRAME         = 0x02  #The frame will be sent the next time LoadTransparentCommand will be called
    COMPLEX_TRIGGER    = 0x04  #The frame will be sent after a complex trigger
    TIMER_0            = 0x08  #The frame will be sent after the timeout of Timer0
    TIMER_1            = 0x10  #The frame will be sent after the timeout of Timer1
    PARITY_BITS        = 0x20  #TypeA only: apply lpTxBufferParity directly as parity bits table


    #ProxiLAB.Measure.GetSMA4Value.dwType
    SMA4_TRANSPARENT        = 0
    SMA4_FIELD_MEASURE      = 1
    SMA4_DC_MEASURE         = 2
    SMA4_FIELD_TRANSPARENT  = 3


    #ProxiLAB.Reader.ISO14443.LoadPSKSOF.dwPhaseIndex, ProxiLAB.Reader.ISO14443.LoadPSKEOF.dwPhaseIndex
    PH_P32 = 0x00
    PH_P28 = 0x01
    PH_P24 = 0x02
    PH_P20 = 0x03
    PH_P16 = 0x04
    PH_P12 = 0x05
    PH_P8  = 0x06
    PH_P4  = 0x07
    PH_0   = 0x08
    PH_N4  = 0x09
    PH_N8  = 0x0A
    PH_N12 = 0x0B
    PH_N16 = 0x0C
    PH_N20 = 0x0D
    PH_N24 = 0x0E
    PH_N28 = 0x0F
    PH_N180= 0x10


    #ProxiLAB.VNA.StartFreq
    VNA_MIN_FREQ        = 8000000
    VNA_MAX_FREQ        = 80000000


    #ProxiLAB.VNA.Power
    VNA_MIN_POWER       = 0
    VNA_MAX_POWER       = 1023


    #ProxiLAB.VNA.NbPoints
    VNA_MIN_NB_POINTS   = 1
    VNA_MAX_NB_POINTS   = 4096


    #ProxiLAB.Filtering.Filter
    DEFAULT_LOWPASS_FILTER  = 0
    EQUALIZER               = 1
    NO_FILTER               = 2


    #ProxiLAB.Spy.AnalogSpy.Source
    ADC_DATA       = 0
    IQ_DEMOD_DATA  = 1


    #ProxiLAB.ExtractClock.Source
    EXTRACT_CLK_NONE    = 0x00
    EXTRACT_CLK_RF_IN   = 0x01
    EXTRACT_CLK_RF_OUT  = 0x02


    #ProxiLAB.ExtractClock.Shift
    EXTRACT_CLK_INCREASE    = 0x01
    EXTRACT_CLK_DECREASE    = 0x02
