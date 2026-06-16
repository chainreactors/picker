---
title: Velvet Ant, dieci anni dentro il sistema di login: l’APT cinese che riscrive la fiducia nelle reti isolate
url: https://www.ictsecuritymagazine.com/notizie/velvet-ant-operation-highland-pam-openssh/
source: ICT Security Magazine
date: 2026-06-15
fetch_date: 2026-06-16T07:16:57.767907
---

# Velvet Ant, dieci anni dentro il sistema di login: l’APT cinese che riscrive la fiducia nelle reti isolate

[Salta al contenuto](#main)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/2016/01/logo-ict-security.jpg)](https://www.ictsecuritymagazine.com/)

* [Home](https://www.ictsecuritymagazine.com/)
* [Articoli](https://www.ictsecuritymagazine.com/argomenti/articoli/)
* RubricheEspandi
  + [Cyber Security](https://www.ictsecuritymagazine.com/argomenti/cyber-security/)
  + [Cyber Crime](https://www.ictsecuritymagazine.com/argomenti/cyber-crime/)
  + [Cyber Risk](https://www.ictsecuritymagazine.com/argomenti/cyber-risk/)
  + [Cyber Law](https://www.ictsecuritymagazine.com/argomenti/cyber-law/)
  + [Digital Forensic](https://www.ictsecuritymagazine.com/argomenti/digital-forensic/)
  + [Digital ID Security](https://www.ictsecuritymagazine.com/argomenti/digital-id-security/)
  + [Business Continuity](https://www.ictsecuritymagazine.com/argomenti/business-continuity/)
  + [Digital Transformation](https://www.ictsecuritymagazine.com/argomenti/digital-transformation/)
  + [Cyber Warfare](https://www.ictsecuritymagazine.com/argomenti/cyber-warfare/)
  + [Ethical Hacking](https://www.ictsecuritymagazine.com/argomenti/ethical-hacking/)
  + [GDPR e Privacy](https://www.ictsecuritymagazine.com/argomenti/gdpr-e-privacy/)
  + [IoT Security](https://www.ictsecuritymagazine.com/argomenti/iot-security/)
  + [Industrial Cyber Security](https://www.ictsecuritymagazine.com/argomenti/industrial-cyber-security/)
  + [Blockchain e Criptovalute](https://www.ictsecuritymagazine.com/argomenti/blockchain-e-criptovalute/)
  + [Intelligenza Artificiale](https://www.ictsecuritymagazine.com/argomenti/intelligenza-artificiale/)
  + [Geopolitica e Cyberspazio](https://www.ictsecuritymagazine.com/argomenti/geopolitica-cyberspazio/)
  + [Prospettive](https://www.ictsecuritymagazine.com/argomenti/prospettive/)
  + [Interviste](https://www.ictsecuritymagazine.com/argomenti/interviste/)
* [Notizie](https://www.ictsecuritymagazine.com/argomenti/notizie/)
* [Pubblicazioni](https://www.ictsecuritymagazine.com/pubblicazioni/)
* [Cybersecurity Video](https://www.ictsecuritymagazine.com/argomenti/cybersecurity-video/)
* [Eventi](https://eventi.ictsecuritymagazine.com/)
* [Newsletter](https://www.ictsecuritymagazine.com/newsletter/)

[Linkedin](https://www.linkedin.com/company/ict-security-magazine/) [YouTube](https://www.youtube.com/%40ictsecuritymagazine) [RSS](https://www.ictsecuritymagazine.com/feed/)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/2016/01/logo-ict-security.jpg)](https://www.ictsecuritymagazine.com/)

Attiva/disattiva menu

[![Forum ICT Security 2026](https://www.ictsecuritymagazine.com/wp-content/uploads/forum-ict-security-banner-header-2026.jpg)](https://eventi.ictsecuritymagazine.com/eventi/forum-ict-security-2026)

![Velvet Ant, dieci anni dentro il sistema di login l'APT cinese](https://www.ictsecuritymagazine.com/wp-content/uploads/Velvet-Ant-dieci-anni-dentro-il-sistema-di-login-lAPT-cinese.png)

# Velvet Ant, dieci anni dentro il sistema di login: l’APT cinese che riscrive la fiducia nelle reti isolate

A cura di:[Redazione](#molongui-disabled-link)  Ore 15 Giugno 202615 Giugno 2026

Per quasi un decennio il gruppo **Velvet Ant**, riconducibile alla Cina, è rimasto nascosto non sui server più sorvegliati, ma dentro il meccanismo che decide chi può accedere a quei server. La società di *incident response* Sygnia ha ricostruito, in una ricerca pubblicata l’11 giugno, l’operazione battezzata [Operation Highland](https://www.sygnia.co/blog/operation-highland-velvet-ant/): l’attore ha modificato i componenti di autenticazione di Linux, *PAM* e *OpenSSH*, per garantirsi una persistenza che i normali interventi di bonifica non riuscivano a raggiungere. Le tracce più antiche risalgono al 2016. Più che un singolo incidente, è la fotografia di una dottrina di spionaggio paziente che interessa direttamente chi gestisce reti segmentate, [infrastrutture critiche](https://www.ictsecuritymagazine.com/articoli/sicurezza-informatica/) e ambienti OT.

## Chi è Velvet Ant e cosa ha fatto

La rete colpita non aveva accesso diretto a Internet. Per arrivarci, il gruppo si è appoggiato a sistemi esposti come ponte, instradando i comandi attraverso un server web pubblico fino al segmento isolato. Una volta dentro, niente *malware* vistoso: l’attaccante ha sostituito i programmi di login considerati affidabili. Sui sistemi compromessi è stato rimpiazzato il modulo *pam\_unix.so*, in nove varianti distinte individuate dai ricercatori, ciascuna compilata in un ambiente di *build* separato; una famiglia consentiva soltanto l’accesso con una password segreta, l’altra combinava il *bypass* (tramite credenziale fissa *Pamauth@123456*) e la registrazione silenziosa di nomi utente e password reali a ogni accesso legittimo. Gli stessi programmi di *OpenSSH* sono stati alterati per annotare credenziali e ogni comando digitato, con un *flag* nascosto (*-d*) per disattivare la registrazione quando serviva, come [ricostruito da BleepingComputer](https://www.bleepingcomputer.com/news/security/chinese-hackers-hijack-auth-flow-spy-on-isolated-network-for-a-decade/). Il punto critico, sul piano difensivo, è che la compromissione del sistema di autenticazione svuota le contromisure abituali: reimpostare le password o terminare le sessioni serve a poco quando proprio il componente che verifica quelle credenziali lavora per l’attaccante. La presenza diventa indistinguibile dalla normale attività amministrativa, perché si annida in *pam\_unix.so*, *sshd* e *ssh*, file presenti praticamente su ogni host Linux.

## Non è la prima volta

Lo schema è coerente con la storia del gruppo. Ogni volta che i difensori scoprono un punto d’appoggio, Velvet Ant si sposta verso apparati meno monitorati. Nel 2024 Sygnia lo aveva osservato trasformare *appliance* F5 BIG-IP esposte in server di comando interni; più avanti nello stesso anno il gruppo sfruttava una falla di Cisco NX-OS, [CVE-2024-20399](https://nvd.nist.gov/vuln/detail/CVE-2024-20399), per impiantare una *backdoor* sugli switch (un bug che richiede privilegi di amministratore, quindi strumento di persistenza più che di intrusione iniziale, corretto da Cisco a luglio 2024 e segnalato come sfruttato dalla CISA il giorno successivo). [Operation Highland](https://thehackernews.com/2026/06/china-linked-hackers-backdoored-linux.html) è la stessa idea, un livello più in profondità: bilanciatori, switch e ora il software di login sono affidabili per default e quasi mai verificati, ed è esattamente per questo che un attaccante paziente vi si nasconde.

## Perché conta sul piano geopolitico

La vicenda conferma una tendenza che le agenzie occidentali segnalano da tempo: gli attori *nation-state*, e in particolare quelli di matrice cinese, privilegiano il pre-posizionamento di lungo periodo nelle reti strategiche rispetto all’attacco rumoroso, [come rilevato](https://www.scworld.com/brief/china-nexus-group-hid-in-linux-login-system-for-nearly-a-decade) da più analisti. La furtività non nasce tanto dall’uso di strumenti integri così come sono (tecnica *living-off-the-land*, presente semmai nella fase d’ingresso con utility pubbliche come *GS-Netcat* e un proxy *SOCKS5* in Perl), quanto dalla manomissione dei binari di autenticazione: l’attaccante si maschera da componente fidato, riscrivendo i programmi di sistema con versioni trojanizzate. È una sovversione della catena di fiducia, difficile da attribuire e rilevare, coerente con obiettivi di *intelligence* più che di estorsione. Per i settori a maggior valore (difesa, telecomunicazioni, energia, pubblica amministrazione) la lezione operativa è netta: la segmentazione non basta, perché la catena di fiducia (*supply chain* del software di sistema) include ora anche i [sistemi di autenticazione](https://www.ictsecuritymagazine.com/articoli/identity-access-management/). La risposta, avvertono i ricercatori, non è il *patch*, ma la verifica di integrità. Operation H...