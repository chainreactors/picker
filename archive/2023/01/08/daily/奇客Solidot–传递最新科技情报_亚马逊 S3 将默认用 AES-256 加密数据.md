---
title: 亚马逊 S3 将默认用 AES-256 加密数据
url: https://www.solidot.org/story?sid=73832
source: 奇客Solidot–传递最新科技情报
date: 2023-01-08
fetch_date: 2025-10-04T03:19:38.254352
---

# 亚马逊 S3 将默认用 AES-256 加密数据

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

**жң¬ж–Үе·Іиў«жҹҘзңӢ 5672 ж¬Ў**

## дәҡй©¬йҖҠ S3 е°Ҷй»ҳи®Өз”Ё AES-256 еҠ еҜҶж•°жҚ®

[![еҠ еҜҶжҠҖжңҜ](https://icon.solidot.org/images/topics/topicencryption.png?123)](/search?tid=70 "еҠ еҜҶжҠҖжңҜ")

[Wilson](/~Wilson) (42865)еҸ‘иЎЁдәҺ 2023е№ҙ01жңҲ07ж—Ҙ 22ж—¶14еҲҶ жҳҹжңҹе…ӯ [ж–°жөӘеҫ®еҚҡеҲҶдә«](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=73832&appkey=1370085986&title=%E4%BA%9A%E9%A9%AC%E9%80%8A%20S3%20%E5%B0%86%E9%BB%98%E8%AE%A4%E7%94%A8%20AES-256%20%E5%8A%A0%E5%AF%86%E6%95%B0%E6%8D%AE "ж–°жөӘеҫ®еҚҡеҲҶдә«")
![](https://icon.solidot.org/images/a7c7.png)

**жқҘиҮӘдјҰж•Ұеңәең°**

дәҡй©¬йҖҠ Simple Storage Service (S3)е°Ҷй»ҳи®ӨеңЁжңҚеҠЎеҷЁз«Ҝз”Ё AES-256 иҮӘеҠЁеҠ еҜҶж–°ж•°жҚ®гҖӮAWS зҡ„жңҚеҠЎеҷЁз«ҜеҠ еҜҶе·Із»ҸеӯҳеңЁдәҶеҚҒеӨҡе№ҙпјҢдҪҶзҺ°еңЁдёәдәҶеҠ ејәе®үе…Ёе°Ҷй»ҳи®ӨеҗҜз”ЁгҖӮз®ЎзҗҶе‘ҳж— йңҖйҮҮеҸ–д»»дҪ•иЎҢеҠЁпјҢдәҡй©¬йҖҠиЎЁзӨәеҠ еҜҶдёҚдјҡеҜ№жҖ§иғҪдә§з”ҹд»»дҪ•еҪұе“ҚгҖӮй»ҳи®Өзҡ„еҠ еҜҶз®—жі•жҳҜ AES-256пјҢз®ЎзҗҶе‘ҳеҸҜд»ҘйҖүжӢ© SSE-C жҲ– SSE-KMS зӯүжӣҝд»Јж–№жі•гҖӮе…¶дёӯ SSE-C е°Ҷз”ұеӯҳеӮЁжЎ¶зҡ„жүҖжңүиҖ…жҺ§еҲ¶еҜҶй’ҘпјҢSSE-KMS е°Ҷз”ұдәҡй©¬йҖҠз®ЎзҗҶеҜҶй’ҘгҖӮеӯҳеӮЁжЎ¶зҡ„жүҖжңүиҖ…иҝҳеҸҜд»ҘдёәжҜҸдёӘ KMS еҜҶй’Ҙи®ҫзҪ®дёҚеҗҢзҡ„жқғйҷҗд»ҘдҫҝдәҺз»ҶеҢ–жҺ§еҲ¶гҖӮ
https://aws.amazon.com/blogs/aws/amazon-s3-encrypts-new-objects-by-default/

п»ҝ

еҚғйҮҢд№ӢиЎҢе§ӢдәҺи¶ідёӢпјҢд№қеұӮд№ӢеҸ°иө·дәҺеһ’еңҹгҖӮ

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