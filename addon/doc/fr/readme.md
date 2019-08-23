# Outlook extended #

* Auteurs: Cyrille Bougot, Ralf Kefferpuetz
* NVDA compatibility: 2018.3 to 2019.3
* Télécharger [version stable][1]
* Télécharger [version de développement][2]

Cette extension améliore l’utilisation de Microsoft Outlook par la
vocalisation de certaines commandes et l’ajout de commandes supplémentaires.

## Commandes

* Alt+1 à Alt+9, Alt+0, Alt+), alt+=: Annonce le champ d’en-tête 1 à 12 dans
  un message, un élément de calendrier ou une tâche. Une double pression
  déplace le focus dans ce champ si possible. Une tripe pression copie son
  contenu dans le presse-papiers.
* NVDA+Maj+I (disposition ordinateur de bureau) / NVDA+control+maj+I
  (disposition ordinateur portable): Annonce la barre d'information dans un
  message, un élément de calendrier ou une fenêtre de tâche. Une double
  pression y déplace le focus. Une tripe pression copie son contenu dans le
  presse-papiers.
* NVDA+maj+A (disposition ordinateur de bureau) / NVDA+control+maj+A
  (disposition ordinateur portable): Annonce le nombre et le nom des pièces
  jointes dans une fenêtre de message. Une double pression y déplace le
  focus.
* * NVDA+maj+M (disposition ordinateur de bureau) / NVDA+control+maj+M
  (disposition ordinateur portable): Déplace le focus dans le corps du
  message.
* Control+Alt+Gauche and Control+Alt+Droite: Dans la liste des résultats de
  recherche du carnet d’adresses, navigue entre les champs de la ligne
  sélectionnée.
* Control+Q: Dans la liste des messages, marque le message ou le groupe de
  messages sélectionné comme lu.
* Control+U: Dans la liste des messages, marque le message ou le groupe de
  messages sélectionné comme non lu.

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

### Version 1.3

* Fix message headers reading for newer Office 365 release.
* Updates to support newer versions of NVDA (Python 2 and 3 compatible)
* Added localizations.
* Releases performed now with appveyor

### Version 1.2

* Fix header reading when forwarding meeting.
* Added localizations.

### Version 1.1

* Added localizations.

### Version 1.0

* Version initiale

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=outlookextended

[2]: https://addons.nvda-project.org/files/get.php?file=outlookextended-dev
