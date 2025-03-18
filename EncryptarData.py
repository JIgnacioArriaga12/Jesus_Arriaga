# -*- coding: utf-8 -*-
"""
Encriptara DataBase 
@author: RobertoRosasGuerrero
"""


import pandas as pd 
import numpy as np
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile#, filedialog
import os
from PIL import Image, ImageTk
from cryptography.fernet import Fernet
from io import BytesIO
import re

#%%


class Encrypted_Data():
    
    def __init__(self):
        self.title = "Control Desk"    
        #Ruta del Icono
        self.icon = "Exitus3.ico"
        
        self.ima = "Neri_5.jpg"
        
        self.size ="500x290"
        self.resizable = False
        
                
        
        #width and height
        self.width_b=90
        self.height_b=40
        
        #Boton 1
        self.name_b1 = "Up Data"
        self.placey_b1=45
        self.placex_b1=10
                         

        #Boton 2
        self.name_b3 = "Descargar"
        self.placey_b3=45
        self.placex_b3=130
        


        


    def encabezado(self):
        encabezado = tk.Label(self.ventana, text="Encryptar Data")
        encabezado.config(fg = "white",bg = "darkblue",font=("Open Sans",18) )
        encabezado.pack(side= LEFT,anchor = NW,fill=X, expand=YES )
        self.encabezado=encabezado
        


    def cargar_ventana(self):
        #global imagen_,render

        ventana = tk.Tk()
        
        self.ventana = ventana
        
        #Icono de la ventana
        ventana.iconbitmap(self.icon)
        
        
        #Cambio el tamaño de la vetana
        ventana.geometry(self.size)
        #Bloquear el tamaño de la ventana
        if self.resizable:
            ventana.resizable(1,1)
        else:
            ventana.resizable(0,0)
            
            
        imagen_ = Image.open(self.ima) 
        self.imagen_ = imagen_
        
        render = ImageTk.PhotoImage(self.imagen_)
        self.render=render
        Label(self.ventana, image = self.render).place(x = 305, y = 120)
        #Nombre de la ventana
        ventana.title(self.title)
        
        
    def open_file(self):
        global df,file
        self.Texto.set("loading...")
        #try:    
        file = askopenfile(parent = self.ventana, 
                           mode = 'rb', 
                           title = 'Choose a file', 
                           filetype = [("Data Files", "*.csv *.txt")])
        self.file = file
        df = pd.read_csv(file, sep = '|', error_bad_lines=False, index_col=False, engine ='python', dtype = str,encoding='latin-1')                   
        self.Texto.set("Uploaded")


    def name_data(self,data):
        data.columns=df.columns.str.upper()
        data.columns=df.columns.str.strip()
        if((("INF_IMPL") in data.columns)|(("NOMBRE_PEN") in data.columns)):
            return 'enc_jub.txt' 
        else:
            return 'enc_trab.txt'
        
     

    """ 
    def encryptar(self):
        global df,encdf
        #key = b'op4J7iyFbQ0eap22pQx4N0ZSOWzsRa2AszcF0lad7DI='
        self.Texto_1.set("Ejec...")
        try:
            f=Fernet(b'op4J7iyFbQ0eap22pQx4N0ZSOWzsRa2AszcF0lad7DI=')
            #encrypted_file = f.encrypt(df)
            df_byte = df.to_json().encode()
            encdf = f.encrypt(df_byte)
            return self.Texto_1.set("Ejecutado")
        except:
            return self.Texto_1.set("Error")
        
      """  


    def encryptar(self,filename,encrypted_name):
        global original
        """
        Given a filename (str) and key (bytes), it encrypts the file and write it
        """
        key = b'op4J7iyFbQ0eap22pQx4N0ZSOWzsRa2AszcF0lad7DI='
        f = Fernet(key)
        with open(filename, "rb") as original_file:
            original = original_file.read()
            
        # encrypt data
        encrypted = f.encrypt(original)
        
        with open(encrypted_name,'wb') as encrypted_file:
            encrypted_file.write(encrypted)
        
        return print("Encryptado")                
      
    
    
    
        
    def export_Data(self):
        global df,ll
        self.Texto_2.set("Exportando...")
        try:
            dire = filedialog.askdirectory()
            os.chdir(dire)
            xD = self.name_data(df)
            hh=str(file)
            jz=re.findall(r"(?:'.*?')|(?:\".*?\")", hh)
            ll=jz[0]
            ll=ll.replace("'","")
            self.encryptar(ll,xD)
            return self.Texto_2.set("Exportado")
        except:
            return self.Texto_2.set("Error")    
         
            



            
         
            
                                   

                

    def botones(self):    

        Texto = tk.StringVar()
        Texto_Boton = tk.Button(self.ventana, textvariable = Texto, 
                               command = lambda:self.open_file(),
                               font = "Raleway", 
                               bg = "#A30041",
                               fg = "white")
        Texto.set(self.name_b1)
        Texto_Boton.place(x = self.placex_b1 , y = self.placey_b1,  width = self.width_b, height = self.height_b)
        self.Texto = Texto


        """
        Texto_1 = tk.StringVar()
        Texto_Boton_1 = tk.Button(self.ventana, textvariable = Texto_1, 
                               command = lambda:self.encryptar(),
                               font = "Raleway", bg = "#A30041",fg = "white")
        Texto_1.set(self.name_b2)
        Texto_Boton_1.place(x = self.placex_b2 , y = self.placey_b2,  width = self.width_b, height = self.height_b)
        self.Texto_1 = Texto_1
        """
        

        Texto_2 = tk.StringVar()
        Texto_Boton_2 = tk.Button(self.ventana, textvariable = Texto_2, 
                               command = lambda:self.export_Data(),
                               font = "Raleway", bg = "#A30041",fg = "white")
        Texto_2.set(self.name_b3)
        Texto_Boton_2.place(x = self.placex_b3 , y = self.placey_b3,  width = self.width_b, height = self.height_b)
        self.Texto_2 = Texto_2




        
    def mostrar(self):
        self.ventana.mainloop()        
        
        
        
        
encrypted_data = Encrypted_Data()
encrypted_data.cargar_ventana() 
encrypted_data.encabezado() 
encrypted_data.botones() 
encrypted_data.mostrar() 


df[df["NOMBRE_PEN"].str.contains("ñ",na=False)].head()
















