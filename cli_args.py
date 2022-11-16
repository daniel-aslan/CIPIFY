#! /usr/bin/env python3
#from argparse import ArgumentParser
import argparse
'''
Options that are needed
WO#
OS = Linux or Windows
url = 
SME filling out the checklist
'''

def print_sme(SME):
    print(SME)

def print_os(OS):
    print(OS)

def print_wo(WO):
    print(WO)

def main_cli():
    parser = argparse.ArgumentParser(
        description='Create file structure for new CIP Work orders',
    )
    parser.version = '0.1'
    parser.add_argument(
        'num',
        type=int,
        help='What is the work order number?'        
        )
    parser.add_argument(
        'o',
        type=str,
        choices=['Linux', 'Windows'],
        help='What is the Operating System Linux or Windows?'        
        )
    parser.add_argument(
        'e',
        type=str.capitalize,
        choices=['USER1', 'USER2', 'USER3'],
        help='Who is the SME filling out the CIPification documentation?'
        )
    parser.add_argument(
        '-v',
        action='version'
        )

    args = parser.parse_args()
    return args

def main():
    #This is the key to using argparse in a separate function ---> args = func()
    args = main_cli()
    print_sme(args.e)
    print_os(args.o)
    print_wo(args.num)

if __name__ == "__main__":
    main()