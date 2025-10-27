---
title: Passkeys for Normal People
url: https://www.troyhunt.com/passkeys-for-normal-people/
source: Troy Hunt's Blog
date: 2025-05-06
fetch_date: 2025-10-06T22:34:48.505560
---

# Passkeys for Normal People

* [Home](https://www.troyhunt.com/)
* [Workshops](https://www.troyhunt.com/workshops/)
* [Speaking](https://www.troyhunt.com/speaking/)
* [Media](https://www.troyhunt.com/media/)
* [About](https://www.troyhunt.com/about/)
* [Contact](https://www.troyhunt.com/contact/)
* [Sponsor](https://www.troyhunt.com/sponsorship/)

**Sponsored by:**

# Passkeys for Normal People

05 May 2025

Let me start by very simply explaining the problem we're trying to solve with passkeys. Imagine you're logging on to a website like this:

![](https://www.troyhunt.com/content/images/2025/03/image-28.png)

And, because you want to protect your account from being logged into by someone else who may obtain your username and password, you've turned on two-factor authentication (2FA). That means that even after entering the correct credentials in the screen above, you're now prompted to enter the six-digit code from your authenticator app:

![](https://www.troyhunt.com/content/images/2025/03/image-29.png)

There are a few different authenticator apps out there, but what they all have in common is that they display a one-time password (henceforth referred to as an OTP) with a countdown timer next to it:

![](https://www.troyhunt.com/content/images/2025/03/image-30.png)

By only being valid for a short period of time, if someone else obtains the OTP then they have a *very* short window in which it's valid. Besides, who can possibly obtain it from your authenticator app anyway?! Well... that's where the problem lies, and I demonstrated this just recently, not intentionally, but rather entirely by accident when [I fell victim to a phishing attack](https://www.troyhunt.com/a-sneaky-phish-just-grabbed-my-mailchimp-mailing-list/). Here's how it worked:

![](https://www.troyhunt.com/content/images/2025/05/troy-phish-1.jpg)

1. I was socially engineered into visiting a phishing page that pretended to belong to Mailchimp who I use to send newsletters for this blog. The website address was mailchimp-sso.com, which was close enough to the real address (mailchimp.com) to be feasible. "SSO" is "single sign on", so also seemed feasible.
2. When I saw the login screen (the one with the big "PHISH" stamp on it), and submitted my username and password to them, the phishing site then automatically used those credentials to begin the login process on Mailchimp.
3. Mailchimp validated the credentials, and because I had 2FA turned on, then displayed the OTP request screen.
4. The legitimate OTP screen from Mailchimp was then returned to the bad guys...
5. ...who responded to my login request with *their own page* requesting the OTP.
6. I entered the code into the form and submitted it to the phishing site.
7. The bad guys then immediately sent that request to Mailchimp, thus successfully logging *themselves* in.

The problem with OTPs from authenticator apps (or sent via SMS) is that they're phishable in that it's possible for someone to trick you into handing one over. What we need instead is a "phishing-resistant" paradigm, and that's precisely what passkeys are. Let's look at how to set them up, how to use them on websites and in mobile apps, and talk about what some of their shortcomings are.

### Passkeys for Log In on Mobile with WhatsApp

We'll start by setting one up for WhatsApp given I got a friendly prompt from them to do this recently:

![](https://www.troyhunt.com/content/images/2025/03/image-31.png)

So, let's "Try it" and walk through the mechanics of what it means to setup a passkey. I'm using an iPhone, and this is the screen I'm first presented with:

![](https://www.troyhunt.com/content/images/2025/03/image-32.png)

A passkey is simply a digital file you store on your device. It has various cryptographic protections in the way it is created and then used to login, but that goes beyond the scope of what I want to explain to the audience in this blog post. Let's touch briefly on the three items WhatsApp describes above:

1. The passkey will be used to logon to the service
2. It works in conjunction with how you already authenticate to your device
3. It needs to be stored somewhere (remember, it's a digital file)

That last point can be very device-specific and very user-specific. Because I have an iPhone, WhatsApp is suggesting I save the passkey into my iCloud Keychain. If you have an Android, you're obviously going to see a different message that aligns to how Google syncs passkeys. Choosing one of these native options is your path of least resistance - a couple of clicks and you're done. However...

I have lots of other services I want to use passkeys on, and I want to authenticate to them both from my iPhone and my Windows PC. For example, I use LinkedIn across all my devices, so I don't want my passkey tied solely to my iPhone. (It's a bit clunky, but some services enable this by using the mobile device your passkey is on to scan a QR code displayed on a web page). And what if one day I switch from iPhone to Android? I'd like my passkeys to be more transferable, so I'm going to store them in my dedicated password manager, [1Password](https://1password.com/?ref=troyhunt.com).

A quick side note: as you'll read in this post, passkeys do not necessarily replace passwords. Sometimes they can be used as a "single factor" (the only thing you use to login with), but they may also be used as a "second factor" with the first being your password. This is up to the service implementing them, and one of the criticisms of passkeys is that your experience with them will differ between websites.

We still need passwords, we still want them to be strong and unique, therefore we still need password managers. [I've been using 1Password for 14 years now](https://www.troyhunt.com/only-secure-password-is-one-you-cant/) (full disclosure: they sponsor [Have I Been Pwned](https://haveibeenpwned.com/?ref=troyhunt.com), and often sponsor this blog too) and as well as storing passwords (and credit cards and passport info and secure notes and sharing it all with my family), they can also store passkeys. I have 1Password installed on my iPhone and set as [the default app to autofill passwords and passkeys](https://support.apple.com/en-au/guide/iphone/iphf9219d8c9/ios?ref=troyhunt.com):

![](https://www.troyhunt.com/content/images/2025/04/image-1.png)

Because of this, I'm given the option to store my WhatsApp passkey directly there:

![](https://www.troyhunt.com/content/images/2025/03/image-33.png)

The obfuscated section is the last four digits of my phone number. Let's "Continue", and then 1Password pops up with a "Save" button:

![](https://www.troyhunt.com/content/images/2025/03/image-35.png)

Once saved, WhatsApp displays the passkey that is now saved against my account:

![](https://www.troyhunt.com/content/images/2025/03/image-36.png)

And because I saved it into 1Password that syncs across all my devices, I can jump over to the PC and see it there too.

![](https://www.troyhunt.com/content/images/2025/03/image-38.png)

And that's it, I now have a passkey for WhatsApp which can be used to log in. I picked this example as a starting point given the massive breadth of the platform and the fact I was literally just prompted to create a passkey (the very day my Mailchimp account was phished, ironically). Only thing is, I genuinely can't see how to *log out* of WhatsApp so I can then test using the passkey to login. Let's go and create another with a different service and see how that experience differs.

### Passkeys For Log In via PC with LinkedIn

Let's pick another example, and we'll set this one up on my PC. I'm going to pick a service that contains some important personal information, which would be damaging if it were taken over. In this case, the service has also previously suffered a data breach themselves: LinkedIn.

I already had two-step verification enabled on LinkedIn, but as evidenced in my own phishing experience, this isn't always enough. (Note: the terms "two-step", "two-factor" and "m...