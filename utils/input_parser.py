import argparse

def create_parser():
    parse = argparse.ArgumentParser()

    remote_settings = parse.add_argument_group('Remote host Settings')
    remote_settings.add_argument('-rh','--RHOST', help='IP Address of Target Machine', dest="rhost")
    remote_settings.add_argument('-rp','--RPORT', help='Port of Target Machine', dest="rport")

    local_settings = parse.add_argument_group('Local host Settings')
    local_settings = parse.add_argument('-lh','--LHOST', help='IP Address of your local machine', dest="lhost")
    local_settings = parse.add_argument('-lp','--LPORT', help='Port of local machine.', dest="lport")

    global_settings = parse.add_argument_group('Global application Settings')
    global_settings.add_argument('-D', '--debug', default=False, action='store_true', help='Run in debug mode')
    global_settings.add_argument('-p','--protocol', help='Protocol for packets, TCP or UDP' ,dest="protocol")
    
    return parse

def parse_arguments(arguments):
    args = arguments.parse_args()
    return args
    