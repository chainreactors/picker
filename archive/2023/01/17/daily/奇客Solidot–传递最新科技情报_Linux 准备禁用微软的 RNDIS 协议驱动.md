---
title: Linux 准备禁用微软的 RNDIS 协议驱动
url: https://www.solidot.org/story?sid=73897
source: 奇客Solidot–传递最新科技情报
date: 2023-01-17
fetch_date: 2025-10-04T04:03:32.421625
---

# Linux 准备禁用微软的 RNDIS 协议驱动

[зҷ»еҪ•](/login) [жіЁеҶҢ](/register)

* ж–Үз«

  [еҫҖж—Ҙж–Үз«](/?issue=20251003)
  [еҫҖж—ҘжҠ•зҘЁ](/polllist)
* зҡ®иӮӨ

  [и“қиүІ](/?theme=blue)
  [ж©ҷиүІ](/?theme=yellow)
  [з»ҝиүІ](/?theme=green)
  [жө…з»ҝиүІ](/?theme=clightgreen)

* еҲҶзұ»:
* [йҰ–йЎө](//www.solidot.org/)
* [Linux](//linux.solidot.org/)
* [з§‘еӯҰ](//science.solidot.org/)
* [з§‘жҠҖ](//technology.solidot.org/)
* [з§»еҠЁ](//mobile.solidot.org/)
* [иӢ№жһң](//apple.solidot.org/)
* [зЎ¬д»¶](//hardware.solidot.org/)
* [иҪҜд»¶](//software.solidot.org/)
* [е®үе…Ё](//security.solidot.org/)
* [жёёжҲҸ](//games.solidot.org/)
* [д№ҰзұҚ](//books.solidot.org/)
* [idle](//idle.solidot.org/)
* [дә‘и®Ўз®—](//cloud.solidot.org/)
* [й«ҳйЈһзҡ„з”өеӯҗжӣҝиә«](//story.solidot.org/)

## е…іжіЁжҲ‘д»¬пјҡ

solidotж–°зүҲзҪ‘з«ҷеёёи§Ғй—®йўҳпјҢиҜ·зӮ№еҮ»[иҝҷйҮҢ](/QA)жҹҘзңӢгҖӮ

## ж¶ҲжҒҜ

**жң¬ж–Үе·Іиў«жҹҘзңӢ 9270 ж¬Ў**

## Linux еҮҶеӨҮзҰҒз”Ёеҫ®иҪҜзҡ„ RNDIS еҚҸи®®й©ұеҠЁ

[![Linux](https://icon.solidot.org/images/topics/topiclinux.png?123)](/search?tid=7 "Linux")
[![е®үе…Ё](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "е®үе…Ё")

[Wilson](/~Wilson) (42865)еҸ‘иЎЁдәҺ 2023е№ҙ01жңҲ16ж—Ҙ 15ж—¶32еҲҶ жҳҹжңҹдёҖ [ж–°жөӘеҫ®еҚҡеҲҶдә«](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=73897&appkey=1370085986&title=Linux%20%E5%87%86%E5%A4%87%E7%A6%81%E7%94%A8%E5%BE%AE%E8%BD%AF%E7%9A%84%20RNDIS%20%E5%8D%8F%E8%AE%AE%E9%A9%B1%E5%8A%A8%20 "ж–°жөӘеҫ®еҚҡеҲҶдә«")
![](https://icon.solidot.org/images/a7c7.png)

**жқҘиҮӘжІҷзҡҮзҡ„йӮ®д»¶**

еҮәдәҺе®үе…ЁжӢ…еҝ§ Linux еҮҶеӨҮзҰҒз”Ёеҫ®иҪҜзҡ„ RNDIS еҚҸи®®й©ұеҠЁгҖӮRNDIS д»ЈиЎЁ Remote Network Driver Interface SpecificationпјҢжҳҜдёҖдёӘз§ҒжңүеҚҸи®®пјҢдё»иҰҒдҪҝз”Ё USB еҚҸи®®дҪңдёәе…¶дёӢеұӮдј иҫ“пјҢеҗ‘дёҠеұӮжҸҗдҫӣиҷҡжӢҹзҡ„д»ҘеӨӘзҪ‘иҝһжҺҘгҖӮ йҷӨдәҶ WindowsпјҢRNDIS еңЁи·Ёе№іеҸ°зҺҜеўғдёӯжІЎжңүе№ҝжіӣдҪҝз”ЁпјҢз”ұдәҺе®үе…ЁжӢ…еҝ§пјҢLinux еҶ…ж ёжӯЈеҜ»жұӮе°Ҷ RNDIS еҶ…ж ёй©ұеҠЁиҪ¬з§»еҲ° BROKEN Kconfig йҖүйЎ№пјҢеӣ жӯӨе®ғеңЁжңӘжқҘзҡ„еҶ…ж ёжһ„е»әдёӯе°Ҷиў«зҰҒз”ЁгҖӮеңЁиў«ж Үи®°дёә BROKEN дёҖж®өж—¶й—ҙд№ӢеҗҺпјҢй©ұеҠЁе°ҶеҸҜиғҪд»ҺдёҠжёёжәҗз Ғж ‘дёӯеҲ йҷӨгҖӮеҶ…ж ёзЁіе®ҡеҲҶж”Ҝз»ҙжҠӨиҖ… Greg Kroah-Hartman з§°пјҢRNDIS еңЁи®ҫи®ЎдёҠе°ұжҳҜдёҚе®үе…Ёзҡ„пјҢеӣ иҜҘеҚҸи®®дёҚеҸҜиғҪеҒҡеҲ°е®үе…ЁпјҢзҰҒз”Ёе…¶й©ұеҠЁе°ҶйҳІжӯўд»»дҪ•дәәдҪҝз”Ёе®ғгҖӮ
https://www.phoronix.com/news/Linux-Disabling-RNDIS-Drivers

п»ҝ

е®—ж•ҷдёҠжңҖж·ұзҡ„иҜҜи§ЈвҖ”вҖ”и®ӨдёәеқҸдәәжІЎжңүе®—ж•ҷгҖӮвҖ”вҖ”е°јйҮҮ

* [йҰ–йЎө](/)
* [иҮійЎ¶зҪ‘](http://www.zhiding.cn)
* [еҫҖж—Ҙж–Үз«](/?issume=20251003)
* [иҝҮеҺ»зҡ„жҠ•зҘЁ](/polllist)
* [зј–иҫ‘д»Ӣз»Қ](/authors)
* [йҡҗз§Ғж”ҝзӯ–](/privacy)
* [дҪҝз”ЁжқЎж¬ҫ](/terms)
* [зҪ‘з«ҷд»Ӣз»Қ](/introd)
* [RSS](/index.rss)

жң¬з«ҷжҸҗеҲ°зҡ„жүҖжңүжіЁеҶҢе•Ҷж ҮеұһдәҺд»–д»¬еҗ„иҮӘзҡ„жүҖжңүдәәжүҖжңүпјҢиҜ„и®әеұһдәҺе…¶еҸ‘иЎЁиҖ…жүҖжңүпјҢе…¶дҪҷеҶ…е®№зүҲжқғеұһдәҺ solidot.org(2009-) жүҖжңү гҖӮ

[![php](https://icon.solidot.org/images/btn/php.gif)](//php.net/ "PHP жңҚеҠЎеҷЁ")
[![apache](https://icon.solidot.org/images/btn/apache.gif)](//apache.org/ "Apache жңҚеҠЎеҷЁ")
[![mysql](https://icon.solidot.org/images/btn/mysql.gif)](//www.mysql.com/ "MySQL")

[![](https://icon.solidot.org/images/btn/solidot-s.gif)](//www.solidot.org "solidot.org")

дә¬ICPиҜҒ161336еҸ·    [дә¬ICPеӨҮ15039648еҸ·-15](http://beian.miit.gov.cn) еҢ—дә¬еёӮе…¬е®үеұҖжө·ж·ҖеҲҶеұҖеӨҮжЎҲеҸ·пјҡ11010802021500 [![](//icon.zhiding.cn/beian/icon.png)](//icp.valu.cn/search/domain/solidot.org?verifyCode=pu7c4)

дёҫжҠҘз”өиҜқпјҡ010-62641205гҖҖж¶үжңӘжҲҗе№ҙдәәдёҫжҠҘдё“зәҝпјҡ010-62641208 дёҫжҠҘйӮ®з®ұпјҡjubao@zhiding.cnгҖҖзҪ‘дёҠжңүе®ідҝЎжҒҜдёҫжҠҘдё“еҢәпјҡ<https://www.12377.cn>