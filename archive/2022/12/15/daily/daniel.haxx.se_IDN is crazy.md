---
title: IDN is crazy
url: https://daniel.haxx.se/blog/2022/12/14/idn-is-crazy/
source: daniel.haxx.se
date: 2022-12-15
fetch_date: 2025-10-04T01:32:38.901677
---

# IDN is crazy

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2022/12/Screenshot-2022-12-13-at-23-17-45-Unicode-Utilities-Confusables.png)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# IDN is crazy

[December 14, 2022](https://daniel.haxx.se/blog/2022/12/14/idn-is-crazy/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [16 Comments](https://daniel.haxx.se/blog/2022/12/14/idn-is-crazy/#comments)

IDN, [International Domain Names](https://en.wikipedia.org/wiki/Internationalized_domain_name), is the concept that lets us register and use *international* characters in domain names, and by international we of course mean characters outside of the ASCII range.

Recently I have fought some battles against IDN and IDN decoding so I felt this urge to write a lot of words about it to help me in my healing process and maybe mend my scars a little. I am not sure it worked but at least I feel a little better now.

(*If WordPress had a more sensible Unicode handling, this post would have nicer looking examples. I can enter Unicode fine, but if I save the post as a draft and come back to it later, most of the Unicodes are replaced by question marks! Because of this, the examples below are not all using the exact Unicode symbols the text speaks of.*)

## Punycode

IDN works by having apps convert the Unicode name into the ASCII based *[punycode](https://en.wikipedia.org/wiki/Punycode)* version under the hood, and then use that with DNS etc. The puny code version of “räksmörgås.se” becomes “`xn--rksmrgs-5wao1o.se`“. A pretty clever solution really.

## The good side

Using this method, we can use URLs like https://räksmörgås.se or even ones written entirely in Arabic, Chinese or Cyrillic etc in compliant applications like browsers and curl. Even the TLD can be “international”. The whole Unicode range is at our disposal and this is certainly a powerful tool and allows a lot of non-Latin based languages to actually be used for domain names.

Gone are the days when everything needed to be converted to Latin.

## There are many ugly sides

Already from the start of the IDN adventure, people realized that Unicode contains a lot of symbols that are identical or almost identical to other symbols, so you can make up the perfect fake sites that provide no or very little visual distinction from the one you try to look like.

### Homographs

I remember early demonstrations using paypal.com vs paypal.com, where the second name was actually using a completely different letter somewhere. Perhaps for example the ‘l’ used the *Cyrillic Capital Letter Iota* ([U+A646](https://www.compart.com/en/unicode/U%2BA646)) – which in most fonts is next to indistinguishable from the lower case ASCII letter L. This is commonly referred to as an [IDN Homograph attack](https://en.wikipedia.org/wiki/IDN_homograph_attack). They look identical, but are different.

This concept of replacing one or more characters by identical glyphs is mitigated in part in browsers, which switch to showing the punycode version in the URL bar instead of the Unicode version – when they think it is mandated. Domain names are not allowed to mix scripts for different languages, and if they do the IDNs names are displayed using their punycode.

This of course does not prevent someone from promoting a command line curl use that uses it, and maybe encourage use of it:

```
curl https://example.com/api/
```

If you would copy and paste such an example, you would find that curl cannot resolve `xn--exampe-7r6v.com`! Or if you use the same symbol in the curl domain name:

```
$ curl https://curl.se
curl: (6) Could not resolve host: xn--cur-ju2l.se
```

### Heterograph?

Similar to the previous confusion, there’s another version of the homograph attack and this is one that stayed under the radar for me for a long time. I suppose we can call it a Heterograph attack, as it makes names look different when they are in fact the same.

The IDN system is also “helpfully” replacing some similarly looking glyphs with their ASCII counterparts. I use quotes around helpfully, because I truly believe that this generally causes more harm and pain in users’ lives than it actually does good.

A user can provide a name using an IDN version of one or more characters within the name, and that name will then get translated into a regular non-IDN name and then get used normally from then on. I realize this may sound complicated, but it really is not.

Let me show you a somewhat crazy example (shown as an image to prevent WordPress from interfering). You want to use a curl command line to get the contents of the URL `https://curl.se` but since you are wild and crazy, you spice up things and replace every character in the domain name with a Unicode replacement:

![](https://daniel.haxx.se/blog/wp-content/uploads/2022/12/Screenshot-2022-12-13-at-17-54-06-Untitled-document-Google-Docs.png)

If you would copy and paste this command line into your terminal, it works. Everyone can see that this domain name looks crazy, but it does not matter. It still works. It also works in browsers. A browser will however immediately show the translated version in the URL bar.

This method can be used for avoiding filters and has several times been used to find flaws in curl’s HSTS handling. Surely other tools can be tricked and fooled using variations of this as well.

This works because the characters used in the domain name are automatically *converted* to their ASCII counterparts by the IDN function. And since there is no IDN characters left after the conversion, it does not end up punycoded but instead it is plain old ASCII again. Those Unicode symbols simply translate into “curl.se”.

The example above also replaces the period before “se” with the Halfwidth Ideographic Full Stop ([U+FF61](https://www.compart.com/en/unicode/U%2BFF61)).

Replacing the dot this way works as well. “Helpful”.

#### A large set to pick from

If we look at the letter ‘c’ alone, it has a huge number of variations in the Unicode set that all translate into ASCII ‘c’ by the IDN conversion. I found at least these *fifteen* variations that all convert to c:

* Fullwidth Latin Small Letter C ([U+FF43](https://www.compart.com/en/unicode/U%2BFF43))
* Modifier Letter Small C ([U+1D9C](https://www.compart.com/en/unicode/U%2B1D9C))
* Small Roman Numeral One Hundred ([U+217D](https://www.compart.com/en/unicode/U%2B217D))
* Mathematical Bold Small C ([U+1D41C](https://www.compart.com/en/unicode/U%2B1D41C))
* Mathematical Italic Small C ([U+1D450](https://www.compart.com/en/unicode/U%2B1D450))
* Mathematical Bold Italic Small C ([U+1D484](https://www.compart.com/en/unicode/U%2B1D484))
* Mathematical Script Small C ([U+1D4B8](https://www.compart.com/en/unicode/U%2B1D4B8))
* Mathematical Fraktur Small C ([U+1D520](https://www.compart.com/en/unicode/U%2B1D520))
* Mathematical Double-Struck Small C ([U+1D554](https://www.compart.com/en/unicode/U%2B1D554))
* Mathematical Bold Fraktur Small C ([U+1D588](https://www.compart.com/en/unicode/U%2B1D588))
* Mathematical Sans-Serif Small C ([U+1D5BC](https://www.compart.com/en/unicode/U%2B1D5BC))
* Mathematical Sans-Serif Bold Small C ([U+1D5F0](https://www.compart.com/en/unicode/U%2B1D5F0))
* Mathematical Sans-Serif Italic Small C ([U+1D624](https://www.compart.com/en/unicode/U%2B1D624))
* Mathematical Sans-Serif Bold Italic Small C ([U+1D658](https://www.compart.com/en/unicode/U%2B1D658))
* Mathematical Monospace Small C ([U+1D68C](https://www.compart.com/en/unicode/U%2B1D68C))

The Unicode consortium even has this collection of [“confusables”](https://util....