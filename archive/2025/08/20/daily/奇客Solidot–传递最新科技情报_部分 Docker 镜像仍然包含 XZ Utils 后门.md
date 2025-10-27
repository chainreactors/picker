---
title: 部分 Docker 镜像仍然包含 XZ Utils 后门
url: https://www.solidot.org/story?sid=82090
source: 奇客Solidot–传递最新科技情报
date: 2025-08-20
fetch_date: 2025-10-07T00:48:03.452733
---

# 部分 Docker 镜像仍然包含 XZ Utils 后门

[уЎ╗тйЋ](/login) [Т│етєї](/register)

* ТќЄуФа

  [тЙђТЌЦТќЄуФа](/?issue=20251006)
  [тЙђТЌЦТіЋуЦе](/polllist)
* уџ«Уѓц

  [УЊЮУЅ▓](/?theme=blue)
  [ТЕЎУЅ▓](/?theme=yellow)
  [у╗┐УЅ▓](/?theme=green)
  [ТхЁу╗┐УЅ▓](/?theme=clightgreen)

* тѕєу▒╗:
* [ждќжАх](//www.solidot.org/)
* [Linux](//linux.solidot.org/)
* [уДЉтГд](//science.solidot.org/)
* [уДЉТіђ](//technology.solidot.org/)
* [уД╗тіе](//mobile.solidot.org/)
* [УІ╣Тъю](//apple.solidot.org/)
* [уАгС╗Х](//hardware.solidot.org/)
* [Уй»С╗Х](//software.solidot.org/)
* [т«ЅтЁе](//security.solidot.org/)
* [ТИИТѕЈ](//games.solidot.org/)
* [С╣ду▒Ї](//books.solidot.org/)
* [idle](//idle.solidot.org/)
* [С║ЉУ«Ау«Ќ](//cloud.solidot.org/)
* [жФўжБъуџёућхтГљТЏ┐У║Ф](//story.solidot.org/)

## тЁ│Т│еТѕЉС╗г№╝џ

solidotТќ░уЅѕуйЉуФЎтИИУДЂжЌ«жбў№╝їУ»иуѓ╣тЄ╗[У┐ЎжЄї](/QA)ТЪЦуюІсђѓ

## ТХѕТЂ»

**ТюгТќЄти▓УбФТЪЦуюІ 6500 ТгА**

## жЃетѕє Docker жЋютЃЈС╗ЇуёХтїЁтљФ XZ Utils тљјжЌе

[![т«ЅтЁе](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "т«ЅтЁе")

[Edwards](/~Edwards) (42866)тЈЉУАеС║ј 2025т╣┤08Тюѕ19ТЌЦ 23ТЌХ35тѕє ТўЪТюЪС║ї [Тќ░ТхфтЙ«тЇџтѕєС║Ф](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=82090&appkey=1370085986&title=%E9%83%A8%E5%88%86%20Docker%20%E9%95%9C%E5%83%8F%E4%BB%8D%E7%84%B6%E5%8C%85%E5%90%AB%20XZ%20Utils%20%E5%90%8E%E9%97%A8%20 "Тќ░ТхфтЙ«тЇџтѕєС║Ф")
![](https://icon.solidot.org/images/a7c7.png)

**ТЮЦУЄфТ│░тЮдуџётЦ│тдќ**

тј╗т╣┤тѕЮжюЄТЃіТЋ┤СИфт╝ђТ║љтњїуйЉу╗ют«ЅтЁеуцЙтї║уџё XZ тљјжЌеС║ІС╗Хт╣ХТ▓АТюЅуд╗ТѕЉС╗гУђїтј╗сђѓтюе XZ С║ІС╗ХСИГ№╝їТћ╗тЄ╗УђЁ Jia Tan№╝ѕтїќтљЇ№╝їТюфт┐ЁТў»тЇјС║║№╝ЅТйюС╝Ј XZ Utils жА╣уЏ«жЋ┐УЙЙСИцт╣┤тцџТЌХжЌ┤№╝їТюђу╗ѕУјитЙЌС┐АС╗╗ТѕљСИ║жА╣уЏ«уџётЁ▒тљїу╗┤ТіцУђЁ№╝їС╣ІтљјС╗ќТѕќС╗ќС╗гтѕЕућетЁХТЮЃжЎљТѓёТѓётюе xz-utils тїЁСИГТцЇтЁЦС║єСИђСИфтцЇТЮѓуџётљјжЌесђѓтюеТЂХТёЈуЅѕТюгтцДУДёТеАС╝аТњГтЅЇ№╝їтљјжЌет░▒УбФтЈЉуј░С║є№╝їтЏаТГцТ▓АТюЅжђаТѕљтцДжЌ«жбўсђѓСйє Binarly REsearch уџёУ░ЃТЪЦтЈЉуј░№╝їтюеТћ╗тЄ╗ТюЪжЌ┤Тъёт╗║уџёжЃетѕє Docker жЋютЃЈС╗ЇуёХтїЁтљФТюЅ XZ Utils тљјжЌесђѓт«ЅтЁеуаћуЕХС║║тЉўС╗ј DockerHub СИітЈЉуј░С║єУХЁУ┐Є 35 СИфтљФТюЅтљјжЌеуџёжЋютЃЈсђѓУЎйуёХТЋ░тГЌСИЇтцџ№╝їСйєуаћуЕХС║║тЉўтЈфТЅФТЈЈС║єСИђт░ЈжЃетѕєжЋютЃЈ№╝їУђїСИћтЈфжњѕт»╣ Debian тЈЉУАїуЅѕ№╝їтЁХт«ЃтЈЉУАїуЅѕтдѓ Fedora тњї OpenSUSE ТЃЁтєхТюфуЪЦсђѓ
www.binarly.io/blog/persistent-risk-xz-utils-backdoor-still-lurking-in-docker-images

[тЏътцЇ](/comments?sid=82090&op=reply&type=story)

№╗┐

ти▓у╗ЈжЏєСИГУхиТЮЦуџёТЮЃтіЏСИЇС╝џућ▒С║јтѕЏжђат«ЃуџёжѓБС║ЏС║║уџёУЅ»тЦйТё┐ТюЏУђїтЈўСИ║ТЌат«│сђѓ--т╝ЌжЄїтЙиТЏ╝

* [ждќжАх](/)
* [УЄ│жАХуйЉ](http://www.zhiding.cn)
* [тЙђТЌЦТќЄуФа](/?issume=20251006)
* [У┐Єтј╗уџёТіЋуЦе](/polllist)
* [у╝ќУЙЉС╗Іу╗Ї](/authors)
* [жџљуДЂТћ┐уГќ](/privacy)
* [Сй┐ућеТЮАТгЙ](/terms)
* [уйЉуФЎС╗Іу╗Ї](/introd)
* [RSS](/index.rss)

ТюгуФЎТЈљтѕ░уџёТЅђТюЅТ│етєїтЋєТаЄт▒ъС║јС╗ќС╗гтљёУЄфуџёТЅђТюЅС║║ТЅђТюЅ№╝їУ»ёУ«║т▒ъС║јтЁХтЈЉУАеУђЁТЅђТюЅ№╝їтЁХСйЎтєЁт«╣уЅѕТЮЃт▒ъС║ј solidot.org(2009-) ТЅђТюЅ сђѓ

[![php](https://icon.solidot.org/images/btn/php.gif)](//php.net/ "PHP ТюЇтіАтЎе")
[![apache](https://icon.solidot.org/images/btn/apache.gif)](//apache.org/ "Apache ТюЇтіАтЎе")
[![mysql](https://icon.solidot.org/images/btn/mysql.gif)](//www.mysql.com/ "MySQL")

[![](https://icon.solidot.org/images/btn/solidot-s.gif)](//www.solidot.org "solidot.org")

С║гICPУ»Ђ161336тЈи    [С║гICPтцЄ15039648тЈи-15](http://beian.miit.gov.cn) тїЌС║гтИѓтЁгт«Ѕт▒ђТхиТиђтѕєт▒ђтцЄТАѕтЈи№╝џ11010802021500 [![](//icon.zhiding.cn/beian/icon.png)](//icp.valu.cn/search/domain/solidot.org?verifyCode=pu7c4)

СИЙТіЦућхУ»Ю№╝џ010-62641205сђђТХЅТюфТѕљт╣┤С║║СИЙТіЦСИЊу║┐№╝џ010-62641208 СИЙТіЦжѓ«у«▒№╝џjubao@zhiding.cnсђђуйЉСИіТюЅт«│С┐АТЂ»СИЙТіЦСИЊтї║№╝џ<https://www.12377.cn>