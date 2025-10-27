---
title: Profiling the Gaza Hackers Team
url: https://ddanchev.blogspot.com/2024/09/profiling-gaza-hackers-team.html
source: Dancho Danchev's Blog - Mind Streams of Information Security Knowledge
date: 2024-09-22
fetch_date: 2025-10-06T18:25:28.082843
---

# Profiling the Gaza Hackers Team

# [Dancho Danchev's Blog - Mind Streams of Information Security Knowledge](https://ddanchev.blogspot.com/)

Independent Contractor. Bitcoin: 15Zvie1j8CjSR52doVSZSjctCDSx3pDjKZ Email: dancho.danchev@hush.com OMEMO: ddanchev@conversations.im | OTR: danchodanchev@xmpp.jp | TOX ID: 53B409440A6DC34F1BA458869A0462D92C15B467AF6319D481CA353690C88667833A0EE82969

## Saturday, September 21, 2024

### Profiling the Gaza Hackers Team

In the following post I'll profile the Gaza Hackers Team.

**Sample photos:**

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1FXVABf_8ItSohhiJNgbqlk8D8WCkchcpQa6rEMrGX6Mp8AeXXXsKjWCsN3hHoreL3O9lDxlZLpvgS-NFYqKp-AYcNMKvjgCPFTT3Ew0Qs9mIeIVaXG79P_hppogRe6XuOjCZE1jJlcoiwFg6mIeK-jDGd3xZFdlYhDGQYv2Os17Fk-aPwh6r/s320/0.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1FXVABf_8ItSohhiJNgbqlk8D8WCkchcpQa6rEMrGX6Mp8AeXXXsKjWCsN3hHoreL3O9lDxlZLpvgS-NFYqKp-AYcNMKvjgCPFTT3Ew0Qs9mIeIVaXG79P_hppogRe6XuOjCZE1jJlcoiwFg6mIeK-jDGd3xZFdlYhDGQYv2Os17Fk-aPwh6r/s978/0.jpg)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh1xhYNAeVh3YD7Q3j6pNHf-sJMV34SNipDwE_g1gPjaOLhta9AOUizunoW84CZeEGeLPEpFUG_QIEtFpoCmLs9GiErxGqzH-U7LDKel0VOt3nLXmGHSzYCobdmor1qU6f2zOUqw5OzD0akihOI5-Ld9l0KR5dWFCPAMhq4fYubsWUR50TqSSSF/s320/1.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh1xhYNAeVh3YD7Q3j6pNHf-sJMV34SNipDwE_g1gPjaOLhta9AOUizunoW84CZeEGeLPEpFUG_QIEtFpoCmLs9GiErxGqzH-U7LDKel0VOt3nLXmGHSzYCobdmor1qU6f2zOUqw5OzD0akihOI5-Ld9l0KR5dWFCPAMhq4fYubsWUR50TqSSSF/s594/1.jpg)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjOOtXBkCMcCdDpfvpB89vcJibanj33eHiLoXfRBDoKIEgctpIZhXDXXpL88cVBc4FFBwYC387VXmqCkrRqgBY1Q5-2GgcvntTdYw6yOhUAfv5Aa0ieKnojf_EPjhvpwzH-fqAGGdttQ50E6rBvOtdp19ercY2PQuIIR4rJpJLeKFl0rF4lFQWn/s320/2.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjOOtXBkCMcCdDpfvpB89vcJibanj33eHiLoXfRBDoKIEgctpIZhXDXXpL88cVBc4FFBwYC387VXmqCkrRqgBY1Q5-2GgcvntTdYw6yOhUAfv5Aa0ieKnojf_EPjhvpwzH-fqAGGdttQ50E6rBvOtdp19ercY2PQuIIR4rJpJLeKFl0rF4lFQWn/s486/2.jpg)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEibNuUAAppKCEmsdQyPc8mBS3iBZenh_YFlySugfEI0SRiHa8981wyQ23vpBvRuGyPXJODcHfjLNBKVSUPh5n32THdN9HEOVK4izqLg2TRX6mslc3_3qbbcsn-9EwgFM-fTTXJtJ4I3PUlhR_0MgsUmQJnvwKlMcmT4iQ1GzccIvzF3tWSI7SeW/s320/3.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEibNuUAAppKCEmsdQyPc8mBS3iBZenh_YFlySugfEI0SRiHa8981wyQ23vpBvRuGyPXJODcHfjLNBKVSUPh5n32THdN9HEOVK4izqLg2TRX6mslc3_3qbbcsn-9EwgFM-fTTXJtJ4I3PUlhR_0MgsUmQJnvwKlMcmT4iQ1GzccIvzF3tWSI7SeW/s733/3.jpg)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiC77CICx-eBoc-H8ybLPd-bqjPM_vkh8ublLMershiRNGNX0Ft4gN3sPZSnw-vbrFkLxIMEvfiZQQ3mlJqnEbrnFHqf6bNxlO0tCZ-LNU3zLci8dTNrXTcXDqvnj_HJYGje6Wc1ipUgjvTYxt1qp2zEr6qfqPQ0NWm6dLNEuKC4CAYccPL9_rt/s320/4.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiC77CICx-eBoc-H8ybLPd-bqjPM_vkh8ublLMershiRNGNX0Ft4gN3sPZSnw-vbrFkLxIMEvfiZQQ3mlJqnEbrnFHqf6bNxlO0tCZ-LNU3zLci8dTNrXTcXDqvnj_HJYGje6Wc1ipUgjvTYxt1qp2zEr6qfqPQ0NWm6dLNEuKC4CAYccPL9_rt/s386/4.jpg)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhXKc03Sn5liO6DR3cw4Su5UJHm-r7yuHW7uN-oncbhDDk3wKSSE-oZffhHmY-tSIZ83BavujkXlXn8_Okgc4NxAkZutZ_S6Hp2ZRX1Vit9VdOPgiNxOzhRHDxT4Hz0DIFnPKskS7XMUK_yn8TZS71TsoZvZoxuhzNF8XtpmdbnbNnwPuftOzx7/s320/5.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhXKc03Sn5liO6DR3cw4Su5UJHm-r7yuHW7uN-oncbhDDk3wKSSE-oZffhHmY-tSIZ83BavujkXlXn8_Okgc4NxAkZutZ_S6Hp2ZRX1Vit9VdOPgiNxOzhRHDxT4Hz0DIFnPKskS7XMUK_yn8TZS71TsoZvZoxuhzNF8XtpmdbnbNnwPuftOzx7/s500/5.jpg)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhiHCg7ZrPZ7j8eKkPg6L7Bp1ZBaxInv5fKtqBB-kb5s4mbUTwp64MjzG8E49a4FV1zy-IaSzzeDmInZTs1oS53HqgBn0Xncx3nRphXn744EnES44Y1pqUC1qz5khMFPg8gQZzuU_EDYK5c1uNxvI6oiozbdQilTJUqIWp4YPuCzmAgJHmGjBYc/s320/6.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhiHCg7ZrPZ7j8eKkPg6L7Bp1ZBaxInv5fKtqBB-kb5s4mbUTwp64MjzG8E49a4FV1zy-IaSzzeDmInZTs1oS53HqgBn0Xncx3nRphXn744EnES44Y1pqUC1qz5khMFPg8gQZzuU_EDYK5c1uNxvI6oiozbdQilTJUqIWp4YPuCzmAgJHmGjBYc/s800/6.jpg)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh6AcIuPSA1UarJYREuoFqpzF_0Md8YxShkFCHLc259Tn87WfDSgBVY7w41K1p00gFt9T4U0ROS2xN8PDF2G-G7p7c3i0ga63g5CwfMdO_CIa0KU9CPyj4BtmuiSV7eCIF-TBZF_k9nj1X4eQ4ccZOriuRatzmqGoshm9AhccKK6HwWxOICiNtJ/s320/7.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh6AcIuPSA1UarJYREuoFqpzF_0Md8YxShkFCHLc259Tn87WfDSgBVY7w41K1p00gFt9T4U0ROS2xN8PDF2G-G7p7c3i0ga63g5CwfMdO_CIa0KU9CPyj4BtmuiSV7eCIF-TBZF_k9nj1X4eQ4ccZOriuRatzmqGoshm9AhccKK6HwWxOICiNtJ/s709/7.jpg)

**Primary group's domains:**

hxxp://gaza-hacker.com
hxxp://hacker.ps
hxxp://gaza-hacker.net
hxxp://gaza-hack.org
hxxp://gaza-hack.info
hxxp://xhackerx.com
hxxp://gaza-hack.com
hxxp://gaza-hackers.com

**Primary group's email address accounts:**

moayy2ad@hotmail.com
c-e@hotmail.com
le0n005061@gmail.com

**Related domain names registered using the same email address accounts:**

hxxp://frontat.com
hxxp://nswaa.com
hxxp://elsahefa.com
hxxp://naji-albatta.com
hxxp://dr-sohila-edu.com
hxxp://samozico.com
hxxp://shahidn.com
hxxp://spider-rss.com
hxxp://sv4media.com
hxxp://m3n4.com
hxxp://shamaly.com
hxxp://g2mz.com
hxxp://4as7ab.com
hxxp://cfpalestine.com
hxxp://q8yh.com
hxxp://wac-yamama.org
hxxp://rawshna.org
hxxp://saawa.com
hxxp://4rbshare.com
hxxp://lajlek.com
hxxp://l7ens.com
hxxp://koraw.com
hxxp://kwgram.com
hxxp://gwafe.com
hxxp://q8ey.com
hxxp://x23x.com
hxxp://kuwaitpwr.com
hxxp://kuwaitfn.com
hxxp://abovlan.com
hxxp://q8pinq.com
hxxp://eli4s.com
hxxp://7koma.com
hxxp://juod.net
hxxp://topteamdns.com
hxxp://nhla7-uae.com
hxxp://3agil.com
hxxp://wtnfjr.com
hxxp://norislam.net
hxxp://universalimporting.com
hxxp://gaza-shell.com
hxxp://remas3.com
hxxp://3dshared.com
hxxp://3dm3mare.com
hxxp://al-ra3ed.com
hxxp://bissan-m.com
hxxp://bnimashhor.com
hxxp://pure4ever.net
hxxp://shaatha.com
hxxp://ispal.net
hxxp://paldream.net
hxxp://islhack.net
hxxp://adsyour.net
hxxp://bnimashhor.net
hxxp://mr-matrix.net
hxxp://amtaar-a.org
hxxp://darhuda.org
hxxp://downiphone.com
hxxp://6ayf.org
hxxp://jadoptical.com
hxxp://yomo-az.com
hxxp://bfbcps.com
hxxp://glaroo7y.com
hxxp://amal-ci.com
hxxp://q8gz.com
hxxp://dubai-g.com
hxxp://3mrrycam.com
hxxp://psdmate.com
hxxp://njomksa.com
hxxp://g-ghram.com
hxxp://coctael.com
hxxp://alhajere.info
hxxp://glaoman.com
hxxp://ascdascascasc.com
hxxp://m7b4.com
hxxp://shrooq.org
hxxp://3uz.com
hxxp://alhajere.net
hxxp://wt2n.com
hxxp://sfena.com
hxxp://artsformedia.com
hxxp://r-alfrsan.com
hxxp://arabgmaes.com
hxxp://studiomustapha.com
hxxp://adamttc.com
hxxp://helolhost.com
hxxp://soblslam.com
hxxp://forexufx.com
hxxp://dsfbdfbsdfgbdsf.com
hxxp://frsan-aslm.com
hxxp://g2z4.com
hxxp://ewfdssdcsdxc.com
hxxp://sam-sport.net
hxxp://fr4wa.com
hxxp://sama-a.net
hxxp://hayatk.net
hxxp://gallerycenter.net
hxxp://frfish.net
hxxp://q8ey.net
hxxp://cfpalestine.net
hxxp://m3n4.net
hxxp://wt2n.net
hxxp://gaza-sporting-club.net
hxxp://mo7et.net
hxxp://alnkhala.com
hxxp://alibel.info
hxxp://q8gz.net
hxxp://dlo3.net
hxxp://butt3rfly.net
hxxp://butt3rfly.org
hxxp://pnsport.net
hxxp://sawasport.net
hxxp://echotic.net
hxxp://healthclubxl.com
hxxp://dancingqueensdk.com
hxxp://dancingqueensuk.com
hxxp://nadinerandle.com
hxxp://hackers.tools
hxxp://pinkybarbie.com
hxxp://florencemodel.com
hxxp://hevreman.co.il
hxxp://radiousnice.com
hxxp://gaza-hacker.net
hxxp://hacker.ps
hxxp://gaza-hack.info
hxxp://gaza-hack.com
hxxp://gaza-hack.org
hxxp://gaza-hackers.com
hxxp://xhackerx.com
hxxp://gaza-hacker.com
hxxp://metasploit-unleashed.com
hxxp://divuae.com
hxxp://xensds.com
hxxp://e107arabic.com
hxxp://h-asiaa.com
hxxp://nsamat.com
hxxp://for-pal.com
hxxp://althbat.com
hxxp://islamdahalan.com
hxxp://37ob.com
hxxp://hamedwayel.com
hxxp://iraq-mawal.com
hxxp://waleedalshami.com
hxxp://fr27.com
hxxp://faloja.us
hxxp://stylatna.us
hxxp://llo9.com
hxxp://g-del3.com
hxxp://ye7g.com
hxxp://ks4-des.com
hxxp://5tmat.com
hxxp:...