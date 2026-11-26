---
title: 备份材料、验证流程与密码规则
url: https://lucifer11.xyz/knowledge/credentials/
source: 0xfd's blog
date: 2026-11-25
fetch_date: 2026-11-26T10:13:49.052272
---

# 备份材料、验证流程与密码规则

![0xfd's blog](/images/fifteen-katana-zero-katana-zero.gif)
[0xfd's blog](/)

by 0xfd

* [首页](/)
* [知识库](/knowledge/)
* [导读](/guide/)
* [分类](/categories/)
* [标签](/tags/)
* [归档](/archives/)
* [关于](/about/)
* 搜索

* 文章目录
* 站点概览

1. [分析重点](#%E5%88%86%E6%9E%90%E9%87%8D%E7%82%B9)
2. [案例与技术索引](#%E6%A1%88%E4%BE%8B%E4%B8%8E%E6%8A%80%E6%9C%AF%E7%B4%A2%E5%BC%95)
3. [邮箱验证边界与密码规则](#%E9%82%AE%E7%AE%B1%E9%AA%8C%E8%AF%81%E8%BE%B9%E7%95%8C%E4%B8%8E%E5%AF%86%E7%A0%81%E8%A7%84%E5%88%99)
4. [备份、哈希与 CMS 账户复用](#%E5%A4%87%E4%BB%BD%E3%80%81%E5%93%88%E5%B8%8C%E4%B8%8E-CMS-%E8%B4%A6%E6%88%B7%E5%A4%8D%E7%94%A8)
5. [应用备份与凭据线索](#%E5%BA%94%E7%94%A8%E5%A4%87%E4%BB%BD%E4%B8%8E%E5%87%AD%E6%8D%AE%E7%BA%BF%E7%B4%A2)

![253](/images/fifteen-katana-zero-katana-zero.gif)

253

漏洞分析、利用机制、二进制研究与安全工程

[83
日志](/archives/)

[65
分类](/categories/)

[312
标签](/tags/)

GitHub

E-Mail

Twitter

FB Page

YouTube

Instagram

infosec.exchange

![Creative Commons](https://cdnjs.cloudflare.com/ajax/libs/creativecommons-vocabulary/2020.11.3/assets/license_badges/big/by_nc_sa.svg)

0%

链接

* atsud0
* 记忆里的纯真
* 小离

# 备份材料、验证流程与密码规则

发表于
2026-11-25

分类于

[身份与域安全](/categories/%E8%BA%AB%E4%BB%BD%E4%B8%8E%E5%9F%9F%E5%AE%89%E5%85%A8/)
，
[凭据分析](/categories/%E8%BA%AB%E4%BB%BD%E4%B8%8E%E5%9F%9F%E5%AE%89%E5%85%A8/%E5%87%AD%E6%8D%AE%E5%88%86%E6%9E%90/)

阅读次数：

本文字数：
9.4k

阅读时长 ≈
34 分钟

原案例中的账户线索分布在工单、聊天、备份和本地文件里。本章保留材料来源、编码或哈希形式，以及恢复后在哪个接口得到验证，避免只记住一个最终口令。

原案例中的账户线索分布在工单、聊天、备份和本地文件里。本章保留材料来源、编码或哈希形式，以及恢复后在哪个接口得到验证，避免只记住一个最终口令。

[知识库目录](/knowledge/)
[研究导读](/guide/)
[下载 Markdown](/knowledge/credentials/source.md)
展开全部技术记录

## 分析重点

Delivery 的工单邮箱与 Mattermost 注册流程连接到密码规则。

Os-hackNos-2.1 结合备份与 WordPress 数据，View2aKill 跟踪开发目录与本地脚本。

字典、规则和哈希格式依原记录保留，具体账号沿各案例核查。

## 案例与技术索引

| 分析入口 | 实验来源 | 技术点 |
| --- | --- | --- |
| [邮箱验证边界与密码规则](#case-delivery) | delivery | 邮箱验证、Mattermost、密码审计 |
| [备份、哈希与 CMS 账户复用](#case-hacknos-os-hacknos-2-1) | hackNos-Os-hackNos-2-1 | WordPress、备份泄露、密码审计 |
| [应用备份与凭据线索](#case-view2akill) | View2aKill | 备份泄露、模糊测试、Python |

## 邮箱验证边界与密码规则

工单邮箱影响内部门户注册，Mattermost 配置和聊天内容进一步连接到密码规则。保留规则生成、哈希验证及失败尝试的原始次序。

来源 delivery · 原记录 2021-01-12 · 14 个代码块 · 3 处图片引用

查看分析过程、攻击步骤与完整代码

#### introduce

OS: Linux
Difficulty: Easy
Points: 20
Release: 09 Jan 2021
IP: 10.10.10.222

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/htb156.jpg)
* ![my htb rank](http://www.hackthebox.eu/badge/image/235857)

#### information gathering

first use nmap as usaul

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` ┌──(root💀kali)-[~/hackthebox/machine/delivery] └─# nmap -sV -v -p- --min-rate=10000 10.10.10.222 PORT     STATE SERVICE VERSION 22/tcp   open  ssh     OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0) 80/tcp   open  http    nginx 1.14.2 8065/tcp open  unknown ``` |

#### Port-80

There is a simple Web Page.

Let’s click on Contact Us.

This give us Two links.

Let’s click on both.

Now we find two domain name with this two links.

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` helpdesk.delivery.htb delivery.htb:8065 ``` |

Let’s add both in our /etc/hosts file.

Now let’s first go to delivery.htb:8065.

There is a login page and create-one-now option let’s click on that real quick.

Give the details and click on Create Account.

It’s asking us for verify our email address. but we don’t have that email id.

So we can’t do anything here let’s go to another domain called helpdesk.delivery.htb

It’s a support center page.

Let’s click on open a new ticket.

I fill all information and then click on Create-Ticket.

* note : Write down your email-address on mousepad or anything you want because it will use after that.

Now you also got another email and ticket number save this also in your notes.

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` ticket id: 3192528. 3192528@delivery.htb. ``` |

Now click on Check-Ticket-Status.

Now enter your email id which you use in your create ticket form and enter ticket number which you store in you notes.

After that click on View-Ticket.

Now you got the inbox of your email-address which will be use when we register on delivery.htb:8065.

Now open delivery.htb:8065 in new tab.

Important : Don’t close this tab.

Now again click on Create account.

Add that email-address which you got after creating ticket.

Now click on create-account.

Now he send the verify link in our previous tab. Let’s go on previous tab.

Now click on View Ticket Thread for refresh the page.

And you got the email with verfication link. copy that link and open in new tab.

Now it’s said Email verified.

Now enter the password and Sign in.

Click on Internal to Continue.

Click on Skip Tutorial.

Now if you see a closer look you find username and passowrd for ssh.

|  |  |
| --- | --- |
| ``` 1 ``` | ``` maildeliverer:Youve_G0t_Mail! ``` |

Let’s ssh in and got our user.txt.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``` | ``` ┌──(root💀kali)-[~/hackthebox/machine/delivery] └─# ssh maildeliverer@10.10.10.222 maildeliverer@10.10.10.222's password:  Linux Delivery 4.19.0-13-amd64 #1 SMP Debian 4.19.160-2 (2020-11-28) x86_64  The programs included with the Debian GNU/Linux system are free software; the exact distribution terms for each program are described in the individual files in /usr/share/doc/*/copyright.  Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent permitted by applicable law. Last login: Tue Jan  5 06:09:50 2021 from 10.10.14.5 maildeliverer@Delivery:~$ cat user.txt 8ba333808740c70f27375b57223df281 ``` |

After some manual Enumeration found an interesting file called config.json inside /opt/mattermost/config/ directory.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197 198 199 200 201 202 203 204 205 206 207 208 209 210 211 212 213 214 215 216 217 218 219 220 221 222 223 224 225 226 227 228 229 230 231 232 233 234 235 236 237 238 239 240 241 242 243 244 245 246 247 248 249 250 251 252 253 254 255 256 257 258 259 260 261 262 263 264 265 266 267 268 269 270 271 272 273 274 275 276 277 278 279 280 281 282 283 284 285 286 287 288 289 290 291 292 293 294 295 296 297 298 299 300 301 302 303 304 305 306 307 308 309 310 311 312 313 314 315 316 317 318 319 320 321 322 323 324 325 326 327 328 329 330 331 332 333 334 335 336 337 338 339 340 341 342 343 344 345 346 347 348 349 350 351 352 353 354 355 356 357 358 359 360 361 362 363 364 365 366 367 368 369 370 371 372 373 374 375 376 377 378 379 380 381 382 383 384 385 386 387 388 389 390 391 392 393 394 395 396 397 398 399 400 401 402 403 404 405 406 407 408 409 410 411 412 413 414 415 416 417 418 419 420 421 422 423 424 425 426 427 428 429 430 431 432 433 434 435 436 437 438 439 440 441 442 443 444 445 446 447 448 449 450 451 452 453 454 455 456 457 458 459 460 461 462 463 464 465 466 467 468 469 470 471 472 473 474 475 476 477 478 479 480 481 482 483 484 485 486 487 488 489 490 491 492 493 494 495 496 497 498 499 500 501 502 503 504 505 506 507 508 509 510 511 512 513 514 515 516 517 518 519 520 521 522 523 524 525 526 527 528 529 530 531 532 533 534 535 536 537 538 539 540 541 542 543 544 545 546 547 ``` | ``` maildeliverer@Delivery:/opt/mattermost/config$ cat config.json  {     "ServiceSettings": {         "SiteURL": "",         "WebsocketURL": "",         "LicenseFileLocation": "",         "ListenAddress": ":8065",         "ConnectionSecurity": "",         "TLSCertFile...