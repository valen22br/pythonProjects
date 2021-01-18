#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 13:36:05 2021

@author: valen
"""

import PyPDF2
import time
from terminal_commands import shellCommand
from terminal_commands import ShellBashScriptExecution
import os

class PDFSignature:
    
    def __init__(self):
        self.pdfPath = '/Users/valen/Desktop/work/laudos/'
        self.watermark_file_name =  "Blank_Signature.pdf"
        self.watermark_file = self.pdfPath + self.watermark_file_name
        
    def signPDF(self, fileName):
        
        input_file = self.pdfPath + fileName
        output_file = self.pdfPath + "_" + fileName 
#        watermark_file = pdfPath + "Blank_Signature.pdf"

        with open(input_file, "rb") as filehandle_input:
            # read content of the original file
            pdf = PyPDF2.PdfFileReader(filehandle_input)
            
            with open(self.watermark_file, "rb") as filehandle_watermark:
                # read content of the watermark
                watermark = PyPDF2.PdfFileReader(filehandle_watermark)
                
                # get first page of the original PDF
                first_page = pdf.getPage(0)
                
                # get first page of the watermark PDF
                first_page_watermark = watermark.getPage(0)
                
                # merge the two pages
                first_page.mergePage(first_page_watermark)
                
                # create a pdf writer object for the output file
                pdf_writer = PyPDF2.PdfFileWriter()
                
                # add page
                pdf_writer.addPage(first_page)
                
                with open(output_file, "wb") as filehandle_output:
                    # write the watermarked file to the new file
                    pdf_writer.write(filehandle_output)
                    
    def prepareFilesToBeSigned(self):
        os.chdir("/Users/valen/Desktop/work")
        commandLine = "./traca.sh"
        ShellBashScriptExecution(commandLine)
    
    def getPDFFilesToSign(self):
        commandLine = "find /Users/valen/Desktop/work/laudos/ -name '*.pdf' | awk -F'/' '{print $NF}'"
        pdfFileList = shellCommand(commandLine, True)
        pdfFileList.remove(self.watermark_file_name)
        
        return pdfFileList
    
    def cleanUpAfterPDFManipulation(self, pdfFileList):
        pdfFileListScaped = [i.replace(' ', '\ ') for i in pdfFileList]
        commandLine = "mv /Users/valen/Desktop/work/laudos/_* /Users/valen/Desktop/work/"
        shellCommand(commandLine, True)
        for fileName in pdfFileListScaped:
            commandLineMV = "rm -rf /Users/valen/Desktop/work/laudos/"+fileName
            shellCommand(commandLineMV, True)
            
    def zipFiles(self):
        commandLine = "zip Archive.zip *.pdf *.rcf *.imp"
        shellCommand(commandLine, True)
        

def main():
    
    PDFSignatureObject = PDFSignature();
    PDFSignatureObject.prepareFilesToBeSigned()

    pdfFileList = PDFSignatureObject.getPDFFilesToSign()
    
    for fileName in pdfFileList:
        print(fileName)
        PDFSignatureObject.signPDF(fileName)
        
    PDFSignatureObject.cleanUpAfterPDFManipulation(pdfFileList)
    PDFSignatureObject.zipFiles()
    
main()