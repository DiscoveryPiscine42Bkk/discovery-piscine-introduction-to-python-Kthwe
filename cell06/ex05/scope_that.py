#!/usr/bin/env python3

def scope_that(arg):
    arg+=1
    return

value=5
print(f"Original value : {value}")
scope_that(value)
print(f"After function is called : {value}")