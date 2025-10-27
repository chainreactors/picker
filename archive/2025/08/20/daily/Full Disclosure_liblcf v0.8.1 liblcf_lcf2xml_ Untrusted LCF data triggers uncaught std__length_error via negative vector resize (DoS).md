---
title: liblcf v0.8.1 liblcf/lcf2xml: Untrusted LCF data triggers uncaught std::length_error via negative vector resize (DoS)
url: https://seclists.org/fulldisclosure/2025/Aug/11
source: Full Disclosure
date: 2025-08-20
fetch_date: 2025-10-07T00:51:09.223791
---

# liblcf v0.8.1 liblcf/lcf2xml: Untrusted LCF data triggers uncaught std::length_error via negative vector resize (DoS)

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

[![Previous](/images/left-icon-16x16.png)](9)
[By Date](date.html#11)
[![Next](/images/right-icon-16x16.png)](12)

[![Previous](/images/left-icon-16x16.png)](9)
[By Thread](index.html#11)
[![Next](/images/right-icon-16x16.png)](12)

![](/shared/images/nst-icons.svg#search)

# liblcf v0.8.1 liblcf/lcf2xml: Untrusted LCF data triggers uncaught std::length\_error via negative vector resize (DoS)

---

*From*: Ron E <ronaldjedgerson () gmail com>
*Date*: Sun, 17 Aug 2025 22:21:22 -0400

---

```
lcf2xml (part of liblcf) aborts when parsing specially crafted RPG Maker
2000/2003 files that supply a negative element count for vectors of
structured records. The generic reader:

template <class S>

void Struct<S>::ReadLcf(std::vector<S>& vec, LcfReader& stream) {

    int count = stream.ReadInt();

    vec.resize(count);        // <— negative -> huge size_t -> throws
length_error

    for (int i = 0; i < count; i++) {

        IDReader::ReadID(vec[i], stream);

        TypeReader<S>::ReadLcf(vec[i], stream, 0);

    }

}

does not validate count. When count is negative, the implicit conversion to
size_t in std::vector::resize requests an enormous size and the C++ runtime
throws std::length_error, which is uncaught in the tool, causing the
process to terminate. This is a straightforward DoS against any consumer of
untrusted LCF data using liblcf’s readers without guarding exceptions.

The issue reproduces across multiple record types (e.g., Event in LMU,
Troop/TroopPage in LDB).

*Technical Details:*

$ lcf2xml --2k3 <poc.lmu>

terminate called after throwing an instance of 'std::length_error'

  what():  vector::_M_default_append

Aborted

*Backtrace (LMU → Map → Events path):*

#0  std::__throw_length_error(char const*)

#1  std::vector<lcf::rpg::Event>::_M_check_len(__n=18446744073574277089,
...)

#2
std::vector<lcf::rpg::Event>::_M_default_append(__n=18446744073574277089)

#3  lcf::Struct<lcf::rpg::Event>::ReadLcf(vec, stream) at
reader_struct_impl.h:220  // vec.resize(count)

    locals: count = -135274527

#4  TypeReader<std::vector<Event>>::ReadLcf(...)

#5  TypedField<Map, std::vector<Event>>::ReadLcf(...)

#6  lcf::Struct<lcf::rpg::Map>::ReadLcf(...)

#7  lcf::LMU_Reader::Load(...)

#8  ReaderWriteToFile(...) -> lcf2xml main
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](9)
[By Date](date.html#11)
[![Next](/images/right-icon-16x16.png)](12)

[![Previous](/images/left-icon-16x16.png)](9)
[By Thread](index.html#11)
[![Next](/images/right-icon-16x16.png)](12)

### Current thread:

* **liblcf v0.8.1 liblcf/lcf2xml: Untrusted LCF data triggers uncaught std::length\_error via negative vector resize (DoS)** *Ron E (Aug 18)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools.org)

* [Vuln scanners](https://sectools.org/tag/vuln-scanners/)* [Password audit](https://sectools.org/tag/pass-audit/)* [Web scanners](https://sectools.org/tag/web-scanners/)* [Wireless](https://sectools.org/tag/wireless/)* [Exploitation](https://sectools.org/tag/sploits/)

## [About](https://insecure.org/)

* [About/Contact](https://insecure.org/fyodor/)* [Privacy](https://insecure.org/privacy.html)* [Advertising](https://insecure.org/advertising.html)* [Nmap Public Source License](https://nmap.org/npsl/)

[![](/shared/images/nst-icons.svg#twitter)](https://twitter.com/nmap "Visit us on Twitter")
[![](/shared/images/nst-icons.svg#facebook)](https://facebook.com/nmap "Visit us on Facebook")
[![](/shared/images/nst-icons.svg#github)](https://github.com/nmap/ "Visit us on Github")
[![](/shared/images/nst-icons.svg#reddit)](https://reddit.com/r/nmap/ "Discuss Nmap on Reddit")