---
title: Meta 开源其内部源码管理系统 Sapling
url: https://www.solidot.org/story?sid=73397
source: 奇客Solidot–传递最新科技情报
date: 2022-11-18
fetch_date: 2025-10-03T23:07:22.634954
---

# Meta 开源其内部源码管理系统 Sapling

[зҷ»еҪ•](/login) [жіЁеҶҢ](/register)

* ж–Үз«

  [еҫҖж—Ҙж–Үз«](/?issue=20251002)
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

**жң¬ж–Үе·Іиў«жҹҘзңӢ 6964 ж¬Ў**

## Meta ејҖжәҗе…¶еҶ…йғЁжәҗз Ғз®ЎзҗҶзі»з»ҹ Sapling

[![ејҖжәҗ](https://icon.solidot.org/images/topics/topicopensource.png?123)](/search?tid=3 "ејҖжәҗ")
[![Facebook](https://icon.solidot.org/images/topics/topicfacebook.png?123)](/search?tid=161 "Facebook")

[WinterIsComing](/~WinterIsComing) (31822)еҸ‘иЎЁдәҺ 2022е№ҙ11жңҲ17ж—Ҙ 16ж—¶45еҲҶ жҳҹжңҹеӣӣ [ж–°жөӘеҫ®еҚҡеҲҶдә«](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=73397&appkey=1370085986&title=Meta%20%E5%BC%80%E6%BA%90%E5%85%B6%E5%86%85%E9%83%A8%E6%BA%90%E7%A0%81%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F%20Sapling "ж–°жөӘеҫ®еҚҡеҲҶдә«")
![](https://icon.solidot.org/images/a7c7.png)

**жқҘиҮӘжӯҢеү§йҷўйӯ…еҪұ**

Git жҳҜе№ҝжіӣдҪҝз”Ёзҡ„жәҗз Ғз®ЎзҗҶзі»з»ҹпјҢдҪҶе®ғеңЁеӨ„зҗҶи§„жЁЎеәһеӨ§зҡ„жәҗд»Јз Ғеә“ж—¶йҖҹеәҰжҜ”иҫғж…ўгҖӮеҫ®иҪҜеҮ е№ҙеүҚеҸ‘еёғдәҶдёҖдёӘи§ЈеҶіж–№жЎҲеҸ« GVFSпјҲGit иҷҡжӢҹж–Үд»¶зі»з»ҹпјүгҖӮзҺ°еңЁеҸҰдёҖе®¶е·ЁеһӢе…¬еҸё Meta/Facebook е®ЈеёғдәҶе®ғзҡ„еҶ…йғЁи§ЈеҶіж–№жЎҲ SaplingгҖӮMeta з§°пјҢSapling йЎ№зӣ®е§ӢдәҺ 10 е№ҙеүҚпјҢж—ЁеңЁи§ЈеҶізҺ°жңүжәҗд»Јз Ғз®ЎзҗҶзі»з»ҹйҡҫд»ҘеӨ„зҗҶеәһеӨ§д»Јз Ғеә“зҡ„йҡҫйўҳпјҢдёҖејҖе§ӢжҳҜдҪңдёә Mercurial зҡ„жү©еұ•пјҢеҗҺжқҘеҝ«йҖҹжҲҗй•ҝдёәжңүзқҖиҮӘе·ұзҡ„еӯҳеӮЁж јејҸгҖҒзәҝзЁӢеҚҸи®®гҖҒз®—жі•е’ҢиЎҢдёәзҡ„зӢ¬з«Ӣзі»з»ҹгҖӮMeta зӣ®еүҚеҸӘејҖжәҗдәҶе…је®№ Git зҡ„ Sapling зі»з»ҹе®ўжҲ·з«ҜпјҢжңӘжқҘе°ҶдјҡејҖжәҗе…¶е®ғйғЁеҲҶгҖӮ
https://sapling-scm.com/
https://github.com/facebook/sapling

п»ҝ

дҪ иҮӘе·ұзҡ„д»Јз ҒеҰӮжһңи¶…иҝҮ6дёӘжңҲдёҚзңӢпјҢеҶҚзңӢзҡ„ж—¶еҖҷд№ҹдёҖж ·еғҸжҳҜеҲ«дәәеҶҷ--дјҠж је°”жЈ®е®ҡеҫӢ

* [йҰ–йЎө](/)
* [иҮійЎ¶зҪ‘](http://www.zhiding.cn)
* [еҫҖж—Ҙж–Үз«](/?issume=20251002)
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