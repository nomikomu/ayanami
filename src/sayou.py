#-*- coding: utf-8 -*-
#!/usr/bin/python
import base64
import os, os.path
import sys
import cmd
import time

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

animu = open("anime.txt","rw+")

if os.path.exists("myfile.dat"):
  f = file("myfile.dat", "r+")
else:
  f = file("myfile.dat", "w")
  
class cmd_input(cmd.Cmd):
  # local time - get h:min:sec
  localtime_h = time.localtime()[3]
  localtime_m = time.localtime()[4]
  localtime_s = time.localtime()[5]  
  prompt = str(localtime_h)+':'+str(localtime_m)+':'+str(localtime_s)+' λ.春: '
  ruler = "-"
  def do_sysinfo(self,line):
    print '[ ' + os.name + ' ' + sys.platform + ' ]'
    print os.uname()
  def do_count_files(self,line):
    print len([name for name in os.listdir('.') if os.path.isfile(name)])
  def do_quit(self,line):
    sys.exit("sayonara")
  def new_entr(self,line):
    anime = "20 " + raw_input()
    animu.seek(0,2)
    line = fo.write( anime )
    
    animu.seek(0,0)
    for index in range(20):
      anime = animu.next()
      print "No %d | %s" % (index,line)

if __name__ == '__main__':
  cmd_input().cmdloop()
  #work on: how to update time
  fo.close()
