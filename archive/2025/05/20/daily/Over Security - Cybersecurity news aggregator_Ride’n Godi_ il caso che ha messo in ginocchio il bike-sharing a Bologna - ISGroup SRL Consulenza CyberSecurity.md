---
title: Ride’n Godi: il caso che ha messo in ginocchio il bike-sharing a Bologna - ISGroup SRL Consulenza CyberSecurity
url: https://consulenza.isgroup.it/kb/riden-godi-il-caso-che-ha-messo-in-ginocchio-il-bike-sharing-a-bologna/
source: Over Security - Cybersecurity news aggregator
date: 2025-05-20
fetch_date: 2025-10-06T22:33:17.078273
---

# Ride’n Godi: il caso che ha messo in ginocchio il bike-sharing a Bologna - ISGroup SRL Consulenza CyberSecurity

* [Home](https://www.isgroup.it/)
* [Servizi](https://www.isgroup.it/it/servizi.html)
* [Contatti](https://www.isgroup.it/it/contatti.html)

[![ISGroup SRL CyberSecurity](https://consulenza.isgroup.it/wp-content/uploads/2024/06/Logo-ISGroup-SRL-CyberSecurity-e1730237752811.webp)](https://www.isgroup.it/)

La vostra risorsa per le operazioni di ITSEC, Ethical Hacking, Penetration Testing e formazione.

* [Home](https://www.isgroup.it/)
* [Servizi](https://www.isgroup.it/it/servizi.html)
* [Contatti](https://www.isgroup.it/it/contatti.html)

* [Facebook](https://www.facebook.com/profile.php?id=61557911384354)
* [Instagram](https://www.instagram.com/isgroup.it/)
* [LinkedIn](https://www.linkedin.com/in/ongaro/)

# Ride’n Godi: il caso che ha messo in ginocchio il bike-sharing a Bologna

![](https://consulenza.isgroup.it/wp-content/uploads/2025/05/hack-ridengodi.webp)

**Quando l’hack diventa una protesta (e un danno enorme) 😈🚲📱**

Estate 2023, Bologna. Più di **1.600 bici sparite** in pochi mesi.

La causa? Un’app pirata: *Ride’n Godi*.

Qualcuno ha **craccato l’autenticazione BLE**, creato una nuova app e pubblicato **codice + credenziali** di sblocco. Tutto accessibile. Tutto replicabile.

Un caso da manuale di reverse engineering, ma anche una riflessione sul **confine tra hacktivism e illegalità**.

🔒 la sicurezza **non è mai un extra**.
🔁 Ogni oggetto connesso può diventare un vettore di rischio.

Che ne pensi? È solo vandalismo digitale o un modo (sbagliato) per farsi ascoltare? 💬

#hacking #ble #bikesharing #security #vulnerability #IoT #cybercrime #tecnologia #privacy #bluetooth

## Analisi tecnica dell’attacco “Ride’n Godi” al servizio di bike sharing RideMovi

### Introduzione

Nel corso del 2023 è stato condotto un attacco particolarmente sofisticato e ben documentato contro il sistema di bike sharing RideMovi, con un impatto reale: più di 1.600 biciclette sottratte nella città di Bologna. Questo documento ripercorre, con taglio da analista di sicurezza, le fasi tecniche dell’attacco, le vulnerabilità sfruttate, gli strumenti impiegati e le implicazioni sistemiche. L’obiettivo non è solo descrivere cosa è successo, ma soprattutto spiegare *come* è successo, passo dopo passo.

Le fonti pubbliche che supportano questa analisi includono:

* Repository codice: [0xacab.org/Hen/ridegodi](https://0xacab.org/Hen/ridegodi)
* Annunci e comunicazioni: [mastodon.bida.im/@RideGodi](https://mastodon.bida.im/%40RideGodi)
* Contesto ideologico e guida tecnica: [honey.noblogs.org](https://honey.noblogs.org/)

---

### 1. Comprensione dell’architettura del sistema

Il sistema RideMovi si basa su un’architettura classica per veicoli condivisi:

```
BIKE <—— BLE ——> APP (smartphone) <—— HTTPS ——> SERVER
```

In alcuni casi più avanzati:

```
BIKE <—— BLE ——> APP
  \———— HTTP ————/
```

Le biciclette sono dotate di moduli BLE (Bluetooth Low Energy) per ricevere comandi dall’app. L’applicazione mobile funge da ponte tra l’utente e i server centrali, ma è anche il punto più vulnerabile del sistema.

---

### 2. Fase iniziale: raccolta informazioni

Il primo passo è stato ottenere l’accesso ai dati critici: ID delle biciclette, MAC address e chiavi di sblocco. Questo è stato probabilmente realizzato tramite:

* Reverse engineering dell’app ufficiale Android
* Accesso alle chiamate API tramite proxy HTTPS (es. mitmproxy)
* Esfiltrazione di file di configurazione o database contenenti le credenziali

Il formato dei dati raccolti era:

```
bike_ID MAC_address chiave
```

Esempio reale:

```
IE12H12508 E6D03CAEB73F 6e036ccfddea27384e939283b9fc405c
```

La chiave è una stringa esadecimale di 32 caratteri (128 bit), priva di protezione e presumibilmente usata direttamente nel protocollo BLE.

---

### 3. Decodifica e analisi del protocollo BLE

Utilizzando strumenti come `bleak` (Python) e Android HCI snoop log (analizzabili con Wireshark), gli attaccanti hanno tracciato la comunicazione BLE tra l’app originale e le bici.

Elementi osservati:

* Comandi BLE inviati in chiaro
* Nessuna mutua autenticazione
* Possibilità di replay

Il protocollo BLE era talmente semplice da permettere la ricostruzione completa del meccanismo di sblocco.

---

### 4. Costruzione di un’app alternativa: Ride’n Godi

Gli attaccanti hanno poi creato un’app custom:

* Sviluppata in Python/Kivy
* Utilizza `bleak` per interazione BLE
* Include codice Java (via JNI) per gestione BLE su Android

L’app carica un file di testo con la lista dei veicoli e delle rispettive chiavi, poi consente di selezionare e sbloccare una bici con un clic.

L’interfaccia è minimale, ma estremamente efficace. Nessuna verifica lato server è necessaria: l’operazione avviene interamente tra smartphone e bicicletta.

---

### 5. Debolezze sistemiche

#### BLE:

* **Chiavi statiche:** nessuna rotazione, rigenerazione o challenge
* **Accettazione cieca:** la bici accetta comandi validi da qualsiasi dispositivo BLE
* **Assenza di cifratura a livello BLE**

#### API:

Anche il lato server mostrava debolezze:

* Possibilità di sniffare e manipolare le richieste HTTPS (post-patching con Frida/Apktool)
* Tecniche menzionate nel blog includono:
  + Lock immediato dopo unlock per minimizzare la tariffa
  + Spoofing della posizione
  + Invio di errori fittizi per dichiarare la bici guasta
  + Hijacking di sessioni attive

---

### 6. Impatto concreto

* **Bici sottratte:** oltre 1.600 a Bologna nell’estate 2023
* **Danni economici diretti:** non recuperabili
* **Rischio elevato di replicabilità:** codice disponibile pubblicamente

Questo non è stato un semplice proof-of-concept. È stata un’operazione diffusa, con impatto reale e tracciabile.

---

### 7. Considerazioni finali

Questo attacco dimostra l’importanza di considerare l’intero stack di sicurezza: non basta proteggere il server se il BLE è completamente esposto. I sistemi di smart mobility, se non adeguatamente protetti, possono essere disattivati, manipolati o replicati da attori dotati di competenze tecniche intermedie.

#### Raccomandazioni per i fornitori:

* Utilizzo di BLE con autenticazione mutua (es. ECDH)
* Generazione dinamica di chiavi
* Verifica lato server dei comandi BLE
* Hardening dell’app: offuscamento, verifica integrità, TLS pinning

Questo caso studio va considerato come esempio emblematico di “insecurity by design”. La trasparenza dell’attacco, unita alla motivazione politica esplicitata dagli autori, ne fa un documento tecnico e sociale allo stesso tempo.

---

*Analisi redatta da esperti in sicurezza informatica per fini di studio, audit e formazione.*

Vuoi garantire la massima sicurezza informatica alla tua azienda? ISGroup SRL è qui per aiutarti con soluzioni di cyber security su misura per la tua azienda.

Vuoi che gestiamo tutto noi per te? Il servizi di [Virtual CISO](https://www.isgroup.it/it/virtual-ciso.html?mtm_campaign=ConsulenzaWebsite&mtm_source=Virtual CISO&mtm_group=ConsulenzaWebsite) e di [gestione delle vulnerabilità](https://www.isgroup.it/it/vulnerability-management-service.html?mtm_campaign=ConsulenzaWebsite&mtm_source=Vulnerability Management Service&mtm_group=ConsulenzaWebsite) sono perfetti per la tua organizzazione.

Hai già le idee chiare su quello che ti serve? Esplora i nostri servizi di:

* [Vulnerability Assessment](https://www.isgroup.it/it/vulnerability-assessment.html?mtm_campaign=ConsulenzaWebsite&mtm_source=Vulnerability Assessment&mtm_group=ConsulenzaWebsite)
* [Network Penetration Testing](https://www.isgroup.it/it/network-penetration-test.html?mtm_campaign=ConsulenzaWebsite&mtm_source=Network Penetration Testing&mtm_group=ConsulenzaWebsite)
* [Web Application Penetration Testing](https://www.isgroup.it/it/web-application-penetration-test.html?mtm_campaign=ConsulenzaWebsite&mtm_source=Web Application Penetration Testing&mtm_group=ConsulenzaWebsite)
* [Mobile Application Security Testing](https://www.isgroup.it/it/mobile-application-security-testing.html?mtm_campaign=ConsulenzaWebsite&mtm_source=Mobile Application Se...