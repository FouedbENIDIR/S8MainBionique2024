#BANC DE TEST REALISER PAR FOUED BENIDIR DURANT LE PROJET S8 2024 SOUS LA TUTELLE DE DAVID CAVARD
#SI UN PROBLEME PERSISTE OU UNE QUESTION CONTACTEZ MOI: foued.benidir@groupe-esigelec.org 



import serial
import time
import PySimpleGUI as sg

#L'objectif de ce banc de test est de vérifier que tout les servosmoteurs 
#présent sur la carte sont oppérationels et peuvent atteindre chacune des 16 positions
#Pour ce faire nous allons concevoir une interphace graphique simple :
#Nous pourrons choisir de tester individuellement un servomoteur pre -sélectionné et de l'asservivr à une des 16 positions via un curseur
#Nous pourrons également lancer un test automatique sur chaque servomoteur allant aux 16 positions 


PortCom = serial.Serial("COM3", 9600, timeout=1)  # Remplacez "COM3" par le port correct en fonction du branchement 

def CheckKey(test):
    summ = 0
    for i in range(8):
        summ = summ + (test >> i) & 0x01
    return summ & 0x01

# Convertir une position (0-15) en un angle (0-180)
def position_to_angle(position):
    return int(position * 180 / 15)

# --Interface graphique----#

layout_main = [
    [sg.Text('Sélectionnez le type de banc de test souhaité : ')],
    [sg.Button('Test unitaire')],
    [sg.Button('Test Général')],
    [sg.Button('Quitter')]
]

# Layout pour Test Unitaire
layout_test_unitaire = [
    [sg.Text('Test Unitaire')],
    [sg.Text('Sélectionnez le servomoteur à tester :')],
    [sg.Button(f'Servo {i+1}', key=f'-SERVO-{i+1}-') for i in range(6)],
    [sg.Slider(range=(0, 15), orientation='h', size=(15, 20), default_value=0, key='Slider')],
    [sg.Button('Envoyer')],
    [sg.Button('Retour')]
]

# Layout pour Test Général
layout_test_general = [
    [sg.Text('Test Général')],
    [sg.Button('Démarrer le test')],
    [sg.Button('Retour')]
]

# Fenêtre principale
window_main = sg.Window('Banc de test', layout_main)

# Boucle principale
while True:
    event, values = window_main.read()

    if event == sg.WIN_CLOSED or event == 'Quitter':
        break

    elif event == 'Test unitaire':
        window_main.hide()  # On cache la fenêtre principale et on affiche la suivante
        window_unitaire = sg.Window('Test Unitaire', layout_test_unitaire)
        while True:
            event_unitaire, values_unitaire = window_unitaire.read()
            if event_unitaire == sg.WIN_CLOSED or event_unitaire == 'Retour':  # Si on clique sur retour ou sur close on revient à la page principale
                window_unitaire.close()
                window_main.un_hide()
                break
            elif event_unitaire.startswith('-SERVO-'):  # Sélection du servomoteur
                servo_id = int(event_unitaire.split('-')[2]) - 1
                servo_position = int(values_unitaire['Slider'])
                b = (servo_position << 1) | (servo_id << 5)
                b = b | CheckKey(b)

                try:
                    PortCom.write(b.to_bytes(1, byteorder='big'))
                    time.sleep(0.05)  # Ajout d'un délai pour permettre au MSP430 de répondre
                    response = PortCom.read()
                    if response:
                        print(f'Sent: {b.to_bytes(1, byteorder="big").hex()}')
                        print(f'Received: {response.hex()}')
                    else:
                        print('No response received')
                except serial.SerialException as e:
                    print(f'Error: {e}')
            elif event_unitaire == 'Envoyer':  # Si on clique sur le bouton Envoyer
                servo_position = int(values_unitaire['Slider'])
                hexservo_position = hex(servo_position)
                print(f'Servo position: {servo_position}')
              
                b_servo = 10
                b = b_servo  # Garder b_servo comme entier
                b_shifted = servo_position << 1  # Exécuter l'opération de décalage binaire sur l'entier
                b_with_key = b_shifted | CheckKey(b_shifted)  # Combiner avec le résultat de CheckKey
                final_b = b_with_key | servo_position  # Combiner avec la valeur initiale du servo_position

                try:
                    PortCom.write(final_b.to_bytes(1, byteorder='big'))
                    time.sleep(0.05)  # Ajout d'un délai pour permettre au MSP430 de répondre
                    response = PortCom.read()
                    if response:
                        print(f'Sent: {final_b.to_bytes(1, byteorder="big").hex()}')
                        print(f'Received: {response.hex()}')
                    else:
                        print('No response received')
                except serial.SerialException as e:
                    print(f'Error: {e}')

    elif event == 'Test Général':
        window_main.hide()
        window_general = sg.Window('Test Général', layout_test_general)
        while True:
            event_general, values_general = window_general.read()
            if event_general == sg.WIN_CLOSED or event_general == 'Retour':
                window_general.close()
                window_main.un_hide()
                break
            elif event_general == 'Démarrer le test':
                # Gérer le test général ici
                Time = 0.1
                for j in range(6):
                    for i in range(16):
                        # angle = position_to_angle(i)
                        b = i << 1 | j << 5
                        b = b | CheckKey(b)
                        try:
                            PortCom.write(b.to_bytes(1, byteorder='big'))
                            time.sleep(Time)
                            response = PortCom.read()
                            if response:
                                print(response)
                            else:
                                print('No response received')
                        except serial.SerialException as e:
                            print(f'Error: {e}')
                    for i in range(16):
                        angle = position_to_angle(15 - i)
                        b = (15 - i) << 1 | j << 5
                        b = b | CheckKey(b)
                        try:
                            PortCom.write(b.to_bytes(1, byteorder='big'))
                            time.sleep(Time)
                            response = PortCom.read()
                            if response:
                                print(response)
                            else:
                                print('No response received')
                        except serial.SerialException as e:
                            print(f'Error: {e}')
window_main.close()
