import parser, os, sys

args = parser.get()
if args.command == '1':
    print(sys.version)
elif args.command == '2':
    os.mkdir('./'.join(args.name))
elif args.command == '3':
    print(os.listdir('..'))
