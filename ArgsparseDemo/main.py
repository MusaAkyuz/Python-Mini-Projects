import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-H", "--hello", type=str, help="saying hello")
parser.add_argument("-b", "--bye", help="saying bye", action="store_true")
parser.add_argument("integer", type=int, help="To sum")
parser.add_argument("-i", "--inte", type=int, dest="show", help="show integer")
parser.add_argument("-s", "--sum", action="store_true")

args = parser.parse_args()

if args.hello:
    print("Hello " + args.hello)

if args.bye:
    print("Bye")

if args.show:
    print(args.integer)

if args.sum:
    print(args.integer + args.show)
