# import the library
import os                               # for clearConsole()
import sys                              # for sleepTime() and exit()import Crypto
import time                             # for timeSleep()
import Crypto                           # for cryptography
import binascii                         # for converting binary into ASCII
from Crypto.PublicKey import RSA        # for key pair generating
from Crypto.Cipher import PKCS1_OAEP    # for input encryption

def menu():

    """Display the encryption menu"""

    print("""
    Please choose the Encryption Methods below
    \t0. Exit
    \t1. RSA
    """)
    userChoice = input("Your Choice : ") # user choice
    while (userChoice != '0') and (userChoice != '1'): # error handling
        print("""
        Wrong Input!!!
        Please Try Again
        """)
        userChoice = input("Your Choice : ") # user choice

    if userChoice =='0':    # choice 0 (exit)
        print("""
        Thank You for Using this Cryptography
        See You Again
        """)
        sleepTime()     # call sleepTime() function
        clearConsole()  # call clearConsole() function
        sys.exit()      # exit the program
    elif userChoice == '1': # choice 1 (RSA)
        sleepTime()     # call sleepTime() function
        clearConsole()  # call clearConsole() function
        rsaFunction()   # call rsaFunction() function

def rsaFunction():

    """Encryption with RSA Algorithm"""

    rsaInput = input("Enter RSA String: ")                          # user input for hashing
    print("Please Wait...\n")

    keyPair = RSA.generate(3072)                                    # generate key pair

    pubKey = keyPair.publickey()                                    # public key generating
    print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
    pubKeyPEM = pubKey.exportKey()                                  # public key exporting
    print(pubKeyPEM.decode('ascii'))                                # display the public key
    print("\n")

    print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
    privKeyPEM = keyPair.exportKey()                                # private key exporting
    print(privKeyPEM.decode('ascii'))                               # display the private key
    print("\n")

    encryptor = PKCS1_OAEP.new(pubKey)                              # encryptor
    encrypted = encryptor.encrypt(rsaInput.encode())                # encryption process
    print("Encryption Successful")
    print("The RSA Encryption Result is : ", end ="")
    print(binascii.hexlify(encrypted))                              # printing the encryption result in hexadecimal value
    print("\n")

    menu()                                                          # display the menu again

def clearConsole():

    """Clear the console based on the OS"""

    command = 'clear'               # command for console clearing
    if os.name in ('nt', 'dos'):    # if the machine is running on Windows, then use cls
        command = 'cls'
    os.system(command)              # othen than Windows, use clear

def sleepTime():

    """delaying the process"""

    for remaining in range(3, 0, -1):   # 3 seconds delay
        sys.stdout.write("\r")                                              # carriage return
        sys.stdout.write("Please wait for{:2d} seconds.".format(remaining)) # delay countdown
        sys.stdout.flush()                                                  # flush the buffer
        time.sleep(1)                                                       # delay 1 second
    print("\nComplete!\n")                                                  # end of delay

print("Welcome to Cryptography")    # Title
menu()                              # call menu() function