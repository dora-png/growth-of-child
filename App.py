# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 21:22:50 2020

@author: NDOUMBE DORA
"""
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import os
from sys import exit
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO

import io
# I/O files path
path = 'Data/'
path1='Data/Girls'
path2='Data/Boys'
Z=[]
Z1=[]
Z2=[]
Z3=[]
S1=[]
S3=[]
L=[]
M=[]
S=[]
L2=[]
M2=[]
S2=[]

root=Tk()
#for the title of the page
root.title('WellGrowth App')
#pour ne pas permettre de redimentionner la fenetre
root.resizable(False,False)
root.configure(background='#263D42')
canvas=tk.Canvas(root, height=600 ,width=1300,bg='#263D42' )
canvas.pack()

frame1=tk.Frame(root,bg='#263D42')
frame1.place(relwidth=0.5, relheight=0.5,rely=0.2)
#New=tk.Button(frame1,text='NEW',padx=10,pady=5,fg='#263D42',bg='white')
#New.pack()
Fermer=tk.Button(root,text='Close',padx=10,pady=5,fg='white',bg='#263D42')
Fermer.pack()
#View=tk.Button(frame1,text='VIEW',padx=10,pady=5,fg='#263D42',bg='white')
#View.pack()
frame2=tk.Frame(root,bg='#e8f8b8')
frame2.place(relwidth=0.5, relheight=0.1,rely=0.1)


Bunew= ttk.Button(frame2,text='New')
Bunew.grid(row=0,column=1)
Buview= ttk.Button(frame2,text='View')
Buview.grid(row=0,column=2)

def funcfermer():
    root.destroy()
Fermer.config(command=funcfermer)


def funcnew():
    for widget in frame1.winfo_children():
        widget.destroy()
    Buadd= ttk.Button(frame1,text='Add data')
    Buadd.grid(row=0,column=1)
    Buchild= ttk.Button(frame1,text='New child')
    Buchild.grid(row=0,column=2)
    def funcadd():
        for widget in frame1.winfo_children():
                widget.destroy()
        
        l1=ttk.Label(frame1,text='Age (months):')
        l1.grid(row=1,column=0)
        etAge=ttk.Entry(frame1,width=30,font=('Arial',12))
        etAge.grid(row=1,column=1,columnspan=2)
        l2=ttk.Label(frame1,text='Gender:')
        l2.grid(row=2,column=0)
#style
        root.configure(background='#263D42')
        style=ttk.Style()
        style.theme_use('classic')
        style.configure('TLabel',background='#263D42')
        style.configure('TButton',background='#263D42')
        style.configure('TRadiobutton',background='#263D42')
#for the check box
        rbVar=StringVar()
        rb1= ttk.Radiobutton(frame1,text='male',variable=rbVar,value='male')
        rb1.grid(row=2,column=1)
#rb1.pack()
        rb2= ttk.Radiobutton(frame1,text='female',variable=rbVar,value='female')
#rb2.pack()
        rb2.grid(row=2,column=2)
        l3=ttk.Label(frame1,text='Weight (kg):')
        l3.grid(row=4,column=0)
        etWeight=ttk.Entry(frame1,width=30,font=('Arial',12))
        etWeight.grid(row=4,column=1,columnspan=2)
        l4=ttk.Label(frame1,text='Lenght (cm):')
        l4.grid(row=5,column=0)
        etHeight=ttk.Entry(frame1,width=30,font=('Arial',12))
        etHeight.grid(row=5,column=1,columnspan=2)
        l5=ttk.Label(frame1,text='Id:')
        l5.grid(row=6,column=0)
        etId=ttk.Entry(frame1,width=30,font=('Arial',12))
        etId.grid(row=6,column=1,columnspan=2)
        
#for the button applied
        Buapplied= ttk.Button(frame1,text='APPLIED')
        Buapplied.grid(row=8,column=0)
        def BuClick():
        #for widget in frame1.winfo_children():
            #widget.destroy()
#exemple d'affichage print('Age{}'.format(etAge.get()))
#create an empty string and add element in it to write in the file
        
            Liste='\n'
            Liste=Liste + etId.get()
            Liste=Liste+','
            Liste=Liste + etAge.get()
            Liste=Liste+','
            Liste=Liste + rbVar.get()
            Liste=Liste+','
            Liste=Liste + etWeight.get()
            Liste=Liste+','
            Liste= Liste + etHeight.get()
            Liste=Liste+','
            Liste= Liste + ''
            Liste=Liste+','
            Liste= Liste + ''
            trouve=0
           
            #check if it is a girl or a boy to write in right file
            if((etId.get()=='')or(etAge.get()=='')or(rbVar.get()=='')or(etWeight.get()=='')or(etHeight.get()=='')):
                messagebox.showinfo(title='empty data',message='enter all your data')
            else:
                
                if(rbVar.get()=='female'):
                    datado= 'GirlDataSet.csv'
                    doub=np.genfromtxt(os.path.join(path,datado), delimiter=',', dtype = None, skip_header=1)
                    for line in doub :
                        if(etId.get()==str(line[0])):
                           trouve=1
                           if((float(etAge.get())<=float(line[1]))or((float(etHeight.get())<float(line[4])))):
                                
                                messagebox.showinfo(title='error on age or height ',message='This ID already have data for this age or this age/height is less than the previous')
                                etAge.delete(0,'end')
                                etHeight.delete(0,'end')
                                Liste[1]=etAge.get()
                                Liste[4]=etHeight.get()
                    if(trouve==1):  
                        out=open('Data/GirlDataSet.csv','a')
                        out.write(str(Liste))
                        out.close()
                        messagebox.showinfo(title='sending data',message='Data well submited')
                        etAge.delete(0,'end')
                        etWeight.delete(0,'end')
                        etHeight.delete(0,'end')
                        etId.delete(0,'end')
                        for widget in frame1.winfo_children():
                            widget.destroy()
                    else:
                         messagebox.showinfo(title='not existing id ',message='You should create a new child')
                         etAge.delete(0,'end')
                         etHeight.delete(0,'end')
                         etId.delete(0,'end')
                         etWeight.delete(0,'end')
                        
                if(rbVar.get()=='male'):
                    datado= 'BoyDataSet.csv'
                    doub=np.genfromtxt(os.path.join(path,datado), delimiter=',', dtype = None, skip_header=1)
                    for line in doub:
                        if(etId.get()==str(line[0])):
                           trouve=1
                           if((float(etAge.get())<=float(line[1]))or((float(etHeight.get())<float(line[4])))):
                                
                                messagebox.showinfo(title='error on age or height ',message='This ID already have data for this age or this age/height is less than the previous')
                                etAge.delete(0,'end')
                                etHeight.delete(0,'end')
                                Liste[1]=etAge.get()
                                Liste[4]=etHeight.get() 
                    if(trouve==1):  
                        out=open('Data/BoyDataSet.csv','a')
                        out.write(str(Liste))
                        out.close()
                        messagebox.showinfo(title='sending data',message='Data well submited')
                        etAge.delete(0,'end')
                        etWeight.delete(0,'end')
                        etHeight.delete(0,'end')
                        etId.delete(0,'end')
                        for widget in frame1.winfo_children():
                            widget.destroy()
                    else:
                         messagebox.showinfo(title='not existing id ',message='You should create a new child')
                         etAge.delete(0,'end')
                         etHeight.delete(0,'end')
                         etId.delete(0,'end')
                         etWeight.delete(0,'end')
        Buapplied.config(command=BuClick)
#for create a new child       
    def funchild():
        
        for widget in frame1.winfo_children():
                widget.destroy()
        
        l1=ttk.Label(frame1,text='Age ( months):')
        l1.grid(row=1,column=0)
        etAge=ttk.Entry(frame1,width=30,font=('Arial',12))
        etAge.grid(row=1,column=1,columnspan=2)
        l2=ttk.Label(frame1,text='Gender:')
        l2.grid(row=2,column=0)
#style
        root.configure(background='#263D42')
        style=ttk.Style()
        style.theme_use('classic')
        style.configure('TLabel',background='#263D42')
        style.configure('TButton',background='#263D42')
        style.configure('TRadiobutton',background='#263D42')
#for the check box
        rbVar=StringVar()
        rb1= ttk.Radiobutton(frame1,text='male',variable=rbVar,value='male')
        rb1.grid(row=2,column=1)
#rb1.pack()
        rb2= ttk.Radiobutton(frame1,text='female',variable=rbVar,value='female')
#rb2.pack()
        rb2.grid(row=2,column=2)
        l3=ttk.Label(frame1,text='Weight (kg):')
        l3.grid(row=4,column=0)
        etWeight=ttk.Entry(frame1,width=30,font=('Arial',12))
        etWeight.grid(row=4,column=1,columnspan=2)
        l4=ttk.Label(frame1,text='Lenght (cm):')
        l4.grid(row=5,column=0)
        etHeight=ttk.Entry(frame1,width=30,font=('Arial',12))
        etHeight.grid(row=5,column=1,columnspan=2)
        l5=ttk.Label(frame1,text='Id:')
        l5.grid(row=6,column=0)
        etId=ttk.Entry(frame1,width=30,font=('Arial',12))
        etId.grid(row=6,column=1,columnspan=2)
        l6=ttk.Label(frame1,text='Name :')
        l6.grid(row=7,column=0)
        etName=ttk.Entry(frame1,width=30,font=('Arial',12))
        etName.grid(row=7,column=1,columnspan=2)
        l7=ttk.Label(frame1,text='Parent :')
        l7.grid(row=8,column=0)
        etParent=ttk.Entry(frame1,width=30,font=('Arial',12))
        etParent.grid(row=8,column=1,columnspan=2)
#for the button applied
        Buapplied= ttk.Button(frame1,text='APPLIED')
        Buapplied.grid(row=9,column=0)
        def BuClick():
        #for widget in frame1.winfo_children():
            #widget.destroy()
#exemple d'affichage print('Age{}'.format(etAge.get()))
#create an empty string and add element in it to write in the file
        
            Liste='\n'
            Liste=Liste + etId.get()
            Liste=Liste+','
            Liste=Liste + etAge.get()
            Liste=Liste+','
            Liste=Liste + rbVar.get()
            Liste=Liste+','
            Liste=Liste + etWeight.get()
            Liste=Liste+','
            Liste= Liste + etHeight.get()
            Liste=Liste+','
            Liste= Liste + etName.get()
            Liste=Liste+','
            Liste= Liste + etParent.get()
       
#check if it is a girl or a boy to write in right file
            if((etId.get()=='')or(etAge.get()=='')or(rbVar.get()=='')or(etWeight.get()=='')or(etHeight.get()=='')or(etName.get()=='')or(etParent.get()=='')):
                messagebox.showinfo(title='empty data',message='enter all your data')
            else:
                
                if(rbVar.get()=='female'):
                    datado= 'GirlDataSet.csv'
                    doub=np.genfromtxt(os.path.join(path,datado), delimiter=',', dtype = None, skip_header=1)
                    for line in doub :
                        if(etId.get()==str(line[0])):
                            messagebox.showinfo(title='existing child ',message='This child (ID) already exist in the file')
                            etId.delete(0,'end')
                            Liste[0]=etId.get()
                    out=open('Data/GirlDataSet.csv','a')
                    out.write(str(Liste))
                    out.close()
                
                if(rbVar.get()=='male'):
                    datado= 'BoyDataSet.csv'
                    doub=np.genfromtxt(os.path.join(path,datado), delimiter=',', dtype = None, skip_header=1)
                    for line in doub:
                        if(etId.get()==str(line[0])):
                            messagebox.showinfo(title='existing child ',message='This child already exist in the file')
                            etId.delete(0,'end')
                            Liste[0]=etId.get() 
                    out=open('Data/BoyDataSet.csv','a')
                    out.write(str(Liste))
                    out.close()
                messagebox.showinfo(title='sending data',message='Data well submited')
                etAge.delete(0,'end')
                etWeight.delete(0,'end')
                etHeight.delete(0,'end')
                etId.delete(0,'end')
                for widget in frame1.winfo_children():
                    widget.destroy()
             
        
            
        Buapplied.config(command=BuClick)
    Buadd.config(command=funcadd)
    Buchild.config(command=funchild)            
    
#to get the different values entered
Bunew.config(command=funcnew)

def But():
    for widget in frame1.winfo_children():
            widget.destroy()
    l5=ttk.Label(frame1,text='Id:')
    l5.grid(row=0,column=0)
    etId=ttk.Entry(frame1,width=30,font=('Arial',12))
    etId.grid(row=0,column=1,columnspan=2)
    l2=ttk.Label(frame1,text='Gender:')
    l2.grid(row=1,column=0)
    rbVar=StringVar()
    rb1= ttk.Radiobutton(frame1,text='male',variable=rbVar,value='male')
    rb1.grid(row=1,column=1)
#rb1.pack()
    rb2= ttk.Radiobutton(frame1,text='female',variable=rbVar,value= 'female')
    rb2.grid(row=1,column=2)
    Buterm= ttk.Button(frame1,text='VISUALISE')
    Buterm.grid(row=0,column=4)
    def funcok():
        
        frame=tk.Frame(root,bg='white')
        frame.place(relwidth=0.8, relheight=0.8,relx=0.5,rely=0.1)
        
        Buchart1= ttk.Button(frame1,text='Individual vs Local chart')
        Buchart1.grid(row=5,column=1)
        Buchart2= ttk.Button(frame1,text='Individual vs WHO')
        Buchart2.grid(row=4,column=1)
        Buchart3= ttk.Button(frame1,text='Individual vs Local chart vs WHO')
        Buchart3.grid(row=7,column=1)
        Buchart4= ttk.Button(frame1,text='Inconsistency in child growth')
        Buchart4.grid(row=6,column=1)
        Bufile= ttk.Button(frame1,text='individual file')
        Bufile.grid(row=3,column=1)
        def funcfile():
            ligne='Id,Age,Gender,Weight,Height,Name,Parent\n'
            if(rbVar.get()=='female'):
                chdat = 'GirlDataSet.csv'
                #charray = np.genfromtxt(os.path.join(path,chdata), delimiter=',', dtype = None, skip_header=1)
                charra = open(os.path.join(path,chdat),'r')
               
                for line in charra:
                        #print(line)
                        #lign = charray.readline()
                        if(etId.get()==str(line[0])):
                             line=str(line)+'\n'
                             ligne=ligne+line
                             #ligne = charray.readlines()
                             #print(ligne)
                             savefile='file' +str(etId.get()) + '.csv'
                out=open(os.path.join(path1,savefile),'w')
                out.write(str(ligne))
                out.close()
            else:
                chdat = 'BoyDataSet.csv'
                #charray = np.genfromtxt(os.path.join(path,chdata), delimiter=',', dtype = None, skip_header=1)
                charra = open(os.path.join(path,chdat),'r')
                for line in charra:
                        if(etId.get()==str(line[0])):
                             line=str(line)+'\n'
                             ligne=ligne+line
                             savefile='file' +str(etId.get()) + '.csv'
                out=open(os.path.join(path2,savefile),'w')
                out.write(str(ligne))
                out.close()
        Bufile.config(command=funcfile)
        def funcpb():
            
            for widget in frame.winfo_children():
                    widget.destroy()
            Busave= ttk.Button(frame,text='Save')
            Busave.pack()
            Buquit= ttk.Button(frame,text='Quit')
            Buquit.pack()
            find=0
            if((rbVar.get()=='')or(etId.get()=='')):
                    messagebox.showinfo(title='empty data',message='enter all data')
            else:
            
                if(rbVar.get()=='female'):
                    chdata = 'GirlDataSet.csv'
# Age, weight, height
                    charray = np.genfromtxt(os.path.join(path,chdata), delimiter=',', dtype = None, skip_header=1,encoding=None)
                    
#skip_header indique la ligne de debut du fichier a prendre en compte
    
    # ---
# ---
                    chawarrayX = []
                    chalarrayX = []
                    chawarrayY = []
                    chalarrayY = []
                
                # sublist[0] : Age
# sublist[1] : Weight
# sublist[2] : Length
        #take the entered values to write them
                    for sublist in charray:
                        if(int(etId.get())==sublist[0]):
                            chawarrayX.append(sublist[1])
                            chawarrayY.append(sublist[3])
                            chalarrayX.append(sublist[1])
                            chalarrayY.append(sublist[4])
                            find=1
                    if(find==0):
                            messagebox.showinfo(title='not existing id',message='individual data are empty')
                            for widget in frame.winfo_children():
                                widget.destroy()
                            frame.destroy()
                    else:
                        # read girls'  WHO charts
    # Read age vs weight WHO data
                        awdata = 'g_age_weight.csv'
                        awarray = np.loadtxt(os.path.join(path,awdata), delimiter=',', skiprows=1)
        # Read age vs length WHO data
                        aldata = 'g_age_length.csv'
                        alarray = np.loadtxt(os.path.join(path,aldata), delimiter=',', skiprows=1)
        # Read age vs weight nigeria data
                        awNdata = 'g_age_N_weight.csv'
                        awNarray = np.loadtxt(os.path.join(path,awNdata), delimiter=',', skiprows=1)
        # Read age vs lenght nigeria data
                        alNdata = 'g_age_N_lenght.csv'
                        alNarray = np.loadtxt(os.path.join(path,alNdata), delimiter=',', skiprows=1)
                        
                         # Plots
                    
                        plt.figure()
                                
   # Age vs weight
                        plt.subplot(2,1,1)
                        scoreData='scoreW_Girls_.csv'
                        Zfile=np.loadtxt(os.path.join(path,scoreData), delimiter=',', skiprows=1)
                        for line in Zfile:
                            Z.append(line[1])
                            L.append(line[2])
                            M.append(line[3])
                            S.append(line[4])
                        for i in range(len(chawarrayX)):
                            if((1/(S[i]*L[i]))*((chawarrayY[i]/M[i])**L[i]-1)<-3)or((1/(S[i]*L[i]))*((chawarrayY[i]/M[i])**L[i]-1)>3):
                                plt.plot(\
                                awarray[:,0],awarray[:,5],'k-',\
                                awNarray[:,0],awNarray[:,1],'b-',\
                                chawarrayX[i:i+2],chawarrayY[i:i+2],'r-*')
            
                                plt.grid(True)
                                plt.title('Girl ID %s' %etId.get())
                                plt.xlabel('age [months]')
                                plt.ylabel('weight [kg]')
                                plt.xlim([0,12])
                                plt.xticks(np.arange(0,13,1))
                
                                plt.text(awarray[5,0], awarray[5,5],'50%',fontsize=10)
                                plt.text(awNarray[1,0], awNarray[1,1],'50%',fontsize=10)
                                
                            if((1/(S[i]*L[i]))*((chawarrayY[i]/M[i])**L[i]-1)>=-3)and((1/(S[i]*L[i]))*((chawarrayY[i]/M[i])**L[i]-1)<-2):
                               
                                plt.plot(\
                                awarray[:,0],awarray[:,5],'k-',\
                                awNarray[:,0],awNarray[:,1],'b-',\
                                chawarrayX[i:i+2],chawarrayY[i:i+2],'y-*')
            
                                plt.grid(True)
                                plt.title('Girl ID %s' %etId.get())
                                plt.xlabel('age [months]')
                                plt.ylabel('weight [kg]')
                                plt.xlim([0,12])
                                plt.xticks(np.arange(0,13,1))
                
                                plt.text(awarray[5,0], awarray[5,5],'50%',fontsize=10)
                                plt.text(awNarray[1,0], awNarray[1,1],'50%',fontsize=10)
                                
                            if((1/(S[i]*L[i]))*((chawarrayY[i]/M[i])**L[i]-1)>=-2)and((1/(S[i]*L[i]))*((chawarrayY[i]/M[i])**L[i]-1)<=3):
                               
                                if(i<=len(chawarrayX)-2)and(chawarrayY[i]==chawarrayY[i+1]):
                                    plt.plot(\
                                    awarray[:,0],awarray[:,5],'k-',\
                                    awNarray[:,0],awNarray[:,1],'b-',\
                                    chawarrayX[i:i+2],chawarrayY[i:i+2],'y-*')
                
                                    plt.grid(True)
                                    plt.title('Girl ID %s' %etId.get())
                                    plt.xlabel('age [months]')
                                    plt.ylabel('weight [kg]')
                                    plt.xlim([0,12])
                                    plt.xticks(np.arange(0,13,1))
                                    plt.text(awarray[5,0], awarray[5,5],'50%',fontsize=10)
                                    plt.text(awNarray[1,0], awNarray[1,1],'50%',fontsize=10)
                                else:
                                    plt.plot(\
                                    awarray[:,0],awarray[:,5],'k-',\
                                    awNarray[:,0],awNarray[:,1],'b-',\
                                    chawarrayX[i:i+2],chawarrayY[i:i+2],'g-*')
                
                                    plt.grid(True)
                                    plt.title('Girl ID %s' %etId.get())
                                    plt.xlabel('age [months]')
                                    plt.ylabel('weight [kg]')
                                    plt.xlim([0,12])
                                    plt.xticks(np.arange(0,13,1))
                                    plt.text(awarray[5,0], awarray[5,5],'50%',fontsize=10)
                                    plt.text(awNarray[1,0], awNarray[1,1],'50%',fontsize=10)
                                
                            # Age vs length
                    
                        plt.subplot(2,1,2)
                        scoreData1='scoreL_Girls_.csv'
                        Z1file=np.loadtxt(os.path.join(path,scoreData1), delimiter=',', skiprows=1)
                        for line in Z1file:
                            Z1.append(line[1])
                            S1.append(line[2])
                        
                        for i in range(len(chalarrayX)):
                            if(chalarrayY[i]-Z1[i]<-3*S1[i])or(chalarrayY[i]-Z1[i]>3*S1[i]):
                                plt.plot(\
                                alarray[:,0],alarray[:,5],'k-',\
                                alNarray[:,0],alNarray[:,1],'b-',\
                                chalarrayX[i:i+2],chalarrayY[i:i+2],'r-*')
            
                                plt.grid(True)
                               
                                plt.xlabel('age [months]')
                                plt.ylabel('lenght [cm]')
                                plt.xlim([0,12])
                                plt.xticks(np.arange(0,13,1))
                
                                plt.text(alarray[5,0], alarray[5,5],'50%',fontsize=10)
                                plt.text(alNarray[1,0], alNarray[1,1],'50%',fontsize=10)
                                
                            if(chalarrayY[i]-Z1[i]>=-3*S1[i])and(chalarrayY[i]-Z1[i]<-2*S1[i]):
                                plt.plot(\
                                alarray[:,0],alarray[:,5],'k-',\
                                alNarray[:,0],alNarray[:,1],'b-',\
                                chalarrayX[i:i+2],chalarrayY[i:i+2],'y-*')
            
                                plt.grid(True)
                                
                                plt.xlabel('age [months]')
                                plt.ylabel('lenght [cm]')
                                plt.xlim([0,12])
                                plt.xticks(np.arange(0,13,1))
                
                                plt.text(alarray[5,0], alarray[5,5],'50%',fontsize=10)
                                plt.text(alNarray[1,0], alNarray[1,1],'50%',fontsize=10)
                                
                            if(chalarrayY[i]-Z1[i]>=-2*S1[i])and(chalarrayY[i]-Z1[i]<=3*S1[i]):
                                if(i<=len(chalarrayX)-2)and(chalarrayY[i]==chalarrayY[i+1]):
                                    plt.plot(\
                                    alarray[:,0],alarray[:,5],'k-',\
                                    alNarray[:,0],alNarray[:,1],'b-',\
                                    chalarrayX[i:i+2],chalarrayY[i:i+2],'y-*')
                
                                    plt.grid(True)
                                    
                                    plt.xlabel('age [months]')
                                    plt.ylabel('lenght [cm]')
                                    plt.xlim([0,12])
                                    plt.xticks(np.arange(0,13,1))
                                    plt.text(alarray[5,0], alarray[5,5],'50%',fontsize=10)
                                    plt.text(alNarray[1,0], alNarray[1,1],'50%',fontsize=10)
                                else:
                                    plt.plot(\
                                    alarray[:,0],alarray[:,5],'k-',\
                                    alNarray[:,0],alNarray[:,1],'b-',\
                                    chalarrayX[i:i+2],chalarrayY[i:i+2],'g-*')
                
                                    plt.grid(True)
                                    
                                    plt.xlabel('age [months]')
                                    plt.ylabel('lenght [cm]')
                                    plt.xlim([0,12])
                                    plt.xticks(np.arange(0,13,1))
                                    plt.text(alarray[5,0], alarray[5,5],'50%',fontsize=10)
                                    plt.text(alNarray[1,0], alNarray[1,1],'50%',fontsize=10)
                                
                        
# Adjust distance between subplots
                        plt.subplots_adjust(wspace=0.4, hspace=0.4)
    # Show & save graphs and show legend
                        fig1 = plt.gcf()
                        fig1.legend(labels=('WHO','local','individual'), loc='lower right')
                        #plt.show()
                        #plt.draw()
            
                        chart=FigureCanvasTkAgg(fig1 , frame)
                        chart.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH) 
        
                        fig1.set_size_inches(16, 9)
                        fig1.savefig(os.path.join(path,'graph.pdf'), dpi=100)
                        fig1.savefig(os.path.join(path,'graph.png'), dpi=100)
                   

                if(rbVar.get()=='male'):
                     chdata = 'BoyDataSet.csv'
    # Age, weight, height

                     charray = np.genfromtxt(os.path.join(path,chdata), delimiter=',', dtype = None, skip_header=1,encoding=None)
#skip_header indique la ligne de debut du fichier a prendre en compte
    
    # --- 

                     chawarrayX = []
                     chalarrayX = []
                     chawarrayY = []
                     chalarrayY = []
# sublist[1] : Age
# sublist[3] : Weight
# sublist[4] : Length
                     for sublist in charray:
                         if(int(etId.get())==sublist[0]):
                            chawarrayX.append(sublist[1])
                            chawarrayY.append(sublist[3]) 
                            chalarrayX.append(sublist[1])
                            chalarrayY.append(sublist[4])
                            find=1
                     if(find==0):
                            messagebox.showinfo(title='not existing id',message='individual data are empty')
                            for widget in frame.winfo_children():
                                widget.destroy()
                            frame.destroy()
                     else:
                     # read boys' (0-2) WHO charts
    # Read age vs weight WHO data
                         awdata = 'b_age_weight.csv'
                         awarray = np.loadtxt(os.path.join(path,awdata), delimiter=',', skiprows=1)
                            # Read age vs length WHO data
                         aldata = 'b_age_length.csv'
                         alarray = np.loadtxt(os.path.join(path,aldata), delimiter=',', skiprows=1)
                            #Read age vs weight nigerian data
                         awNdata = 'b_age_N_weight.csv'
                         awNarray = np.loadtxt(os.path.join(path,awNdata), delimiter=',', skiprows=1)
                            #Read age vs lenght nigerian data
                         alNdata = 'b_age_N_length.csv'
                         alNarray = np.loadtxt(os.path.join(path,alNdata), delimiter=',', skiprows=1)
                                 # Plots
                         plt.figure()
                          # Age vs weight
                         plt.subplot(2,1,1)
                         scoreData2='scoreW_Boys_.csv'
                         Z2file=np.loadtxt(os.path.join(path,scoreData2), delimiter=',', skiprows=1)
                         for line in Z2file:
                             Z2.append(line[1])
                             L2.append(line[2])
                             M2.append(line[3])
                             S2.append(line[4])
                         for i in range(len(chawarrayX)):
                                if((1/(S2[i]*L2[i]))*((chawarrayY[i]/M2[i])**L2[i]-1)<-3)or((1/(S2[i]*L2[i]))*((chawarrayY[i]/M2[i])**L2[i]-1)>3):
                                    plt.plot(\
                                    awarray[:,0],awarray[:,5],'k-',\
                                    awNarray[:,0],awNarray[:,1],'b-',\
                                    chawarrayX[i:i+2],chawarrayY[i:i+2],'r-*')
                
                                    plt.grid(True)
                                    plt.title('Boy ID %s' %etId.get())
                                    plt.xlabel('age [months]')
                                    plt.ylabel('weight [kg]')
                                    plt.xlim([0,12])
                                    plt.xticks(np.arange(0,13,1))
                    
                                    plt.text(awarray[5,0], awarray[5,5],'50%',fontsize=10)
                                    plt.text(awNarray[1,0], awNarray[1,1],'50%',fontsize=10)
                                    
                                if((1/(S2[i]*L2[i]))*((chawarrayY[i]/M2[i])**L2[i]-1)>=-3)and((1/(S2[i]*L2[i]))*((chawarrayY[i]/M2[i])**L2[i]-1)<-2):
                                    plt.plot(\
                                    awarray[:,0],awarray[:,5],'k-',\
                                    awNarray[:,0],awNarray[:,1],'b-',\
                                    chawarrayX[i:i+2],chawarrayY[i:i+2],'y-*')
                                    plt.grid(True)
                                    plt.title('Boy ID %s' %etId.get())
                                    plt.xlabel('age [months]')
                                    plt.ylabel('weight [kg]')
                                    plt.xlim([0,12])
                                    plt.xticks(np.arange(0,13,1))
                    
                                    plt.text(awarray[5,0], awarray[5,5],'50%',fontsize=10)
                                    plt.text(awNarray[1,0], awNarray[1,1],'50%',fontsize=10)
                                    
                                if((1/(S2[i]*L2[i]))*((chawarrayY[i]/M2[i])**L2[i]-1)>=-2)and((1/(S2[i]*L2[i]))*((chawarrayY[i]/M2[i])**L2[i]-1)<=3):
                                    if(i<=len(chawarrayX)-2)and(chawarrayY[i]==chawarrayY[i+1]):
                                        plt.plot(\
                                        awarray[:,0],awarray[:,5],'k-',\
                                        awNarray[:,0],awNarray[:,1],'b-',\
                                        chawarrayX[i:i+2],chawarrayY[i:i+2],'y-*')
                    
                                        plt.grid(True)
                                        plt.title('Boy ID %s' %etId.get())
                                        plt.xlabel('age [months]')
                                        plt.ylabel('weight [kg]')
                                        plt.xlim([0,12])
                                        plt.xticks(np.arange(0,13,1))
                                        plt.text(awarray[5,0], awarray[5,5],'50%',fontsize=10)
                                        plt.text(awNarray[1,0], awNarray[1,1],'50%',fontsize=10)
                                    else:
                                        plt.plot(\
                                        awarray[:,0],awarray[:,5],'k-',\
                                        awNarray[:,0],awNarray[:,1],'b-',\
                                        chawarrayX[i:i+2],chawarrayY[i:i+2],'g-*')
                    
                                        plt.grid(True)
                                        plt.title('Boy ID %s' %etId.get())
                                        plt.xlabel('age [months]')
                                        plt.ylabel('weight [kg]')
                                        plt.xlim([0,12])
                                        plt.xticks(np.arange(0,13,1))
                                        plt.text(awarray[5,0], awarray[5,5],'50%',fontsize=10)
                                        plt.text(awNarray[1,0], awNarray[1,1],'50%',fontsize=10)
                              
                       # Age vs length
                         plt.subplot(2,1,2)
                         scoreData3='scoreL_Boys_.csv'
                         Z3file=np.loadtxt(os.path.join(path,scoreData3), delimiter=',', skiprows=1)
                         for line in Z3file:
                             Z3.append(line[1])
                             S3.append(line[2])
                             
                         for i in range(len(chalarrayX)):
                                    if(chalarrayY[i]-Z3[i]<-3*S3[i])or(chalarrayY[i]-Z3[i]>3*S3[i]):
                                        plt.plot(\
                                        alarray[:,0],alarray[:,5],'k-',\
                                        alNarray[:,0],alNarray[:,1],'b-',\
                                        chalarrayX[i:i+2],chalarrayY[i:i+2],'r-*')
                    
                                        plt.grid(True)
                                        
                                        plt.xlabel('age [months]')
                                        plt.ylabel('lenght [cm]')
                                        plt.xlim([0,12])
                                        plt.xticks(np.arange(0,13,1))
                        
                                        plt.text(alarray[5,0], alarray[5,5],'50%',fontsize=10)
                                        plt.text(alNarray[1,0], alNarray[1,1],'50%',fontsize=10)
                                  
                                    if(chalarrayY[i]-Z3[i]>=-3*S3[i])and(chalarrayY[i]-Z3[i]<-2*S3[i]):
                                        plt.plot(\
                                        alarray[:,0],alarray[:,5],'k-',\
                                        alNarray[:,0],alNarray[:,1],'b-',\
                                        chalarrayX[i:i+2],chalarrayY[i:i+2],'y-*')
                    
                                        plt.grid(True)
                                      
                                        plt.xlabel('age [months]')
                                        plt.ylabel('lenght [cm]')
                                        plt.xlim([0,12])
                                        plt.xticks(np.arange(0,13,1))
                        
                                        plt.text(alarray[5,0], alarray[5,5],'50%',fontsize=10)
                                        plt.text(alNarray[1,0], alNarray[1,1],'50%',fontsize=10)
                                        
                                    if(chalarrayY[i]-Z3[i]>=-2*S3[i])and(chalarrayY[i]-Z3[i]<=3*S3[i]):
                                        if(i<=len(chalarrayX)-2)and(chalarrayY[i]==chalarrayY[i+1]):
                                            plt.plot(\
                                            alarray[:,0],alarray[:,5],'k-',\
                                            alNarray[:,0],alNarray[:,1],'b-',\
                                            chalarrayX[i:i+2],chalarrayY[i:i+2],'y-*')
                        
                                            plt.grid(True)
                                            
                                            plt.xlabel('age [months]')
                                            plt.ylabel('lenght [kg]')
                                            plt.xlim([0,12])
                                            plt.xticks(np.arange(0,13,1))
                                            plt.text(alarray[5,0], alarray[5,5],'50%',fontsize=10)
                                            plt.text(alNarray[1,0], alNarray[1,1],'50%',fontsize=10)
                                        else:
                                            plt.plot(\
                                            alarray[:,0],alarray[:,5],'k-',\
                                            alNarray[:,0],alNarray[:,1],'b-',\
                                            chalarrayX[i:i+2],chalarrayY[i:i+2],'g-*')
                            
                                            plt.grid(True)
                                                
                                            plt.xlabel('age [months]')
                                            plt.ylabel('lenght [kg]')
                                            plt.xlim([0,12])
                                            plt.xticks(np.arange(0,13,1))
                                            plt.text(alarray[5,0], alarray[5,5],'50%',fontsize=10)
                                            plt.text(alNarray[1,0], alNarray[1,1],'50%',fontsize=10)
     # Adjust distance between subplots
                         plt.subplots_adjust(wspace=0.4, hspace=0.4)
    # Show & save graphs and show legend
                         fig1 = plt.gcf()
                         fig1.legend(labels=('WHO','local','individual'), loc='lower right')
                         #plt.show()
                         #plt.draw()
            
                         chart=FigureCanvasTkAgg(fig1 , frame)
                         chart.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH) 
                
                         fig1.set_size_inches(16, 9)
                         fig1.savefig(os.path.join(path,'graph.pdf'), dpi=100)
                         fig1.savefig(os.path.join(path,'graph.png'), dpi=100)
                                
            def funcsave():
                    if(rbVar.get()=='female'):
                        savefile='curve' +str(etId.get()) + '.png'
                        fig1.savefig(os.path.join(path1,savefile), dpi=100)
                    else:
                        savefile='curve' +str(etId.get()) + '.png'
                        fig1.savefig(os.path.join(path2,savefile), dpi=100)
                    
            Busave.config(command=funcsave)  
            def funcquit():
                    frame.destroy()
                    for widget in frame1.winfo_children():
                         widget.destroy()
            Buquit.config(command=funcquit)
                                            
        Buchart4.config(command=funcpb)           
                
        def funct3():
            
            for widget in frame.winfo_children():
                widget.destroy()
            Busave= ttk.Button(frame,text='Save')
            Busave.pack()
            Buquit= ttk.Button(frame,text='Quit')
            Buquit.pack()
            find=0
           # Busave.grid(row=7,column=1)
            if((rbVar.get()=='')or(etId.get()=='')):
                messagebox.showinfo(title='empty data',message='enter all data')
            else:
            
                if(rbVar.get()=='female'):
                    chdata = 'GirlDataSet.csv'
# Age, weight, height
                    

                    charray = np.genfromtxt(os.path.join(path,chdata), delimiter=',', dtype = None, skip_header=1, encoding=None)
                    
#skip_header indique la ligne de debut du fichier a prendre en compte
    
    # ---
# ---
                    chawarrayX = []
                    chalarrayX = []
                    chawarrayY = []
                    chalarrayY = []
                
                # sublist[0] : Age
# sublist[1] : Weight
# sublist[2] : Length
        #take the entered values to write them
                    for sublist in charray:
                        if(int(etId.get())==sublist[0]):
                            chawarrayX.append(sublist[1])
                            chawarrayY.append(sublist[3])
                            chalarrayX.append(sublist[1])
                            chalarrayY.append(sublist[4])
                            find=1
                    if(find==0):
                            messagebox.showinfo(title='not existing id',message='individual data are empty')
                            for widget in frame.winfo_children():
                                widget.destroy()
                            frame.destroy()
                    else:        
    # read girls'  WHO charts
    # Read age vs weight WHO data
                        awdata = 'g_age_weight.csv'
                        awarray = np.loadtxt(os.path.join(path,awdata), delimiter=',', skiprows=1)
        # Read age vs length WHO data
                        aldata = 'g_age_length.csv'
                        alarray = np.loadtxt(os.path.join(path,aldata), delimiter=',', skiprows=1)
        # Read age vs weight nigeria data
                        awNdata = 'g_age_N_weight.csv'
                        awNarray = np.loadtxt(os.path.join(path,awNdata), delimiter=',', skiprows=1)
        # Read age vs lenght nigeria data
                        alNdata = 'g_age_N_lenght.csv'
                        alNarray = np.loadtxt(os.path.join(path,alNdata), delimiter=',', skiprows=1)
        
                         # Plots
                        plt.figure()
                
                 # Age vs weight
                        plt.subplot(2,1,1)
                        plt.plot(\
                        awarray[:,0],awarray[:,5],'k-',\
                        awNarray[:,0],awNarray[:,1],'b-',\
                        chawarrayX,chawarrayY,'g-*')
            
                        plt.grid(True)
                        plt.title('Girl ID %s' %etId.get())
                        plt.xlabel('age [months]')
                        plt.ylabel('weight [kg]')
                        plt.xlim([0,12])
                        plt.xticks(np.arange(0,13,1))
        
                        plt.text(awarray[5,0], awarray[5,5],'50%',fontsize=10)
                        plt.text(awNarray[1,0], awNarray[1,1],'50%',fontsize=10)
                    
                     # Age vs length
                        plt.subplot(2,1,2)
                        plt.plot(\
                        alarray[:,0],alarray[:,5],'k-',\
                        alNarray[:,0],alNarray[:,1],'b-',\
                        chalarrayX,chalarrayY,'g-*')
    
                        plt.grid(True)
                        plt.xlabel('age [months]')
                        plt.ylabel('length [cm]')
                        plt.xlim([0,12])
                        plt.xticks(np.arange(0,13,1))
        
                        plt.text(alarray[5,0], alarray[5,5],'50%',fontsize=10)
                        plt.text(alNarray[1,0], alNarray[1,1],'50%',fontsize=10)
                    
                      # Adjust distance between subplots
                        plt.subplots_adjust(wspace=0.4, hspace=0.4)

# Show & save graphs and show legend
                        fig1 = plt.gcf()
                        fig1.legend(labels=('WHO','local','individual'), loc='lower right')
                        #plt.show()
                        #plt.draw()
            
                        chart=FigureCanvasTkAgg(fig1 , frame)
                        chart.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH) 
        
                        fig1.set_size_inches(16, 9)
                        fig1.savefig(os.path.join(path,'graph.pdf'), dpi=100)
                        fig1.savefig(os.path.join(path,'graph.png'), dpi=100)
                        
                if(rbVar.get()=='male'):
                     chdata = 'BoyDataSet.csv'
    # Age, weight, height

                     charray = np.genfromtxt(os.path.join(path,chdata), delimiter=',', dtype = None, skip_header=1, encoding=None)
                     
#skip_header indique la ligne de debut du fichier a prendre en compte
    
    # --- 

                     chawarrayX = []
                     chalarrayX = []
                     chawarrayY = []
                     chalarrayY = []
# sublist[0] : Age
# sublist[1] : Weight
# sublist[2] : Length
                     for sublist in charray:
                         if(int(etId.get())==sublist[0]):
                            chawarrayX.append(sublist[1])
                            chawarrayY.append(sublist[3]) 
                            chalarrayX.append(sublist[1])
                            chalarrayY.append(sublist[4])
                            find=1
                     if(find==0):
                            messagebox.showinfo(title='not existing id',message='individual data are empty')
                            for widget in frame.winfo_children():
                                widget.destroy()
                            frame.destroy()
                     else:
     # read boys' (0-2) WHO charts
    # Read age vs weight WHO data
                         awdata = 'b_age_weight.csv'
                         awarray = np.loadtxt(os.path.join(path,awdata), delimiter=',', skiprows=1)
                            # Read age vs length WHO data
                         aldata = 'b_age_length.csv'
                         alarray = np.loadtxt(os.path.join(path,aldata), delimiter=',', skiprows=1)
                            #Read age vs weight nigerian data
                         awNdata = 'b_age_N_weight.csv'
                         awNarray = np.loadtxt(os.path.join(path,awNdata), delimiter=',', skiprows=1)
                            #Read age vs lenght nigerian data
                         alNdata = 'b_age_N_length.csv'
                         alNarray = np.loadtxt(os.path.join(path,alNdata), delimiter=',', skiprows=1)
                                 # Plots
                         plt.figure()
            
         # Age vs weight
                         plt.subplot(2,1,1)
                         plt.plot(\
                         awarray[:,0],awarray[:,5],'k-',\
                         awNarray[:,0],awNarray[:,1],'b-',\
                         chawarrayX,chawarrayY,'g-*')
                                
                         plt.grid(True)
                         plt.title('Boy ID %s' %etId.get())
                         plt.xlabel('age [months]')
                         plt.ylabel('weight [kg]')
                         plt.xlim([0,12])
                         plt.xticks(np.arange(0,13,1))
                        
                         plt.text(awarray[5,0], awarray[5,5],'50%',fontsize=10)
                         plt.text(awNarray[1,0], awNarray[1,1],'50%',fontsize=10)
            # Age vs length 
                         plt.subplot(2,1,2)
                         plt.plot(\
                         alarray[:,0],alarray[:,5],'k-',\
                         alNarray[:,0],alNarray[:,1],'b-',\
                         chalarrayX,chalarrayY,'g-*')
                        
                         plt.grid(True)
                         plt.xlabel('age [months]')
                         plt.ylabel('length [cm]')
                         plt.xlim([0,12])
                         plt.xticks(np.arange(0,13,1))
                                
                         plt.text(alarray[5,0], alarray[5,5],'50%',fontsize=10)
                         plt.text(alNarray[1,0], alNarray[1,1],'50%',fontsize=10)
                # Adjust distance between subplots
                         plt.subplots_adjust(wspace=0.4, hspace=0.4)
            

# Show & save graphs and Show legend 
                         fig1 = plt.gcf()
                         fig1.legend(labels=('WHO','local','individual'), loc='lower right')
                         #plt.show()
                         #plt.draw()
            
                         chart=FigureCanvasTkAgg(fig1 , frame)
                         chart.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH) 
                                
                         fig1.set_size_inches(16, 9)
                         fig1.savefig(os.path.join(path,'graph.pdf'), dpi=100)
                         fig1.savefig(os.path.join(path,'graph.png'), dpi=100)
                
            def funcsave():
                if(rbVar.get()=='female'):
                    savefile='curve' +str(etId.get()) + '.png'
                    fig1.savefig(os.path.join(path1,savefile), dpi=100)
                else:
                    savefile='curve' +str(etId.get()) + '.png'
                    fig1.savefig(os.path.join(path2,savefile), dpi=100)
                    
            Busave.config(command=funcsave) 
            def funcquit():
                    frame.destroy()
                    for widget in frame1.winfo_children():
                        widget.destroy()
            Buquit.config(command=funcquit)
            
       
                                        
        def funct1():
           
            for widget in frame.winfo_children():
                    widget.destroy()
            Busave= ttk.Button(frame,text='Save')
            Busave.pack()
            Buquit= ttk.Button(frame,text='Quit')
            Buquit.pack()
            find=0
            if((rbVar.get()=='')or(etId.get()=='')):
                    messagebox.showinfo(title='empty data',message='enter all data')
            else:
            
                if(rbVar.get()=='female'):
                    chdata = 'GirlDataSet.csv'
# Age, weight, height

                    charray = np.genfromtxt(os.path.join(path,chdata), delimiter=',', dtype = None, skip_header=1, encoding=None)
                    #print(charray)
#skip_header indique la ligne de debut du fichier a prendre en compte
    
    # ---
# ---
                    chawarrayX = []
                    chalarrayX = []
                    chawarrayY = []
                    chalarrayY = []
                     # sublist[0] : Age
# sublist[1] : Weight
# sublist[2] : Length
        #take the entered values to write them
                    for sublist in charray:
                        if(int(etId.get())==sublist[0]):
                            chawarrayX.append(sublist[1])
                            chawarrayY.append(sublist[3])
                            chalarrayX.append(sublist[1])
                            chalarrayY.append(sublist[4])
                            find=1
                    if(find==0):
                            messagebox.showinfo(title='not existing id',message='individual data are empty')
                            for widget in frame.winfo_children():
                                widget.destroy()
                            frame.destroy()
                    else:
    # read girls'  WHO charts
    # Read age vs weight WHO data
                        awdata = 'g_age_weight.csv'
                        awarray = np.loadtxt(os.path.join(path,awdata), delimiter=',', skiprows=1)
        # Read age vs length WHO data
                        aldata = 'g_age_length.csv'
                        alarray = np.loadtxt(os.path.join(path,aldata), delimiter=',', skiprows=1)
        # Read age vs weight nigeria data
                        awNdata = 'g_age_N_weight.csv'
                        awNarray = np.loadtxt(os.path.join(path,awNdata), delimiter=',', skiprows=1)
        # Read age vs lenght nigeria data
                        alNdata = 'g_age_N_lenght.csv'
                        alNarray = np.loadtxt(os.path.join(path,alNdata), delimiter=',', skiprows=1)
        
                         # Plots
                        plt.figure()
                        
                     # Age vs weight
                        plt.subplot(2,1,1)
                        plt.plot(\
                        awNarray[:,0],awNarray[:,1],'b-',\
                        chawarrayX,chawarrayY,'g-*')
            
                        plt.grid(True)
                        plt.title('Girl ID %s' %etId.get())
                        plt.xlabel('age [months]')
                        plt.ylabel('weight [kg]')
                        plt.xlim([0,12])
                        plt.xticks(np.arange(0,13,1))
        
                        plt.text(awNarray[1,0], awNarray[1,1],'50%',fontsize=10)
                        
                     # Age vs length
                        plt.subplot(2,1,2)
                        plt.plot(\
                        alNarray[:,0],alNarray[:,1],'b-',\
                        chalarrayX,chalarrayY,'g-*')
    
                        plt.grid(True)
                        plt.xlabel('age [months]')
                        plt.ylabel('length [cm]')
                        plt.xlim([0,12])
                        plt.xticks(np.arange(0,13,1))
        
                        plt.text(alNarray[1,0], alNarray[1,1],'50%',fontsize=10)
                        
                         # Adjust distance between subplots
                        plt.subplots_adjust(wspace=0.4, hspace=0.4)

# Show & save graphs and show legend
                        fig1 = plt.gcf()
                        fig1.legend(labels=('local','individual'), loc='lower right')
                        #plt.show()
                        #plt.draw()
            
                        chart=FigureCanvasTkAgg(fig1 , frame)
                        chart.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH) 
        
                        fig1.set_size_inches(16, 9)
                        fig1.savefig(os.path.join(path,'graph.pdf'), dpi=100)
                        fig1.savefig(os.path.join(path,'graph.png'), dpi=100)
                        
                if(rbVar.get()=='male'):
                     chdata = 'BoyDataSet.csv'
    # Age, weight, height

                     charray = np.genfromtxt(os.path.join(path,chdata), delimiter=',', dtype = None, skip_header=1, encoding=None)
                     
#skip_header indique la ligne de debut du fichier a prendre en compte
    
    # --- 

                     chawarrayX = []
                     chalarrayX = []
                     chawarrayY = []
                     chalarrayY = []
# sublist[0] : Age
# sublist[1] : Weight
# sublist[2] : Length
                     for sublist in charray:
                         if(int(etId.get())==sublist[0]):
                            chawarrayX.append(sublist[1])
                            chawarrayY.append(sublist[3]) 
                            chalarrayX.append(sublist[1])
                            chalarrayY.append(sublist[4])
                            find=1
                     if(find==0):
                            messagebox.showinfo(title='not existing id',message='individual data are empty')
                            for widget in frame.winfo_children():
                                widget.destroy()
                            frame.destroy()
                     else:
                     # read boys' (0-2) WHO charts
    # Read age vs weight WHO data
                         awdata = 'b_age_weight.csv'
                         awarray = np.loadtxt(os.path.join(path,awdata), delimiter=',', skiprows=1)
                            # Read age vs length WHO data
                         aldata = 'b_age_length.csv'
                         alarray = np.loadtxt(os.path.join(path,aldata), delimiter=',', skiprows=1)
                            #Read age vs weight nigerian data
                         awNdata = 'b_age_N_weight.csv'
                         awNarray = np.loadtxt(os.path.join(path,awNdata), delimiter=',', skiprows=1)
                            #Read age vs lenght nigerian data
                         alNdata = 'b_age_N_length.csv'
                         alNarray = np.loadtxt(os.path.join(path,alNdata), delimiter=',', skiprows=1)
               
                              # Plots
                         plt.figure()
            
         # Age vs weight
                         plt.subplot(2,1,1)
                         plt.plot(\
                         awNarray[:,0],awNarray[:,1],'b-',\
                         chawarrayX,chawarrayY,'g-*')
                                
                         plt.grid(True)
                         plt.title('Boy ID %s' %etId.get())
                         plt.xlabel('age [months]')
                         plt.ylabel('weight [kg]')
                         plt.xlim([0,12])
                         plt.xticks(np.arange(0,13,1))
                        
                         plt.text(awNarray[1,0], awNarray[1,1],'50%',fontsize=10)
            # Age vs length 
                         plt.subplot(2,1,2)
                         plt.plot(\
                         alNarray[:,0],alNarray[:,1],'b-',\
                         chalarrayX,chalarrayY,'g-*')
                        
                         plt.grid(True)
                         plt.xlabel('age [months]')
                         plt.ylabel('length [cm]')
                         plt.xlim([0,12])
                         plt.xticks(np.arange(0,13,1))
                                
                         plt.text(alNarray[1,0], alNarray[1,1],'50%',fontsize=10)
                # Adjust distance between subplots
                         plt.subplots_adjust(wspace=0.4, hspace=0.4)
                         
                     # Show & save graphs and Show legend 
                         fig1 = plt.gcf()
                         fig1.legend(labels=('local','individual'), loc='lower right')
                         #plt.show()
                         #plt.draw()
            
                         chart=FigureCanvasTkAgg(fig1 , frame)
                         chart.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH) 
                                
                         fig1.set_size_inches(16, 9)
                         fig1.savefig(os.path.join(path,'graph.pdf'), dpi=100)
                         fig1.savefig(os.path.join(path,'graph.png'), dpi=100)
            def funcsave():
                if(rbVar.get()=='female'):
                    savefile='curve' +str(etId.get()) + '.png'
                    fig1.savefig(os.path.join(path1,savefile), dpi=100)
                else:
                    savefile='curve' +str(etId.get()) + '.png'
                    fig1.savefig(os.path.join(path2,savefile), dpi=100)
                    
            Busave.config(command=funcsave) 
            def funcquit():
                    frame.destroy()
                    for widget in frame1.winfo_children():
                        widget.destroy()
            Buquit.config(command=funcquit)
        
     
               
        def funct2():
                
                for widget in frame.winfo_children():
                    widget.destroy()
                
                Busave= ttk.Button(frame,text='Save')
                Busave.pack()
                Buquit= ttk.Button(frame,text='Quit')
                Buquit.pack()
                find=0
                if((rbVar.get()=='')or(etId.get()=='')):
                    messagebox.showinfo(title='empty data',message='enter all data')
                else:
            
                    if(rbVar.get()=='female'):
                        chdata = 'GirlDataSet.csv'
# Age, weight, height

                        charray = np.genfromtxt(os.path.join(path,chdata), delimiter=',', dtype = None, skip_header=1, encoding=None)
                        
#skip_header indique la ligne de debut du fichier a prendre en compte
    
    # ---
# ---
                        chawarrayX = []
                        chalarrayX = []
                        chawarrayY = []
                        chalarrayY = []
                
                # sublist[0] : Age
# sublist[1] : Weight
# sublist[2] : Length
                         #take the entered values to write them
                        for sublist in charray:
                            if(int(etId.get())==sublist[0]):
                                chawarrayX.append(sublist[1])
                                chawarrayY.append(sublist[3])
                                chalarrayX.append(sublist[1])
                                chalarrayY.append(sublist[4])
                                find=1
                        if(find==0):
                            messagebox.showinfo(title='not existing id',message='individual data are empty')
                            for widget in frame.winfo_children():
                                widget.destroy()
                            frame.destroy()   
                        else:
    # read girls'  WHO charts
    # Read age vs weight WHO data
                            awdata = 'g_age_weight.csv'
                            awarray = np.loadtxt(os.path.join(path,awdata), delimiter=',', skiprows=1)
        # Read age vs length WHO data
                            aldata = 'g_age_length.csv'
                            alarray = np.loadtxt(os.path.join(path,aldata), delimiter=',', skiprows=1)
            # Read age vs weight nigeria data
                            awNdata = 'g_age_N_weight.csv'
                            awNarray = np.loadtxt(os.path.join(path,awNdata), delimiter=',', skiprows=1)
            # Read age vs lenght nigeria data
                            alNdata = 'g_age_N_lenght.csv'
                            alNarray = np.loadtxt(os.path.join(path,alNdata), delimiter=',', skiprows=1)
            
                             # Plots
                            plt.figure()
                            
                             # Age vs weight
                            plt.subplot(2,1,1)
                            plt.plot(\
                            awarray[:,0],awarray[:,5],'k-',\
                            chawarrayX,chawarrayY,'g-*')
                
                            plt.grid(True)
                            plt.title('Girl ID %s' %etId.get())
                            plt.xlabel('age [months]')
                            plt.ylabel('weight [kg]')
                            plt.xlim([0,12])
                            plt.xticks(np.arange(0,13,1))
        
                            plt.text(awarray[5,0], awarray[5,5],'50%',fontsize=10)
                       
                             # Age vs length
                            plt.subplot(2,1,2)
                            plt.plot(\
                            alarray[:,0],alarray[:,5],'k-',\
                            chalarrayX,chalarrayY,'g-*')
    
                            plt.grid(True)
                            plt.xlabel('age [months]')
                            plt.ylabel('length [cm]')
                            plt.xlim([0,12])
                            plt.xticks(np.arange(0,13,1))
            
                            plt.text(alarray[5,0], alarray[5,5],'50%',fontsize=10)
                            
                             # Adjust distance between subplots
                            plt.subplots_adjust(wspace=0.4, hspace=0.4)

# Show & save graphs and show legend
                            fig1 = plt.gcf()
                            fig1.legend(labels=('WHO','individual'), loc='lower right')
                            #plt.show()
                            #plt.draw()
                
                            chart=FigureCanvasTkAgg(fig1 , frame)
                            chart.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH) 
            
                            fig1.set_size_inches(16, 9)
                            fig1.savefig(os.path.join(path,'graph.pdf'), dpi=100)
                            fig1.savefig(os.path.join(path,'graph.png'), dpi=100)

                    if(rbVar.get()=='male'):
                         chdata = 'BoyDataSet.csv'
        # Age, weight, height
    
                         charray = np.genfromtxt(os.path.join(path,chdata), delimiter=',', dtype = None, skip_header=1,encoding=None)
                         
    #skip_header indique la ligne de debut du fichier a prendre en compte
        
        # --- 
    
                         chawarrayX = []
                         chalarrayX = []
                         chawarrayY = []
                         chalarrayY = []
# sublist[0] : Age
# sublist[1] : Weight
# sublist[2] : Length
                         for sublist in charray:
                             if(int(etId.get())==sublist[0]):
                                chawarrayX.append(sublist[1])
                                chawarrayY.append(sublist[3]) 
                                chalarrayX.append(sublist[1])
                                chalarrayY.append(sublist[4])
                                find=1
                         if(find==0):
                                
                             messagebox.showinfo(title='not existing id',message='individual data are empty')
                             for widget in frame.winfo_children():
                                    widget.destroy()
                             frame.destroy()      
                         else:
                          # read boys' (0-2) WHO charts
        # Read age vs weight WHO data
                             awdata = 'b_age_weight.csv'
                             awarray = np.loadtxt(os.path.join(path,awdata), delimiter=',', skiprows=1)
                                # Read age vs length WHO data
                             aldata = 'b_age_length.csv'
                             alarray = np.loadtxt(os.path.join(path,aldata), delimiter=',', skiprows=1)
                                #Read age vs weight nigerian data
                             awNdata = 'b_age_N_weight.csv'
                             awNarray = np.loadtxt(os.path.join(path,awNdata), delimiter=',', skiprows=1)
                                #Read age vs lenght nigerian data
                             alNdata = 'b_age_N_length.csv'
                             alNarray = np.loadtxt(os.path.join(path,alNdata), delimiter=',', skiprows=1)
                                     # Plots
                             plt.figure()
                              # Age vs weight
                             plt.subplot(2,1,1)
                             plt.plot(\
                             awarray[:,0],awarray[:,5],'k-',\
                             chawarrayX,chawarrayY,'g-*')
                                    
                             plt.grid(True)
                             plt.title('Boy ID %s' %etId.get())
                             plt.xlabel('age [months]')
                             plt.ylabel('weight [kg]')
                             plt.xlim([0,12])
                             plt.xticks(np.arange(0,13,1))
                        
                             plt.text(awarray[5,0], awarray[5,5],'50%',fontsize=10)
                # Age vs length 
                             plt.subplot(2,1,2)
                             plt.plot(\
                             alarray[:,0],alarray[:,5],'k-',\
                             chalarrayX,chalarrayY,'g-*')
                            
                             plt.grid(True)
                             plt.xlabel('age [months]')
                             plt.ylabel('length [cm]')
                             plt.xlim([0,12])
                             plt.xticks(np.arange(0,13,1))
                                
                             plt.text(alarray[5,0], alarray[5,5],'50%',fontsize=10)
                             
                    # Adjust distance between subplots
                             plt.subplots_adjust(wspace=0.4, hspace=0.4)
                
    
    # Show & save graphs and Show legend 
                             fig1 = plt.gcf()
                             fig1.legend(labels=('WHO','individual'), loc='lower right')
                             #plt.show()
                             #plt.draw()
                
                             chart=FigureCanvasTkAgg(fig1 , frame)
                             chart.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH) 
                                    
                             fig1.set_size_inches(16, 9)
                             fig1.savefig(os.path.join(path,'graph.pdf'), dpi=100)
                             fig1.savefig(os.path.join(path,'graph.png'), dpi=100)
                def funcsave():
                    if(rbVar.get()=='female'):
                        savefile='curve' +str(etId.get()) + '.png'
                        fig1.savefig(os.path.join(path1,savefile), dpi=100)
                    else:
                        savefile='curve' +str(etId.get()) + '.png'
                        fig1.savefig(os.path.join(path2,savefile), dpi=100)
                        
                Busave.config(command=funcsave) 
                def funcquit():
                    frame.destroy()
                    for widget in frame1.winfo_children():
                        widget.destroy()
                Buquit.config(command=funcquit)
        
                
                
        Buchart3.config(command=funct3)
        Buchart1.config(command=funct1)
        Buchart2.config(command=funct2)
    Buterm.config(command=funcok)
Buview.config(command=But)





root.mainloop()
