


import argparse
import func

parser = argparse.ArgumentParser(description='Process some integers.')

# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                    const=sum, default=max,
#                    help='sum the integers (default: find the max)')


parser.add_argument('-t','--table',default='targets')
parser.add_argument('-s','--select',)
parser.add_argument('-i','--insert',)
parser.add_argument('-u','--update',)
parser.add_argument('-d','--delete',)

args = parser.parse_args()
print(args)

if args.select is not None:
	
elif args.insert is not None:

elif args.update is not None:

elif args.delete is not None:

else:
	print('Please choose an operation! ')