---
title: Google Drive Auth Bypass: How View-Only Folder Sharing Leaked Google Form Responses ($5000 Bug)
url: https://infosecwriteups.com/google-drive-auth-bypass-how-view-only-folder-sharing-leaked-google-form-responses-5000-bug-fa99c7bbfdf4?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-18
fetch_date: 2025-10-06T23:28:40.912668
---

# Google Drive Auth Bypass: How View-Only Folder Sharing Leaked Google Form Responses ($5000 Bug)

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Ffa99c7bbfdf4&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fgoogle-drive-auth-bypass-how-view-only-folder-sharing-leaked-google-form-responses-5000-bug-fa99c7bbfdf4&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fgoogle-drive-auth-bypass-how-view-only-folder-sharing-leaked-google-form-responses-5000-bug-fa99c7bbfdf4&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-fa99c7bbfdf4---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-fa99c7bbfdf4---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# 💣 Google Drive Auth Bypass: How View-Only Folder Sharing Leaked Google Form Responses ($5000 Bug)

[![Aditya Sunny](https://miro.medium.com/v2/resize:fill:64:64/1*XcAW_t_riaR4a4fPbM4VcA.webp)](https://adityasunny06.medium.com/?source=post_page---byline--fa99c7bbfdf4---------------------------------------)

[Aditya Sunny](https://adityasunny06.medium.com/?source=post_page---byline--fa99c7bbfdf4---------------------------------------)

4 min read

·

Jul 17, 2025

--

1

Listen

Share

Author: Aditya Sunny |
Category: Bug Bounty | Google VRP | Auth Bypass

🔍 TL;DR

A simple Google Drive folder sharing misconfiguration led to a critical authorization bypass that allowed anyone with “View-only” access to download private Google Form responses. The bug, responsibly disclosed by security researcher Andrew Sirkin, earned a $5000 reward from Google under its Vulnerability Reward Program (VRP).

🧩 What Was the Vulnerability?

When a user creates a Google Form and saves it inside a shared Google Drive folder, the form responses (CSV) are internally stored alongside the form. Even when a folder is shared with view-only permissions, a user could:

Download the entire folder as a zip.

Unzip it.

Find a second zipped file containing the form’s responses.

Extract the CSV file with complete form submission data.

This essentially allowed unauthorized access to private data that was never meant to be shared.

🧪 Reproduction Steps (PoC)

The issue was fully reproducible using these steps:

1. Create a Folder on Google Drive.
2. Inside that folder:

Create a Google Form.

Create a Google Doc (just for demonstration).

3. Submit some test data into the form.
4. Share the folder link with anyone (use "Viewer" access).
5. On the recipient side:

Click “Download All” from the folder options.

This downloads a .zip file containing all files.

Inside this .zip, you’ll find another zip file: yourformname.zip.

Extract it to reveal a CSV file of form responses.

🔁 Example Test Data Used

You can test this behavior yourself using this public Google Drive folder.

⚠️ The Real-World Attack Scenario

This bug had very real implications, especially in:

Educational Institutions: Teachers sharing forms for feedback or quizzes may have unknowingly exposed student data.

HR and Recruitment: Application forms often collect resumes, phone numbers, and private responses — easily accessible via shared links.

Startups and Enterprises: Internal surveys or polls could be downloaded by unintended recipients.
Imagine a scenario where you only wanted a collaborator to view a form, but they also downloaded sensitive responses like:

Email addresses

Employee feedback

Customer complaints

Security issue reports
All without ever being explicitly granted that access.

🧠 Why Did It Happen?

This happened because of how Google Drive handles shared folders and batch downloads:

Google Drive assumes that everything in a shared folder is intended for download.

Google Forms automatically store their responses in associated .csv files.

These .csv response files are not shown in the Drive UI, but are included during a "Download All".
This breakdown in access control enforcement created a privilege escalation via zip packaging — a classic yet dangerous flaw.

💰 Google's Response and Reward

After submission to Google’s Vulnerability Reward Program (VRP), the issue was:

Acknowledged and triaged.

Marked as a security misconfiguration/auth bypass.

Assigned a bounty of $5000 to the reporter.

This is a textbook example of how even minor-seeming bugs can have major security consequences.

![]()

POC For Bounty

🔒 Lessons Learned

✅ For Google (and similar platforms):

Never assume view access to a folder equates to consent to view internal auto-generated files.

Form responses should be explicitly excluded from downloads unless access is explicitly granted.

✅ For Users:

Avoid storing forms and sensitive data in shared folders, even with “View Only” links.

Use Individual File Sharing instead of folder-level sharing when privacy matters.

Double-check what gets included in “Download All” options.

🛡️ Broader Takeaways for Bug Bounty Hunters

This bug teaches several valuable lessons for security researchers:

1. Look beyond the UI – sometimes what the user sees isn’t what the server sends.
2. Think like an attacker – what happens when a user downloads, zips, exports, or interacts in bulk?
3. Test auto-generated content – services like Google Forms, Docs, or Sheets often create background files that can leak data.
4. Revisit basic products – even trusted platforms like Google Drive still have edge cases and security bugs hiding in plain sight.

🎯 Final Thoughts

This auth bypass was elegant in its simplicity — no complex payloads, no token hijacking, no advanced exploitation. Just a zip file revealing more than it should.

Yet the impact could have been massive.

The best vulnerabilities are often hidden in the mundane. Google’s Drive + Forms system is something billions of users trust every day, and this case is a powerful reminder that convenience should never override access control.

Kudos to Andrew Sirkin for the discovery — and hats off to Google for handling it responsibly.

🤝 If You Liked This...

Follow me on Medium for more deep dives into real-world vulnerabilities, bug bounty wins, and practical cybersecurity knowledge.

[Yeswehack](https://medium.com/u/b8ebb8852210?source=post_page---user_mention--fa99c7bbfdf4---------------------------------------)

[Artificial Intelligence](https://medium.com/tag/artificial-intelligence?source=post_page-----fa99c7bbfdf4---------------------------------------)

[Technology](https://medium.com/tag/technology?source=post_page-----fa99c7bbfdf4---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----fa99c7bbfdf4--------...