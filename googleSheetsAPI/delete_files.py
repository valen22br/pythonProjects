#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 08:41:53 2021

@author: valen
"""

from terminal_commands import shellCommand

# delete all .pdf, .imp and .rcf files
commandLine = "rm -rf /Users/valen/Desktop/work/*21.zip"
shellCommand(commandLine, True)

commandLine = "rm -rf /Users/valen/Desktop/work/*.pdf"
shellCommand(commandLine, True)

commandLine = "rm -rf /Users/valen/Desktop/work/*.imp"
shellCommand(commandLine, True)

commandLine = "rm -rf /Users/valen/Desktop/work/*.rcf"
shellCommand(commandLine, True)