

#! /usr/bin/python3

import socket
import os.path
import argparse as arg

class ProxyChecker():

    def __init__(self):
        print("Starting the checker...")


    def CheckProxy(self, file, timeout, verbose, output):
        try:
            with open(file, 'r') as f:
                for line in f.readlines():
                    ipAddress = str.split(line, ':')[0]
                    port = str.split(line, ':')[1]
                    proxyIP = (ipAddress, int(port))
                    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
                    s.settimeout(timeout)
                    if verbose:
                        print("[!] - Checking {} ...".format(proxyIP))
                    if s.connect_ex(proxyIP):
                        pass
                    else:
                        self.AddProxy(ipAddress + ":" + str(port), verbose, output)
        except IOError:
            print(file + ' not found')


            
    def AddProxy(self, proxyAddress, verbose, output):
        with open(output, 'a') as f:
            #Duplicate Check:
            with open(output, 'r+') as r:
                if proxyAddress in r.readlines():
                    if verbose:
                        print("[!] - {} already added!".format(proxyAddress))
                else:
                    if verbose:
                        print("[+] - {} added!".format(proxyAddress))
                    f.write(proxyAddress)

def main():
    parser = arg.ArgumentParser()
    parser.add_argument("--file", "-f", type=str, required=True,
                help="File to check.")
    parser.add_argument("--timeout", "-t", type=int, default=2,
                help="Integer time out value, default value is 2 seconds.")
    parser.add_argument("--output", "-o", default="positive.txt",
                help="Output filename, default is 'positive.txt'")
    parser.add_argument("--verbose", "-v", default=False, action="store_true",


