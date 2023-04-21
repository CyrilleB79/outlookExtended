# Outlook extended #

* Auteurs : Cyrille Bougot, Ralf Kefferpuetz
* Compatibilité NVDA: 2019.3 et ultérieure
* Télécharger [version stable][1]
* Télécharger [version de développement][2]

This addon improves the use of Microsoft Outlook by vocalizing some native
commands, adding extra commands and adds extra features.

## Commandes

* Alt+1 à Alt+9, Alt+0, Alt+), alt+=: Annonce le champ d’en-tête 1 à 12 dans
  un message, un élément de calendrier ou une tâche. Une double pression
  déplace le focus dans ce champ si possible. Une triple pression copie son
  contenu dans le presse-papiers.
* NVDA+Maj+I (disposition ordinateur de bureau) / NVDA+control+maj+I
  (disposition ordinateur portable): Annonce la barre d'information dans un
  message, un élément de calendrier ou une fenêtre de tâche. Une double
  pression y déplace le focus. Une triple pression copie son contenu dans le
  presse-papiers.
* NVDA+maj+A (disposition ordinateur de bureau) / NVDA+control+maj+A
  (disposition ordinateur portable): Annonce le nombre et le nom des pièces
  jointes dans une fenêtre de message. Une double pression y déplace le
  focus.
* NVDA+maj+M (disposition ordinateur de bureau) / NVDA+control+maj+M
  (disposition ordinateur portable): Déplace le focus dans le corps du
  message.
* NVDA+shift+N (desktop layout) / NVDA+control+shift+N (laptop layout):
  Reports the notification in a message window. If pressed twice, moves the
  focus to it. If pressed three times, copies its content to the clipboard.
* Control+Q: Dans la liste des messages, marque le message ou le groupe de
  messages sélectionné comme lu.
* Control+U: Dans la liste des messages, marque le message ou le groupe de
  messages sélectionné comme non lu.

## Additional improvements

* When the recipient you have entered in the To, Cc or Bcc fields sends
  automatic out of office replies or is not present anymore on the Exchange
  server, Outlook report it in the notification area. In this notification
  area, you also have buttons to remove the address of these recipients.
  This add-on will inform you with a ding when this notification area
  appear, disappear or be updated. You can then press NVDA+shif+N /
  NVDA+control+shift+N once to have it read and twice to jump to this
  area. Then move with arrows on the recipient buttons and press a button to
  remove the corresponding recipient.
* In the address book's result list, you can use horizontal table navigation
  commands to read the content of each column.
  
## Notes

Tous les gestes de commandes peuvent être modifiés dans la boîte de dialogue
Gestes de commandes de NVDA. Vous pourriez en particulier vouloir les
modifier dans les situations suivantes :

* Les raccourcis par défaut pour marquer un message comme lu ou non lu sont
  ceux de la version anglaise d’Outlook. S’ils sont différents de ceux de
  votre version locale d’Outlook, vous devrez les modifier en conséquence.
* Les geste de commande par défaut pour lire les en-têtes correspondent à
  Alt en combinaison avec les touches de la première ligne du clavier
  alpha-numérique. Vous pourriez avoir besoin de réattribuer les gestes de
  commandes pour lire les en-têtes 11 et 12 s’ils ne sont pas en concordance
  avec votre disposition de clavier locale.

## Journal des modifications

### Version 2.0

* Improve the user experience with notifications appearing when entering
  e-mail addresses which are not valid anymore or which send automatic out
  of office replies: a sound alerts when such notifications appear or are
  updated, a gesture allows to read it or to move to it, and navigation in
  this area with arrows is made more easy.

### Version 1.10

* Compatibility with NVDA 2023.1.
* Ajout de localisations.

### Version 1.9

* Compatibilité avec NVDA 2022.1.
* Abandon de la compatibilité pour les versions de NVDA inférieures à
  2019.3.
* La release est maintenant effectuée grâce à une action GitHub au lieu
  d'appVeyor.
* Correction de l'annonce lorsque l'utilisateur appuie trois fois sur les
  raccourcis alt+chiffre.
* Correction d'un problème empêchant la lecture des en-têtes des éléments de
  calendrier de certaines versions d'Outlook 365.
* Amélioration de l'environnement de test de l'extension : navigation dans
  la boîte de dialogue fake root.
* Ajout de localisations.

### Version 1.8

* Ajout de localisations.
* Garantit que toutes les variables du module applicatif Outlook d'origine
  sont toujours disponibles.

### Version 1.7

* Mise à jour de la compatibilité pour NVDA 2021.1.
* Ajout de localisations.

### Version 1.6

* Correction de divers problèmes lors de la lecture des en-têtes de messages
  dans Outlook 365.
* Correction d'une erreur dans le script d'annonce des pièces jointes
  lorsqu'un clavier braille est utilisé.
* Ajout d'un environnement de test unitaire.
* Ajout de localisations.

### Version 1.5

* La lecture de la barre d'informations fonctionne désormais avec NVDA
  2019.3.
* La navigation de tableau dans les résultats du carnet d'adresses
  fonctionne désormais avec NVDA 2019.3.

### Version 1.4

* Le script pour déplacer le focus aux en-têtes fonctionne à nouveau.
* Le script pour se déplacer aux pièces jointes fonctionne désormais lorsque
  plus de pièces jointes sont présentes.
* Ajout de localisations.

### Version 1.3

* Correction de la lecture des en-têtes de message pour la nouvelle version
  d'Office 365.
* Mises à jour pour prendre en charge les versions les plus récentes de NVDA
  (compatible Python 2 et 3).
* Ajout de localisations.
* Release effectuée maintenant avec appveyor.

### Version 1.2

* Correction de la lecture des en-têtes lorsqu'on transfère un message.
* Ajout de localisations.

### Version 1.1

* Ajout de localisations.

### Version 1.0

* Version initiale

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=outlookextended

[2]: https://www.nvaccess.org/addonStore/legacy?file=outlookextended-dev
