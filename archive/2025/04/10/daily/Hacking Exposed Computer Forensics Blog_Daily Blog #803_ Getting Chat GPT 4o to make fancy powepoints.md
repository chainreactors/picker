---
title: Daily Blog #803: Getting Chat GPT 4o to make fancy powepoints
url: https://www.hecfblog.com/2025/04/daily-blog-803-getting-chat-gpt-4o-to.html
source: Hacking Exposed Computer Forensics Blog
date: 2025-04-10
fetch_date: 2025-10-06T22:07:36.109663
---

# Daily Blog #803: Getting Chat GPT 4o to make fancy powepoints

[![Hacking Exposed Computer Forensics Blog](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhV1r9Fx_K3sKHfI8wnPUPPQFkxWhuxayNz8tT11sG8lYQgY1gGiwV9Qdlfeq-b80FMkRdsOwimMVCo2VbnE0aXyGxaTX1YYhUB5IZ4yK1LhASjfZxFmkAstIM9DnylPabPqQ15WEAFysbZ/s384/unnamed.png)](https://www.hecfblog.com/)

* [Extended Mapi](https://www.hecfblog.com/search/label/extended%20mapi)
* [ObjectID](https://www.hecfblog.com/search/label/objectid)
* [Amcache](https://www.hecfblog.com/search/label/amcache)
* [CTF](https://www.hecfblog.com/search/label/ctf)
* [Python](https://www.hecfblog.com/search/label/python)
* [Syscache](https://www.hecfblog.com/search/label/syscache)
* [Daily Blogs](https://www.hecfblog.com/search/label/Daily%20Blog?max-results=6)
  + [Saturday Reading](https://www.hecfblog.com/search/label/Saturday%20reading)
  + [Solution Saturday](https://www.hecfblog.com/search/label/solution%20saturday)
  + [Forensic Lunch](https://www.hecfblog.com/search/label/forensic%20lunch?&max-results=8)
  + [Sunday Funday](https://www.hecfblog.com/search/label/sunday%20funday?&max-results=8)

[Home](https://www.hecfblog.com/)

[powerpoint](https://www.hecfblog.com/search/label/powerpoint)

Daily Blog #803: Getting Chat GPT 4o to make fancy powepoints

# Daily Blog #803: Getting Chat GPT 4o to make fancy powepoints

By
[David Cowen](https://www.blogger.com/profile/17629115910611763170 "author profile")
•
April 09, 2025
•

[4o](https://www.hecfblog.com/search/label/4o?&max-results=8)
[AI](https://www.hecfblog.com/search/label/AI?&max-results=8)
[chat gpt](https://www.hecfblog.com/search/label/chat%20gpt?&max-results=8)
[Daily Blog](https://www.hecfblog.com/search/label/Daily%20Blog?&max-results=8)
[powerpoint](https://www.hecfblog.com/search/label/powerpoint?&max-results=8)
•

Comments :
0

**Hello Reader,**

Yesterday, when I shared my presentation, I mentioned that while I conducted all the research myself, I used ChatGPT-4o to create all of the slides.

Why? Because I have absolutely no artistic skills—but I did have all the technical knowledge I wanted to communicate. If you’re like me and want your presentations to *look* like you hired a professional designer, here’s how I made it happen.

---

### Step 1: Tell It What You Want

I started by describing the scope of the presentation:

> ```
> Create a slideshow presentation about Windows Hello forensics complete with graphics
> ```
>
> ```
> and text.
>
> It should cover how to perform forensics on the Windows 11 Hello security feature.
> ```
>
> ```
> Include slides on:
>
> - History of Hello
> - The historical forensic challenge of identifying who is at the keyboard
> - A list of Windows Hello authentication methods
> - Where in the registry to find which authentication methods are enabled
> - What the event logs show for:
>     - PIN login
>     - Fingerprint login
>     - Facial scan login
> - Where Windows Hello data is stored
> - How the stored data is protected
> - How the data can be accessed
>
> Also, include any other slides you think would be interesting.
> ```

```

```

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgOqJGbVCIvmFWZDvsjH90rVoYAK7kIUOaYmy-NVyMt2lqzrpKBX_ZfqJ6VFVSoCYKoxWnYYAwm5CvjVyonDtR4XDiRttsGvp_iRduWswZZ9fDU6LCorVnwYcjUAQ84ucm3GgQuE391YXcMxDKWuX7_-gZ13kYR7SlV4Mcw3lNF90A9rDik9b4N0MVDIJ8/w640-h466/firstprompt.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgOqJGbVCIvmFWZDvsjH90rVoYAK7kIUOaYmy-NVyMt2lqzrpKBX_ZfqJ6VFVSoCYKoxWnYYAwm5CvjVyonDtR4XDiRttsGvp_iRduWswZZ9fDU6LCorVnwYcjUAQ84ucm3GgQuE391YXcMxDKWuX7_-gZ13kYR7SlV4Mcw3lNF90A9rDik9b4N0MVDIJ8/s817/firstprompt.jpg)

```

```

```
It responded with a detailed outline of the slide contents—a sort of text storyboard.
```

```

```

---

### Step 2: Ask for the Presentation

```
So I followed up with:
```

```
> Turn this into a PowerPoint presentation with graphics you create for each slide.
```

```
![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgLAnkeayPJjhFHHccHxKuuUEQNm9pgeJO6SQ24tgdvic5yvVpoCh59mYX8QYAGAncDojT1tGXYx-uC8j5K_GXRhBygxv1Qq8ZdGaPBEDtFpgqU6zI2Bxm9GGEIN3nDVCGjY9dhKW8ITzm0CfanH-zCEO2zwYxVBs6dM_MruVoAZcmzEL7D1GW1MFRUMaU/w640-h234/secondprompt.jpg)

```

This generated text-only slides. So I clarified further:

> ```
> Yes, I would like all of the above as you find them most useful.
> ```
>
> ```
> Generate all relevant graphics and insert them into the slides.
> ```
>
> ```
> Also give it a cyberpunk theme.
> ```

```
![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjsgM-P_vY0u46fq6ZmZKaYCLemaX4Qf8FzIa8HPYWi01uqZ2KqUCr4cixEppnrHQrAQM8Lde4sJhfvdUTyBAi1nmTywxbt7uX1-d8iP4IXaf-ifJfmpprcBN56nB18rrgA6NG_fUHKk6goNUSAtjR7YHDHOu6KPpyXdVkySrR5rlNgHVA5iFksD6MHuuM/w640-h500/thirdprompt.jpg)

```

---

### Step 3: Let It Build

It generated the first image, and I simply told it:

```
> Finish all the slides and provide me the updated PPT with the graphics added in.
```

```
![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4oH5KvIwLRsPDQGk_ONbFKwkuPECU-95ISJ1QeuEysd3Cp6vSEl1QqlnmGIKg946ROJ2557kptpxte_yTqeCh9d6dPzpv9XC1D6VIGILUBm47ujEz2mGt5rzgjxlKNzc-f6lcCla7c-BKAc92fOMPMcTBrQi6yu4BPbFKwyipVW9uaiSAatlHeGx3kA4/w640-h554/fourthprompt.jpg)

```

I had to say “continue” a couple of times to get it to finish the entire deck—but that was it! Afterward, I went in and added relevant technical facts, and the presentation was complete.

---

Looking back, I probably could have done it all in one prompt if I had been more specific. Still, I’m incredibly happy with the results—and I didn’t need any design skills to get there.

#### Post a Comment

[Newer Post](https://www.hecfblog.com/2025/04/daily-blog-804-introducing-puck.html "Newer Post")

[Older Post](https://www.hecfblog.com/2025/04/daily-blog-802-windows-helllo-forensics.html "Older Post")
[Home](https://www.hecfblog.com/)

Subscribe to:
[Post Comments
(
Atom
)](https://www.hecfblog.com/feeds/7776967981098016521/comments/default)

## Top Posts/Right Now

* [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiS4Zw9KQkjNkc2JCwa0rDb1zPUCypCWZgocTE2voitZGOwzeZ2L_4D63LJ0j9JPosWO-nLahPLJYL-tsQMEgmfVhxmjpJ6Smn6FKVk2_JhClTq_WWhvcE13R76fsdeVWnJb-lPNFnJnif0HpOq-5yuADLWqHUQjQG4zpbLb46P0PM-dvHaM9rsb-D39qs/s72-c/sundayfunday.png)](https://www.hecfblog.com/2025/04/daily-blog-814-sunday-funday-42025.html)

  [Daily Blog #814: Sunday Funday 4/20/25](https://www.hecfblog.com/2025/04/daily-blog-814-sunday-funday-42025.html)
* [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj5GWh0tXGteqxfrTQFDzW2kMooGHcwNkA6h9f_bfBDpsRMJtvg0UR1SHfIqx4UYxViUSiLEJFeWq9SryUdFz5gwlrOlXEFCZDoNnqRlbU3pn_lGfYxr60W3HgTAXc7b3IqLHYN3F0kW72JbkCoEID0IEVH-rls7Q1LRd_0awNugK97uT7EDxugHyuXvFM/s72-c/forgive.png)](https://www.hecfblog.com/2025/04/daily-blog-815-i-missed-day.html)

  [Daily Blog #815: I missed a day](https://www.hecfblog.com/2025/04/daily-blog-815-i-missed-day.html)
* [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi60iLy5WiSNWWSyeIoM9JsOK9Xwv5L7GT5g4NxBmdQwyQNbbHzgWoiG4FbwefVVrqg1yDaz0ripRAlyXSWNX4xJ3tACOcH7a0_YyoPVT2XMPnI2-0aE3gKc9hJWhMWYqDWlTUDM2XM3DEHiJB5Z1iSrtjQeP0qG5xKxmt4RewUfbqA0FR7cw1DXPwxYNM/s72-c/solutionsaturday.png)](https://www.hecfblog.com/2025/04/daily-blog-813-solution-saturday-41925.html)

  [Daily Blog #813: Solution Saturday 4/19/25](https://www.hecfblog.com/2025/04/daily-blog-813-solution-saturday-41925.html)
* [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhK3OAgdGTujkTy5X-nM4364yuWc8TJa-ct4GGE-Phw3vdXX9DApDT_kRhIvjELWVYLvnTPIrJTGFuz2hhkhVoklmY6bixe4fypY1X1A8RuJgAoPUUK597HYTBKVrOgLMn11x2g6b0azfhNnVv7CE6p-ZZRcfmAnaIIB-RNEBL_rIakVyr80MUyDhMQGgI/s72-c/removefromgroup.png)](https://www.hecfblog.com/2025/04/daily-blog-812-testing-aws-log-latency.html)

  [Daily Blog #812: Testing AWS Log latency - Removing Users from Groups](https://www.hecfblog.com/2025/04/daily-blog-812-testing-aws-log-latency.html)
* [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEitgwVMjukTzCuo_bdlGs6...