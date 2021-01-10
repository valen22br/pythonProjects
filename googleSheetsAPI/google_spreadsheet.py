#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 16:52:12 2021

@author: valen
"""

from __future__ import print_function
import pickle
import os.path
import sys
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


class GoogleSpreadsheet:
    def __init__(self):
        self.clientToSpreadsheetMap = {
            'ov':['360100036','OdontoVida'],
            'rd':['1273125380','ANEO'],
            'pi':['1450122021','PROImagem'],
            'smalto':['283209946','SMALTO'],
            'oc':['279638154','ORTOCOMPANY'],
            'fr':['167773507','FASCIO'],
            'ci':['902420804','INTEGRA'],
            'sdcisper':['1446124105',''],
            'prox':['890581440','PRO X'],
            'vs':['537195957','VISAO'],
            'ra':['453344557','Renata ArtDente'],
            'ex':['360100036','Excellence_Jaragua'],
            'sdm':['709165713','SorridentsSAOMIGUEL_Centro'],
            'svr':['10239997','SorridentsVILARE'],
            'sdl':['1270284303','Sorridents_Limao'],
            'ssm':['1981683637','SorridentsSAOMATHEUS'],
            'sem':['1448631721','SorridentsERMELINO_MATARAZO'],
            'sl':['168276381','Sorridents_Lajeado'],
            'sdi':['1890566493','Sorridents_Itaqua'],
            'scs':['867401973','SorridentsChacaraStoAntonio'],
            'ssp':['622687295','SorridentsSAPOPEMBA'],
            'sjh':['895482455','SorridentsJARDIM_HELENA'],
            'crd':['1176660590',''],
            'sco':['452429227','SORRIDENTSCOCAIA'],
            'sgu':['289112547','SorridentsGUARULHOS'],
            'smaior':['603875069','SORRISO_MAIOR'],
            'sgo':['1571258573','SorridentsGOIANIA_CENTRO'],
            'sdp':['389745783','SORRIDENTS_SANTANADEPARNAIBA'],
            'svd':['610182461','SORRIDENTS_VILA_DIVA'],
            'srv':['229236959','SORRIDENTS_RIO_VERDE'],
            'exo':['318979593','ExcellenceOESTE'],
            'sdme':['2086549618','SorridentsSAOMIGUEL_Estacao'],
            'sgon':['307959967','SorridentsGO_NovoHorizonte'],
            'slsm':['1163021938','Sorridents_LAGOA_SAOMATHEUS'],
            'sbp':['343540097','SORRIDENTS_BRAG_PAUL'],
            'scl':['992104235','SORRIDENTS_CIDADE_LIVRE'],
            'exx':['734273943','ExcellenceXAXIM'],
            'sis':['1656686275','SORRIDENTS_ITAIM_SILVATELES']
        }
        self.spreadsheetID = '1n7fNL39lksm8Vua7jBW8CaTmqGi7Y-_s6ITB0JPxGOk'
        
        # self.SAMPLE_RANGE_NAME = 'Saldo à receber!A1:C7'
        
        self.SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
        
    def getSheetIds(self):
        print(self.clientToSpreadsheetMap)
        
    def getSpreadsheedID(self):
        print(self.spreadsheetID)
        
    def getSheetID(self, key):
        return self.clientToSpreadsheetMap[key][1]
    
    def setSheetName(self, sheetName):
        self.SAMPLE_RANGE_NAME = sheetName+'!A1:C7'
        
    def connectToSpreadsheet(self):
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
    
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
    
        service = build('sheets', 'v4', credentials=creds)
        
        return service
    
    def readSpreadsheet(self, service):
        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=self.spreadsheetID,
                                    range=self.SAMPLE_RANGE_NAME,).execute()
        values = result.get('values', [])
    
        if not values:
            print('No data found.')
        else:
            print(values)
#            print('Name, Major:')
#            for row in values:
#                # Print columns A and E, which correspond to indices 0 and 4.
#                print('%s, %s' % (row[0], row[4]))
    
    #if __name__ == '__main__':
    
    def writeToSpreadsheet(self, values):
        pass
        
def main():
    print('\nNumber of arguments:', len(sys.argv), 'arguments.', end='\n'*2)
    print('\nArgument List:', str(sys.argv), end='\n'*2)
    # clinicInitials = 'sis'
    if(len(sys.argv) > 1):
        clinicInitials = str(sys.argv[1])
    print('\nArgument List:', str(sys.argv), end='\n'*2)
    
    spreadSheed = GoogleSpreadsheet()
    spreadSheed.getSheetIds()
    spreadSheed.getSpreadsheedID()
    try:
        if(clinicInitials):
            print('\nSheetID = ' + spreadSheed.getSheetID(clinicInitials), end = '\n'*2)
            spreadSheed.setSheetName(spreadSheed.getSheetID(clinicInitials))
        else:
            print('\nSheetID = ' + spreadSheed.getSheetID('sis'), end = '\n'*2)
            spreadSheed.setSheetName(spreadSheed.getSheetID('sis'))
        service = spreadSheed.connectToSpreadsheet()
        spreadSheed.readSpreadsheet(service)
    except NameError:
        print('\nAn Exception flew by', end='\n'*2) 
    
main()