# Quick example to understand args
import sys
args = sys.argv[1:]
todir = '1'
if args[0] == '--todir': 
    todir = args[1]
    del args[0:2]
    print('aaa')
    print(todir)

