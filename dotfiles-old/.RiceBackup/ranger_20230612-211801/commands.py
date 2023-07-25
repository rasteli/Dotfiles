# This is a sample commands.py.  You can add your own commands here.
#
# Please refer to commands_full.py for all the default commands and a complete
# documentation.  Do NOT add them all here, or you may end up with defunct
# commands when upgrading ranger.

# A simple command for demonstration purposes follows.
# -----------------------------------------------------------------------------

from __future__ import (absolute_import, division, print_function)

# You can import any python module as needed.
import os

# You always need to import ranger.api.commands here to get the Command class:
from ranger.api.commands import *

# Any class that is a subclass of "Command" will be integrated into ranger as a
# command.  Try typing ":my_edit<ENTER>" in ranger!
class newfile(Command):
    def execute(self):
        if not self.arg(1):
            self.fm.notify('Wrong number of arguments', bad=True)
            return
        self.fm.run(['touch', self.arg(1)])

class newdir(Command):
    def execute(self):
        if not self.arg(1):
            self.fm.notify('Wrong number of arguments', bad=True)
            return
        self.fm.run(['mkdir', self.arg(1)])

