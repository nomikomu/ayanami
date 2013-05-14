import base64
import os, os.path
import sys
import cmd

# This program is free software; you can redistribute it and #
# /or modify it under the terms of the GNU General  Public - #
# License as published by the Free Software Foundation; eit- #
# her version 2 of the License, or (at your option) any lat- #
# er version.                          Copyright 2013 defm03 #
#                                                            #
#              /     \                                       #
#              vvvvvvv  /|__/|                               #
#                 I   /O,O   |                               #
#                 I /_____   |      /|/|                     #
#                J|/^ ^ ^ \  |    /00  |    _//|             #
#                 |^ ^ ^ ^ |W|   |/^^\ |   /oo |             #
#                  \m___m__|_|    \m_m_|   \mm_|             #
#                                                            #
#   NERV HQ - defm03 // github@defm03 // yutsuro@gmail.com   #

class cmd_input(cmd.Cmd):
  def do_print_info(self,line):
    print os.name 
    print sys.platform
    print os.uname()
  def do_count_files(self,line):
    print len([name for name in os.listdir('.') if os.path.isfile(name)])
  def do_quit(self,line):
    sys.exit("sayonara")

if __name__ == '__main__':
  cmd_input().cmdloop()
