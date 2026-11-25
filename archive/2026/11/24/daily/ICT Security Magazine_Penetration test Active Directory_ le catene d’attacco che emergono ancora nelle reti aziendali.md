---
title: Penetration test Active Directory: le catene d’attacco che emergono ancora nelle reti aziendali
url: https://www.ictsecuritymagazine.com/notizie/penetration-test-active-directory/
source: ICT Security Magazine
date: 2026-11-24
fetch_date: 2026-11-25T10:48:06.565415
---

# Penetration test Active Directory: le catene d’attacco che emergono ancora nelle reti aziendali

[Salta al contenuto](#main)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/logo-ict-security-trasparente-1.webp)](https://www.ictsecuritymagazine.com/)

Cerca nel magazine

* Argomenti

  [Cyber Security: tutti gli articoli 1.364 articoli](https://www.ictsecuritymagazine.com/argomenti/cyber-security/)

  Minacce e attacchi

  + [Vulnerabilità](https://www.ictsecuritymagazine.com/argomenti/vulnerabilita/)
  + [Cyber Crime](https://www.ictsecuritymagazine.com/argomenti/cyber-crime/)
  + [Cyber Warfare](https://www.ictsecuritymagazine.com/argomenti/cyber-warfare/)
  + [Ethical Hacking](https://www.ictsecuritymagazine.com/argomenti/ethical-hacking/)
  + [Digital Forensic](https://www.ictsecuritymagazine.com/argomenti/digital-forensic/)

  Rischio, norme e privacy

  + [GDPR e Privacy](https://www.ictsecuritymagazine.com/argomenti/gdpr-e-privacy/)
  + [Cyber Risk](https://www.ictsecuritymagazine.com/argomenti/cyber-risk/)
  + [Cyber Law](https://www.ictsecuritymagazine.com/argomenti/cyber-law/)
  + [Business Continuity](https://www.ictsecuritymagazine.com/argomenti/business-continuity/)

  Tecnologie

  + [Intelligenza Artificiale](https://www.ictsecuritymagazine.com/argomenti/intelligenza-artificiale/)
  + [IoT Security](https://www.ictsecuritymagazine.com/argomenti/iot-security/)
  + [Industrial Cyber Security](https://www.ictsecuritymagazine.com/argomenti/industrial-cyber-security/)
  + [Digital ID Security](https://www.ictsecuritymagazine.com/argomenti/digital-id-security/)
  + [Blockchain e Criptovalute](https://www.ictsecuritymagazine.com/argomenti/blockchain-e-criptovalute/)
  + [Digital Transformation](https://www.ictsecuritymagazine.com/argomenti/digital-transformation/)

  Scenari

  + [Geopolitica e Cyberspazio](https://www.ictsecuritymagazine.com/argomenti/geopolitica-cyberspazio/)
  + [Prospettive](https://www.ictsecuritymagazine.com/argomenti/prospettive/)

  Ultimi in **Cyber Security**

  [Tutti gli articoli di Cyber Security →](https://www.ictsecuritymagazine.com/argomenti/cyber-security/)
* [Notizie](https://www.ictsecuritymagazine.com/argomenti/notizie/)
* [Approfondimenti](https://www.ictsecuritymagazine.com/argomenti/articoli/)
* [Video](https://www.ictsecuritymagazine.com/argomenti/cybersecurity-video/)
* [Pubblicazioni](https://www.ictsecuritymagazine.com/pubblicazioni/)
* [Eventi ↗](https://eventi.ictsecuritymagazine.com/)

[Newsletter](/newsletter/)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/logo-ict-security-trasparente-1.webp)](https://www.ictsecuritymagazine.com/)

Cerca

Attiva/disattiva menu

[Vulnerabilità](https://www.ictsecuritymagazine.com/argomenti/vulnerabilita/) · [Cyber Security](https://www.ictsecuritymagazine.com/argomenti/cyber-security/)Contenuto sponsorizzato

# Penetration test Active Directory: le catene d’attacco che emergono ancora nelle reti aziendali

I red team di CISA mostrano che il controllo di Active Directory nasce da catene di configurazioni deboli: ecco come un penetration test Active Directory le fa emergere.

A cura di:[Francesco Pandiscia](https://www.ictsecuritymagazine.com/author/francesco-pandiscia/)  Ore Pubblicato il24 Novembre 20263 Novembre 2026  Condividi

![penetration test Active Directory: Catena di post-it, badge, certificato e cavo di rete sale dalla reception a un palazzo, in stampa risograph terracotta](https://www.ictsecuritymagazine.com/wp-content/uploads/penetration-test-active-directory-catena-risograph-terracotta.webp)

In sintesi

* Nell’agosto 2026 CISA ha pubblicato i risultati di due red team che hanno portato al controllo completo del dominio Active Directory.
* Il percorso ha combinato impostazioni predefinite permissive, un modello di certificato AD CS configurato male e credenziali in chiaro.
* Un penetration test Active Directory interno deve far emergere le catene, non solo i singoli difetti, e verificarne la correzione.

Active Directory è il punto in cui convergono identità, permessi e accessi di quasi tutte le reti aziendali basate su Windows. Per questo è anche il primo obiettivo di chi riesce a entrare: chi controlla il dominio controlla, di fatto, l’intera infrastruttura. La guida congiunta [Detecting and mitigating Active Directory compromises](https://cisa.gov/resources-tools/resources/detecting-and-mitigating-active-directory-compromises) è stata redatta dall’agenzia australiana ASD insieme a CISA, NSA e alle agenzie di Canada, Regno Unito e Nuova Zelanda. Censisce le 17 tecniche più comuni usate per [compromettere Active Directory](/articoli/badsuccessor-vulnerabilita/). Secondo la guida, la superficie d’attacco deriva soprattutto da impostazioni predefinite permissive, relazioni e permessi complessi e dal supporto a protocolli datati.

Il dato più significativo, però, non arriva da un elenco di tecniche ma da un esercizio reale. Il 25 agosto 2026 CISA ha pubblicato l’advisory [AA26-237A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-237a), intitolato “A Tale of Two SOCs”. Documenta due red team condotti in parallelo presso due organizzazioni di infrastrutture critiche: una nel settore dei servizi e delle strutture governative, l’altra in quello idrico e delle acque reflue. In entrambi i casi il risultato tecnico è stato lo stesso: compromissione completa del dominio, accesso ai sistemi di business sensibili e alle risorse cloud. Le tecniche usate sono note e documentate.

## Il caso AA26-237A: dal default al controllo del dominio

La sequenza descritta da CISA per la prima organizzazione è istruttiva proprio perché ordinaria. Il punto d’ingresso è stato un’applicazione web esposta su Internet che usava ancora credenziali predefinite. Da lì il red team ha inviato email di *phishing* da un indirizzo interno legittimo, superando di fatto i controlli che si basano sull’origine esterna dei messaggi.

Una volta ottenuto un utente di dominio senza privilegi, la scalata è avvenuta combinando due elementi. Il primo è il parametro *Machine Account Quota*, lasciato al valore predefinito di Windows, che consente a qualunque utente di dominio di aggiungere fino a dieci computer al dominio. Il secondo è un modello di certificato di Active Directory Certificate Services (AD CS) configurato in modo da permettere a chi lo richiede di indicare liberamente l’identità per cui viene emesso. È la classe di errore nota come ESC1.

Insieme hanno consentito di ottenere un certificato valido a nome di qualsiasi utente, account privilegiati compresi, e quindi di muoversi nella rete con quelle identità fino alla compromissione completa del dominio. A completare il quadro c’erano credenziali in chiaro lasciate su postazioni e condivisioni di rete.

La differenza tra le due organizzazioni è emersa solo sul piano della rilevazione. La prima non ha risposto agli alert generati dal red team, sommersi da migliaia di falsi positivi. La seconda ha isolato le postazioni compromesse entro 20 minuti. CISA attribuisce questo divario alle persone, ai processi e alle procedure che gestiscono gli strumenti, non agli strumenti stessi.

## Quando il “medio” diventa critico

Il punto centrale del caso è che nessuno degli anelli della catena, preso isolatamente, avrebbe allarmato un team IT. Un valore predefinito di Windows non è nemmeno una vulnerabilità. Un modello di certificato configurato in modo permissivo compare, nel migliore dei casi, come rilievo di configurazione. Una password in un file su una condivisione è un problema di igiene. Le credenziali predefinite di un’applicazione sono un errore banale. Eppure, messi in sequenza, questi elementi portano dal primo accesso al controllo totale.

È il limite strutturale di qualsiasi valutazione che consideri le vulnerabilità una alla volta. Uno scanner assegna un punteggio a ciascun rilievo, ma non sa che il rilievo numero 37 rende sfruttabile il numero 112. [Il *penetration test* esiste](/notizie/penetration-test-2/) esattamente per questo: non per trovare ...