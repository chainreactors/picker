---
title: Defensive Technology: Ransomware Data Recovery
url: https://textslashplain.com/2025/11/19/defensive-technology-ransomware-data-recovery/
source: text/plain
date: 2025-11-19
fetch_date: 2025-11-20T03:08:44.061934
---

# Defensive Technology: Ransomware Data Recovery

[Skip to content](#content)

[text/plain](https://textslashplain.com/)

ericlaw talks about security, the web, and software in general

# Defensive Technology: Ransomware Data Recovery

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2025-11-192025-11-19](https://textslashplain.com/2025/11/19/defensive-technology-ransomware-data-recovery/)Posted in[security](https://textslashplain.com/category/security/)Tags:[Defender](https://textslashplain.com/tag/defender/), [security](https://textslashplain.com/tag/security/), [Windows](https://textslashplain.com/tag/windows/)

In a prior installment we looked at [Controlled Folder Access](https://textslashplain.com/2024/11/15/defensive-technology-controlled-folder-access/), a Windows feature designed to hamper ransomware attacks by preventing untrusted processes from modifying files in certain user folders. In today’s post, we look at the other feature on the **Ransomware protection** page of the [Windows Security Center App](https://learn.microsoft.com/en-us/windows/security/operating-system-security/system-security/windows-defender-security-center/windows-defender-security-center) — **Ransomware data recovery**.

### User-Interface

The UI of the feature is simple and reflects the state of your cloud file provider (if any) which for most folks will be OneDrive. Depending on whether OneDrive is enabled, and what kind of account you have, you’ll see one of the following four sets of details:

[![](https://textslashplain.com/wp-content/uploads/2025/11/onedriveransom-1.png?w=949)](https://textslashplain.com/wp-content/uploads/2025/11/onedriveransom-1.png)

Windows 11 Ransomware data recovery feature status

### What’s it do?

Conceptually, this whole feature is super-simple.

Ransomware works by encrypting your files with a secret key and holding that key for ransom. If you have a backup of your files, you can simply restore the files without paying the bad guys.

However, for backup to work well as a ransomware recovery method, you need

1. to ensure that your backup processes don’t overwrite the legitimate files with the encrypted versions, and
2. to easily recognize which files were modified by ransomware to replace them with their latest uncorrupted version.

The mechanism of this feature is quite simple: If Defender recognizes a ransomware attack is underway, it battles the ransomware (killing its processes, etc) and also notifies your cloud file provider of the timestamp of the detected infection. Internally, we’ve called this a **shoulder tap**, as if we tapped the backup software on the shoulder and said “*Uh, hang on, this device is infected right now.*“

This notice serves two purposes:

1. To allow the file backup provider to pause backups until given an “all clear” (remediation complete) notification, and
2. To allow the file backup provider to determine which files may have been corrupted from the start of the infection so that it can restore their backups.

Simple, right?

-Eric

#### Appendix: Extensibility

As far as I can tell, this feature represents *semi-public* interface that allows 3P security software and cloud backup software to integrate with the Windows Security Center. `OnDataCorruptionMalwareFoundNotification` and `OnRemediationNotification`. Unfortunately, the documentation isn’t public — I suspect it’s only available to members of the [Microsoft Virus Initiative](https://learn.microsoft.com/en-us/unified-secops/virus-initiative-criteria) program for AV partners.

### Share this:

* [Click to share on X (Opens in new window)
  X](https://textslashplain.com/2025/11/19/defensive-technology-ransomware-data-recovery/?share=twitter)
* [Click to share on Facebook (Opens in new window)
  Facebook](https://textslashplain.com/2025/11/19/defensive-technology-ransomware-data-recovery/?share=facebook)

Like Loading...

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2025-11-192025-11-19](https://textslashplain.com/2025/11/19/defensive-technology-ransomware-data-recovery/)Posted in[security](https://textslashplain.com/category/security/)Tags:[Defender](https://textslashplain.com/tag/defender/), [security](https://textslashplain.com/tag/security/), [Windows](https://textslashplain.com/tag/windows/)

## Published by ericlaw

Impatient optimist. Dad. Author/speaker. Created Fiddler & SlickRun. PM @ Microsoft 2001-2012, and 2018-, working on Office, IE, and Edge. Now working on Microsoft Defender. My words are my own, I do not speak for any other entity. [View more posts](https://textslashplain.com/author/ericlaw1979/)

## Post navigation

[Previous Post Previous post:
Windows Shell Previews – Restricted](https://textslashplain.com/2025/10/20/windows-shell-previews/)

### Leave a comment [Cancel reply](/2025/11/19/defensive-technology-ransomware-data-recovery/#respond)

Δ

## Search Text/Plain

Search for:

## Pages

* [About](https://textslashplain.com/about/)
* [Browse All Posts](https://textslashplain.com/browse-all-posts/)
* [Categories](https://textslashplain.com/categories/)
* [Cruises](https://textslashplain.com/cruises/)
* [IEInternals Archive](https://textslashplain.com/ieinternals-archive/)
* [Real-World Races](https://textslashplain.com/races/)

## RSS

[![RSS Feed](https://textslashplain.com/i/rss/orange-small.png)](https://textslashplain.com/feed/ "Subscribe to Posts") [RSS - Posts](https://textslashplain.com/feed/ "Subscribe to Posts")

## Blog Stats

* 2,415,150 hits

## Categories

Categories
Select Category
bluebadge  (16)
books  (3)
browsers  (183)
design  (21)
dev  (84)
fiddler  (25)
life  (52)
perf  (20)
politics  (2)
privacy  (26)
reviews  (2)
running  (18)
security  (160)
storytelling  (47)
tech  (35)
travel  (9)
Uncategorized  (16)
web  (151)
windmills  (12)

![ericlaw](https://2.gravatar.com/avatar/89c27d27b73dd3690b3dad59f3a539d1?s=320)

#### [ericlaw](https://gravatar.com/ericlaw1979)

Impatient optimist. Dad. Author/speaker. Created Fiddler & SlickRun. PM @ Microsoft 2001-2012, and 2018-, working on Office, IE, and Edge. Now working on Microsoft Defender. My words are my own, I do not speak for any other entity.

[View Full Profile →](https://gravatar.com/ericlaw1979)

[text/plain](https://textslashplain.com/),
[A WordPress.com Website](https://wordpress.com/?ref=footer_custom_acom).

* [Comment](https://textslashplain.com/2025/11/19/defensive-technology-ransomware-data-recovery/#respond)
* Reblog
* Subscribe
  Subscribed

  + [![](https://secure.gravatar.com/blavatar/82d40d311a11c0cfe6d128d043693048c9216bb5abceef9296346a9b262f3f95?s=50&d=https%3A%2F%2Fs2.wp.com%2Fi%2Flogo%2Fwpcom-gray-white.png) text/plain](https://textslashplain.com)

  Join 265 other subscribers

  Sign me up

  + Already have a WordPress.com account? [Log in now.](https://wordpress.com/log-in?redirect_to=https%3A%2F%2Fr-login.wordpress.com%2Fremote-login.php%3Faction%3Dlink%26back%3Dhttps%253A%252F%252Ftextslashplain.com%252F2025%252F11%252F19%252Fdefensive-technology-ransomware-data-recovery%252F)
* + [![](https://secure.gravatar.com/blavatar/82d40d311a11c0cfe6d128d043693048c9216bb5abceef9296346a9b262f3f95?s=50&d=https%3A%2F%2Fs2.wp.com%2Fi%2Flogo%2Fwpcom-gray-white.png) text/plain](https://textslashplain.com)
  + Subscribe
    Subscribed
  + [Sign up](https://wordpress.com/start/)
  + [Log in](https://wordpress.com/log-in?redirect_to=https%3A%2F%2Fr-login.wordpress.com%2Fremote-login.php%3Faction%3Dlink%26back%3Dhttps%253A%252F%252Ftextslashplain.com%252F2025%252F11%252F19%252Fdefensive-technology-ransomware-data-recovery%252F)
  + [Copy shortlink](https://wp.me/p60i9o-3za)
  + [Report this content](https://wordpress.com/abuse/?report_url=https://textslashplain.com/2025/11/19/defensive-technology-ransomware-data-recovery/)
  + [View post in Reader](https://wordpress.com/reader/blogs/88727790/posts/13712)
  + [Manage subscriptions](https://subscribe.wordpress.com/)
  + Collapse this bar

##

##

Loading Comments...

Write a Comment...

Email (Required)

Name (Requi...