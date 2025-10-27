---
title: [译] Socket listen 多地址需求与 SK_LOOKUP BPF 的诞生（LPC, 2019）
url: https://arthurchiao.github.io/blog/birth-of-sk-lookup-bpf-zh/
source: ArthurChiao's Blog
date: 2022-12-12
fetch_date: 2025-10-04T01:14:17.698399
---

# [译] Socket listen 多地址需求与 SK_LOOKUP BPF 的诞生（LPC, 2019）

# [ArthurChiao's Blog](https://arthurchiao.github.io/)

* [Home](/index.html)
* [Articles (EN)](/articles)
* [Articles (дЄ≠жЦЗ)](/articles-zh)
* [Categories](/categories)
* [About](/about)
* [Donate](/donate)

# [иѓС] Socket listen е§ЪеЬ∞еЭАйЬАж±ВдЄО SK\_LOOKUP BPF зЪДиѓЮзФЯпЉИLPC, 2019пЉЙ

Published at 2022-12-11 | Last Update 2022-12-11

### иѓСиАЕеЇП

жЬђжЦЗзїДеРИзњїиѓС Cloudflare зЪДеЗ†зѓЗеИЖдЇЂпЉМдїЛзїНдЇЖдїЦдїђйЭҐдЄізЪДзЛђзЙєзљСзїЬйЬАж±ВгАБиІ£еЖ≥жЦєж°ИзЪДжЉФињЫпЉМ
дї•еПКзїИжЮБиІ£еЖ≥жЦєж°И `SK_LOOKUP` BPF зЪДиѓЮзФЯпЉЪ

1. [Programming socket lookup with BPF](https://linuxplumbersconf.org/event/4/contributions/487/), LPC, 2019
2. [ItвАЩs crowded in here](https://blog.cloudflare.com/its-crowded-in-here/), Cloudflare blog, 2019
3. [Steering connections to sockets with BPF socket lookup hook](https://github.com/jsitnicki/ebpf-summit-2020)пЉМeBPF SummitпЉМ2020

**зФ±дЇОиѓСиАЕж∞іеє≥жЬЙйЩРпЉМжЬђжЦЗдЄНеЕНе≠ШеЬ®йБЧжЉПжИЦйФЩиѓѓдєЛе§ДгАВе¶ВжЬЙзЦСйЧЃпЉМиѓЈжЯ•йШЕеОЯжЦЗгАВ**

дї•дЄЛжШѓиѓСжЦЗгАВ

---

* [иѓСиАЕеЇП](#иѓСиАЕеЇП)
* [1 еЉХи®А](#1-еЉХи®А)
  + [1.1 зО∞зКґпЉЪCloudflare иЊєзЉШжЮґжЮД](#11-зО∞зКґcloudflare-иЊєзЉШжЮґжЮД)
  + [1.2 йЬАж±ВпЉЪе¶ВдљХиЃ©дЄАдЄ™жЬНеК°зЫСеРђиЗ≥е∞СеЗ†зЩЊдЄ™ IP еЬ∞еЭА](#12-йЬАж±Ве¶ВдљХиЃ©дЄАдЄ™жЬНеК°зЫСеРђиЗ≥е∞СеЗ†зЩЊдЄ™-ip-еЬ∞еЭА)
* [2 еЬЇжЩѓйЬАж±ВдЄОиІ£еЖ≥жЦєж°ИжЉФињЫ](#2-еЬЇжЩѓйЬАж±ВдЄОиІ£еЖ≥жЦєж°ИжЉФињЫ)
  + [2.1 зЃАеНХеЬЇжЩѓпЉЪдЄАдЄ™ socket зЫСеРђдЄАдЄ™ IP еЬ∞еЭА](#21-зЃАеНХеЬЇжЩѓдЄАдЄ™-socket-зЫСеРђдЄАдЄ™-ip-еЬ∞еЭА)
  + [2.2 ињЫйШґеЬЇжЩѓпЉЪдЄАдЄ™ socket зЫСеРђе§ЪдЄ™ IP еЬ∞еЭА](#22-ињЫйШґеЬЇжЩѓдЄАдЄ™-socket-зЫСеРђе§ЪдЄ™-ip-еЬ∞еЭА)
    - [2.2.1 `bind(INADDR_ANY)` жИЦ `bind(0.0.0.0)`](#221-bindinaddr_any-жИЦ-bind0000)
    - [2.2.2 `listen()` unbound socket](#222-listen-unbound-socket)
    - [2.2.3 жКАжЬѓеОЯзРЖпЉЪеЖЕж†Є socket lookup йАїиЊС](#223-жКАжЬѓеОЯзРЖеЖЕж†Є-socket-lookup-йАїиЊС)
    - [2.2.4 дЉШзЉЇзВєжѓФиЊГ](#224-дЉШзЉЇзВєжѓФиЊГ)
  + [2.3 й≠ФйђЉеЬЇжЩѓпЉЪеРМдЄАеП∞жЬЇеЩ®дЄКдЄНеРМ service дљњзФ®еРМдЄАдЄ™ portпЉИIP дЄНйЗНеП†пЉЙ](#23-й≠ФйђЉеЬЇжЩѓеРМдЄАеП∞жЬЇеЩ®дЄКдЄНеРМ-service-дљњзФ®еРМдЄАдЄ™-portip-дЄНйЗНеП†)
  + [2.4 еЬ∞зЛ±еЬЇжЩѓпЉЪдЄАдЄ™ service зЫСеРђжЙАжЬЙ 65535 дЄ™зЂѓеП£](#24-еЬ∞зЛ±еЬЇжЩѓдЄАдЄ™-service-зЫСеРђжЙАжЬЙ-65535-дЄ™зЂѓеП£)
    - [2.4.1 `iptables + TPROXY`](#241-iptables--tproxy)
    - [2.4.2 `TPROXY` жЦєж°ИзЉЇзВє](#242-tproxy-жЦєж°ИзЉЇзВє)
    - [2.4.3 жЬЙж≤°жЬЙйУґеЉєпЉЯ](#243-жЬЙж≤°жЬЙйУґеЉє)
* [3 `SK_LOOKUP` BPFпЉЪеѓє socket lookup ињЗз®ЛињЫи°МзЉЦз®Л](#3-sk_lookup-bpfеѓє-socket-lookup-ињЗз®ЛињЫи°МзЉЦз®Л)
  + [3.1 иЃЊиЃ°жАЭжГ≥](#31-иЃЊиЃ°жАЭжГ≥)
  + [3.2 еЉХеЕ•жЦ∞зЪД BPF з®ЛеЇПз±їеЮЛ SK\_LOOKUP](#32-еЉХеЕ•жЦ∞зЪД-bpf-з®ЛеЇПз±їеЮЛ-sk_lookup)
    - [3.2.1 з®ЛеЇПжЙІи°МдљНзљЃ](#321-з®ЛеЇПжЙІи°МдљНзљЃ)
    - [3.2.2 еЈ•дљЬеОЯзРЖ](#322-еЈ•дљЬеОЯзРЖ)
  + [3.3 BPF з®ЛеЇПз§ЇдЊЛ](#33-bpf-з®ЛеЇПз§ЇдЊЛ)
  + [3.4 Demo](#34-demo)
    - [3.4.1 жХИжЮЬпЉЪеНХдЄ™ socket еРМжЧґзЫСеРђ 4 дЄ™зЂѓеП£](#341-жХИжЮЬеНХдЄ™-socket-еРМжЧґзЫСеРђ-4-дЄ™зЂѓеП£)
    - [3.4.2 еИЫеїЇжЬНеК°зЂѓ echo server](#342-еИЫеїЇжЬНеК°зЂѓ-echo-server)
    - [3.4.3 еЃҐжИЈзЂѓиЃњйЧЃжµЛиѓХ](#343-еЃҐжИЈзЂѓиЃњйЧЃжµЛиѓХ)
    - [3.4.4 зЉЦиѓСгАБеК†иљљ BPF з®ЛеЇП](#344-зЉЦиѓСеК†иљљ-bpf-з®ЛеЇП)
* [4 жАїзїУ](#4-жАїзїУ)

---

# 1 еЉХи®А

## 1.1 зО∞зКґпЉЪCloudflare иЊєзЉШжЮґжЮД

Cloudflare зЪДиЊєзЉШжЬНеК°еЩ®йЗМињРи°МзЭАе§ІйЗПз®ЛеЇПпЉМдЄНдїЕеМЕжЛђеЊИе§Ъ**еЖЕйГ®еЇФзФ®**пЉМ
ињШеМЕжЛђеЊИе§Ъ**еЕђзљСжЬНеК°**пЉИpublic facing servicesпЉЙпЉМдЊЛе¶ВпЉЪ

1. [HTTP CDN](https://www.cloudflare.com/cdn/) (tcp/80)
2. [HTTPS CDN](https://www.cloudflare.com/ssl/) (tcp/443, [udp/443](https://cloudflare-quic.com/))
3. [authoritative DNS](https://www.cloudflare.com/dns/) (udp/53)
4. [recursive DNS](https://blog.cloudflare.com/dns-resolver-1-1-1-1/) (udp/53, 853)
5. [NTP with NTS](https://blog.cloudflare.com/secure-time/) (udp/1234)
6. [Roughtime time service](https://blog.cloudflare.com/roughtime/) (udp/2002)
7. [IPFS Gateway](https://blog.cloudflare.com/distributed-web-gateway/) (tcp/443)
8. [Ethereum Gateway](https://blog.cloudflare.com/cloudflare-ethereum-gateway/) (tcp/443)
9. [Spectrum proxy](https://blog.cloudflare.com/spectrum/) (tcp/any, udp/any)1
10. [WARP](https://blog.cloudflare.com/announcing-warp-plus/) (udp)

ињЩдЇЫеЇФзФ®йАЪињЗж®™иЈ® **100+ зљСжЃµ**зЪД **100 дЄЗдЄ™ Anycast**
[еЕђзљС IPv4 еЬ∞еЭА](https://www.cloudflare.com/ips)
жПРдЊЫжЬНеК°гАВдЄЇдЇЖдњЭжМБдЄАиЗіжАІпЉМCloudflare зЪД**жѓПеП∞жЬНеК°еЩ®йГљињРи°МжЙАжЬЙжЬНеК°**пЉМ
жѓПеП∞жЬЇеЩ®йГљиГље§ДзРЖжѓПдЄ™ Anycast еЬ∞еЭАзЪДиѓЈж±ВпЉМињЩж†ЈиГљ**еЕЕеИЖеИ©зФ®жЬНеК°еЩ®з°ђдїґиµДжЇР**пЉМ
еЬ®жЙАжЬЙжЬНеК°еЩ®дєЛйЧіеБЪиѓЈж±ВзЪДиіЯиљљеЭЗи°°пЉМе¶ВдЄЛеЫЊжЙАз§ЇпЉМ

![](/assets/img/birth-of-sk-lookup-bpf/edge_data_center.png)

дєЛеЙНзЪДеИЖдЇЂдЄ≠еЈ≤зїПдїЛзїНдЇЖ **Cloudflare зЪДиЊєзЉШзљСзїЬжЮґжЮД**пЉМжДЯеЕіиґ£еПѓзІїж≠•пЉЪ

1. [No Scrubs: The Architecture That Made Unmetered Mitigation Possible](https://blog.cloudflare.com/no-scrubs-architecture-unmetered-mitigation/)
2. [(иѓС) Cloudflare иЊєзЉШзљСзїЬжЮґжЮДпЉЪжЧ†е§ДдЄНеЬ®зЪД BPFпЉИ2019пЉЙ](/blog/cloudflare-arch-and-bpf-zh/)

## 1.2 йЬАж±ВпЉЪе¶ВдљХиЃ©дЄАдЄ™жЬНеК°зЫСеРђиЗ≥е∞СеЗ†зЩЊдЄ™ IP еЬ∞еЭА

**е¶ВдљХиГљиЃ©дЄАдЄ™жЬНеК°зЫСеРђеЬ®иЗ≥е∞СеЗ†зЩЊдЄ™ IP еЬ∞еЭАдЄК**пЉМиАМдЄФиГљз°ЃдњЭеЖЕж†ЄзљСзїЬж†Из®≥еЃЪињРи°МеСҐпЉЯ

ињЩжШѓ Cloudflare еЈ•з®ЛеЄИињЗеОїеЗ†еєідЄАзЫіеЬ®жАЭиАГзЪДйЧЃйҐШпЉМеЕґз≠Фж°ИдєЯеЬ®й©±еК®зЭАжИСдїђзЪДзљСзїЬдЄНжЦ≠жЉФињЫгАВ
зЙєеИЂжШѓпЉМеЃГиЃ©жИСдїђ**жЫіжЬЙеИЫйА†жАІеЬ∞еОїдљњзФ®**
[Berkeley sockets API](https://en.wikipedia.org/wiki/Berkeley_sockets)пЉМ
ињЩжШѓдЄАдЄ™зїЩеЇФзФ®еИЖйЕН IP еТМ port зЪД POSIX ж†ЗеЗЖгАВ

дЄЛйЭҐжИСдїђжЭ•еЫЮй°ЊдЄАдЄЛињЩиґЯе•Зе¶ЩзЪДжЧЕз®ЛгАВ

# 2 еЬЇжЩѓйЬАж±ВдЄОиІ£еЖ≥жЦєж°ИжЉФињЫ

## 2.1 зЃАеНХеЬЇжЩѓпЉЪдЄАдЄ™ socket зЫСеРђдЄАдЄ™ IP еЬ∞еЭА

![](/assets/img/birth-of-sk-lookup-bpf/mapping_1_to_1.png)

Fig. жЬАзЃАеНХеЬЇжЩѓпЉЪдЄАдЄ™ socket зїСеЃЪдЄАдЄ™ `IP:Port`

ињЩжШѓжЬАзЃАеНХзЪДеЬЇжЩѓпЉМ`(ip,port)` дЄО service дЄАдЄАеѓєеЇФгАВ

* Service зЫСеРђеЬ®жЯРдЄ™еЈ≤зЯ•зЪД `IP:Port` жПРдЊЫжЬНеК°пЉЫ
* Service е¶ВжЮЬи¶БжФѓжМБе§ЪзІНеНПиЃЃз±їеЮЛпЉИTCPгАБUDPпЉЙпЉМеИЩйЬАи¶Б**дЄЇжѓПзІНеНПиЃЃз±їеЮЛжЙУеЉАдЄАдЄ™ socket**гАВ

дЊЛе¶ВпЉМжИСдїђзЪД[жЭГе®Б DNS](https://www.cloudflare.com/dns/) жЬНеК°дЉЪеИЖеИЂйТИеѓє TCP еТМ UDP еИЫеїЇдЄАдЄ™ socketпЉЪ

```
    (192.0.2.1, 53/tcp) -> ("auth-dns", pid=1001, fd=3)
    (192.0.2.1, 53/udp) -> ("auth-dns", pid=1001, fd=4)
```

дљЖжШѓпЉМеѓєдЇО Cloudflare зЪДиІДж®°жЭ•иѓіпЉМжИСдїђйЬАи¶Б**еЬ®иЗ≥е∞С 4K дЄ™ IP**
дЄКеИЖеИЂеИЫеїЇ socketпЉМжЙНиГљжї°иґ≥дЄЪеК°йЬАж±ВпЉМдєЯе∞±жШѓиѓі DNS ињЩдЄ™жЬНеК°йЬАи¶БзЫСеРђдЄАдЄ™иЗ≥е∞С `/20` зЪДзљСжЃµгАВ

![](/assets/img/birth-of-sk-lookup-bpf/mapping_many_1_to_1.png)

Fig. дЄЇдЇЖжФѓжТСдЄЪеК°иІДж®°пЉМйЬАи¶БдЄЇ DNS ињЩж†ЈзЪДжЬНеК°еЬ®иЗ≥е∞С 4000 дЄ™ IP еЬ∞еЭАдЄКеИЫеїЇ socket

е¶ВжЮЬзФ® `ss` дєЛз±їзЪДеЈ•еЕЈзЬЛпЉМе∞±дЉЪзЬЛеИ∞йЭЮеЄЄйХњзЪД socket еИЧи°®пЉЪ

```
$ sudo ss -ulpn 'sport = 53'
State  Recv-Q Send-Q  Local Address:Port Peer Address:Port
...
UNCONN 0      0           192.0.2.40:53        0.0.0.0:*    users:(("auth-dns",pid=77556,fd=11076))
UNCONN 0      0           192.0.2.39:53        0.0.0.0:*    users:(("auth-dns",pid=77556,fd=11075))
UNCONN 0      0           192.0.2.38:53        0.0.0.0:*    users:(("auth-dns",pid=77556,fd=11074))
UNCONN 0      0           192.0.2.37:53        0.0.0.0:*    users:(("auth-dns",pid=77556,fd=11073))
UNCONN 0      0           192.0.2.36:53        0.0.0.0:*    users:(("auth-dns",pid=77556,fd=11072))
UNCONN 0      0           192.0.2.31:53        0.0.0.0:*    users:(("auth-dns",pid=77556,fd=11071))
...
```

жШЊзДґпЉМињЩзІНжЦєеЉПйЭЮеЄЄеОЯеІЛеТМз≤ЧжЪіпЉЫдЄНињЗдєЯжЬЙеЃГзЪДдЉШзВєпЉЪељУеЕґдЄ≠дЄАдЄ™ IP йБ≠еПЧ UDP ж≥Ыжі™жФїеЗїжЧґпЉМ
еЕґдїЦ IP дЄНеПЧељ±еУНгАВ

## 2.2 ињЫйШґеЬЇжЩѓпЉЪдЄАдЄ™ socket зЫСеРђе§ЪдЄ™ IP еЬ∞еЭА

дї•дЄКеБЪж≥ХжШЊзДґе§™ињЗз≤Чз≥ЩпЉМдЄАдЄ™жЬНеК°е∞±дљњзФ®ињЩдєИе§Ъ IP еЬ∞еЭАгАВдљЖжЫіе§ІзЪДйЧЃйҐШжШѓпЉЪ
зЫСеРђзЪД **socket иґКе§ЪпЉМhash table дЄ≠зЪД chain е∞±иґКйХњпЉМsocket lookup ињЗз®Ле∞±иґКжЕҐ**гАВ
жИСдїђеЬ® [The revenge of the listening sockets](https://blog.cloudflare.com/revenge-listening-sockets/)
дЄ≠зїПеОЖдЇЖињЩдЄАйЧЃйҐШгАВйВ£дєИпЉМжЬЙж≤°жЬЙжЫіе•љзЪДеКЮж≥ХиІ£еЖ≥ињЩдЄ™йЧЃйҐШеСҐпЉЯжЬЙгАВ

### 2....