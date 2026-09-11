---
title: The Phishing Email Was Actually From Google, but Should I Trust It?
url: https://toooold.com/2026/09/10/fake_google_call.html
source: Toooold
date: 2026-09-10
fetch_date: 2026-09-11T06:51:44.182528
---

# The Phishing Email Was Actually From Google, but Should I Trust It?

[Toooold](/)
[ ]

[Make a CatGPT out of ChatGPT](/2023-02-02-cat_laser_chatgpt.html)[About](/about.html)

# The Phishing Email Was Actually From Google, but Should I Trust It?

Sep 10, 2026

Last night I received one of the more interesting phishing attacks I have seen personally. I work as an AI researcher at a cybersecurity company, so after a few steps I became more interested in studying the attack than following the caller’s instructions. Still, I can easily see how this could succeed against someone who is distracted, worried about losing an important Gmail account, or simply trying to cooperate with what appears to be Google’s security team.

The most interesting part was that several things I saw on my phone were genuinely produced by Google. The account recovery prompt was real. The verification request was real. The later security email also came through Google’s infrastructure.

The attacker was exploiting the meaning I would assign to those legitimate messages.

I would describe this technique as **trusted-channel laundering**. An attacker deliberately triggers legitimate security mechanisms from a trusted service, then uses a phone call or another social channel to provide a false explanation of what those mechanisms mean. Instead of constructing a convincing imitation of Google, the attacker gets Google to produce much of the convincing material.

![Fake Google Call](/images/fake_google_call.jpg)

There is an important defense that makes this particular attack much easier to stop. Google’s own current security guidance says very clearly:

> “Google will never call you about your account security.”

Google also says it will never call and ask you to read a verification code or approve a device prompt. Even messages from legitimate Google domains should not be interpreted as proof that a caller represents Google.

That simple rule turns out to be extremely relevant to what happened.

## Step 1: “Google” calls me

At around 8 PM Pacific time, I received a call from:

**650-215-XXXX**

The caller ID displayed **Google**.

The person said that someone had recently changed the contact phone number associated with my Gmail account. He told me that Google’s Trust and Safety team would contact me shortly to help secure the account.

A few minutes later, another call arrived from:

**347-329-XXXX**

This time a man speaking fluent English said he worked for Google’s security team. He explained that somebody had changed the contact information on my Gmail account and that he needed to verify my identity and help me recover it.

I am including both phone numbers because they were the numbers displayed during this incident and may be useful to someone searching for the same scam.

They should not be treated as durable identities for the attackers.

Caller ID names and numbers can be spoofed. A scammer can make a call appear to originate from a different number and can manipulate the displayed caller name. Even if these particular numbers were controlled by the attackers during my call, they can switch numbers at any time. Carriers may block them, Google may take action if its name is being abused, and the numbers themselves may later be reassigned.

So the useful indicator here is:

**These were the numbers used in this incident.**

The stronger security signal is the behavior that followed.

The timing also felt strange. It was around 8 PM in California and 11 PM in New York. More importantly, I had never asked Google for support.

### Why did they use two calls?

The first call established the story before the second caller asked me to do anything sensitive.

By the time the supposed Google security engineer appeared, I had already been told that there was an account incident and that another Google employee would contact me.

The second call therefore arrived as an expected event.

That sequencing matters. The attacker was creating context first, then asking for authorization.

## Step 2: They made Google send me a real recovery prompt

While “Google Security” was talking to me, my Gmail app displayed a Google account recovery notification.

A device in New York was attempting to recover my account.

That was a real Google prompt.

The caller immediately explained that this was expected because he was working on my recovery case. He told me to click **Yes** because the New York device belonged to the Google security process he had just initiated.

This is where the attack became much more interesting.

Google prompts can be used during account recovery. If Google sees an unusual sign-in or recovery attempt, the prompt can contain information such as the device and approximate location so that the account owner can reject an attempt they did not initiate.

The attacker had triggered exactly the warning that was supposed to protect me, then used the phone call to reinterpret it.

The notification was effectively asking:

> Someone in New York is trying to recover this account. Is that you?

The caller’s explanation was:

> Yes, that is me in New York helping you recover your account.

The same event now had two possible meanings, and the security outcome depended on which explanation I believed.

### Why did they use Google’s own recovery prompt?

Because a genuine Google notification carries much more credibility than a fake webpage or a phishing email.

Once the victim accepts the premise that the person on the phone represents Google, suspicious information inside the notification can start working in the attacker’s favor.

The location **New York** could have warned me that somebody elsewhere was trying to access my account.

Under the attacker’s explanation, it became evidence that the supposed Google security engineer was doing exactly what he had promised.

That is the core pattern of this attack.

## Step 3: “Please enter my job ID, 48”

Then came my favorite part of the attack.

The caller told me that his **Google employee ID was 48** and instructed me to use `48` in the authentication prompt.

Of course, `48` was functioning as part of Google’s authentication challenge.

Google can use number matching as part of an authentication flow. A number displayed during one part of the transaction must correspond to the trusted device authorizing it.

The attacker gave the number a new meaning.

The security system was effectively saying:

> Verify that this authentication session is the one you intended to authorize.

The caller told me:

> This is my Google employee ID. Enter 48 to verify that I am helping you.

That is a subtle and effective semantic substitution.

For the victim, typing `48` feels almost harmless. There is no password being disclosed, no long OTP being read aloud, and no suspicious website being opened.

It sounds like entering an employee identifier into Google’s own application.

### Why did they call 48 an “employee ID”?

People have been trained for years not to share passwords or verification codes.

A two-digit employee ID feels very different.

The attacker did not need to hide the authentication token. He changed the victim’s understanding of what the token represented.

This is one of the most interesting parts of the attack from a security-design perspective.

I refused to enter it.

## Step 4: When the first path failed, they pivoted

After I questioned the first request, the caller immediately changed approaches.

An unfamiliar Gmail account:

**{something with letters and numbers}@gmail.com**

attempted to establish a recovery relationship involving my email address. Google then sent me another legitimate request related to that recovery process.

There was another verification code involved, and the caller wanted me to provide or confirm it.

Again, I refused.

I am including the Gmail address because it was directly involved in this incident and may help other people identify the same campaign.

Like the phone numbers, however, this email address should be treated as a temporary incident indicator rather than...