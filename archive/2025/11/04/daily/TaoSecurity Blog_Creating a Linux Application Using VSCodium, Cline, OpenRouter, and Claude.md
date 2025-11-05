---
title: Creating a Linux Application Using VSCodium, Cline, OpenRouter, and Claude
url: https://taosecurity.blogspot.com/2025/11/creating-linux-application-using.html
source: TaoSecurity Blog
date: 2025-11-04
fetch_date: 2025-11-05T03:12:54.785338
---

# Creating a Linux Application Using VSCodium, Cline, OpenRouter, and Claude

[Skip to main content](#main)

### Search This Blog

# [TaoSecurity Blog](https://taosecurity.blogspot.com/)

Richard Bejtlich's blog on digital security, strategic thought, and military history.

### Creating a Linux Application Using VSCodium, Cline, OpenRouter, and Claude

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

[November 03, 2025](https://taosecurity.blogspot.com/2025/11/creating-linux-application-using.html "permanent link")

In March I created a [Windows Application Using Visual Studio Code, Cline, OpenRouter, and Claude](https://taosecurity.blogspot.com/2025/03/creating-windows-application-using.html).
This was a program that created square screen captures. The user
doesn't need to manually ensure the dimensions are a square. The program
makes the window grow and shrink while keeping the length equal to the
height.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguCCVz3lbVrU6Ct1ejGqTaQgicYRU_e4E6SLCwbHJEHr5In8w5ou-hEdTwOSUu_RE2VOXnnzFwsitCoYmSlRLhvsGeybOx9WbhhLoP6zEikI_E4IRXylyvvVl1RA11ea8rVGwqPGVl4wUSOgjX1PTO5IVTwBBieLXNLwbBn6hyphenhyphenxQfazMlc2-RtRXpkxtSm/w640-h640/BejSnap-20251103001.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguCCVz3lbVrU6Ct1ejGqTaQgicYRU_e4E6SLCwbHJEHr5In8w5ou-hEdTwOSUu_RE2VOXnnzFwsitCoYmSlRLhvsGeybOx9WbhhLoP6zEikI_E4IRXylyvvVl1RA11ea8rVGwqPGVl4wUSOgjX1PTO5IVTwBBieLXNLwbBn6hyphenhyphenxQfazMlc2-RtRXpkxtSm/s2100/BejSnap-20251103001.png)

In June I created an equivalent program on Linux using VSCodium, Cline, OpenRouter, and Claude.

I provided this prompt, which I derived from the last project.

==

Create a graphical Linux application to take screen captures with the following features:

Square Region Selection: Enforces a 1:1 aspect ratio during region selection

1:1 Aspect Ratio: Ensures all captures are perfectly square

PNG Output: Saves high-quality images in PNG format

Preview: Shows the captured image before saving

Dark Mode by Default: Toggle to light theme if desired

Square Interface: The application window itself uses a square ratio

Default Save Location: Set a preferred folder for saving captures

Automatic File Naming: Uses format "BejCap-YYYYMMDD###" for organized file management

I prefer C++ with Qt.

For shortcuts use Ctrl+S to Save the current image and Esc to Cancel region selection (when in region selection mode).

I do not want to capture to clipboard.

==

I also supplied these guidelines:

Always test the project at the end to ensure it doesn't contain errors.

Don't create placeholder code unless you plan to expand on it later.

Code from A to Z rather than just small parts that don't fulfill the user's needs.

Keep project files between 300-500 lines where possible.

Don't duplicate code. Build upon existing implementations.

==

I had to install the following to enable the program development:

**sudo apt install build-essential cmake qtbase5-dev qt5-qmake qtbase5-dev-tools**

The development seemed much faster than my last project, and the result works very well.

If you'd like to try it on Linux, you can access it here: <https://github.com/taosecurity/BejSnap>.

[linux](https://taosecurity.blogspot.com/search/label/linux)
[vibecoding](https://taosecurity.blogspot.com/search/label/vibecoding)

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

### Comments

[Post a Comment](https://www.blogger.com/comment/fullpage/post/4088979/5484172568637501696)

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

I've completed the TaoSecurity Blog book series . The new book is  The Best of TaoSecurity Blog, Volume 4: Beyond the Blog with Articles, Testimony, and Scholarship .  It's available now for Kindle , and I'm working on the print edition.  I'm running a 50% off promo on Volumes 1-3 on Kindle through midnight 20 April. Take advantage before the prices go back up. I described the new title thus: Go beyond TaoSecurity Blog with this new volume from author Richard Bejtlich. In the first three volumes of the series, Mr. Bejtlich selected and republished the very best entries from 18 years of writing and over 18 million blog views, along with commentaries and additional material.  In this title, Mr. Bejtlich collects material that has not been published elsewhere, including articles that are no longer available or are stored in assorted digital or physical archives. Volume 4 offers early white papers that Mr. Bejtlich wrote as a network defender, either for technica...

[Read more](https://taosecur...