#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 21:42:03 2021

@author: Marcelo Mazo

cm.mazo@hotmail.com

"""

# Bibliotécas necessárias
from telnetlib import Telnet
import PySimpleGUI as sg
import time

host = '192.168.1.10' # Coloque o IP do seu servidor UNM2000

select1 = (1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14, 15, 16, 17, 18)

select2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)

# Interface gráfica
layout = [
    [sg.Frame(layout=[
        [sg.Text('OLT:'), 
         sg.Text(' ' * 40),
         sg.Text('SLOT:'),
         sg.Text(' ' * 13),
         sg.Text('PON:')],
        [sg.Input(size=(25, 20), enable_events=True, key='-OLT-'),          
         sg.Text(' '),
         sg.Combo(select1, size=(10, 20), enable_events=True, key='-SLOT-'),
         sg.Text(' '),
         sg.Combo(select2, size=(10, 20), enable_events=True, key='-PON-')]         
        ],
        title='OLT Dados:',
             title_color='red',
             relief=sg.RELIEF_SUNKEN,
             tooltip='Use these to set flags')],
    
    [sg.Text('_' * 61)],
    [sg.Text(''),
     sg.Input(size=(4, 20), key='-VLAN-'),
     sg.Text('CVLAN ID'),
     sg.Text(' '),
     sg.Radio('Cadastrar CVLAN', 'CADVLAN', default=True, key='-CAD-'),
     sg.Text(' '),
     sg.Radio('Alterar CVLAN', 'CADVLAN', default=False, key='-ALT-') 
    ],    
    [sg.Text('_' * 61)],
    
    [sg.Frame(layout=[
        [sg.Slider((1, 128), orientation='h', size=(22, 20),  enable_events=True, key='-N1-')]
        ],
        title='Primeira ONU:',
             title_color='red',
             relief=sg.RELIEF_SUNKEN,
             tooltip='Use these to set flags'),
     sg.Frame(layout=[
        [sg.Slider((1, 128), orientation='h', size=(22, 20),  enable_events=True, key='-ONU-')]
        ],
        title='Ultima ONU:',
             title_color='red',
             relief=sg.RELIEF_SUNKEN,
             tooltip='Use these to set flags')
    ],
    
    [sg.Frame(layout=[
        [sg.ProgressBar(1, orientation='h', size=(42, 20), key='-PROGRESSO-')]
        ],
        title='Status do Processo:',
             title_color='red',
             relief=sg.RELIEF_SUNKEN,
             tooltip='Use these to set flags')],
    
    [sg.Frame(layout=[
        [sg.Text('User:'), 
         sg.Text(' ' * 42),
         sg.Text('Senha:')],
        [sg.Input(size=(28, 20), key='-USER-'), 
         sg.Text(' '),
         sg.Input(size=(27, 20), key='-PASS-', password_char='*')]
        ],
        title='Acesso UNM2000:',
             title_color='red',
             relief=sg.RELIEF_SUNKEN,
             tooltip='Use these to set flags')],
    
    [sg.Button('Cancelar'), sg.Button('Executar')]
]

janela = sg.Window("CADASTRAR CVLAN ONU", layout, finalize=True)

while True:

    eventos, valores = janela.read()

    if (eventos == sg.WINDOW_CLOSED) or (eventos == "Cancelar"):
        break
    
    if eventos == "Executar":
        
        progress_bar = janela.FindElement('-PROGRESSO-')
        n1 = int(valores['-N1-'])
        onu = int(valores['-ONU-'])
        
        if valores['-OLT-'] == '':
           layout1 = [
               [sg.Text('Digite um IP válido para a OLT!')],
               [sg.Text(' Ex: 192.168.0.1!')]
           ]
           
           alerta1 = sg.Window("ERRO IP INVÁLIDO!", layout1)
           
           while True:
               
               evento1, valor1 = alerta1.read()

               if (evento1 == sg.WINDOW_CLOSED):
                   oltIP = 0
                   break
               
        elif valores['-SLOT-'] == '':
           layout2 = [
               [sg.Text(' ' * 6), sg.Text('Não foi Selecionado nenhum SLOT!', size =(34,0))],
               [sg.Text(' ' * 10), sg.Text('Selecione o SLOT Desejado!')]
           ]
           
           alerta2 = sg.Window("ERRO SLOT NÃO SELECIONADO!", layout2)
           
           
           while True:
               
               evento2, valor2 = alerta2.read()

               if (evento2 == sg.WINDOW_CLOSED):
                   slot = 0
                   break
               
        elif valores['-PON-'] == '':
           layout3 = [
               [sg.Text(' ' * 6), sg.Text('Não foi Selecionada nenhuma PON!', size =(34,0))],
               [sg.Text(' ' * 10), sg.Text(' Selecione a PON Desejada!')]
           ]
           
           alerta3 = sg.Window("ERRO PON NÃO SELECIONADA!", layout3)
           
           
           while True:
               
               evento3, valor3 = alerta3.read()

               if (evento3 == sg.WINDOW_CLOSED):
                   pon = 0
                   break
         
        elif valores['-USER-'] == '':
           layout6 = [
               [sg.Text(' ' * 8), sg.Text('Usuário Inválido!')],
               [sg.Text('Digite seu Usuário do UNM2000!')]
           ]
           
           alerta6 = sg.Window("ERRO USER ID!", layout6)
           
           
           while True:
               
               evento6, valor6 = alerta6.read()

               if (evento6 == sg.WINDOW_CLOSED): 
                   userTL1 = 0
                   break
        
        elif valores['-PASS-'] == '':
           layout7 = [
               [sg.Text(' ' * 8), sg.Text('Senha Inválida!')],
               [sg.Text('Digite um Valor para a Senha!')]
           ]
           
           alerta7 = sg.Window("ERRO PASS ID!", layout7)
           
           
           while True:
               
               evento7, valor7 = alerta7.read()

               if (evento7 == sg.WINDOW_CLOSED): 
                   passTL1 = 0
                   break
               
        else :
            
            oltIP = valores['-OLT-']
            
            slot = valores['-SLOT-']
            pon = valores['-PON-']
            vlan = valores['-VLAN-']
            userTL1 = valores['-USER-']
            passTL1 = valores['-PASS-']
            
            if (valores['-CAD-'] == True) :
                   login = 'LOGIN:::CTAG::UN='+userTL1+',PWD='+passTL1+';'
                   terminal = Telnet(host, 3337)           
                   time.sleep(3)
                   terminal.write(login.encode('ascii') + b"\n")
                   time.sleep(2)
                       
                   while int(n1) <= int(onu) :
                       
                       cvlanID = 'CFG-LANPORTVLAN::OLTID='+oltIP+',PONID=NA-NA-'+str(slot)+'-'+str(pon)+',ONUIDTYPE=ONU_NUMBER,ONUID='+str(n1)+',ONUPORT=NA-NA-NA-1:CTAG::CVLAN='+vlan+',CCOS=3;'
                       terminal.write(cvlanID.encode('ascii') + b"\n")
                       time.sleep(1)
                       reset = 'RESET-ONU::OLTID='+oltIP+',PONID=NA-NA-'+str(slot)+'-'+str(pon)+',ONUIDTYPE=ONU_NUMBER,ONUID='+str(n1)+':CTAG::;'
                       n1 += 1
                       progress_bar.UpdateBar(n1, onu)
                       
                   logout = 'LOGOUT:::CTAG::;'
                   terminal.write(logout.encode('ascii') + b"\n")
                
            if (valores['-ALT-'] == True) :
                   login = 'LOGIN:::CTAG::UN='+userTL1+',PWD='+passTL1+';'
                   terminal = Telnet(host, 3337)           
                   time.sleep(3)
                   terminal.write(login.encode('ascii') + b"\n")
                   time.sleep(2)
                       
                   while int(n1) <= int(onu) :
                       
                       delete = 'DEL-LANPORTVLAN::OLTID='+oltIP+',PONID=NA-NA-'+str(slot)+'-'+str(pon)+',ONUIDTYPE=ONU_NUMBER,ONUID='+str(n1)+',PORTID=NA-NA-NA-1:CTAG::;'
                       terminal.write(delete.encode('ascii') + b"\n")
                       time.sleep(1)
                       cvlanID = 'CFG-LANPORTVLAN::OLTID='+oltIP+',PONID=NA-NA-'+str(slot)+'-'+str(pon)+',ONUIDTYPE=ONU_NUMBER,ONUID='+str(n1)+',ONUPORT=NA-NA-NA-1:CTAG::CVLAN='+vlan+',CCOS=3;'
                       terminal.write(cvlanID.encode('ascii') + b"\n")
                       time.sleep(1)
                       reset = 'RESET-ONU::OLTID='+oltIP+',PONID=NA-NA-'+str(slot)+'-'+str(pon)+',ONUIDTYPE=ONU_NUMBER,ONUID='+str(n1)+':CTAG::;'
                       terminal.write(reset.encode('ascii') + b"\n")
                       n1 += 1
                       progress_bar.UpdateBar(n1, onu)
                       
                   logout = 'LOGOUT:::CTAG::;'
                   terminal.write(logout.encode('ascii') + b"\n")
               
            layout8 = [
                   [sg.Text('Operação Finalizada!')],
                   [sg.Text('')]
            ]
               
            alerta8 = sg.Window("ALERTA!", layout8)
               
            while True:
                  evento8, valor8 = alerta8.read()
    
                  if (evento8 == sg.WINDOW_CLOSED): 
                        break

janela.close()
