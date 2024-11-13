from easy1.LinkedList1Bundle import *
from easy1.ListBundle import ListBundle
from easy1.BTreeBundle1 import *
from easy1.StringBundle import *
from easy1.BinaryBundle import * 
from easy1.NumbersBundle import *
from easy1.MyStack import *

import math


def main():
    while True:
        print("\n[ MAIN MENU ] ")

        print("99. to Exit")
        x = int(input("Type option:"))
        match x:
            case 99: exit()

main()