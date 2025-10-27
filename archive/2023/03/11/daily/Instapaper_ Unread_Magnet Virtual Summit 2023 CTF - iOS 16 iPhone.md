---
title: Magnet Virtual Summit 2023 CTF - iOS 16 iPhone
url: https://www.stark4n6.com/2023/03/magnet-virtual-summit-2023-ctf-ios-16.html
source: Instapaper: Unread
date: 2023-03-11
fetch_date: 2025-10-04T09:18:57.981273
---

# Magnet Virtual Summit 2023 CTF - iOS 16 iPhone

[Skip to main content](#main)

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhKbEuDpbWt2h4R7y02WrWiCmAG90SxVmMkXsEXZE0k3gAACuFYgfUVuTHkKpfowS3WWbkh6XGjqMXh77QkxuZv0osjeusHJnR_ehrMU9r8RaAa3a2R61zmMgl3wLsGpQxSh7rCRX4oQEM/s1600/1947245.png)

Search

### Search This Blog

### Magnet Virtual Summit 2023 CTF - iOS 16 iPhone

Posted by

[Kevin Pagano](https://www.blogger.com/profile/13417965550116928863 "author profile")

[March 09, 2023](https://www.stark4n6.com/2023/03/magnet-virtual-summit-2023-ctf-ios-16.html "permanent link")

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgIyGhYK1OhICDhBgMhbymi3_Yhbob2ePTHSpa3d6G4qWYe4JwUwYKDTKOpydzQjpk1-jP47LVi5mTIFUooZiYxkBSOWShs8ro1MUptuUcKcWXH6rrCoroToCc-YPBcDrXuBfBzdzi-IpO_BUBuYc2R8A-GLRnQqkk73OG6ksJyR5FOwqE47ZOedLCm/w640-h336/ios-16-og.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgIyGhYK1OhICDhBgMhbymi3_Yhbob2ePTHSpa3d6G4qWYe4JwUwYKDTKOpydzQjpk1-jP47LVi5mTIFUooZiYxkBSOWShs8ro1MUptuUcKcWXH6rrCoroToCc-YPBcDrXuBfBzdzi-IpO_BUBuYc2R8A-GLRnQqkk73OG6ksJyR5FOwqE47ZOedLCm/s1200/ios-16-og.jpg)

Previous: [Windows 11](https://www.stark4n6.com/2023/03/magnet-virtual-summit-2023-ctf-windows.html) | [Cipher](https://www.stark4n6.com/2023/03/magnet-virtual-summit-2023-ctf-cipher.html) | [Windows Server](https://www.stark4n6.com/2023/03/magnet-virtual-summit-2023-ctf-windows_8.html)

Like last year's
[iOS 15 image](https://www.stark4n6.com/2022/06/magnet-user-summit-2022-ctf-iphone.html), we get one of the first full file system "test" images for iOS 16 publicly
available. Let's see what we get.

Tools used:

* [iLEAPP v1.18.4](https://github.com/abrignoni/iLEAPP)
* [Magnet AXIOM v6.11](https://www.magnetforensics.com/products/magnet-axiom/)

Evidence: [00008101-0010541A1130001E\_files\_full-001.zip](https://go.magnetforensics.com/e/52162/41A1130001E-files-full-001-zip/lhmdf2/1324250137?h=VjIef9nVy7wB1qONdAWbDcVEBzeNtFMM_Ou-e_OJSOw&_gl=1*17863h4*_ga*MTMwNzI2NDgzMS4xNTkwNDQ2OTMz*_ga_YTB3MPRL03*MTY3OTQyNjg0Ny45NC4xLjE2Nzk0MjczNzguNDIuMC4w)

## A few too many (5 points)

> How many email accounts did the user own? (not counting privaterelay)

This one required a bit of correlation. Via the Refined Results > User
Accounts artifact in AXIOM we can see 3 distinct email addresses:

* blueisth3best@gmail.com

+ pulled from Accounts3.sqlite / Apple Mail

* borchardtmichael78@gmail.com

+ pulled from Chrome Login Data

* michaelkborchardt@proton.me

+ pulled from Chrome Login Data

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEioQQntyvwgsQSWiKPOrAvcffDt2cAxxjCnQwoZ8DpMCkbAfO3m7a31To3j0PFeZML_QQRIhopKsJRjDeCvMys0dT6e8N5gGJAa27cwtuOeWO3L_9XIR4GEE8o4AyKLt27p200pQ8KYW73gjKJp4S5nUrQKLmDrtP6OHS-2U5Q4juM5zw5JIeBpgZsd/w640-h198/accounts.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEioQQntyvwgsQSWiKPOrAvcffDt2cAxxjCnQwoZ8DpMCkbAfO3m7a31To3j0PFeZML_QQRIhopKsJRjDeCvMys0dT6e8N5gGJAa27cwtuOeWO3L_9XIR4GEE8o4AyKLt27p200pQ8KYW73gjKJp4S5nUrQKLmDrtP6OHS-2U5Q4juM5zw5JIeBpgZsd/s724/accounts.png)

***Figure 1: User Accounts via AXIOM***

What we also need to account for is other communication methods too. Slack
was installed on the phone and if we check the Slack Accounts artifact we
see we get yet another different email address.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEia69oIXwZeXWff8ECN-QEp5Is-PfF-xTbq4T0zMvPpCO8NeZaGnndVkcoqemM-gBU4AS-sDVRWfFfr_K5OrZgnFdDL1r4uy3RY7IxskSoYf-hdkSg90vPkcLWH-2puGycLYmja_fU1ZMenOeUHqGWRJS-qJmhDOvkWyqPZuaK6r8Mq_XMYHnHHVt1w/w640-h389/slack.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEia69oIXwZeXWff8ECN-QEp5Is-PfF-xTbq4T0zMvPpCO8NeZaGnndVkcoqemM-gBU4AS-sDVRWfFfr_K5OrZgnFdDL1r4uy3RY7IxskSoYf-hdkSg90vPkcLWH-2puGycLYmja_fU1ZMenOeUHqGWRJS-qJmhDOvkWyqPZuaK6r8Mq_XMYHnHHVt1w/s629/slack.png)

***Figure 2: Slack Account details via AXIOM***

So in total we have 4 different
email accounts from the owner of the phone.

## autoFill me in on the deets (5 points)

> Which email, other than their own, was autofilled in Chrome?

Heading over to the Chrome Autofill again, we can see only one other
email address that didn't belong to Michael Borchardt, and that was
tlouis@kurvalis.com.

[![](https://blogger.googleusercontent.com/img/a/AVvXsEj9aV03CItQX3e73dv0QNFUTSVXXfzDZ5UDBoGLoU9n-uF40nSfQdNi95DrttA7vbutJFPsof2CwpQFrKnKEvLHrjEWiXSjM2JJOx4AsKmwcnjtQcJ8wPc0F2OK8azYtF693J_tOfcwVC4lmADvSM2-lTP6-3NDUXehLw4ssjlnpfG-Xr0P3VFhlZlL=w640-h300)](https://blogger.googleusercontent.com/img/a/AVvXsEj9aV03CItQX3e73dv0QNFUTSVXXfzDZ5UDBoGLoU9n-uF40nSfQdNi95DrttA7vbutJFPsof2CwpQFrKnKEvLHrjEWiXSjM2JJOx4AsKmwcnjtQcJ8wPc0F2OK8azYtF693J_tOfcwVC4lmADvSM2-lTP6-3NDUXehLw4ssjlnpfG-Xr0P3VFhlZlL)

***Figure 3: Chrome Autofill in AXIOM***

## 1 fish 2 fish, red fish blue fish (5 points)

> According to the user's email accounts, what is his favorite
> color?

I way overlooked this one originally, just don't make it too
complicated. Michael's iCloud email address was
blueisth3best@icloud.com, his favorite color is
blue. It's littered all
over the Account Data.

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhMJ8bTUc0KRP30wgufYQ9kkzx56-0Sc5-QJDFvwDJBbt5uJz8PgDhVM2KKkiW5Qb9cOIXl25IYIGqY2iooAoZhqUqx3LJ7pP9qb4k5Grvc0VMRx5KYl9YWWlxosohHAEDnNAygKuRS34q_J7mYE5bzil5X8sEvkAs-u1SwtUIdlScaaSQ8NTPE7pbe=w640-h509)](https://blogger.googleusercontent.com/img/a/AVvXsEhMJ8bTUc0KRP30wgufYQ9kkzx56-0Sc5-QJDFvwDJBbt5uJz8PgDhVM2KKkiW5Qb9cOIXl25IYIGqY2iooAoZhqUqx3LJ7pP9qb4k5Grvc0VMRx5KYl9YWWlxosohHAEDnNAygKuRS34q_J7mYE5bzil5X8sEvkAs-u1SwtUIdlScaaSQ8NTPE7pbe)

***Figure 4: Account Data report in iLEAPP***

## Q-uestion (5 points)

> What Chinese networking website was associated with Linkedin?

I first did a keyword search on LinkedIn to narrow down the
scope to hopefully have a quick win in a path or something. My
first thought was to go directly to
[QQ Chat](https://en.wikipedia.org/wiki/Tencent_QQ)
which appeared to be partially correct. Carved from potential
browser activity was a URL for QQ.

[![](https://blogger.googleusercontent.com/img/a/AVvXsEiguaTD9Q08G3uXAMOHzagE1ev5InbujdY-AQHalzEa0vkL3PTeFngPJduhyV230Odxw9InW5EFf1CWI97oxIRt_R2RDX50h85gWWUQCdQcbMVIFFRdq467bOUgnAodA-Td5VuPoW0FDhDLTZdgiP1uWmsdH4O8YYApxaZpRp6tYlL9F66uSbK7PKnS=w640-h400)](https://blogger.googleusercontent.com/img/a/AVvXsEiguaTD9Q08G3uXAMOHzagE1ev5InbujdY-AQHalzEa0vkL3PTeFngPJduhyV230Odxw9InW5EFf1CWI97oxIRt_R2RDX50h85gWWUQCdQcbMVIFFRdq467bOUgnAodA-Td5VuPoW0FDhDLTZdgiP1uWmsdH4O8YYApxaZpRp6tYlL9F66uSbK7PKnS)

***Figure 5: Potential Browser Activity for LinkedIn related
sites***

QQ didn't work but
QZone took. As you can see
it's being pulled from the LinkedIn application folder location.

## Chef Boyardee 2.0 (10 points)

> At which market was the user viewing Chef Pasquale tomato sauce?

The first thing I gravitated to was to look at the DCIM folder for the
user's images. Filtering for the folder and hitting the Pictures
artifact, we can see a few different pictures of grocery store shelves
with cans and bottles but one specifically fits the description.

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjV_lkem4pIxGUq056wNn4N3gGxuPDEWCm0QfBRRx2hmEDhyPUHDGa-5wcz8DQl7HgHlSiXcSciITxW0qH2deOOxPDMPHr73jzTIr82W8JrblgEo1pB1gFViZqONFP5jwJ74L39wwghbcQ_8o00h0aUw9uM32Z4OSpe1JWw8s4n7dbjwFu16zRevKMp=w565-h640)](https://blogger.googleusercontent.com/img/a/AVvXsEjV_lkem4pIxGUq056wNn4N3gGxuPDEWCm0QfBRRx2hmEDhyPUHDGa-5wcz8DQl7HgHlSiXcSciITxW0qH2deOOxPDMPHr73jzTIr82W8JrblgEo1pB1gFViZqONFP5jwJ74L39wwghbcQ_8o00h0aUw9uM32Z4OSpe1JWw8s4n7dbjwFu16zRevKMp)

***Figure 6: Pasquale's tomato sauce from DCIM***

We can see 3 different varieties from Chef Pasquale. Looking at the
EXIF data of the image we get the latitude and longitude of where the
picture was taken.

[![](https://blogger.googleusercontent.com/img/a/AVvXsEga0ZSVZdpoVvWNNnxVbnqmIhLZ5uYddlAxjEowfD6i8vsT_hUgckEjWJDx3dPKp-noCcuBtHTwWbr2hc8tbZFlCVKl3gzvvFR19mzmZXn6wXdBwutLMpU0qnjifkFJCl1x...