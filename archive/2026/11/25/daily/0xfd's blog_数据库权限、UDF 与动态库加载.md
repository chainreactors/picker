---
title: 数据库权限、UDF 与动态库加载
url: https://lucifer11.xyz/knowledge/database/
source: 0xfd's blog
date: 2026-11-25
fetch_date: 2026-11-26T10:13:50.085933
---

# 数据库权限、UDF 与动态库加载

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
3. [数据库进程权限与 UDF](#%E6%95%B0%E6%8D%AE%E5%BA%93%E8%BF%9B%E7%A8%8B%E6%9D%83%E9%99%90%E4%B8%8E-UDF)
4. [PHPMailer 参数与 UDF 动态库](#PHPMailer-%E5%8F%82%E6%95%B0%E4%B8%8E-UDF-%E5%8A%A8%E6%80%81%E5%BA%93)
5. [管理平台与 MariaDB 加载路径](#%E7%AE%A1%E7%90%86%E5%B9%B3%E5%8F%B0%E4%B8%8E-MariaDB-%E5%8A%A0%E8%BD%BD%E8%B7%AF%E5%BE%84)

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

# 数据库权限、UDF 与动态库加载

发表于
2026-11-25

分类于

[系统安全](/categories/%E7%B3%BB%E7%BB%9F%E5%AE%89%E5%85%A8/)
，
[数据库权限](/categories/%E7%B3%BB%E7%BB%9F%E5%AE%89%E5%85%A8/%E6%95%B0%E6%8D%AE%E5%BA%93%E6%9D%83%E9%99%90/)

阅读次数：

本文字数：
12k

阅读时长 ≈
44 分钟

数据库账户、数据库进程的系统身份以及插件路径权限共同决定扩展能力。本章保留 MySQL UDF、MariaDB 配置与应用初始入口，按数据、文件和执行三层核查。

数据库账户、数据库进程的系统身份以及插件路径权限共同决定扩展能力。本章保留 MySQL UDF、MariaDB 配置与应用初始入口，按数据、文件和执行三层核查。

[知识库目录](/knowledge/)
[研究导读](/guide/)
[下载 Markdown](/knowledge/database/source.md)
展开全部技术记录

## 分析重点

Raven 两篇分别保留 PHPMailer、编译的共享库、插件路径与 setuid 程序。

Shibboleth 的 Zabbix 身份连接 MariaDB 配置分支，不能只看数据库版本。

同类 UDF 出现在其他案例时，可从技术索引找到对应来源。

## 案例与技术索引

| 分析入口 | 实验来源 | 技术点 |
| --- | --- | --- |
| [数据库进程权限与 UDF](#case-raven-1) | Raven-1 | MySQL、UDF、PHPMailer |
| [PHPMailer 参数与 UDF 动态库](#case-raven-2) | Raven-2 | PHPMailer、UDF、MySQL |
| [管理平台与 MariaDB 加载路径](#case-shibboleth) | shibboleth | Zabbix、MariaDB、CVE-2021-27928 |

## 数据库进程权限与 UDF

WordPress、PHPMailer 和配置文件连接 MySQL 身份，UDF 插件路径与进程权限决定本地执行。Python SUID 的替代路径也在原文中。

来源 Raven-1 · 原记录 2020-02-12 · 30 个代码块 · 7 处图片引用

查看分析过程、攻击步骤与完整代码

#### 名称

名称：Raven: 1
发布日期：2018年8月14日

#### 下载

* Download: https://drive.google.com/open?id=1pCFv-OXmknLVluUu\_8ZCDr1XYWPDfLxW
* Download (Mirror): https://download.vulnhub.com/raven/Raven.ova
* Download (Torrent): https://download.vulnhub.com/raven/Raven.ova.torrent

#### 描述

Raven是初学者/中级boot2root计算机。有四个flag可以找到，并且有两个预期的root方法。使用VMware构建并在Virtual Box上进行了测试。设置为使用NAT网络。

#### 信息收集

上nmap

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197 198 199 200 201 202 203 204 205 206 207 208 209 210 211 212 213 214 215 216 217 218 219 220 221 222 223 224 225 226 227 228 229 230 231 232 233 234 235 236 237 238 239 240 241 242 243 244 245 246 247 248 249 250 251 252 253 254 255 256 257 258 259 260 261 262 263 264 265 266 267 268 269 270 271 272 273 274 275 276 277 278 279 280 281 282 283 284 285 286 287 288 289 290 291 292 293 294 295 296 297 298 299 300 301 302 303 304 305 306 307 308 309 310 311 312 313 314 315 316 317 318 319 320 321 322 323 324 325 326 327 328 329 330 331 332 333 334 335 336 337 338 339 340 341 342 343 344 345 346 347 348 349 350 351 352 353 354 355 356 357 358 359 360 361 362 363 364 365 366 367 368 369 370 371 372 373 374 375 376 377 378 379 380 381 382 383 384 385 386 387 388 389 390 391 392 393 394 395 396 397 398 399 400 401 402 403 404 405 406 407 408 409 410 411 412 413 414 415 416 417 418 419 420 421 422 423 424 425 426 427 428 429 430 431 432 433 434 435 436 437 438 439 440 441 442 443 444 445 446 447 448 449 450 451 452 453 454 455 456 457 458 459 460 461 462 463 464 465 466 467 468 469 470 471 472 473 474 475 476 477 478 479 480 481 482 483 484 485 486 487 488 489 490 491 492 493 494 495 496 497 498 499 500 501 502 503 504 505 506 507 508 509 510 511 512 513 514 515 516 517 518 519 520 521 522 523 524 525 526 527 528 529 530 531 532 533 534 535 536 537 538 539 540 541 542 543 544 545 546 547 548 549 550 551 552 553 554 555 556 557 558 559 560 561 562 563 564 565 566 567 568 569 570 571 572 573 574 575 576 577 578 579 580 581 582 583 584 585 586 587 588 589 590 591 592 593 594 595 596 597 598 599 600 601 602 603 604 605 606 607 608 609 610 611 612 613 614 615 616 617 618 619 620 621 622 623 624 625 626 627 628 629 630 631 632 633 634 635 636 637 638 639 640 641 642 643 644 645 646 647 648 649 650 651 652 653 654 655 656 657 658 659 660 661 662 663 664 665 666 667 668 669 670 671 672 673 674 675 676 677 678 679 680 681 682 683 684 685 686 687 688 689 690 691 692 693 694 695 696 697 698 699 700 701 702 703 704 705 706 707 708 709 710 711 712 713 714 715 716 717 718 719 720 721 722 723 724 725 726 727 728 729 730 731 732 733 734 735 736 737 738 739 740 741 742 743 744 745 746 747 748 749 750 751 752 753 754 755 756 757 758 759 760 761 762 763 764 765 766 767 768 769 770 771 772 773 774 775 776 777 778 779 780 781 782 783 784 785 786 787 788 789 790 791 792 793 794 795 796 797 798 799 800 801 802 803 804 805 806 807 808 809 810 811 812 813 814 815 816 817 818 819 820 821 822 823 824 825 826 827 828 829 830 831 832 833 834 835 836 837 838 839 840 841 842 843 844 845 846 847 848 849 850 851 852 853 854 855 856 857 858 859 860 861 862 863 864 865 866 867 868 869 870 871 872 873 874 875 876 877 878 879 880 881 882 883 884 885 886 887 888 889 890 891 892 893 894 895 896 897 898 899 900 901 902 903 904 905 ``` | ``` root@kali:~# nmap -sn -v 192.168.56.0/24 Nmap scan report for 192.168.56.118 Host is up (0.00016s latency). MAC Address: 08:00:27:D2:E6:4F (Oracle VirtualBox virtual NIC)  root@kali:~# nmap -p- -sV -v -Pn 192.168.56.118 PORT      STATE SERVICE VERSION 22/tcp    open  ssh     OpenSSH 6.7p1 Debian 5+deb8u4 (protocol 2.0) 80/tcp    open  http    Apache httpd 2.4.10 ((Debian)) 111/tcp   open  rpcbind 2-4 (RPC #100000) 36286/tcp open  status  1 (RPC #100024)  root@kali:~# nmap -p- -sU -Pn -v 192.168.56.118 --min-rate=10000 PORT    STATE SERVICE 111/udp open  rpcbind  root@kali:~# nmap -p 22,80,111,36286 -sV -v -Pn -A --script all 192.168.56.118 --min-rate=100000 PORT      STATE SERVICE VERSION 22/tcp    open  ssh     OpenSSH 6.7p1 Debian 5+deb8u4 (protocol 2.0) |_banner: SSH-2.0-OpenSSH_6.7p1 Debian-5+deb8u4 |_clamav-exec: ERROR: Script execution failed (use -d to debug) | ssh-auth-methods:  |   Supported authentication methods:  |     publickey |_    password | ssh-brute:  |   Accounts: No valid accounts found |_  Statistics: Performed 0 guesses in 1807 seconds, average tps: 0.0 | ssh-hostkey:  |   1024 26:81:c1:f3:5e:01:ef:93:49:3d:91:1e:ae:8b:3c:fc (DSA) |   2048 31:58:01:19:4d:a2:80:a6:b9:0d:40:98:1c:97:aa:53 (RSA) |   256 1f:77:31:19:de:b0:e1:6d:ca:77:07:76:84:d3:a9:a0 (ECDSA) |_  256 0e:85:71:a8:a2:c3:08:69:9c:91:c0:3f:84:18:df:ae (ED25519) | ssh-publickey-acceptance:  |_  Accepted Public Keys: No public keys accepted |_ssh-run: Failed to specify credentials and command to run. | ssh2-enum-algos:  |   kex_algorithms: (6) |       curve25519-sha256@libssh.org |       ecdh-sha2-nistp256 |       ecdh-sha2-nistp384 |       ecdh-sha2-nistp521 |       diffie-hellman-group-exchange-sha256 |       diffie-hellman-group14-sha1 |   server_host_key_algorithms: (4) |       ssh-rsa |       ssh-dss |       ecdsa-sha2-nistp256 |       ssh-ed25519 |   encryption_algorithms: (6) |       aes128-ctr |       aes1...