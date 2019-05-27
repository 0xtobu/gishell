from utils import load
from shellcode.x86 import *
from sys import exit
from shellcode.x86 import reverse_TCP
from utils.input_parser import gui

class construc:
    loaded_payloads = load.payloads()
    loaded_encoders = load.encoders()

    def main(self, parsed_userinput):

        if parsed_userinput.list:
            print(gui.info('Avilable payloads:'))

            for key in self.loaded_payloads:
                print("- " + key)

            print('\n')
            print(gui.info('Avilable encoders:'))

            for key in self.loaded_encoders:
                print("- " + key)

            exit(0)

        if parsed_userinput.lhost and parsed_userinput.lport:
            print(gui.success('Creating payload!:'))
            e = reverse_TCP.payload_module(parsed_userinput)
            e.run()

        else:
            print(gui.warning('Could not find LHOST param or LPORT'))