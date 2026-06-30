---
title: Tokenizzazione: il dato più sicuro è quello che non si conserva
url: https://www.ictsecuritymagazine.com/cyber-security/tokenizzazione-protezione-dato/
source: ICT Security Magazine
date: 2026-06-29
fetch_date: 2026-06-30T06:10:09.706370
---

# Tokenizzazione: il dato più sicuro è quello che non si conserva

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

![Tokenizzazione](https://www.ictsecuritymagazine.com/wp-content/uploads/Tokenizzazione.png)

# Tokenizzazione: il dato più sicuro è quello che non si conserva

A cura di:[Redazione](#molongui-disabled-link)  Ore 29 Giugno 20269 Giugno 2026

Tokenizzazione è la tecnica che protegge un dato sensibile facendone sparire l’originale dai sistemi che lo usano. Al posto del numero di una carta di pagamento, di un codice fiscale, di un identificativo personale, si mette un surrogato senza alcun valore in sé, un *token*, e il dato vero viene custodito in un solo luogo protetto. Tutto il resto dell’organizzazione, le applicazioni, i database, i log, lavora soltanto con quei surrogati. La conseguenza è tanto semplice quanto potente: chi ruba i token non ruba nulla, perché un token, da solo, non significa niente e non riconduce a niente.

È un’idea che ribalta l’istinto difensivo comune. Di solito si cerca di proteggere meglio il dato sensibile là dove si trova: lo si cifra, si rafforzano gli accessi, si sorveglia chi lo tocca. La tokenizzazione segue la strada opposta, e parte da un principio più radicale: il dato più sicuro è quello che non si conserva affatto. Se la maggior parte dei sistemi non detiene mai il valore reale, ma solo un sostituto inutile, allora una loro compromissione smette di essere una fuga di dati e diventa la cattura di un mucchio di segnaposto privi di senso.

## Sostituire, non cifrare

La distinzione più importante, e più fraintesa, è quella con la [cifratura](https://netwrix.com/en/resources/blog/tokenization-vs-encryption/). Cifrare un dato significa trasformarlo con una chiave in un testo illeggibile, ma reversibile: chi possiede la chiave riottiene l’originale, e il testo cifrato resta legato matematicamente al dato di partenza. Ne discende una dipendenza scomoda: la sicurezza dell’intero sistema poggia sulla segretezza della chiave, e ogni componente che la detiene resta un punto critico. Se la chiave trapela, tutto ciò che ha cifrato torna in chiaro.

La tokenizzazione non trasforma il dato, lo rimpiazza. Il token, nella sua forma più solida, è un valore generato in modo casuale, senza alcun rapporto matematico con il dato che sostituisce. Non c’è una chiave che lo riporti all’originale, non c’è un algoritmo da invertire: l’unico modo per risalire dal token al dato vero è consultare l’archivio che ne conserva la corrispondenza. Non è il dato camuffato, è un’altra cosa che prende il suo posto. È questa la differenza che conta, perché elimina alla radice il problema della chiave da proteggere.

## Il caveau e ciò che ne esce

Il cuore del modello è proprio quell’archivio, il *token vault*, l’unico punto in cui vive la corrispondenza tra ogni token e il dato reale che rappresenta. Il vault è isolato e sorvegliato con accessi rigorosamente controllati, ed è il solo componente dell’architettura che maneggia davvero l’informazione sensibile. Quando un sistema ha bisogno del valore reale, e solo se ne ha davvero bisogno, lo richiede al vault presentando il token; tutto il resto del tempo, ovunque, circolano soltanto i surrogati.

Per non rompere le applicazioni che li trattano, i token sono di norma costruiti in modo da conservare il formato dell’originale: un token che sostituisce un numero di carta ne mantiene la lunghezza e una forma compatibile, così i sistemi a valle continuano a funzionare senza modifiche. Le linee guida impongono però che non sia confondibile con un numero di carta reale, per esempio che non superi il controllo di validità di Luhn. Il risultato architetturale è netto: la superficie che custodisce dati sensibili si restringe a un solo punto fortificato, mentre tutto il resto diventa un territorio in cui una violazione non trova nulla di utile da portare via. È la traduzione pratica del principio per cui non si può perdere ciò che non si possiede, e si lega bene alle logiche di [prevenzione della perdita di dati](https://www.ictsecuritymagazine.com/articoli/dlp/).

## Tokenizzazione e la riduzione del perimetro

C’è una ragione molto concreta per cui la tokenizzazione è nata e si è diffusa nel mondo dei [pagamenti](https://www.bluefin.com/bluefin-news/tokenization-vs-encryption-choosing-a-payment-and-data-security-solution/), e ha a che fare con la conformità. Gli standard di sicurezza dei dati delle carte impongono controlli stringenti a ogni sistema che tratta il numero di carta reale. Sostituendo quel numero con un token, i sistemi che da quel momento maneggiano solo surrogati escono dal perimetro soggetto a quei controlli, perché non contengono più dati di carta da proteggere. Il vantaggio non è solo di sicurezza, è anche di costo e di [conformità](https://www.ictsecuritymagazine.com/articoli/security-compliance/): meno sistemi nel perimetro significano meno audit, meno requisiti, meno rischio concentrato in meno punti.

Quella che è nata per le carte di pagamento si è poi estesa a ogni categoria di dato personale che valga la pena non disseminare: identificativi, dati sanitari, anagrafiche. La logica resta la stessa, ed è una logica di minimizzazione: ridurre al minimo indispensabile l’insieme dei sistemi che toccano davvero il dato reale, e quindi la supe...