---
title: Decrypting the ‘Calculator’ App(s)
url: https://theincidentalchewtoy.wordpress.com/2021/12/07/decrypting-the-calculator-apps/
source: Over Security - Cybersecurity news aggregator
date: 2024-09-03
fetch_date: 2025-10-06T18:26:44.074489
---

# Decrypting the ‘Calculator’ App(s)

[Skip to content](#content)

[Forensics – One Byte at a Time](https://theincidentalchewtoy.wordpress.com/)

He used to byte, now its just a nibble

Menu

* [Home](/)

[![Forensics – One Byte at a Time](https://theincidentalchewtoy.wordpress.com/wp-content/uploads/2021/11/cropped-binary_banner.png)](https://theincidentalchewtoy.wordpress.com/)

# Decrypting the ‘Calculator’ App(s)

This week I have been looking at another Android application designed to keep files secure. ‘Calculator – hide photos’ has many features, including a vault ‘…*Through the AES encryption algorithm, encrypt the content that you do not want to share with others, and the file format, size without any restrictions, but also support taking pictures and recording videos.’*

One of many applications which presents itself as a functioning calculator but can hide a wealth of data in the background.

‘One of many initially’ referenced the fact that these types of applications are not that uncommon, however, the developers of this application base all of their applications on ‘Sgallery’ (<https://play.google.com/store/apps/details?id=com.hld.anzenbokusu&hl=en&gl=US>). This means that this post initially covering 1 application is applicable to 4 of their applications:

![](https://theincidentalchewtoy.wordpress.com/wp-content/uploads/2021/12/image-16.png?w=1024)

*(This post is based on version 10.0.2 but I have also tested it on the most up-to-date version 10.1.1)*

All data throughout this post was written based on test data from the application with the package name ‘com.hld.anzenbokusufake’. However, it can be applied to all 4 applications.

![](https://theincidentalchewtoy.wordpress.com/wp-content/uploads/2021/12/screenshot_2021-12-02-13-36-32.png?w=512)

Initial Calculator Screen

![](https://theincidentalchewtoy.wordpress.com/wp-content/uploads/2021/12/screenshot_2021-12-02-13-37-03.png?w=512)

Hidden Pattern Screen

Examination into the application identified the following key locations:

|  |
| --- |
| Data |
| /data/data/com.hld.anzenbokusufake |
| Media Files |
| /sdcard/.privacy\_safe |

The Pattern Lock

Within the ‘/data/data/com.hld.anzenbokusufake/shared\_prefs’ folder is the preferences file, ‘**share\_privacy\_safe.xml**‘. This file contains a number of encrypted values:

![](https://theincidentalchewtoy.wordpress.com/wp-content/uploads/2021/12/image.png?w=1024)

Although it’s not obvious, the above screenshot shows the encrypted pattern lock along with the encrypted tag.

Media Files

![](https://theincidentalchewtoy.wordpress.com/wp-content/uploads/2021/12/image-2.png?w=1024)

Media files are stored separately, split into subfolders based on file types. A separate encrypted database file is stored in its own folder. During testing I didn’t see the ‘account’ folder populated. The media files in this location are also encrypted.

Decryption?

When presented with a locked application my first port of call is always to try and get manual access. That way if the application is protecting files using encryption that I can’t work out or replicate in my own code, I can get the application to do the heavy lifting for me and show me the decrypted data. In the case of this app, the pattern and the files can both be covered at once.

Within the applications code there is reference to a hard coded value, along with 2 other functions which appear to be concatenated into one string:

![](https://theincidentalchewtoy.wordpress.com/wp-content/uploads/2021/12/image-4.png?w=590)

Although it may be difficult to see, the above code boils down to being:

**‘Rny4 + ? + ?’** .

After some more digging I found that the code always generates the same value, **Rny48Ni8aPjYCnUI**.

During further examination it was determined that all cryptographic functions, including the encryption of the pattern lock and media files, use this value as part of an AES\_CBC algorithm.

The Pattern Lock – Decrypted

![](https://theincidentalchewtoy.wordpress.com/wp-content/uploads/2021/12/image-6.png?w=490)

CyberChef Decrypting Pattern Lock

Using CyberChef is a nice way to test this out and see it in action. If we take the value, **Rny48Ni8aPjYCnUI**, and convert it to its hexadecimal equivalent we are left with the key required to decrypt the pattern. If we take a look at the decrypted value and convert it from hex, we are left with a string of ‘**03678**‘. As with some of the other Android applications we can determine that this maps out to the android pattern layout which makes our pattern an ‘L’ shape:

![](https://theincidentalchewtoy.wordpress.com/wp-content/uploads/2021/12/image-7.png?w=341)

Pattern Screen Layout

Media Files – Decryption

As it has been mentioned, the media files are also encrypted with the value ‘**Rny48Ni8aPjYCnUI**‘. Interestingly, rather than having a blank IV or one that changes with each file, as is common with AES\_CBC, it simply uses the same value as the encryption key.

![](https://theincidentalchewtoy.wordpress.com/wp-content/uploads/2021/12/image-8.png?w=1024)

CyberChef Decrypting Media File

Each file can be decrypted in this way. There is no correlation between the pattern and the encryption key. Regardless of the pattern lock the Key and IV are the same in each instance of the application.

The Database – Decryption

The database file, ‘**privacy\_safe.db**‘, is also encrypted using the same value. However, rather than converting the value to hex it can be used directly as the passphrase to decrypt it.

Using ‘DB Browser (SQLCipher)’ the database can be imported and decrypted:

![](https://theincidentalchewtoy.wordpress.com/wp-content/uploads/2021/12/image-10.png?w=1024)

DB Browser (SQLCipher) Database Decryption

It is important to make sure that within the encryption settings the SQLCipher is set to 3, otherwise it will not work.

Some Additional Information

Just in case it comes in handy.

It’s possible to change the default pattern to a PIN lock instead. Luckily, its also encrypted with the same key:

![](https://theincidentalchewtoy.wordpress.com/wp-content/uploads/2021/12/image-13.png?w=1024)

Encrypted PIN

Taking this value it simply decrypts directly to the PIN code, without the need for any further interpretation:

![](https://theincidentalchewtoy.wordpress.com/wp-content/uploads/2021/12/image-14.png?w=1024)

PIN Decrypted in CyberChef

![](https://theincidentalchewtoy.wordpress.com/wp-content/uploads/2021/12/screenshot_2021-12-02-13-37-16.png?w=1024)

During the process of setting up the application the user is prompted to setup a recovery answer in case they forget their password (not that it would really be an issue). This is stored in the same preferences file as the encrypted pattern and PIN lock details. This is also encrypted with the same key.

Within the preferences file the recovery question is denoted by the value ‘*A4CDA7B11C92D7943C99DFE00A362E1503D904E2932364D4D66F22966789A926*‘. When decrypted it shows the tag as ‘security\_question’.

![](https://theincidentalchewtoy.wordpress.com/wp-content/uploads/2021/12/image-15.png?w=1024)

Recovery Question Decryption

Conclusion

To summarise, the value **Rny48Ni8aPjYCnUI** or its hexadecimal equivalent **526e7934384e693861506a59436e5549** is used to encrypt / decrypt the pattern / PIN and any media files encrypted using the application.

This mechanism is the same for the other applications shown at the start of the post made by the same developers.

I have made a script which can decrypt the media files and the pattern lock in a streamlined process. I will more than likely be making a github page so I will make it available on there! If you would like it in the meantime then let me know!

Also, please let me know if you have found this helpful, it would be nice to know its not *fur* nothing.

### Share this:

* [Click to share on X (Opens in new window)
  X](https://theincidentalchewtoy.wordpress.com/2021/12/07/decrypting-the-calculator-apps/?share=twitter)
* [Click to share on Facebook (Opens in...