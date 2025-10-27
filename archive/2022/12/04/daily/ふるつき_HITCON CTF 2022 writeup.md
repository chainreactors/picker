---
title: HITCON CTF 2022 writeup
url: https://furutsuki.hatenablog.com/entry/2022/12/03/172249
source: ふるつき
date: 2022-12-04
fetch_date: 2025-10-04T00:28:36.561452
---

# HITCON CTF 2022 writeup

[![сЂхсѓІсЂцсЂЇ](https://cdn.image.st-hatena.com/image/square/22d94d91fe8214e59637e6fa6173edbe2edc56c6/backend=imagemagick;height=128;version=1;width=128/https%3A%2F%2Fcdn.user.blog.st-hatena.com%2Fblog_custom_icon%2F96439929%2F1745809789466802)](https://furutsuki.hatenablog.com/)

[сЂхсѓІсЂцсЂЇ](https://furutsuki.hatenablog.com/)

[УфГУђЁсЂФсЂфсѓІ](https://blog.hatena.ne.jp/Furutsuki/furutsuki.hatenablog.com/subscribe?utm_source=blogs_topright_button&utm_campaign=subscribe_blog&utm_medium=button)

# [сЂхсѓІсЂцсЂЇ](https://furutsuki.hatenablog.com/)

## v(\*'='\*)v УеўС║ІсЂїсѓѕсЂІсЂБсЂЪсѓЅсѓ╣сѓ┐сЃ╝сЂцсЂЉсЂдсЂёсЂБсЂдсЂЈсЂасЂЋсЂё

[2022-12-03](https://furutsuki.hatenablog.com/archive/2022/12/03)

# [HITCON CTF 2022 writeup](https://furutsuki.hatenablog.com/entry/2022/12/03/172249)

сѓѓсЂєТЌЦсЂїухїсЂБсЂдсЂЌсЂЙсЂБсЂЪсЂЉсЂЕсђЂHITCON CTF 2022сЂ«cryptoтЋЈжАїсЂ«writeupсЂДсЂЎсђѓжЏБсЂЌсЂётЋЈжАїсЂ»УДБсЂЉсЂфсЂІсЂБсЂЪсЂЉсЂЕу░АтЇўсЂфтЋЈжАїсѓѓТЦйсЂЌсЂІсЂБсЂЪсЂДсЂЎсђѓсЂѓсѓЅсѓєсѓІсЂесЂЊсѓЇсЂДУеђсЂБсЂдсѓІсЂЉсЂЕсђЂ[maple](http://d.hatena.ne.jp/keyword/maple)сЂеlyxсЂїсѓЂсЂАсѓЃсѓЂсЂАсѓЃС┐АућесЂДсЂЇсѓІсђѓ

* [Baby SSS](#Baby-SSS)
* [Secret](#Secret)
* [Superprime](#Superprime)

## Baby SSS

```
from random import SystemRandom
from Crypto.Cipher import AES
from hashlib import sha256
from secret import flag

rand = SystemRandom()

def polyeval(poly, x):
    return sum([a * x**i for i, a in enumerate(poly)])

DEGREE = 128
SHARES_FOR_YOU = 8  # I am really stingy :)

poly = [rand.getrandbits(64) for _ in range(DEGREE + 1)]
shares = []
for _ in range(SHARES_FOR_YOU):
    x = rand.getrandbits(16)
    y = polyeval(poly, x)
    shares.append((x, y))
print(shares)

secret = polyeval(poly, 0x48763)
key = sha256(str(secret).encode()).digest()[:16]
cipher = AES.new(key, AES.MODE_CTR)
print(cipher.encrypt(flag))
print(cipher.nonce)
```

сЂесѓісЂѓсЂѕсЂџсЂ▓сЂеуЏ«УдІсЂдсѓЈсЂІсѓІсЂЊсЂесѓњТЋ┤уљєсЂЌсЂЙсЂЎсђѓ

* СИђУдІShamir's Secret Sharing
* [тцџжаЁт╝Ј](http://d.hatena.ne.jp/keyword/%C2%BF%EF%BF%BD%E0%BC%B0)сѓњтЙЕтЁЃсЂЌсЂд![ x = 0x48763](https://chart.apis.google.com/chart?cht=tx&chl=%20x%20%3D%200x48763)сѓњС╗БтЁЦсЂЌсЂЪтђцсЂїтЙЌсѓЅсѓїсѓїсЂ░OK
* 128ТгАсЂ«[тцџжаЁт╝Ј](http://d.hatena.ne.jp/keyword/%C2%BF%EF%BF%BD%E0%BC%B0)сЂфсЂ«сЂФт»ЙсЂЌсЂдсђЂ8тђІсЂЌсЂІсѓисѓДсѓбсЂїСИјсЂѕсѓЅсѓїсЂдсЂёсЂфсЂёсЂ«сЂДсђЂжђџтИИсЂ»УДБсЂЉсЂфсЂЋсЂЮсЂє
* ![ \mod p](https://chart.apis.google.com/chart?cht=tx&chl=%20%5Cmod%20p)сЂесЂБсЂдсЂёсЂфсЂёсЂ«сЂїТђфсЂЌсЂё

сЂесѓісЂѓсЂѕсЂџСИђт╝ЈсЂІсѓЅ[тцџжаЁт╝Ј](http://d.hatena.ne.jp/keyword/%C2%BF%EF%BF%BD%E0%BC%B0)тЁежЃесѓњтЙЕтЁЃсЂДсЂЇсЂфсЂёсЂІсѓњУђЃсЂѕсЂЙсЂЎсЂїсђЂ[тцџжаЁт╝Ј](http://d.hatena.ne.jp/keyword/%C2%BF%EF%BF%BD%E0%BC%B0)сЂ«С┐ѓТЋ░сЂ»64bitсЂДсЂѓсѓІсЂ«сЂФт»ЙсЂЌсЂдсђЂтљёсѓисѓДсѓбсЂ«![ x](https://chart.apis.google.com/chart?cht=tx&chl=%20x)сЂ»16bitсЂфсЂ«сЂДсђЂсЂЪсЂесЂѕсЂ░сѓѓсѓЅсЂБсЂдсЂёсѓІ![ y_1](https://chart.apis.google.com/chart?cht=tx&chl=%20y_1)сЂФт»ЙсЂЌсЂд![ y_1 \mod x_1](https://chart.apis.google.com/chart?cht=tx&chl=%20y_1%20%5Cmod%20x_1)сЂесЂІсѓњсЂесЂБсЂдсѓѓсђЂ0ТгАсЂ«С┐ѓТЋ░сЂФжќбсЂЌсЂдсЂ»1/4сЂЌсЂІтЙЕтЁЃсЂДсЂЇсЂфсЂЋсЂЮсЂєсЂДсЂЎсђѓ

сЂЌсЂІсЂЌС╗ітЏъсЂ»8тђІсЂ«сѓисѓДсѓбсЂїСИјсЂѕсѓЅсѓїсЂдсЂёсѓІсЂ«сЂДсђЂсЂЮсѓїсЂъсѓїсЂ«сѓисѓДсѓбсЂД![ y_i \mod x_i](https://chart.apis.google.com/chart?cht=tx&chl=%20y_i%20%5Cmod%20x_i) сѓњтЈќсѓІсЂесђЂС┐ѓТЋ░сЂ«т«џТЋ░жаЁсѓњСИГтЏйтЅ░СйЎсЂДтЙЕтЁЃсЂДсЂЇсЂЮсЂєсЂДсЂЎсђѓт«џТЋ░жаЁ№╝ѕС╗«сЂФ![ k_{i, 0}](https://chart.apis.google.com/chart?cht=tx&chl=%20k_%7Bi%2C%200%7D)сЂесЂЌсЂЙсЂЎ№╝ЅсЂїсѓЈсЂІсѓїсЂ░сђЂ![ y_i = k_0 + \sum_{j=1}^{N} k_0x_i^j](https://chart.apis.google.com/chart?cht=tx&chl=%20y_i%20%3D%20k_0%20%2B%20%5Csum_%7Bj%3D1%7D%5E%7BN%7D%20k_0x_i%5Ej)сЂфсЂ«сЂД ![ (y_i - k_0) / x_i \equiv k_1 \mod x_i](https://chart.apis.google.com/chart?cht=tx&chl=%20%28y_i%20-%20k_0%29%20%2F%20x_i%20%5Cequiv%20k_1%20%5Cmod%20x_i)сЂесЂфсѓісђЂТгАсђЁсЂФС┐ѓТЋ░сЂїТ▒ѓсЂЙсѓісЂЙсЂЎсђѓ

т«ЪУБЁсЂЎсѓІсЂесЂЊсЂє

```
import ast
from hashlib import sha256
from Crypto.Cipher import AES

with open("output.txt") as f:
    shares = ast.literal_eval(f.readline())
    ciphertext = ast.literal_eval(f.readline())
    nonce = ast.literal_eval(f.readline())

def polyeval(poly, x):
    return sum([a * x**i for i, a in enumerate(poly)])

DEGREE = 128
SHARES_FOR_YOU = 8  # I am really stingy :)

coeffs = []
for d in range(DEGREE + 1):
    pairs = []
    values = []
    mods = []
    for i in range(len(shares)):
        x, y = shares[i]
        s = y - polyeval(coeffs, x)
        values.append(s // x**d)
        mods.append(x)

    c = CRT(values, mods)
    coeffs.append(c)

secret = polyeval(coeffs, int(0x48763))
key = sha256(str(secret).encode()).digest()[:16]
cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
print(cipher.decrypt(ciphertext))
```

ptrlibсЂ«CRTсЃАсѓйсЃЃсЃЅсЂ»тљё![ x_i](https://chart.apis.google.com/chart?cht=tx&chl=%20x_i)сЂїтј│т»єсЂФС║њсЂёсЂФу┤асЂДсЂѓсѓІсЂЊсЂесѓњУдЂТ▒ѓсЂЌсЂдсЂЇсЂЪсЂ«сЂДС╗ітЏъсЂ»SagemathсѓњСй┐сЂёсЂЙсЂЌсЂЪсђѓсЂЮсЂ«сЂєсЂАТ▓╗сЂЌсЂЪсЂёсђѓ

## Secret

тЋЈжАїсЂ»сЂЊсЂє

```
import random, os
from Crypto.Util.number import getPrime, bytes_to_long

p = getPrime(1024)
q = getPrime(1024)
n = p * q

flag = open('flag','rb').read()
pad_length = 256 - len(flag)
m = bytes_to_long(os.urandom(pad_length) + flag)
assert(m < n)
es = [random.randint(1, 2**512) for _ in range(64)]
cs = [pow(m, p + e, n) for e in es]
print(es)
print(cs)
```

тћ»СИђсЂ«![ n](https://chart.apis.google.com/chart?cht=tx&chl=%20n)сЂ«сѓѓсЂесЂДсђЂ64тђІсЂ«![ { e_i }](https://chart.apis.google.com/chart?cht=tx&chl=%20%7B%20e_i%20%7D)сѓњућесЂёсЂд![ c_i = m^{e_i + p} \mod n](https://chart.apis.google.com/chart?cht=tx&chl=%20c_i%20%3D%20m%5E%7Be_i%20%2B%20p%7D%20%5Cmod%20n)сЂесЂёсЂєТџЌтЈитїќсѓњсЂЌсЂдсЂёсѓІ[RSA](http://d.hatena.ne.jp/keyword/RSA)сЂДсЂЎсђѓСИђУдІCommon Moudulus AttackтЁИтъІсЂ«сѓѕсЂєсЂфтйбсѓњсЂЌсЂдсЂёсЂЙсЂЎсЂїсђЂ![ n](https://chart.apis.google.com/chart?cht=tx&chl=%20n)сЂїСИЇТўјсЂфсЂ«сЂДсђЂсЂЙсЂџ![ n](https://chart.apis.google.com/chart?cht=tx&chl=%20n)сѓњТ▒ѓсѓЂсѓІт┐ЁУдЂсЂїсЂѓсѓісЂЮсЂєсЂДсЂЎсђѓ

сЂЊсѓїсЂФсЂцсЂёсЂдсЂ»ТюђУ┐ЉN1CTF 2022сЂДтЄ║жАїсЂЋсѓїсЂЪBrand new checkinсЂесЂёсЂєтЋЈжАїсЂДС╝╝сЂЪсѓѕсЂєсЂфУдЂТ▒ѓсЂїсЂѓсЂБсЂЪсЂЊсЂесѓњТђЮсЂётЄ║сЂЌсђЂтЄ║жАїУђЁсЂДсЂѓсѓІ[maple](http://d.hatena.ne.jp/keyword/maple)сЂЋсѓЊсЂ«writeupсѓњУдІсЂФУАїсЂБсЂЪсЂесЂЊсѓЇсђЂсЂЋсѓЅсЂФжЂјтј╗сЂФ[maple](http://d.hatena.ne.jp/keyword/maple)сЂЋсѓЊсЂїтЄ║жАїсЂЌсЂЪтЋЈжАїсЂ«УДБУфгсЂїсЂѓсѓісЂЙсЂЌсЂЪсђѓ

[github.com](https://github.com/maple3142/My-CTF-Challenges/tree/master/ImaginaryCTF/Round%2026/no_modulus)

сЂЊсѓїсЂФсѓѕсѓїсЂ░сђЂС╗ЦСИІсЂ«сѓѕсЂєсЂфуљєт▒ѕсЂД![ c](https://chart.apis.google.com/chart?cht=tx&chl=%20c)сЂе![ e](https://chart.apis.google.com/chart?cht=tx&chl=%20e)сЂ«УцЄТЋ░сЂ«ухёсЂІсѓЅ![ n](https://chart.apis.google.com/chart?cht=tx&chl=%20n)сЂїТ▒ѓсЂЙсѓісЂЙсЂЎсђѓ

УцЄТЋ░сЂ«ТЋ░сЂ«ухё![ {a_i}](https://chart.apis.google.com/chart?cht=tx&chl=%20%7Ba_i%7D)сѓњС╗«т«џсЂЌсЂдсђЂ![ a_0e_0 + a_1e_1 + \dots = 0 \mod \phi(n)](https://chart.apis.google.com/chart?cht=tx&chl=%20a_0e_0%20%2B%20a_1e_1%20%2B%20%5Cdots%20%3D%200%20%5Cmod%20%5Cphi%28n%29)сЂесЂфсѓІсЂесЂЇсђЂ![ \prod m^{a_ie_i} \equiv m^{1} \equiv 1 \mod n](https://chart.apis.google.com/chart?cht=tx&chl=%20%5Cprod%20m%5E%7Ba_ie_i%7D%20%5Cequiv%20m%5E%7B1%7D%20%5Cequiv%201%20%5Cmod%20n)сЂфсЂ«сЂДсђЂ![ \prod c_i^{a_i} -1 = kn](https://chart.apis.google.com/chart?cht=tx&chl=%20%5Cprod%20c_i%5E%7Ba_i%7D%20-1%20%3D%20kn)сЂесЂфсѓісђЂсЂЊсЂ«сѓѕсЂєсЂф![ {a_i}](https://chart.apis.google.com/chart?cht=tx&chl=%20%7Ba_i%7D)сЂетљїТДўсЂ«![ {b_i}](https://chart.apis.google.com/chart?cht=tx&chl=%20%7Bb_i%7D)сѓњућеТёЈсЂЌсЂдсђЂ![ \gcd(\prod c_i^{a_i} - 1, \prod c_i^{b_i} - 1) = n](https://chart.apis.google.com/chart?cht=tx&chl=%20%5Cgcd%28%5Cprod%20c_i%5E%7Ba_i%7D%20-%201%2C%20%5Cprod%20c_i%5E%7Bb_i%7D%20-%201%29%20%3D%20n)сЂесЂфсѓІсЂЊсЂесЂїТюЪтЙЁсЂДсЂЇсЂЙсЂЎ[\*1](#f-1fd3529c "т«ЪжџЏсЂФсЂ»LLLсЂДТЋ┤ТЋ░УДБсЂДсЂ»сЂфсЂЈТюЅуљєТЋ░УДБсЂїтЙЌсѓЅсѓїсѓІсЂ«сЂДтѕєТ»ЇсѓњТЅЋсЂБсЂЪтйбсЂ«gcdсѓњсЂесѓІсЂЊсЂесЂФсЂфсѓІсЂесЂісѓѓсЂёсЂЙсЂЎсђѓУЕ│сЂЌсЂЈсЂ»mapleсЂЋсѓЊсЂ«УДБУфгсЂФсЂѓсѓісЂЙсЂЎ")сђѓ

сЂЋсЂдсђЂ![ {e_i}](https://chart.api...