---
title: Gone in a Click: IDOR Vulnerabilities in Image Upload Function
url: https://buaq.net/go-175115.html
source: unSafe.sh - 不安全
date: 2023-08-23
fetch_date: 2025-10-04T11:58:45.304275
---

# Gone in a Click: IDOR Vulnerabilities in Image Upload Function

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/30f3353eccedcd1997c3f61bc84cccd0.jpg)

Gone in a Click: IDOR Vulnerabilities in Image Upload Function

Greetings, fellow cybersecurity researchers! I’m Rootxyash, a passionate security researcher and an
*2023-8-22 22:50:35
Author: [infosecwriteups.com(查看原文)](/jump-175115.htm)
阅读量:22
收藏*

---

[![rootxy4sh](https://miro.medium.com/v2/resize:fill:88:88/1*Nj7jv67m35lAfqpB8aVnyA.png)](https://medium.com/%40rootxyash?source=post_page-----6c4817b44d8c--------------------------------)[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:48:48/1*A6LVtmXcJ3QJy_sdCyFx1Q.png)](https://infosecwriteups.com/?source=post_page-----6c4817b44d8c--------------------------------)

Greetings, fellow cybersecurity researchers! I’m Rootxyash, a passionate security researcher and an unwavering part-time bug bounty hunter. So this marks my third writeup of bug bounty since I embarked on this thrilling journey of bug bounty in 2022. As time passes, 2023 proves to be a bit more demanding for me with ongoing studies in Engineering, but rest assured, whenever a fleeting moment of time allows I love to discover vulnerabilities for fun and profit & to make the digital world more secure.

So let’s start with our story, So what is IDOR?

Let’s see one example, considering there are two users in an application i.e. User A and User B. User-A is having a unique profile ID of 1000 and User B is having a profile ID of 1002.

In a normal scenario user A will only have access to his own profile with ID 1000 and user B will only have access to his own profile with ID 1002. But here if user A changed the profile ID to User B’s ID 1002, user A can able to access the profile of User B. This is due to Broken Access Control And Insecure Direct Object Reference. This is just a normal scenario stating small info about IDOR.

Mostly I do hunting on weekends so while hunting on one program let’s consider the program as a redacted.com so while hunting on a platform within a three hours I got 3–4 IDOR vulnerabilities with full account takeover (Regarding account takeover I will write about it later in detail). Let’s see how was the approach in discovering it, so after creating the account I started looking for vulnerabilities while going through the website features and functionalities.

I found various other issues like XSS, password reset poisoning, business logic flaws, etc. After some time, I thought, why not check JavaScript files? So I instantly inspected the page and began searching for JS files. After some time, I found one JS file having some interesting things.

As you can see the following JavaScript code is responsible for handling the “*deletion of image” &* “*displaying the* *current profile image of the user*” using the dropzone.js library, as well as interacting with a server using AJAX requests. There is one interesting line `/image/delete/66` it means if the file was newly uploaded it sends an AJAX request to delete the file on the server using the URL `/image/delete/66` (with `66` being the user's ID). I went to the profile section & instantly captured the preview request of an image in Burpsuite.

Displaying Existing Profile Image of User 40

I changed the request from `/get_profile_img/40`to `/image/delete/39` for 39 User and sent the request.

> And as you can see I was successfully able to delete the profile image of the 39th user which means now I can delete the image of any user present on the platform just by changing the user ID. I can easily do that using the intruder in Burpsuite.

So, this was the first IDOR for the “*preview current image & image deletion endpoint*”.

After this, I thought why not check the image upload endpoint as well and try to abuse it? I instantly went to the image upload endpoint and captured the request by uploading an image for the user with ID 40.

Request of ID 40

I changed the request from `/image_upload/40`to `/image_upload/39` for 39th user and sent the request.

Request after changing ID from 40 > 39

> And, as you can see, I was successfully able to change the profile image of the 39th user. This means that I can now change the image of any user present on the platform by replacing the ID.

After reporting these two issues I still tried to abuse the image upload functionality and found one more vulnerable endpoint.

When we upload any image on the platform, it takes seconds of time to upload, and we can even cancel the uploading of the image within that time frame.

I tried to capture the request for this endpoint and thought that this one could also be exploitable. And yes, it was indeed vulnerable to IDOR.

Here, we only need to replace the file name of the image with the victim’s file name, and that’s all. We can delete the profile image of any user present on the platform.

I changed the file name from `endpoint.png`to `/1_1690351316.jpeg` which is the image file name of user 39. Interestingly, changing the user ID isn’t necessary to delete an image from this endpoint. We can easily delete profile images of any user just by knowing their image file name.

Replaced file name with victims file name

And yes, here we successfully deleted the profile image of our another testing account.

I reported these all three vulnerabilities to the developers, and they applied fixes to them within a day!

Thanks a ton for diving into this quick writeup — I really appreciate your curiosity & time. 🌟 If you have loved this little piece of writeup, don’t be shy — give it a hearty clap! 👏 Your virtual applause truly makes my digital heart to write more writeups.

I occasionally share tips and insights about Bug Bounties and related topics on my Twitter and LinkedIn handles. Follow me on these platforms to share more moments together.

*My Twitter handle:* [*https://twitter.com/rootxyash*](https://twitter.com/rootxyash)

*My Instagram handle:* [*https://instagram.com/\_y.a.s.h.w.a.n.t\_*](https://instagram.com/_y.a.s.h.w.a.n.t_)

*My LinkedIn handle:* [*https://www.linkedin.com/in/yash-devkate-644aa120a/*](https://www.linkedin.com/in/yash-devkate-644aa120a/)

Feel free to reach out if you have any questions, thoughts, or simply want to connect. I am always here to assist and engage with like-minded individuals.

*HAPPY HUNTING, SEE YOU SOON!*

文章来源: https://infosecwriteups.com/gone-in-a-click-idor-vulnerabilities-in-image-upload-function-6c4817b44d8c?source=rss----7b722bfd1b8d--bug\_bounty
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)