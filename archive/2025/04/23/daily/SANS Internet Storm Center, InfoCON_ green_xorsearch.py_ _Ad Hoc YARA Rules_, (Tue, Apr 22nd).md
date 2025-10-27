---
title: xorsearch.py: "Ad Hoc YARA Rules", (Tue, Apr 22nd)
url: https://isc.sans.edu/diary/rss/31856
source: SANS Internet Storm Center, InfoCON: green
date: 2025-04-23
fetch_date: 2025-10-06T22:09:24.051725
---

# xorsearch.py: "Ad Hoc YARA Rules", (Tue, Apr 22nd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31854)
* [next](/diary/31858)

# [xorsearch.py: "Ad Hoc YARA Rules"](/forums/diary/xorsearchpy%2BAd%2BHoc%2BYARA%2BRules/31856/)

**Published**: 2025-04-22. **Last Updated**: 2025-04-22 05:31:49 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/xorsearchpy%2BAd%2BHoc%2BYARA%2BRules/31856/#comments)

In diary entry "[xorsearch.py: Searching With Regexes](https://isc.sans.edu/diary/xorsearchpy%2BSearching%2BWith%2BRegexes/31854/)" I showed how one can let [xorsearch.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/xorsearch.py) generate a YARA rule with a given regular expression.

This is a feature in many of my tools that support YARA, and I call it "[Ad Hoc Yara Rules](https://blog.didierstevens.com/2019/12/31/yara-ad-hoc-rules/)": rules that are created on the spot with your input.

Here is the example from my previous diary entry:

![](https://isc.sans.edu/diaryimages/images/20250421-102206.png)

The regular expression is:

```

\d+\.\d+\.\d+\.\d+
```

It matches one or more digits (\d+) followed by a dot (\.) followed by one or more digits (\d+) followed by a dot (\.) followed by one or more digits (\d+) followed by a dot (\.) followed by one or more digits (\d+).

To instruct my tool xorsearch.py to generate a YARA rule for this regular expression, one uses the prefix #r#, like this (r stands for regex):

```

#r#\d+\.\d+\.\d+\.\d+
```

This generates the following YARA rule:

```

rule regex {

    strings:

        $a = /\d+\.\d+\.\d+\.\d+/ ascii wide nocase

    condition:

        $a

}
```

The rule uses modifiers ascii, wide and nocase for the regular instruction. Thus the regex will match ASCII and UNICODE strings, regardless of case.

To view the YARA rule generate by my tools, use option -V (verbose):

![](https://isc.sans.edu/diaryimages/images/20250421-102807.png)

This works for simple strings too, when you use prefix #s#:

![](https://isc.sans.edu/diaryimages/images/20250421-103347.png)

And for hexadecimal too, using prefix #x#:

![](https://isc.sans.edu/diaryimages/images/20250421-103645.png)

If you can write your YARA rule in a single line, you can also pass it along as an option using prefix #, like this:

![](https://isc.sans.edu/diaryimages/images/20250421-104407.png)

This uses the following custom YARA rule (it searches for data that starts with ABC) :

```

rule hexadecimal {strings: $x = { 41 42 43 } condition: $x at 0}
```

If you can't write a YARA rule on the command-line (because it is too complex, or you want to use characters that you can't escape), then there are several solutions.

If you want to use a double-quote character in Windows cmd.exe:

![](https://isc.sans.edu/diaryimages/images/20250421-105202.png)

One solution is to use prefix #q# and replace double quotes with single quotes, like this:

![](https://isc.sans.edu/diaryimages/images/20250421-105502.png)

The tool will then replace all your single quotes with double quotes.

For more complex situations, you can use BASE64 and hexadecimal encoding. Encode the complete rule, and pass it along on the command-line in encoded form.

Take for example my YARA rule [contains\_pe\_file.yara](https://github.com/DidierStevens/DidierStevensSuite/blob/master/contains_pe_file.yara) that is designed to find PE files in binary data:

![](https://isc.sans.edu/diaryimages/images/20250421-105947.png)Converting this rule to BASE64 gives

```

LyoNCiAgVmVyc2lvbiAwLjAuMSAyMDE0LzEyLzEzDQogIFNvdXJjZSBjb2RlIHB1dCBpbiBwdWJsaWMgZG9tYWluIGJ5IERpZGllciBTdGV2ZW5zLCBubyBDb3B5cmlnaHQNCiAgaHR0cHM6Ly9EaWRpZXJTdGV2ZW5zLmNvbQ0KICBVc2UgYXQgeW91ciBvd24gcmlzaw0KDQogIFNob3J0Y29taW5ncywgb3IgdG9kbydzIDstKSA6DQoNCiAgSGlzdG9yeToNCiAgICAyMDE0LzEyLzEzOiBzdGFydA0KICAgIDIwMTQvMTIvMTU6IGRvY3VtZW50YXRpb24NCiovDQoNCnJ1bGUgQ29udGFpbnNfUEVfRmlsZQ0Kew0KICAgIG1ldGE6DQogICAgICAgIGF1dGhvciA9ICJEaWRpZXIgU3RldmVucyAoaHR0cHM6Ly9EaWRpZXJTdGV2ZW5zLmNvbSkiDQogICAgICAgIGRlc2NyaXB0aW9uID0gIkRldGVjdCBhIFBFIGZpbGUgaW5zaWRlIGEgYnl0ZSBzZXF1ZW5jZSINCiAgICAgICAgbWV0aG9kID0gIkZpbmQgc3RyaW5nIE1aIGZvbGxvd2VkIGJ5IHN0cmluZyBQRSBhdCB0aGUgY29ycmVjdCBvZmZzZXQgKEFkZHJlc3NPZk5ld0V4ZUhlYWRlcikiDQogICAgc3RyaW5nczoNCiAgICAgICAgJGEgPSAiTVoiDQogICAgY29uZGl0aW9uOg0KICAgICAgICBmb3IgYW55IGkgaW4gKDEuLiNhKTogKHVpbnQzMihAYVtpXSArIHVpbnQzMihAYVtpXSArIDB4M0MpKSA9PSAweDAwMDA0NTUwKQ0KfQ0K
```

And this can then be used on the command-line like this:

![](https://isc.sans.edu/diaryimages/images/20250421-110430.png)

And the same can be done when the rule is converted to hexadecimal, by using prefix #h#:

```

2f2a0d0a202056657273696f6e20302e302e3120323031342f31322f31330d0a2020536f7572636520636f64652070757420696e207075626c696320646f6d61696e206279204469646965722053746576656e732c206e6f20436f707972696768740d0a202068747470733a2f2f44696469657253746576656e732e636f6d0d0a202055736520617420796f7572206f776e207269736b0d0a0d0a202053686f7274636f6d696e67732c206f7220746f646f2773203b2d29203a0d0a0d0a2020486973746f72793a0d0a20202020323031342f31322f31333a2073746172740d0a20202020323031342f31322f31353a20646f63756d656e746174696f6e0d0a2a2f0d0a0d0a72756c6520436f6e7461696e735f50455f46696c650d0a7b0d0a202020206d6574613a0d0a2020202020202020617574686f72203d20224469646965722053746576656e73202868747470733a2f2f44696469657253746576656e732e636f6d29220d0a20202020202020206465736372697074696f6e203d202244657465637420612050452066696c6520696e73696465206120627974652073657175656e6365220d0a20202020202020206d6574686f64203d202246696e6420737472696e67204d5a20666f6c6c6f77656420627920737472696e672050452061742074686520636f7272656374206f66667365742028416464726573734f664e657745786548656164657229220d0a20202020737472696e67733a0d0a20202020202020202461203d20224d5a220d0a20202020636f6e646974696f6e3a0d0a2020202020202020666f7220616e79206920696e2028312e2e2361293a202875696e7433322840615b695d202b2075696e7433322840615b695d202b20307833432929203d3d2030783030303034353530290d0a7d0d0a
```

![](https://isc.sans.edu/diaryimages/images/20250421-110710.png)

To summarize, the prefixes you can use for Ad Hoc YARA rules are:

| Prefix | Explanation |
| --- | --- |
| #s# | search string (ascii wide nocase) |
| #x# | search hexadecimal sequence |
| #r# | search regex (ascii wide nocase) |
| # | literal YARA rule |
| #q# | encoded YARA rule: replaces single quote (') with double quote (") |
| #b# | encoded YARA rule; uses BASE64 to decode |
| #h# | encoded YARA rule; uses hexadecimal to decode |

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/xorsearchpy%2BAd%2BHoc%2BYARA%2BRules/31856/#comments)

* [previous](/diary/31854)
* [next](/diary/31858)

### Comments

[Login here to join the discussion.](/login)

Top of page

×

![modal content]()

[Diary Archives](/diaryarchive.html)

* [![SANS.edu research journal](https://isc.sans.edu/images/researchjournal5.png)](/j/research)
* [Homepage](/index.html)
* [Diaries](/diaryarchive.html)
* [Podcasts](/podcast.html)
* [Jobs](/jobs)
* [Data](/data)
  + [TCP/UDP Port Activity](/data/port.html)
  + [Port Trends](/data/trends.html)
  + [SSH/Telnet Scanning Activity](/data/ssh.html)
  + [Weblogs](/weblogs)
  + [Domains](/data/domains.html)
  + [Threat Feeds Activity](/data/threatfeed.html)
  + [Threat Feeds Map](/data/threatmap.html)
  + [Useful InfoSec Links](/data/links.html)
  + [Presentations & Papers](/data/presentation.html)
  + [Research Papers](/data/researchpapers.html)
  + [API](/api)
* [Tools](/tools/)
  + [DShield Sensor](/howto.html)
  + [DNS Looking Glass](/tools/dnslookup)
  + [Honeypot (RPi/AWS)](/tools/honeypot)
  + [InfoSec Glossary](/tools/glossary)
* [Contact Us](/contact.html)
  + [Contact Us](/contact.html)
  + [About Us](/about.html)
  + [Handlers](/handler_list.html)* [About Us](/about.html)

[Slack ...