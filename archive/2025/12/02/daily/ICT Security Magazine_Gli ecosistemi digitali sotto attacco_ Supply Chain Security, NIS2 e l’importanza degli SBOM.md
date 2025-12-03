---
title: Gli ecosistemi digitali sotto attacco: Supply Chain Security, NIS2 e l’importanza degli SBOM
url: https://www.ictsecuritymagazine.com/articoli/sbom/
source: ICT Security Magazine
date: 2025-12-02
fetch_date: 2025-12-03T03:17:04.930875
---

# Gli ecosistemi digitali sotto attacco: Supply Chain Security, NIS2 e l’importanza degli SBOM

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

![Vincenzo Sammartino al Forum ICT Security 2025 spiega SBOM e Digital Twin per difendere la supply chain da minacce cyber emergenti.](https://www.ictsecuritymagazine.com/wp-content/uploads/untitled-design-6_uoONfzQ3.png)

# Gli ecosistemi digitali sotto attacco: Supply Chain Security, NIS2 e l’importanza degli SBOM

A cura di:[Vincenzo Sammartino](#molongui-disabled-link)  Ore 2 Dicembre 20252 Dicembre 2025

*Al Forum ICT Security 2025, Vincenzo Sammartino analizza i rischi emergenti degli attacchi alla catena di fornitura e le strategie di difesa attraverso Digital Twin e Software Bill of Materials*

## Dal biologico al digitale: comprendere gli ecosistemi informatici

Quando si parla di cybersecurity, pensare in termini di singoli sistemi isolati non è più sufficiente. Questa consapevolezza emerge con chiarezza dall’intervento dal titolo **“NIS2, Supply Chain Security e SBOM”**, tenuto da Vincenzo Sammartino durante la 23ª edizione del [Forum ICT Security](https://www.ictsecuritymagazine.com/eventi/forumictsecurity2025), svoltosi a Roma il 19 e 20 novembre 2025. Sammartino, dottorando del National PhD in Artificial Intelligence presso l’Università di Pisa, ha sostituito il professor Fabrizio Baiardi, impossibilitato a partecipare per motivi di salute.

L’esperto ha aperto la sua presentazione con un’analogia tanto efficace quanto illuminante: quella tra ecosistema biologico ed ecosistema digitale. Ha spiegato che così come nell’ecosistema biologico l’energia fluisce dal basso verso l’alto della piramide alimentare, trasportando con sé non solo nutrimento ma anche tossine, funghi e batteri, allo stesso modo nell’ecosistema digitale le vulnerabilità si propagano attraverso la catena di fornitura. Ciò che per gli organismi viventi rappresentano le tossine, nel mondo digitale sono le vulnerabilità informatiche che si diffondono da un componente all’altro, da un fornitore all’utilizzatore finale.

![](https://www.ictsecuritymagazine.com/wp-content/uploads/Ecosistemi-e-catene-alimentari.png)

Ecosistemi e catene alimentari

Questa prospettiva sistemica rappresenta un cambio di paradigma fondamentale per comprendere la natura degli attacchi *supply chain*, dove una singola vulnerabilità inserita a un determinato livello della catena può propagarsi come un’onda a tutti i sistemi che dipendono da quel componente. La sicurezza, quindi, non è più una proprietà dei singoli sistemi, ma dell’intero ecosistema informativo a cui tali sistemi appartengono.

## L’industria del ransomware: un ecosistema criminale strutturato e maturo

Uno degli aspetti più inquietanti emersi dall’intervento riguarda l’evoluzione del ransomware, che è diventato ormai una vera e propria industria strutturata con attori specializzati e ben organizzati. Come ha sottolineato Sammartino, non si parla più di singoli criminali informatici, ma di vere e proprie organizzazioni che operano secondo il modello del *ransomware as a service*, dove diversi attori collaborano ciascuno con competenze specifiche.

![](https://www.ictsecuritymagazine.com/wp-content/uploads/Ecosistema-Ransomware.png)

Ecosistema Ransomware

Al centro di questo ecosistema criminale si trova una figura chiave: l’*Initial Access Broker*, ovvero chi vende l’accesso iniziale a una rete o sistema compromesso. Questo punto di accesso iniziale nella catena di fornitura viene poi sfruttato da altri attori per perpetrare l’attacco vero e proprio. L’ecosistema include sviluppatori di malware, fornitori di infrastrutture di hosting protette (*bulletproof hosting*), affiliati che distribuiscono il ransomware, servizi di negoziazione con le vittime e persino servizi di riciclaggio del denaro (*money laundering*).

La complessità dell’ecosistema della cybersecurity è stata illustrata attraverso una slide deliberatamente caotica che mostra centinaia di fornitori, servizi e prodotti interconnessi. Lo speaker ha fatto notare come dietro ogni singolo logo rappresentato ci siano in realtà tantissimi attori, e di conseguenza la superficie di attacco aumenta in maniera esponenziale. Un esempio recente citato è stato quello di Cloudflare, che nei giorni precedenti al convegno era stato al centro delle cronache per quello che inizialmente sembrava un attacco informatico ma che si è poi rivelato essere un errore di programmazione. Tuttavia, questo errore ha comunque avuto ripercussioni su numerosi altri servizi che dipendevano da Cloudflare, dimostrando quanto sia estesa e fragile la rete di interdipendenze nell’ecosistema digitale.

## Anatomia di un attacco supply chain: come funziona la compromissione

Sammartino ha illustrato con precisione il meccanismo attraverso cui si sviluppa un attacco alla catena di fornitura. Il processo inizia con la scelta strategica di un fornitore: gli attaccanti non colpiscono direttamente l’obiettivo finale, ma identificano prima quali fornitori utilizza il target prescelto. Una volta individuato il fornitore più vulnerabile o strategico, gli attaccanti lo compromettono inserendo del codice malevolo all’interno del suo prodotto o servizio.

![](https://www.ictsecuritymagazine.com/wp-content/uploads/Supply-chain-attack.png)

Supply chain attack

Un aspetto particolarmente insidioso di questi attacchi riguarda la scelta dei target preferiti: paradossalmente, i sistemi di sicurezza stessi rappresentano gli obiettivi ideali. Il relatore ha spiegato che questo avviene perché inserire un malware all’interno di un prodotto di ...