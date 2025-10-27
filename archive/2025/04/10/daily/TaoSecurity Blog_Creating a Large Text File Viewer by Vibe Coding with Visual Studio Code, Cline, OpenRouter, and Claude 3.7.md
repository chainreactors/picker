---
title: Creating a Large Text File Viewer by Vibe Coding with Visual Studio Code, Cline, OpenRouter, and Claude 3.7
url: https://taosecurity.blogspot.com/2025/04/creating-large-text-file-viewer-by-vibe.html
source: TaoSecurity Blog
date: 2025-04-10
fetch_date: 2025-10-06T22:08:11.717537
---

# Creating a Large Text File Viewer by Vibe Coding with Visual Studio Code, Cline, OpenRouter, and Claude 3.7

[Skip to main content](#main)

### Search This Blog

# [TaoSecurity Blog](https://taosecurity.blogspot.com/)

Richard Bejtlich's blog on digital security, strategic thought, and military history.

### Creating a Large Text File Viewer by Vibe Coding with Visual Studio Code, Cline, OpenRouter, and Claude 3.7

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

[April 09, 2025](https://taosecurity.blogspot.com/2025/04/creating-large-text-file-viewer-by-vibe.html "permanent link")

I just created another Windows 10/11 application using AI. This is a follow-up to the [SquareCap program I posted about a few weeks ago](https://taosecurity.blogspot.com/2025/03/creating-windows-application-using.html).

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhj99wkC1UeCsdDK6dQJSjXu6q9XY_vKGKbag0bHQo72hs7SoTAfCpUIYQqMEhTL_TVwp7a8h1aMEl_NMCzG5MV5CcrREOteeLFYO6_cDhemM2Q3_OuZbx2l1KyUofFWnMGexOiDvlH-aC-MlARuWmnTnKcuSVygKGdyPUziNKB67zSL92sjiHw/w640-h640/SquareCap-20250409023%20bejview%20for%2026%20GB%20file.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhj99wkC1UeCsdDK6dQJSjXu6q9XY_vKGKbag0bHQo72hs7SoTAfCpUIYQqMEhTL_TVwp7a8h1aMEl_NMCzG5MV5CcrREOteeLFYO6_cDhemM2Q3_OuZbx2l1KyUofFWnMGexOiDvlH-aC-MlARuWmnTnKcuSVygKGdyPUziNKB67zSL92sjiHw/s2091/SquareCap-20250409023%20bejview%20for%2026%20GB%20file.png)

The problem I was trying to solve this time was opening and searching extremely large text files.

I used to use the old Mandiant Highlighter program for this, but it was last updated in 2011 and couldn't handle the 26 GB text file I wanted to open.

If you're wondering what that file is, it's a dump of the contents of the main Starfield.esm file from the Bethesda Game Studios game called Starfield. I use the xdump64 program bundled with xEdit.

You can try this program for yourself if you like. It's a stand-alone Windows C# .NET 9 application that runs on Windows 10 and 11.

Like my last program, all I did was work with the model for about 3 hours to get it to where it is now.

I tried for an hour or so to implement a "highlight all search matches" function but could not get that to work.

The screen capture cuts of the right side of the page where the search and match feature lives.

You can download the .exe from GitHub at <https://github.com/taosecurity/BejView>.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgRbAeYd-m-yHOUaeeJGWzgt_uPglrWAFE7sK9sr48CCHprPtvF2IgiGR2ZeCAbOU51jTVyEb8iF7Pkyt74SCH4mXz_uPBUKo5-WM1DkwUhJqby0bWtmz1A7YyZENTRB_TONvUwAKoE3Z6p56tQRuS-WzSoNF_yArso_MqcN1eSL7pIjsxg28rB/w640-h640/SquareCap-20250409025%20github.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgRbAeYd-m-yHOUaeeJGWzgt_uPglrWAFE7sK9sr48CCHprPtvF2IgiGR2ZeCAbOU51jTVyEb8iF7Pkyt74SCH4mXz_uPBUKo5-WM1DkwUhJqby0bWtmz1A7YyZENTRB_TONvUwAKoE3Z6p56tQRuS-WzSoNF_yArso_MqcN1eSL7pIjsxg28rB/s1905/SquareCap-20250409025%20github.png)

Windows will probably complain because it is not signed.

As with my last program, I have no idea of code quality or vulnerabilities. This was a fun exercise to see if I could create a program that would address a problem I was working.

[ai](https://taosecurity.blogspot.com/search/label/ai)
[github](https://taosecurity.blogspot.com/search/label/github)
[vibecoding](https://taosecurity.blogspot.com/search/label/vibecoding)

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

### Comments

[Post a Comment](https://www.blogger.com/comment/fullpage/post/4088979/2830801047918158256)

### Popular posts from this blog

### [Zeek in Action Videos](https://taosecurity.blogspot.com/2021/07/zeek-in-action-videos.html)

[July 29, 2021](https://taosecurity.blogspot.com/2021/07/zeek-in-action-videos.html "permanent link")

[![Image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhcWFyS3aGQrT6UiiiBbLkOiUs5W_Y9cYMLeH2Z7KkzzqINSWjFIEG8inSUNbYNGTjF7dcEUOOOkK7DzHQXcNMY3Nhl1PIFsdZZeJOH7bzRzpQMUdez5M7_g3t_xyygra49FBKK/w640-h360/capture_001_29072021_143006.jpg)](https://taosecurity.blogspot.com/2021/07/zeek-in-action-videos.html)

This is a quick note to point blog readers to my Zeek in Action YouTube video series for the Zeek network security monitoring project .  Each video addresses a topic that I think might be of interest to people trying to understand their network using Zeek and adjacent tools and approaches, like Suricata, Wireshark, and so on.  I am especially pleased with Video 6 on monitoring wireless networks . It took me several weeks to research material for this video. I had to buy new hardware and experiment with a Linux distro that I had not used before -- Parrot .  Please like and subscribe, and let me know if there is a topic you think might make a good video.

[Read more](https://taosecurity.blogspot.com/2021/07/zeek-in-action-videos.html "Zeek in Action Videos")

### [MITRE ATT&CK Tactics Are Not Tactics](https://taosecurity.blogspot.com/2020/10/mitre-att-tactics-are-not-tactics.html)

[October 23, 2020](https://taosecurity.blogspot.com/2020/10/mitre-att-tactics-are-not-tactics.html "permanent link")

[![Image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgh8UtkHOxII5KLGuTgeVk3iVj3KMfkoFLyDb11MrasYGQ9J2Q5NPBgNUX4-Dk5YKF_26s2quTQ_ve4bEh4yIF1H97CJeNqoGqlpAATJPzThQ_IGALsANV3MZLlF_zogZNHM-LI/s320/on+tactics.jpg)](https://taosecurity.blogspot.com/2020/10/mitre-att-tactics-are-not-tactics.html)

Just what are "tactics"? Introduction MITRE ATT&CK  is a great resource, but something about it has bothered me since I first heard about it several years ago. It's a minor point, but I wanted to document it in case it confuses anyone else. The MITRE ATT&CK Design and Philosophy document from March 2020 says the following: At a high-level, ATT&CK is a behavioral model that consists of the following core components: • Tactics, denoting short-term, tactical adversary goals during an attack; • Techniques, describing the means by which adversaries achieve tactical goals; • Sub-techniques, describing more specific means by which adversaries achieve tactical goals at a lower level than techniques; and • Documented adversary usage of techniques, their procedures, and other metadata. My concern is with MITRE's definition of "tactics" as "short-term, tactical adversary goals during an attack," which is oddly recursive. The key word in the tacti...

[Read more](https://taosecurity.blogspot.com/2020/10/mitre-att-tactics-are-not-tactics.html "MITRE ATT&CK Tactics Are Not Tactics")

### [New Book! The Best of TaoSecurity Blog, Volume 4](https://taosecurity.blogspot.com/2021/04/new-book-best-of-taosecurity-blog.html)

[April 13, 2021](https://taosecurity.blogspot.com/2021/04/new-book-best-of-taosecurity-blog.html "permanent link")

[![Image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhe6YF9WJiKp0uULA6gH7y4zgy_L4W5xkOUmCV3fENBessbRL3bdnf6xy2y-uWNS1ScWWzyQ5qBL56XVyeknUtWhFk29Ol6pGst3H78RCAT2c53h7VCq4bU00BGhRhXRygZs8kZ/w400-h640/The+Best+of+TaoSecurity+Blog%252C+Volume+4.jpg)](https://taosecurity.blogspot.com/2021/04/new-book-best-of-taosecurity-blog.html)

I've completed the TaoSecurity Blog book series . The new book is  The Best of TaoSecurity Blog, Volume 4: Beyond the Blog with Articles, Testimony, and Scholarship .  It's available now for Kindle , and I'm working on the print edition.  I'm running a 50% off promo on Volumes 1-3 on Kindle through midnight 20 April. Take advantage before the prices go back up. I described the new title thus: Go beyond TaoSecurity Blog with this new volume from author Richard Bejtlich. In the first three volumes of the series, Mr. Bejtlich selected and republished the very best entries from 18 years of writing and over 18 million blog views, along with commentaries and additional material.  In this title, Mr. Bejtlich collects material that has not been published elsewhere, including articles that are no longer available or are stored in assorted digital or physical archives. Volume 4 offers early white papers that Mr. Bejtlich wrote as a network de...