---
title: Il PDF di Schrödinger stesso hash, due contenuti diversi
url: https://www.forenser.it/schrodinger-pdf-apple-jpx-renderer/
source: Instapaper: Unread
date: 2026-09-10
fetch_date: 2026-09-11T06:53:15.465181
---

# Il PDF di Schrödinger stesso hash, due contenuti diversi

Search for:

 Search

Menu

Close

* [Servizi](https://www.forenser.it/servizi-informatica-forense/)
* [Formazione](https://www.forenser.it/formazione/)
* [News](https://www.forenser.it/news/)
* [Staff](https://www.forenser.it/staff/)
* [Press](https://www.forenser.it/press/)
  + [Video e TV](https://www.forenser.it/press/video-tv/)
  + [Radio](https://www.forenser.it/press/radio/)
  + [Quotidiani e Periodici](https://www.forenser.it/press/quotidiani-e-periodici/)
* [Guide](https://www.forenser.it/category/guide/)
* [Contatti](https://www.forenser.it/contatti/)
  + [Cookie Policy](https://www.forenser.it/contatti/cookie-policy/)
  + [Privacy Policy](https://www.forenser.it/contatti/privacy-policy/)

Search for:

 Search

[![Forenser Srl](https://www.forenser.it/wp-content/uploads/forenser-digital-investigations.png)](https://www.forenser.it/)

[Forenser Srl](https://www.forenser.it/)

Studio Informatica Forense

* [Servizi](https://www.forenser.it/servizi-informatica-forense/)
* [Formazione](https://www.forenser.it/formazione/)
* [News](https://www.forenser.it/news/)
* [Staff](https://www.forenser.it/staff/)
* [Press](https://www.forenser.it/press/)
  + [Video e TV](https://www.forenser.it/press/video-tv/)
  + [Radio](https://www.forenser.it/press/radio/)
  + [Quotidiani e Periodici](https://www.forenser.it/press/quotidiani-e-periodici/)
* [Guide](https://www.forenser.it/category/guide/)
* [Contatti](https://www.forenser.it/contatti/)
  + [Cookie Policy](https://www.forenser.it/contatti/cookie-policy/)
  + [Privacy Policy](https://www.forenser.it/contatti/privacy-policy/)

# Il PDF di Schrödinger: stesso hash, due contenuti diversi

[![](https://secure.gravatar.com/avatar/65af508883433ee06fa507bcdcb1e77747fc2aba840a2130e6877e5be7ffdded?s=44&d=mm&r=g)](https://www.forenser.it/author/forenser/ "Posts by forenser")

[forenser](https://www.forenser.it/author/forenser/)
on
8 Settembre 2026

![](https://www.forenser.it/wp-content/uploads/schrodinger-pdf-apple-jpx-bug.jpg)

Nell’informatica forense, la **PDF forensics** si occupa dell’acquisizione e dell’analisi tecnica dei documenti PDF: struttura interna, immagini, metadati, revisioni, possibili manipolazioni e firme digitali. Anche l’esame delle firme rappresentate graficamente richiede di distinguere ciò che il documento contiene da ciò che viene mostrato sullo schermo.

Ci sono casi nei quali questa analisi diventa più complessa a causa di differenze di interpretazione o di rendering, dovute alla struttura del documento, al software utilizzato o alla loro interazione. Tali differenze possono anche essere sfruttate intenzionalmente da chi costruisce il PDF.

Ci siamo imbattuti in un PDF nel quale **alcune immagini non comparivano in Anteprima (Preview) su macOS**, pur essendo visibili con altri software. Al posto di alcune fotografie apparivano riquadri grigi; lo stesso documento, aperto con altri visualizzatori, mostrava invece le immagini.

L’indagine è partita dalle immagini della copertina: prima di considerarle mancanti o danneggiate, abbiamo verificato che fossero effettivamente presenti negli oggetti del PDF.

Attraverso una serie di test sempre più ridotti è stato possibile circoscrivere una differenza di comportamento alla gestione di particolari immagini **JPEG 2000 con campi della File Type Box che dichiarano il formato JPX**. Questa dichiarazione va distinta dalla piena conformità del container allo standard.

Il risultato è particolarmente interessante: abbiamo costruito **due PDF che differiscono esclusivamente per due byte nell’intero file**, con lo stesso codestream JPEG 2000. Nel test effettuato con PDFKit su macOS, una variante mostra l’immagine e l’altra produce una pagina bianca.

Abbiamo poi sfruttato la differenza di rendering per costruire un secondo esperimento: **un solo PDF che mostra un cane con un renderer e un gatto con un altro**. Il file non cambia; cambia la sua rappresentazione visiva.

Table of Contents

Toggle

* [La struttura del PDF e le immagini contenute](#La_struttura_del_PDF_e_le_immagini_contenute)
* [Le immagini “scomparse” erano ancora dentro il PDF](#Le_immagini_%E2%80%9Cscomparse%E2%80%9D_erano_ancora_dentro_il_PDF)
* [I formati JP2 e JPX](#I_formati_JP2_e_JPX)
* [Analizzare il codestream JPEG 2000](#Analizzare_il_codestream_JPEG_2000)
* [I test svolti per isolare il problema](#I_test_svolti_per_isolare_il_problema)
* [Due PDF con due soli byte di differenza](#Due_PDF_con_due_soli_byte_di_differenza)
* [Il test aggiuntivo: quale dei due byte cambia il risultato?](#Il_test_aggiuntivo_quale_dei_due_byte_cambia_il_risultato)
* [Quindi JPX è un errore e causa un baco?](#Quindi_JPX_e_un_errore_e_causa_un_baco)
* [Un PDF di test per “riconoscere” il renderer](#Un_PDF_di_test_per_%E2%80%9Criconoscere%E2%80%9D_il_renderer)
* [Come evitare il problema creando un PDF](#Come_evitare_il_problema_creando_un_PDF)
* [Gli strumenti per l’analisi forense dei PDF e del rendering](#Gli_strumenti_per_lanalisi_forense_dei_PDF_e_del_rendering)
* [Oltre il riquadro grigio: due immagini nello stesso PDF](#Oltre_il_riquadro_grigio_due_immagini_nello_stesso_PDF)
* [Come funziona l’esperimento](#Come_funziona_lesperimento)
* [Il problema non è più solo un’immagine che non si vede](#Il_problema_non_e_piu_solo_unimmagine_che_non_si_vede)
* [L’interesse nell’ambito informatico forense](#Linteresse_nellambito_informatico_forense)
* [Conclusioni](#Conclusioni)

## La struttura del PDF e le immagini contenute

Per capire il problema bisogna innanzitutto distinguere il documento PDF dal modo in cui viene visualizzato.

Un PDF è un contenitore strutturato che può includere testo, font, grafica vettoriale, immagini raster, trasparenze, profili colore, maschere, livelli e numerosi altri oggetti. Quando apriamo il documento non stiamo necessariamente vedendo qualcosa di già “disegnato”: è il **renderer PDF** a interpretare quegli oggetti e a trasformarli nei pixel mostrati sul display.

Applicazioni differenti possono utilizzare motori differenti, mentre applicazioni diverse possono anche condividere lo stesso motore. Anteprima e altre applicazioni Apple utilizzano le tecnologie PDF del sistema; altri visualizzatori impiegano implementazioni differenti. Anche nel browser il risultato dipende dal componente che apre il PDF: per descrivere una prova servono quindi **applicazione, versione e modalità di apertura**, oltre al sistema operativo.

Un documento leggibile da un renderer può dunque evidenziare un limite, un errore o una diversa gestione dell’input in un altro. Il fatto che un software mostri l’immagine, da solo, non dimostra però che l’intero documento sia conforme alle specifiche.

## Le immagini “scomparse” erano ancora dentro il PDF

Nel documento originario, gli Image XObject delle fotografie erano presenti, con dimensioni e stream apparentemente coerenti. Altri visualizzatori riuscivano a decodificarli e a mostrarli: l’assenza sullo schermo non corrispondeva all’assenza dei dati nel PDF.

Le sei immagini problematiche della copertina condividevano una caratteristica:

**JPEG 2000 + CMYK + filtro PDF `/JPXDecode`.**

Il filtro `/JPXDecode`, introdotto con PDF 1.5, è il meccanismo previsto per decodificare immagini JPEG 2000. Il suo nome non significa che ogni stream debba avere il brand `jpx` : lo stesso filtro è usato anche per immagini con container JP2. La specifica disciplina inoltre il rapporto tra le informazioni colore interne all’immagine e quelle dell’Image XObject.

La presenza di `/JPXDecode`, quindi, **non costituisce di per sé un errore**.

## I formati JP2 e JPX

JPEG 2000 comprende una famiglia di specifiche. La **Part 1** definisce il sistema di codifica principale e il formato **JP2**; la **Part 2** introduce estensioni alla codifica e il formato **JPX**, con funzionalità aggiuntive per la descrizione del colore, più codestream e la composizione delle immagini. È essenziale distinguere il **codestream compresso** dal **container** che lo racchiude.

Un container JP2...