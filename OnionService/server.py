import sys, os, subprocess
from stem.control import Controller
from termcolor import colored
from os import system, path, stat
from time import sleep
from pwd import getpwuid

def process_up(p):
    try:
        call = subprocess.check_output("pidof '{}'".format(p), shell=True)
        return True
    except subprocess.CalledProcessError:
        return False

def find_owner(filename):
    return getpwuid(stat(filename).st_uid).pw_name

##################################################################################################################
# Checks for configuration for running

if __name__ == "__main__":
    try:

        if os.getuid() != 0:
            print(colored("[-] You are not root. Run me as root", 'red'))
            sys.exit(0)
        else:
            print(colored("[+] You are root!. Continuing...", 'green'))
        try:
            with open("/etc/tor/torrc", 'r+') as torrc:
                torrc_filtered = "\n".join(torrc.read().split("\n"))
                if "ControlPort 9051" in torrc_filtered and "#ControlPort 9051" in torrc_filtered:
                    print(colored("[+] Control port enabled!", 'green'))
                elif "ControlPort 9051" in torrc_filtered and "#ControlPort 9051" not in torrc_filtered:
                    print(colored("[+] Control port enabled!", 'green'))

                elif "#ControlPort 9051" in torrc_filtered:
                    print(colored("[-] Control port is not enabled. Enabling it...", 'red'))
                    torrc.seek(0)
                    torrc.write(torrc_filtered.replace("#ControlPort 9051", 'ControlPort 9051'))

                elif "ControlPort 9051" not in torrc_filtered and "#ControlPort 9051" not in torrc_filtered:  
                    print(colored("[-] Control port is not enabled. Enabling it...", 'red'))
                    torrc.seek(0)
                    torrc.write(torrc_filtered + "ControlPort 9051")

        except FileNotFoundError:
            print(colored("[-] Tor is not installed, installing it...", 'red'))
            system("apt install tor -y 0>/dev/null 1>/dev/null 2>/dev/null")
            print(colored("[+] Tor instalation finished!", 'green'))
            system("echo 'SocksPort 9050' > /etc/tor/torrc")
            system("echo 'ControlPort 9051' >> /etc/tor/torrc")


        if process_up("tor"):
            print(colored("[+] Tor is running!", 'green'))
        else:
            print(colored("[-] Tor is not running, starting it...", 'red'))
            system(f"""sudo -u {find_owner(str(path.abspath(__file__)).replace("server.py", "service/"))} tor 0>/dev/null 1>/dev/null 2>/dev/null &""")
            sleep(5)

################################################################################################################################
####### Variables for functionality
        port = int(input(colored("[i] service port: ", 'yellow')))  # service port
        host = str(input(colored("[i] service host: ", 'yellow')))  # service host
        hidden_svc_dir = str(path.abspath(__file__)).replace("server.py", "service")

        system(f"rm -rf {hidden_svc_dir}/*")   # for new .onion domain
        system(f"chmod 700 {hidden_svc_dir}") # for avoiding error "too permisive"

######################################################################################################################
####### starting tor domain

        print(colored("[+] Getting controller", 'green'))

        controller = Controller.from_port(address="127.0.0.1", port=9051) #Connect to controller tor port

        
        controller.authenticate(password="")
        controller.set_options([
            ("HiddenServiceDir", hidden_svc_dir),
            ("HiddenServicePort", "80 %s:%s" % (host, str(port)))
            ])
        svc_name = open(hidden_svc_dir + "/hostname", "r").read().strip()
        print(colored(f"[i] Created host: {svc_name}", 'yellow'))

        while True:
            sleep(1000)


    except KeyboardInterrupt:
        print(colored("[+] Exiting!", 'green'))
