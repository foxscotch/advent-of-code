import os
import re
from pathlib import Path
from shutil import copyfile


BOILERPLATE_DIRECTORY = Path('./bp/')
DAY_PATTERN = re.compile('(\d{4}).(\d{2}).?(\d)?')


class BoilerplateException(Exception):
    pass


def create_day_directory(year, day):
    directory = Path() / year / day
    if not directory.exists():
        os.makedirs(directory)
    return directory

def create_source_file(folder, lang, part='1', force=False):
    if part != '1':
        boilerplate = folder / f'p{int(part) - 1}.{lang}'
    else:
        boilerplate = BOILERPLATE_DIRECTORY / f'bp.{lang}'

    destination = folder / f'p{part}.{lang}'

    if destination.exists() and not force:
        raise BoilerplateException(
            'Can not copy to a file that already exists: {}'
              .format(destination))
    elif not boilerplate.exists():
        raise BoilerplateException(
            'No .{} boilerplate file exists'.format(lang))

    copyfile(boilerplate, destination)

def create_empty_files(folder, input=False):
    if input:
        (folder / 'input.txt').touch()
    (folder / 'challenge.txt').touch()

def main(args):
    year, day, part = DAY_PATTERN.match(args.day).groups()
    dest_folder = create_day_directory(year, day)
    create_source_file(dest_folder, args.lang, part or '1', args.force)
    create_empty_files(dest_folder, args.input)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Create a new empty day.')
    parser.add_argument('day', help='Day to make a new directory for; e.g. "2020.06"')
    parser.add_argument('lang', help='Corresponds to a file extension in ./bp/')
    parser.add_argument('-i', '--input', action='store_true', help='Add empty input file too')
    parser.add_argument('-f', '--force', action='store_true', help='Force copying of boilerplate file')
    args = parser.parse_args()

    try:
        main(args)
    except BoilerplateException as e:
        print('Error:', e)
