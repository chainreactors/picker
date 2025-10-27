---
title: Analisi di una campagna Lumma Stealer con falso CAPTCHA condotta attraverso domino italiano compromesso
url: https://cert-agid.gov.it/news/analisi-di-una-campagna-lumma-stealer-con-falso-captcha-condotta-attraverso-domino-italiano-compromesso/
source: Over Security - Cybersecurity news aggregator
date: 2025-01-14
fetch_date: 2025-10-06T20:13:12.431606
---

# Analisi di una campagna Lumma Stealer con falso CAPTCHA condotta attraverso domino italiano compromesso

* [Vai al contenuto](#main)
* [Vai alla navigazione del sito](#menu "accedi al menu")

[![Logo CERT-AGID](/wp-content/themes/cert-agid/assets/images/cert-agid-logo-white.svg)](https://cert-agid.gov.it/)

# [CERT-AGID Computer Emergency Response Team AGID](https://cert-agid.gov.it/)

[Agenzia per
l'Italia Digitale](https://www.agid.gov.it)

[![Logo AgID - Agenzia per l'Italia Digitale](/wp-content/themes/cert-agid/assets/images/logo-agid.svg)](https://www.agid.gov.it)

Seguici su

* [RSS](https://cert-agid.gov.it/feed/ "RSS")
* [Telegram](https://t.me/certagid "Telegram")
* [X / Twitter](https://twitter.com/agidcert "X / Twitter")

cerca nel sito

[Menu](#menu "accedi al menu")

![Logo del CERT-PA](/wp-content/themes/cert-agid/assets/images/cert-agid-logo-black.svg)
CERT-AGID

<https://cert-agid.gov.it/>

## Menu di navigazione

* Documentazione
  + [Documenti AGID](https://cert-agid.gov.it/documenti-agid/)
  + [Pillole informative](https://cert-agid.gov.it/pillole-informative/)
  + [Flusso IoC](https://cert-agid.gov.it/scarica-il-modulo-accreditamento-feed-ioc/)
* [Chi siamo](https://cert-agid.gov.it/chi-siamo/)
* [Contatti](https://cert-agid.gov.it/contatti/)
* [Strumenti](https://cert-agid.gov.it/strumenti/)
  + [hashr](https://cert-agid.gov.it/hashr/)
  + [Verifica HTTPS e CMS](https://cert-agid.gov.it/verifica-https-cms/)
  + [Statistiche sulle campagne italiane di malware e phishing](https://cert-agid.gov.it/statistiche/)
* [Glossario](https://cert-agid.gov.it/glossario/)
  + [0day](https://cert-agid.gov.it/glossario/0day/)
  + [Botnet](https://cert-agid.gov.it/glossario/botnet/)
  + [Data breach](https://cert-agid.gov.it/glossario/data-breach/)
  + [DDOS-DOS](https://cert-agid.gov.it/glossario/ddos-dos/)
  + [Deep-Dark web](https://cert-agid.gov.it/glossario/deep-dark-web/)
  + [Defacing](https://cert-agid.gov.it/glossario/defacing/)
  + [Exploit](https://cert-agid.gov.it/glossario/exploit/)
  + [MITM](https://cert-agid.gov.it/glossario/mitm/)
  + [OSINT-CLOSINT](https://cert-agid.gov.it/glossario/osint-closint/)
  + [Phishing](https://cert-agid.gov.it/glossario/phishing/)
  + [Privilege escalation](https://cert-agid.gov.it/glossario/privilege-escalation/)
  + [Spam](https://cert-agid.gov.it/glossario/spam/)
  + [Spoofing](https://cert-agid.gov.it/glossario/spoofing/)
  + [SQLi-SQL Injection](https://cert-agid.gov.it/glossario/sqli-sql-injection/)
  + [XSS](https://cert-agid.gov.it/glossario/xss/)
* Link utili
  + [Agenzia per l’Italia Digitale](https://www.agid.gov.it/)
  + [CSIRT Italia](https://csirt.gov.it)
  + [CERT-GARR](https://www.cert.garr.it/)
  + [CNAIPIC](https://www.commissariatodips.it/profilo/cnaipic/index.html)
  + [CERT-DIFESA](https://www.difesa.it/smd/cor/cert-difesa/25338.html)

* [Home](https://cert-agid.gov.it/)
* [Notizie](https://cert-agid.gov.it/category/news/)
* [Malware](https://cert-agid.gov.it/category/news/malware/)
* Analisi di una campagna Lumma Stealer con falso CAPTCHA condotta attraverso domino italiano compromesso

# Analisi di una campagna Lumma Stealer con falso CAPTCHA condotta attraverso domino italiano compromesso

13/01/2025

 [CAPTCHA](https://cert-agid.gov.it/tag/captcha/)
[lumma stealer](https://cert-agid.gov.it/tag/lumma-stealer/)

Una delle tattiche più recenti adottate da **Lumma Stealer** per ingannare le vittime è l’impiego di CAPTCHA falsi, progettati per indurre gli utenti a eseguire script dannosi.

Questo metodo si sta dimostrando estremamente efficace per gli attaccanti poiché sfrutta la fiducia che gli utenti ripongono nelle sfide CAPTCHA, generalmente percepite come controlli di sicurezza legittimi per verificare l’identità umana.

In una campagna [osservata](https://cert-agid.gov.it/news/lumma-stealer-diffuso-tramite-notifica-di-falsa-vulnerabilita-di-sicurezza-sul-proprio-progetto-github/) dal CERT-AGID nel mese di **ottobre 2024**, le vittime venivano avvisate di una presunta vulnerabilità di sicurezza nei loro repository GitHub e invitate a cliccare su un link sospetto. All’apertura del link, si trovavano di fronte a un falso CAPTCHA che le istruiva a copiare ed eseguire uno script *PowerShell* tramite la funzione `WIN+R` (Esegui). Questo processo portava direttamente all’infezione del sistema con il malware Lumma Stealer.

## Dominio italiano compromesso con kit Lumma Stealer

![](https://cert-agid.gov.it/wp-content/uploads/2025/01/lumma-it-domain-1024x539.png)

La scorsa settimana, il CERT-AGID si è imbattuto in un dominio italiano, basato su una versione obsoleta del CMS WordPress, che è stato compromesso e sfruttato per diffondere il malware Lumma Stealer. L’analisi del codice sorgente ha rivelato la presenza di uno script JavaScript codificato in Base64, inserito in modo furtivo, progettato per generare un falso CAPTCHA esclusivamente per le visite provenienti da sistemi operativi MS Windows:

![](https://cert-agid.gov.it/wp-content/uploads/2025/01/image-1.png)

Una volta seguite le istruzioni fornite dal falso CAPTCHA, viene eseguito il seguente script PowerShell, il cui compito è quello di scaricare un file da una risorsa remota ed eseguirlo.

![](https://cert-agid.gov.it/wp-content/uploads/2025/01/image-2-1024x572.png)

## Analisi dello script PowerShell

Il file **`sh`** è un nuovo script PowerShell di 10MB, composto da circa 22.000 righe di codice. L’esecuzione dello script nelle [sandbox online](https://www.joesandbox.com/analysis/1586809/0/html) non ha prodotto risultati utili, poiché è in grado di rilevare la natura dell’ambiente, rendendo quindi necessaria un’analisi manuale.

Analizzando attentamente il contenuto è possibile notare una funzione, denominata `fdsjnh`, che legge una lista di numeri (`charcode`), li converte in una stringa e li interpreta come una sequenza codificata in Base64. Successivamente decodifica la stringa Base64 per ottenere un array di byte e poi li trasforma applicando un’operazione **XOR** con una chiave specifica.

`function fdsjnh {
$arRmAtH = New - Object sYsTEm.CoLLectiONS.arRAyLISt;
FOR ($i = 0;
$i - le $dsAHg78dAS.Length - 1;
$i++) {
$arRmAtH.Add([char]$dsAHg78dAS[$i]) | Out - Null
};
$z = $arRmAtH - join "";
$Enc = [SYStEM.TEXt.ENcODinG]::UTF8;
$XoRKEy = $Enc.$BBB("$GdFsODSAO");
$strinG = $Enc.GetString([systEm.coNVerT]::FromBase64String($z));
$byteSTriNG = $Enc.$BBB($strinG);
$xoRdData = $(for ($i = 0;
$i - lt $byteSTriNG.length;
) {
for ($j = 0;
$j - lt $XoRKEy.length;
$j++) {
$byteSTriNG[$i] - bxor $XoRKEy[$j];
$i++;
if ($i - ge $byteSTriNG.Length) {
$j = $XoRKEy.length
}
}
}
);
$xoRdData = $Enc.GetString($xoRdData);
return $xoRdData
}`

## La chiave XOR

La chiave `XOR` è associata alla variabile `$GdFsODSAO` ed è derivata dalla riassegnazione di variabili in un codice lungo 18.000 righe. Senza questa chiave, non è possibile decodificare correttamente il contenuto.

La soluzione più rapida per ottenere la chiave `XOR` è stata quella di isolare il codice fino alla dichiarazione della variabile `$GdFsODSAO`, aggiungendo una riga allo script per salvare il valore in un file (denominato `xorkey.txt`) ed eseguirlo sulla sandbox [AnyRun](https://app.any.run/tasks/155507cd-698c-44af-85ce-6b3d5f46dd20).

`Set-Content C:\Users\admin\Desktop\xorkey.txt $GdFsODSAO;`

![](https://cert-agid.gov.it/wp-content/uploads/2025/01/image-3-1024x581.png)

*Decodifica della chiave XOR sfruttando AnyRun*

La chiave XOR ottenuta è `AMSI_RESULT_NOT_DETECTED`, che rappresenta il valore restituito dall’API [AMSI](https://learn.microsoft.com/en-us/windows/win32/api/amsi/ne-amsi-amsi_result) (Antimalware Scan Interface) di Microsoft ed indica che il contenuto analizzato non è stato identificato come dannoso o sospetto dal software antivirus.

## Decodifica della funzione principale

A questo punto è possibile utilizzare la chiave all’interno della funzione `fdsjnh` per decodificare il contenuto. A tal proposito, è stato sviluppato il seguente codice Python per eseguire la decodifica:

`import base64
# Array di byte
dsAHg78dAS = [83,50,53,122,68,84, ...]
def fds...