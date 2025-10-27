---
title: SQL INJECTIONS
url: https://infosecwriteups.com/sql-injections-b1d1da3751e5?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-02-13
fetch_date: 2025-10-04T06:27:46.580532
---

# SQL INJECTIONS

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fb1d1da3751e5&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsql-injections-b1d1da3751e5&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsql-injections-b1d1da3751e5&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-b1d1da3751e5---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-b1d1da3751e5---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# SQL INJECTIONS

[![iam_with_you11](https://miro.medium.com/v2/resize:fill:64:64/1*Azrr2HTQCrxwIIiwcJf97A.jpeg)](https://medium.com/%40kosanamharish232242?source=post_page---byline--b1d1da3751e5---------------------------------------)

[iam\_with\_you11](https://medium.com/%40kosanamharish232242?source=post_page---byline--b1d1da3751e5---------------------------------------)

5 min read

·

Jan 19, 2023

--

3

Listen

Share

Hii amigos today we are going to discuss about complete overview of SQLinjection and how to find them to earn some good bounties

**what is an SQLi vulnerability**

A SQL injection vulnerability is a weakness in a web application’s code that allows an attacker to insert malicious SQL code into a website’s input fields, such as a login form or a search bar. This can allow the attacker to gain unauthorized access to sensitive information or to manipulate the data in a database.

SQL injection vulnerabilities typically occur when a website’s code is not properly sanitized and does not validate user input. This can allow an attacker to insert malicious SQL code into a website’s input fields, which can then be executed by the database.

For example, if a website’s login form does not properly validate user input, an attacker could enter a malicious SQL statement into the form that would allow them to bypass the login process and gain unauthorized access to sensitive information.

SQL injection vulnerabilities can have serious consequences, such as the theft of sensitive information, the disruption of business operations, and damage to a company’s reputation. Therefore, it is important for web developers to take steps to prevent SQL injection attacks by validating user input, using parameterized queries, and keeping software and scripts up to date.

### classification of SQL injections

SQL injection attacks can be classified into several different types, depending on the methods used by the attacker and the impact of the attack. Some common types of SQL injection include:

=>**Classic SQL Injection**: This type of attack involves the insertion of malicious SQL code into a website’s input fields in order to gain unauthorized access to sensitive information or to manipulate the data in a database.

=>**In-band SQL Injection**: This type of attack uses the same channel for both the injection and the retrieval of data. The attacker can use the same connection to both inject the malicious code and to receive the results.

=>**Out-of-band SQL Injection**: This type of attack uses a separate channel for the injection and the retrieval of data. The attacker can use a different connection to receive the results of the injection, making it harder to detect.

=>**Blind SQL Injection**: This type of attack is used when the attacker cannot see the results of the injection. Instead, the attacker must rely on a series of True/False statements to determine if the injection was successful.

=>**Inferential SQL Injection**: This type of attack is also known as “time-based” SQL injection. The attacker can use a series of delays to infer whether the injection was successful, without being able to see the results.

=>**Union-Based SQL Injection**: This type of attack uses the UNION SQL operator to combine the results of multiple SELECT statements into a single result set. This can be used to extract data from multiple tables or to gain access to sensitive information.

=>**Stacked SQL Injection**: This type of attack uses multiple SQL statements in a single input field in order to gain unauthorized access to sensitive information or to manipulate the data in a database.

=>**Error-based SQL Injection**: This type of attack uses error messages generated by the database to gather information about the structure of the database, and then uses that information to perform the injection.

These are some common types of SQL injection, but new and advanced forms of SQL injection are constantly being developed by attackers. It is important to keep software and scripts up to date, and validate user input to prevent SQL injection attacks.

HOW to find SQLi vulnerabilities

There are several methods that can be used to find SQL injection vulnerabilities in web applications:

=>Manual testing: This method involves manually entering different inputs into a website’s input fields in order to identify any that may be vulnerable to SQL injection. This can include entering single quotes, double quotes, and special characters into input fields.

=>Automated tools: There are several automated tools, such as sqlmap and sqlninja, that can be used to scan a website for SQL injection vulnerabilities. These tools can automatically test a website’s input fields and identify any that may be vulnerable to SQL injection.

=>Application Penetration Testing: Penetration testing is a simulated cyber attack on a web application in order to identify vulnerabilities and weaknesses. Penetration testing can include both manual and automated testing methods and it can be performed by a specialized security consultant.

=>Source code review: Reviewing the source code of a web application can reveal SQL injection vulnerabilities that may not be immediately visible during manual or automated testing.

=>Network traffic analysis: Monitoring network traffic can help to identify any abnormal traffic patterns that may indicate an SQL injection attack is taking place.

Once an SQL injection vulnerability is found, it is important to report it to the website’s owner or to a bug bounty program, if it has one. The website owner or the bug bounty program will then take steps to fix the vulnerability and prevent it from being exploited in the future.

It is important to note that finding and exploiting vulnerabilities without permission is illegal and could lead to serious legal consequences. It is always recommended to disclose vulnerabilities responsibly, to the right parties and according to the vulnerability disclosure policy of the company/website

Best automated tools ...