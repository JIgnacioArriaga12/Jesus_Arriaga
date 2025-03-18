# -*- coding: utf-8 -*-
"""
Created on Fri May 20 18:39:02 2022

Pagos directos, anulaciones y reembolsos
@author: RobertoRosasGuerrero
"""


#%%Importamos paqueterías 
import pandas as pd
import numpy as np
import os
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as MB
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfilename 



#%% Creamos la clase y la ventana


class rodamientos():
    
    def __init__(self):
        
        self.title = "Rembolsos, Anulaciones y Pagos D"
        
        self.icon = "Exitus3.ico"
        self.ima = "Neri.jpg"
        
        self.size = "600x360"
        self.resizable = False
        

        
        

    def cargar_ventana(self):     
        
        ventana = tk.Tk()
        self.ventana = ventana
        
        ventana.iconbitmap(self.icon)
        
        ventana.geometry(self.size)
        
        if self.resizable:
            ventana.resizable(1,1)
        else:
            ventana.resizable(0,0) 
            
    
        # Create Notebook
        notebook = ttk.Notebook(self.ventana)
        notebook.pack(pady = 10, expand = True)
        
        
        #Create Frames
        frame1 = ttk.Frame(notebook, width = 600, height = 320)
        frame1.pack(fill = 'both', expand = True)
        #Add frame to notebook
        notebook.add(frame1, text = 'Rem, Anul y PagD')        
        self.frame1 = frame1
        

        
        
        imagen_ = Image.open(self.ima)
        self.imagen_ = imagen_
        
        render = ImageTk.PhotoImage(self.imagen_)
        self.render=render
        
        tk.Label(self.frame1, image = self.render).place(x = 355, y = 90)
        #Nombre de la ventana
        ventana.title(self.title)        
        
        
    def RenomColumns(self,df):
        try:
            df.rename(columns={'iCredId':"Credito"},inplace=True)
        except:
            pass

        try:
            df.rename(columns={'ï»¿Credito':"Credito"},inplace=True)
        except:
            pass        
        
        
        if("Dias" in (df.columns)):
            df.rename(columns={"Dias":"iDays","Pagare":"nTAmount","Sdo Cap":"nPendingK","Saldo Total":"nTotBalance","Monto":"nAmount","Prim Venc":"vFirstDate"},inplace=True)            
            return df
        else:
            return df        
        
        
#%% Funciones Para Botones         
        
    def botones(self):
        
        #Botones del FRAME 1
              
        # Boton 1 
        Texto = tk.StringVar()
        Texto_Boton = tk.Button(self.frame1, textvariable = Texto, 
                               command = lambda:self.open_file(),
                               font = "Raleway", 
                               bg = "red",
                               fg = "white")
        Texto.set("Up Ap. Pag")
        Texto_Boton.place(x = 10 , y = 15,  width = 100, height = 40)
        self.Texto = Texto                

        # Boton 2 
        Texto_1 = tk.StringVar()
        Texto_Boton_1 = tk.Button(self.frame1, textvariable = Texto_1, 
                               command = lambda:self.open_file1(),
                               font = "Raleway", 
                               bg = "orange",
                               fg = "white")
        Texto_1.set("Up LC")
        Texto_Boton_1.place(x = 130 , y = 15,  width = 100, height = 40)
        self.Texto_1 = Texto_1 

        #Boton 3
        ejecutar_textf2=tk.StringVar()
        ejecutar_Botonf2= tk.Button(self.frame1, textvariable = ejecutar_textf2,
                              command = lambda: self.Process_1(Base_1, LC),
                              font="Raleway",
                              bg = "#A30041",
                              fg = "white")
        ejecutar_textf2.set("Ejecutar")
        ejecutar_Botonf2.place(x = 250 , y = 15,  width = 100, height = 40)
        self.ejecutar_textf2 = ejecutar_textf2
        
        

        
        
        #Boton 4
        Save_textf2=tk.StringVar()
        Save_Botonf2= tk.Button(self.frame1, textvariable = Save_textf2,
                              command = lambda: self.save(),
                              font="Raleway",
                              bg = "green",
                              fg = "white")
        Save_textf2.set("Exportar")
        Save_Botonf2.place(x = 370 , y = 15,  width = 100, height = 40)
        self.Save_textf2 = Save_textf2


               

        
#%% Funciones para cargar y guardar los  archivos        
        
    def open_file(self):
        global Base_1
        errorT = tk.StringVar()
        error = tk.Button(self.frame1, textvariable = errorT, font = "Raleway", bg = "red",fg = "white")
        errorT.set("Data con columnas mal")
        
        self.error = error
        self.errorT = errorT

        #self.error = error
        
        #try:
        self.Texto.set("loading...")
        try:
            file = askopenfile(parent = self.ventana, 
                               mode = 'rb', 
                               title = 'Choose a file', 
                               filetype = [("Data Files", "*.csv *.txt *.xlsx")])
            try:                            
                Base_1 = pd.read_csv(file, low_memory = False,encoding='latin-1')
            except:
                Base_1 = pd.read_excel(file)
            
            self.Texto.set("Cargado")
        except:
            errorT.set("Archivo Mal, cargalo en CSV")
            self.error.place(x = 10 , y = 80,  width = 300, height = 50)
         
        Base_1 = self.RenomColumns(Base_1)    
        try:                
           Base_1=Base_1[["Credito", "Afiliado", "vDescription", "vDateMovement", "vDepositDate", "vIdPago",	"F.Aplicacion", "vReference",	"vName", "Ref Pag", "Pagado","Capital"]]
           self.Base_1 = Base_1
        except:
             self.error.place(x = 10 , y = 80,  width = 300, height = 50)



    def open_file1(self):
        global LC
        errorT = tk.StringVar()
        error = tk.Button(self.frame1, textvariable = errorT, font = "Raleway", bg = "red",fg = "white")
        errorT.set("Data con columnas mal")


        #self.error = error
        
        try:
            self.Texto_1.set("loading...")
            file = askopenfile(parent = self.ventana, 
                               mode = 'rb', 
                               title = 'Choose a file', 
                               filetype = [("Data Files", "*.csv *.txt *.xlsx")])
                                        
            LC = pd.read_csv(file, low_memory = False,encoding='latin1')
            self.Texto_1.set("Cargado")
        except:
            errorT.set("Error cargalo como CSV")
            error.place(x = 10 , y = 80,  width = 300, height = 50)             
            
            
        LC = self.RenomColumns(LC)
        try:
           LC = LC[["Credito","nAmount","vFrecuencia","vTipo","vRegional","vDivisional","nDescuento"]]
           self.LC = LC
        except:
             error.place(x = 10 , y = 80,  width = 300, height = 50)             
        
        
    def save(self):
        try:
            self.Save_textf2.set("Exportando...")
            files = [("Excel Files", '*.xlsx')]
            fname = asksaveasfilename(filetypes = files, defaultextension = files)
            writer = pd.ExcelWriter(fname, engine='xlsxwriter')        
            
            self.Z_1.to_excel(writer, sheet_name = 'Data',startrow = 0 , startcol = 0 ,index=False)
            self.DIN.to_excel(writer, sheet_name = 'Resumen',startrow = 0 , startcol = 0 ,index=False)
            writer.save()
            writer.close()
            self.Save_textf2.set("Exportado")
            return self.Save_textf2.set("Exportado")
        except:
            return self.Save_text.set("Error")        
        
        




#%% Processing Data


    def AFILIADOPARA_C(self,dff):
        dff["Afiliado_2"]=np.where(dff["Afiliado"]=="ISSSTE ACTIVOS","Issste Activos",
                        np.where(dff["Afiliado"]=="IMSS ACTIVO ONLINE","Activos IMSS",
                        np.where(dff["Afiliado"]=="JYP PEMEX","JyP PEMEX",
                        np.where(dff["Afiliado"]=="JYP ESTATAL EXITUS","JYP ESTATAL EXITUS",
                        np.where(dff["Afiliado"]=="JYP IMSS PLATINO","J y P IMSS",
                        np.where(dff["Afiliado"]=="JYP ISSSTE 499","J y P ISSSTE",
                        np.where(dff["Afiliado"]=="JYP ISSSTE BCE","J y P ISSSTE",
                        np.where(dff["Afiliado"]=="JYP IMSS EXITUS","J y P IMSS",
                        np.where(dff["Afiliado"]=="IMSS ACTIVOS","Activos IMSS",
                        np.where(dff["Afiliado"]=="JYP ISSSTE EXITUS","J y P ISSSTE",
                        np.where(dff["Afiliado"]=="JYP ISSSTE ONLINE","J y P ISSSTE",
                        np.where(dff["Afiliado"]=="JYP FERRONALES","JyP FERRONALES",
                        np.where(dff["Afiliado"]=="JYP COMISION FEDERAL ELECTRICIDAD","JyP COMISION FEDERAL ELECTRICIDAD",
                        np.where(dff["Afiliado"]=="JYP ISSEMYM DOMICILIACION","JYP ISSEMYM DOMICILIACION",
                        np.where(dff["Afiliado"]=="JYP OTROS EXITUS","JyP OTROS",
                        np.where(dff["Afiliado"]=="SEP ACTIVOS","SEP ACTIVOS",
                        np.where(dff["Afiliado"]=="JYP ISSSTE PLATINO","J y P ISSSTE",
                        np.where(dff["Afiliado"]=="IMSS ACTIVOS BCE","Activos IMSS",
                        np.where(dff["Afiliado"]=="ESTATAL ACTIVOS","Estatal Activos",
                        np.where(dff["Afiliado"]=="JYP IMSS ONLINE","J y P IMSS",
                        np.where(dff["Afiliado"]=="JYP IMSS BCE","J y P IMSS",
                        np.where(dff["Afiliado"]=="JYP AFORES","JYP AFORES",
                        np.where(dff["Afiliado"]=="ACTIVOS GOBIERNO EDO MEX","Gobierno EDO MEX",
                        np.where(dff["Afiliado"]=="ACTIVOS GOBIERNO CDMX","Gobierno CDMX","NO APLICA"))))))))))))))))))))))))
        return dff
    
    
    def Process_1(self,df,df_LC):
        global Z_1
        self.ejecutar_textf2.set("Procesando..")
        try:
            df = self.AFILIADOPARA_C(df)
        except:
            self.errorT.set("Error Afiliado")
            self.error.place(x = 10 , y = 80,  width = 300, height = 50)
            
        try:
            df.drop(df.filter(regex = '^Unnamed:',axis = 1),1,inplace=True)
            df.drop_duplicates(keep = 'first', ignore_index=False,inplace=True)
            df['vReference_4'] = df['vReference'].str[:4]
            df = df[-df['vReference'].str.contains('DOM', na=False)]
            Pagos_D = df[(df['vReference'].str.contains('PAGO D', na=False))|(df['vReference'].str.contains('QUITA', na=False))|(df['vReference'].str.contains('SERLE', na=False))|(df['vReference'].str.contains('GAGSE', na=False))|(df['vReference'].str.contains('LIQUI', na=False))|(df['vReference'].str.contains('CAJIG', na=False))|(df['vReference'].str.contains('AYE', na=False))|(df['vReference'].str.contains('DG', na=False))]
            Pagos_D["Dictamen"] = "PaDi"
            Pagos_D["vReference_4"] = "PaDi"
            Remb_Ticket=df[df['vReference_4'].str.contains('7500', na=False)]
            Z=df[(df['vReference'].str.contains('Reembolsos', na=False))|(df['vReference'].str.contains('Anul', na=False))]#Checamos lo de anulaciones |(C['vReference'].str.contains('Anul', na=False))
            Z = pd.concat([Z,Remb_Ticket],axis=0)
            Z.reset_index(drop =  True, inplace = True)
            Z["Dictamen"] = np.where(Z['vReference'].str.contains('Anul', na=False),"Anulacion",np.where(Z['vReference'].str.contains('7500', na=False), "Reembolsos Ticket", "Reembolsos"))
            Z=pd.concat([Z,Pagos_D],axis=0)
            Z.reset_index(drop =  True, inplace = True)
            Z["vDateMovement"] = pd.to_datetime(Z["vDateMovement"],errors='coerce', format="%d/%m/%Y")
            Z['Mes'] = pd.to_datetime(Z['vDateMovement']).dt.to_period('M')
            Z=Z[["Credito","Afiliado","vDescription","vDateMovement","vDepositDate","vIdPago","F.Aplicacion","vReference","vName","Ref Pag","Pagado","Capital","vReference_4","Dictamen","Mes"]]
            Z_1 = pd.merge(Z,LC,how='left',on=["Credito"])
            Z_1 = Z_1[Z_1["vTipo"]=="DOMICILIA"]
            self.Z_1 = Z_1
            try:
                DIN = self.resumen()
                self.show_df(DIN)
            except:
                self.errorT.set("Error en el Resumen")
                self.error.place(x = 10 , y = 80,  width = 300, height = 50)

            
        except:
            self.errorT.set("Error al procesar la Data")
            self.error.place(x = 10 , y = 80,  width = 300, height = 50)
            
        return self.ejecutar_textf2.set("Ejecutado")
    
    
    def resumen(self):
        try:
            temp = pd.DataFrame(Z_1.groupby("Mes")["Credito"].count())
            temp = temp.rename_axis(None, axis=1).reset_index()
            temp.reset_index(drop = True, inplace= True)
            MM = temp[temp["Credito"] == temp["Credito"].max()]["Mes"].max()
    
            DIN = pd.pivot_table(Z_1[Z_1["Mes"]==MM], index = ["Mes", "vFrecuencia"], columns = "Dictamen", values = 'Pagado', aggfunc= [np.sum, np.count_nonzero],margins=True)
            DIN.columns = [f'{j}_{i}' for i, j in DIN.columns]
            DIN = DIN.rename_axis(None, axis=1).reset_index()
            DIN.drop(columns = ["All_sum", "All_count_nonzero"],inplace=True)
            DIN.replace(np.nan,0, inplace = True)
            DIN.iloc[:,2:6]=DIN.iloc[:,2:6].applymap("${0:,.2f}".format) #Este lo cambia a moneda 
            DIN.iloc[:,6:]=DIN.iloc[:,6:].applymap("{0:,.0f}".format) #Este lo cambia a moneda 
            self.DIN = DIN
            return self.DIN
        except:
            self.errorT.set("Error al procesar el Resumen")
            return self.error.place(x = 10 , y = 80,  width = 300, height = 50)
    

#Mostrar datos en Tkinter
    def show_df(self,df):
        
        frame = tk.Frame(self.ventana)
        frame.place(x = 10, y = 100, width = 580, height = 150)#frame.place(x = 20, y = 110, width = 185, height = 230)
        tree = tk.ttk.Treeview(frame, show="headings", columns=df.columns)#tree = tk.ttk.Treeview(self.ventana, show="headings", columns=F1.columns)
        hsb = tk.Scrollbar(frame, orient="horizontal", command=tree.xview)
        vsb = tk.Scrollbar(frame, orient="vertical", command=tree.yview)
        tree.configure(xscrollcommand=hsb.set, yscrollcommand=vsb.set)
        tree.grid(column=0, row=0, sticky=tk.NSEW)
        vsb.grid(column=1, row=0, sticky=tk.NS)
        hsb.grid(column=0, row=1, sticky=tk.EW)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(0, weight=1)
        for i, header in enumerate(df.columns):
            tree.column(i, width=100, anchor='center')
            tree.heading(i, text=header)
        for row in range(df.shape[0]):
            tree.insert('', 'end', values=list(df.iloc[row]))        
        return self.ejecutar_textf2.set("Ejecutado")



        
    def mostrar(self):
        self.ventana.mainloop()
    
  
    
  
        



#%% Creamos las funciones, botones y más 


roda = rodamientos()
roda.cargar_ventana()
roda.botones()
roda.mostrar()



"""

Z_1 = Z_1[Z_1["vTipo"]== "DOMICILIA"]

temp = pd.DataFrame(Z_1.groupby("Mes")["Credito"].count())
temp = temp.rename_axis(None, axis=1).reset_index()
temp.reset_index(drop = True, inplace= True)
MM = temp[temp["Credito"] == temp["Credito"].max()]["Mes"].max()

DIN = pd.pivot_table(Z_1[Z_1["Mes"]==MM], index = ["Mes", "vFrecuencia"], columns = "Dictamen", values = 'Pagado', aggfunc= [np.sum, np.count_nonzero])
DIN.columns = [f'{j}_{i}' for i, j in DIN.columns]
DIN = DIN.rename_axis(None, axis=1).reset_index()
DIN.replace(np.nan,0, inplace = True)


"""









