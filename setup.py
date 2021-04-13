from distutils.core import setup

setup(name='quicknote',
      version='0.1a',
      py_modules=['quicknote'],
      entry_points = {
          'console_scripts': ['quicknote=quicknote.command_line:main'],
          }
      )
