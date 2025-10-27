---
title: Exposing the "PDF Botnet" - An OSINT Analysis
url: https://ddanchev.blogspot.com/2023/03/exposing-pdf-botnet-osint-analysis.html
source: Dancho Danchev's Blog - Mind Streams of Information Security Knowledge
date: 2023-03-04
fetch_date: 2025-10-04T08:37:59.898543
---

# Exposing the "PDF Botnet" - An OSINT Analysis

# [Dancho Danchev's Blog - Mind Streams of Information Security Knowledge](https://ddanchev.blogspot.com/)

Independent Contractor. Bitcoin: 15Zvie1j8CjSR52doVSZSjctCDSx3pDjKZ Email: dancho.danchev@hush.com OMEMO: ddanchev@conversations.im | OTR: danchodanchev@xmpp.jp | TOX ID: 53B409440A6DC34F1BA458869A0462D92C15B467AF6319D481CA353690C88667833A0EE82969

## Friday, March 03, 2023

### Exposing the "PDF Botnet" - An OSINT Analysis

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiOtoPrGr1Brmf18iXXhjXBEJ3NCjcDfW19O_ofLIqN9igX4DvI00UCOALrKVGC0o9QgzCh9sNttzmJ6djy3CEXNG8i8lXDHM6hriGNqeCAoLrMxTuVBysnMDvV5gAzSh5YLRs5H9-mVHoJM34uxKt7aTSocmXO6poZCI0YBmh7McIfownvcQ/s320/Screenshot_15.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiOtoPrGr1Brmf18iXXhjXBEJ3NCjcDfW19O_ofLIqN9igX4DvI00UCOALrKVGC0o9QgzCh9sNttzmJ6djy3CEXNG8i8lXDHM6hriGNqeCAoLrMxTuVBysnMDvV5gAzSh5YLRs5H9-mVHoJM34uxKt7aTSocmXO6poZCI0YBmh7McIfownvcQ/s810/Screenshot_15.png)

Dear blog readers,

I've recently stumbled upon a pretty interesting and worth mentioning malicious software and botnet spam and malicious software serving campaign that can be best described as a "PDF botnet" where the ultimate idea for both propagation and infection is the active utilization of PDF files which are exclusively hosted on compromised or on purposely malicious and fraudulent rogue and bogus infrastructure.

**Sample screenshots include:**

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgbk2LS3gtO8vjDnxA8BqAxcU17vJKqmBwYhVYUkJMA36vt66qVOm3n0xB-bbG2eWeWtfFe-vy3KbKlqmGvjv_9-YMFj_bEvyOQqTR0UI9C7p7Env1iTLpdNBYoSBHlDEAyipYmZq35hK51WqpKo5w0my-Cjp7clMiTKCYHiXDN5gLJ_Gjclg/s1600/Screenshot_4.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgbk2LS3gtO8vjDnxA8BqAxcU17vJKqmBwYhVYUkJMA36vt66qVOm3n0xB-bbG2eWeWtfFe-vy3KbKlqmGvjv_9-YMFj_bEvyOQqTR0UI9C7p7Env1iTLpdNBYoSBHlDEAyipYmZq35hK51WqpKo5w0my-Cjp7clMiTKCYHiXDN5gLJ_Gjclg/s197/Screenshot_4.png)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhE9m2b3hRbPk4-4giU0LLw5HVvUWz6AMzVdtKrSqzaEEkls_s5ButxJUlQnmLYF6sTeHVN8N4osyKrbWuMuBCxrMpcaVsj5pQRDRBDNMuBMmJjQmaHukkcJvwaXHsrNcrvInNFG9nQTOGVfIZHr0gEXNkh7NoBrHCQHVAfdpRZQFYfmXUmLg/s1600/Screenshot_3.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhE9m2b3hRbPk4-4giU0LLw5HVvUWz6AMzVdtKrSqzaEEkls_s5ButxJUlQnmLYF6sTeHVN8N4osyKrbWuMuBCxrMpcaVsj5pQRDRBDNMuBMmJjQmaHukkcJvwaXHsrNcrvInNFG9nQTOGVfIZHr0gEXNkh7NoBrHCQHVAfdpRZQFYfmXUmLg/s253/Screenshot_3.png)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhHJ72HrN9kOEZkHotdUQK2-mYtWLJHRTq7KAKtmhNUBaNhu66kQ-ROD9ZPSEUwzo7NbW1iyRSIGTD9nR4IbslguD60DGLXtfHDXcMhhBy086vfnf_sR3l_6eEsGzk-JJZUsFcWmLOtAIHbm3AaK9pmJ1OEFhdShLYj3ChPOIVTZCnQZdF6Xg/s1600/Screenshot_2.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhHJ72HrN9kOEZkHotdUQK2-mYtWLJHRTq7KAKtmhNUBaNhu66kQ-ROD9ZPSEUwzo7NbW1iyRSIGTD9nR4IbslguD60DGLXtfHDXcMhhBy086vfnf_sR3l_6eEsGzk-JJZUsFcWmLOtAIHbm3AaK9pmJ1OEFhdShLYj3ChPOIVTZCnQZdF6Xg/s269/Screenshot_2.png)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgqdGbbYAj96hb7Z7JYYFMwq0utDK2jRM_zMGnUpcAGltYXOCZ3aVZ3tK37cTL7jnOYftoxoH43IqkdytEgFrcE_FvWjfDT1JS74w0c88zA3AwDK6HIyFMk4GeX5c5NW2ev2FyWuG5NEFOo5pQQJI5e1_8yEfIIpAtG6cskwwSpkbR83N0Xrw/s1600/Screenshot_1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgqdGbbYAj96hb7Z7JYYFMwq0utDK2jRM_zMGnUpcAGltYXOCZ3aVZ3tK37cTL7jnOYftoxoH43IqkdytEgFrcE_FvWjfDT1JS74w0c88zA3AwDK6HIyFMk4GeX5c5NW2ev2FyWuG5NEFOo5pQQJI5e1_8yEfIIpAtG6cskwwSpkbR83N0Xrw/s266/Screenshot_1.png)

**Sample URLs known to have been involved in the campaign include:**

hxxp:[/][/]ragaz[.]co[.]za[/]XSRYdR1H?utm\_term=picsart+background+image++hd

hxxp:[/][/]www[.]lbtfilm[.]com[/]uploads[/]files[/]koxuwegemagobuwidewas[.]pdf

hxxp:[/][/]teputire[.]weebly[.]com[/]uploads[/]1[/]3[/]0[/]8[/]130813428[/]tixok[.]pdf

hxxp:[/][/]www[.]hypnotiseur[.]com[/]wp-content[/]plugins[/]formcraft[/]file-upload[/]server[/]content[/]files[/]16210e2f2aed0f---favagujegelivos[.]pdf

hxxp:[/][/]applecentervn[.]com[/]uploads[/]image[/]files[/]81922078809[.]pdf

hxxp:[/][/]villamishkan[.]com[/]310renonew[/]front[/]images[/]files[/]womosutilonotolil[.]pdf

hxxp:[/][/]jackinthegymtpe[.]com[/]uploads[/]files[/]202204101711569256[.]pdf

hxxp:[/][/]jigupipugefelo[.]weebly[.]com[/]uploads[/]1[/]3[/]4[/]3[/]134387822[/]kexowanegakuxiku[.]pdf

hxxp:[/][/]ulicetwojegomiasta[.]pl[/]kcfinder[/]upload[/]files[/]vadanetezukamiludi[.]pdf

hxxp:[/][/]toys4boysleather[.]com[/]userfiles[/]file[/]7982175874[.]pdf

hxxp:[/][/]93564497[.]com[/]userfiles[/]texanefimewakatovatoz[.]pdf

hxxp:[/][/]ceb[.]lk[/]assets[/]js[/]kcfinder[/]upload[/]files[/]58252873057[.]pdf

hxxp:[/][/]glassinter[.]de[/]kcfinder[/]upload[/]upload[/]23524790716[.]pdf

hxxp:[/][/]jaxurevinul[.]weebly[.]com[/]uploads[/]1[/]3[/]4[/]8[/]134868463[/]3f2975c6121556[.]pdf

hxxp:[/][/]szm[.]hu[/]userfiles[/]file[/]wenutoxeworudif[.]pdf

hxxp:[/][/]dojexivosofu[.]weebly[.]com[/]uploads[/]1[/]3[/]4[/]3[/]134348646[/]6486123[.]pdf

hxxp:[/][/]veraschwemmle[.]de[/]fckdata[/]file[/]dugivisoxolel[.]pdf

hxxp:[/][/]happycondo[.]leaddeehub[.]com[/]userfiles[/]files[/]lipefagajetelegusir[.]pdf

hxxp:[/][/]ninofupefuf[.]weebly[.]com[/]uploads[/]1[/]3[/]1[/]8[/]131856131[/]6e401701aa[.]pdf

hxxp:[/][/]www[.]auditsi[.]com[/]wp-content[/]plugins[/]formcraft[/]file-upload[/]server[/]content[/]files[/]1622914d312f84---45312087428[.]pdf

hxxp:[/][/]www[.]christinemartin[.]co[.]uk[/]wp-content[/]plugins[/]formcraft[/]file-upload[/]server[/]content[/]files[/]1621dac28b28a0---tufupavokuj[.]pdf

hxxp:[/][/]sendedianqi[.]com[/]upload\_fck[/]file[/]2022-3-21[/]20220321161426543141[.]pdf

hxxp:[/][/]erdelyironkbutor[.]hu[/]admin[/]kcfinder[/]upload[/]files[/]sukotigipapewefowu[.]pdf

hxxp:[/][/]studioingegneriavaragnolo[.]com[/]userfiles[/]files[/]kilukowap[.]pdf

hxxp:[/][/]f-kcc[.]jp[/]user\_data[/]userfiles[/]files[/]22156092393[.]pdf

hxxp:[/][/]alkoplast[.]rs[/]files[/]28560168304[.]pdf

hxxp:[/][/]arborspringsforestry[.]com[/]img[/]files[/]kelagug[.]pdf

hxxp:[/][/]cissud[.]it[/]uploads[/]ck\_editor[/]files[/]33956310758[.]pdf

hxxp:[/][/]jfd[.]news[/]app[/]webroot[/]uploads[/]files[/]71167178402[.]pdf

hxxp:[/][/]leg-vein[.]jp[/]kcfinder[/]upload[/]files[/]sevavimelozojufezetowe[.]pdf

hxxp:[/][/]duxotitur[.]weebly[.]com[/]uploads[/]1[/]3[/]4[/]5[/]134596147[/]5545494[.]pdf

hxxp:[/][/]tree-house[.]jp[/]assets[/]news[/]files[/]tevasurodajaxajezetatug[.]pdf

hxxp:[/][/]kikebazelagugez[.]weebly[.]com[/]uploads[/]1[/]4[/]1[/]2[/]141287616[/]77fd513b304b[.]pdf

**Sample MD5s known to have been involved in the campaign include:**

5BB96B309B8CB58071B73118D1A59C05  1278967687.pdf

6E3EB89CFD46D107905D9F60853E2661  1410845058.pdf

0CF4455F92A6397521FC9BD08FC70A12  1487091430.pdf

20DA43AD4878B9F925F88854574010E2  1983674347.pdf

8C2E4E0C3EB5E0131324CA54FD1648BE  3480745958.pdf

23C45840B8F4EEF5F53CD35BC087D299  3552074133.pdf

9DA1E72A18F214555449BA3F8EBD1399  3964667732.pdf

879332C060A637B45E958911B84627B0  4092425255.pdf

A409086CDEF2B6C412B33EA8B53E70AD  4474449835.pdf

A4BB4C77DF8328AE46CEED4F373D2C1C  5741836759.pdf

B2EB74B29686039C6DCAAD0B801A125E  6103190089.pdf

342D15A9D8A9CAC6C482EF24C63FB7FF  6497559623.pdf

53A8F7A614EAC9833F0CC5B97AE8650A  8742646775.pdf

82D26DA61A8A0F389664859B38ECC08C  8791363493.pdf

99B141C2A8E5073C17E81E144734A361  8983036096.pdf

AD4C11FEFBE2A16AE8358BC51A8CBF3F  9120465087.pdf

C9A7E18ACBF4EE0ED5435B73E1957A9F  9231960459.pdf

699553341D62FBC0C1EE86266865DE72  9348069038.pdf

FBFE529A50E15B66DD40829525E7F7BA  9699229203.pdf

63BB161319E4E3584821D861AB541A0C  10348572906.pdf

BB568F6CD8AE515EAD55259470298D9E  13416475440.pdf

16E42D227211DAC5260BD8FD15A795C7  13823887193.pdf

3C1CE3A5A0B49D5AA198F0279889D493  13847861787.pdf

66BD8B8E665AC62A0FA67F111256541F  14137532633.pdf

B16E989493AD266A39A123629EADD229  14318140657.pdf

01373CA6F7533D66BF5A57390F9FFA31  16011902586.pdf

5A5AA084699C1415D962E0D59E637815  1663...