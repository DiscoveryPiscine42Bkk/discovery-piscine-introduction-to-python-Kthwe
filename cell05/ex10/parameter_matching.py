#!/usr/bin/env python3

import sys
parameters=sys.argv
if len(parameters)!=2:
    print("none")
else :
    text=input("What was the parameter? : ")
    if text==parameters[1]:
        print("Good job!")
    else :
        print("Nope , sorry ...")
