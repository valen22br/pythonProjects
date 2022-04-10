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
import time
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient import discovery
from pprint import pprint
from terminal_commands import shellCommand
from pdf_module_by_valen import PDFSignature


class GoogleSpreadsheet:
    def __init__(self):
        
        """
        Structure
        {([SheetId, SheetName],[Tracados, Tomografia, Periapical, Carpal, Laudo, Conversao])}
        """

        self.clientToSpreadsheetMap = {
            'ov':(['360100036','OdontoVida'],[8,120,8,8,12,15]),
            'rd':(['1273125380','ANEO'],[8,120,8,8,12,15]),
#            'rd':(['1385808257','Copy of ANEO'],[6,120,6,6,10,15]),
            'pi':(['1450122021','PROImagem'],[8,120,8,8,12,15]),
#            'smalto':(['283209946','SMALTO'],[0,0,0,0,0,0]),
            'oc':(['279638154','ORTOCOMPANY'],[8,120,8,8,12,15]),
            'fr':(['167773507','FASCIO'],[8,120,8,8,12,15]),
            'ci':(['902420804','INTEGRA'],[8,120,8,8,12,15]),
            'sdcisper':(['1446124105','SORRIDENTS_CISPER'],[8,120,8,8,12,15]),
            'prox':(['890581440','PRO X'],[8,120,8,8,12,15]),
            'vs':(['537195957','VISAO'],[8,120,8,8,12,15]),
            'ra':(['453344557','Renata ArtDente'],[8,120,8,8,12,15]),
            'ex':(['360100036','Excellence_Jaragua'],[8,120,8,8,12,15]),
            'sdm':(['709165713','SorridentsSAOMIGUEL_Centro'],[8,120,8,8,12,15]),
            'svr':(['10239997','SorridentsVILARE'],[8,120,8,8,12,15]),
            'sdl':(['1270284303','Sorridents_Limao'],[8,120,8,8,12,15]),
            'ssm':(['1981683637','SorridentsSAOMATHEUS'],[8,120,8,8,12,15]),
            'sem':(['1448631721','SorridentsERMELINO_MATARAZO'],[8,120,8,8,12,15]),
            'sl':(['168276381','Sorridents_Lajeado'],[8,120,8,8,12,15]),
            'sdi':(['1890566493','Sorridents_Itaqua'],[8,120,8,8,12,15]),
            'scs':(['867401973','SorridentsChacaraStoAntonio'],[8,120,8,8,12,15]),
            'ssp':(['622687295','SorridentsSAPOPEMBA'],[8,120,8,8,12,15]),
            'sjh':(['895482455','SorridentsJARDIM_HELENA'],[8,120,8,8,12,15]),
            'crd':(['1176660590','CRD'],[8,120,8,8,12,15]),
            'sco':(['452429227','SORRIDENTSCOCAIA'],[8,120,8,8,12,15]),
            'sgv':(['1603591808','SorridentsGARAVELO'],[8,120,8,8,12,15]),
            'sgu':(['289112547','SorridentsGUARULHOS'],[8,120,8,8,12,15]),
            'smaior':(['603875069','SORRISO_MAIOR'],[8,120,8,8,12,15]),
            'sgo':(['1571258573','SorridentsGOIANIA_CENTRO'],[8,120,8,8,12,15]),
            'sdp':(['389745783','SORRIDENTS_SANTANADEPARNAIBA'],[8,120,8,8,12,15]),
            'svd':(['610182461','SORRIDENTS_VILA_DIVA'],[8,120,8,8,12,15]),
            'srv':(['229236959','SORRIDENTS_RIO_VERDE'],[8,120,8,8,12,15]),
            'exo':(['318979593','ExcellenceOESTE'],[8,120,8,8,12,15]),
            'sdme':(['2086549618','SorridentsSAOMIGUEL_Estacao'],[8,120,8,8,12,15]),
            'sgon':(['307959967','SorridentsGO_NovoHorizonte'],[8,120,8,8,12,15]),
            'slsm':(['1163021938','Sorridents_LARGO_SAOMATHEUS'],[8,120,8,8,12,15]),
            'sbp':(['343540097','SORRIDENTS_BRAG_PAUL'],[8,120,8,8,12,15]),
            'scl':(['992104235','SORRIDENTS_CIDADE_LIVRE'],[8,120,8,8,12,15]),
            'exx':(['734273943','ExcellenceXAXIM'],[8,120,8,8,12,15]),
            'sis':(['1656686275','SORRIDENTS_ITAIM_SILVATELES'],[8,120,8,8,12,15]),
            'sist':(['148500071','SORRIDENTS_ITAIM_TIBURCIO'],[8,120,8,8,12,15]),
            'ssc':(['786524798','SORRIDENTS_CURUCA'],[8,120,8,8,12,15]),
            'ssr':(['1333441969','SorridentsSTARITA'],[8,120,8,8,12,15]),
            'sgva':(['921845397','SORRIDENTS_GETULIO_VARGAS'],[8,120,8,8,12,15]),
            'stp':(['1619069009','SORRIDENTS_TATUAPE'],[8,120,8,8,12,15]),
            'sse':(['2004635372','SORRIDENTS_SUMARE'],[8,120,8,8,12,15]),
            'sivv':(['342275993','SORRIDENTS_ITAVUVU'],[8,120,8,8,12,15]),
            'sjo':(['1540311325','SORRIDENTS_JARDIM_ODETE'],[8,120,8,8,12,15]),
            'spt':(['694491676','SORRIDENTS_PIRATININGA'],[8,120,8,8,12,15]),
            'ocsa':(['1125238977','ODONTOCOMPANY_CHACARA_SANTO_ANTONIO'],[8,120,8,8,12,15]),
            'test':(['1413480013','test'],[8,120,8,8,12,15]),
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
#        print(formula)
        return formula
    
    def getLaudos(self, fileExtension):
        commandLine = "find /Users/valen/Desktop/work -name '*." + fileExtension + "' | awk -F'/' '{print $NF}'"
        outputList = shellCommand(commandLine, True)
        return outputList
    
    def executeShellScript(self, commandLine):
        outputList = shellCommand(commandLine, True)
        return outputList
        
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
        
    
    def writeToSpreadsheet(self, service, data, jobDesc, value, formula, received, fileExtension):
#        commandLine = "find /Users/valen/Desktop/work -name '*.imp' | awk -F'/' '{print $NF}'"
#        patientNames = shellCommand(commandLine, False)
        laudos = self.getLaudos(fileExtension)

        patientNames = ' -- '.join(map(str, laudos))
        
        range_ = self.SAMPLE_RANGE_NAME
        value_input_option = 'USER_ENTERED'
        insert_data_option = 'INSERT_ROWS'
        value_range_body = {"values": [[data, jobDesc, value, formula , received, patientNames]]}
        
        request = service.spreadsheets().values().append(spreadsheetId=self.spreadsheetID, range=range_, valueInputOption=value_input_option, insertDataOption=insert_data_option, body=value_range_body)
        response = request.execute()
        
        pprint(response)
        return response
        

        
def main():
    print('\nNumber of arguments:', len(sys.argv), 'arguments.', end='\n'*2)
    print('\nArgument List:', str(sys.argv), end='\n'*2)
    # clinicInitials = 'test'
    if(len(sys.argv) > 1):
        clinicInitials = str(sys.argv[1])
        date = str(sys.argv[2])
    print('\nArgument List:', str(sys.argv), end='\n'*2)
    
    spreadSheet = GoogleSpreadsheet()
    try:

        #Sign PDF Files
        PDFSignatureObject = PDFSignature();
        PDFSignatureObject.prepareFilesToBeSigned()

        pdfFileList = PDFSignatureObject.getPDFFilesToSign()

        for fileName in pdfFileList:
            print(fileName)
            PDFSignatureObject.signPDF(fileName)

        PDFSignatureObject.cleanUpAfterPDFManipulation(pdfFileList)
        PDFSignatureObject.zipFiles()

        if(clinicInitials):
            print('\nSheetID = ' + spreadSheet.getSheetID(clinicInitials), end = '\n'*2)
            spreadSheet.setSheetName(spreadSheet.getSheetID(clinicInitials))
        else:
            print('\nSheetID = ' + spreadSheet.getSheetID('sis'), end = '\n'*2)
            spreadSheet.setSheetName(spreadSheet.getSheetID('sis'))
        service = spreadSheet.connectToSpreadsheet()
        
        laudos = spreadSheet.getLaudos('imp')
        tracados = spreadSheet.getLaudos('rcf')
        response = ''
        
        if '' not in laudos:
            formula = spreadSheet.getFormula(clinicInitials, spreadSheet.getRowCount(service, spreadSheet.getSheetID(clinicInitials)))
            response = spreadSheet.writeToSpreadsheet(service, date, 'laudos', len(laudos), formula, 0, 'imp')
            
        if '' not in tracados:
            formula = spreadSheet.getFormula(clinicInitials, spreadSheet.getRowCount(service, spreadSheet.getSheetID(clinicInitials)))
            response = spreadSheet.writeToSpreadsheet(service, date, 'tracados', len(tracados), formula, 0, 'rcf')
        
#        time.sleep(5)

#        if(response != ''):
#            # delete all .pdf, .imp and .rcf files
#            commandLine = "rm -rf /Users/valen/Desktop/work/*21.zip"
#            spreadSheet.executeShellScript(commandLine)

#            commandLine = "rm -rf /Users/valen/Desktop/work/*.pdf"
#            spreadSheet.executeShellScript(commandLine)

#            commandLine = "rm -rf /Users/valen/Desktop/work/*.imp"
#            spreadSheet.executeShellScript(commandLine)

#            commandLine = "rm -rf /Users/valen/Desktop/work/*.rcf"
#            spreadSheet.executeShellScript(commandLine)

    except NameError:
        print('\nAn Exception flew by', end='\n'*2) 
    
main()
