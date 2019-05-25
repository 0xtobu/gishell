import argparse
import struct
import socket
import binascii


def create_parser():
    parse = argparse.ArgumentParser()

    remote_settings = parse.add_argument_group('Remote host Settings')
    
    remote_settings.add_argument(
        '-rh', '--RHOST', help='IP Address of Target Machine', dest="rhost")
    
    remote_settings.add_argument(
        '-rp', '--RPORT', help='Port of Target Machine', dest="rport")

    local_settings = parse.add_argument_group('Local host Settings')

    local_settings.add_argument(
        '-lh', '--LHOST', help='IP Address of your local machine', dest="lhost")
    local_settings.add_argument(
        '-lp', '--LPORT', help='Port of local machine.', dest="lport", type=int)

    global_settings = parse.add_argument_group('Global application Settings')
    global_settings.add_argument(
        '-D', '--debug', default=False, action='store_true', help='Run in debug mode')
    global_settings.add_argument(
        '-p', '--protocol', help='Protocol for packets, TCP or UDP', dest="protocol")
    global_settings.add_argument(
        '-L', '--list', default=False, action='store_true', help='Lists active encoders and payloads.')

    return parse


def parse_arguments(arguments):
    args = arguments.parse_args()
    return args


def sockaddr(LHOST, LPORT):

    family = struct.pack('H', socket.AF_INET)
    portbytes = struct.pack('H', socket.htons(LPORT))
    ipbytes = socket.inet_aton(LHOST)
    number = struct.unpack('Q', family + portbytes + ipbytes)
    number = -number[0]

    value = "0x" + binascii.hexlify(struct.pack('>q', number)).decode('utf-8')

    return value
