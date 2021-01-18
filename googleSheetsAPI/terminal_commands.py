#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 20:48:20 2021

@author: valen
"""

import subprocess

def shellCommand(command, listOutput = False):
    out = subprocess.Popen([command], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    output = out.communicate()
    output = output[0].decode('utf-8')
    output = output.replace('\n', '|')
    output = output[0:len(output)-1]
    if(listOutput):
        return output.split('|')
    else:
        return output

def ShellBashScriptExecution(command):
    out = subprocess.call(command)
    return out

commandLine = "find /Users/valen/Desktop/work -name '*.rcf' | awk -F'/' '{print $NF}'"
myList = shellCommand(commandLine, True)
print('\n' + str(len(myList)), end='\n'*2)
for x in myList:
    print(x)
print('\n')

