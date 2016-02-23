# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import re
import sys
ipList = set("")
ipBanned = set("")

def verify_ips(listToAdd):
    for ip in listToAdd:
        if (ip not in ipBanned):
            if ip not in ipList:
                ipList.add(ip)
                
def add_to_banned(listToAdd):
    for ip in listToAdd:
        if (ip not in ipBanned):
            ipBanned.add(ip)
        
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

def add_ip():
    ip_to_add = input("IP to add:")
    verify_ips(extract_ips(ip_to_add))
    
def ban_ip():
    ip_to_add = input("IP to ban:")
    add_to_banned(extract_ips(ip_to_add))
    
def print_ip_list(ipsToPrint):
    for ip in ipsToPrint:
        print(ip)

def add_many_ips():
    to_ip=""
    lineIn=""
    while lineIn != "END":
        lineIn = input("")
        to_ip = to_ip + input()
    print(to_ip)
    verify_ips(extract_ips(to_ip))
    
def menu():
    choice=""
    while choice!="-1":
        print(  "==============================\n"+
                "Main Menu:\n"+
                "  1) Add ip to hack list.\n"+
                "  2) Add many ip's to hack list.(unimplemented)\n"+
                "  3) Add ip to banned list.\n"+
                "  4) Print Hack list.\n"+
                "  5) Print Banned list.\n"+
                "  6) Export Lists.(unimplemented)\n"+
                " -1) Exit.")
        choice = input("Option:")
        if choice == "1":
            add_ip()
        elif choice == "2":
            add_many_ips()
        elif choice == "3":
            ban_ip()
        elif choice == "4":
            print_ip_list(ipList)
        elif choice == "5":
            print_ip_list(ipBanned)
        elif choice == "6":
            print("you chose 6")
        elif choice == "-1":
            pass
        else:
            print("Invalid option.")
    print("Exiting...")

def main():
    if len(sys.argv)>1:
        with open(sys.argv[1], 'r') as myfile:
            data=myfile.read().replace('\n', '')
        verify_ips(extract_ips(data))
    if len(sys.argv)>2:
        with open(sys.argv[2], 'r') as myfile:
            data=myfile.read().replace('\n', '')
        add_to_banned(extract_ips(data))
    menu()
    
main()