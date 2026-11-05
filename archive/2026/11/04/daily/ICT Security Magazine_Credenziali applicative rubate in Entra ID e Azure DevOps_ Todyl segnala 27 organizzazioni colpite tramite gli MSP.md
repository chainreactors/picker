---
title: Credenziali applicative rubate in Entra ID e Azure DevOps: Todyl segnala 27 organizzazioni colpite tramite gli MSP
url: https://www.ictsecuritymagazine.com/notizie/credenziali-applicative-rubate-entra-id-azure-devops-msp/
source: ICT Security Magazine
date: 2026-11-04
fetch_date: 2026-11-05T08:45:04.364213
---

# Credenziali applicative rubate in Entra ID e Azure DevOps: Todyl segnala 27 organizzazioni colpite tramite gli MSP

[Salta al contenuto](#main)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/logo-ict-security-trasparente-1.webp)](https://www.ictsecuritymagazine.com/)

Cerca nel magazine

* Argomenti

  [Cyber Security: tutti gli articoli 1.345 articoli](https://www.ictsecuritymagazine.com/argomenti/cyber-security/)

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

[Cyber Crime](https://www.ictsecuritymagazine.com/argomenti/cyber-crime/) · [Cyber Security](https://www.ictsecuritymagazine.com/argomenti/cyber-security/)

# Credenziali applicative rubate in Entra ID e Azure DevOps: Todyl segnala 27 organizzazioni colpite tramite gli MSP

Secondo Todyl, dal 1° novembre 2026 un operatore usa credenziali applicative rubate nei tenant degli MSP (campagna Key Eater) e raggiunge 27 organizzazioni. Attore non attribuito.

A cura di:[Redazione](https://www.ictsecuritymagazine.com/author/redazione/)  Ore Pubblicato il4 Novembre 20264 Novembre 2026  Condividi

![Credenziali applicative rubate in Entra ID e Azure DevOps: Todyl segnala 27 organizzazioni colpite tramite gli MSP: Chiave gigante con testa a circuito, rossa e nera, che innesca una scarica gialla su una città di uffici con finestre rosse](https://www.ictsecuritymagazine.com/wp-content/uploads/credenziali-applicative-rubate-entra-id-azure-devops-msp.webp)

In sintesi

* Todyl segnala che dal 1° novembre 2026 un operatore usa credenziali applicative rubate per accedere ai tenant degli MSP, con 27 organizzazioni raggiunte.
* Todyl esclude una vulnerabilità Microsoft e un worm: indica un singolo operatore con una scorta di segreti, non attribuito.
* Secondo Todyl ruotare i segreti non basta: l'attore riprova contro app disabilitate e riusa i refresh token, finora bloccati dal Conditional Access.

Todyl, società di sicurezza gestita, segnala che dal 1° novembre 2026 un singolo operatore entra negli ambienti Microsoft 365 e Azure di *diversi managed service provider* (MSP) con credenziali applicative rubate e ancora valide. Lo scrive nel [post d’indagine](https://www.todyl.com/blog/stolen-app-credentials-real-access-an-actor-is-signing-into-entra-id-and-azure-devops-as-your-workloads) firmato da Andrew Scott, Field CISO, e aggiornato il 3 novembre. La campagna prende il nome di Key Eater.

L’operatore si presenta come le applicazioni stesse degli MSP e da lì raggiunge i loro clienti. Todyl conta 27 organizzazioni, tra governo, energia, agroalimentare, trasporti, edilizia, studi legali, istruzione e non profit. Esclude una vulnerabilità di Microsoft e non attribuisce la campagna a un attore noto.

Una precisazione sulle fonti. I dati vengono quasi tutti dal blog di Todyl, che è anche il fornitore che ha scoperto la campagna, e la redazione non ha potuto verificarli in modo indipendente. Altri fornitori compaiono soltanto in un thread del forum r/msp, con account di cui non si conosce l’identità. Dove non è indicato altrimenti, quello che segue è la ricostruzione di Todyl.

## Credenziali applicative rubate: che cosa ha rilevato Todyl

### I numeri

Todyl parla di circa 45 registrazioni di applicazioni (*app registration*) prese di mira in circa 18 organizzazioni, di cui più di 33 autenticate con successo. L’operatore ha cercato in circa 25 tenant, ha scaricato 81 file e ha consultato circa 2.279 elementi di posta.

Sono cifre minime, perché Todyl vede soltanto le organizzazioni che le inviano i log. L’ultimo tentativo, alle 21:31 UTC del 3 novembre, è stato bloccato. L’ultima azione riuscita risale alle 15:16 UTC dello stesso giorno. [Cyber Security News](https://cybersecuritynews.com/stolen-entra-id-and-azure-credentials/) ha ripreso i dati il 4 novembre senza aggiungere riscontri propri.

### Come si muove l’operatore

L’operatore firma come *service principal*, cioè come identità applicativa di Entra ID, usando segreti dei client. In un caso ha usato una credenziale federata di *workload identity* di Azure DevOps, attiva dal 1° novembre alle 14:39 UTC, e ha riprodotto le sessioni Azure DevOps di due utenti.

Il copione si ripete. Per quasi ogni credenziale chiede prima un token per Azure Resource Manager e poi uno per Key Vault. Spesso, entro pochi secondi, seguono quelli per Graph, Storage e Cognitive Services. Nel giro di minuti si autenticano anche app mai usate prima. Todyl pensa che le letture di Key Vault siano la fonte del materiale nuovo, ma per confermarlo servono i log di audit di Key Vault.

Poi arrivano le ricerche con carattere jolly in Microsoft Graph (29, in circa 25 tenant) e i download da SharePoint, circa un file al secondo, scelti per nome. Todyl elenca password, chiavi private, profili VPN, chiavi API di servizi MFA e di piattaforme RMM, credenziali di backup, configurazioni di firewall e RDP, inventari Azure. Secondo Todyl servono a colpire VPN, servizi MFA, piattaforme RMM, storage di backup e apparati di rete, sistemi che i log di Microsoft 365 non mostrano.

L’accesso a un MSP si estende ai clienti. Una sola app multi-tenant ha attraversato 15 tenant clienti in cicli di circa 10 secondi. In un altro MSP l’app di automazione GDAP, quella delle deleghe di amministrazione, è stata provata sui tenant dei clienti senza successo.

Dopo i rilevamenti delle 07:57 UTC del 3 novembre l’operatore è passato da curl e Python a *user agent* di browser contraffatti. Alle 18:12 UTC ha riprodotto i *refresh token* di più utenti con client scriptati, e il Conditional Access li ha bloccati tutti. Todyl non ha osservato persistenza: nessun nuovo consenso, credenziale, ruolo o utente.

## Sembra un worm, ma Todyl dice di no

La velocità fa pensare a un *worm*. In tre famiglie di MSP l’operatore ha usato materiale appena raccolto per accedere ad altre app nel giro di minuti. In ...