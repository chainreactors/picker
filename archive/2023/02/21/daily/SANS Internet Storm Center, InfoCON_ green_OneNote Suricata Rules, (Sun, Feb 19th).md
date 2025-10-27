---
title: OneNote Suricata Rules, (Sun, Feb 19th)
url: https://isc.sans.edu/diary/rss/29564
source: SANS Internet Storm Center, InfoCON: green
date: 2023-02-21
fetch_date: 2025-10-04T07:39:10.722219
---

# OneNote Suricata Rules, (Sun, Feb 19th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29562)
* [next](/diary/29570)

# [OneNote Suricata Rules](/forums/diary/OneNote%2BSuricata%2BRules/29564/)

**Published**: 2023-02-19. **Last Updated**: 2023-02-20 07:46:06 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/OneNote%2BSuricata%2BRules/29564/#comments)

I end my diary entry “[Detecting (Malicious) OneNote Files](https://isc.sans.edu/diary/Detecting%2BMalicious%2BOneNote%2BFiles/29494)” with a set of Suricata [rules to detect various OneNote files](https://github.com/DidierStevens/Beta/blob/master/onenote.rules).

Let’s take a closer look at these rules.

Here is the first rule, that I split over several lines so that each option has it own line, making it easier to explain.

```

alert http any any -> any any (
msg:"[MS-ONESTORE] .one GUID";
flow:established,from_server;
file_data;
content:"|E4 52 5C 7B 8C D8 A7 4D AE B1 53 78 D0 29 96 D3|";
classtype:policy-violation;
reference:url,blog.didierstevens.com;
reference:url,github.com/Neo23x0/signature-base/blob/master/yara/gen_onenote_phish.yar;
sid:1000001;
rev:1;)
```

The rule inspects HTTP traffic and triggers an alert when the right conditions are met.

The rule looks at any origin (any any) and any destination (any any). Usually, you would want to refine such a rule, to inspect HTTP traffic with requests originating from inside your network ($HOME\_NET) and destined outside your network ($EXTERNAL\_NET), typically the Internet.

Then follow all the rule’s options (between parantheses).

Option msg specifies the message to be displayed when this rule triggers.

Option flow specifies what traffic we want to look at: the connection has to be established (for TCP, this means that the three way handshake must have taken place) and the rule inspects data coming from the server.

file\_data is a sticky buffer that defines what data the following options (like content) should inspect. file\_data is the data (body) of the replies (and also requests), excluding the headers. If the data is GZip compressed, it will be decompressed prior to inspection.

content is the heart of the rule: it specifies a byte sequence (hexadecimal digits between | |) that has to be found inside the server’s reply for the rule to trigger. These hexadecimal values represent the GUID ({7B5C52E4-D88C-4DA7-AEB1-5378D02996D3}) that is found at the start of a OneNote file.
Remark that the content option here will look further into the file\_data than just the beginning. How deep depends on your Suricata configuration.
The options that follow the content option, are there for administration and documentation.

To summarize: this rule generates an alert when it finds the byte sequence for a particular GUID inside the body of the reply of a web server. So this rule will not only trigger on OneNote files, but also on data that contains the GUID somewhere else than at the beginning, for example contained in uncompressed archive files. If you want this rule to only trigger when the GUID is found at the start of the data, then you can use extra options (after option content) like depth and offset, although the simplest way to achieve this is just to add option startswith after the content option.

The second rule is very similar to the first rule, except that it searches for another GUID ({BDE316E7-2665-4511-A4C4-8D4D0B7A9EAC}):

```

content:"|E7 16 E3 BD 65 26 11 45 A4 C4 8D 4D 0B 7A 9E AC|";
```

This GUID is present when a OneNote file contains embedded files (it's the start of a [FileDataStoreObject structure](https://learn.microsoft.com/en-us/openspecs/office_file_formats/ms-onestore/8806fd18-6735-4874-b111-227b83eaac26)).

The remaining rules all detect traffic with this FileDataStoreObject structure, but for a particular file type that is often malicious when embedded.

Like the first of the remaining rules: it looks for embedded Windows executables (PE files):

```

content:"|E7 16 E3 BD 65 26 11 45 A4 C4 8D 4D 0B 7A 9E AC|";
content:"MZ";
distance:20;
within:2;
```

So first the rule looks for the FileDataStoreObject GUID anywhere in the file\_data.

Then it searches for string MZ, that's the magic sequence of a PE file. But MZ has to be present at a particular position: 20 bytes after the GUID (distance:20), that's where the embedded file data starts. And it is restricted to inspecting the first 2 bytes (within:2) at this position.

Then there are 2 rules for .BAT and .VBS files. Since this file type can start with anything, the rule looks for typical hearders we have seen with OneNote payloads:

```

content:"@echo off";
nocase;
distance:20;
within:9;

```

```

content:"|E7 16 E3 BD 65 26 11 45 A4 C4 8D 4D 0B 7A 9E AC|";
content:"on error";
nocase;
distance:20;
within:8;
```

Just like the rule for PE files, these rules look for a string ("@echo off" and "on error") at the beginning of the embedded file. There's one difference: the string mathcing is not case-sensitive (nocase option).

Then there's a rule for embedded .LNK files (the magic sequence for LNK files is a uppercase L followed by 3 NULLs).

```

content:"|E7 16 E3 BD 65 26 11 45 A4 C4 8D 4D 0B 7A 9E AC|";
content:"L|00 00 00|";
distance:20;
within:4;
```

And finally, there are 2 rules for embedded .hta files.

Here are the relevant options of the first .hta rule:

```

content:"|E7 16 E3 BD 65 26 11 45 A4 C4 8D 4D 0B 7A 9E AC|";
content:"<HTA:APPLICATION";
nocase;
distance:20;
```

It searches for string "<HTA:APPLICATION" inside the embedded file. Not just at the start of the embedded file (distance:20), but also further down the file: that's why there is no within option for this rule. But since the search is not limited (no within), the rule will also search beyond the embedded file.

To avoid this, I have my last rule (relevant options only):

```

content:"|E7 16 E3 BD 65 26 11 45 A4 C4 8D 4D 0B 7A 9E AC|";
byte_extract:8,0,size,relative,little;
content:"<HTA:APPLICATION";
nocase;
distance:20;
within:size;
```

To know the size of the embedded file, I have to read an integer right after the FileDataStoreObject GUID. I do this with option byte\_extract: I read an 8 byte-long (8) little-endian integer (little) into variable size. This integer starts directly after the FileDataStoreObject GUID: offset 0 relative to the last content match. And then, I can limit the search for string "<HTA:APPLICATION" to the size of the embedded file: within:size.

As I said in my previous OneNote diary entry, I have not tested these rules in a production environment. If you would want to do this, first decide which rules you want to use. The first 2 rules for example, just detect OneNote files, regardless of embedded payloads (with some degree of false positives), so these might generate too much alerts for your environment.

The other rules look for specific payloads, some of them can be easily bypassed (.bat and .vbs) rules by changing the start of the embedded .bat and/or .vbs file.

Didier Stevens
Senior handler
Microsoft MVP
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/OneNote%2BSuricata%2BRules/29564/#comments)

* [previous](/diary/29562)
* [next](/diary/29570)

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
 ...