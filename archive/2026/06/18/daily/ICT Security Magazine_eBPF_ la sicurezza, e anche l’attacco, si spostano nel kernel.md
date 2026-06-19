---
title: eBPF: la sicurezza, e anche l’attacco, si spostano nel kernel
url: https://www.ictsecuritymagazine.com/cyber-security/ebpf-sicurezza/
source: ICT Security Magazine
date: 2026-06-18
fetch_date: 2026-06-19T07:09:10.492588
---

# eBPF: la sicurezza, e anche l’attacco, si spostano nel kernel

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

![eBPF](https://www.ictsecuritymagazine.com/wp-content/uploads/eBPF-.png)

# eBPF: la sicurezza, e anche l’attacco, si spostano nel kernel

A cura di:[Redazione](#molongui-disabled-link)  Ore 18 Giugno 20269 Giugno 2026

eBPF è la tecnologia che ha reso il cuore di Linux programmabile senza doverlo riscrivere, e nel farlo ha spostato il baricentro della sicurezza dove finora era difficile arrivare: dentro il kernel. La sigla sta per *extended Berkeley Packet Filter*, e descrive la capacità di eseguire piccoli programmi in uno spazio protetto del sistema operativo, senza modificare il codice del kernel, senza caricare moduli e senza riavviare la macchina. Nato per filtrare pacchetti di rete, eBPF è diventato una macchina virtuale generalista che oggi serve per la rete, l’osservabilità e, sempre più, la difesa.

Il motivo per cui interessa chi si occupa di sicurezza è una questione di posizione. Un programma eBPF vede ogni *system call*, ogni esecuzione di processo, ogni accesso a un file e ogni pacchetto di rete prima che qualunque applicazione o container li elabori. È il punto di osservazione più vicino alla verità che un difensore possa avere, e per giunta a costo bassissimo. La stessa posizione, però, è preziosa anche per chi attacca, ed è questa ambivalenza a rendere eBPF uno dei temi più rilevanti, e meno raccontati, della sicurezza dei sistemi.

## Cos’è eBPF, e perché il kernel è il posto giusto

Il problema storico di chi voleva sorvegliare un sistema dall’interno era il rischio: un errore in un modulo del kernel manda in crash l’intera macchina. eBPF aggira questo pericolo con un meccanismo che è la sua vera innovazione, il verificatore. Prima di lasciar girare un programma, il kernel ne dimostra la sicurezza: i cicli devono essere limitati, così da garantire che il programma termini in un numero prevedibile di istruzioni, e ogni accesso alla memoria viene validato. Un programma che non supera la verifica non viene eseguito. È questa garanzia a permettere di iniettare logica nel kernel senza trasformarlo in una mina.

Da qui nasce il vantaggio per la sicurezza, descritto bene dalla documentazione ufficiale del progetto su [cosa sia eBPF](https://ebpf.io/what-is-ebpf/). Raccogliere dati su processi, file e rete direttamente dal kernel significa avere una visibilità completa su tutto ciò che accade, senza la frammentazione e i punti ciechi degli strumenti che lavorano nello spazio utente. Significa anche un dato più difficile da manomettere: un *malware* che inganna o disattiva un agente di *logging* in spazio utente ha vita molto più dura contro un sensore che osserva dal kernel. E significa basso impatto, perché la raccolta avviene là dove gli eventi nascono, senza i costi di intermediazione che gravano sugli approcci tradizionali.

## Dalla visibilità all’enforcement: Falco e Tetragon

Su questa base è cresciuto un ecosistema di strumenti che ha cambiato il modo di fare sicurezza a runtime, soprattutto in ambienti containerizzati. Il capostipite è Falco, progetto della CNCF che ha aperto la strada al rilevamento comportamentale basato su eBPF: osserva gli eventi del kernel e segnala le anomalie sulla base di una vasta libreria di regole, lavorando soprattutto sul versante del rilevamento. È il sensore che dice al [centro operativo di sicurezza](https://www.ictsecuritymagazine.com/articoli/security-operations-center/) cosa sta accadendo nel momento in cui accade.

Il passo successivo è non limitarsi a vedere, ma intervenire. Tetragon, progetto CNCF nato all’interno di Cilium, porta la logica di sicurezza dentro i programmi eBPF stessi, e questo gli consente non solo di rilevare ma di applicare: può accorgersi di un comportamento ostile e terminare il processo che lo sta eseguendo prima che la *system call* si completi, con un impatto contenuto anche sotto grandi volumi di eventi. La differenza tra rilevare e bloccare nel kernel non è cosmetica: è la distanza tra sapere che qualcosa è andato storto e impedire che vada a termine. È anche la ragione per cui la difesa cloud-native si sta spostando dalla sola visibilità alla prevenzione in tempo reale, e per cui i pesanti agenti a *sidecar* di un tempo cedono il passo a sensori nativi del kernel ben più leggeri.

## eBPF è un’arma a doppio taglio

Qui arriva la parte che si tende a non raccontare. Lo stesso potere che rende eBPF prezioso per i difensori lo rende attraente per gli attaccanti, e la frontiera del kernel è terreno conteso. Una nuova generazione di *rootkit* sfrutta eBPF per agganciare le *system call* e intercettare gli eventi del kernel senza caricare un modulo tradizionale, l’artefatto che gli strumenti di difesa hanno sempre cercato. Con programmi eBPF malevoli un attaccante può nascondere processi, socket e file, sottrarre credenziali e manomettere la telemetria che dovrebbe tradirlo, restando invisibile a chi cerca solo moduli sospetti.

Non è teoria. Famiglie come BPFDoor e Symbiote, emerse dal 2021, sono state tra le prime a usare questa tecnologia per canali di comando e controllo furtivi a livello di kernel, e analisi più recenti come quella del *rootkit* LinkPro mostrano una sofisticazione crescente. Le ricerche dei ven...