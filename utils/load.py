import glob
import imp


def payloads():
    loaded_payloads = list
    active_payloads = {}
    for name in glob.glob('shellcode/x86/*.py'):
        if name.endswith(".py") and ("__init__" not in name) and ("template" not in name):
            loaded_payloads = imp.load_source(
                name.replace("/", ".").rstrip('.py'), name)
            active_payloads[name] = loaded_payloads.payload_module

    #print(active_payloads)
    return active_payloads


def encoders():
    loaded_encoders = list
    active_encoders = {}
    for name in glob.glob('encoders/*.py'):
        if name.endswith(".py") and ("__init__" not in name) and ("template" not in name):

            loaded_encoders = imp.load_source(
                name.replace("/", ".").rstrip('.py'), name)
            active_encoders[name] = loaded_encoders.EncoderModule

    return active_encoders
