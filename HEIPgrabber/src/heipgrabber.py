import re
import sys
ipList = set("")
ipBanned = set("")

#This function takes in a list of ip's then if they are not
# already there and not banned it addes them ot the list.
def verify_ips(listToAdd):
    for ip in listToAdd:
        if (ip not in ipBanned):
            if ip not in ipList:
                ipList.add(ip)

#This function adds a IP to the banned list if it is not
# already there.
def add_to_banned(listToAdd):
    for ip in listToAdd:
        if (ip not in ipBanned):
            ipBanned.add(ip)

#This function extracts the ip form a large text string or a
# files contents
def extract_ips(fileContent):
    pattern = r"((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)([ (\[]?(\.|dot)[ )\]]?(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3})"
    ips = [each[0] for each in re.findall(pattern, fileContent)]   
    for item in ips:
        location = ips.index(item)
        ip = re.sub("[ ()\[\]]", "", item)
        ip = re.sub("dot", ".", ip)
        ips.remove(item)
        ips.insert(location, ip) 
    return ips

#This is the basic single IP add
def add_ip():
    ip_to_add = input("IP to add:")
    verify_ips(extract_ips(ip_to_add))

#This is the basic add ip to ban list
def ban_ip():
    ip_to_add = input("IP to ban:")
    add_to_banned(extract_ips(ip_to_add))
    
#This prints a set of ips
def print_ip_list(ipsToPrint):
    print("Num ip's: " + str(len(ipsToPrint)) )
    for ip in ipsToPrint:
        print(ip)

#This is where i intend to implemet pasting of a log into the console
# to add many ips to the list
def add_many_ips():
    to_ip=""
    lineIn=""
    while lineIn != "END":
        lineIn = input("")
        to_ip = to_ip + input()
    print(to_ip)
    verify_ips(extract_ips(to_ip))

def purge():
    oldSet = ipList.copy()
    ipList.clear()
    for ip in oldSet:
        verify_ips(ip)

def export_lists():
    pass
#The main menu of the util
def menu():
    choice=""
    while choice!="-1":
        print(  "==============================\n"+
                "Main Menu:\n"+
                "  1) Add ip to hack list.\n"+
                "  2) Add many ip's to hack list.(unimplemented)\n"+
                "  3) Import ip's from file.(unimplemented)\n"+
                "  4) Add ip to banned list.\n"+
                "  5) Print Hack list.\n"+
                "  6) Print Banned list.\n"+
                "  7) Export Lists.(unimplemented)\n"+
                "  8) Purge banned ips.\n"+
                " -1) Exit.")
        choice = input("Option:")
        if choice == "1":
            add_ip()
        elif choice == "2":
            add_many_ips()
        elif choice == "4":
            ban_ip()
        elif choice == "5":
            print_ip_list(ipList)
        elif choice == "6":
            print_ip_list(ipBanned)
        elif choice == "7":
            print("you chose 7")
        elif choice == "8":
            purge()
        elif choice == "-1":
            pass
        else:
            print("Invalid option.")
    print("Exiting...")

#Main function
#If there is one argument it is assumed to be a to hack list
#if there are two arguments the first is the hack list the
#   secound is the banned list
#example:
#   python heipgrabber.py
#   python heipgrabber.py toHack.txt
#   python heipgrabber.py toHack.txt banList.txt
def main():
    if len(sys.argv)>2: #if there is a secound argument given
        with open(sys.argv[2], 'r') as myfile:
            data=myfile.read().replace('\n', '')
        add_to_banned(extract_ips(data))
    if len(sys.argv)>1: #if there is a argument given
        with open(sys.argv[1], 'r') as myfile:
            data=myfile.read().replace('\n', '')
        verify_ips(extract_ips(data))   
    menu()

main()
