#S8MainBionique2024
Cette branche compile toutes les avancées côtés logicielle que le projet recquiert.
LES ANCIENS CODES DU PING 2023 EST A RETROUVER DANS LE LIEN DU README DANS LA BRANCHE MAIN

Au cours des années et des groupes ayant travaillé dessus, plusieurs modifications mais également complexification ont été constaté. 
Cette branche apour but de simplifier la compréhension pour les prochains groupes. 


Le code du PING 2023 utilisait une interface appelée BioSignal PLUX. Cela requiert la malette de la marque avec le logciel installé pour pouvoir l'uiliser. 
Le code est cependant très mal commenté et détaillé, ne permettant pas la compréhension facile. 

Le groupe S8 2024 s'est concentré sur la résolution de bug au niveau du code du MSP430 qui présentait des défauts empêchant la bonne communication avec les servomoteurs et le maintient de la tension, élement primordial pour maintenir une position (comme une main fermée).
Le code du MSP430 est transmit dans cette branche. IL EST FONCTIONNEL 

Le groupe S8 s'estégalement penché sur un code de test en Python permetant, avec une carte électronique fonctionnelle, de tester les servomoteurs sur chaque sortie.
CE CODE FONCTIONNE POUR LE TEST GENERAL MAIS PRESENTE DES ERREURS POUR LE TEST UNITAIRE.
CODE A AMELIORER EN FONCTION DU BANC DE TEST SOUHAITE


