---
title: REcollapse Is A Helper Tool For Black-Box Regex Fuzzing To Bypass Validations And Discover Normalizations In Web Applications
url: https://buaq.net/go-161279.html
source: unSafe.sh - 不安全
date: 2023-05-02
fetch_date: 2025-10-04T11:38:34.552056
---

# REcollapse Is A Helper Tool For Black-Box Regex Fuzzing To Bypass Validations And Discover Normalizations In Web Applications

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

![](https://8aqnet.cdn.bcebos.com/ffc7af5e0898de12990cedb78b756ad2.jpg)

REcollapse Is A Helper Tool For Black-Box Regex Fuzzing To Bypass Validations And Discover Normalizations In Web Applications

REcollapse is a helper tool for black-box regex fuzzing to bypass validations and discover n
*2023-5-1 20:30:0
Author: [www.kitploit.com(查看原文)](/jump-161279.htm)
阅读量:39
收藏*

---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj0aeM5AY2sPDZs8jC4A1dnktU3PWPeQi7KuV3T4fjiIeWKqozn0jHOqdIrX3xmqd-zcrmYhwjdTcGQOeYu3hz3IQa6sXOpcSQexzEFJTiBONkApmFw0HDEmE1uEJi_zoz6FZZBoqPSGZqsSNJ1mkNudHXYmrUTBrE6nULBS688s9-iI4ssu5btWR5sUw/w640-h350/recollapse.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj0aeM5AY2sPDZs8jC4A1dnktU3PWPeQi7KuV3T4fjiIeWKqozn0jHOqdIrX3xmqd-zcrmYhwjdTcGQOeYu3hz3IQa6sXOpcSQexzEFJTiBONkApmFw0HDEmE1uEJi_zoz6FZZBoqPSGZqsSNJ1mkNudHXYmrUTBrE6nULBS688s9-iI4ssu5btWR5sUw/s1186/recollapse.png)

REcollapse is a helper tool for black-box [regex](https://www.kitploit.com/search/label/Regex "regex") [fuzzing](https://www.kitploit.com/search/label/Fuzzing "fuzzing") to bypass validations and [discover](https://www.kitploit.com/search/label/Discover "discover") normalizations in web applications.

It can also be helpful to bypass WAFs and weak [vulnerability](https://www.kitploit.com/search/label/Vulnerability "vulnerability") mitigations. For more information, take a look at the [REcollapse blog post](https://0xacb.com/2022/11/21/recollapse/ "REcollapse blog post").

The goal of this tool is to generate payloads for testing. Actual fuzzing shall be done with other tools like [Burp](https://portswigger.net/burp "Burp") (intruder), [ffuf](https://github.com/ffuf/ffuf "ffuf"), or similar.

### Installation

**Requirements**: Python 3

`pip3 install --user --upgrade -r requirements.txt` or `./install.sh`

**Docker**

`docker build -t recollapse .` or `docker pull 0xacb/recollapse`

### Usage

```
$ recollapse -h
```

```

```

### Detailed options explanation

Let's consider `this_is.an_example` as the input.

**Positions**

1. Fuzz the beginning of the input: `$this_is.an_example`
2. Fuzz the before and after special characters: `this$_$is$.$an$_$example`
3. Fuzz normalization positions: replace all possible bytes according to the [normalization table](https://0xacb.com/normalization_table "normalization table")
4. Fuzz the end of the input: `this_is.an_example$`

**Encoding**

1. URL-encoded format to be used with `application/x-www-form-urlencoded` or query parameters: `%22this_is.an_example`
2. Unicode format to be used with `application/json`: `\u0022this_is.an_example`
3. Raw format to be used with `multipart/form-data`: `"this_is.an_example`

**Range**

Specify a range of bytes for fuzzing: `-r 1-127`. This will exclude alphanumeric characters unless the `-an` option is provided.

**Size**

Specify the size of fuzzing for positions `1`, `2` and `4`. The default approach is to fuzz all possible values for one byte. Increasing the size will consume more resources and generate many more inputs, but it can lead to finding new bypasses.

**File**

Input can be provided as a positional argument, stdin, or a file through the `-f` option.

**Alphanumeric**

By default, alphanumeric characters will be excluded from output generation, which is usually not interesting in terms of responses. You can allow this with the `-an` option.

**Maximum number or normalizations**

Not all normalization libraries have the same behavior. By default, three possibilities for normalizations are generated for each input index, which is usually enough. Use the `-mn` option to go further.

**Normalization table**

Use the `-nt` option to show the normalization table.

### Example

```
$ recollapse -e 1 -p 1,2,4 -r 10-11 https://legit.example.com
%0ahttps://legit.example.com
%0bhttps://legit.example.com
https%0a://legit.example.com
https%0b://legit.example.com
https:%0a//legit.example.com
https:%0b//legit.example.com
https:/%0a/legit.example.com
https:/%0b/legit.example.com
https://%0alegit.example.com
https://%0blegit.example.com
https://legit%0a.example.com
https://legit%0b.example.com
https://legit.%0aexample.com
https://legit.%0bexample.com
https://legit.example%0a.com
https://legit.example%0b.com
https://legit.example.%0acom
https://legit.example.%0bcom
https://legit.example.com%0a
https://legit.example.com%0b
```

```

```

### Resources

This technique has been presented on [BSidesLisbon 2022](https://bsideslisbon.org/ "BSidesLisbon 2022")

**Blog post**: [https://0xacb.com/2022/11/21/recollapse/](https://0xacb.com/2022/11/21/recollapse/ "https://0xacb.com/2022/11/21/recollapse/")

**Slides**:

* [nahamcon\_2022\_eu\_till\_recollapse.pdf](https://github.com/0xacb/recollapse/blob/main/slides/nahamcon_2022_eu_till_recollapse.pdf "nahamcon_2022_eu_till_recollapse.pdf")
* [bsideslisbon\_2022\_till\_recollapse.pdf](https://github.com/0xacb/recollapse/blob/main/slides/bsideslisbon_2022_till_recollapse.pdf "bsideslisbon_2022_till_recollapse.pdf")

**Videos**:

* [NahamCon 2022 EU](https://www.youtube.com/watch?v=1eLTMKWciic "NahamCon 2022 EU")
* [BSidesLisbon 2022](https://www.youtube.com/watch?v=nb91qhj5cOE "BSidesLisbon 2022")

**Normalization table**: [https://0xacb.com/normalization\_table](https://0xacb.com/normalization_table "https://0xacb.com/normalization_table")

**Thanks**

* [@regala\_](https://twitter.com/regala_ "@regala_")
* [@0xz3z4d45](https://twitter.com/0xz3z4d45 "@0xz3z4d45")
* [@jllis](https://twitter.com/jllis "@jllis")
* [@samwcyo](https://twitter.com/samwcyo "@samwcyo")
* [@yassineaboukir](https://twitter.com/yassineaboukir "@yassineaboukir")
* [@0xteknogeek](https://twitter.com/0xteknogeek "@0xteknogeek")
* [@vgpinho](https://github.com/vgpinho "@vgpinho")
* **BBAC**

and

* [@ethiack](https://twitter.com/ethiack "@ethiack") team
* [@0xdisturbance](https://twitter.com/0xdisturbance "@0xdisturbance") team
* [@hacker0x01](https://twitter.com/hacker0x01 "@hacker0x01") team

REcollapse Is A Helper Tool For Black-Box Regex Fuzzing To Bypass Validations And Discover Normalizations In Web Applications
![REcollapse Is A Helper Tool For Black-Box Regex Fuzzing To Bypass Validations And Discover Normalizations In Web Applications](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj0aeM5AY2sPDZs8jC4A1dnktU3PWPeQi7KuV3T4fjiIeWKqozn0jHOqdIrX3xmqd-zcrmYhwjdTcGQOeYu3hz3IQa6sXOpcSQexzEFJTiBONkApmFw0HDEmE1uEJi_zoz6FZZBoqPSGZqsSNJ1mkNudHXYmrUTBrE6nULBS688s9-iI4ssu5btWR5sUw/s72-w640-c-h350/recollapse.png)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2023/05/recollapse-is-helper-tool-for-black-box.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)