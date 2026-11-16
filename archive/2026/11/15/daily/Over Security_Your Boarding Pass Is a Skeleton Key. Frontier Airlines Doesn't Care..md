---
title: Your Boarding Pass Is a Skeleton Key. Frontier Airlines Doesn't Care.
url: https://pentester.ca/blog/frontier-airlines-hack
source: Over Security
date: 2026-11-15
fetch_date: 2026-11-16T08:48:45.549461
---

# Your Boarding Pass Is a Skeleton Key. Frontier Airlines Doesn't Care.

[Skip to main content](#main)

[](/assets/images/Orbs/PT_Orb_LoopDark.webm)
![](/assets/images/Logos/Pentester.ca_Full_Logo_Dark.svg)

[](/assets/images/Orbs/PT_DarkPink_Orb.webm)

* Based in Tokyo,
  [E: [email protected]](/cdn-cgi/l/email-protection#22554a4b56474a43566252474c5647515647500c4143)
* Japan
  --:--:-- (GMT+9)

* [Home](/)
* [What You Get](/#what-you-get)
* [Why Hire Me?](/#why-hire-me)
* [Who Have I Helped?](/#who-helped)
* [The Feedback](/#feedback)
* [Blog](/blog)
* [Contact](#contact)

[![Pentester.ca - home](/assets/images/Logos/Pentester.ca_Full_Logo_Light.svg)](/)

[![](/assets/images/Title_Element_Black.svg)
BLOG](/blog)

# Your Boarding Pass Is a Skeleton Key. Frontier Airlines Doesn't Care.

By Kaeden | Pentester.ca | June 16, 2026

*I reported this on March 3rd, 2026. It is now June 16th. 105 days later. The critical vulnerabilities are still live. Frontier fixed the least important one and ghosted me on the rest. Your passport number is still leaking.*

## It Started With a Tweet

Someone posted their Frontier Airlines boarding pass on X. Unblurred. PNR and last name right there. But even if they'd blurred it, it wouldn't matter because the BCBP barcode on every boarding pass contains the PNR and last name in cleartext. Any barcode reader can decode it.

![Public boarding pass tweet](/assets/images/blogs/frontier/boarding_pass_tweet.png)

*A real Frontier boarding pass posted publicly on X. The original poster blacked out their name and confirmation code, but left the barcode visible. I added the pink redactions.*

Here's what most people don't know: the barcode on your boarding pass isn't just a random scanner thing. It's a BCBP (Bar Coded Boarding Pass) format defined by IATA. It contains your full name, PNR (booking confirmation code), flight details, and more, all in plaintext. Any barcode reader app on your phone can decode it in seconds. So even if you black out your name and confirmation number like this person did, the barcode gives it all away. Most people think they're being careful by hiding the text. They're not.

I wondered what you could do with just a PNR and a last name.

Turns out: everything. And I mean *everything*. Passport numbers, home addresses, credit card details, your kid's birthday. The full internal booking object, served raw like gas station sushi.

## Vulnerability 1: The Mobile API That Returns Everything

Frontier's mobile app API has an endpoint that returns the **entire raw internal booking object**. The only authentication? A PNR and a last name. That's it. That's the security. Two pieces of information printed on every boarding pass in existence.

```
https://mtier.flyfrontier.com/bookingssv/GetBookingbyParams?lastName={LAST_NAME}&recordLocator={PNR}
```

The response includes, for **every passenger on the booking** (including children):

* Full home address (street, city, state, zip)
* Email address
* Phone number
* Full date of birth (including minors)
* **Full unmasked passport number**, issuing country, and expiration date
* Nationality
* Known Traveler Number (TSA PreCheck)
* Frontier Miles / loyalty program number
* Credit card last 4 digits, BIN (first 6), expiration date, cardholder name, and billing IP address
* Full payment history with authorization codes
* Internal system comments showing every email and SMS notification sent
* Baggage tag numbers, booking agent IDs, fare breakdown
* Gender and passenger type (adult/child)

The website masks passport numbers as `XXXXX8151`. The API returns the full number. No filtering. No masking. The complete internal booking object, dumped straight to the client.

### Travel Documents (Passport Data)

![Mobile API travel document response - KTN](/assets/images/blogs/frontier/api_travel_doc_ktn.png)

*The KTN (Known Traveler Number) document. documentTypeCode "K". Full name, date of birth, gender. All in the API response.*

![Mobile API travel document response - Passport](/assets/images/blogs/frontier/api_travel_doc_passport.png)

*The passport document. documentTypeCode "P". Full passport number (redacted), nationality "IT", issued by "IT", expiration date 2034. The website masks this. The API doesn't.*

### Why the KTN Leak Matters

Your Known Traveler Number is what gives you TSA PreCheck. It's tied to your identity and lets you skip the long security line at US airports. If an attacker has your KTN, they can add it to their own booking and fraudulently gain PreCheck status, skipping enhanced security screening. You know, the screening that exists to stop bad things from happening on planes. TSA's own guidance says KTNs should be treated as sensitive and never exposed in client-side applications. Frontier dumps it in a JSON response to anyone with a 6-character code and a last name. Thanks Frontier, very cool.

### Payment Data

![Mobile API payment response](/assets/images/blogs/frontier/api_payment.png)

*Credit card details: accountNumber "XXXXXXXXXXXX7586" (last 4), expirationDate, BIN range, cardholder name, billing address including street/city/state/zip, billing email, billing IP address, authorization code, and payment amount ($609.88). All from one API call.*

The `binRange` field in the JSON is the first 6 digits of the credit card number (the Bank Identification Number). Combined with the last 4 visible in `accountNumber`, that's 10 of 16 digits known. The 16th digit is deterministic (it's a Luhn check digit, calculated from the other 15). That leaves 5 unknown digits in the middle, which is ~100,000 possible combinations. That's not a theoretical attack, that's a for-loop.

### Internal System Comments

![Mobile API internal comments](/assets/images/blogs/frontier/api_comments.png)

*Internal system comments logging every SMS and email notification sent to the passenger. "SMS Sent to [phone number]", "Email notify-gate-change sent to [email]@gmail.com". The API leaks contact info again through the notification logs even if you somehow missed it in the passenger data.*

These comments are internal system logs. They re-expose the passenger's email and phone number in plaintext, embedded in notification text strings. Even if Frontier masked the contact fields (they don't), the comments would leak them anyway. It's like putting a privacy screen on your monitor but leaving the screen mirrored to a projector in the lobby.

In the booking I tested (from a publicly posted boarding pass on X), there was a **3-year-old child** whose full name, date of birth, and gender were fully exposed.

## Vulnerability 2: The Website Leaks Your Email Too

The Manage My Booking page at `flyfrontier.com` displays your email address and phone number as masked. Great, right?

Except the full unmasked email is sitting right there in the HTML source. And it has been through **two different versions of the code**.

**How it used to leak:**

The old page had two leaks: `window._mfq` JavaScript variables and hidden  elements. Both exposed the email.

![Old email leak in JavaScript source](/assets/images/blogs/frontier/email_leak_mfq.png)

*`window._mfq.push(["setVariable", "email", "[[email protected]](/cdn-cgi/l/email-protection)"])` alongside the PNR and last name.*

![Old email leak in hidden span elements](/assets/images/blogs/frontier/email_leak_spans.png)

*`[[email protected]](/cdn-cgi/l/email-protection)` and `xxxxx`. Invisible on the page. Fully present in the source.*

**How it leaks now:**

They removed both of those. Great, right? No. They replaced them with two new leaks that expose even more data. The old version only leaked your email. The new version also leaks your phone number.

![New PII leak in JavaScript source](/assets/images/blogs/frontier/email_leak_js.png)

*`window.NOIBUJS.addCustomAttribute('EmailAddress', '[[email protected]](/cdn-cgi/l/email-protection)')` and `addCustomAttribute('PhoneNumber', 'xxxxx')`. Your email and phone number, in plaintext, in client-side JavaScript.*

And the email also appears in a **second** place in t...