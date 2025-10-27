---
title: Behind the Attack: Account Takeover (ATO)
url: https://buaq.net/go-158901.html
source: unSafe.sh - 不安全
date: 2023-04-17
fetch_date: 2025-10-04T11:31:38.583567
---

# Behind the Attack: Account Takeover (ATO)

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/3b12f281249d741cb5a3b6decc704d47.jpg)

Behind the Attack: Account Takeover (ATO)

Account takeovers (ATO), a form of cyber attack where unauthorized individuals gain access to a
*2023-4-16 20:8:35
Author: [perception-point.io(查看原文)](/jump-158901.htm)
阅读量:25
收藏*

---

Account takeovers (ATO), a form of cyber attack where unauthorized individuals gain access to a user’s account, have been prevalent for over two decades. With the increasing dependence on digital services and online transactions, the frequency of such attacks has only risen in recent years. [Research](https://tech.co/news/adult-account-takeover-fraud#:~:text=Considering%20the%20average%20cost%20of,in%20the%20last%20year%20alone.) has shown that the average cost of an account takeover, including impact and recovery costs, is approximately $12,000. Furthermore, the number of account takeover attacks has increased substantially in 2022 and is projected to only further grow in 2023.

In this blog we will delve into the kill chain of a compromised mailbox, tracing the steps from the initial phishing delivery to setting up inbox rules with deletion logic, and ultimately delivering malicious payloads to known contacts. Read on to learn more.

## Step 1: Building The Phish

To gain access to a victim’s mailbox, an attacker typically needs to obtain the victim’s credentials. In the vast majority of cases, this begins with a mass phishing campaign initiated by the attacker. In rare instances, the attacker may acquire the credentials through information leakage or via malware that sends the data to their command-and-control center (C2).

Unfortunately, launching a phishing attack has become relatively straightforward. Attackers can typically generate a list of potential victims within minutes, create a phishing template (often impersonating a Microsoft or Google login page), and set up an email server to deliver the phishing emails. With this accomplished, the attacker can proceed to the next step.

## Step 2: Going Phishing

The next step for the attacker is to construct a convincing phishing email and send it to the list of recipients they generated earlier. The email must be well-crafted to increase the likelihood that users will be tricked into clicking on the malicious link.

Typical phishing email subjects often contain language such as:

* Direct ACH Deposit Processed
* Expired Password
* Action Required
* Notification Alert
* Missed Voice Message
* New Fax Received
* Mail Server Quota Full
* Email Delivery Failure
* Reactivate Your Account

By using these types of subject lines, the attacker hopes to entice the user to open the email and take the desired action, such as clicking on a link or entering login credentials.

![](https://lh5.googleusercontent.com/nX2Y0DBB9IxbkIi5FksZFt0vXq5uUKykWKHB1YPHYOVaheImQnyhcPCsdSWv5Fm1AYCkKmM4KIJuyOtViH8wh6wyj_e-PRBPNATzJL9xlD8ntUu2ejmautPkfWIWTGk8GSXqVDna5fnPiLoMWk8Lvg)

Figure 2: Common Phishing Template (March 2023)

Phishing email templates are becoming increasingly sophisticated. Attackers are now utilizing AI tools to generate templates that are nearly identical to the service they are impersonating, further increasing the likelihood that the recipient will fall for the scam.

[*For more information about the impact of AI in cyber attacks and defense, check out this blog!*](https://perception-point.io/blog/ai-the-double-edged-sword-of-cybersecurity/)

## Steps 3 to 5: Stealing Credentials

Since the steps involved in phishing attacks are well-known within the cybersecurity industry, we will not discuss them further in this blog post. Instead, we invite you to explore our other blog posts that delve deeper into the technical aspects of phishing:

[7 Ways to Prevent Phishing and Advanced Anti-Phishing Techniques](https://perception-point.io/guides/phishing/how-to-prevent-phishing-attacks/)

[How to Conduct a Phishing Attack in 5 Easy Steps](https://perception-point.io/blog/how-to-conduct-a-phishing-attack-5-easy-steps/)

## Step 6: Inside the Victim’s Mailbox

After gaining access to the victim’s mailbox, the attacker has limited time to extract sensitive data before being detected or locked out. At the same time, the attacker must establish rules that will help them execute the attack.

But how can you detect suspicious mailbox access before the attack progresses further? Microsoft’s audit logs can provide valuable insight into potential ATO events. Key properties to consider include:

* **Subject**: This refers to the subject line of the message that was accessed. If you discover access to subjects with words like “Password,” “Account,” “Invoice,” “Deposit,” or “Payment” appearing consecutively, it’s a strong indication that the attacker is seeking sensitive data.
* **Operation**: This property describes the operation performed by a user. In ATO events, common operations include “Set-InboxRule,” “New-InboxRule,” “Set-Mailbox,” and “New-InboxRuleForwardTo.” Attackers often use these operations to delete, conceal, or forward emails out of the organization.
* **ClientIP**: This refers to the IP address from which the login took place. Unknown or unauthorized IP addresses could suggest an ATO event.
* **LoginStatus**: A high number of failed logins followed by a successful login can indicate a brute force attack. Microsoft also includes a lockout event that occurs after a certain number of unsuccessful login attempts.
* **UserAgent**: This property contains data on the OS and browser used by the user to sign in. Therefore, if an organization is operating in a Linux environment with Edge and you discover a login from MacOS and Chrome, it’s something to watch for closely.

## Step 7: These Are the (Inbox & Forwarding) Rules

Once the attacker has gathered the necessary information, they often create rules to help them carry out the attack. These rules usually involve either forwarding emails outside the organization or defining inbox rules. While forwarding rules are less common due to organization policies for data loss prevention (DLP) purposes, inbox rules are extremely prevalent in ATO cases.

Before launching a malicious attack, the attacker defines rules with deletion actions to avoid detection. The rules’ logic varies according to the type of attack they plan to launch. Here is an example of a malicious rule we recently encountered:

![](https://lh5.googleusercontent.com/xKnxWUid0_yBA_IvrfQtTZgmjeOMyjvTyBx0HLfoUi_M6nUJc1iNQJVUVMDsKHNfsqls659R09IO62qnKemfxbpExATQJS8DSQfZRn7jE3qYW2FEyhv01XU7b7HjfXU25lzhzWDujXmsz5gu1nOemQ)

Figure 3: ATO Inbox Rule

In this case, there were a few indicators of malicious intent, including:

1. **Name**:  A suspicious name such as “ddd”, as opposed to default names like “Move all emails from XXXX to YYYY”.
2. **Mark as read**: The rule marks all incoming emails that match the logic as read.
3. **Delete message**: The rule deletes all incoming emails that match the logic.
4. **Content-based value**: Here, the attacker used the property of searching for words in the email’s subject or body.

Breaking down the logic, we can see that the attacker is deleting all messages that contain the words [“Incomparable Incentives Awareness – Planning 2022;spam;hack;email;virus;delivery;undeliverable;failure;out of office;scam”].

Typically, attackers define rules that delete bounce-back messages. This is necessary, as a compromised mailbox is often used for mass delivery of malicious emails, resulting in many bounce-back and auto-reply messages returning to the mailbox. By creating this rule, the compromised user won’t know about the ongoing campaign.

R...