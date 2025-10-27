---
title: Bypassing Door Passwords
url: https://infosecwriteups.com/bypassing-door-passwords-4004b8d7995?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-07-10
fetch_date: 2025-10-04T11:52:43.426279
---

# Bypassing Door Passwords

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F4004b8d7995&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbypassing-door-passwords-4004b8d7995&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbypassing-door-passwords-4004b8d7995&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-4004b8d7995---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-4004b8d7995---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Bypassing Door Passwords

[![sockpuppets](https://miro.medium.com/v2/resize:fill:64:64/1*UwhozTdVkFbnBAweIAVcvQ.png)](https://sockpuppets.medium.com/?source=post_page---byline--4004b8d7995---------------------------------------)

[sockpuppets](https://sockpuppets.medium.com/?source=post_page---byline--4004b8d7995---------------------------------------)

3 min read

·

Jan 7, 2022

--

Listen

Share

Instead of a key, this type of lock system requires a numerical code to grant entry to a facility or property. The code is punched in by users via a numerical pad, similar to those on a basic calculator. If the correct code is entered, the door lock or deadbolt should release. Some mechanisms require batteries or a small electrical current to unlock.

Some keypad locks have an integrated security feature that keeps the door locked for a set amount of time (usually 10 to 15 minutes) after several incorrect attempts to enter the code.

The purpose of this research is to understand how insecure we live.

![]()

Audio Smart Lock

## Most Popular Entry Door Keypads in Turkey

1. Perkotek
2. ERD-1120
3. Efes Digital Panel
4. Mas
5. AC 13PX
6. Burg Wachter
7. DIP40
8. Lorex LR-DPH2
9. M100
10. MB05–03
11. MB DYF40
12. MLŞ 14–70
13. MLŞ 14–107
14. MRA 101
15. Netalsan Obsidian
16. ONDRIVE ED07
17. OP705
18. OP M400
19. OP M500
20. Pratik Kart
21. Desi Steely
22. Audio
23. Teknoline
24. Teknoline IMR18
25. Desi UTOPIC
26. WL02
27. D45
28. A20 Kapı Kilidi

## Most Used Default Passwords

1. #0000
2. 0000
3. 0411#
4. 0571
5. #0789
6. 0880#
7. 1014
8. 1111
9. 1200#
10. #1234
11. \*\*1234
12. 1234
13. 1234#
14. 1357#
15. 1453
16. 1629#
17. 1881
18. 1979/
19. \*1992#
20. 2000
21. 2013
22. 2020
23. 2020#
24. \*\*2510
25. 2707#
26. 2828
27. 3263
28. 4050#
29. 4233#
30. 4570#
31. 5555
32. 5656#
33. 5689#
34. 5757
35. 6161
36. \*\*6565
37. \*\*6771
38. 7305
39. \*\*7788
40. #7889
41. \*\*7890
42. 8182#
43. #8888#
44. 88888888
45. 8988#
46. 9575
47. 991453
48. 991903
49. 992211
50. 992525
51. 998877
52. C12341234
53. c2638
54. C6161

## Real Life Tests

I try the admin password on “Audio Şifreli Kapı Kiliti” and it is successful. Now we can change all user’s passwords, close the alarm, delete all users.

Press enter or click to view image in full size

![]()

Also, we don’t need to know the passwords, we can reset the admin password using some simple steps.

* Push the reset button behind the box for 10 seconds.
* Unplug the DT-8 socket and wait for 5 seconds and plug.
* After 10 seconds passed, stop the pressing button and unplug the socket again at the same time.
* After that, you can use default admin password :)

## Statistics

Until now, I try 3 Audio Door Locks and all of them have default passwords (including the admin password). You can contribute the statistics.

**Contact me :** aydinnyunus@gmail.com

Press enter or click to view image in full size

![]()

## Github Repository for Default Passwords

Enter the ID for getting information about the Model.

<https://github.com/aydinnyunus/gateCracker-REST>

![]()

## Demo

<https://aydinnyunus-gatecracker-main-y5wdmi.streamlit.app/>

Press enter or click to view image in full size

![]()

## Source Code

<https://github.com/aydinnyunus/gateCracker-REST>

<https://github.com/aydinnyunus/gateCracker>

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----4004b8d7995---------------------------------------)

[Security](https://medium.com/tag/security?source=post_page-----4004b8d7995---------------------------------------)

[Infosec](https://medium.com/tag/infosec?source=post_page-----4004b8d7995---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----4004b8d7995---------------------------------------)

[Siber Guvenlik](https://medium.com/tag/siber-guvenlik?source=post_page-----4004b8d7995---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--4004b8d7995---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--4004b8d7995---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--4004b8d7995---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--4004b8d7995---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--4004b8d7995---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![sockpuppets](https://miro.medium.com/v2/resize:fill:96:96/1*UwhozTdVkFbnBAweIAVcvQ.png)](https://sockpuppets.medium.com/?source=post_page---post_author_info--4004b8d7995---------------------------------------)

[![sockpuppets](https://miro.medium.com/v2/resize:fill:128:128/1*UwhozTdVkFbnBAweIAVcvQ.png)](https://sockpuppets.medium.com/?source=post_page---post_author_info--4004b8d7995---------------------------------------)

[## Written by sockpuppets](https://sockpuppets.medium.com/?source=post_page---post_author_info--4004b8d7995---------------------------------------)

[186 followers](https://sockpuppets.medium.com/followers?source=post_page---post_author_info--4004b8d7995---------------------------------------)

·[10 following](https://medium.com/%40sockpuppets/following?source=post_page---post_author_info--4004b8d7995---------------------------------------)

## No response...