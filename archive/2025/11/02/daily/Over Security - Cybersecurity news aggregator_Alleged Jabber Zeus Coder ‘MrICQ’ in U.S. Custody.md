---
title: Alleged Jabber Zeus Coder ‘MrICQ’ in U.S. Custody
url: https://krebsonsecurity.com/2025/11/alleged-jabber-zeus-coder-mricq-in-u-s-custody/
source: Over Security - Cybersecurity news aggregator
date: 2025-11-02
fetch_date: 2025-11-03T03:15:39.631869
---

# Alleged Jabber Zeus Coder ‘MrICQ’ in U.S. Custody

Advertisement

[![](/b-gartner/3.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

Advertisement

[![](/b-sysdig/2.png)](https://content.foleon.com/sysdig/sysdig-cloud-defense-report-2025/?utm_source=krebs-on-security&utm_medium=display&utm_campaign=aware_amer_the-right-way_na_ung_display&utm_content=AD000462_1240x160)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Alleged Jabber Zeus Coder ‘MrICQ’ in U.S. Custody

November 2, 2025

[1 Comment](https://krebsonsecurity.com/2025/11/alleged-jabber-zeus-coder-mricq-in-u-s-custody/#comments)

A Ukrainian man indicted in 2012 for conspiring with a prolific hacking group to steal tens of millions of dollars from U.S. businesses was arrested in Italy and is now in custody in the United States, KrebsOnSecurity has learned.

Sources close to the investigation say **Yuriy Igorevich Rybtsov**, a 41-year-old from the Russia-controlled city of Donetsk, Ukraine, was previously referenced in U.S. federal charging documents only by his online handle “**MrICQ**.” According to [a 13-year-old indictment](https://www.justice.gov/iso/opa/resources/2162014411104532407242.pdf) (PDF) filed by prosecutors in Nebraska, MrICQ was a developer for a cybercrime group known as “**Jabber Zeus**.”

![](https://krebsonsecurity.com/wp-content/uploads/2025/11/rybtsov-lockedup.png)

The Jabber Zeus name is derived from the malware they used — a custom version of the [ZeuS banking trojan](https://krebsonsecurity.com/?s=zeus+trojan) — that stole banking login credentials and would send the group a Jabber instant message each time a new victim entered a one-time passcode at a financial institution website. The gang targeted mostly small to mid-sized businesses, and they were an early pioneer of so-called “man-in-the-browser” attacks, malware that can silently intercept any data that victims submit in a web-based form.

Once inside a victim company’s accounts, the Jabber Zeus crew would modify the firm’s payroll to add dozens of “money mules,” people recruited through elaborate work-at-home schemes to handle bank transfers. The mules in turn would forward any stolen payroll deposits — minus their commissions — via wire transfers to other mules in Ukraine and the United Kingdom.

The 2012 indictment targeting the Jabber Zeus crew named MrICQ as “**John Doe #3**,” and said this person handled incoming notifications of newly compromised victims. The Department of Justice (DOJ) said MrICQ also helped the group launder the proceeds of their heists through electronic currency exchange services.

Two sources familiar with the Jabber Zeus investigation said Rybtsov was arrested in Italy, although the exact date and circumstances of his arrest remain unclear. A [summary of recent decisions](https://www.cortedicassazione.it/resources/cms/documents/Rassegna_mensile_MAGGIO_2025__settore_penale.pdf) (PDF) published by the Italian Supreme Court states that in April 2025, Rybtsov lost a final appeal to avoid extradition to the United States.

According to the mugshot website **lockedup[.]wtf**, Rybtsov arrived in Nebraska on October 9, and was being held under an arrest warrant from the **U.S. Federal Bureau of Investigation** (FBI).

The data breach tracking service [Constella Intelligence](https://constella.ai) found breached records from the business profiling site bvdinfo[.]com showing that a 41-year-old Yuriy Igorevich Rybtsov worked in a building at 59 Barnaulska St. in Donetsk. Further searching on this address in Constella finds the same apartment building was shared by a business registered to **Vyacheslav “Tank” Penchukov**, the leader of the Jabber Zeus crew in Ukraine.

![](https://krebsonsecurity.com/wp-content/uploads/2022/11/tank-dj.png)

Penchukov was [arrested in 2022](https://krebsonsecurity.com/2022/11/top-zeus-botnet-suspect-tank-arrested-in-geneva/) while traveling to meet his wife in Switzerland. Last year, a federal court in Nebraska [sentenced Penchukov to 18 years in prison](https://www.wired.com/story/vyacheslav-igorevich-penchukov-tank-zeus-malware-sentencing/) and ordered him to pay more than $73 million in restitution.

**Lawrence Baldwin** is founder of [myNetWatchman](https://mynetwatchman.com), a threat intelligence company based in Georgia that began tracking and disrupting the Jabber Zeus gang in 2009. myNetWatchman had secretly gained access to the Jabber chat server used by the Ukrainian hackers, allowing Baldwin to eavesdrop on the daily conversations between MrICQ and other Jabber Zeus members.

Baldwin shared those real-time chat records with multiple state and federal law enforcement agencies, and with this reporter. Between 2010 and 2013, I spent several hours each day alerting small businesses across the country that their payroll accounts were about to be drained by these cybercriminals.

Those notifications, and Baldwin’s tireless efforts, saved countless would-be victims a great deal of money. In most cases, however, we were already too late. Nevertheless, the pilfered Jabber Zeus group chats provided the basis for dozens of stories published here about [small businesses fighting their banks](https://krebsonsecurity.com/category/smallbizvictims/) in court over six- and seven-figure financial losses.

Baldwin said the Jabber Zeus crew was far ahead of its peers in several respects. For starters, their intercepted chats showed they worked to create a highly customized botnet directly with the author of the original Zeus Trojan — **Evgeniy Mikhailovich Bogachev**, a Russian man who has long been on the FBI’s “Most Wanted” list. The feds have a [standing $3 million reward](https://krebsonsecurity.com/2015/02/fbi-3m-bounty-for-zeus-trojan-author/) for information leading to Bogachev’s arrest.

![](https://krebsonsecurity.com/wp-content/uploads/2019/12/bogachev.png)

The core innovation of Jabber Zeus was an alert that MrICQ would receive each time a new victim entered a one-time password code into a phishing page mimicking their financial institution. The gang’s internal name for this component was “**Leprechaun**,” (the [video below](https://www.youtube.com/watch?v=UiAg3puABeA) from myNetWatchman shows it in action). Jabber Zeus would actually re-write the HTML code as displayed in the victim’s browser, allowing them to intercept any passcodes sent by the victim’s bank for multi-factor authentication.

“These guys had compromised such a large number of victims that they were getting buried in a tsunami of stolen banking credentials,” Baldwin told KrebsOnSecurity. “But the whole point of Leprechaun was to isolate the highest-value credentials — the commercial bank accounts with two-factor authentication turned on. They knew these were far juicier targets because they clearly had a lot more money to protect.”

Baldwin said the Jabber Zeus trojan also included a custom “backconnect” component that allowed the hackers to relay their bank account takeovers through the victim’s own infected PC.

“The Jabber Zeus crew were literally connecting to the victim’s bank account from the victim’s IP address, or from the remote control function and by fully emulating the device,” he said. “That trojan was like a hot knife through butter of what everyone thought was state-of-the-art secure online banking at the time.”

Although the Jabber Zeus crew was in direct contact with the Zeus author, the chats intercepted by myNetWatchman show Bogachev frequently ignored the group’s pleas for help. The government says the real leader of the Jabber Zeus crew was **Maksim Yakubets**, a 38-year Ukrainian man with Russian c...