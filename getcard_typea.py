# This code and associated information is provided to guide KEOLABS'
# customers in their use of KEOLABS' testing tools. KEOLABS shall not be
# liable for any direct, indirect or consequential damages with respect
# to claims arising from the content and/or its use by the KEOLABS' customers.
# For more information, refer to KEOLABS Sales Conditions at www.keolabs.com.

"""
@file   GetCard_TypeA.py
@brief  This is an example to send a GetCard command in type A to a tag.
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
    
#Function main()
def GetCard_TypeA(proxilab):

    error = 0
    PcdBitrate = 106
    PiccBitrate = 106
    
    #Set ProxiLAB in Reader mode
    ProxiLAB.Settings.Mode = ProxiLABUtilities.Constants.MODE_READER_AB
    
    #Set the field Off
    ProxiLAB.Reader.PowerOff()
    
    OUTPUT_FILE_PATH = os.getcwd()
    #Configure the trace
    ProxiLAB.Spy.OutputFile = OUTPUT_FILE_PATH + "\\temp.trc"
    
    #Configure the analyzer
    ProxiLAB.Spy.Analyzer.ISO14443Enable = 1
    ProxiLAB.Spy.Analyzer.ISO15693Enable = 0
    ProxiLAB.Spy.Analyzer.ISO18092Enable = 0
    ProxiLAB.Spy.Analyzer.JISX6319Enable = 0
    ProxiLAB.Spy.Analyzer.DisplaySMA1 = 1
    ProxiLAB.Spy.Analyzer.InputFile = ProxiLAB.Spy.OutputFile
    ProxiLAB.Spy.Analyzer.OutputFile = OUTPUT_FILE_PATH + "\\temp.xgpa"
    
    
    #Start the trace
    error = ProxiLABUtilities.StartSpy(proxilab)
    if(error):
        sys.exit("Spy Start error")
        
    
    #Set the field On
    ProxiLAB.Reader.Power_1024(600)
    ProxiLAB.Delay(200)
    
    
    
    err                     = 1
    AFI                     = 0x00
    ISO14443_compliant      = ProxiLABUtilities.CreateVARIANT()
    CID_x                     = ProxiLABUtilities.CreateVARIANT()
    ATQB                    = ProxiLABUtilities.CreateVARIANT()
    PcdBitRate              = 106
    PiccBitRate            = 106
    
    err = ProxiLAB.Reader.ISO14443.TypeA.GetCard(AFI, PcdBitRate, PiccBitRate, ISO14443_compliant, CID_x, ATQB)
    print(CID_x) # this is UID actually, parameters mixed in eg
    #win32com.client.VARIANT(24592, (4, 56, 99, 1, 18, 8, 7)) decimal equals in hex:
    #quest log: 04 38 63 01 12 08
    print(ISO14443_compliant)
    
    #--------------------Send Request GetCard TypeA--------------------#    
    
    #Get Card
    ISO14443_4 = []
    CID = []
    UID = []
    #test x
    #UID                     = ProxiLABUtilities.CreateVARIANT()
    ATS = []
    msg = str()
    
    #Send Request and get answer
    print("custom_cmd")
    ProxiLAB.Emulator.ISO14443.TypeA.Enable = 1
    error = ProxiLAB.Reader.ISO14443.TypeA.GetCard(PcdBitrate, PiccBitrate, ISO14443_4, CID, UID, ATS)
    print("custom_cmd")
    
    
    if (error):
        #Display the error
        msg = "Send command A: {0}.".format(ProxiLAB.GetErrorInfo(error))
        print('GetCard_TypeA', msg, 0)
        #Mbox('GetCard_TypeA', msg, 0)
    else:
        #Display the answer
        print('GetCard_TypeA', 'Card Found !', 1)
        #Mbox('GetCard_TypeA', 'Card Found !', 1)
        
    print(ISO14443_4)
    print("2 ", CID)
    print("3 ", UID)
    print(id(UID))
    #print(UID[0])
    print("4 ", ATS)
    print("5 ", msg)
    
    
    #Power off
    ProxiLAB.Reader.PowerOff()
    ProxiLAB.Delay(10)
    
    #Stop the trace
    ProxiLABUtilities.StopSpy(proxilab)
    

if __name__ == "__main__":

    # Create ProxiLAB COM object
    ProxiLAB = win32com.client.Dispatch("KEOLABS.ProxiLAB")

    # Test if ProxiLAB is connected
    if (ProxiLAB.IsConnected==0):
        print('GetCard_TypeA', 'ProxiLAB not found', 0) 
        #Mbox('GetCard_TypeA', 'ProxiLAB not found', 0) 
        
    # Reset ProxiLAB's configuration
    ProxiLAB.Settings.LoadDefaultConfig()

    #Clear RGPA Output view
    ProxiLAB.Display.ClearOutput()
        
    #Call main function
    GetCard_TypeA(ProxiLAB)
        
