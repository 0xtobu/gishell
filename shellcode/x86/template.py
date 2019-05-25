import ctypes
import struct
import binascii
import os
import socket
from keystone import *
from utils.input_parser import sockaddr


class payload_module:

    def __init__(self):
        self.name = "Payload Template"
        self.description = "Used to create a template for "
        self.cli_name = "payload_template"
        self.platform = None
        self.arch = None
        self.lport = None
        self.lhost = None
        self.shellcode = None
        self.encoded_shellcode = None
        self.size = None
        self.assembly = None
        self.address = str

    @staticmethod
    def generate_shellcode(assembly):
        engine = Ks(KS_ARCH_X86, KS_MODE_64)
        shellcode, size = engine.asm(assembly)
        shellcode = bytearray(shellcode)
        
        return shellcode

    @staticmethod
    def view_shellcode(raw_shellcode):
        LINE_LENGTH = 40
        raw = binascii.hexlify(raw_shellcode)
        escaped = (b"\\x" + b"\\x".join(raw[i:i+2]
                                        for i in range(0, len(raw), 2))).decode('utf-8')
        lines = [escaped[i: i+LINE_LENGTH]
                 for i in range(0, len(escaped), LINE_LENGTH)]
        return "shellcode = \tb\"" + "\"\nshellcode += \tb\"".join(lines) + "\""

    @staticmethod
    def configure_socketaddr(lhost, lport):
        return sockaddr(lhost, lport)
