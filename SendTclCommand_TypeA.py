# This code and associated information is provided to guide KEOLABS'
# customers in their use of KEOLABS' testing tools. KEOLABS shall not be
# liable for any direct, indirect or consequential damages with respect
# to claims arising from the content and/or its use by the KEOLABS' customers.
# For more information, refer to KEOLABS Sales Conditions at www.keolabs.com.

"""
@file   SendTclCommand_TypeA.py
@brief  This is an example to select a type A smart card
        and to send a TCL command
        (and REQA, Anticollision, RATS, PPS commands also).
"""

import sys
import site
import os
site.addsitedir( os.environ['RGPA_PATH'] + '..\\Quest\\Lib' )

import win32com.client
import pythoncom
import sys
import ctypes

# Import constants values
sys.path.append(os.path.join(os.environ["RGPA_PATH"], "Tools\ProxiLAB\Inc"))
import ProxiLABUtilities        
    
def Mbox(title, text, style):
    ctypes.windll.user32.MessageBoxA(0, text, title, style)
    
def SendTclCommand_TypeA(proxilab):
    
    answer = ProxiLABUtilities.CreateVARIANT()
    command = ProxiLABUtilities.CreateVARIANT()
    error = 0
    PcdBitRate = 106
    PiccBitRate = 106
    CID = ProxiLABUtilities.CreateVARIANT()
    UID = ProxiLABUtilities.CreateVARIANT()
    ATS = ProxiLABUtilities.CreateVARIANT()
    ISO14443_compliant = ProxiLABUtilities.CreateVARIANT()
    SAK = ProxiLABUtilities.CreateVARIANT()

    #Set ProxiLAB in Reader mode
    ProxiLAB.Settings.Mode = ProxiLABUtilities.Constants.MODE_READER_AB
    
    #Start the trace
    error = ProxiLABUtilities.StartSpy(proxilab)
    if(error):
        sys.exit("Spy Start error")
        
    #Set the field Off
    ProxiLAB.Reader.PowerOff()
    #Set the field On
    ProxiLAB.Reader.Power_1024(600)
    
    ProxiLAB.Delay(1000)
    
    PopMsg = str()
    
    #Command GET CARD A
    error = ProxiLAB.Reader.ISO14443.TypeA.GetCard(PcdBitRate, PiccBitRate, ISO14443_compliant, CID, UID, ATS)
    if (error[0]):
        PopMsg += "GetCard: {0}".format(ProxiLAB.GetErrorInfo(error[0]))
    else:
        PopMsg +=  "UID: " + ''.join(["0x%02X " % x for x in UID.value]) + "\n"
    
    ProxiLAB.Delay(1000)

    #Command RF RESET
    ProxiLAB.Reader.RfReset()

    ProxiLAB.Delay(1000)
    
    #Command REQUEST A
    error = ProxiLAB.Reader.ISO14443.TypeA.Request(answer)
    if (error[0]):
        PopMsg += "ATQA: {0}".format(ProxiLAB.GetErrorInfo(error[0]))
    else:
        PopMsg +=  "ATQA: " + ''.join(["0x%02X " % x for x in answer.value]) + "\n"
    #Command AnticollisionA
    CascadeLevel = 1
    while(CascadeLevel <= 3):

        ProxiLAB.Delay(1000)

        #Command ANTICOLLISION A
        ProxiLAB.Reader.ISO14443.TypeA.Anticollision(CascadeLevel, UID)

        ProxiLAB.Delay(1000)
      
        #Command SELECT A
        PopMsg +=  "UID: " + ''.join(["0x%02X " % x for x in answer.value]) + "\n"
        error = ProxiLAB.Reader.ISO14443.TypeA.Select(CascadeLevel, UID, SAK)
        if (error[0]):
            PopMsg += "SAK: {0}".format(ProxiLAB.GetErrorInfo(error[0]))
        else:
            PopMsg +=  "SAK: " + ''.join(["0x%02X " % x for x in SAK.value]) + "\n"


        #Is UID complete ?
        if((SAK.value[0] & 0x04) == 0):
            break
        CascadeLevel += 1
        
    ProxiLAB.Delay(1000)

    #Command RATS
    PopMsg +=  "RATS command..." + "\n"
    error = ProxiLAB.Reader.ISO14443.TypeA.Rats(CID.value[0], ATS)
    if (error[0]):
        PopMsg += "ATS: {0}".format(ProxiLAB.GetErrorInfo(error[0]))
    else:
        PopMsg +=  "ATS: " + ''.join(["0x%02X " % x for x in ATS.value]) + "\n"
    
    ProxiLAB.Delay(1000)

    #Command PPS
    ProxiLAB.Reader.ISO14443.TypeA.Pps(CID.value[0], PcdBitRate, PiccBitRate)

    ProxiLAB.Delay(1000)

    #Command T=CL
    RxBuffer = ProxiLABUtilities.CreateVARIANT()
    TxBuffer = [0x00, 0xA4 , ...]
    PopMsg +=  "Tcl command..." + "\n"
    error = ProxiLAB.Reader.ISO14443.SendTclCommand(0x00, 0x00, TxBuffer, RxBuffer)
    if (error[0]):
        print("Tcl: {0}".format(ProxiLAB.GetErrorInfo(error[0])))
        PopMsg += "Tcl: {0}".format(ProxiLAB.GetErrorInfo(error[0])) + "\n"
    else:
        print("Tcl response: " + ''.join(["0x%02X " % x for x in RxBuffer.value]))
        PopMsg +=  "Tcl response: " + ''.join(["0x%02X " % x for x in RxBuffer.value]) + "\n"

    ProxiLAB.Delay(1000)

    #Command DESELECT
    ProxiLAB.Reader.ISO14443.Deselect(CID.value[0])

    ProxiLAB.Delay(1000)    

    #Power off
    ProxiLAB.Reader.PowerOff()
    
    Mbox('SendTclCommand_TypeA', PopMsg, 0)

    #Stop the trace
    ProxiLABUtilities.StopSpy(proxilab)


if __name__ == "__main__":  

    # Create ProxiLAB COM object
    ProxiLAB = win32com.client.Dispatch("KEOLABS.ProxiLAB")

    # Test if ProxiLAB is connected
    if (ProxiLAB.IsConnected==0):
        sys.exit("ProxiLAB not found") 
    
    # Reset ProxiLAB's configuration
    ProxiLAB.Settings.LoadDefaultConfig()

    #Clear RGPA Output view
    ProxiLAB.Display.ClearOutput()
    
    #Call main function
    SendTclCommand_TypeA(ProxiLAB)
    
