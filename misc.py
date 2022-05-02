# This code and associated information is provided to guide KEOLABS'
# customers in their use of KEOLABS' testing tools. KEOLABS shall not be
# liable for any direct, indirect or consequential damages with respect
# to claims arising from the content and/or its use by the KEOLABS' customers.
# For more information, refer to KEOLABS Sales Conditions at www.keolabs.com.

"""
@file   Reader_Triggers.py
@brief  Python example that uses the ProxiLAB.
        Complex Trigger example for Emulator
        Generate a signal after :
            - 1 Anticol layer1 (Pattern0)
            - 1 Select (Pattern1)
            - 2nd Byte in the response (Event0)
            - 5th Bit (Event1)   
"""


import sys
import site
import os
site.addsitedir( os.environ['RGPA_PATH'] + '..\\Quest\\Lib' )

import win32com.client
import pythoncom
import sys
import ctypes

def Mbox(title, text, style):
    ctypes.windll.user32.MessageBoxA(0, text, title, style)

# Main function    
def main(proxilab):
    
    #Set the ProxiLAB in reader mode
    ProxiLAB.Settings.Mode = ProxiLABUtilities.Constants.MODE_READER_AB
    
    #Event Sequencer
    #4 states
    ProxiLAB.Trigger.NbState = 4
    ProxiLAB.Trigger.State4 = ProxiLABUtilities.Constants.TRIGGER_PATTERN_0
    ProxiLAB.Trigger.State5 = ProxiLABUtilities.Constants.TRIGGER_PATTERN_1
    ProxiLAB.Trigger.State6 = ProxiLABUtilities.Constants.TRIGGER_EVENT_0
    ProxiLAB.Trigger.State7 = ProxiLABUtilities.Constants.TRIGGER_EVENT_1
    
    #Pattern0 Settings
    ProxiLAB.Trigger.Pattern0.Mask0 = 0x00
    ProxiLAB.Trigger.Pattern0.Mask1 = 0x00
    ProxiLAB.Trigger.Pattern0.Mask2 = 0x00
    ProxiLAB.Trigger.Pattern0.Mask3 = 0x00
    ProxiLAB.Trigger.Pattern0.Mask4 = 0x00
    ProxiLAB.Trigger.Pattern0.Mask5 = 0x00
    ProxiLAB.Trigger.Pattern0.Mask6 = 0x00
    ProxiLAB.Trigger.Pattern0.Value7 = 0x1D
    ProxiLAB.Trigger.Pattern0.Mask7 = 0xFF
    #Set AutoReload Mode
    ProxiLAB.Trigger.Pattern0.AutoReload = 1
    ProxiLAB.Trigger.Pattern0.Shifting = 1
    ProxiLAB.Trigger.Pattern0.Flow = ProxiLABUtilities.Constants.TRIGGER_FLOW_READER
    ProxiLAB.Trigger.Pattern0.Counter = 1
    ProxiLAB.Trigger.Pattern0.Shifting = 1
    
    #Pattern1 Settings
    ProxiLAB.Trigger.Pattern1.Mask0 = 0x00
    ProxiLAB.Trigger.Pattern1.Mask1 = 0x00
    ProxiLAB.Trigger.Pattern1.Mask2 = 0x00
    ProxiLAB.Trigger.Pattern1.Mask3 = 0x00
    ProxiLAB.Trigger.Pattern1.Mask4 = 0x00
    ProxiLAB.Trigger.Pattern1.Mask5 = 0x00
    ProxiLAB.Trigger.Pattern1.Mask6 = 0x00
    ProxiLAB.Trigger.Pattern1.Value7 = 0x0A
    ProxiLAB.Trigger.Pattern1.Mask7 = 0xFF
    #Set AutoReload Mode
    ProxiLAB.Trigger.Pattern1.AutoReload = 1
    ProxiLAB.Trigger.Pattern1.Flow = ProxiLABUtilities.Constants.TRIGGER_FLOW_CARD
    ProxiLAB.Trigger.Pattern1.Counter = 1  
    ProxiLAB.Trigger.Pattern1.Shifting = 1
    
    #Event0 Settings
    ProxiLAB.Trigger.Event0.EnEvents = ProxiLABUtilities.Constants.EVENT_PCD_BYTE_SYNC
    #Set AutoReload Mode
    ProxiLAB.Trigger.Event0.AutoReload = 1
    ProxiLAB.Trigger.Event0.Counter = 2
    
    #Event1 Settings
    ProxiLAB.Trigger.Event1.EnEvents = ProxiLABUtilities.Constants.EVENT_PCD_BIT_SYNC
    #Set AutoReload Mode
    ProxiLAB.Trigger.Event1.AutoReload = 1
    ProxiLAB.Trigger.Event1.Counter = 4
    
    ProxiLAB.Spy.Analyzer.DisplayTrigger = 1
    
    #Start the trace module
    ProxiLABUtilities.StartSpy(proxilab)

    
    #Scenario
    err                     = 1
    AFI                     = 0x00
    ISO14443_compliant      = ProxiLABUtilities.CreateVARIANT()
    CID                     = ProxiLABUtilities.CreateVARIANT()
    ATQB                    = ProxiLABUtilities.CreateVARIANT()
    picc_response           = ProxiLABUtilities.CreateVARIANT()
    PcdBitRate              = 106
    PiccBitRate            = 106
    
    buffer1                 = ProxiLABUtilities.CreateVARIANT()
    
    tested_command1 = [0x0A,0x00,0x01,0x02,0x03,0x04]
    tested_command2 = [0x0B,0x00,0x01,0x02,0x03,0x04]
    add_crc        = 1

    ProxiLAB.Reader.PowerOff()
    ProxiLAB.Reader.Power_1024(600)
    ProxiLAB.Delay(200)
    
    
    #Card Selection
    err = ProxiLAB.Reader.ISO14443.TypeA.GetCard(AFI, PcdBitRate, PiccBitRate, ISO14443_compliant, CID, ATQB)
    print(CID)
    
    # 4 IBlocks
    err = ProxiLAB.Reader.ISO14443.TypeB.SendTransparentCommand(PcdBitRate,PiccBitRate,add_crc,1000000,tested_command1,picc_response)
    
    err = ProxiLAB.Reader.ISO14443.TypeB.SendTransparentCommand(PcdBitRate,PiccBitRate,add_crc,1000000,tested_command2,picc_response)
    
    err = ProxiLAB.Reader.ISO14443.TypeB.SendTransparentCommand(PcdBitRate,PiccBitRate,add_crc,1000000,tested_command1,picc_response);
    
    err = ProxiLAB.Reader.ISO14443.TypeB.SendTransparentCommand(PcdBitRate,PiccBitRate,add_crc,1000000,tested_command2,picc_response);
    
    ProxiLAB.Reader.PowerOff()

    #Stop the trace
    ProxiLABUtilities.StopSpy(proxilab)
    
    return 0
    

# Create ProxiLAB COM object
ProxiLAB = win32com.client.Dispatch("KEOLABS.ProxiLAB")

# Test if ProxiLAB is connected
if (ProxiLAB.IsConnected==0):
    Mbox('Reader_Triggers', 'ProxiLAB not found', 0)
else:  
    # Import constants values
    sys.path.append(ProxiLAB.GetToolDirectory() + '\inc')
    import ProxiLABUtilities
    
    # Reset ProxiLAB's configuration
    ProxiLAB.Settings.LoadDefaultConfig()

    #Clear RGPA Output view
    ProxiLAB.Display.ClearOutput()
    
    #Call main function
    main(ProxiLAB)
