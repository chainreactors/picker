---
title: Lovense: The Company That Lies to Security Researchers
url: https://bobdahacker.com/blog/lovense-still-leaking-user-emails
source: Over Security
date: 2026-11-02
fetch_date: 2026-11-03T08:51:35.696318
---

# Lovense: The Company That Lies to Security Researchers

[bobdahacker](/)

☰

* [home](/)
* [blog](/blog)

# Lovense: The Company That Lies to Security Researchers

July 28, 2025

BobDaHacker

*This post has been updated multiple times. BOTH critical vulnerabilities were finally fixed on July 30, 2025 - but only after public pressure forced their hand. The email disclosure they claimed would take 14 months to fix? Fixed in 2 days. The account takeover vulnerability first reported in 2023? Also suddenly fixed after 2 years of lies. This went viral and within 48 hours, they miraculously found solutions to "impossible" problems. Lovense knew about the XMPP email bug since 2017 (Pentest Partners reported it - 8 years ago!). OSINT sites were actively exploiting these vulnerabilities. See all updates below for the full story of Lovense's negligence, lies, and how public exposure accomplished what years of responsible disclosure couldn't. After reading this, I highly recommend watching Mental Outlaw's video (linked at the end of the blogpost) on the subject. You should read this first though as there are some things in here not covered in his video that I added later.*

## What Happened

So it all started when I was using the Lovense app and muted someone. That's it. Just muted them. But then I saw the API request and was like... wait, is that an email address? Why is that there?

![Initial Discovery](/static/images/blogs/lovense/lovense_my_ex.png)
*Just muting someone exposed their email - wtf*

After digging deeper, I figured out how to turn any username into their email address.

So we had two big problems:

1. **Email Disclosure** - Any username could be turned into their email address
2. **Account Takeover** - Make auth tokens with just an email, no password needed

## How Bad Was It?

### The Email Thing

The email disclosure vulnerability was surprisingly straightforward once you understood the flow. Here's exactly how it worked:

**The Attack Steps:**

1. **Get a GToken with encryption parameters:**

   * Make a POST request to `/api/wear/genGtoken` with your account credentials
   * This returns a gtoken and encryption keys (x and y parameters)
2. **Look up any username:**

   * Take any Lovense username you want to get the email for
   * Encrypt the username using AES-CBC with the keys from step 1
   * Send POST request to `/app/ajaxCheckEmailOrUserIdRegisted?email={encrypted_username}`
   * Include your gtoken and X parameter in headers
3. **Get the encrypted user data:**

   * The API returns encrypted user information including a fake email
   * Decrypt the response using the same AES-CBC keys
4. **Extract the real email through XMPP manipulation:**

   * Connect to Lovense's XMPP server using your account
   * Take the fake email from step 3's API response and convert it to XMPP JID format (@ replaced by !!!, add \_w suffix)
   * Example: `cfc561791785b996b989593402dc41a8!!!lovense.remote.email_w@im.lovense.com`
   * Add this fake JID as a contact to your XMPP roster
   * Send a presence subscription request to that JID
   * Fetch your roster - this returns both the fake JID you added AND the user's actual JID with their real email
   * Example real JID: `[[email protected]](/cdn-cgi/l/email-protection)` (which reveals the real email: [[email protected]](/cdn-cgi/l/email-protection#542c2d2e31223514263d273121247a3a3120))
   * The XMPP server links them by ofId, so you can match and extract the real email
   * Remove the contact to clean up

The whole process took maybe 30 seconds per username manually, with the script we made though to automate it, it took less than 1 second for a username to be converted to an email. We could have easily harvested emails from any public username list. This is especially bad for cam models who share their usernames publicly but obviously don't want their personal emails exposed.

### Taking Over Accounts

While Eva and I were checking out the Lovense Connect app later, we found something even worse (Eva did most of the work) - it was making gtokens (auth tokens) without ever asking for a password. Just an email was enough.
![haha yes](/static/images/blogs/lovense/lovense_@everyone_takeover.png)

**The Attack Steps:**

1. **Get the target's email** - Either from the email disclosure bug or if you already know it (later on we discovered after Krissy came forwards this endpoint worked with usernames too.)
2. **Set up the request parameters:**
   * `userName`: The target's email or username
   * `userType`: "0"
   * `pf`: "connect-pc" (platform)
   * `ver`: "1.7.9" (version)
3. **Generate the signature:**
   * Create an MD5 hash of: `{platform}-#-{version}-#-{email}##0`
   * Append timestamp: `{md5hash}-#-{timestamp}`
4. **Encrypt the signature** using AES-CBC with:
   * Key: The app's hardcoded appId (`a79643e665bb9833`)
   * IV: The app's hardcoded appSecret (`2DF65319C4D46284`)
5. **Send POST request** to `https://apps.lovense-api.com/api/connect/genGtoken`
6. **Get back a valid gtoken** - No password needed!

These tokens worked on:

* Lovense Extension
* Lovense Connect
* StreamMaster
* Cam101 (through the login link)
* Even admin accounts

Cam models use these tools for work, so this was a huge deal. Literally anyone could take over any account just by knowing the email address.

## The Timeline (Get Ready for This)

**March 26, 2025**: We reported both bugs to Lovense with help from Internet of Dongs.

**March 26, 2025**: They said they're looking at it.

**March 27, 2025**: They confirmed the bugs exist and they're working on fixes.

**March 28, 2025**: We also put both bugs on HackerOne.

**April 8, 2025**: On HackerOne:

* Email bug: They said it's "already known and fixed in new version" (not released yet). Paid $1,000 total.
* Account takeover: They downgraded it from critical to high saying it "doesn't involve database access." Also paid $1,000.

**April 9, 2025**: After we explained you can literally take over ANY account including admins, they finally made it critical and added $2,000.

**May 30, 2025**: We told them nothing was fixed.

**June 4, 2025**: This is where it gets insane. They said:

1. Account takeover was "fixed on April 7" (it wasn't)
2. For the email leak, here's a snippet from their email:

   > "Following your report, we conducted a thorough investigation and rolled out initial mitigation steps, including a temporary fix for the script path issue you identified. However, resolving the root cause involves deeper architectural work. We've launched a long-term remediation plan that will take approximately ten months, with at least four more months required to fully implement a complete solution. We also evaluated a faster, one-month fix. However, it would require forcing all users to upgrade immediately, which would disrupt support for legacy versions. We've decided against this approach in favor of a more stable and user-friendly solution."

   Read that again. They wanted **14 MONTHS** to fix it. They could fix it in 1 month but won't because "legacy versions"

**June 14, 2025**: We sent them a long email saying:

* Account takeover still works
* 14 months is insane
* Just make people update their apps
* Or use a proxy to hide emails without breaking old apps

We suggested they just proxy the XMPP stuff. It would hide emails without breaking anything, work with old apps, and be quick to implement. They said they'd do it but ignored the idea completely.

The technical reality is messy - their entire XMPP architecture relies on JIDs (Jabber IDs) that directly contain user emails. These JIDs are probably used everywhere: message routing, contact lists, presence status, group chats, device pairing. When your core identifier system exposes the exact data you need to protect, you've got a fundamental architectural problem.

Fixing it properly means touching every part of their chat system - updating databases, rewriting message routing logic, migrating existing contacts and chat histories, and ensuring all their apps can handle the new format....