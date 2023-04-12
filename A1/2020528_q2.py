
import hashlib
import hmac
from base64 import urlsafe_b64decode as b64d
from base64 import urlsafe_b64encode as b64e

def crackSecret(JWTToken):
    '''
    returns secret of 5 characters
    using brute force methods
    '''
    SecretString = 'abcdefghijklmnopqrstuvwxyz0123456789'
    for i in range(0, len(SecretString)):
        for j in range(0, len(SecretString)):
            for k in range(0, len(SecretString)):
                for l in range(0, len(SecretString)):
                    for m in range(0, len(SecretString)):
                        cracked = SecretString[i] + SecretString[j] + SecretString[k] + SecretString[l] + SecretString[m]
                        if(verify(JWTToken, cracked)):
                            return cracked
                        
def changetoken(JWTToken, Secret):
    '''
    creates a new JWT with
    the same secret, and 
    the role changed to “admin”
    '''
    (Header,Payload,Signature) = breakJWT(JWTToken)

    PaddedPayload = Payload + '='*(-len(Payload)%3)
    DecodedPayload = (b64d(PaddedPayload)).decode()
    EditPayload = DecodedPayload.replace("user", "admin" )
    NewPayload = b64e(EditPayload.encode()).decode().strip('=')

    NewMessage = Header + '.' + NewPayload
    NewMessageEncode = NewMessage.encode()
    SecretEncode = Secret.encode()
    NewSignature = hmac.new(SecretEncode, NewMessageEncode, hashlib.sha256).digest()
    NewSignatureEncode = b64e(NewSignature)
    NewSignatureDecode = NewSignatureEncode.decode().strip('=')
    return (NewMessage + '.' + NewSignatureDecode)

def verify(JWTToken,Secret):
    '''
    function takes jwt token and secret
    and returns true if they verify the
    signature and false otherwise
    '''
    (Header,Payload,Signature) = breakJWT(JWTToken)
    Message = Header + '.' + Payload

    MessageEncode = Message.encode()
    SecretEncode = Secret.encode()
    SignatureTemp1 = hmac.new(SecretEncode, MessageEncode, hashlib.sha256).digest()
    SignatureTemp2 = hmac.new(SecretEncode, MessageEncode, hashlib.sha384).digest()
    SignatureTemp3 = hmac.new(SecretEncode, MessageEncode, hashlib.sha512).digest()

    SignatureTempEncode1 = b64e(SignatureTemp1)
    SignatureTempEncode2 = b64e(SignatureTemp2)
    SignatureTempEncode3 = b64e(SignatureTemp3)
    
    SignatureTempDecode1 = SignatureTempEncode1.decode().strip('=')
    SignatureTempDecode2 = SignatureTempEncode2.decode().strip('=')
    SignatureTempDecode3 = SignatureTempEncode3.decode().strip('=')

    if(SignatureTempDecode1 == Signature):
        return True
    elif(SignatureTempDecode2 == Signature):    
        return True
    elif(SignatureTempDecode3 == Signature):
        return True
    else:
        return False

def verifyJwt(JWTToken,Secret):
    '''
    takes in a JWT and a secret as
    arguments. Validate the token’s
    signature against the supplied 
    secret. If it is valid, return the
    decoded payload. Otherwise,
    throw an exception.
    '''
    if(verify(JWTToken,Secret)):
        (Header,Payload,Signature) = breakJWT(JWTToken)
        PaddedPayload = Payload + '='*(-len(Payload)%3)
        DecodedPayload = (b64d(PaddedPayload)).decode()
        return DecodedPayload
    else:
        raise Exception("Secret Mismatch Exception")

def breakJWT(JWTToken):
    '''
    splits jwt token into
    header, payload and signature
    and returns them as a tuple
    '''
    JWTSplit = JWTToken.split(".")
    Header = JWTSplit[0]
    Payload = JWTSplit[1]
    Signature = JWTSplit[2]
    return (Header, Payload, Signature)

if __name__ == '__main__':
    JWTToken = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJmY3MtYXNzaWdubWVudC0xIiwiaWF0IjoxNTE2MjM5MDIyLCJleHAiOjE2NzI1MTE0MDAsInJvbGUiOiJ1c2VyIiwiZW1haWwiOiJhcnVuQGlpaXRkLmFjLmluIiwiaGludCI6Imxvd2VyY2FzZS1hbHBoYW51bWVyaWMtbGVuZ3RoLTUifQ.LCIyPHqWAVNLT8BMXw8_69TPkvabp57ZELxpzom8FiI'
    #verifyJwt(JWTToken, "nakul")
    Secret = crackSecret(JWTToken)
    #Secret = 'p1gzy'
    print("Secret: " + Secret)
    print("Edited JWTToken: ")
    print(changetoken(JWTToken,Secret))

   