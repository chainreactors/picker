---
title: Finland’s Most-Wanted Hacker Nabbed in France
url: https://krebsonsecurity.com/2023/02/finlands-most-wanted-hacker-nabbed-in-france/
source: Krebs on Security
date: 2023-02-06
fetch_date: 2025-10-04T05:48:09.916030
---

# Finland’s Most-Wanted Hacker Nabbed in France

Advertisement

[![](/b-gartner/3.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

Advertisement

[![](/b-gartner/4.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Finland’s Most-Wanted Hacker Nabbed in France

February 5, 2023

[24 Comments](https://krebsonsecurity.com/2023/02/finlands-most-wanted-hacker-nabbed-in-france/#comments)

**Julius “Zeekill” Kivimäki,** a 25-year-old Finnish man charged with extorting a local online psychotherapy practice and leaking therapy notes for more than 22,000 patients online, was arrested this week in France. A notorious hacker convicted of perpetrating tens of thousands of cybercrimes, Kivimäki had been in hiding since October 2022, when he failed to show up in court and Finland issued an international warrant for his arrest.

![](https://krebsonsecurity.com/wp-content/uploads/2022/11/kikmaki-wanted.png)

In late October 2022, Kivimäki was charged (and “arrested in absentia,” according to the Finns) with attempting to extort money from the**Vastaamo Psychotherapy Center**. In that breach, which occurred in October 2020, a hacker using the handle “Ransom Man” threatened to publish patient psychotherapy notes if Vastaamo did not pay a six-figure ransom demand.

Vastaamo refused, so Ransom Man shifted to extorting individual patients — sending them targeted emails threatening to publish their therapy notes unless paid a 500-euro ransom.

When Ransom Man found little success extorting patients directly, they uploaded to the dark web a large compressed file containing all of the stolen Vastaamo patient records.

But as [documented by KrebsOnSecurity in November 2022](https://krebsonsecurity.com/2022/11/hacker-charged-with-extorting-online-psychotherapy-service/), security experts soon discovered Ransom Man had mistakenly included an entire copy of their home folder, where investigators found many clues pointing to Kivimäki’s involvement. From that story:

“Among those who grabbed a copy of the database was **Antti Kurittu**, a team lead at **Nixu Corporation** and a former criminal investigator. In 2013, Kurittu worked on an investigation involving Kivimäki’s use of the Zbot botnet, among other activities Kivimäki engaged in as a member of the hacker group [Hack the Planet](https://krebsonsecurity.com/2015/02/webnic-registrar-blamed-for-hijack-of-lenovo-google-domains/) (HTP).”

“It was a huge opsec [operational security] fail, because they had a lot of stuff in there — including the user’s private SSH folder, and a lot of known hosts that we could take a very good look at,” Kurittu told KrebsOnSecurity, declining to discuss specifics of the evidence investigators seized. “There were also other projects and databases.”

According to the [French news site actu.fr](https://actu.fr/ile-de-france/courbevoie_92026/courbevoie-appelee-pour-violences-conjugales-la-police-arrete-un-criminel-international_57121782.html), Kivimäki was arrested around 7 a.m. on Feb. 3, after authorities in [Courbevoie](https://en.wikipedia.org/wiki/Courbevoie) responded to a domestic violence report. Kivimäki had been out earlier with a woman at a local nightclub, and later the two returned to her home but reportedly got into a heated argument.

Police responding to the scene were admitted by another woman — possibly a roommate — and found the man inside still sleeping off a long night. When they roused him and asked for identification, the 6′ 3″ blonde, green-eyed man presented an ID that stated he was of Romanian nationality.

The French police were doubtful. After consulting records on most-wanted criminals, they quickly identified the man as Kivimäki and took him into custody.

Kivimäki initially gained notoriety as a self-professed member of the [Lizard Squad](https://krebsonsecurity.com/tag/lizard-squad/), a mainly low-skilled hacker group that specialized in DDoS attacks. But American and Finnish investigators say Kivimäki’s involvement in cybercrime dates back to at least 2008, when he was introduced to a founding member of what would soon become HTP.

Finnish police said Kivimäki also used the nicknames “Ryan”, “RyanC” and “Ryan Cleary” (Ryan Cleary was actually a member of a rival hacker group — [LulzSec](https://en.wikipedia.org/wiki/LulzSec) — who was sentenced to prison for hacking).

Kivimaki and other HTP members were involved in mass-compromising web servers using known vulnerabilities, and by 2012 Kivimäki’s alias Ryan Cleary was selling access to those servers in the form of a DDoS-for-hire service. Kivimäki was 15 years old at the time.

![](https://krebsonsecurity.com/wp-content/uploads/2023/02/ryancddos.png)

In 2013, investigators going through devices seized from Kivimäki found computer code that had been used to crack more than 60,000 web servers using a previously unknown vulnerability in **Adobe’s ColdFusion** software.

KrebsOnSecurity detailed the work of HTP in September 2013, after the group [compromised servers inside data brokers LexisNexis, Kroll, and Dun & Bradstreet](https://krebsonsecurity.com/2013/09/data-broker-giants-hacked-by-id-theft-service/).

The group used the same ColdFusion flaws [to break into the National White Collar Crime Center (NWC3)](https://krebsonsecurity.com/2013/10/data-broker-hackers-also-compromised-nw3c/), a non-profit that provides research and investigative support to the **U.S. Federal Bureau of Investigation** (FBI).

As KrebsOnSecurity reported at the time, this small ColdFusion botnet of data broker servers was being controlled by the same cybercriminals who’d assumed control over **ssndob[.]ms**, which operated one of the underground’s most reliable services for obtaining Social Security Number, dates of birth and credit file information on U.S. residents.

Multiple law enforcement sources told KrebsOnSecurity that Kivimäki was responsible for making [an August 2014 bomb threat](http://www.forbes.com/sites/insertcoin/2014/08/24/sony-online-entertainment-presidents-flight-diverted-by-psn-hackers-bomb-threat/) against former **Sony Online Entertainment President John Smedley** that grounded an American Airlines plane. That incident was widely reported to have started with a tweet from the Lizard Squad, but Smedley and others said it started with a call from Kivimäki.

Kivimäki also was involved in calling in multiple fake bomb threats and “swatting” incidents — reporting fake hostage situations at an address to prompt a heavily armed police response to that location.

Kivimäki’s apparent indifference to hiding his tracks drew the interest of Finnish and American cybercrime investigators, and soon Finnish prosecutors charged him with an array of cybercrime violations. At trial, prosecutors presented evidence showing he’d used stolen credit cards to buy luxury goods and shop vouchers, and participated in a money laundering scheme that he used to fund a trip to Mexico.

Kivimäki was ultimately convicted of orchestrating more than 50,000 cybercrimes. But largely because he was still a minor at the time (17) , he was given a 2-year suspended sentence and ordered to forfeit EUR 6,558.

As [I wrote in 2015 following Kivimäki’s trial](https://krebsonsecurity.com/2015/07/finnish-decision-is-win-for-internet-trolls/):

> “The danger in such a decision is that it emboldens young malicious hackers by reinforcing the already popular notion that there are no consequences for cybercrimes committed by individuals...