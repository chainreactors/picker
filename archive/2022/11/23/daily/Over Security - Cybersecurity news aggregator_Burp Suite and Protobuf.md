---
title: Burp Suite and Protobuf
url: https://security.humanativaspa.it/burp-suite-and-protobuf/
source: Over Security - Cybersecurity news aggregator
date: 2022-11-23
fetch_date: 2025-10-03T23:30:52.099050
---

# Burp Suite and Protobuf

[![logo](https://hnsecurity.it/wp-content/uploads/2025/09/HN_Security_v2.svg)](https://hnsecurity.it/)

* [Home](https://hnsecurity.it)
* [Company](https://hnsecurity.it/company/)
* [Services](https://hnsecurity.it/services/)
  + [Red Teaming](https://hnsecurity.it/services/red-teaming/)
  + [DORA TLPT](https://hnsecurity.it/services/threat-led-penetration-test-dora/)
  + [AI Red Teaming](https://hnsecurity.it/services/ai-red-teaming/)
  + [Network Assessment](https://hnsecurity.it/services/network-assessment/)
  + [Web Assessment](https://hnsecurity.it/services/web-application-assessment/)
  + [Mobile Assessment](https://hnsecurity.it/services/mobile-application-assessment/)
  + [Mainframe Assessment](https://hnsecurity.it/services/mainframe-assessment/)
  + [Cloud Assessment](https://hnsecurity.it/services/cloud-assessment/)
  + [OT Assessment](https://hnsecurity.it/services/ot-assessment/)
  + [IoT Assessment](https://hnsecurity.it/services/iot-assessment/)
  + [Hardware Assessment](https://hnsecurity.it/services/hardware-assessment/)
  + [Security by Design](https://hnsecurity.it/services/security-by-design/)
* [Blog](https://hnsecurity.it/blog/)
* [Careers](https://hnsecurity.it/careers/)
* [Contacts](https://hnsecurity.it/contacts/)
* [![Italian](https://hnsecurity.it/wp-content/plugins/sitepress-multilingual-cms/res/flags/it.svg)](https://hnsecurity.it/it/blog/burp-suite-and-protobuf/ "Switch to ")

Get in touch

info@hnsecurity.it

![](https://hnsecurity.it/wp-content/uploads/2025/09/GOOGLE-DEV-uai-836x836.jpg)

# Burp Suite and Protobuf

November 22, 2022|[![Federico Dotta](https://hnsecurity.it/wp-content/uploads/2025/09/Dotta-sm-150x150.jpg)](https://hnsecurity.it/blog/author/federico-dotta/)By [Federico Dotta](https://hnsecurity.it/blog/author/federico-dotta/)

[Tools](https://hnsecurity.it/blog/category/tools/ "View all posts in Tools")

Hi,

Last year (I know, I’m “a little” late with this article 😀 ) I tested a couple of applications that employed the [Protocol Buffers](https://developers.google.com/protocol-buffers) data format (aka “Protobuf”) to serialize data transmitted using the HTTP protocol. Protobuf serializes data in **binary format**, not the ideal situation from a penetration tester’s perspective. So, as usual, I first searched for a [Burp Suite extension](https://portswigger.net/bappstore) able to deserialize/serialize Protobuf messages, in order to be able to inspect and tamper requests and responses in a more comfortable way.

In the BApp Store there is an extension named [protobuf-decoder](https://portswigger.net/bappstore/bd8c70d3f1b74679b2a9fed03d36e81a) created for this purpose. I installed and tried it. Unfortunately, this extension has **a lot of bugs** and **many functionalities are only partially implemented**, which seems to indicate that something went wrong probably in the code added in the last releases. Furthermore, it is not clear who the maintainer is, because the [PortSwigger’s fork of the extension](https://github.com/portswigger/protobuf-decoder) is 37 commits ahead of the forked repository of a potential owner/maintainer (that is in turn a fork of another repository).

By the way, my target applications were quite complex and I really needed to overcome the Protobuf inspection/tampering problem. So I **fixed many bugs** in the extension and implemented some **new features** that I needed. The code is in [my protobuf-decoder fork](https://github.com/federicodotta/protobuf-decoder). I will not open a pull request because my code was developed quickly for a specific need, and some of the changes I made were tested only during a couple of engagements and may not work in every situation (and probably the extension has no maintainer at the moment anyway). My advice is to use my version if possible, because the one currently in the store has too many bugs to be reliable.

Beside fixing all the bugs that I noticed, the main need I had was to handle applications that defined a lot of **custom “proto” definition files**, which are files that describe Protobuf data structures (**called “messages”**) and services that will be used by the application. In detail, I had to solve the following issues:

* These tons of proto files have multiple dependencies between them and it was necessary to import the proto files in the correct order (not easy when you have tens of hundreds of proto files with multiple dependencies)
* Most proto files contained “nested messages”, which means that many data structures were inside the same “proto” file

I implemented some functions that **recursively import proto files** this way: if a proto depends on another one that is still not loaded, the extension looks for the missing proto in the same directory (this process is executed recursively because maybe the missing proto depends on another proto, and so on…). Recursive import also handles nested messages, creating a tree structure accessible from the right-button menu that shows all loaded messages in a parent/child relationship.

Another issue I observed was that the original extension tried to deserialize Protobuf data using each loaded message, stopping at the first message that does not throw a parsing exception. In case no proto is loaded or none of the supplied protos works, the packed “protoc” binary is executed with the “decode\_raw” option, which gives a “raw” representation of the serialized data for inspection (please note that without a valid proto file, data cannot be tampered and serialized again). This is not the best way to handle complex applications, because the fact that deserialization does not throw an exception definitely does not mean that the correct message descriptor has been selected, especially when working on applications with a lot of different protos and messages. Often a wrong proto is selected, maybe due to similarities in the protos that partially match the serialized data. To overcome this limitation I added a **context-menu option that can be used to choose which message we want to use for the deserialization**, as follows (the picture is highly obfuscated, sorry about that):

![](https://hnsecurity.it/wp-content/uploads/2022/11/ProtobufEdited-1.png)

**By default, if no message is selected**, my version of the extension shows the “raw” representation because this way we don’t miss any data due to deserialization using a wrong proto message. If you prefer otherwise, **two alternative implementations** are included in the code (commented). The first one is the original one that tries to decode with every loaded messages, stopping at the first that does not throw an error. The second one, useful to quickly identify the right proto message to use, tries to decode the data with all the loaded proto messages without stopping at the first that match and prints the results on the standard output.

Here’s a **full list of the changes** I made to the original extension:

* **Recursive import** was added: now if a proto depends on another one, the extension looks in the same folder to find it. All messages showed in the previous screenshot have been recursively loaded as dependencies of a single proto file
* The extension now handles **nested messages** (messages that contain other messages) in a recursive manner and it is possible to choose any available proto in the tree for deserialization
* A filter was added to **search** for a specific proto file, necessary because we had a lot of messages types and their number made them very difficult to find in the context menu
* A lot of **bug fixes** in the code present in the Portswigger BAppStore were applied
* **Protobuf library was updated** to one of the last versions compatible with Python2
* Protobuf library was fixed in a couple of points because it uses a bytearray Python structure not fully compatible with Jython (a small patch but quite difficult to debug)
* The extension used a **deprecated** technique in the deserialization routines that has been rep...