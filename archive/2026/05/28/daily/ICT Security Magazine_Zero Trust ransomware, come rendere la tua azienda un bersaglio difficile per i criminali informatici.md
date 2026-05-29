---
title: Zero Trust ransomware, come rendere la tua azienda un bersaglio difficile per i criminali informatici
url: https://www.ictsecuritymagazine.com/articoli/zero-trust-ransomware-infosec/
source: ICT Security Magazine
date: 2026-05-28
fetch_date: 2026-05-29T06:06:35.935040
---

# Zero Trust ransomware, come rendere la tua azienda un bersaglio difficile per i criminali informatici

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

![Cristiano Guerrieri (ThreatLocker), Zero Trust ransomware alla Cyber Crime Conference 2026: default-deny, allowlisting e Zero Trust per fermare il ransomware](https://www.ictsecuritymagazine.com/wp-content/uploads/Cristiano-Guerrieri-ThreatLocker-Cyber-Crime-Conference-2026.jpg)

# Zero Trust ransomware, come rendere la tua azienda un bersaglio difficile per i criminali informatici

A cura di:[Redazione](#molongui-disabled-link)  Ore 28 Maggio 202625 Maggio 2026

*Intervento di Cristiano Guerrieri, Solutions Engineer di ThreatLocker, 1[4ª Cyber Crime Conference](https://eventi.ictsecuritymagazine.com/eventi/cyber-crime-conference-2026), Roma, 6 maggio 2026*

Il punto di partenza scelto da Cristiano Guerrieri per il suo intervento alla 14ª Cyber Crime Conference è un’immagine domestica: l’allarme antifurto.

> «Io metto l’allarme a casa, la casa a fianco non lo ha: è più semplice che l’attaccante vada a cercare di entrare nell’altra casa piuttosto che nella mia».

Da qui il filo conduttore di tutto il suo intervento, dedicato a un cambio di paradigma nella postura di sicurezza aziendale: smettere di rincorrere ciò che è “cattivo” e iniziare a permettere soltanto ciò che è esplicitamente necessario.

## Il cybercrime come industria matura

Guerrieri ha esordito ricordando che lo stereotipo del *nerd* solitario nel sottoscala è ormai una rappresentazione del passato. «Adesso sono aziende che fanno questo di mestiere». Il *Ransomware-as-a-Service* è la dimostrazione più nitida di questa industrializzazione: chi vuole condurre un’estorsione si limita a comprare il *ransomware* da chi lo sviluppa, esattamente come si acquista un software gestionale.

![Cristiano Guerrieri (ThreatLocker), Zero Trust ransomware alla Cyber Crime Conference 2026: default-deny, allowlisting e Zero Trust per fermare il ransomware.](https://www.ictsecuritymagazine.com/wp-content/uploads/chrome_HvIRQkvBQP-700x394.png)

*Cristiano Guerrieri, Solutions Engineer di ThreatLocker, alla Cyber Crime Conference 2026*

Da questa premessa discendono tre coordinate che guidano la selezione delle vittime: la **scalabilità** (quanti dati posso esfiltrare, in quanto tempo), la **velocità** di accesso all’ambiente, e soprattutto il **return on investment**. Gli attaccanti non scelgono a caso: scelgono in base ai dati che si possono ottenere e alla facilità con cui si può colpire. Il costo annuale globale del *cybercrime* continua a salire in modo netto, anche per effetto della situazione geopolitica, e il guadagno non deriva soltanto dal furto dei dati: anche il *downtime* infrastrutturale, ha ricordato Guerrieri, è ormai parte del repertorio (la guerra, oggi, «è anche questo, non soltanto bombe»).

## Perché proprio io? I criteri di selezione del bersaglio

Gli ambienti senza controlli adeguati, ridotti al solo *antivirus* gratuito, sono per gli attaccanti i più appetibili. I criteri di selezione individuati da Guerrieri sono quattro:

* **Esposizione su internet.** Servizi pubblicati per errore, *firewall* mal configurati, porte aperte. Su strumenti come Shodan è possibile filtrare per area geografica e ottenere mappe puntuali di ciò che è raggiungibile da fuori. «Se io espongo su internet dei miei servizi, magari anche a mia insaputa, per l’attaccante sono un bersaglio semplice».
* **Disponibilità di credenziali.** Account rubati e rivenduti sul *dark web*: «non li rubano per metterli in tasca, li rivendono». Se per la mia azienda esistono credenziali già in vendita, il lavoro dell’attaccante è enormemente facilitato.
* **Configurazioni di default.** «Compro il migliore dei *firewall*, lo accendo, password “administrator”, administrator. E questo succede».
* **Controlli deboli sugli *endpoint***. È sugli *endpoint* che vivono i dati, ed è lì che spesso le difese sono più sottili.

A tutto questo Guerrieri ha aggiunto la falsa rassicurazione del “sono troppo piccolo per interessare”. Le piccole imprese sono in realtà tra i bersagli preferiti: controlli deboli, strumenti inadeguati, gestione della sicurezza affidata a non specialisti. E il calcolo dell’attaccante è banale: «se riesco a colpire 100.000 aziende che hanno pochissimi dati, e da ognuna ottengo un riscatto da un euro, ho fatto 100.000 euro».

#### Le porte di accesso più comuni

Sul vettore iniziale, l’analisi di Guerrieri è netta: nella maggioranza dei casi sono gli utenti stessi a “consegnare le chiavi”. Le modalità ricorrenti includono il classico furto di credenziali tramite *phishing*, l’inganno via *social engineering* (l’attaccante che si finge “Microsoft Support” e induce l’utente a installare TeamViewer per “ricevere aiuto”), e l’abuso di strumenti perfettamente legittimi: TeamViewer è “buono” quando lo usa l’amministratore, “malevolo” quando lo usa l’attaccante. **È il contesto a fare la differenza, non lo strumento.**

Lo stesso vale per IP scanner, *vulnerability assessment* e PowerShell, definito da Guerrieri «l’applicativo più pericoloso del mondo, e ce l’abbiamo tutti»: secondo i dati citati, **il 53% degli attacchi ai sistemi SMB utilizza PowerShell almeno una volta**. Da qui il punto chiave: *«bloccare ciò che accade dopo l’accesso iniziale è cruciale»*. L’accesso iniziale è spesso inevitabile; ciò che fa la differenza è impedire all’att...