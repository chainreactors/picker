---
title: Protected OOXML Text Documents, (Mon, Sep 2nd)
url: https://isc.sans.edu/diary/rss/31078
source: SANS Internet Storm Center, InfoCON: green
date: 2024-09-03
fetch_date: 2025-10-06T18:28:21.024649
---

# Protected OOXML Text Documents, (Mon, Sep 2nd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31076)
* [next](/diary/31084)

# [Protected OOXML Text Documents](/forums/diary/Protected%2BOOXML%2BText%2BDocuments/31078/)

**Published**: 2024-09-02. **Last Updated**: 2024-09-02 20:28:27 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/Protected%2BOOXML%2BText%2BDocuments/31078/#comments)

Just like "[Protected OOXML Spreadsheets](https://isc.sans.edu/diary/Protected%2BOOXML%2BSpreadsheets/31070)", Word documents can also be protected:

![](https://isc.sans.edu/diaryimages/images/20240902-203716.png)

You have to look into the word/settings.xml file, and search for element w:documentProtection:

![](https://isc.sans.edu/diaryimages/images/20240902-203753.png)

The hash algorithm is the same as for OOXML spreadsheets. However, you will not be able to use hashcat to crack protected Word document hashes, because the password is encoded differently before it is repeatedly hashed.

A legacy algorithm is used to preprocess the password, and I found a Python implementation [here](https://stackoverflow.com/questions/65877620/open-xml-document-protection-implementation-documentprotection-class).

```

# https://stackoverflow.com/questions/65877620/open-xml-document-protection-implementation-documentprotection-class
dHighOrderWordLists = [
    [0xE1, 0xF0],
    [0x1D, 0x0F],
    [0xCC, 0x9C],
    [0x84, 0xC0],
    [0x11, 0x0C],
    [0x0E, 0x10],
    [0xF1, 0xCE],
    [0x31, 0x3E],
    [0x18, 0x72],
    [0xE1, 0x39],
    [0xD4, 0x0F],
    [0x84, 0xF9],
    [0x28, 0x0C],
    [0xA9, 0x6A],
    [0x4E, 0xC3]
]

dEncryptionMatrix = [
    [[0xAE, 0xFC], [0x4D, 0xD9], [0x9B, 0xB2], [0x27, 0x45], [0x4E, 0x8A], [0x9D, 0x14], [0x2A, 0x09]],
    [[0x7B, 0x61], [0xF6, 0xC2], [0xFD, 0xA5], [0xEB, 0x6B], [0xC6, 0xF7], [0x9D, 0xCF], [0x2B, 0xBF]],
    [[0x45, 0x63], [0x8A, 0xC6], [0x05, 0xAD], [0x0B, 0x5A], [0x16, 0xB4], [0x2D, 0x68], [0x5A, 0xD0]],
    [[0x03, 0x75], [0x06, 0xEA], [0x0D, 0xD4], [0x1B, 0xA8], [0x37, 0x50], [0x6E, 0xA0], [0xDD, 0x40]],
    [[0xD8, 0x49], [0xA0, 0xB3], [0x51, 0x47], [0xA2, 0x8E], [0x55, 0x3D], [0xAA, 0x7A], [0x44, 0xD5]],
    [[0x6F, 0x45], [0xDE, 0x8A], [0xAD, 0x35], [0x4A, 0x4B], [0x94, 0x96], [0x39, 0x0D], [0x72, 0x1A]],
    [[0xEB, 0x23], [0xC6, 0x67], [0x9C, 0xEF], [0x29, 0xFF], [0x53, 0xFE], [0xA7, 0xFC], [0x5F, 0xD9]],
    [[0x47, 0xD3], [0x8F, 0xA6], [0x0F, 0x6D], [0x1E, 0xDA], [0x3D, 0xB4], [0x7B, 0x68], [0xF6, 0xD0]],
    [[0xB8, 0x61], [0x60, 0xE3], [0xC1, 0xC6], [0x93, 0xAD], [0x37, 0x7B], [0x6E, 0xF6], [0xDD, 0xEC]],
    [[0x45, 0xA0], [0x8B, 0x40], [0x06, 0xA1], [0x0D, 0x42], [0x1A, 0x84], [0x35, 0x08], [0x6A, 0x10]],
    [[0xAA, 0x51], [0x44, 0x83], [0x89, 0x06], [0x02, 0x2D], [0x04, 0x5A], [0x08, 0xB4], [0x11, 0x68]],
    [[0x76, 0xB4], [0xED, 0x68], [0xCA, 0xF1], [0x85, 0xC3], [0x1B, 0xA7], [0x37, 0x4E], [0x6E, 0x9C]],
    [[0x37, 0x30], [0x6E, 0x60], [0xDC, 0xC0], [0xA9, 0xA1], [0x43, 0x63], [0x86, 0xC6], [0x1D, 0xAD]],
    [[0x33, 0x31], [0x66, 0x62], [0xCC, 0xC4], [0x89, 0xA9], [0x03, 0x73], [0x06, 0xE6], [0x0D, 0xCC]],
    [[0x10, 0x21], [0x20, 0x42], [0x40, 0x84], [0x81, 0x08], [0x12, 0x31], [0x24, 0x62], [0x48, 0xC4]]
]

def WordEncodePassword(password):
  password_bytes = password.encode('utf-8')
  password_bytes = password_bytes[:15]

  password_length = len(password_bytes)

  if password_length > 0:
    high_order_word_list = dHighOrderWordLists[password_length - 1].copy()
  else:
    high_order_word_list = [0x00, 0x00]

  for i in range(password_length):
    password_byte = password_bytes[i]
    matrix_index = i + len(dEncryptionMatrix) - password_length

    for j in range(len(dEncryptionMatrix[0])):
      # Only perform XOR operation using the encryption matrix if the j-th bit is set
      mask = 1 << j
      if (password_byte & mask) == 0:
        continue

      for k in range(len(dEncryptionMatrix[0][0])):
        high_order_word_list[k] = high_order_word_list[k] ^ dEncryptionMatrix[matrix_index][j][k]

  low_order_word = 0x0000

  for i in range(password_length - 1, -1, -1):
    password_byte = password_bytes[i]
    low_order_word = (
      (((low_order_word >> 14) & 0x0001) | ((low_order_word << 1) & 0x7fff))
      ^ password_byte
    )

  low_order_word = (
    (((low_order_word >> 14) & 0x0001) | ((low_order_word << 1) & 0x7fff))
    ^ password_length
    ^ 0xce4b
  )

  low_order_word_list = [(low_order_word & 0xff00) >> 8, low_order_word & 0x00ff]

  key = high_order_word_list + low_order_word_list
  key.reverse()

  # `key_str` is a hex string with uppercase hexadecimal letters, e.g. '7EEDCE64'
  key_str = ''.join(f'{c:X}' for c in key)

  return key_str
```

This password preprocessing code can then be used with the same hashing function as for Excel, like this:

```

def CalculateHash(password, salt):
    passwordBytes = password.encode('utf16')[2:]
    buffer = salt + passwordBytes
    hash = hashlib.sha512(buffer).digest()
    for iter in range(100000):
        buffer = hash + struct.pack('<I', iter)
        hash = hashlib.sha512(buffer).digest()
    return hash

def WordCalculateHash(password, salt):
    return CalculateHash(WordEncodePassword(password), binascii.a2b_base64(salt))

```

Using password "P@ssword" and the salt seen in the screenshot above, we can calculate the hash:

![](https://isc.sans.edu/diaryimages/images/20240902-221509.png)

This calculated hash (BASE64 representation) is the same as the stored hash, thus the password is indeed "P@ssw0rd".

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/Protected%2BOOXML%2BText%2BDocuments/31078/#comments)

* [previous](/diary/31076)
* [next](/diary/31084)

### Comments

[Login here to join the discussion.](/login)

Top of page

×

![modal content]()

[Diary Archives](/diaryarchive.html)

* [![SANS.edu research journal](https://isc.sans.edu/images/researchjournal5.png)](/j/research)
* [Homepage](/index.html)
* [Diaries](/diaryarchive.html)
* [Podcasts](/podcast.html)
* [Jobs](/jobs)
* [Data](/data)
  + [TCP/UDP Port Activity](/data/port.html)
  + [Port Trends](/data/trends.html)
  + [SSH/Telnet Scanning Activity](/data/ssh.html)
  + [Weblogs](/weblogs)
  + [Domains](/data/domains.html)
  + [Threat Feeds Activity](/data/threatfeed.html)
  + [Threat Feeds Map](/data/threatmap.html)
  + [Useful InfoSec Links](/data/links.html)
  + [Presentations & Papers](/data/presentation.html)
  + [Research Papers](/data/researchpapers.html)
  + [API](/api)
* [Tools](/tools/)
  + [DShield Sensor](/howto.html)
  + [DNS Looking Glass](/tools/dnslookup)
  + [Honeypot (RPi/AWS)](/tools/honeypot)
  + [InfoSec Glossary](/tools/glossary)
* [Contact Us](/contact.html)
  + [Contact Us](/contact.html)
  + [About Us](/about.html)
  + [Handlers](/handler_list.html)* [About Us](/about.html)

[Slack Channel](/slack/index.html)

[Mastodon](https://infosec.exchange/%40sans_isc)

[Bluesky](https://bsky.app/profile/sansisc.bsky.social)

[X](https://twitter.com/sans_isc)

![](/adimg.html?id=)

© 2025 SANS™ Internet Storm Center
Developers: We have an [API](/api/) for you!   [![Creative Commons License](/images/cc.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

* [Link To Us](/linkback.html)
* [About Us](/about.html)
* [Handlers](/handler_list.html)
* [Privacy Policy](/privacy.html)