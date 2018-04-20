from setuptools import setup
import lsankidb

setup(name='lsankidb',
      version=lsankidb.__version__,
      install_requires=['AnkiTools'],
      description='"ls" for your local Anki database.',

      #FIXME this duplicates README.md
      long_description="""
lsankidb
========

``ls`` for your local `Anki <https://apps.ankiweb.net/>`__ database.

Dump all your Anki terms in order to save them, search them, ``grep`` them or ``diff`` them.

::

    $ lsankidb
    Listing /home/me/.local/share/Anki2/User 1/collection.anki2 ...
    
    German
        ['Hello', 'Hallo']
        ['How are you?', "Wie geht's?"]
    French
        ['Hello', 'Bonjour']
        ['How are you?', 'Comment ça va ?']

`See on GitHub. <https://github.com/AurelienLourot/lsankidb>`__
""",
      keywords=['anki',
                'terminal',
                'cli',
                'dump',
                'ls',],
      author='Aurelien Lourot',
      author_email='aurelien.lourot@gmail.com',
      url='https://github.com/AurelienLourot/lsankidb',
      download_url='https://github.com/AurelienLourot/lsankidb/tarball/'
                   + lsankidb.__version__,
      license='public domain',
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Console',
                   'Intended Audience :: Developers',
                   'License :: Public Domain',
                   'Natural Language :: English',
                   'Operating System :: POSIX :: Linux',
                   'Programming Language :: Python :: 3.5',
                   'Topic :: Education',
                   'Topic :: Utilities'],
      packages=['lsankidb'],
      entry_points="""
[console_scripts]
lsankidb = lsankidb.lsankidb:main
""")
