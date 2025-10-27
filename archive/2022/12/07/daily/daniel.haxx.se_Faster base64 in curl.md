---
title: Faster base64 in curl
url: https://daniel.haxx.se/blog/2022/12/06/faster-base64-in-curl/
source: daniel.haxx.se
date: 2022-12-07
fetch_date: 2025-10-04T00:41:02.134098
---

# Faster base64 in curl

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2022/12/cheetah.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# Faster base64 in curl

[December 6, 2022](https://daniel.haxx.se/blog/2022/12/06/faster-base64-in-curl/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [8 Comments](https://daniel.haxx.se/blog/2022/12/06/faster-base64-in-curl/#comments)

This adventure started with [an issue](https://github.com/curl/curl/issues/10024) where a user pointed out that the libcurl function for base64 encoding actually would allocate a few bytes too many at times.

That turned out to be true and [we fixed it](https://github.com/curl/curl/pull/10025) fairly quickly.

As I glanced at that base64 encoder function that was still loaded and showing in my editor window, it struck me that it really was not written in an optimal way.

## Base64 encoding

This “encoding” converts 8 bit data into a 6 bit data, where each 6 bit combination has a dedicated ASCII character. It uses these 64 different characters: `ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/`.

Three 8-bit bytes make up 24 bit of data, which can be represented by four 6-bit symbols. Like this: the example byte sequence 0x12 , 0x34 and 0x56 creates the 24 bit value **0x123456**. Shown in binary it looks like: **000100100 0110100 01010110**

That 24 bit number is split into 6-bit chunks: **000100**, **100011**, **010001** and **010110**. Written in decimal, they are 4, 35, 17 and 22. Pick the corresponding symbols from those indexes in the base64 table shown above and they make the base64 encoded sequence: **EjRW**. And so on.

That’s base 64 encoding.

## A realization

The base64 encoder function source code I looked at, was introduced in curl in the late 1990s and existed in [the first commit](https://github.com/curl/curl/commit/ae1912cb0d494) we have saved. It has remained mostly intact since. Over twenty two years old.

This is how the code used to look. Fairly readable, but with a lot of conditions and perhaps most importantly, with calls to `msnprintf()` to output data. [msnprintf()](https://github.com/curl/curl/blob/fc02a78081f095670344411d480d4021ecdfe0ae/lib/mprintf.c#L1051) is our internal snprintf implementation,

## The old base64 encoder

```
while(insize > 0) {
  for(i = inputparts = 0; i < 3; i++) {
    if(insize > 0 {
     inputparts++;
     ibuf[i] = (unsigned char) *indata;
     indata++;
     insize--;
   }
   else
     ibuf[i] = 0;
  }

  obuf[0] = ((ibuf[0] & 0xFC) >> 2);
  obuf[1] = (((ibuf[0] & 0x03) << 4) |
            ((ibuf[1] & 0xF0) >> 4));
  obuf[2] = (((ibuf[1] & 0x0F) << 2) |
            ((ibuf[2] & 0xC0) >> 6));
  obuf[3] = (ibuf[2] & 0x3F);

  switch(inputparts) {
  case 1: /* only one byte read */
    i = msnprintf(output, 5, "%c%c%s%s",
                  table64[obuf[0]],
                  table64[obuf[1]],
                  padstr,
                  padstr);
    break;

  case 2: /* two bytes read */
    i = msnprintf(output, 5, "%c%c%c%s",
                  table64[obuf[0]],
                  table64[obuf[1]],
                  table64[obuf[2]],
                  padstr);
    break;

  default:
    i = msnprintf(output, 5, "%c%c%c%c",
                  table64[obuf[0]],
                  table64[obuf[1]],
                  table64[obuf[2]],
                  table64[obuf[3]]);
    break;
  }
  output += i;
```

}

(The `padstr` variable in there is for handling the mode where it does not output any final `=` padding characters. )

## Improving

I started out by writing a [test program](https://gist.github.com/bagder/baee5725e09a5977ef5b0471e2b3334f). I created a huge string, and made the test program base64-encode a part of that string. Starting from one byte string, then increasing the length one by one to iterating over all sizes until the final size which happened to be 106128 bytes. Maybe not the most realistic test in the world, but at least it does a lot of base64 encoding. The base64 encode algorithm is also content agnostic so it doesn’t matter what the exact content is, the size of it is the main thing.

My first casual attempt that only replaced the snprintf() calls with direct assigns into the target buffer first made me doubt my numbers or test program. My test program ran 14 times faster.

Motivated by the enormous performance gain seen with that minor change, I continued. I removed the use of the `obuf` array and it occurred to me I should deal with the encoding in two phases; one main one for all complete three-byte triplets and then do the padding final chunk separately – as then we can avoid conditions in the main loop.

The final result that I ended up merging showed **an almost 29 times improvement**. With the old code the test program took six minutes to complete, the new one finished in twelve seconds.

## The new encoder

```
  while(insize >= 3) {
    *output++ = table64[ in[0] >> 2 ];
    *output++ = table64[ ((in[0] & 0x03) << 4) |
                         (in[1] >> 4) ];
    *output++ = table64[ ((in[1] & 0x0F) << 2) |
                         ((in[2] & 0xC0) >> 6) ];
    *output++ = table64[ in[2] & 0x3F ];
    insize -= 3;
    in += 3;
  }
  if(insize) {
    /* this is only one or two bytes now */
    *output++ = table64[ in[0] >> 2 ];
    if(insize == 1) {
      *output++ = table64[(in[0] & 0x03) << 4];
      if(*padstr) {
        *output++ = *padstr;
        *output++ = *padstr;
      }
    }
    else {
      /* insize == 2 */
      *output++ = table64[((in[0] & 0x03) << 4) |
                          ((in[1] & 0xF0) >> 4)];
      *output++ = table64[(in[1] & 0x0F) << 2];
      if(*padstr)
        *output++ = *padstr;
    }
  }
```

I think the new version still is highly readable, and it actually is significantly smaller in size than the previous version!

## Base64 decoding

Energized by that fascinating improvement I managed to do to the encoder function, I turned my eyes to the base64 decoder function. This function is slightly newer in curl than the encoder, but still traces back to 2001 and it too was never improved much after its initial merge.

I started again by writing [another test program](https://gist.github.com/bagder/959b087c933465317407b20bc0fb0b53). This one creates a 2948 bytes base64 encoded string which the application then iterates over and decodes pieces of. From one byte up to the full size, and then it loops so that it repeats that procedure a thousand times.

When decoding base64, the core of the code needs to find out what binary number each particular input octet represents. ‘A’ is zero, ‘B’ is one etc. Then it needs to take four such consecutive (effectively 6 bit) letters at a time and output 3 eight bit bytes. Over and over. In a final round it might need to deal with =-padding to make it an even 4 bytes size.

## The old decoder

This is how the old `decodeQuantum` function looked like. It decodes a 4-letter sequence into three output bytes.

```
  for(i = 0, s = src; i < 4; i++, s++) {
    if(*s == '=') {
      x <<= 6;
      padding++;
    }
    else {
      const char *p = strchr(base64, *s);
      if(p)
        x = (x << 6) + curlx_uztoul(p - base64);
      else
        return 0;
    }
  }

  if(padding < 1)
    dest[2] = curlx_ultouc(x & 0xFFUL);

  x >>= 8;
  if(padding < 2)
    dest[1] = curlx_ultouc(x & 0xFFUL);

  x >>= 8;
  dest[0] = curlx_ultouc(x & 0xFFUL);
```

## The new decoder

What immediately sticks out in the old code is the use of `strchr()` to find the letters’ offset in the base64 table as a means to figure out its byte value. The larger the value...