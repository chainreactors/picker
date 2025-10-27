---
title: Judge Orders U.S. Lawyer in Russian Botnet Case to Pay Google
url: https://krebsonsecurity.com/2022/12/judge-orders-u-s-lawyer-in-russian-botnet-case-to-pay-google/
source: Over Security - Cybersecurity news aggregator
date: 2022-12-06
fetch_date: 2025-10-04T00:35:29.743837
---

# Judge Orders U.S. Lawyer in Russian Botnet Case to Pay Google

Advertisement

[![](/b-gartner/7.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

Advertisement

[![](/b-ninjio/7.png)](https://ninjio.com/lp46d-krebs/)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Judge Orders U.S. Lawyer in Russian Botnet Case to Pay Google

December 5, 2022

[17 Comments](https://krebsonsecurity.com/2022/12/judge-orders-u-s-lawyer-in-russian-botnet-case-to-pay-google/#comments)

In December 2021, **Google** filed a civil lawsuit against two Russian men thought to be responsible for operating **Glupteba**, one of the Internet’s largest and oldest botnets. The defendants, who initially pursued a strategy of counter suing Google for interfering in their sprawling cybercrime business, later brazenly offered to dismantle the botnet in exchange for payment from Google. The judge in the case was not amused, found for the plaintiff, and ordered the defendants *and their U.S. attorney* to pay Google’s legal fees.

![](https://krebsonsecurity.com/wp-content/uploads/2022/12/gluptebamodules.png)

Glupteba is a rootkit that steals passwords and other access credentials, disables security software, and tries to compromise other devices on the victim network — such as Internet routers and media storage servers — for use in relaying spam or other malicious traffic.

Collectively, the tens of thousands of systems infected with Glupteba on any given day feed into a number of major cybercriminal businesses: The botnet’s proprietors sell the credential data they steal, use the botnet to place disruptive ads on the infected computers, and mine cryptocurrencies. Glupteba also rents out infected systems as “proxies,” directing third-party traffic through the infected devices to disguise the origin of the traffic.

In June 2022, KrebsOnSecurity showed how the malware proxy services [RSOCKS and AWMProxy were entirely dependent on the Glupteba botnet](https://krebsonsecurity.com/2022/06/the-link-between-awm-proxy-the-glupteba-botnet/) for fresh proxies, and that the founder of AWMProxy was **Dmitry Starovikov** — one of the Russian men named in Google’s lawsuit.

Google sued Starovikov and 15 other “John Doe” defendants, alleging violations of the Racketeer Influenced and Corrupt Organizations Act (RICO), the Computer Fraud and Abuse Act, trademark and unfair competition law, and unjust enrichment.

In June, Google and the named defendants agreed that the case would proceed as a nonjury action because Google had withdrawn its claim for damages — seeking only injunctive relief to halt the operations of the botnet.

The defendants, who worked for a Russian firm called “**Valtron**” that was also named in the lawsuit, told Google that they were interested in settling. The defendants said they could potentially help Google by taking the botnet offline.

![](https://krebsonsecurity.com/wp-content/uploads/2022/12/glupteba-eco.png)

But the court expressed frustration that the defendants were unwilling to consent to a permanent injunction, and at the same time were unable to articulate why an injunction forbidding them from engaging in unlawful activities would pose a problem.

“The Defendants insisted that they were not engaged in criminal activity, and that any alleged activity in which they were engaged was legitimate,” U.S. District Court Judge Denise Cote wrote. “Nevertheless, the Defendants resisted entry of a permanent injunction, asserting that Google’s use of the preliminary injunction had disrupted their normal business operations.”

While the defendants represented that they had the ability to dismantle the Glupteba botnet, when it came time for discovery — the stage in a lawsuit where both parties can compel the production of documents and other information pertinent to their case — the attorney for the defendants told the court his clients had been fired by Valtron in late 2021, and thus no longer had access to their work laptops or the botnet.

The lawyer for the defendants — New York-based cybercrime defense attorney **Igor Litv****ak** — told the court he first learned about his clients’ termination from Valtron on May 20, a fact Judge Cote said she found “troubling” given statements he made to the court after that date representing that his clients still had access to the botnet.

The court ultimately suspended the discovery process against Google, saying there was reason to believe the defendants sought discovery only “to learn whether they could circumvent the steps Google has taken to block the malware.”

On September 6, Litvak emailed Google that his clients were willing to discuss settlement.

“The parties held a call on September 8, at which Litvak explained that the Defendants would be willing to provide Google with the private keys for Bitcoin addresses associated with the Glupteba botnet, and that they would promise not to engage in their alleged criminal activity in the future (without any admission of wrongdoing),” the judge wrote.

“In exchange, the Defendants would receive Google’s agreement not to report them to law enforcement, and a payment of $1 million per defendant, plus $110,000 in attorney’s fees,” Judge Cote continued. “The Defendants stated that, although they do not currently have access to the private keys, Valtron would be willing to provide them with the private keys if the case were settled. The Defendants also stated that they believe these keys would help Google shut down the Glupteba botnet.”

Google rejected the defendants’ offer as extortionate, and reported it to law enforcement. Judge Cote also found Litvak was complicit in the defendants’ efforts to mislead the court, and ordered him to join his clients in paying Google’s legal fees.

“It is now clear that the Defendants appeared in this Court not to proceed in good faith to defend against Google’s claims but with the intent to abuse the court system and discovery rules to reap a profit from Google,” Judge Cote wrote.

Litvak has filed [a motion to reconsider](https://krebsonsecurity.com/wp-content/uploads/2022/12/133-1.pdf) (PDF), asking the court to vacate the sanctions against him. He said his goal is to get the case back into court.

“The judge was completely wrong to issue sanctions,” Litvak said in an interview with KrebsOnSecurity. “From the beginning of the case, she acted as if she needed to protect Google from something. If the court does not decide to vacate the sanctions, we will have to go to the Second Circuit ([Court of Appeals](https://en.wikipedia.org/wiki/United_States_Court_of_Appeals_for_the_Second_Circuit)) and get justice there.”

In [a statement on the court’s decision](https://blog.google/outreach-initiatives/public-policy/a-ruling-in-our-legal-case-against-the-glupteba-botnet/), Google said it will have significant ramifications for online crime, and that since its technical and legal attacks on the botnet last year, Google has observed a 78 percent reduction in the number of hosts infected by Glupteba.

“While Glupteba operators have resumed activity on some non-Google platforms and IoT devices, shining a legal spotlight on the group makes it less appealing for other criminal operations to work with them,” reads a blog post from Google’s General Counsel **Halimah DeLaine Prado** and vice president of engineering **Royal Hansen**. “And the steps [Google] took last year to disrupt their operations have already had significant impact.”

![](https://krebsonsecurity.com/wp-content/uploads/2022/06/certpolska-glupteba.png)

*This entry was posted on Monday 5th of December 2022 02:44 PM*

[A Little Sunshine](https://kre...