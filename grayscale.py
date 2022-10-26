#python grayscale.py --input color --output blackwhite

from glob import glob
from argparse import ArgumentParser

parser = ArgumentParser(description='Zamiana kolorwych jpgów na czarnobiałe.')
parser.add_argument('--input', help='Folder, z którego pobieram obrazy', required=True)
parser.add_argument('--output', help='Folder, do którego zapiszę obrazy', required=True)
args = parser.parse_args()

for path in glob(args.input + '/*'):
    directory, filename = path.split('\\')
    print(path, directory, filename)