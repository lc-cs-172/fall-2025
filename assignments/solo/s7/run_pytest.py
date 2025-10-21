''' Purpose: invoke pytest from the terminal/shell/command-line via "python3 run_pytest.py -s"
    Motivation: the pytest command is not always installed in a bin directory on the user's PATH
    Prerequisite: install the pytest module, e.g., "python3 -m pip install [--user] pytest"
'''

import sys
from pytest import console_main

if 1: print(f'''
================================================
DEBUG: sys.argv={sys.argv}
================================================
''', file=sys.stderr)

sys.exit(console_main())
##NOTREACHED##
