import argparse
import patoolib
import pathlib
import shutil

parser = argparse.ArgumentParser()

parser.add_argument("-e", "--extract",                  action="store_true",    help="extract file/files",)
parser.add_argument("-c", "--compress",                 action="store_true",    help="compress file/files")
parser.add_argument("-o", "--output-dir",   type=str,   dest="OUTPUT",          help="Output directory to save changes",    default=None)
parser.add_argument("-f", "--file",         type=str,   dest="FILE",            help="Single file to be processed",         default=None)
parser.add_argument("-d", "--directory",    type=str,   dest="DIRECTORY",       help="Directory to be processed",           default=None)

args = parser.parse_args()

if args.extract and args.compress:
    print("Cannot be use tow argument [-e] and [-c]")
    exit()

if not (args.extract or args.compress):
    print("Must be choose one operation [-e] or [-c]")
    exit()

if args.FILE and args.DIRECTORY:
    print("Cannot be use tow argument [-f] and [-d]")
    exit()

if not (args.FILE or args.DIRECTORY):
    print("Must be choose one operation [-f] or [-d]")
    exit()

if args.extract:
    if args.OUTPUT is not None:
        if args.FILE is not None:
            patoolib.extract_archive(args.FILE, outdir=args.OUTPUT)
        elif args.DIRECTORY is not None:
            files = pathlib.Path(args.DIRECTORY)
            for file in files.iterdir():
                patoolib.extract_archive(file, outdir=args.OUTPUT)
        else:
            print("File or directory could not found")
    else:
        if args.FILE is not None:
            patoolib.extract_archive(args.FILE)
        elif args.DIRECTORY is not None:
            files = pathlib.Path(args.DIRECTORY)
            for file in files.iterdir():
                patoolib.extract_archive(file)
        else:
            print("File or directory could not found")

if args.compress:
    if args.OUTPUT is not None:
        if args.FILE is not None:
            directory = pathlib.Path(args.OUTPUT)
            shutil.make_archive(args.FILE, 'zip', directory)
        elif args.DIRECTORY is not None:
            directory = pathlib.Path(args.OUTPUT)
            files = pathlib.Path(args.DIRECTORY)
            for file in files.iterdir():
                shutil.make_archive(file, 'zip', directory)
        else:
            print("File or directory could not found")
    else:
        if args.FILE is not None:
            shutil.make_archive(args.FILE, 'zip')
        elif args.DIRECTORY is not None:
            files = pathlib.Path(args.DIRECTORY)
            for file in files.iterdir():
                shutil.make_archive(file, 'zip')
        else:
            print("File or directory could not found")