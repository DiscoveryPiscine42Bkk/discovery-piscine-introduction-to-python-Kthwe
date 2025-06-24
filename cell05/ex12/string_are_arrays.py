#!/usr/bin/env python3
import sys
if len(sys.argv) != 2:
    print("none")
else:
    input_str = sys.argv[1]
    z_chars = [char for char in input_str if char == 'z']
    
    if z_chars:
        print(''.join(z_chars))
    else:
        print("none")
