---
title: Attack Techniques: Priming Attacks on Legitimate Sites
url: https://textslashplain.com/2023/01/11/attack-techniques-priming-attacks-on-legitimate-sites/
source: text/plain
date: 2023-01-12
fetch_date: 2025-10-04T03:39:33.492679
---

# Attack Techniques: Priming Attacks on Legitimate Sites

[Skip to content](#content)

[text/plain](https://textslashplain.com/)

ericlaw talks about security, the web, and software in general

# Attack Techniques: Priming Attacks on Legitimate Sites

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2023-01-112025-09-08](https://textslashplain.com/2023/01/11/attack-techniques-priming-attacks-on-legitimate-sites/)Posted in[security](https://textslashplain.com/category/security/), [web](https://textslashplain.com/category/tech/web/)Tags:[InfoSecTTP](https://textslashplain.com/tag/infosecttp/), [phishing](https://textslashplain.com/tag/phishing/), [security](https://textslashplain.com/tag/security/)

Earlier today, we looked at [two](https://textslashplain.com/2023/01/11/attack-techniques-phishing-via-local-files/) [techniques](https://textslashplain.com/2023/01/11/attack-techniques-phishing-via-mailto/) for attackers to evade anti-phishing filters by using lures that are not served from `http` and `https` urls that are subject to reputation analysis.

A third [attack technique](https://textslashplain.com/tag/InfoSecTTP) is to send a lure that entices a user to visit a *legitimate* site and perform an *unsafe operation* on that site. In such an attack, the phisher never collects the user’s password directly, and because the brunt of the attack occurs while on the legitimate site, anti-phishing filters typically have no way to block the attacks. I will present three examples of such attacks in this post.

### “Consent Phishing”

In the first example, the attacker sends their target an email containing lure text that entices the user to click a link in the email:

[![](https://textslashplain.com/wp-content/uploads/2023/01/image-24.png?w=659)](https://textslashplain.com/wp-content/uploads/2023/01/image-24.png)

The attacker controls the text of the email and can thus *prime* the user to make an unsafe decision on the legitimate site, which the attacker does not control. In this case, clicking the link brings the victim to an account configuration page. *If* the user is prompted for credentials when clicking the link, the credentials are collected on the legitimate site (not a phishing URL), so anti-phishing filters have nothing to block.

The attacker has very limited control over the contents of the account config page, but thanks to priming, the user is likely to make a bad decision, unknowingly granting the attacker access to the content of their account:

[![](https://textslashplain.com/wp-content/uploads/2023/01/image.png?w=472)](https://textslashplain.com/wp-content/uploads/2023/01/image.png)

A malicious app whose OAuth prompt shows a misleading name (“Outlook Mail”) and icon

If access is granted, the attacker has the ability to act “as the user” when it comes to their email. Beyond sensitive content within the user’s email account, most sites offer password recovery options bound to an email address, and after compromising the user’s email account the attacker can likely *pivot* to attack their credentials on other sites.

This technique isn’t limited to Microsoft accounts, as demonstrated by this [similar attack](https://blog.sekoia.io/targeted-supply-chain-attack-against-chrome-browser-extensions/) against Google:

[![](https://textslashplain.com/wp-content/uploads/2023/01/image-54.png?w=1024)](https://textslashplain.com/wp-content/uploads/2023/01/image-54.png)

… and this recent [campaign against users of Salesforce](https://techcommunity.microsoft.com/blog/MicrosoftThreatProtectionBlog/protect-against-oauth-attacks-in-salesforce-with-microsoft-defender/4450584).

### “Invoice Scam”

A second example is a [long-running attack via sites like PayPal](https://textslashplain.com/2024/06/05/attack-techniques-paypal-invoice-scams/). PayPal allows people to send requests for money to one another, with content controlled by the attacker. In this case, the lure is sent *by PayPal* itself. As you can see, Outlook even notes that “*This message is from a trusted sender*” without the important caveat that the email *also* contains untrusted and inaccurate content authored by a malicious party.

[![](https://textslashplain.com/wp-content/uploads/2023/01/image-25.png?w=1024)](https://textslashplain.com/wp-content/uploads/2023/01/image-25.png)

A victim encountering this email may respond in one of two ways. First, they might pick up the phone and call the phone number provided by the attacker, and the attack would then continue via telephone– because the attack is now “offline”, [anti-phishing filters will not get in the way](https://textslashplain.com/2023/02/09/attack-techniques-blended-attacks-via-phone/).

Alternatively, a victim encountering the email might click on the link, which brings them to the legitimate PayPal website. Anti-phishing filters have nothing to say here, since the victim has been directed to the legitimate site (albeit with dangerous parameters). Perhaps alarmingly, PayPal has decided to “reduce friction” and automatically trust devices you’ve previously used, meaning that users might not even prompted for a password when clicking through the link:

[![](https://textslashplain.com/wp-content/uploads/2023/01/image-26.png?w=600)](https://textslashplain.com/wp-content/uploads/2023/01/image-26.png)

Misleading trust indicators and the desire for simple transactions mean that a user is just clicks away from losing hundreds of dollars to an attacker.

### “Malicious Extensions”

In the final example of a priming attack, a malicious website can trick the user into installing a malicious browser extension. This is often positioned as a [security check](https://twitter.com/ericlaw/status/1369026682926039043), and often uses [assorted](https://twitter.com/ericlaw/status/1185172184848916480/) [trickery](https://twitter.com/ericlaw/status/1196555928381902850) to try to prevent the user from recognizing what’s happening, including sizing and positioning the Web Store window in ways to try to obscure important information. Google explicitly bans such conduct in their policy:

[![](https://textslashplain.com/wp-content/uploads/2023/01/image-27.png?w=944)](https://textslashplain.com/wp-content/uploads/2023/01/image-27.png)

… but technical enforcement is more challenging.

Because the extension is hosted and delivered by the “official” web store, the browser’s security restrictions and anti-malware filters are not triggered.

After a victim installs a malicious browser extension, the extension can hijack their searches, spam notifications, steal personal information, or embark upon other attacks until such time as the extension is recognized as malicious by the store and nuked from orbit.

### Best Practices

When building web experiences, it’s important that you consider the effect of priming — an attacker can structure lures to confuse a user and potentially misunderstand a choice offered by your website. Any flow that offers the user a security choice should have a simple and unambiguous option for users to report “*I think I’m being scammed*“, allowing you to take action against abuse of your service and protect your customers.

If you’re an Entra administrator, you can configure your tenant to restrict individual users from granting consent to applications:

[![](https://textslashplain.com/wp-content/uploads/2023/01/image-55.png?w=1024)](https://textslashplain.com/wp-content/uploads/2023/01/image-55.png)

-Eric

### Share this:

* [Click to share on X (Opens in new window)
  X](https://textslashplain.com/2023/01/11/attack-techniques-priming-attacks-on-legitimate-sites/?share=twitter)
* [Click to share on Facebook (Opens in new window)
  Facebook](https://textslashplain.com/2023/01/11/attack-techniques-priming-attacks-on-legitimate-sites/?share=facebook)

Like Loading...

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2023-01-112025-09-08](https://textslashplain.com/2023/01/11/attack-techniques-priming-attacks-on-legitimate-sites/)Posted in[security](https://text...