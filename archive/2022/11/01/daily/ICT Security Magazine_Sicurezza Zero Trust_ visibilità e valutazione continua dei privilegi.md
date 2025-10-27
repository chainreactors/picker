---
title: Sicurezza Zero Trust: visibilità e valutazione continua dei privilegi
url: https://www.ictsecuritymagazine.com/articoli/sicurezza-zero-trust-visibilita-e-valutazione-continua-dei-privilegi/
source: ICT Security Magazine
date: 2022-11-01
fetch_date: 2025-10-03T21:27:48.301069
---

# Sicurezza Zero Trust: visibilità e valutazione continua dei privilegi

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
* [Eventi](https://www.ictsecuritymagazine.com/eventi/)
* [Newsletter](https://www.ictsecuritymagazine.com/newsletter/)

[Linkedin](https://www.linkedin.com/company/ict-security-magazine/) [YouTube](https://www.youtube.com/%40ictsecuritymagazine1403) [RSS](https://www.ictsecuritymagazine.com/feed/)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/2016/01/logo-ict-security.jpg)](https://www.ictsecuritymagazine.com/)

Attiva/disattiva menu

[![Forum ICT Security 2025](https://www.ictsecuritymagazine.com/wp-content/uploads/banner-header-2025.jpg)](https://www.ictsecuritymagazine.com/eventi/forumictsecurity2025)

![](https://www.ictsecuritymagazine.com/wp-content/uploads/zero-trust.jpg)

# Sicurezza Zero Trust: visibilità e valutazione continua dei privilegi

A cura di:[Massimiliano Galvagna](#molongui-disabled-link)  Ore 31 Ottobre 202231 Ottobre 2022

*Il punto di contatto iniziale durante un attacco informatico è raramente l’obiettivo effettivo. Gli aggressori spesso accedono alle reti da una postazione di lavoro o da una risorsa IoT meno sicura e lavorano da lì ottenendo l’accesso a host e account con privilegi più elevati.*

### Il concetto di Zero Trust

Di conseguenza, il concetto di Zero Trust è cresciuto in modo significativo negli ultimi due anni, poiché le applicazioni cloud e il lavoro a distanza hanno ridefinito il perimetro di sicurezza. Le risorse e i servizi aziendali moderni spesso aggirano i modelli di sicurezza fondati sul perimetro aziendale, che si basano su firewall di rete e reti private virtuali (VPN) e sono diventati obsoleti. Un’architettura Zero Trust fondamentalmente considera ostili tutte le entità di una rete e non consente l’accesso alle risorse finché l’account e l’host non sono stati autenticati individualmente e autorizzati a utilizzare quella specifica risorsa.

Zero Trust garantisce che anche se un host o un account è compromesso, ulteriori movimenti laterali vengano bloccati all’interno della rete.

### Le lacune degli approcci di solo accesso

Tuttavia, questo approccio Zero Trust, comunemente visto nelle soluzioni di Privileged Access Management e Identity Access Management, si basa ancora su decisioni di sicurezza single point-in-time che utilizzano un elenco predefinito di identità privilegiate. Questo approccio presenta diversi problemi, uno dei quali è l’implementazione.

Uno dei problemi riguarda i semplici errori di configurazione. Ciò è particolarmente comune negli ambienti cloud a causa delle competenze differenziate richieste per gestire la complessità delle risorse cloud, che cambiano continuamente, rispetto a quelle tradizionali on-premise.

Un altro problema è che, una volta concesso, l’accesso può essere facilmente manipolato dagli aggressori con metodi quali l’abuso di credenziali e l’escalation dei privilegi. Entrambi i metodi sono particolarmente difficili da rilevare per i professionisti della sicurezza. Raramente hanno visibilità sulle credenziali utilizzate in rete rispetto a quelle assegnate dagli identity provider (IdP).

### Visibilità e valutazione continua dei privilegi

Per colmare questo divario è necessario estendere il metodo di autenticazione e autorizzazione a monte, monitorando continuamente gli account e le identità utilizzate per accedere alla rete e al cloud. Ecco perché la visibilità e l’analisi sono state la componente principale dell’[Ecosistema Zero Trust di Forrester](https://www.forrester.com/blogs/the-definition-of-modern-zero-trust/#:~:text=Zero%20Trust%20Defined,users%20and%20their%20associated%20devices.).

Secondo Gartner, “i responsabili della sicurezza e del rischio devono adottare un approccio strategico in cui la sicurezza sia adattiva, ovunque e in ogni momento”. Gartner chiama questo approccio strategico “continuous adaptive risk and trust assessment”, o CARTA, e sostiene che “con un approccio strategico CARTA, dobbiamo progettare ambienti aziendali digitali in cui il rischio e la fiducia sono dinamici e devono essere valutati continuamente dopo la valutazione iniziale”.

Con il monitoraggio, è possibile osservare se i comportamenti si discostano dalle aspettative in modo rischioso e comunicarlo ai professionisti della sicurezza per determinare se l’accesso alle funzionalità debba essere adattato o rimosso del tutto. Il monitoraggio delle interazioni che si verificano effettivamente rivela ciò che accade in un ambiente specifico.

### L’utilizzo dell’Intelligenza Artificiale (AI) per ottenere un quadro Zero Trust

L’Intelligenza Artificiale viene utilizzata per individuare efficacemente e dare priorità agli attacchi nascosti in tempo reale all’interno dei servizi cloud come Microsoft Office 365, Azure AD, il cloud, il data center, l’IoT e le reti aziendali, prima che gli aggressori causino danni irreparabili all’organizzazione. Una piattaforma basata sull’Intelligenza Artificiale consente ai team di sicurezza di prevenire gli attacchi prima, nelle fasi iniziali della catena di attacchi, garantendo che le applicazioni essenziali per la continuità aziendale siano disponibili e accessibili all’intera forza lavoro distribuita su più sedi.

Come componente chiave di un quadro Zero Trust, una piattaforma basata sull’Intelligenza Artificiale contribuirà a fornire visibilità e analisi su tre principi guida:

1. Verificare esplicitamente. Autenticare e autorizzare sempre in base a tutti i dati disponibili, tra cui l’identità dell’utente, la posizione, la condizione del dispositivo, il servizio o il carico di lavoro, la classificazione dei dati e le anomalie.
2. Utilizzare l’accesso meno privilegiato possibile. Limitare l’accesso degli utenti con criteri adattivi basati sul rischio e sulla protezione dei dati per proteggere sia i dati sia la produttività.
3. Ipotizzare una violazione della sicurezza. Ridurre al minimo il raggio d’azione delle violazioni e prevenire i movimenti laterali segmentando l’accesso in base alla...