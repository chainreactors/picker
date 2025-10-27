---
title: Fintech Giant Finastra Investigating Data Breach
url: https://krebsonsecurity.com/2024/11/fintech-giant-finastra-investigating-data-breach/
source: Over Security - Cybersecurity news aggregator
date: 2024-11-21
fetch_date: 2025-10-06T19:20:15.595300
---

# Fintech Giant Finastra Investigating Data Breach

Advertisement

[![](/b-gartner/3.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

Advertisement

[![](/b-gartner/4.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Fintech Giant Finastra Investigating Data Breach

November 19, 2024

[15 Comments](https://krebsonsecurity.com/2024/11/fintech-giant-finastra-investigating-data-breach/#comments)

The financial technology firm **Finastra** is investigating the alleged large-scale theft of information from its internal file transfer platform, KrebsOnSecurity has learned. Finastra, which provides software and services to 45 of the world’s top 50 banks, notified customers of the security incident after a cybercriminal began selling more than 400 gigabytes of data purportedly stolen from the company.

![](https://krebsonsecurity.com/wp-content/uploads/2020/03/finastra.png)

London-based Finastra has offices in 42 countries and reported $1.9 billion in revenues last year. The company employs more than 7,000 people and serves approximately 8,100 financial institutions around the world. A major part of Finastra’s day-to-day business involves processing huge volumes of digital files containing instructions for wire and bank transfers on behalf of its clients.

On November 8, 2024, Finastra notified financial institution customers that on Nov. 7 its security team detected suspicious activity on Finastra’s internally hosted file transfer platform. Finastra also told customers that someone had begun selling large volumes of files allegedly stolen from its systems.

“On November 8, a threat actor communicated on the dark web claiming to have data exfiltrated from this platform,” reads [Finastra’s disclosure](https://krebsonsecurity.com/wp-content/uploads/2024/11/finastra-notice.png), a copy of which was shared by a source at one of the customer firms.

“There is no direct impact on customer operations, our customers’ systems, or Finastra’s ability to serve our customers currently,” the notice continued. “We have implemented an alternative secure file sharing platform to ensure continuity, and investigations are ongoing.”

But its notice to customers does indicate the intruder managed to extract or “exfiltrate” an unspecified volume of customer data.

“The threat actor did not deploy malware or tamper with any customer files within the environment,” the notice reads. “Furthermore, no files other than the exfiltrated files were viewed or accessed. We remain focused on determining the scope and nature of the data contained within the exfiltrated files.”

In a written statement in response to questions about the incident, Finastra said it has been “actively and transparently responding to our customers’ questions and keeping them informed about what we do and do not yet know about the data that was posted.” The company also shared an updated communication to its clients, which said while it was still investigating the root cause, “initial evidence points to credentials that were compromised.”

“Additionally, we have been sharing Indicators of Compromise (IOCs) and our CISO has been speaking directly with our customers’ security teams to provide updates on the investigation and our eDiscovery process,” the statement continues. Here is the rest of what they shared:

> “In terms of eDiscovery, we are analyzing the data to determine what specific customers were affected, while simultaneously assessing and communicating which of our products are not dependent on the specific version of the SFTP platform that was compromised. The impacted SFTP platform is not used by all customers and is not the default platform used by Finastra or its customers to exchange data files associated with a broad suite of our products, so we are working as quickly as possible to rule out affected customers. However, as you can imagine, this is a time-intensive process because we have many large customers that leverage different Finastra products in different parts of their business. We are prioritizing accuracy and transparency in our communications.
>
> Importantly, for any customers who are deemed to be affected, we will be reaching out and working with them directly.”

On Nov. 8, a cybercriminal using the nickname “**abyss0**” posted on the English-language cybercrime community **BreachForums** that they’d stolen files belonging to some of Finastra’s largest banking clients. The data auction did not specify a starting or “buy it now” price, but said interested buyers should reach out to them on Telegram.

[![](https://krebsonsecurity.com/wp-content/uploads/2024/11/finastra-sales-nov8.png)](https://krebsonsecurity.com/wp-content/uploads/2024/11/finastra-sales-nov8.png)

abyss0’s Nov. 7 sales thread on BreachForums included many screenshots showing the file directory listings for various Finastra customers. Image: Ke-la.com.

According to screenshots collected by the cyber intelligence platform [Ke-la.com](https://www.ke-la.com), abyss0 first attempted to sell the data allegedly stolen from Finastra on October 31, but that earlier sales thread did not name the victim company. However, it did reference many of the same banks called out as Finastra customers in the Nov. 8 post on BreachForums.

[![](https://krebsonsecurity.com/wp-content/uploads/2024/11/finastra-bf-oct2024.png)](https://krebsonsecurity.com/wp-content/uploads/2024/11/finastra-bf-oct2024.png)

The original October 31 post from abyss0, where they advertise the sale of data from several large banks that are customers of a large financial software company. Image: Ke-la.com.

The October sales thread also included a starting price: $20,000. By Nov. 3, that price had been reduced to $10,000. A review of abyss0’s posts to BreachForums reveals this user has offered to sell databases stolen in several dozen other breaches advertised over the past six months.

The apparent timeline of this breach suggests abyss0 gained access to Finastra’s file sharing system at least a week before the company says it first detected suspicious activity, and that the Nov. 7 activity cited by Finastra may have been the intruder returning to exfiltrate more data.

Maybe abyss0 found a buyer who paid for their early retirement. We may never know, because this person has effectively vanished. The Telegram account that abyss0 listed in their sales thread appears to have been suspended or deleted. Likewise, abyss0’s account on BreachForums no longer exists, and all of their sales threads have since disappeared.

It seems improbable that both Telegram and BreachForums would have given this user the boot at the same time. The simplest explanation is that something spooked abyss0 enough for them to abandon a number of pending sales opportunities, in addition to a well-manicured cybercrime persona.

In March 2020, Finastra [suffered a ransomware attack](https://krebsonsecurity.com/2020/03/security-breach-disrupts-fintech-firm-finastra/) that sidelined a number of the company’s core businesses for days. According to [reporting from Bloomberg](https://www.bloomberg.com/news/articles/2020-04-08/how-finastra-survived-a-ransomware-attack-without-paying-ransom), Finastra was able to recover from that incident without paying a ransom.

*This is a developing story. Updates will be noted with timestamps. If you have any additional information about this incident, please reach out to krebsonsecurity @ gmail.com or at protonmail.com.*

*This entry ...