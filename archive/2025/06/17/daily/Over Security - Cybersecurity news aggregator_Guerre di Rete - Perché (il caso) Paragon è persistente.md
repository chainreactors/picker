---
title: Guerre di Rete - Perché (il caso) Paragon è persistente
url: https://guerredirete.substack.com/p/guerre-di-rete-perche-il-caso-paragon
source: Over Security - Cybersecurity news aggregator
date: 2025-06-17
fetch_date: 2025-10-06T22:56:04.982663
---

# Guerre di Rete - Perché (il caso) Paragon è persistente

[![Guerre di Rete](https://substackcdn.com/image/fetch/$s_!JKxa!,w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9c3cbe9e-1c39-4535-99d8-940270e03588_1010x1010.png)](/)

# [Guerre di Rete](/)

IscrivitiAccedi

# Guerre di Rete - Perché (il caso) Paragon è persistente

### E poi le frontiere belliche dell'AI.

[![Avatar di Carola Frediani](https://substackcdn.com/image/fetch/$s_!tOoV!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F9403bb00-3959-45dc-afb5-ac7994d708b8_750x741.jpeg)](https://substack.com/%40guerredirete)

[Carola Frediani](https://substack.com/%40guerredirete)

giu 16, 2025

20

2

Condividi

[![](https://substackcdn.com/image/fetch/$s_!Zr9u!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd7fa1198-17d7-4d85-8426-224290c28d17_1396x1300.png)](https://substackcdn.com/image/fetch/%24s_%21Zr9u%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//substack-post-media.s3.amazonaws.com/public/images/d7fa1198-17d7-4d85-8426-224290c28d17_1396x1300.png)

Credits: https://citizenlab.ca/2025/06/first-forensic-confirmation-of-paragons-ios-mercenary-spyware-finds-journalists-targeted/

**Guerre di Rete - una newsletter di notizie cyber
di Carola Frediani
N. 207 - 16 giugno 2025**

***Cosa è e come funziona la newsletter Guerre di Rete**Specie per i nuovi, ricordo che questa newsletter (che oggi conta quasi 15mila iscritti - ma molti più lettori, essendo pubblicata anche online) **è gratuita e del tutto indipendente,** non ha mai accettato sponsor o pubblicità, e viene fatta nel mio tempo libero. Se vi piace potete contribuire inoltrandola a possibili interessati, o promuovendola sui social. Molti lettori sono diventati sostenitori facendo una [donazione.](https://www.paypal.com/donate/?hosted_button_id=V8WAZ44NT942C)*

[Dona alla newsletter](https://www.paypal.com/donate/?hosted_button_id=V8WAZ44NT942C)

***Il progetto editoriale Guerre di Rete**In più, il progetto si è ingrandito con un sito indipendente e noprofit di informazione cyber, [GuerrediRete.it](https://www.guerredirete.it/). Qui spieghiamo il [progetto](https://www.guerredirete.it/il-progetto/). Qui [l’editoriale](https://www.guerredirete.it/perche-e-il-momento-di-fare-e-informare/) di lancio del sito.
Qui una [lista con link dei nostri progetti](https://linktr.ee/guerredirete) per avere un colpo d’occhio di quello che facciamo.*

Iscriviti

---

**In questo numero:
- Perché (il caso) Paragon è persistente
- Le frontiere belliche dell’AI**

---

**SORVEGLIANZA**
**Perché (il caso) Paragon è persistente**“Qualsiasi tentativo di accedere illegalmente ai dati dei cittadini, compresi i giornalisti e gli oppositori politici, è inaccettabile, se confermato. La Commissione utilizzerà tutti gli strumenti a sua disposizione per garantire l'effettiva applicazione delle norme dell'Unione europea”.
11 giugno 2025. La Commissione europea [interviene](https://apnews.com/article/spyware-italy-paragon-meloni-pegasus-f36dd32106f44398ee24001317ccf2bb) su alcune domande poste da membri del Parlamento Ue. Oggetto: l’Italia.
“La Commissione è a conoscenza dei recenti rapporti sull'uso di Paragon", ha [dichiarato](https://www.eunews.it/en/2025/06/12/brussels-warns-italy-on-spying-on-journalists-we-will-enforce-eu-law/) la vicepresidente esecutiva e commissaria europea per le Tecnologie digitali e di frontiera Henna Virkkunen. Che ricorda all'Italia come il nuovo Regolamento europeo sulla libertà dei media ([European Media Freedom Regulation](https://eur-lex.europa.eu/eli/reg/2024/1083/oj/eng) - EMFA) sarà applicabile dall'8 agosto 2025.

Il riferimento è a un articolo del regolamento che mira a salvaguardare le fonti giornalistiche vietando alle autorità statali di utilizzare strumenti di sorveglianza sui giornalisti, salvo circostanze eccezionali (“giustificato da un motivo imperativo di interesse generale”). Quindi no all’uso di spyware, anche se, come [avevano commentato](https://cmpf.eui.eu/emfa-and-state-surveillance-of-journalists/) alcuni, rischia di rimanere sempre aperta la finestra delle esigenze di sicurezza nazionale che potrebbe essere sfruttata per far rientrare questi malware nei dispositivi di chi fa informazione.

**Cosa dice la relazione Copasir**

L’intervento della commissaria però arriva dopo giorni in cui sembrava che il caso Paragon fosse, se non chiuso, ibernato. Caso che invece, da quando è scoppiato, assomiglia sempre di più a un virus che non si riesce a eliminare. Che anche quando pensi di averlo rimosso ricompare, persistente.

La questione sembrava essere stata chiusa il 4 giugno, quando il Copasir (il Comitato parlamentare per la sicurezza della Repubblica) aveva confermato in una [relazione](https://documenti.camera.it/_dati/leg19/lavori/documentiparlamentari/IndiceETesti/034/004/INTERO.pdf) che la società israeliana Paragon ha effettivamente venduto il suo spyware Graphite alle due agenzie di intelligence italiane, Aisi e Aise, a partire dal 2023. La versione di Graphite fornita non includeva la possibilità di attivare il microfono o la fotocamera del telefono, secondo la relazione. Ma consentiva agli operatori di accedere alle comunicazioni crittografate sui dispositivi violati.

Scrive il Copasir al riguardo: “*A partire dal mese di gennaio 2024, lo spyware Graphite è stato utilizzato per acquisire dati dinamici, cioè comunicazioni in corso attraverso sistemi cifrati di messaggistica istantanea, relativamente a un numero estremamente limitato di utenze sempre con autorizzazione del Procuratore generale presso la Corte di appello di Roma, (...) nonché per esfiltrare messaggi di chat giacenti nella memoria di dispositivi di target (...)”.*

**Gli attivisti di Mediterranea**

La relazione conferma anche che Graphite ha sfruttato una vulnerabilità di WhatsApp che Meta aveva identificato e chiuso (“patchato”) nel dicembre 2024, un mese prima che l'attività dello spyware venisse rivelata pubblicamente. Ma la conferma più importante della relazione è che sono stati davvero intercettati attraverso questo software sia Luca Casarini (che avevo [intervistato qua](https://guerredirete.substack.com/p/guerre-di-rete-starlink-e-i-negoziati)) sia Giuseppe Caccia, figure di spicco della ong Mediterranea SavingHumans. David Yambio, portavoce dell’ONG Refugees in Libya, sarebbe stato intercettato, scrive la relazione, in modo tradizionale mentre il cappellano di *Mediterranea* don Mattia Ferrari non sarebbe stato intercettato direttamente. Si tratta, ricordiamolo, di attivisti coinvolti nel salvataggio di migranti in mare. Non solo: questi attivisti - in particolare Luca Casarini - sono sono stati spiati ripetutamente, e da diversi esecutivi. Anche se l’uso dello spyware sarebbe recente e nato sotto l’attuale governo.

Riprendo al riguardo direttamente la sintesi della relazione Copasir che ha fatto [Fanpage](https://www.fanpage.it/politica/cosa-ce-nella-relazione-finale-del-copasir-sul-caso-paragon-e-lo-spionaggio-a-fanpage/%20https%3A//www.fanpage.it/): “Casarini sarebbe stato colpito da "due operazioni condotte dai servizi", entrambe autorizzate da Giuseppe Conte nel suo secondo governo. La prima sarebbe durata qualche mese a cavallo tra 2019 e 2020. La seconda, "di natura più ampia", partita il 26 maggio 2020, "inizialmente come intercettazione telefonica, si è conclusa nel mese di maggio 2024, sotto il controllo dei Governi Draghi e Meloni". Inizialmente non veniva utilizzato Graphite, che invece è stato "autorizzato in data 5 settembre 2024" dall'attuale sottosegretario Mantovano.
Nel corso di questa operazione sono stati "attenzionati" non solo Casarini e Beppe Caccia, ma "anche il cittadino sudanese David Yambio". Non sarebbe stato colpito don Mattia Ferrari, anche se era sottoposta a intercettazione "un'ute...