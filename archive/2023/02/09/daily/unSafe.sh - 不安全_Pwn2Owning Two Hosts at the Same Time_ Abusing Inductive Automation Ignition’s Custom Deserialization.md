---
title: Pwn2Owning Two Hosts at the Same Time: Abusing Inductive Automation Ignition’s Custom Deserialization
url: https://buaq.net/go-148552.html
source: unSafe.sh - 不安全
date: 2023-02-09
fetch_date: 2025-10-04T06:05:09.599023
---

# Pwn2Owning Two Hosts at the Same Time: Abusing Inductive Automation Ignition’s Custom Deserialization

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

![](https://8aqnet.cdn.bcebos.com/893f194bd9ecef58298981371dad694f.jpg)

Pwn2Owning Two Hosts at the Same Time: Abusing Inductive Automation Ignition’s Custom Deserialization

Pwn2Own Miami 2022 was a fine competition. At the cont
*2023-2-8 23:55:1
Author: [www.thezdi.com(查看原文)](/jump-148552.htm)
阅读量:31
收藏*

---

Pwn2Own Miami 2022 was a fine competition. At the contest, I successfully exploited three different targets. In this blog post, I would like to show you my personal best research of the competition: the custom deserialization issue in Inductive Automation Ignition.

There are several things that make this vulnerability interesting, including the following:

·       It exists in a custom deserialization routine, which seems to derive some inspiration from the Java XMLDecoder.

Since the remote vector requires an authentication bypass, at Pwn2Own, I decided to keep it simple and stick with the local vector.

This vulnerability was discovered through static code analysis. My full write-up for the contest was 50 pages long. Here I will try my best to provide you with as much information as possible, while not producing a blog post of excessive length. First, here’s a quick video of the exploit in action, showing RCE on both the client and the server! I popped `calc.exe` on the client, whereas `cmd.exe /c whoami > C:\poc.txt` was executed on the server.

**Introduction to Ignition Projects**

According to the Ignition manual, projects are one of the two main components of this platform, the other component being Ignition Gateway. Projects allow you to specify views, data operations, reports and so forth. Moreover, an official [“Ignition Exchange”](https://www.inductiveautomation.com/exchange/) platform exists, which allows users to share their projects globally. This results in a very interesting vector, where a project file can be shared through the vendor’s website. Some of the projects I found have been downloaded hundreds of times. As file handling bugs in this product were in scope for this Pwn2Own, I decided to learn something more about project files.

Let’s have a quick look at project file structure. In recent Ignition versions, a project file is a ZIP-compressed archive containing multiple files and directories. We will highlight several basic components:
      -- `project.json` – this file contains basic information about the project, such as its name.
      -- `ignition\global-props` directory – this directory stores properties of the project. This directory will include files named `data.bin` and `resource.json`.
      -- `com.inductiveautomation.perspective` directory – this directory stores all the data concerning the visual aspects of the projects, such as page configurations, views and styles.
      -- `com.inductiveautomation.reporting` directory – this directory stores all the data concerning reports.

Every project contains multiple pairs of corresponding `data.bin` and `resource.json` files. The following screenshot presents several `data.bin` files that are included in the sample project delivered by the vendor:

*Figure 1 - Example of the data.bin files*

Some of these files contain JSON data, whereas others are gzip-compressed. Let’s open one of the gzip-compressed files in a text editor, after decompression:

*Figure 2 - Fragment of the exemplary data.bin file*

Red flags! This file contains:
       -- Full names of Java classes.
       -- Something that looks like setters.

At this stage, I knew that I was dealing with something interesting and that it involved a custom serialization mechanism. I decided to dig further and see where it leads.

**data.bin Handling and Two Deserializers**

The main class responsible for the handling of `data.bin` files is called `XMLDeserializer`. It implements multiple `deserialize` methods. The following code snippet presents the one that is interesting for us:

The method checks to see if the input is in a binary format by calling the `isBinaryFormat` function. Depending on the result, it calls either `deserializeBinary` or `deserializeXML`. This decision is based on a magic number stored in the first bytes of the file, and it is not interesting for us.

It seems that both the binary and XML deserializers can be used to achieve remote code execution. They are based on the same deserialization handling classes. I focused solely on the XML deserialization, as it seemed less error-prone and I did not want any surprises during the contest. I had no sample XML file and I had to recreate the format from scratch.

**Inner Workings of `XMLDeserializer`**

This section describes the main aspects of the Ignition `XMLDeserializer`. It contains a lot of source code, which may be hard to follow during the first read. Don’t worry, the end of this chapter contains a summary, which fully describes the deserialization scheme. If you feel overwhelmed by the amount of code, go straight to the end of this section.

Now, let’s have a look at the fragments of the `deserializeXML` function.

At [1], we see the reference to the `org.xml.sax.XMLReader`.

At [2], the `ParseContext` is created. This is an Ignition-specific class.

At [3], code initializes the `XMLParser` object. This is also an Ignition-specific class. The constructor accepts the `ParseContext` object as a parameter.

At [4], code sets the content handler of the SAX `XMLReader` to the `XMLParser`.

At [5], the XML is parsed.

It seems that the `XMLParser` and the `ParseContext` are the key objects here. They will define the behavior of the `XMLReader`. When we deal with the SAX `XMLReader`, we should see calls to two main methods:
       -- `startElement`, which will be called when a new element starts (like ).
       -- `endElement`, which will be called when an element ends (like ).

Let’s look at three main parts of `XMLParser`: the constructor, the `startElement` method and the `endElement` method.

The constructor basically sets the `context` member to the provided context (the `ParseContext` class implements the `ParsingHandler` interface, so we are good here).

Two lines can be highlighted here:
       -- The `subName` string is retrieved using the `getSubElementName` method.
       -- The code calls `this.context.onElementStart`, which accepts both `name` and `subName` as arguments.

We can skip a detailed analysis of the `endElement` method, as its functioning is analogous to the previously shown method:
       -- It retrieves the `subName` in the same way as `startElement` does.
       -- It calls `this.context.onElementEnd`.

We must investigate the `getSubElementName`, as it is something new and not typical for SAX.

As shown here, `getSubElementName` just checks if the element’s name contains either a colon or hyphen, and retrieves the part after the first such character. If there is no colon or hyphen it returns `null`.

At this point, we know that the `XMLDeserializer` will call the following two methods:
       -- `ParseContext.onElementStart` when an XML element starts.
       -- `ParseContext.onElementEnd` when an XML element ends.

These methods are crucial, as they define the whole behavior of the deserializer. Let’s have a look at the first of them.

We can see that this function implements special handling for an element with the name `objects`. This suggests an element containing serialized objects. We can also expect the function to act differently in response to “main” elements (no colon or hypen) versus sub-elements. Let’s start with the main elements.

For a main element, at [4] an object of type `DeserializationHandler` is retrieved via the `lookupHandler` method. An impo...