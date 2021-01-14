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
from googleapiclient import discovery
from pprint import pprint
from terminal_commands import shellCommand


class GoogleSpreadsheet:
    def __init__(self):
        
        """
        Structure
        {([SheetId, SheetName],[Tracados, Tomografia, Periapical, Carpal, Laudo, Conversao])}
        """

        self.clientToSpreadsheetMap = {
            'ov':(['360100036','OdontoVida'],[0,0,0,0,0,0]),
            #'rd':(['1273125380','ANEO'],[0,0,0,0,0,0]),
            'rd':(['1385808257','Copy of ANEO'],[6,120,6,6,10,15]),
            'pi':(['1450122021','PROImagem'],[0,0,0,0,0,0]),
            'smalto':(['283209946','SMALTO'],[0,0,0,0,0,0]),
            'oc':(['279638154','ORTOCOMPANY'],[0,0,0,0,0,0]),
            'fr':(['167773507','FASCIO'],[0,0,0,0,0,0]),
            'ci':(['902420804','INTEGRA'],[0,0,0,0,0,0]),
            'sdcisper':(['1446124105',''],[0,0,0,0,0,0]),
            'prox':(['890581440','PRO X'],[0,0,0,0,0,0]),
            'vs':(['537195957','VISAO'],[0,0,0,0,0,0]),
            'ra':(['453344557','Renata ArtDente'],[0,0,0,0,0,0]),
            'ex':(['360100036','Excellence_Jaragua'],[0,0,0,0,0,0]),
            'sdm':(['709165713','SorridentsSAOMIGUEL_Centro'],[0,0,0,0,0,0]),
            'svr':(['10239997','SorridentsVILARE'],[0,0,0,0,0,0]),
            'sdl':(['1270284303','Sorridents_Limao'],[0,0,0,0,0,0]),
            'ssm':(['1981683637','SorridentsSAOMATHEUS'],[0,0,0,0,0,0]),
            'sem':(['1448631721','SorridentsERMELINO_MATARAZO'],[0,0,0,0,0,0]),
            'sl':(['168276381','Sorridents_Lajeado'],[0,0,0,0,0,0]),
            'sdi':(['1890566493','Sorridents_Itaqua'],[0,0,0,0,0,0]),
            'scs':(['867401973','SorridentsChacaraStoAntonio'],[0,0,0,0,0,0]),
            'ssp':(['622687295','SorridentsSAPOPEMBA'],[0,0,0,0,0,0]),
            'sjh':(['895482455','SorridentsJARDIM_HELENA'],[0,0,0,0,0,0]),
            'crd':(['1176660590',''],[0,0,0,0,0,0]),
            'sco':(['452429227','SORRIDENTSCOCAIA'],[0,0,0,0,0,0]),
            'sgu':(['289112547','SorridentsGUARULHOS'],[0,0,0,0,0,0]),
            'smaior':(['603875069','SORRISO_MAIOR'],[0,0,0,0,0,0]),
            'sgo':(['1571258573','SorridentsGOIANIA_CENTRO'],[0,0,0,0,0,0]),
            'sdp':(['389745783','SORRIDENTS_SANTANADEPARNAIBA'],[0,0,0,0,0,0]),
            'svd':(['610182461','SORRIDENTS_VILA_DIVA'],[0,0,0,0,0,0]),
            'srv':(['229236959','SORRIDENTS_RIO_VERDE'],[0,0,0,0,0,0]),
            'exo':(['318979593','ExcellenceOESTE'],[0,0,0,0,0,0]),
            'sdme':(['2086549618','SorridentsSAOMIGUEL_Estacao'],[0,0,0,0,0,0]),
            'sgon':(['307959967','SorridentsGO_NovoHorizonte'],[0,0,0,0,0,0]),
            'slsm':(['1163021938','Sorridents_LAGOA_SAOMATHEUS'],[0,0,0,0,0,0]),
            'sbp':(['343540097','SORRIDENTS_BRAG_PAUL'],[0,0,0,0,0,0]),
            'scl':(['992104235','SORRIDENTS_CIDADE_LIVRE'],[0,0,0,0,0,0]),
            'exx':(['734273943','ExcellenceXAXIM'],[0,0,0,0,0,0]),
            'sis':(['1656686275','SORRIDENTS_ITAIM_SILVATELES'],[0,0,0,0,0,0])
         }
        self.spreadsheetID = '1n7fNL39lksm8Vua7jBW8CaTmqGi7Y-_s6ITB0JPxGOk'
        
       
        self.SCOPES = [
                'https://www.googleapis.com/auth/drive',
                'https://www.googleapis.com/auth/drive.file',
                'https://www.googleapis.com/auth/spreadsheets']

        
    def getSheetIds(self):
        for x in self.clientToSpreadsheetMap:
            print('\n' + x + ' ==> ' + str(self.clientToSpreadsheetMap[x]), end = '\n')
        #print(self.clientToSpreadsheetMap)
        for x in self.clientToSpreadsheetMap:
            print('\n' + x + ' ==> ' + str(self.clientToSpreadsheetMap[x]), end = '\n')
        
    def getSpreadsheedID(self):
        print(self.spreadsheetID)
        
    def getSheetID(self, key):
        return self.clientToSpreadsheetMap[key][0][1]
    
    def setSheetName(self, sheetName):
        self.SAMPLE_RANGE_NAME = sheetName+'!A1:F7'
        
    def getValuesList(self, key):
        return self.clientToSpreadsheetMap[key][1]
    
    def getFormula(self, key, actualRow):
        valuesList = self.getValuesList(key)
        nextRow = str(actualRow + 1)
        actualRow = str(actualRow)
        formula = ('='
        'IF(ISBLANK(C'+ nextRow + '),"",'
        'IF(EXACT("laudos",B'+ nextRow + '),((D'+ actualRow + '+(C'+ nextRow + '*'+ str(valuesList[4]) +'))-E'+ nextRow + '),'
        'IF(EXACT("tomo",B'+ nextRow + '),((D'+ actualRow + '+(C'+ nextRow + '*'+ str(valuesList[1]) +'))-E'+ nextRow + '),'
        'IF(EXACT("conversao",B'+ nextRow + '),((D'+ actualRow + '+(C'+ nextRow + '*'+ str(valuesList[5]) +'))-E'+ nextRow + '),'
        'IF(EXACT("tomo total",B'+ nextRow + '),((D'+ actualRow + '+(C'+ nextRow + '*'+ str(valuesList[1]) +'))-E'+ nextRow + '),'
        'IF(EXACT("periapicais",B'+ nextRow + '),((D'+ actualRow + '+(C'+ nextRow + '*'+ str(valuesList[2]) +'))-E'+ nextRow + '),'
        '((D'+ actualRow + '+(C'+ nextRow + '*'+ str(valuesList[0]) +'))-E'+ nextRow + ')))))))''')
        print(formula)
        return formula
    
    def getLaudos():
        commandLine = "find /Users/valen/Desktop/work -name '*.imp' | awk -F'/' '{print $NF}'"
        myList = shellCommand(commandLine, True)
        print('\n' + str(len(myList)), end='\n'*2)
        for x in myList:
            print(x)
        print('\n')
        
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
    
    
    def getRowCount(self, service, sheetName):
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=self.spreadsheetID,
                                    range=sheetName,).execute()
        values = result.get('values', [])
        count = len(values)
        print('\n--- ' + str(count) + ' ---\n')
        return count
        
    
    def writeToSpreadsheet(self, service, data, jobDesc, value, formula, received):
        commandLine = "find /Users/valen/Desktop/work -name '*.imp' | awk -F'/' '{print $NF}'"
        patientNames = shellCommand(commandLine, False)
        range_ = self.SAMPLE_RANGE_NAME
        value_input_option = 'USER_ENTERED'
        insert_data_option = 'INSERT_ROWS'
        value_range_body = {"values": [[data, jobDesc, value, formula , received, patientNames]]}
        
        request = service.spreadsheets().values().append(spreadsheetId=self.spreadsheetID, range=range_, valueInputOption=value_input_option, insertDataOption=insert_data_option, body=value_range_body)
        response = request.execute()
        
        pprint(response)
        

        
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
        spreadSheed.getRowCount(service, spreadSheed.getSheetID(clinicInitials))
        formula = spreadSheed.getFormula(clinicInitials, spreadSheed.getRowCount(service, spreadSheed.getSheetID(clinicInitials)))
        print('\n========================>>>>>>>>>>\n')
        spreadSheed.writeToSpreadsheet(service, '01/12/2021', 'laudos', 10, formula, 0)
    except NameError:
        print('\nAn Exception flew by', end='\n'*2) 
    
main()