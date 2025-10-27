---
title: 攻防演练中红队常用的攻击方法之横向移动（上）
url: https://blog.csdn.net/ZAWX_NETSTARSEC/article/details/131561487
source: ZAWX_NETSTARSEC的博客
date: 2023-07-06
fetch_date: 2025-10-04T11:53:09.729780
---

# 攻防演练中红队常用的攻击方法之横向移动（上）

# ж”»йҳІжј”з»ғдёӯзәўйҳҹеёёз”Ёзҡ„ж”»еҮ»ж–№жі•д№ӢжЁӘеҗ‘з§»еҠЁпјҲдёҠпјү

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[![](https://csdnimg.cn/release/blogv2/dist/pc/img/identityVipNew.png)](https://mall.csdn.net/vip)
[зҪ‘жҳҹе®үе…ЁпјҲдёӯе®үзҪ‘жҳҹпјү](https://blog.csdn.net/ZAWX_NETSTARSEC "зҪ‘жҳҹе®үе…ЁпјҲдёӯе®үзҪ‘жҳҹпјү")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCurrentTime2.png)
дәҺ 2023-07-05 18:09:56 еҸ‘еёғ

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
йҳ…иҜ»йҮҸ1.1k
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
ж”¶и—Ҹ

2

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
зӮ№иөһж•°
1

CC 4.0 BY-SAзүҲжқғ

ж–Үз« ж Үзӯҫпјҡ
[зҪ‘з»ң](https://so.csdn.net/so/search/s.do?q=%E7%BD%91%E7%BB%9C&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[е®үе…Ё](https://so.csdn.net/so/search/s.do?q=%E5%AE%89%E5%85%A8&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[иҝҗз»ҙ](https://so.csdn.net/so/search/s.do?q=%E8%BF%90%E7%BB%B4&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

зүҲжқғеЈ°жҳҺпјҡжң¬ж–ҮдёәеҚҡдё»еҺҹеҲӣж–Үз« пјҢйҒөеҫӘ [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) зүҲжқғеҚҸи®®пјҢиҪ¬иҪҪиҜ·йҷ„дёҠеҺҹж–ҮеҮәеӨ„й“ҫжҺҘе’Ңжң¬еЈ°жҳҺгҖӮ

жң¬ж–Үй“ҫжҺҘпјҡ<https://blog.csdn.net/ZAWX_NETSTARSEC/article/details/131561487>

![](https://i-operation.csdnimg.cn/images/a7311a21245d4888a669ca3155f1f4e5.png)жң¬ж–Үйҳҗиҝ°дәҶжЁӘеҗ‘з§»еҠЁж”»еҮ»зҡ„еҺҹзҗҶпјҢйҖҡиҝҮж”»еҮ»иҖ…и§Ҷи§’иҝҳеҺҹж”»еҮ»иҝҮзЁӢпјҢеҢ…жӢ¬дҝЎжҒҜж”¶йӣҶгҖҒеҹҹжҺ§зҷ»еҪ•е’ҢжқғйҷҗиҺ·еҸ–дёүдёӘйҳ¶ж®өгҖӮдјҒдёҡеҶ…зҪ‘еӣ е…¶и®Ўз®—жңәиҒҡйӣҶжҖ§е’Ңж•Ҹж„ҹдҝЎжҒҜеӯҳеӮЁпјҢжҲҗдёәжЁӘеҗ‘з§»еҠЁзҡ„йҮҚзҒҫеҢәгҖӮй»‘е®ўйҖҡиҝҮжҸҗжқғзӯүжүӢж®өпјҢе®һзҺ°еҜ№е…ій”®дҝЎжҒҜе’Ңж•Ҹж„ҹж•°жҚ®зҡ„иҺ·еҸ–пјҢеҜ№зҪ‘з»ңе®үе…Ёжһ„жҲҗдёҘйҮҚеЁҒиғҒгҖӮ

жЁӘеҗ‘з§»еҠЁпјҢжҳҜж”»еҮ»иҖ…дҫөе…ҘдјҒдёҡзі»з»ҹж—¶пјҢиҺ·еҸ–зӣёе…іжқғйҷҗеҸҠйҮҚиҰҒж•°жҚ®зҡ„еёёи§Ғж”»еҮ»жүӢжі•гҖӮдәҶи§ЈжЁӘеҗ‘з§»еҠЁзҡ„еҺҹзҗҶжңүеҠ©дәҺдёӘдәәе’ҢдјҒдёҡжӣҙеҘҪең°з»ҙжҠӨзҪ‘з»ңе®үе…ЁгҖӮ

дёӯе®үзҪ‘жҳҹзү№жӯӨжҺЁеҮәдәҶжЁӘеҗ‘з§»еҠЁз§‘жҷ®зі»еҲ—пјҢжң¬зі»еҲ—е…ұжңүдёүзҜҮж–Үз« гҖӮ

иҝ‘е№ҙжқҘпјҢйҡҸзқҖзҪ‘з»ңж”»еҮ»гҖҒеӢ’зҙўдәӢд»¶йў‘еҸ‘пјҢдјҒдёҡе®үе…ЁйҳІжҠӨйңҖжұӮиҝ…йҖҹдёҠеҚҮпјҢдј з»ҹе®үе…ЁйҳІжҠӨдёӯд»ҘеҜҶз Ғе’Ңжқғйҷҗз®ЎзҗҶдёәж ёеҝғзҡ„еҚ•дёҖйҳІжҠӨжЁЎејҸж„ҲеҸ‘дёҚиғҪж»Ўи¶ізӣ®еүҚзҡ„зҪ‘з»ңе®үе…ЁзҺҜеўғгҖӮеӣ иҖҢпјҢж·ұе…ҘдәҶи§Јж”»еҮ»жҖқи·ҜпјҢвҖңеҜ№з—ҮдёӢиҚҜвҖқпјҢжҳҜзӣ®еүҚзҪ‘з»ңе®үе…ЁиЎҢдёҡеҸ‘еұ•зҡ„йҮҚиҰҒж–№еҗ‘гҖӮ

жң¬зҜҮж–Үз« е°Ҷе°ұвҖңжЁӘеҗ‘з§»еҠЁвҖқиҝҷдёҖе…ёеһӢж”»еҮ»иЎҢдёәиҝӣиЎҢз®ҖеҚ•йҳҗиҝ°пјҢд»Һж”»еҮ»иҖ…и§Ҷи§’иҝҳеҺҹвҖңжЁӘеҗ‘з§»еҠЁвҖқж”»еҮ»иҝҮзЁӢдёӯзҡ„е…ёеһӢеңәжҷҜпјҢдёәж·ұе…Ҙеү–жһҗвҖңжЁӘеҗ‘з§»еҠЁвҖқж”»еҮ»иЎҢдёәжҸҗдҫӣз®ҖеҚ•еҸӮиҖғгҖӮ

з®ҖеҚ•жқҘи®ІпјҢжЁӘеҗ‘з§»еҠЁжҳҜжҢҮж”»еҮ»иҖ…жҲҗеҠҹж”»еҮ»дёҖеҸ°и®Ўз®—жңәеҗҺпјҢз”ұиҜҘи®Ўз®—жңәжЁӘеҗ‘и·Ёи¶ҠеҲ°еҸҰдёҖеҸ°и®Ўз®—жңәпјҢиҺ·еҸ–зӣёе…іжқғйҷҗпјҢиҝӣиҖҢзӘғеҸ–ж•Ҹж„ҹдҝЎжҒҜзҡ„жҙ»еҠЁгҖӮ

д»Һе®ҡд№үдёҠжқҘзңӢпјҢжҲ‘д»¬дёҚйҡҫеҸ‘зҺ°пјҢвҖңжЁӘеҗ‘з§»еҠЁвҖқж”»еҮ»зҡ„дё»иҰҒзӣ®ж ҮжҳҜдјҒдёҡе…ій”®дҝЎжҒҜеҸҠзӣёе…із®ЎзҗҶжқғйҷҗпјҢиҖҢжЁӘеҗ‘и·Ёи¶Ҡзҡ„ж”»еҮ»еұһжҖ§д№ҹиЎЁжҳҺиҝҷдёҖж”»еҮ»иЎҢдёәеӨҡж•°жғ…еҶөдёӢеҸ‘з”ҹеңЁдјҒдёҡеҶ…зҪ‘дёӯгҖӮ

жҚўдёӘи§’еәҰжқҘи®ІпјҢд№ҹжӯЈжҳҜз”ұдәҺдјҒдёҡеҶ…зҪ‘дёӯи®Ўз®—жңәеӯҳеңЁиҒҡйӣҶжҖ§пјҢд»ҘеҸҠеҶ…зҪ‘дёӯдёҖдәӣйӣҶжқғз®ЎзҗҶи®ҫеӨҮеӮЁеӯҳжңүеӨ§йҮҸиә«д»ҪеҮӯиҜҒдҝЎжҒҜеҸҠе…ій”®ж•°жҚ®пјҢдҪҝеҫ—дјҒдёҡеҶ…зҪ‘жӣҙе®№жҳ“жҲҗдёәж”»еҮ»иҖ…зҡ„зӣ®ж ҮпјҢд№ҹе°ұжҲҗдёәдәҶжЁӘеҗ‘з§»еҠЁзҡ„йҮҚзҒҫеҢәгҖӮ

еҹәдәҺиҝҷж ·зҡ„еүҚжҸҗпјҢжң¬зҜҮж–Үз« е°Ҷд»ҘвҖңдјҒдёҡеҶ…зҪ‘дёӯзҡ„жЁӘеҗ‘з§»еҠЁвҖқж”»еҮ»и·Ҝеҫ„дёәдҫӢпјҢе°ҪйҮҸе…Ёйқўзҡ„еұ•зӨәвҖңжЁӘеҗ‘з§»еҠЁвҖқж”»еҮ»зҡ„жҖқи·ҜдёҺж–№жі•гҖӮ

**дёҖгҖҒдјҒдёҡеҶ…зҪ‘дёӯзҡ„жЁӘеҗ‘з§»еҠЁ**

еҒҮи®ҫдёҖе®¶дјҒдёҡе°ҶдҝқеӯҳжңүжүҖжңүи®Ўз®—жңәз”ЁжҲ·иҙҰеҸ·еҜҶз ҒдҝЎжҒҜзҡ„ж–Үд»¶еӯҳж”ҫеңЁеҹҹжҺ§дё»жңәдёҠпјҢеҗҢж—¶и®ҫзҪ®еҸӘжңүз®ЎзҗҶе‘ҳжүҚеҸҜд»ҘжҹҘзңӢгҖӮ

зҺ°еңЁжңүдёҖдҪҚз»ҸйӘҢдё°еҜҢзҡ„й»‘е®ўжғіиҰҒзӘғеҸ–иҜҘж–Үд»¶гҖӮ

**Step 1 : гҖҗдҝЎжҒҜж”¶йӣҶгҖ‘**

йҰ–е…Ҳй»‘е®ўйҖҡиҝҮдёҖзі»еҲ—ж”»еҮ»жүӢж®өиҝӣе…ҘдёҖеҸ°жҷ®йҖҡе‘ҳе·Ҙзҡ„и®Ўз®—жңәпјҢдҪҶжҳҜиҝҷеҸ°и®Ўз®—жңәдёҠеҸӘжңүиҜҘе‘ҳе·Ҙе№іж—¶е·ҘдҪңдҪҝз”Ёзҡ„PPTпјҢж–Үд»¶зӯүеҶ…е®№пјҢжІЎжңүй«ҳж•Ҹж„ҹдҝЎжҒҜгҖӮ

жӯӨж—¶д»–е°Ҷж”¶йӣҶеҹҹеҶ…дҝЎжҒҜпјҢжҺўжҹҘеҸҜиғҪдҝқеӯҳжңәеҜҶж–Үд»¶е’Ңж•Ҹж„ҹдҝЎжҒҜзҡ„дё»жңәдҪҚзҪ®пјҢзЎ®е®ҡжЁӘеҗ‘з§»еҠЁзҡ„зӣ®ж ҮгҖӮ

еҲҶжһҗеҗҺпјҢй»‘е®ўеҸ‘зҺ°иҜҘдјҒдёҡйҮҮз”Ёзҡ„жҳҜADеҹҹжқҘз®ЎзҗҶеҶ…зҪ‘и®Ўз®—жңәз”ЁжҲ·пјҢж №жҚ®з»ҸйӘҢеҫ—зҹҘпјҢеҹҹжҺ§дёҠеӯҳеӮЁжңүжүҖжңүи®Ўз®—жңәз”ЁжҲ·зҡ„иҙҰеҸ·еҜҶз ҒдҝЎжҒҜпјҢдәҺжҳҜд»–еҶіе®ҡжЁӘеҗ‘з§»еҠЁеҲ°еҹҹжҺ§дё»жңәгҖӮ

![](https://csdnimg.cn/release/blogv2/dist/pc/img/lock.png)жңҖдҪҺ0.47е…ғ/еӨ© и§Јй”Ғж–Үз«

200дёҮдјҳиҙЁеҶ…е®№ж— йҷҗз•…еӯҰ

![](https://csdnimg.cn/release/blogv2/dist/pc/img/vip-limited-close-newWhite.png)

зЎ®е®ҡиҰҒж”ҫејғжң¬ж¬Ўжңәдјҡпјҹ

зҰҸеҲ©еҖ’и®Ўж—¶

*:*

*:*

![](https://csdnimg.cn/release/blogv2/dist/pc/img/vip-limited-close-roup.png)
з«ӢеҮҸ ВҘ

жҷ®йҖҡVIPе№ҙеҚЎеҸҜз”Ё

[з«ӢеҚідҪҝз”Ё](https://mall.csdn.net/vip)

[![](https://profile-avatar.csdnimg.cn/8b87a58891594bbaab06aa3616d9a702_zawx_netstarsec.jpg!1)

зҪ‘жҳҹе®үе…ЁпјҲдёӯе®үзҪ‘жҳҹпјү](https://blog.csdn.net/ZAWX_NETSTARSEC)

е…іжіЁ
е…іжіЁ

* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarThumbUpactive.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/like-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/like.png)

  1

  зӮ№иөһ
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike.png)

  иё©
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectActive.png)

  2

  ж”¶и—Ҹ

  и§үеҫ—иҝҳдёҚй”ҷ?
  дёҖй”®ж”¶и—Ҹ
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/collectionCloseWhite.png)
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/guideRedReward01.png)
  зҹҘйҒ“дәҶ

  [![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/comment.png)

  0](#commentBox)

  иҜ„и®ә
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/share.png)
  еҲҶдә«

  еӨҚеҲ¶й“ҫжҺҘ

  еҲҶдә«еҲ° QQ

  еҲҶдә«еҲ°ж–°жөӘеҫ®еҚҡ

  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/share/icon-wechat.png)жү«дёҖжү«
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/more.png)

  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/report.png)
  дёҫжҠҘ

  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/report.png)
  дёҫжҠҘ

еҸӮдёҺиҜ„и®ә
жӮЁиҝҳжңӘзҷ»еҪ•пјҢиҜ·е…Ҳ
зҷ»еҪ•
еҗҺеҸ‘иЎЁжҲ–жҹҘзңӢиҜ„и®ә

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
еҚҡе®ў
[ITDRдҪ•д»ҘжҲҗдёәIAMзҡ„жңҖдҪіжҗӯжЎЈпјҹ](https://blog.csdn.net/ZAWX_NETSTARSEC/article/details/131768506)

07-17
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
439

[е…·дҪ“иҖҢиЁҖпјҢжӯЈеҰӮ EDR еҜ№з«ҜзӮ№и®ҫеӨҮзҡ„иЎҢдёәиҝӣиЎҢеҲҶжһҗпјҢITDRйҖҡиҝҮAI е’ҢжңәеҷЁеӯҰд№ жҠҖжңҜпјҢеҜ№д»ҘActive Directory е’Ң Oktaдёәд»ЈиЎЁзҡ„иә«д»ҪеҹәзЎҖи®ҫж–ҪдёҠдәӨжҚўзҡ„иә«д»ҪйӘҢиҜҒжөҒйҮҸзҡ„иЎҢдёәиҝӣиЎҢеҲҶжһҗгҖӮеҚідҪҝжӮЁиғҪеӨҹдҪҝз”ЁIAMзӯүе°ҪеҸҜиғҪйҖӮеҪ“ең°и®ҫзҪ®е…¬еҸёзҡ„иә«д»ҪеҹәзЎҖи®ҫж–ҪзҺҜеўғпјҢжҜ«дёҚеӨёеј ең°иҜҙпјҢжғіиҰҒе®Ңе…Ёйҳ»жӯўж”»еҮ»иҖ…йҖҡиҝҮе·§еҰҷзҡ„ж–№жі•е…ҘдҫөжӮЁзҡ„иә«д»ҪеҹәзЎҖи®ҫж–ҪжҳҜдёҚеҸҜиғҪзҡ„гҖӮжӯӨеӨ–пјҢеңЁеӨҡADе’ҢеҹҹзҺҜеўғдёӯе®һзҺ°зҒөжҙ»зҡ„иә«д»Ҫи®ҝй—®з®ЎзҗҶзҡ„Oktaзӯүеҗ„з§ҚIAMи§ЈеҶіж–№жЎҲзҡ„йҮҮз”Ёе’Ңеј•е…ҘпјҢд»ҘеҸҠеҗ‘Azure ADзҡ„иҝҒз§»д»ҘеҸҠSSOеҗ‘SaaSзҡ„иҝҒз§»д№ҹеңЁйҖҗжӯҘеҸ‘еұ•гҖӮ](https://blog.csdn.net/ZAWX_NETSTARSEC/article/details/131768506)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
еҚҡе®ў
[K8Sе®үе…ЁйЈҺйҷ©еҸҠйҳІжҠӨе»әи®®](https://blog.csdn.net/ZAWX_NETSTARSEC/article/details/131766750)

07-17
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
1161

[дҫӢеҰӮпјҢж”»еҮ»иҖ…еҸҜд»ҘеҲӣе»әдёҖдёӘзү№жқғе®№еҷЁпјҢиҜҘе®№еҷЁеҸҜд»Ҙи®ҝй—®е®ҝдё»жңәдёҠзҡ„иө„жәҗпјҢе№¶еңЁиҜҘе®№еҷЁеҶ…жү§иЎҢе‘Ҫд»ӨпјҢд»ҺиҖҢдҪҝе…¶иҺ·еҫ—жӣҙй«ҳзҡ„жқғйҷҗгҖӮдәӢдёӯпјҢйҖҡиҝҮиһҚеҗҲеӣҫи®Ўз®—гҖҒи...