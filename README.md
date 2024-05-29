#S8MainBionique2024
Ce répertoire est un recueil des travaux effectués durant le projet S8 2024.

Ce projet, initié il y a quelques années, a pour but de concevoir une main mécanique contrôlée électroniquement par les signaux électriques que le corps envoie au niveau d'un moignon issu d'un bras amputé.

Notre projet S8 consistait en premier lieu à identifier les éventuels problèmes de la carte électronique en effectuant d'abord les tests préliminaires du protocole de test du groupe précédent l'ayant conçue, puis de faire nous-mêmes nos propres tests et d'en déduire des résultats. En effet, l'un des problèmes correspond aux sorties qui ne pilotent pas tous les servomoteurs. En effet, seulement 2 sorties permettent de contrôler un servomoteur, contre 6 normalement. Nous devions donc identifier pourquoi cela se produit. Ces tests ont été menés manuellement avec un oscilloscope et des sondes afin de déterminer de potentiels courts-circuits et de voir si toutes les sorties avaient un signal PWM, mais également avec l'utilisation et la réalisation d'un banc de test codé en Python permettant d'explorer tous les angles possibles de chaque servomoteur, branchés sur l'une des sorties.

Après tests électroniques et informatiques, l'hypothèse de court-circuit a été écartée, et à la place l'hypothèse d'une mauvaise conception des plans de masse sur cette carte a été retenue. Effectivement, le groupe précédent a mis, dans son plan de masse, les masses d'électronique de puissance et d'électronique de logique dans le même plan, créant ainsi des interférences et pouvant expliquer que nous recevons une PWM mais pas d'information lisible par les servomoteurs.

"Cette carte doit donc être revue pour séparer les plans de masse, ce qui permettrait d'éviter les surchauffes et de régler les problèmes d'asservissement."

Par ailleurs, une problématique mécanique a également été posée. Jusqu'à présent, aucun prototype viable n'a été conçu, ne permettant pas au projet de progresser correctement. Notre second objectif a donc été de produire un modèle mécanique d'un doigt et d'une main, répondant aux enjeux d'un pliage naturel, d'un maintien d'une position avec force constante et de solidité dans le temps.

Plusieurs prototypes ont été conçus en répondant aux critères nécessaires énumérés dans le rapport mécanique, présent dans ce répertoire.
"L'utilisation d'une main à 3-4 doigts, avec 2 servomoteurs par doigt, ainsi que l'utilisation de roulements pour fluidifier le mouvement entre chaque phalange doit être étudiée autour d'un projet S8 complet, avec une partie de réflexion autour de nos conclusions, une partie de conception à partir de nos propositions de modèles et une partie de tests permettant de valider ou non le modèle proposé. Si les tests ne sont pas concluants, le groupe reviendra à la conception."
