import math

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

help_fun_list = [] # list of functions with help
class HelpEntry:
  def __init__(self,key_config,func_name):
  	global key_config
  	self.key_config = key_config
  	self.func_name = func_name
  def print_help(self,key_config):
    global key_config, help
    print str(key_config) + ' - ' + func_name + ' - ' + help
  def help(self,help=''):
  	global key_config, help
  	self.help = help
  	help_fun_list.append(key_config)

#   manual - type=man all functions of Evangelion Register   # 
#                                                            #
#            list of help info for functions                 #

# p - generate list of index

p_help = HelpEntry('p','generate index')
p_help.help = 'generating index numbers 1-99999 for one type'