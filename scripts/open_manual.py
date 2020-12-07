import os
from scripts.path import the_local_path

def open_the_manual() ->bool:
    if not os.path.isfile(the_local_path() + '\\manual.pdf'):
        return False

    print(the_local_path())
    print(the_local_path() + '\\manual.pdf')
    os.startfile(the_local_path() + '\\manual.pdf')

    return True