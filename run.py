from utils import input_parser
from utils.runtime import construc



def main():
    raw_user_input = input_parser.create_parser()
   
    user_arguments = input_parser.parse_arguments(raw_user_input)

    runtime = construc()
    runtime.main(user_arguments)

if __name__ == '__main__':
    main()