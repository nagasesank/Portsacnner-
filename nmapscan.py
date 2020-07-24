#!/usr/bin/python3

import nmap

scanner = nmap.Portscanner()

print("Welcome ,This is a simple nmap automation tool")
print("<---------------------------------------------")

 ip_addr= input("Please enter the ip address u want to scan")
 print("the ip you enter is:",ip_addr)
 type(ip_addr)

resp = input("""\n Please enter the type of scan you want to run
                 1) SYN ACK Scan
                 2) UDP Scan
                 3) Comprehensive Scan \n """)
print(" You Selected option :",resp) 

if resp=='1':
    print("NMAP Version ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("IP status :", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Port:", Scanner[ip_addr]['tcp'].keys())
elif resp == '2':
    print("NMAP Version ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print("IP status :", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Port:", Scanner[ip_addr]['udp'].keys())
elif resp =='3':
    print("NMAP Version ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("IP status :", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Port:", Scanner[ip_addr]['tcp'].keys())
else resp >== '4':
    print("please enter a vaild option")    
