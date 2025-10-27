---
title: The rise of Savastan0: a look into a growing carding marketplace
url: https://labs.yarix.com/2025/02/savastan0_carding/
source: Over Security - Cybersecurity news aggregator
date: 2025-02-14
fetch_date: 2025-10-06T20:38:18.016760
---

# The rise of Savastan0: a look into a growing carding marketplace

[![YLabs](//labs.yarix.com/wp-content/uploads/2025/01/Logo_Yarix.png)![YLabs](//labs.yarix.com/wp-content/uploads/2021/01/yarix_logo.png)![YLabs](//labs.yarix.com/wp-content/uploads/2025/01/Logo_Yarix.png)](https://labs.yarix.com/ "YLabs - Research & Development")

* [Home](https://labs.yarix.com/)
* [Blog](https://labs.yarix.com/category/blog/)
* [Advisories](https://labs.yarix.com/advisories/)
* [Careers](https://www.yarix.com/job-opportunity/)

# The rise of Savastan0: a look into a growing carding marketplace

* [Home](https://labs.yarix.com "Go to Home Page")
* The rise of Savastan0: a look into a growing carding marketplace

[Back to Posts](https://labs.yarix.com)

![](https://labs.yarix.com/wp-content/uploads/2025/01/savastan0.png)

13Feb13/02/2025

## The rise of Savastan0: a look into a growing carding marketplace

[Ylabs](https://labs.yarix.com/author/ylabs/ "Posts by Ylabs")2025-02-13T15:54:06+01:00

By
[Ylabs](https://labs.yarix.com/author/ylabs/ "Posts by Ylabs")

Reading Time:   6 minutes

# **Introduction**

Carding is a sort of fraud in which unauthorized individuals, referred to as “carders,” utilize stolen payment card information for their own benefit. This can involve not only making unlawful withdrawals and transactions, but also selling card information to other criminals in order to make money.

First of all, it is useful giving a look to carding main terminology:

* **Fullz**: it refers to a full information package which includes person’s true name, address, and complete identification (PII) such as full name, date of birth and fiscal code. This is the most valuable material, because it allows full access to online banking profiles and allows threat actors to replace the contacts of the victim with their ones.
* **Credit card dump**: digital or physical copy of a credit card. It includes data such as card number (PAN), first and last name, expiry date, CVV code.
* **AVS**: Address Verification System. It is a method that compares the billing address utilized in the transaction with the cardholder’s address issuing bank archives. Companies can use such information to decide whether to accept or cancel the order based on whether they match completely, partially, or not at all.
* **Vbiv (Input)**: term used mainly by Russian carders to enter the information gathered into payment forms. To bypass AVS checks, carders frequently try to match the card’s billing address with the address of them card stolen before using it for an online transaction.
* **PAN**: Primary Account Number, the universal standard for uniquely identifying each payment instrument. This code, typically consisting of 16 digits (in some cases 13), is assigned directly by the issuing institution according to a rigorous and structured process.
* **BIN**: Bank Identification Number: first 6 digits of the PAN. It identifies the issuing bank.

# **How are cards stolen?**

Threat actors usually use methods like:

* **Social engineering:** manipulation techniques aimed to exploit human errors.
* **Phishing/vishing scams**: scams that try to trick people into giving their cards information and login details.
* **Infostealer/spyware Malware:** malware designed to gather and steal sensitive information. Main targets are passwords for banking services, corporate VPN accesses and social media profiles.
* **Skimmers devices**, which take credit and debit card data from petrol pumps and ATMs where they have been put. **Skimmers** **can also be digital**, in form of malware that can be embedded into a website and steal data entered into payment forms. An example of digital skimming is the **Magecart** attack, named after the hacking group Magecart born in 2016 [[1]](#_ftn1); once data is stolen, criminals send payment details entered by customers to their servers, from which they can use them to conduct fraudulent purchases or sell them on the dark web.
* **Data breaches,** mainly against e-commerce platforms or payment gateway services.
* Additionally, they obtain information via buying it on **underground forums or marketplaces.**

Cards stolen are often placed on sale both on clear and dark web. Among the most famous marketplace we can quote **Brian’s Club**, **Bidencash** and **Rescator**. This Article however will focus on another market called **Savastan0**.

Depending on the quality of the information, the cost of payment card information on carding marketplaces can vary from a few dollars to several hundred dollars per card: card numbers alone are not as important as payment card leaks that include expiration dates and CVV codes. In a similar vein, high credit limit cards – like corporate, platinum, or gold cards – are worth more than ordinary cards. The price is also influenced by the card’s security features, issuing bank, and country of origin, but also by the source of the information gathered: Payment card details that were acquired via a high-profile data breach can be worth more than data obtained from lower risk methods such as phishing.

# **Savastan0.tools**

**Savastan0** is one of the leading carding markets all over the web. It is currently advertised on popular carding forums. The marketplace offers credit or debit card dumps and fullz.

According to the first screenshot below taken from a popular carding forum and posted on the 12th of October 2020, the user/group behind Savastan0 has been being active from around 2010, while the shop is online since 2019 or 2020 (the domain savastan0.biz was registered in 2019).

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x45.jpg)

*Picture 1. Screenshot of a self-promoting post of Savastan0 taken from a popular carding forum.*

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x23.jpg)

*Picture 2. Screenshot of a post about Savastan0 taken from another popular carding forum.*

The market also owns a Telegram Channel where are posted updates about the databases on sale:

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x98.jpg)

Savastan0 totally looks like a legitimate online store. Once logged in, the landing page shows the latest added bases.

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x45.jpg)

*Picture 3. Screenshot of Savastan0’s landing page.*

In the “cards” section, members can explore several ones, which can be filtered by BIN codes, country or Zip code, but also by database or check for the data included in the log.

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x41.jpg)

*Picture 4. Screenshot of  the cards search page.*

The cards catalogue appears organized in a table with this fields (may not be available for all items):

*Bin info, BankName Exp, Holder, City, State, Zip, Country, Base, extra info, buy*

To purchase a card, you just have to charge your profile with cryptocurrencies like Bitcoin or Litecoin.

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x40.jpg)

*Picture 5. Screenshot of  the wallet charging page.*

Stolen cards bought on every store must be validated, because they have a short lifespan due to the probable deactivation. Savastan0’s rules establish that a buyer only has 10 minutes to use a checker, otherwise the card cannot be refunded. Every check costs 0,30 $. Without making any transaction, card checker services may be used to “soft check” the authenticity of cards. This lowers the possibility of alerting the legitimate owner to the activity or warning anti-fraud systems. It may also be used to infer expiration dates and CVV codes, among other missing information.

In order to be accepted as a seller, you are required to submit a ticket to the staff:

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x32.jpg)

*Picture 6. Screenshot of the seller page activation*

# **Data analysis**

At the moment of the writing of this article, on the website contains more than 15 million cards on sale from all over the world.

Below are reported some ...