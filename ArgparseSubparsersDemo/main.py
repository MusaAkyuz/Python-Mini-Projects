import argparse

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(help='sub-command help')
subparsers2 = parser.a
mainA = subparsers.add_parser("mainA")
mainB = subparsers.add_parser("mainB")
mainC = subparsers.add_parser("mainC")

mainA.add_argument("--Aar1")
mainA.add_argument("--Aar2")
mainA.add_argument("--Aar3")

mainB.add_argument("--Bar1")
mainB.add_argument("--Bar2")
mainB.add_argument("--Bar3")

mainC.add_argument("--Car1")
mainC.add_argument("--Car2")
mainC.add_argument("--Car3")

subA = mainA.add_subparsers()

Asub11 = subA.add_parser("Asub11")
Asub22 = subA.add_parser("Asub22")

Asub11.add_argument("-b")
Asub22.add_argument("-c")

parser.add_argument("--sabit")
parser.add_argument("--klassor")




# a = subparsers.add_parser('a')
# c = subparsers.add_parser('c')
# subB = a.add_subparsers()
# b = subB.add_parser("-bb")
# b.add_argument("-c")
# c.add_argument("-l")
# c.add_argument("-g")
# a.add_argument('-b')
# a.add_argument("-d")

args = parser.parse_args()

