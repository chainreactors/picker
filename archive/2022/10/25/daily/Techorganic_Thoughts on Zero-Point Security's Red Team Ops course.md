---
title: Thoughts on Zero-Point Security's Red Team Ops course
url: http://blog.techorganic.com/2022/10/24/thoughts-on-zeropoint-securitys-red-team-ops-course/
source: Techorganic
date: 2022-10-25
fetch_date: 2025-10-03T20:46:21.739672
---

# Thoughts on Zero-Point Security's Red Team Ops course

[![](/images/glider.png)](/)

#

Musings from the brainpan

[About](/about)
[Contact](/contact)
[Disclaimer](/disclaimer)
[Vulns](https://github.com/superkojiman/vulnerabilities)
[Slides](https://speakerdeck.com/superkojiman)

# Thoughts on Zero-Point Security's Red Team Ops course

Written on October 24, 2022

This weekend I successfully completed the [Red Team Ops](https://training.zeropointsecurity.co.uk/courses/red-team-ops) exam offered by [Zero-Point Security](https://www.zeropointsecurity.co.uk/) and [Rasta Mouse](https://twitter.com/_rastamouse). This is a red team training course with a focus on exploiting misconfigurations within an Active Directory environment. Completing the lessons earns you a certificate, so if that’s all you want, then you can stop there. However, if you really want to challenge what you’ve learnt, you’ll definitely want to take on the exam.

The course includes lessons that covers various techniques to identify and exploit misconfigurations in Active Directory. While it focuses primarily on offensive techniques, it also covers indicators left by various attacks that could be used to alert a blue team to your activities. The entire curriculum is at [Zero-Point Security’s](https://training.zeropointsecurity.co.uk/courses/red-team-ops) website so I won’t repeat it here.

A virtual lab environment is provided where you can test out everything you’ve learned. The biggest selling point for me was the inclusion of the [Cobalt Strike](https://www.cobaltstrike.com/features/) software that you can use in the lab. I’ve done a few red team engagements in the past, so I was familiar with the topics covered in the course. However, I had always used open source C2 frameworks such as [Empire](https://github.com/BC-SECURITY/Empire) and [Covenant](https://github.com/cobbr/Covenant), so I was excited to test drive Cobalt Strike. While it may not be everyone’s cup of tea, Cobalt Strike is used by many red teamers and threat actors alike. It was great to be able to explore its capabilities within a vulnerable environment.

You retain access to the lessons and any updates it gets even after the exam is over. The lessons themselves were only recently updated with new topics and restructured to make it flow better. Lab access can be purchased by the hour, and I made full use of it, even during the exam. It was helpful to be able to test and experiment with different things, and then just revert the entire lab if something broke.

The exam is 48 hours long, spaced out over four days. You can pause the exam at any time so as to not burn through the 48 hours. There’s plenty of time to hack, eat, sleep and repeat. I did about 12 hours of hacking each day, and spent the remaining hours doing non-computer related things. This gave my brain a break whenever I hit a brick wall, and allowed me to look at the problem with a clear mind. There are 8 flags in the exam environment, but you only need 6 to pass. No report writing is required, and once you’ve submitted 6 flags, you’ve pretty much passed.

The week before the exam, I went through the lessons and labs once more, and I kept detailed and structured notes. I put together a game plan on what to do once I had a foothold on a computer to try and reduce my chances of missing anything important or making a mistake. One of the tips given by Rasta Mouse was to ensure that we were prepared to bypass anti-virus and defenses. So I made sure my payloads in the lab were executing properly in a machine that had anti-virus running.

I started the exam on Tuesday morning, and by Thursday I had six flags. By the end of Friday, I scored the remaining two flags and ended the exam with a 100% score, and 10 hours to spare. Despite my best efforts, I missed a crucial enumeration step early on which prevented me from getting a flag much sooner than I should have. After a long break and looking at my findings again, I finally saw it and was able to move forward.

Whenever I got a flag, I took a short break so I could approach the next problem with a clear mind. If I had to take a long break, I paused the lab, which effectively turned it off. If you’ve understood the lessons and play your cards right, you’ll know how to pick up right where you left off without too much trouble.

As soon as the exam event ended, I received my Certified Red Team Ops badge:

[![](/images/2022-10-24/01.png)](https://ca.badgr.com/public/assertions/kndcIHx6RAGZJ5zol8XLIA)

Overall, I had a positive experience taking the course and exam. I highly recommend it to anyone interested in red teaming, or learning how to use Cobalt Strike. I took the course with the intention of gaining some experience with Cobalt Strike and learning some new things, and I walked away with exactly that.