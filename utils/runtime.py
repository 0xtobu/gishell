from utils import load
from shellcode.x86 import *
from sys import exit
from shellcode.x86 import reverse_TCP

class construc:
    loaded_payloads = load.payloads()
    loaded_encoders = load.encoders()

    def main(self, parsed_userinput):

        if parsed_userinput.list:
            print('\nAvilable payloads:')
            for key in self.loaded_payloads:
                print(key)

            print('\nAvilbable encoders:')

            for key in self.loaded_encoders:
                print(key)

            exit(0)

        #for payload_module in self.loaded_payloads:
        #    print(payload_module.lower())

        e = reverse_TCP.payload_module(parsed_userinput)
        e.run()