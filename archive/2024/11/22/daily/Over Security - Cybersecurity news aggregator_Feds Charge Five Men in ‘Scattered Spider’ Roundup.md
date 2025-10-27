---
title: Feds Charge Five Men in ‘Scattered Spider’ Roundup
url: https://krebsonsecurity.com/2024/11/feds-charge-five-men-in-scattered-spider-roundup/
source: Over Security - Cybersecurity news aggregator
date: 2024-11-22
fetch_date: 2025-10-06T19:17:44.076835
---

# Feds Charge Five Men in ‘Scattered Spider’ Roundup

Advertisement

[![](/b-sysdig/1.png)](https://content.foleon.com/sysdig/sysdig-cloud-defense-report-2025/?utm_source=krebs-on-security&utm_medium=display&utm_campaign=aware_amer_the-right-way_na_ung_display&utm_content=AD000460_1240x110)

Advertisement

[![](/b-action1/2.jpg)](https://action1.com/double-endpoints-free-cam2025/?utm_source=paidmedia&refid=Display_CAM_Krebs)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Feds Charge Five Men in ‘Scattered Spider’ Roundup

November 21, 2024

[9 Comments](https://krebsonsecurity.com/2024/11/feds-charge-five-men-in-scattered-spider-roundup/#comments)

Federal prosecutors in Los Angeles this week unsealed criminal charges against five men alleged to be members of a hacking group responsible for dozens of cyber intrusions at major U.S. technology companies between 2021 and 2023, including **LastPass**, **MailChimp**, **Okta**, **T-Mobile** and **Twilio**.

![](https://krebsonsecurity.com/wp-content/uploads/2022/08/amitaico.png)

The five men, aged 20 to 25, are allegedly members of a hacking conspiracy dubbed “**Scattered Spider**” and “**Oktapus**,” which specialized in SMS-based phishing attacks that tricked employees at tech firms into entering their credentials and one-time passcodes at phishing websites.

The targeted SMS scams asked employees to click a link and log in at a website that mimicked their employer’s Okta authentication page. Some SMS phishing messages told employees their VPN credentials were expiring and needed to be changed; other phishing messages advised employees about changes to their upcoming work schedule.

These attacks leveraged newly-registered domains that often included the name of the targeted company, such as [twilio-help[.]com](https://urlscan.io/result/ca9d3120-7c5f-4502-8faf-09a94274ba71/) and [ouryahoo-okta[.]com](https://urlscan.io/result/d17edad8-ef65-4d25-a0eb-39b7cc4ab593/). The phishing websites were normally kept online for just one or two hours at a time, meaning they were often yanked offline before they could be flagged by anti-phishing and security services.

The phishing kits used for these campaigns featured a hidden Telegram instant message bot that forwarded any submitted credentials in real-time. The bot allowed the attackers to use the phished username, password and one-time code to log in as that employee at the real employer website.

In August 2022, multiple security firms gained access to the server that was receiving data from that Telegram bot, which on several occasions leaked the Telegram ID and handle of its developer, who used the nickname “**Joeleoli**.”

[![](https://krebsonsecurity.com/wp-content/uploads/2024/11/joeleoli-tg.png)](https://krebsonsecurity.com/wp-content/uploads/2024/11/joeleoli-tg.png)

The Telegram username “Joeleoli” can be seen sandwiched between data submitted by people who knew it was a phish, and data phished from actual victims. Click to enlarge.

That Joeleoli moniker registered on the cybercrime forum **OGusers** in 2018 with the email address **joelebruh@gmail.com**, which also was used to register accounts at several websites for a Joel Evans from North Carolina. Indeed, prosecutors say Joeleoli’s real name is **Joel Martin Evans**, and he is a 25-year-old from Jacksonville, North Carolina.

One of Scattered Spider’s first big victims in its 2022 SMS phishing spree was **Twilio**, a company that provides services for making and receiving text messages and phone calls. The group then used their access to Twilio to attack at least 163 of its customers. According to prosecutors, the group mainly sought to steal cryptocurrency from victim companies and their employees.

“The defendants allegedly preyed on unsuspecting victims in this phishing scheme and used their personal information as a gateway to steal millions in their cryptocurrency accounts,” [said](https://www.justice.gov/usao-cdca/pr/5-defendants-charged-federally-running-scheme-targeted-victim-companies-phishing-text) **Akil Davis**, the assistant director in charge of the FBI’s Los Angeles field office.

Many of the hacking group’s phishing domains were registered through the registrar **NameCheap**, and FBI investigators said records obtained from NameCheap showed the person who managed those phishing websites did so from an Internet address in Scotland. The feds then obtained records from Virgin Media, which showed the address was leased for several months to **Tyler Buchanan**, a 22-year-old from Dundee, Scotland.

![](https://krebsonsecurity.com/wp-content/uploads/2022/08/twiliophish.png)

A Scattered Spider phishing lure sent to Twilio employees.

As [first reported here in June](https://krebsonsecurity.com/2024/06/alleged-boss-of-scattered-spider-hacking-group-arrested/), Buchanan was arrested in Spain as he tried to board a flight bound for Italy. The Spanish police told local media that Buchanan, who allegedly went by the alias “**Tylerb**,” at one time possessed Bitcoins worth $27 million.

The government says much of Tylerb’s cryptocurrency wealth was the result of successful **SIM-swapping** attacks, wherein crooks transfer the target’s phone number to a device they control and intercept any text messages or phone calls sent to the victim — including one-time passcodes for authentication, or password reset links sent via SMS.

According to several SIM-swapping channels on Telegram where Tylerb was known to frequent, rival SIM-swappers hired thugs to invade his home in February 2023. Those accounts state that the intruders assaulted Tylerb’s mother in the home invasion, and that they threatened to burn him with a blowtorch if he didn’t give up the keys to his cryptocurrency wallets. Tylerb was reputed to have fled the United Kingdom after that assault.

![](https://krebsonsecurity.com/wp-content/uploads/2024/06/tylerb.png)

A still frame from a video released by the Spanish national police, showing Tyler Buchanan being taken into custody at the airport.

Prosecutors allege Tylerb worked closely on SIM-swapping attacks with **Noah Michael Urban**, another alleged Scattered Spider member from Palm Coast, Fla. who went by the handles “**Sosa**,” “**Elijah**,” and “**Kingbob**.”

Sosa was known to be a top member of the broader cybercriminal community online known as “**The Com**,” wherein hackers boast loudly about high-profile exploits and hacks that almost invariably begin with social engineering — tricking people over the phone, email or SMS into giving away credentials that allow remote access to corporate networks.

In January 2024, KrebsOnSecurity [broke the news](https://krebsonsecurity.com/2024/01/fla-man-charged-in-sim-swapping-spree-is-key-suspect-in-hacker-groups-oktapus-scattered-spider/) that Urban had been arrested in Florida in connection with multiple SIM-swapping attacks. That story noted that Sosa’s alter ego Kingbob routinely targeted people in the recording industry to steal and share “grails,” a slang term used to describe unreleased music recordings from popular artists.

FBI investigators identified a fourth alleged member of the conspiracy – **Ahmed Hossam Eldin Elbadawy**, 23, of College Station, Texas — after he used a portion of cryptocurrency funds stolen from a victim company to pay for an account used to register phishing domains.

The indictment unsealed Wednesday alleges Elbadawy controlled a number of cryptocurrency accounts used to receive stolen funds, along with another Texas man — **Evans Onyeaka Osiebo**, 20, of Dallas.

Members of Scattered Spider are reputed to have been involved in [a September 2023 ransomware attack](https://archive.ph/MuU4s) against the **MGM Resorts** hotel chain that quickly brought multi...