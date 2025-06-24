#!/usr/bin/env python3

import sys
if len(sys.argv) != 3:
    print("none")
else:
    keyword = sys.argv[1]
    search_str = sys.argv[2]
    count = search_str.count(keyword)
    if count == 0:
        print("none")
    else:
        print(count)