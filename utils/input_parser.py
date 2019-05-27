import argparse
import struct
import socket
import binascii
from colorama import Fore, Style


def create_parser():
    parse = argparse.ArgumentParser()

    remote_settings = parse.add_argument_group("Remote host Settings")

    remote_settings.add_argument(
        "-rh", "--RHOST", help="IP Address of Target Machine", dest="rhost"
    )

    remote_settings.add_argument(
        "-rp", "--RPORT", help="Port of Target Machine", dest="rport"
    )

    local_settings = parse.add_argument_group("Local host Settings")

    local_settings.add_argument(
        "-lh", "--LHOST", help="IP Address of your local machine", dest="lhost"
    )
    local_settings.add_argument(
        "-lp", "--LPORT", help="Port of local machine.", dest="lport", type=int
    )

    global_settings = parse.add_argument_group("Global application Settings")
    global_settings.add_argument(
        "-D", "--debug", default=False, action="store_true", help="Run in debug mode"
    )
    global_settings.add_argument(
        "-p", "--protocol", help="Protocol for packets, TCP or UDP", dest="protocol"
    )
    global_settings.add_argument(
        "-L",
        "--list",
        default=False,
        action="store_true",
        help="Lists active encoders and payloads.",
    )

    return parse


def parse_arguments(arguments):
    args = arguments.parse_args()
    return args


def sockaddr(LHOST, LPORT):

    family = struct.pack("H", socket.AF_INET)
    portbytes = struct.pack("H", socket.htons(LPORT))
    ipbytes = socket.inet_aton(LHOST)
    number = struct.unpack("Q", family + portbytes + ipbytes)
    number = -number[0]

    value = "0x" + binascii.hexlify(struct.pack(">q", number)).decode("utf-8")

    return value


class gui:
    @staticmethod
    def error(message):
        return '[' + Fore.RED + 'x' + Style.RESET_ALL + '] ' + message

    @staticmethod
    def info(message):
        return '[' + Fore.LIGHTBLUE_EX + '*' + Style.RESET_ALL + '] ' + message

    @staticmethod
    def success(message):
        return '[' + Fore.GREEN + '+' + Style.RESET_ALL + '] ' + message

    @staticmethod
    def warning(message):
        return '[' + Fore.YELLOW + '!' + Style.RESET_ALL + '] ' + message

    @staticmethod
    def logo():
        return Fore.RED + '''
 _____ _____    _          _ _ 
|  __ \_   _|  | |        | | |
| |  \/ | | ___| |__   ___| | |
| | __  | |/ __| '_ \ / _ \ | |
| |_\ \_| |\__ \ | | |  __/ | |
 \____/\___/___/_| |_|\___|_|_|
                                                             
''' + Style.RESET_ALL + '''
.+´ GIshell v1.0 `+.
        '''