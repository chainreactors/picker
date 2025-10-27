---
title: Reversing A Network Protocol
url: https://buaq.net/go-241555.html
source: unSafe.sh - 不安全
date: 2024-05-26
fetch_date: 2025-10-06T16:49:05.844440
---

# Reversing A Network Protocol

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

![](https://8aqnet.cdn.bcebos.com/268f3123e5d2b118196970c27bc7e29b.jpg)

Reversing A Network Protocol

I also recorded a video for this blog post.I recently helped a colleague and friend with the
*2024-5-25 19:31:42
Author: [blog.didierstevens.com(查看原文)](/jump-241555.htm)
阅读量:12
收藏*

---

*I also recorded a [video](https://youtu.be/mj4S0hkqBxI) for this blog post.*

I recently helped a colleague and friend with the reversing of a network protocol to update an IOT device. As I can’t be more specific for the moment, I created a capture file similar to this network protocol to explain how one can reverse engineer a protocol like this with Wireshark and the [Lua dissector I developed](https://blog.didierstevens.com/2024/05/20/wireshark-lua-fixed-field-length-dissector-fl-dissector/).

This is how the traffic looks like (the pcapng file can be found inside the [ZIP file with the dissector](https://blog.didierstevens.com/2024/05/20/wireshark-lua-fixed-field-length-dissector-fl-dissector/).).

![](https://blog.didierstevens.com/wp-content/uploads/2024/05/20240520-214045.png)

The capture file I created contains TCP traffic to port 50500. The device has IPv4 address 127.0.0.2 and my machine 127.0.0.1.

First I perform a TCP follow:

![](https://blog.didierstevens.com/wp-content/uploads/2024/05/20240520-214112.png)
![](https://blog.didierstevens.com/wp-content/uploads/2024/05/20240520-214153.png)

In pink you have the packets sent by the client; the server packets are blue.

We can apply a filter to see these packets separately:

![](https://blog.didierstevens.com/wp-content/uploads/2024/05/20240520-214216.png)
![](https://blog.didierstevens.com/wp-content/uploads/2024/05/20240520-214251.png)

And here is the raw view:

![](https://blog.didierstevens.com/wp-content/uploads/2024/05/20240520-214317.png)

We can see that the client (Windows machine) is sending a lot of data, and that the server (IOT device) sends back packets up to 4 bytes in size.

To facilitate the analysis, it would be useful to have a dissector that splits up the TCP traffic into fields. It’s not necessary to write a custom Wireshark dissector for this, I can use my [fixed field length Lua dissector](https://blog.didierstevens.com/2024/05/20/wireshark-lua-fixed-field-length-dissector-fl-dissector/).

One way to load the dissector in Wireshark, is to start Wireshark from the command-line with options to load the dissector:

```
"c:\Program Files\Wireshark\Wireshark.exe" -X lua_script:fl-dissector.lua -X lua_script1:port:50500 capture-firmware-upload.pcapng
```

-X lua\_script:fl-dissector.lua loads the dissector when Wireshark starts. The file fl-dissector.lua has to be in the current folder.

I also have to specify the port (50500) for this dissector:

lua\_script1:port:50500

Wireshark will only invoke the dissector for TCP traffic coming from or going to the given port. If I don’t provide a port, the hard-coded port number (1234) will be used.

And finally, I provide the name of the capture file: capture-firmware-upload.pcapng

![](https://blog.didierstevens.com/wp-content/uploads/2024/05/20240520-224854.png)

This starts Wireshark and loads the dissector:

![](https://blog.didierstevens.com/wp-content/uploads/2024/05/20240520-235517.png)

When I select a packet with some traffic of interest, the result of the dissector appears in the Packet Details pane at the bottom of the protocols. Protocol dissector FLDISSECTOR shows two fields: Field1 and Field2. That’s the default field length definition: one field (Field1) of length 1 (1 byte long) and a second field (Field2) with the remaining TCP payload data.

Since I want a more descriptive protocol name, I’m stopping Wireshark and loading it again with an extra argument:

-X lua\_script1:protocolname:firmware

Argument protocolname allows me to specify the name of the dissector/protocol:

![](https://blog.didierstevens.com/wp-content/uploads/2024/05/20240520-225142.png)
![](https://blog.didierstevens.com/wp-content/uploads/2024/05/20240520-225010-1.png)

Next, I define the length of the fields with the protocol preferences dialog:

![](https://blog.didierstevens.com/wp-content/uploads/2024/05/20240520-225045.png)
![](https://blog.didierstevens.com/wp-content/uploads/2024/05/20240520-225159.png)

What you see here is “1”: one field with size 1 (1 byte long).

I define 4 fields, each on byte in size:

![](https://blog.didierstevens.com/wp-content/uploads/2024/05/20240520-225219.png)

If I select a packet with just 2 bytes of TCP payload, I get 2 fields:

![](https://blog.didierstevens.com/wp-content/uploads/2024/05/20240520-225350.png)

But when I select a packet with more than 4 bytes of TCP payload, I get 5 fields: 4 fields of 1 byte in size, and the last field with the remaining bytes of the TCP payload:

![](https://blog.didierstevens.com/wp-content/uploads/2024/05/20240520-225416.png)

Next, I add each field as a column in the Packet List pane:

![](https://blog.didierstevens.com/wp-content/uploads/2024/05/20240521-000919.png)
![](https://blog.didierstevens.com/wp-content/uploads/2024/05/20240521-000951.png)
![](https://blog.didierstevens.com/wp-content/uploads/2024/05/20240521-001050.png)

And I apply display filter “firmware” (the name I gave to the protocol I’m reversing) to see only packets with protocol data:

![](https://blog.didierstevens.com/wp-content/uploads/2024/05/20240521-001120.png)

Now I can start to see some patterns.

Field1 has values 10, 11 and 12. Remark that each field’s type is “bytes”, so this is hexadecimal. These are not numbers/integers, but bytes (I can change that later).

Field2 is equal to 00 when the destination is 127.0.0.2 (the “server”), and equal to 01 when the destination is 127.0.0.1.

This can be verified with display filters (useful when there is a lot of data that doesn’t fit the screen like here).

If my assumption is correct, there shouldn’t be any packets with Field1 equal to 00 and destination 127.0.0.1. I confirm this with display filter “firmware.field2 == 00: and ip.dst == 127.0.0.1”:

![](https://blog.didierstevens.com/wp-content/uploads/2024/05/20240524-171455.png)

And there shouldn’t be any packets with Field2 equal to 01 and destination 127.0.0.2. I confirm this with display filter “firmware.field2 == 01: and ip.dst == 127.0.0.2”:

![](https://blog.didierstevens.com/wp-content/uploads/2024/05/20240524-171743.png)

And when Field1 is 10 or 12, no data follows Field2 (Field3 and following are empty). Fields Field3 and following are only populated when Field1 is 11.

This too can be checked with display filters, should there be a lot of data that doesn’t fit on a single screen.

This is one advantage of a prototyping dissector like this one: it allows me to check my assumptions directly in Wireshark with display filters.

If there is any remaining data after all defined fields have been populated, this dissector will populate the next field with the remaining data. As I defined the length for 4 fields, Field5 contains that remaining data.

Taking a closer look at the data in field 5, I spot string PK: PK are the initials of Phil Katz, who invented the ZIP file format, and all ZIP records start with bytes 0x50 and 0x4B, e.g., PK:

![](https://blog.didierstevens.com/wp-content/uploads/2024/05/20240524-173144.png)

Byte sequence 50 4b 03 04 is the header of a ZIP File entry record. And if I look at the ASCII dump, I see “firmware.bin” about 30 bytes after PK. So this is very likely a ZIP file, and it is possible that the update protocol uses the ZIP file format. As there are 2 bytes preceding this PK header, I’m going to add 2 extra fields to capt...