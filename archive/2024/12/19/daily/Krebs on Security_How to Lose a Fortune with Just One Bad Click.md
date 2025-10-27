---
title: How to Lose a Fortune with Just One Bad Click
url: https://krebsonsecurity.com/2024/12/how-to-lose-a-fortune-with-just-one-bad-click/
source: Krebs on Security
date: 2024-12-19
fetch_date: 2025-10-06T19:48:20.880405
---

# How to Lose a Fortune with Just One Bad Click

Advertisement

[![](/b-knowbe4/36.jpg)](https://www.knowbe4.com/resources/kits/cybersecurity-awareness-month?utm_source=Krebs&utm_medium=display&utm_campaign=cybersecurityawarenessmonth&utm_content=hrm+)

Advertisement

[![](/b-action1/2.jpg)](https://action1.com/double-endpoints-free-cam2025/?utm_source=paidmedia&refid=Display_CAM_Krebs)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# How to Lose a Fortune with Just One Bad Click

December 18, 2024

[75 Comments](https://krebsonsecurity.com/2024/12/how-to-lose-a-fortune-with-just-one-bad-click/#comments)

![](https://krebsonsecurity.com/wp-content/uploads/2024/12/thumb-mobile.png)

**Adam Griffin** is still in disbelief over how quickly he was robbed of nearly $500,000 in cryptocurrencies. A scammer called using a real **Google** phone number to warn his Gmail account was being hacked, sent email security alerts directly from google.com, and ultimately seized control over the account by convincing him to click “yes” to a Google prompt on his mobile device.

Griffin is a battalion chief firefighter in the Seattle area, and on May 6 he received a call from someone claiming they were from Google support saying his account was being accessed from Germany. A Google search on the phone number calling him — **(650) 203-0000** — revealed it was an official number for [Google Assistant](https://en.wikipedia.org/wiki/Google_Assistant), an AI-based service that can engage in two-way conversations.

At the same time, he received an email that came from a google.com email address, warning his Google account was compromised. The message included a “Google Support Case ID number” and information about the Google representative supposedly talking to him on the phone, stating the rep’s name as “Ashton”— the same name given by the caller.

Griffin didn’t learn this until much later, but the email he received had a real google.com address because it was sent via [Google Forms](https://en.wikipedia.org/wiki/Google_Forms), a service available to all **Google Docs** users that makes it easy to send surveys, quizzes and other communications.

![](https://krebsonsecurity.com/wp-content/uploads/2024/12/gsid19472345.png)

A phony security alert Griffin received prior to his bitcoin heist, via Google Forms.

According to tripwire.com’s **Graham Cluely**, phishers will use Google Forms to create a security alert message, and then change the form’s settings to automatically send a copy of the completed form to any email address entered into the form. The attacker then sends an invitation to complete the form to themselves, not to their intended victim.

“So, the attacker receives the invitation to fill out the form – and when they complete it, they enter their intended victim’s email address into the form, not their own,” Cluely [wrote in a December 2023 post](https://www.tripwire.com/state-of-security/google-forms-used-call-back-phishing-scam). “The attackers are taking advantage of the fact that the emails are being sent out directly by Google Forms (from the google.com domain). It’s an established legitimate domain that helps to make the email look more legitimate and is less likely to be intercepted en route by email-filtering solutions.”

The fake Google representative was polite, patient, professional and reassuring. Ashton told Griffin he was going to receive a notification that would allow him to regain control of the account from the hackers. Sure enough, a Google prompt instantly appeared on his phone asking, “Is it you trying to recover your account?”

![](https://krebsonsecurity.com/wp-content/uploads/2024/12/griffin-gar.png)

Adam Griffin clicked “yes,” to an account recovery notification similar to this one on May 6.

Griffin said that after receiving the pop-up prompt from Google on his phone, he felt more at ease that he really was talking to someone at Google. In reality, the thieves caused the alert to appear on his phone merely by stepping through Google’s account recovery process for Griffin’s Gmail address.

“As soon as I clicked yes, I gave them access to my Gmail, which was synched to **Google Photos**,” Griffin said.

Unfortunately for Griffin, years ago he used Google Photos to store an image of the secret seed phrase that was protecting his cryptocurrency wallet. Armed with that phrase, the phishers could drain all of his funds.

“From there they were able to transfer approximately $450,000 out of my Exodus wallet,” Griffin recalled.

Griffin said just minutes after giving away access to his Gmail account he received a call from someone claiming to be with Coinbase, who likewise told him someone in Germany was trying to take over his account.

Griffin said a follow-up investigation revealed the attackers had used his Gmail account to gain access to his Coinbase account from a VPN connection in California, providing the multi-factor code from his Google Authenticator app. Unbeknownst to him at the time, Google Authenticator by default also makes the same codes available in one’s Google account online.

But when the thieves tried to move $100,000 worth of cryptocurrency out of his account, Coinbase sent an email stating that the account had been locked, and that he would have to submit additional verification documents before he could do anything with it.

## GRAND THEFT AUTOMATED

Just days after Griffin was robbed, a scammer impersonating Google managed to phish 45 bitcoins — approximately $4,725,000 at today’s value — from **Tony**, a 42-year-old professional from northern California. Tony agreed to speak about his harrowing experience on condition that his last name not be used.

Tony got into bitcoin back in 2013 and has been investing in it ever since. On the evening of May 15, 2024, Tony was putting his three- and one-year-old boys to bed when he received a message from Google about an account security issue, followed by a phone call from a “Daniel Alexander” at Google who said his account was compromised by hackers.

Tony said he had just signed up for Google’s **Gemini AI** (an artificial intelligence platform formerly known as “Bard”), and mistakenly believed the call was part of that service. Daniel told Tony his account was being accessed by someone in Frankfurt, Germany, and that he could evict the hacker and recover access to the account by clicking “yes” to the prompt that Google was going to send to his phone.

The Google prompt arrived seconds later. And to his everlasting regret, Tony clicked the “Yes, it’s me” button.

Then came another call, this one allegedly from security personnel at **Trezor**, a company that makes encrypted hardware devices made to store cryptocurrency seed phrases securely offline. The caller said someone had submitted a request to Trezor to close his account, and they forwarded Tony a message sent from his Gmail account that included his name, Social Security number, date of birth, address, phone number and email address.

Tony said he began to believe then that his Trezor account truly was compromised. The caller convinced him to “recover” his account by entering his cryptocurrency seed phrase at a phishing website (**verify-trezor[.]io**) that mimicked the official Trezor website.

“At this point I go into fight or flight mode,” Tony recalled. “I’ve got my kids crying, my wife is like what the heck is going on? My brain went haywire. I put my seed phrase into a phishing site, and that was it.”

Almost immediately, all of the funds he was planning to save for retirement and for his children’s college fund were drained from his account.

“I made mistakes due to being so busy and not thinking correctly,” Tony told KrebsOnSecurity. “I had gotten so far away fr...