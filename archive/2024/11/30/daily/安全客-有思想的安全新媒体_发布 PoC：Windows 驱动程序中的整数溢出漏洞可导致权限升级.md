---
title: 发布 PoC：Windows 驱动程序中的整数溢出漏洞可导致权限升级
url: https://www.anquanke.com/post/id/302305
source: 安全客-有思想的安全新媒体
date: 2024-11-30
fetch_date: 2025-10-06T19:13:46.297626
---

# 发布 PoC：Windows 驱动程序中的整数溢出漏洞可导致权限升级

йҰ–йЎө

йҳ…иҜ»

* [е®үе…Ёиө„и®Ҝ](https://www.anquanke.com/news)
* [е®үе…ЁзҹҘиҜҶ](https://www.anquanke.com/knowledge)
* [е®үе…Ёе·Ҙе…·](https://www.anquanke.com/tool)

жҙ»еҠЁ

зӨҫеҢә

еӯҰйҷў

е®үе…ЁеҜјиҲӘ

еҶ…е®№зІҫйҖү

* [дё“ж Ҹ](/column/index.html)
* [зІҫйҖүдё“йўҳ](https://www.anquanke.com/subject-list)
* [е®үе…ЁKERеӯЈеҲҠ](https://www.anquanke.com/discovery)
* [360зҪ‘з»ңе®үе…Ёе‘ЁжҠҘ](https://www.anquanke.com/week-list)

# еҸ‘еёғ PoCпјҡWindows й©ұеҠЁзЁӢеәҸдёӯзҡ„ж•ҙж•°жәўеҮәжјҸжҙһеҸҜеҜјиҮҙжқғйҷҗеҚҮзә§

йҳ…иҜ»йҮҸ**85447**

еҸ‘еёғж—¶й—ҙ : 2024-11-29 11:22:55

**x**

##### иҜ‘ж–ҮеЈ°жҳҺ

жң¬ж–ҮжҳҜзҝ»иҜ‘ж–Үз« пјҢж–Үз« еҺҹдҪңиҖ… do sonпјҢж–Үз« жқҘжәҗпјҡsecurityonline

еҺҹж–Үең°еқҖпјҡ<https://securityonline.info/integer-overflow-vulnerability-in-windows-driver-enables-privilege-escalation-poc-published/>

иҜ‘ж–Үд»…дҫӣеҸӮиҖғпјҢе…·дҪ“еҶ…е®№иЎЁиҫҫд»ҘеҸҠеҗ«д№үеҺҹж–ҮдёәеҮҶгҖӮ

![Windows 11 22H2 security updates]()

дёҖеҗҚзӢ¬з«Ӣз ”з©¶дәәе‘ҳеңЁ ksthunk.sys й©ұеҠЁзЁӢеәҸдёӯеҸ‘зҺ°дәҶдёҖдёӘе…ій”®жјҸжҙһпјҢиҜҘй©ұеҠЁзЁӢеәҸжҳҜ Windows ж“ҚдҪңзі»з»ҹдёӯиҙҹиҙЈдҝғиҝӣ 32 дҪҚеҲ° 64 дҪҚиҝӣзЁӢйҖҡдҝЎзҡ„дёҖдёӘз»„д»¶гҖӮиҜҘжјҸжҙһе…Ғи®ёжң¬ең°ж”»еҮ»иҖ…еҲ©з”Ёж•ҙж•°жәўеҮәе®һзҺ°жқғйҷҗеҚҮзә§пјҢиҜҘжјҸжҙһе·ІеңЁи‘—еҗҚзҡ„ TyphoonPWN 2024 жҙ»еҠЁдёӯиў«жҲҗеҠҹжј”зӨәе’Ңејәи°ғпјҢе№¶иҺ·еҫ—дәҶз¬¬дәҢеҗҚзҡ„еҘҪжҲҗз»©гҖӮ

иҜҘжјҸжҙһеӯҳеңЁдәҺ CKSAutomationThunk::ThunkEnableEventIrp еҮҪж•°дёӯпјҢиҜҘеҮҪж•°еҲҶй…Қзј“еҶІеҢәз”ЁдәҺз®ЎзҗҶеҶ…ж ёдёӯзҡ„иҫ“е…Ҙе’Ңиҫ“еҮәж•°жҚ®гҖӮй—®йўҳжәҗдәҺеңЁзј“еҶІеҢәеӨ§е°ҸеҜ№йҪҗи®Ўз®—иҝҮзЁӢдёӯзјәд№Ҹж•ҙж•°жәўеҮәйӘҢиҜҒгҖӮиҝҷдёҖз–ҸеҝҪеҜјиҮҙеҲҶй…ҚеӨ§е°ҸдёҚеҪ“пјҢеј•еҸ‘е ҶжәўеҮәпјҢдҪҝж”»еҮ»иҖ…иғҪеӨҹиҰҶзӣ–зӣёйӮ»еҶ…еӯҳгҖӮ

```
// Only Called when the calling process is 32bit.
__int64 __fastcall CKSAutomationThunk::ThunkEnableEventIrp(__int64 a1, PIRP a2, __int64 a3, int *a4)
{
  ...
  inbuflen = CurrentStackLocation->Parameters.DeviceIoControl.InputBufferLength;
  outbuflen = CurrentStackLocation->Parameters.DeviceIoControl.OutputBufferLength;
  // [1]. Align the length of output buffer
  outlen_adjust = (outbuflen + 0x17) & 0xFFFFFFF8;
  if ( a2->AssociatedIrp.MasterIrp )
    return 1i64;

  if ( (unsigned int)inbuflen < 0x18 )
    ExRaiseStatus(-1073741306);

  ProbeForRead(CurrentStackLocation->Parameters.DeviceIoControl.Type3InputBuffer, inbuflen, 1u);
  if ( (*((_DWORD *)CurrentStackLocation->Parameters.DeviceIoControl.Type3InputBuffer + 5) & 0xEFFFFFFF) == 1
    || (*((_DWORD *)CurrentStackLocation->Parameters.DeviceIoControl.Type3InputBuffer + 5) & 0xEFFFFFFF) == 2
    || (*((_DWORD *)CurrentStackLocation->Parameters.DeviceIoControl.Type3InputBuffer + 5) & 0xEFFFFFFF) == 4 )
  {
    // [2]. Validate the Length
    if ( (unsigned int)outbuflen < 0x10 )
      ExRaiseStatus(-1073741306);
    if ( outlen_adjust < (int)outbuflen + 16 || outlen_adjust + (unsigned int)inbuflen < outlen_adjust )
      ExRaiseStatus(-1073741306);

    // [3]. Allocate the buffer to store the data
    // 0x61 == POOL_FLAG_USE_QUOTA | POOL_FLAG_RAISE_ON_FAILURE POOL_FLAG_NON_PAGED
    a2->AssociatedIrp.MasterIrp = (struct _IRP *)ExAllocatePool2(
                                                   0x61i64,
                                                   outlen_adjust + (unsigned int)inbuflen,
                                                   1886409547i64);
    a2->Flags |= 0x30u;
    ProbeForRead(a2->UserBuffer, outbuflen, 1u); // [*]
    data = (__int64)a2->AssociatedIrp.MasterIrp;
    ...
    // [4]. Copy the Data
    if ( (unsigned int)outbuflen > 0x10 )
      memmove((void *)(data + 0x20), (char *)a2->UserBuffer + 16, outbuflen - 16);
    memmove(
      (char *)a2->AssociatedIrp.MasterIrp + outlen_adjust,
      CurrentStackLocation->Parameters.FileSystemControl.Type3InputBuffer,
      inbuflen);
    ...
}
```

SSD Secure Disclosure жҠҖжңҜеӣўйҳҹи§ЈйҮҠиҜҙпјҡ вҖңеңЁ [1] еӨ„пјҢи®Ўз®— outbuflen + 0x17 ж—¶жІЎжңүж•ҙж•°жәўеҮәйӘҢиҜҒгҖӮеӣ жӯӨпјҢoutlen\_adjust еҸҜиғҪиў«и®ҫзҪ®дёәдёҖдёӘиҫғе°Ҹзҡ„еҖјпјҢеҜјиҮҙеҲҶй…ҚдёҚи¶іпјҢжңҖз»ҲеңЁ [4] еӨ„еӨҚеҲ¶ж•°жҚ®ж—¶еҸ‘з”ҹе ҶжәўеҮәгҖӮ

иҜҘжјҸжҙһеҲ©з”ЁдёҖзі»еҲ—жӯҘйӘӨз»•иҝҮеҶ…ж ёдҝқжҠӨжҺӘж–ҪпјҢиҺ·еҫ—зі»з»ҹзә§жқғйҷҗпјҡ

1. **еҶ…еӯҳж“Қзәө**пјҡ ж”»еҮ»иҖ…еңЁеҶ…ж ёйқһеҲҶйЎөжұ дёӯе‘ҪеҗҚзҡ„з®ЎйҒ“еҜ№иұЎд№Ӣй—ҙеҲ¶йҖ й—ҙйҡҷпјҢд»ҺиҖҢжӣҙе®№жҳ“еҲ©з”ЁжәўеҮәгҖӮ
2. **д»»ж„ҸеҶ…еӯҳи®ҝй—®**пјҡ йҖҡиҝҮз ҙеқҸзӣёйӮ»зҡ„е‘ҪеҗҚз®ЎйҒ“пјҢж”»еҮ»иҖ…еҸҜиҺ·еҫ—д»»ж„ҸиҜ»еҶҷиғҪеҠӣгҖӮ
3. **д»ӨзүҢйҮҚеҶҷ**пјҡ ж”»еҮ»иҖ…дҝ®ж”№еҪ“еүҚиҝӣзЁӢд»ӨзүҢд»ҘиҺ·еҫ— SYSTEM жқғйҷҗпјҢд»ҺиҖҢе®Ңе…ЁжҺ§еҲ¶жңәеҷЁгҖӮ

иҜҘжјҸжҙһе·ІйҖҡзҹҘеҫ®иҪҜпјҢдҪҶеҫ®иҪҜеЈ°з§°иҝҷжҳҜдёҖдёӘе·Із»Ҹи§ЈеҶізҡ„йҮҚеӨҚй—®йўҳгҖӮе°Ҫз®ЎжңүиҝҷдәӣдҝқиҜҒпјҢдҪҶз ”з©¶дәәе‘ҳеҸ‘зҺ°иҜҘжјҸжҙһд»ҚеҸҜеңЁ Windows 11 23H2 дёҠиў«еҲ©з”ЁгҖӮиҝ„д»ҠдёәжӯўпјҢе°ҡжңӘжҸҗдҫӣ CVE зј–еҸ·жҲ–иҜҰз»Ҷзҡ„иЎҘдёҒдҝЎжҒҜгҖӮ

иҜҘжјҸжҙһдҪ“зҺ°дәҶдёҺеҶ…ж ёзә§жјҸжҙһзӣёе…ізҡ„йЈҺйҷ©гҖӮйҖҡиҝҮй©ұеҠЁзЁӢеәҸеҚҮзә§жқғйҷҗзҡ„иғҪеҠӣеҮёжҳҫдәҶеҶ…ж ёд»Јз ҒдёҘж јйӘҢиҜҒзҡ„йҮҚиҰҒжҖ§гҖӮжӯЈеҰӮ SSD Secure Disclosure жүҖжҢҮеҮәзҡ„пјҢз”ұдәҺж¶үеҸҠзҡ„еҲҶй…ҚеӨ§е°Ҹе’Ңж•°жҚ®жҳҜеҸҜжҺ§зҡ„пјҢеӣ жӯӨеҲ©з”ЁиҝҷдёӘжјҸжҙһ вҖңе№¶дёҚйҡҫвҖқпјҢиҝҷдҪҝе®ғжҲҗдёәй«ҳзә§еЁҒиғҒиЎҢдёәиҖ…зҡ„жҪңеңЁе·Ҙе…·гҖӮ

иҰҒйҳ…иҜ»жҠҖжңҜз»ҶиҠӮе’ҢжҰӮеҝөйӘҢиҜҒпјҲPoCпјүд»Јз ҒпјҢиҜ·и®ҝй—® SSD е®үе…ЁжҠ«йңІзҡ„е®ҳж–№е…¬е‘ҠгҖӮ

жң¬ж–Үзҝ»иҜ‘иҮӘsecurityonline [еҺҹж–Үй“ҫжҺҘ](https://securityonline.info/integer-overflow-vulnerability-in-windows-driver-enables-privilege-escalation-poc-published/)гҖӮеҰӮиӢҘиҪ¬иҪҪиҜ·жіЁжҳҺеҮәеӨ„гҖӮ

е•ҶеҠЎеҗҲдҪңпјҢж–Үз« еҸ‘еёғиҜ·иҒ”зі» anquanke@360.cn

жң¬ж–Үз”ұ**е®үе…Ёе®ў**еҺҹеҲӣеҸ‘еёғ

иҪ¬иҪҪпјҢиҜ·еҸӮиҖғ[иҪ¬иҪҪеЈ°жҳҺ](https://www.anquanke.com/note/repost)пјҢжіЁжҳҺеҮәеӨ„пјҡ [https://www.anquanke.com/post/id/302305](/post/id/302305)

е®үе…ЁKER - жңүжҖқжғізҡ„е®үе…Ёж–°еӘ’дҪ“

жң¬ж–ҮиҪ¬иҪҪиҮӘ: [securityonline](https://securityonline.info/integer-overflow-vulnerability-in-windows-driver-enables-privilege-escalation-poc-published/)

еҰӮиӢҘиҪ¬иҪҪ,иҜ·жіЁжҳҺеҮәеӨ„пјҡ <https://securityonline.info/integer-overflow-vulnerability-in-windows-driver-enables-privilege-escalation-poc-published/>

е®үе…ЁKER - жңүжҖқжғізҡ„е®үе…Ёж–°еӘ’дҪ“

еҲҶдә«еҲ°пјҡ![еҫ®дҝЎ](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [жјҸжҙһ](/tag/%D0%B6%D1%98%D2%B8%D0%B6%D2%99%D2%BB)
* [жјҸжҙһжғ…жҠҘ](/tag/%D0%B6%D1%98%D2%B8%D0%B6%D2%99%D2%BB%D0%B6%D2%93%E2%80%A6%D0%B6%D2%A0%D2%98)

**+1**0иөһ

ж”¶и—Ҹ

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)е®үе…Ёе®ў

еҲҶдә«еҲ°пјҡ![еҫ®дҝЎ](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## еҸ‘иЎЁиҜ„и®ә

жӮЁиҝҳжңӘзҷ»еҪ•пјҢиҜ·е…Ҳзҷ»еҪ•гҖӮ

[зҷ»еҪ•](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

[е®үе…Ёе®ў](/member.html?memberId=173683)

иҝҷдёӘдәәеӨӘжҮ’дәҶпјҢзӯҫеҗҚйғҪжҮ’еҫ—еҶҷдёҖдёӘ

* ж–Үз«
* **553**

* зІүдёқ
* **2**

### TAзҡ„ж–Үз«

* ##### [е№ҙеәҰзӣҳзӮ№пјҡAI+е®үе…ЁеҸҢйҮҚиөӢиғҪпјҢ360и§Јй”ҒдјҒдёҡжөҸи§ҲеҷЁж–°еҠЁеҠӣ](/post/id/303791)

  2025-01-24 10:00:53
* ##### [IntelBroker зҡ„ж•°еӯ—и¶іиҝ№пјҡ OSINT еҲҶжһҗжҸӯйңІзҪ‘з»ңзҠҜзҪӘеҲҶеӯҗзҡ„иЎҢеҠЁ](/post/id/303788)

  2025-01-24 09:55:58
* ##### [7-Zip дҝ®еӨҚдәҶеҸҜз»•иҝҮ Windows MoTW е®үе…ЁиӯҰе‘Ҡзҡ„й”ҷиҜҜпјҢз«ӢеҚідҝ®иЎҘ](/post/id/303776)

  2025-01-24 09:49:56
* ##### [Microsoft еңЁ Edge Stable дёӯйў„и§Ҳ Game Assist жёёжҲҸеҶ…жөҸи§ҲеҷЁ](/post/id/303773)

  2025-01-24 09:43:16
* ##### [ModiLoader жҒ¶ж„ҸиҪҜд»¶еҲ©з”Ё CAB ж ҮеӨҙжү№еӨ„зҗҶж–Үд»¶йҖғйҒҝжЈҖжөӢ](/post/id/303770)

  2025-01-24 09:36:10

### зӣёе…іж–Үз«

* ##### [Apache Airflow еӯҳеңЁжқғйҷҗжјҸжҙһпјҢеҸҜеҜјиҮҙеҸӘиҜ»з”ЁжҲ·иҺ·еҸ–ж•Ҹж„ҹдҝЎжҒҜ](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Formbricks еӯҳеңЁй«ҳеҚұжјҸжҙһ (CVE-2025-59934)пјҢж”»еҮ»иҖ…еҸҜйҖҡиҝҮдјӘйҖ JWTд»ӨзүҢеҜјиҮҙжңӘжҺҲжқғзҡ„еҜҶз ҒйҮҚзҪ®](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ дёӯеӯҳеңЁDLLеҠ«жҢҒжјҸжҙһпјҲCVE-2025-56383пјүпјҢеҸҜеҜјиҮҙд»»ж„Ҹд»Јз Ғжү§иЎҢпјҢдё”POCе·Іе…¬ејҖ](/post/id/312448)

  2025-09-29 18:04:33
* ##### [CISAз§°й»‘е®ўеҲ©з”ЁGeoServerжјҸжҙһжҲҗеҠҹе…ҘдҫөдёҖиҒ”йӮҰжңәжһ„](/post/id/312347)

  2025-09-24 16:45:06
* ##### [SolarWindsзҙ§жҖҘеҸ‘еёғиЎҘдёҒпјҢдҝ®еӨҚй«ҳеҚұиҝңзЁӢд»Јз Ғжү§иЎҢжјҸжҙһCVE-2025-26399](/post/id/312357)

  2025-09-24 ...