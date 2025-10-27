---
title: Ermir - An Evil Java RMI Registry
url: https://buaq.net/go-133330.html
source: unSafe.sh - 不安全
date: 2022-10-31
fetch_date: 2025-10-03T21:20:47.610259
---

# Ermir - An Evil Java RMI Registry

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

![](https://8aqnet.cdn.bcebos.com/912cf999542fd2157603b7ce73e72d83.jpg)

Ermir - An Evil Java RMI Registry

Ermir is an Evil/Rogue RMI Registry, it exploits unsecure deserialization on any Java code c
*2022-10-30 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-133330.htm)
阅读量:37
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEi5M-qQI0jAEcuuEEaopyFsMT-DMUz_w8NCvWLibYBeKWmHqfFEISZ1QrpwKYbDsj9O2cETouE06Wb9Wr-l92evRmVVr7m8-WuwFUlIBfB8fut9CBzNd8O1_MtnY6KP74dSl93h-wphZJe1kp9PnDkcAhekIREIf6gWToGMGaZR0NCPtqsuSCMOZZKSug=w640-h310)](https://blogger.googleusercontent.com/img/a/AVvXsEi5M-qQI0jAEcuuEEaopyFsMT-DMUz_w8NCvWLibYBeKWmHqfFEISZ1QrpwKYbDsj9O2cETouE06Wb9Wr-l92evRmVVr7m8-WuwFUlIBfB8fut9CBzNd8O1_MtnY6KP74dSl93h-wphZJe1kp9PnDkcAhekIREIf6gWToGMGaZR0NCPtqsuSCMOZZKSug)

Ermir is an Evil/Rogue RMI Registry, it [exploits](https://www.kitploit.com/search/label/Exploits "exploits") unsecure [deserialization](https://www.kitploit.com/search/label/Deserialization "deserialization") on any Java code calling standard RMI methods on it (`list()`/`lookup()`/`bind()`/`rebind()`/`unbind()`).

* Ruby v3 or newer.

## Installation

Install Ermir from rubygems.org:

or clone the repo and build the gem:

```
$ git clone https://github.com/hakivvi/ermir.git
```

## Usage

Ermir is a cli gem, it comes with 2 cli files `ermir` and `gadgetmarshal`, `ermir` is the actual gem and the latter is just a pretty interface to [GadgetMarshaller.java](https://github.com/hakivvi/ermir/blob/main/helpers/gadgetmarshaller/GadgetMarshaller.java "GadgetMarshaller.java") file which rewrites the [gadgets](https://www.kitploit.com/search/label/Gadgets "gadgets") of [Ysoserial](https://github.com/frohoff/ysoserial "Ysoserial") to match `MarshalInputStream` requirements, the output should be then piped into `ermir` or a file, in case of custom gadgets use `MarshalOutputStream` instead of `ObjectOutputStream` to write your serialized object to the output stream.

`ermir` usage:

RMI Registry which exploits unsecure Java deserialization on any Java code calling standard RMI methods on it. Usage: ermir [options] -l, --listen bind the RMI [Registry](https://www.kitploit.com/search/label/Registry "Registry") to this ip and port (default: 0.0.0.0:1099). -f, --file path to file containing the gadget to be deserialized. -p, --pipe read the serialized gadget from the standard input stream. -v, --version print Ermir version. -h, --help print options help. Example: $ gadgetmarshal /path/to/ysoserial.jar Groovy1 calc.exe | ermir --listen 127.0.0.1:1099 --pipe" dir="auto">

```
➜  ~ ermir
Ermir by @hakivvi * https://github.com/hakivvi/ermir.
Info:
    Ermir is a Rogue/Evil RMI Registry which exploits unsecure Java deserialization on any Java code calling standard RMI methods on it.
Usage: ermir [options]
    -l, --listen   bind the RMI Registry to this ip and port (default: 0.0.0.0:1099).
    -f, --file     path to file containing the gadget to be deserialized.
    -p, --pipe     read the serialized gadget from the standard input stream.
    -v, --version  print Ermir version.
    -h, --help     print options help.
Example:
    $ gadgetmarshal /path/to/ysoserial.jar Groovy1 calc.exe | ermir --listen 127.0.0.1:1099 --pipe
```

`gadgetmarshal` usage:

```
➜  ~ gadgetmarshal
Usage: gadgetmarshal /path/to/ysoserial.jar Gadget1 cmd (optional)/path/to/output/file
```

## How does it work?

`java.rmi.registry.Registry` offers 5 methods: `list()`, `lookup()`, `bind()`, `rebind()`, `unbind()`:

* `public Remote lookup(String name)`: lookup() searches for a bound object in the registry by its name, the registry returns a `Remote` object which references the remote object that was looked up, the returned object is read using [`MarshalInputStream.readObject()`](http://hg.openjdk.java.net/jdk8u/jdk8u/jdk/file/jdk8u232-ga/src/share/classes/sun/rmi/registry/RegistryImpl_Stub.java#l127 "an Evil Java RMI Registry. (7)") which is just another layer on top of `ObjectInputStream`, basically it excpects after each class/proxy descriptor (`TC_CLASSDESC`/`TC_PROXYCLASSDESC`) an URL that will be used to load this class or proxy class. this is the same wild bug that was fixed in [jdk7u21](https://docs.oracle.com/javase/7/docs/technotes/guides/rmi/enhancements-7.html "jdk7u21"). (Ermir does not specify this URL as only old Java version are vulnerable, instead it just write [null](https://github.com/hakivvi/ermir/blob/240880237eb3a565daf1f5d79be19ac1d21cb4c8/helpers/gadgetmarshaller/GadgetMarshaller.java#L54 "null")). as [Ysoserial](https://github.com/frohoff/ysoserial "Ysoserial") gadgets are being serialized using `ObjectOutputStream`, Ermir uses `gadgetmarshal` -a wrapper around [GadgetMarshaller.java](https://github.com/hakivvi/ermir/blob/main/helpers/gadgetmarshaller/GadgetMarshaller.java "GadgetMarshaller.java")- to serialize the specified gagdet to match `MarshalInputStream` requirements. [![](https://blogger.googleusercontent.com/img/a/AVvXsEi5M-qQI0jAEcuuEEaopyFsMT-DMUz_w8NCvWLibYBeKWmHqfFEISZ1QrpwKYbDsj9O2cETouE06Wb9Wr-l92evRmVVr7m8-WuwFUlIBfB8fut9CBzNd8O1_MtnY6KP74dSl93h-wphZJe1kp9PnDkcAhekIREIf6gWToGMGaZR0NCPtqsuSCMOZZKSug=w640-h310)](https://blogger.googleusercontent.com/img/a/AVvXsEi5M-qQI0jAEcuuEEaopyFsMT-DMUz_w8NCvWLibYBeKWmHqfFEISZ1QrpwKYbDsj9O2cETouE06Wb9Wr-l92evRmVVr7m8-WuwFUlIBfB8fut9CBzNd8O1_MtnY6KP74dSl93h-wphZJe1kp9PnDkcAhekIREIf6gWToGMGaZR0NCPtqsuSCMOZZKSug)
* `public String[] list()`: list() asks the registry for all the bound objects names, while `String` type cannot be subsitued with a malicious gadget as it is not like any ordinary object and it is not read using `readObject()` but rather `readUTF()`, however as `list()` returns `String[]` which is an actual object and it is read using [`readObject()`](http://hg.openjdk.java.net/jdk8u/jdk8u/jdk/file/jdk8u232-ga/src/share/classes/sun/rmi/registry/RegistryImpl_Stub.java#l95 "an Evil Java RMI Registry. (13)"), Ermir sends the gadget instead of this `String[]` type. [![](https://blogger.googleusercontent.com/img/a/AVvXsEj93Qx7mmrlzWQ87KJmdGmkJzluP6DjaA5tZ6hAMOD-ijZyY9xxGRJv9u6PH_ugtdGiAwMHuH91UxhLhLH5XdmJFkRvNuqGFktkEbblWiSftuF7cS1eqWXtPQJnc0eyMEJ8Gk7qLFhcq3vCJrpqd99pO0rM_kqvoSJRCb9nEAkK8qQYKVC--5_vsqo3Ow=w640-h266)](https://blogger.googleusercontent.com/img/a/AVvXsEj93Qx7mmrlzWQ87KJmdGmkJzluP6DjaA5tZ6hAMOD-ijZyY9xxGRJv9u6PH_ugtdGiAwMHuH91UxhLhLH5XdmJFkRvNuqGFktkEbblWiSftuF7cS1eqWXtPQJnc0eyMEJ8Gk7qLFhcq3vCJrpqd99pO0rM_kqvoSJRCb9nEAkK8qQYKVC--5_vsqo3Ow)
* `public void bind(java.lang.String $param_String_1, java.rmi.Remote $param_Remote_2)`: bind() binds an object to a name on the registry, in bind() case the return type is `void` and there is nothing being returned, however if the registry specifies in the RMI return data packet that this return is an execptional return, the client/server client will call [`readObject()`](https://hg.openjdk.java.net/jdk8u/jdk8u/jdk/file/tip/src/share/classes/sun/rmi/transport/StreamRemoteCall.java#l270 "an Evil Java RMI Registry. (15)") despite the return type is `void`, this is how the regitry sends exceptions to its client (usually `java.lang.ClassNotFoundException`), once again Ermir will deliver the serialized gadget instead of a legitimate Exception object. [![](https://blogger.googleusercontent.com/img/a/AVvXsEjoE87SuTKFsZT_34AoMztCeFwP2G6yxoQeNSor2bl7mrxnYEwxMSCgjVBSUOk7gtBmnh2dCOTP2dxrQTPdvkVos3VxXK7gpcAllslTJcPc6jiuYekVZKKyTtSXVpPZmzssuh5dRo4qqqIH8AD72eCfEUvqcBnayzrL6bAy7LE-_T5agvw8do8y1QKf7g=w640-h282)](https://blogger.googleusercontent.com/img/a/AVvXsEjoE87SuTKFsZT_34AoMztCeFwP2G6yxoQeNSor2bl7mrxnYEwxMSCgjVBSUOk7gtBmnh2dCOTP2dxrQTPdvkVos3VxXK7gpcAllslTJcPc6jiuY...