#S8MainBionique2024
--------------------------------A LIRE AVANT DE DEBUTER LE PROJET--------------------------------


Ce projet, initié il y a quelques années, a pour but de concevoir une main mécanique contrôlée électroniquement par les signaux électriques que le corps envoie au niveau d'un moignon issu d'un bras amputé.

Notre projet S8 consistait en premier lieu à identifier les éventuels problèmes de la carte électronique en effectuant d'abord les tests préliminaires du protocole de test du groupe précédent l'ayant conçue, puis de faire nous-mêmes nos propres tests et d'en déduire des résultats. En effet, l'un des problèmes correspond aux sorties qui ne pilotent pas tous les servomoteurs. En effet, seulement 2 sorties permettent de contrôler un servomoteur, contre 6 normalement. Nous devions donc identifier pourquoi cela se produit. Ces tests ont été menés manuellement avec un oscilloscope et des sondes afin de déterminer de potentiels courts-circuits et de voir si toutes les sorties avaient un signal PWM, mais également avec l'utilisation et la réalisation d'un banc de test codé en Python permettant d'explorer tous les angles possibles de chaque servomoteur, branchés sur l'une des sorties.

Après tests électroniques et informatiques, l'hypothèse de court-circuit a été écartée, et à la place l'hypothèse d'une mauvaise conception des plans de masse sur cette carte a été retenue. Effectivement, le groupe précédent a mis, dans son plan de masse, les masses d'électronique de puissance et d'électronique de logique dans le même plan, créant ainsi des interférences et pouvant expliquer que nous recevons une PWM mais pas d'information lisible par les servomoteurs.

"Cette carte doit donc être revue pour séparer les plans de masse, ce qui permettrait d'éviter les surchauffes et de régler les problèmes d'asservissement."


SUJET POSSIBLE POUR UN FUTUR GROUPE 
-(Re)Conception de la carte électronique avec contrainte de longueur et de largeur (doit rentrer dans un avant-bras).
  -Etude préliminaire des avancées électroniques déjà effectuées (document de synthèse sur cette branche).
  -Compréhension des problèmes rencontrés et résolution de ceux-ci
  -Conception sous Eagle/KiCAD d'une nouvelle carte + impression
