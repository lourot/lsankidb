# -*- coding: utf-8 -*-
# pylint: disable=no-self-use,invalid-name,protected-access

import sqlite3

from unittest import mock, TestCase

from src import lsankidb

class LsankidbTests(TestCase):
    @mock.patch('src.lsankidb.print')
    @mock.patch('src.lsankidb.Db')
    @mock.patch('src.lsankidb._find_db_path')
    @mock.patch('src.lsankidb._parse_args')
    def test_main_finds_db_and_prints_it(self, mock_parse_args, mock_find_db_path, mock_db,
                                         mock_print):
        mock_parse_args.return_value.PATH = None
        mock_find_db_path.return_value = '/path/to/db.anki2'
        mock_db.side_effect = ['hello']

        lsankidb.main()

        mock_db.assert_called_once_with(mock_find_db_path.return_value)
        mock_print.assert_has_calls([mock.call('hello')])

    @mock.patch('src.lsankidb.print')
    @mock.patch('src.lsankidb.Db')
    @mock.patch('src.lsankidb._parse_args')
    def test_main_prints_passed_db(self, mock_parse_args, mock_db, mock_print):
        mock_parse_args.return_value.PATH = '/path/to/db.anki2'
        mock_db.side_effect = ['hello']

        lsankidb.main()

        mock_db.assert_called_once_with(mock_parse_args.return_value.PATH)
        mock_print.assert_has_calls([mock.call('hello')])

    @mock.patch('src.lsankidb._find_db_path')
    @mock.patch('src.lsankidb._parse_args')
    def test_main_fails_if_no_db_found(self, mock_parse_args, mock_find_db_path):
        mock_parse_args.return_value.PATH = None
        mock_find_db_path.return_value = None

        with self.assertRaises(SystemExit):
            lsankidb.main()

    @mock.patch('src.lsankidb.Db')
    @mock.patch('src.lsankidb._parse_args')
    def test_main_fails_with_corrupted_db(self, mock_parse_args, mock_db):
        mock_parse_args.return_value.PATH = '/path/to/db.anki2'
        mock_db.side_effect = sqlite3.OperationalError('error')

        with self.assertRaises(sqlite3.OperationalError):
            lsankidb.main()

    @mock.patch('src.lsankidb.os.walk')
    def test_find_db_path_happy_case(self, mock_walk):
        mock_walk.return_value = [('/root', [], ['unsupported.ext', 'db.anki2'])]

        self.assertEqual('/root/db.anki2', lsankidb._find_db_path('/search/here'))

    @mock.patch('src.lsankidb.os.walk')
    def test_find_db_path_sad_case(self, mock_walk):
        mock_walk.return_value = [('/root', [], ['unsupported.ext', 'unsupported2.ext'])]

        self.assertIsNone(lsankidb._find_db_path('/search/here'))

class DbTests(TestCase):
    @mock.patch('AnkiTools.tools.read.readAnki2')
    def test_init_reads_decks_and_cards(self, mock_read):
        mock_read.return_value.__enter__.return_value.decks = {
            '1': {
                'did': '1',
                'name': 'german',
            },
            '2': {
                'did': '2',
                'name': 'french',
            },
        }
        mock_read.return_value.__enter__.return_value.cards = {
            '10': {
                'did': '1',
                'note': {
                    'content': 'a',
                },
            },
            '11': {
                'did': '1',
                'note': {
                    'content': 'b',
                },
            },
            '20': {
                'did': '2',
                'note': {
                    'content': 'c',
                },
            },
        }

        self.assertEqual("""\
french
    c
german
    a
    b""", str(lsankidb.Db('/path/to/db.anki2')))

    def test_init_fails_if_unsupported_extension(self):
        with self.assertRaises(KeyError):
            lsankidb.Db('/path/to/unsupported.ext')

    @mock.patch('AnkiTools.tools.read.readApkg')
    def test_init_supports_apkg_extension(self, mock_read):
        db_path = '/path/to/db.apkg'

        lsankidb.Db(db_path)

        mock_read.assert_called_once_with(db_path)

    @mock.patch('AnkiTools.tools.read.readAnki2')
    def test_init_removes_duplicate_cards(self, mock_read):
        mock_read.return_value.__enter__.return_value.decks = {
            '1': {
                'did': '1',
                'name': 'german',
            },
        }
        mock_read.return_value.__enter__.return_value.cards = {
            '10': {
                'did': '1',
                'note': {
                    'content': 'a',
                },
            },
            '11': {
                'did': '1',
                'note': {
                    'content': 'a',
                },
            },
        }

        self.assertEqual("""\
german
    a""", str(lsankidb.Db('/path/to/db.anki2')))
