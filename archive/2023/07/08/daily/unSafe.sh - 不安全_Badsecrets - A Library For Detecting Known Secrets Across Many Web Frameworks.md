---
title: Badsecrets - A Library For Detecting Known Secrets Across Many Web Frameworks
url: https://buaq.net/go-171490.html
source: unSafe.sh - 不安全
date: 2023-07-08
fetch_date: 2025-10-04T11:52:22.464036
---

# Badsecrets - A Library For Detecting Known Secrets Across Many Web Frameworks

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

![](https://8aqnet.cdn.bcebos.com/6bf7772704866106a9e5f1c6a1ab8503.jpg)

Badsecrets - A Library For Detecting Known Secrets Across Many Web Frameworks

A pure python library for identifying the use of known or very weak cryptographic secrets
*2023-7-7 20:30:0
Author: [www.kitploit.com(查看原文)](/jump-171490.htm)
阅读量:21
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjtrwVHCUpOcR4Rgbs1P2vHYMsCZX17A82o3QF3Ls4H7GI91tmYzAwks9B0582qIo5_DlWyi4ZK4xwxSk6PZal4tnBJ8WebuN9V_5maK8-SVqfs7B_j-Z_VENCaMT-TGLqD-GslgkJzMpCwDUSNVcplHfuIJXYUCur4p-8F76cp2CFCjCNoju2TQfJTEQ=w640-h640)](https://blogger.googleusercontent.com/img/a/AVvXsEjtrwVHCUpOcR4Rgbs1P2vHYMsCZX17A82o3QF3Ls4H7GI91tmYzAwks9B0582qIo5_DlWyi4ZK4xwxSk6PZal4tnBJ8WebuN9V_5maK8-SVqfs7B_j-Z_VENCaMT-TGLqD-GslgkJzMpCwDUSNVcplHfuIJXYUCur4p-8F76cp2CFCjCNoju2TQfJTEQ)

A pure [python library](https://www.kitploit.com/search/label/Python%20Library "python library") for identifying the use of known or very weak cryptographic secrets across a variety of platforms. The project is designed to be both a repository of various "known secrets" (for example, ASP.NET machine keys found in examples in tutorials), and to provide a language-agnostic abstraction layer for identifying their use.

Knowing when a 'bad secret' was used is usually a matter of examining some cryptographic product in which the secret was used: for example, a cookie which is signed with a keyed hashing algorithm. Things can get complicated when you dive into the individual implementation oddities each platform provides, which this library aims to alleviate.

Check out our full [blog post](https://blog.blacklanternsecurity.com/p/introducing-badsecrets "blog post") on the Black Lantern Security blog!

Inspired by [Blacklist3r](https://github.com/NotSoSecure/Blacklist3r "Blacklist3r"), with a desire to expand on the supported platforms and remove language and operating system dependencies.

## Current Modules

| Name | Description |
| --- | --- |
| ASPNET\_Viewstate | Checks the viewstate/generator against a list of known machine keys. |
| Telerik\_HashKey | Checks patched (2017+) versions of Telerik UI for a known Telerik.Upload.ConfigurationHashKey |
| Telerik\_EncryptionKey | Checks patched (2017+) versions of Telerik UI for a known Telerik.Web.UI.DialogParametersEncryptionKey |
| Flask\_SignedCookies | Checks for weak Flask cookie signing password. Wrapper for [flask-unsign](https://github.com/Paradoxis/Flask-Unsign "flask-unsign") |
| Peoplesoft\_PSToken | Can check a peoplesoft PS\_TOKEN for a bad/weak signing password |
| Django\_SignedCookies | Checks django's session cookies (when in signed\_cookie mode) for known django secret\_key |
| Rails\_SecretKeyBase | Checks [Ruby on Rails](https://www.kitploit.com/search/label/Ruby%20on%20Rails "Ruby on Rails") signed or encrypted session cookies (from multiple major releases) for known secret\_key\_base |
| Generic\_JWT | Checks JWTs for known HMAC secrets or RSA private keys |
| Jsf\_viewstate | Checks Both Mojarra and Myfaces implimentations of Java Server Faces (JSF) for use of known or weak secret keys |
| Symfony\_SignedURL | Checks symfony "\_fragment" urls for known HMAC key. Operates on Full URL, including hash |
| Express\_SignedCookies | Checks express.js signed cookies and session cookies for known 'session secret' |
| Laravel\_SignedCookies | Checks 'laravel\_session' cookies for known laravel 'APP\_KEY' |

## Installation

We have a [pypi](https://pypi.org/project/badsecrets/ "pypi") package, so you can just do `pip install badsecrets` to make use of the library.

## Simple Usage

The absolute easiest way to use Badsecrets is by simply running `badsecrets` after doing a pip install:

```
pip install badsecrets
```

This is doing the same thing as the `cli.py` example shown below.

## Examples

To use the examples, after doing the pip install just `git clone` the repo and `cd` into the `badsecrets` directory:

```
git clone https://github.com/blacklanternsecurity/badsecrets.git
cd badsecrets
```

The commands in the example section below assume you are in this directory.

If you are using the Badsecrets [BBOT](https://github.com/blacklanternsecurity/bbot "BBOT") module, you don't need to do anything else - BBOT will install the package for you.

### cli.py

Bad secrets includes an [example CLI](https://github.com/blacklanternsecurity/badsecrets/blob/dev/examples/cli.py "example CLI") for convenience when manually checking secrets. It also has a URL mode, which will connect to a target and attempt to carve for cryptographic products and check any it finds against all modules.

* Basic usage - checking a crytographic product for a known secret (against all modules):

```
python ./badsecrets/examples/cli.py eyJhbGciOiJIUzI1NiJ9.eyJJc3N1ZXIiOiJJc3N1ZXIiLCJVc2VybmFtZSI6IkJhZFNlY3JldHMiLCJleHAiOjE1OTMxMzM0ODMsImlhdCI6MTQ2NjkwMzA4M30.ovqRikAo_0kKJ0GVrAwQlezymxrLGjcEiW_s3UJMMCo
```

* URL Mode - Connecting to a target and carving for a cryptographic product, and if found checking it for known secrets (against all modules):

```
python ./badsecrets/examples/cli.py --url http://example.com/contains_bad_secret.html
```

You can also set a custom user-agent with `--user-agent "user-agent string"` or a proxy with `--proxy http://127.0.0.1` in this mode.

Example output:

command line interface \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Known Secret Found! Detecting Module: Generic\_JWT Secret: 1234 Details: {'Issuer': 'Issuer', 'Username': 'BadSecrets', 'exp': 1593133483, 'iat': 1466903083, 'jwt\_headers': {'alg': 'HS256'}} \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*" dir="auto">

```
$ python ./badsecrets/examples/cli.py eyJhbGciOiJIUzI1NiJ9.eyJJc3N1ZXIiOiJJc3N1ZXIiLCJVc2VybmFtZSI6IkJhZFNlY3JldHMiLCJleHAiOjE1OTMxMzM0ODMsImlhdCI6MTQ2NjkwMzA4M30.ovqRikAo_0kKJ0GVrAwQlezymxrLGjcEiW_s3UJMMCo
badsecrets - example command line interface

***********************
Known Secret Found!

Detecting Module: Generic_JWT

Secret: 1234
Details: {'Issuer': 'Issuer', 'Username': 'BadSecrets', 'exp': 1593133483, 'iat': 1466903083, 'jwt_headers': {'alg': 'HS256'}}
***********************
```

### Blacklist3r.py

Bad secrets includes a [fully functional CLI example](https://github.com/blacklanternsecurity/badsecrets/blob/dev/badsecrets/examples/blacklist3r.py "fully functional CLI example") which replicates the functionality of [blacklist3r](https://github.com/NotSoSecure/Blacklist3r "blacklist3r") in python badsecrets/examples/blacklist3r.

```
python ./badsecrets/examples/blacklist3r.py --url http://vulnerablesite/vulnerablepage.aspx
python ./badsecrets/examples/blacklist3r.py --viewstate /wEPDwUJODExMDE5NzY5ZGQMKS6jehX5HkJgXxrPh09vumNTKQ== --generator EDD8C9AE
```

### Telerik\_knownkey.py

Fully functional CLI example for identifying known Telerik Hash keys and [Encryption](https://www.kitploit.com/search/label/Encryption "Encryption") keys for Post-2017 versions (those patched for CVE-2017-9248), and brute-forcing version / generating [exploitation](https://www.kitploit.com/search/label/Exploitation "exploitation") DialogParameters values.

```
python ./badsecrets/examples/telerik_knownkey.py --url http://vulnerablesite/Telerik.Web.UI.DialogHandler.aspx
```

Optionally include ASP.NET MachineKeys with --machine-keys (Will SIGNIFICANTLY increase brute-forcing time)

### Symfony\_knownkey.py

Brute-force detection of Symfony known secret key when "\_fragment" URLs are enabled, even when no example URL containing a hash can be located. [Relevent Blog Post](https://www.ambionics.io/blog/symfony-secret-fragment "Relevent Blog Post").

```
python ./badsecrets/exampl...