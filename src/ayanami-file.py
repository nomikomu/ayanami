import base64
import os
import sys
import cmd

class cmd_input(cmd.Cmd):
  def print_info(self,line):
    print os.name 
    print sys.platform
    print os.uname()
  def quit(self,line):
    sys.exit("sayonara")

if __name__ == '__main__':
  cmd_input().cmdloop()
