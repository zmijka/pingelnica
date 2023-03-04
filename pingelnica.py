import os, sys, getopt, ipaddress
from colorama import Fore, Style


# Function usage (help)
def usage():
    print(f"Usage: pingelnica [OPTION] IP or file\n")
    print(f"[OPTION]:")
    print(f"-i: IP address".format("-i", "IP address"))
    print(f"-f: file".format("-f", "file name"))
    print(f"-h: This help\n".format("-h", "This help"))
    print(f"App home page: https://github.com/zmijka/pingelnica")
    
   
# Function open IP address from file
def from_file(filename):
    
    try:
        with open(filename, 'r') as f:
            for row in f:
                ping(row.rstrip())
        f.close()
    # File not found 
    except FileNotFoundError:
        print(f"Sorry, file not found!!!\n")
        usage()


# Function ping
def ping(dest):
    # validates the IP address and ping IP or hosts from file
    try:
        ip_object = ipaddress.ip_address(dest)
        response = os.system("ping -c 1 -w 1 " + dest + " > /dev/null")

        if response == 0:
            # Host UP
            print(dest + Fore.GREEN + " is UP" + Style.RESET_ALL)
        else:
            # Host DOWN
            print(dest + Fore.RED + " is DOWN" + Style.RESET_ALL)
    # Address IP not correct
    except ValueError:
        print(dest + " <- Invalid IP address!!!")


# Function main
def main():
    
    # Get [OPTION] + <destination>
    argv = sys.argv[1:3]
    # <destination> 
    arg = ''
    
    try:
        opts, args = getopt.getopt(argv, "h:i:f:")
    
    # Arguments not correct
    except getopt.error:
        usage()
        sys.exit(2)
    
    for opt, arg in opts:
        # Help option
        if opt == '-h':
            usage()
            sys.exit(0)
        # Ping IP address option
        elif opt in ("-i"):
            ping(arg)
        # Ping from file option
        elif opt in ("-f"):
            from_file(arg)
    

if __name__ == "__main__":
    main()
