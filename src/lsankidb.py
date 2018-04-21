#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import sqlite3
import sys

import AnkiTools.tools.read

from . import __version__

class Card:
    def __init__(self, content):
        self.content = str(content)

    def __lt__(self, other):
        return self.content < other.content

    def __eq__(self, other):
        return self.content == other.content

    def __hash__(self):
        return hash(self.content)

    def __str__(self):
        return self.content

class Deck:
    def __init__(self, name):
        self.name = name
        self.__cards = set()

    def __lt__(self, other):
        return self.name < other.name

    def __str__(self):
        return self.name + ''.join('\n    ' + str(card) for card in sorted(self.__cards))

    def add(self, card):
        self.__cards.add(card)

class Db:
    @staticmethod
    def extensions():
        return {
            'anki2': AnkiTools.tools.read.readAnki2,
            'apkg': AnkiTools.tools.read.readApkg,
        }

    def __init__(self, path):
        self.__decks = dict()

        extension = path.split('.')[-1]
        try:
            open_function = self.extensions()[extension]
        except KeyError:
            raise KeyError('".{}" extension not supported. Supported extensions: {}'.format(
                extension, ', '.join('.' + ext for ext, _ in self.extensions().items())))

        with open_function(path) as anki:
            for deck in anki.decks.values():
                self.__decks[deck['did']] = Deck(deck['name'])
            for card in anki.cards.values():
                self.__decks[card['did']].add(Card(card['note']['content']))

    def __str__(self):
        return '\n'.join(str(deck) for deck in sorted(self.__decks.values()))

def _parse_args():
    parser = argparse.ArgumentParser(description='"ls" for your local Anki database.')
    parser.add_argument('--version', action='version',
                        version='%(prog)s version ' + __version__)
    parser.add_argument(
        'PATH', nargs='?',
        help='path to your DB file (e.g. "~/.local/share/Anki2/User/collection.anki2")')
    return parser.parse_args(sys.argv[1:])

def _find_db_path(search_folder):
    for root, _, files in os.walk(search_folder):
        for name in files:
            for supported_extension, _ in Db.extensions().items():
                if name.endswith('.' + supported_extension):
                    return os.path.join(root, name)
    return None

def main():
    args = _parse_args()

    search_folder = os.path.join(os.path.expanduser('~'), '.local/share/Anki2')
    path = args.PATH if args.PATH else _find_db_path(search_folder)
    if not path:
        print("""\
Error: no Anki database found in "{}". Try
    {} /path/to/my/collection.anki2\
""".format(search_folder, sys.argv[0]))
        sys.exit(1)

    print('Listing {} ...\n'.format(path))
    try:
        print(Db(path))
    except sqlite3.OperationalError:
        raise sqlite3.OperationalError('{} seems to be corrupted.'.format(path))

if __name__ == '__main__':
    main()
