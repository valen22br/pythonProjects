#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 16:52:12 2021

@author: valen
"""

class GoogleSpreadsheet:
    def __init__(self):
        self.clientToSpreadsheetMap = {
            'ov':'360100036',
            'rd':'1273125380',
            'pi':'1450122021',
            'smalto':'283209946',
            'oc':'279638154',
            'fr':'167773507',
            'ci':'902420804',
            'sdcisper':'1446124105',
            'prox':'890581440',
            'vs':'537195957',
            'ra':'453344557',
            'ex':'360100036',
            'sdm':'709165713',
            'svr':'10239997',
            'sdl':'1270284303',
            'ssm':'1981683637',
            'sem':'1448631721',
            'vsl':'168276381',
            'sdi':'1890566493',
            'scs':'867401973',
            'ssp':'622687295',
            'sjh':'895482455',
            'crd':'1176660590',
            'sco':'452429227',
            'sgu':'289112547',
            'smaior':'603875069',
            'sgo':'1571258573',
            'sdp':'389745783',
            'svd':'610182461',
            'srv':'229236959',
            'exo':'318979593',
            'sdme':'2086549618',
            'sgon':'307959967',
            'slsm':'1163021938',
            'sbp':'343540097',
            'scl':'992104235',
            'exx':'734273943',
            'sis':'1656686275'
        }
        self.spreadsheetID = '1n7fNL39lksm8Vua7jBW8CaTmqGi7Y-_s6ITB0JPxGOk'
        
    def getSheetIds(self):
        print(self.clientToSpreadsheetMap)
        
    def getSpreadsheedID(self):
        print(self.spreadsheetID)
        
def main():
    spreadSheed = GoogleSpreadsheet()
    spreadSheed.getSheetIds()
    spreadSheed.getSpreadsheedID()
    
main()