from utils import input_parser
from utils.runtime import construc
from utils.input_parser import gui



def main():
    print(gui.logo())
    raw_user_input = input_parser.create_parser()
   
    user_arguments = input_parser.parse_arguments(raw_user_input)

    runtime = construc()
    runtime.main(user_arguments)

if __name__ == '__main__':
    main()