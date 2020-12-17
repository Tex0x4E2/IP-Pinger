import os, ctypes, time, colorama, requests, random
from colorama import init
from colorama import Fore
from random import randint
import urllib.request
import json
import socket
import sys

IP_PINGER = False
IP_LOOKUP = False
VPN_DETEC = False
init()
RPM = 0
Fail = 0
bytes = 9
count = 0
First = 0
Success = 0
RPMcount = 0
totaltime = 0
SuccessRate = 0
choice = True
choicy = 0
blablablablabla = 0


class ip():

    def __init__(self):

        self.HTTP_headers = ['SERVER_ADDR',
                            'REMOTE_ADDR',
                            'HTTP_CLIENT_IP'
                            ]
        self.HTTP_proxy_header = ['HTTP_VIA',
                                  'VIA',
                                  'Proxy-Connection',
                                  'HTTP_X_FORWARDED_FOR',
                                  'HTTP_FORWARDED_FOR',
                                  'HTTP_X_FORWARDED',
                                  'HTTP_FORWARDED',
                                  'HTTP_CLIENT_IP',
                                  'HTTP_FORWARDED_FOR_IP',
                                  'X-PROXY-ID',
                                  'MT-PROXY-ID',
                                  'X-TINYPROXY',
                                  'X_FORWARDED_FOR',
                                  'FORWARDED_FOR',
                                  'X_FORWARDED',
                                  'FORWARDED',
                                  'CLIENT-IP',
                                  'CLIENT_IP',
                                  'PROXY-AGENT',
                                  'HTTP_X_CLUSTER_CLIENT_IP',
                                  'FORWARDED_FOR_IP',
                                  'HTTP_PROXY_CONNECTION'
                                  ]
        self.ips = ['127.0.0.0', '127.0.0.1', '127.0.0.2', '192.0.0.0', '192.0.0.1', '192.168.0.0',
               '192.168.0.1', '192.168.0.253', '192.168.0.254', '192.168.0.255', '192.168.1.0',
               '192.168.1.1', '192.168.1.253', '192.168.1.254', '192.168.1.255', '192.168.2.0',
               '192.168.2.1', '192.168.2.253', '192.168.2.254', '192.168.2.255', '10.0.0.0', '10.0.0.1',
               '11.0.0.0', '11.0.0.1', '1.0.0.0', '1.0.1.0', '1.1.1.1', '255.0.0.0', '255.0.0.1',
               '255.255.255.0', '255.255.255.254', '255.255.255.255', '0.0.0.0', '::', '0::', '::1',
               '0:0:0:0:0:0:0:0']


        self.ip = ""
        self.hostname = ""
        self.city = ""
        self.region = ""
        self.country = ""
        self.loc = ""
        self.org = ""
        self.is_vpn = False
        return None

    def get(self):

        for header in self.HTTP_headers:
            if self.os(header) is not "":
                self.ip = '127.0.0.0' if self.os(header) in self.ips else self.os(header)
                self.property(self.ip)
            return self



    def os(self, header):
        return os.environ.get(header, '')

    def check(self, ip):
        for header in self.HTTP_proxy_header:
            response = True if self.os(header) is not "" else False
        return response

    def vpn(self, IPAdrress):

        for header in self.HTTP_proxy_header:
            if self.os(header) is not "":
                self.ip = self.os(IPAdrress)
                self.is_vpn = self.check(self, self.ip)
                self.property(self.ip)
            return self


    def property(self, ip):
        ipU= "http://ipinfo.io/{ip}/json".format(ip=ip)
        url_ip = urllib.request.urlopen(ipU).read()
        response = url_ip.decode('utf-8')
        j_response = json.loads(response)
        if j_response.get("bogon", "") == "":
            self.hostname = j_response.get("hostname", "")
            self.city = j_response.get("city", "")
            self.region = j_response.get("region", "")
            self.country = j_response.get("country", "")
            self.loc = j_response.get("loc", "")
            self.org = j_response.get("org", "")
        return self


def is_valid_ipv4_address(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:  # no inet_pton here, sorry
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:  # not a valid address
        return False

    return True

while choice == True:
    ctypes.windll.kernel32.SetConsoleTitleW("Tex's multi-tool")
    if choicy == 99:
        choicy = input(" >> ")
    elif choicy == 0:
        os.system('cls')

        choicy = input(f"{Fore.WHITE}(1) IP PINGER\n(2) IP LOOKUP\n(3) VPN Detection [Debug]\n \n >> ")
    elif choicy == "1":
        os.system("cls")
        IP_PINGER = True
    elif choicy == "2":
        os.system("cls")
        IP_LOOKUP = True
    elif choicy == "3":
        os.system("cls")
        VPN_DETEC = True
    elif choicy != "3" or choicy != "2" or choicy != "1":
        print("Incorrect >> Please only pick an option from the choices above :)")
        choicy = 99
    if IP_LOOKUP == True:
        os.system('cls')
        IPAdrress = input("Enter a IP Address: ")
        if is_valid_ipv4_address(IPAdrress) == True:
            os.system("cls")
            print("-------------------------------------------")
            print(f"Hostname: {ip().property(IPAdrress).hostname}")
            print(f"City: {ip().property(IPAdrress).city}")
            print(f"Region: {ip().property(IPAdrress).region}")
            print(f"Country: {ip().property(IPAdrress).country}")
            print(f"Loc: {ip().property(IPAdrress).loc}")
            print(f"Org: {ip().property(IPAdrress).org}")
            print("-------------------------------------------")
            IP_LOOKUP = False
        else:
            print(f"{Fore.CYAN} {IPAdrress}{Fore.WHITE} - {Fore.RED} is not a vaild IP Address...{Fore.WHITE}")

        exit_ = input(f"{Fore.MAGENTA}Would you like to exit? (Y/N):{Fore.YELLOW} ")
        if exit_.lower() == "y":
            sys.exit(1)
        elif exit_.lower() == "n":
            choicy = 0
        else:
            print("Input was incorrect exiting...")
            sys.exit(1)

    if VPN_DETEC == True:
        os.system('cls')
        IPAdrress = input("Enter a IP Address: ")
        if is_valid_ipv4_address(IPAdrress) == True:
            is_vpn = ip().check(IPAdrress)
            os.system("cls")
            if is_vpn == True:
                print(f"{IPAdrress} - True")
            else:
                print(f"{IPAdrress} - False")
        else:
            print(f"{Fore.CYAN} {IPAdrress}{Fore.WHITE} - {Fore.RED} is not a vaild IP Address...{Fore.WHITE}")
        exit_ = input(f"{Fore.MAGENTA}Would you like to exit? (Y/N):{Fore.YELLOW} ")
        if exit_.lower() == "y":
            sys.exit(1)
        elif exit_.lower() == "n":
            choicy = 0
        else:
            print("Input was incorrect exiting...")
            sys.exit(1)
    while IP_PINGER == True:
        try:
            ctypes.windll.kernel32.SetConsoleTitleW("Tex's multi-tool")
            ip = input("IP address    | ")
            response = os.popen(f"ping {ip} -n 1 -l {bytes}").read()
            if "General failure" in response:
                First = 69
            elif "Ping request could not find host" in response:
                First = 69
            else:
                First = 0
            while IP_PINGER == True:
                if First == 0:
                    time.sleep(1)
                    First = 69
                ctypes.windll.kernel32.SetConsoleTitleW(f"Tex's multi-tool | Success: {Success}   Fail: {Fail}   Pings: {count}   PPS: {RPM}   SuccessRate: {SuccessRate}")
                count += 1
                RPMcount += 1
                start_time = time.time()
                response = os.popen(f"ping {ip} -n 1 -l {bytes}").read()
                Received_loc = response.find("Received = ")
                Delaytim_loc = response.find("Average = ")
                ms_loc = response.find("ms")
                Received_loc += 11
                Delaytim_loc += 10
                ms_loc += 1
                ReceivedNoti = response[Received_loc:Received_loc + 1]
                ResponseNoti = response[Delaytim_loc:]
                blablabla = (len(ResponseNoti))
                blablabla -= 1
                ResponseNoti = ResponseNoti[:blablabla]
                CurrentRound = time.time() - start_time
                if "General failure" in response:
                    First = 69
                    print("General Failure. Please try again.")
                    break
                
                if "Ping request could not find host" in response:
                    First = 69
                    print(response)
                    break
                if int(ReceivedNoti) == 1 and "Destination host unreachable" not in response:
                    status = "ONLINE"
                elif int(ReceivedNoti) == 0:
                    status = "OFFLINE"
                CurrentRound = time.time() - start_time
                totaltime = totaltime + CurrentRound
                if totaltime >= 1:
                    RPM = RPMcount
                    totaltime = 0
                    RPMcount = 0
                Whitespace_one_one = 6 - len(ResponseNoti)
                Whitespace_one = Whitespace_one_one * " "
                if status == "ONLINE":
                    Success += 1
                    print(f'{Fore.WHITE}|{Fore.WHITE}  CONNECTION STATUS - {Fore.GREEN}ONLINE  {Fore.WHITE}|{Fore.WHITE} IP - {Fore.GREEN}{ip} {Fore.WHITE}|{Fore.WHITE} DELAY - {Fore.GREEN}{ResponseNoti}{Whitespace_one}{Fore.WHITE}|{Fore.WHITE}')
                else:
                    Fail += 1
                    print(f'{Fore.WHITE}|{Fore.WHITE}  CONNECTION STATUS - {Fore.RED}DOWNED  {Fore.WHITE}|{Fore.WHITE} IP - {Fore.RED}{ip} {Fore.WHITE}|{Fore.WHITE} DELAY - {Fore.RED}ZERO  {Fore.WHITE}|{Fore.WHITE}')
                SuccessRateNum = Success/count * 100
                SuccessRateNum = round(SuccessRateNum,1)
                SuccessRate = (str(SuccessRateNum) + "%")
        except KeyboardInterrupt:
            print("Restarting now...")
            count       = 0
            First       = 0
            RPM         = 0
            SuccessRate = 0
            Success     = 0
            Fail        = 0
            time.sleep(1)
