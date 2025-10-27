---
title: A software controlled power supply for $25
url: https://grymoire.wordpress.com/2024/11/11/a-software-controlled-power-supply-for-25/
source: The Grymoire
date: 2024-11-12
fetch_date: 2025-10-06T19:21:39.230250
---

# A software controlled power supply for $25

[The Grymoire](https://grymoire.wordpress.com/ "The Grymoire")

Notebook for wizards

[![](https://grymoire.wordpress.com/wp-content/themes/pub/twentyten/images/headers/concave.jpg?m=1610459589i)](https://grymoire.wordpress.com/ "The Grymoire")

[Skip to content](#content "Skip to content")

* [Home](https://grymoire.wordpress.com/)
* [About](https://grymoire.wordpress.com/about-2/)

[← Compiling GhidraNinja’s Pico Debug’N’Dump](https://grymoire.wordpress.com/2022/01/24/compiling-ghidraninjas-pico-debugndump/)

## [A software controlled power supply for $25](https://grymoire.wordpress.com/2024/11/11/a-software-controlled-power-supply-for-25/)

Posted on [November 11, 2024](https://grymoire.wordpress.com/2024/11/11/a-software-controlled-power-supply-for-25/ "6:31 pm") by [grymoire](https://grymoire.wordpress.com/author/grymoire/ "View all posts by grymoire")

## The RK6006-BT power supply

I had a DPS3003 power supply, and I’ve always found the device difficult to use. There are only 4 buttons and a knob, and the manual was difficult to parse. I noticed a similar power supply that have both USB and Bluetooth. the RK6006-BT! There were several listings on [Aliexpress](https://www.aliexpress.us/w/wholesale-rk6006%252525252dbt.html) and the price ranged from $27 to $37. I used a new user account and purchased one for $25. The interface looked very similar to the DPS3003. Okay!

[![](https://grymoire.wordpress.com/wp-content/uploads/2024/11/rk6006.jpg?w=299)](https://grymoire.wordpress.com/wp-content/uploads/2024/11/rk6006.jpg)

I received it quickly, and was surprised there was no documentation with it.

## Where is the software?

I expected a download link for the software. I checked the vendor page and nothing was listed. Hmm. I looked at other vendors and found a reference to a link on a [Google drive](https://drive.google.com/drive/folders/1V9CMtTBnc4Ww-sNHrabN8522YPYQcrNI?usp=sharing). I finally downloaded the software, (which required unpacking an encrypted RAR, and installing a driver) and when I tried running it on the PC, it said “No support this product model”

![](https://grymoire.wordpress.com/wp-content/uploads/2024/11/rk6006pc.png)

I tried installing the Android software from the Google play Store and it says my phone isn’t compatible. A copy of the manual says only Android OS 5.0 through 12.0 was supported, and I have 14.0, with the latest being 15.0. So I searched for new firmware.

## Finding alternative software

I found a link on the [EEVBlog](https://www.eevblog.com/forum/testgear/ruideng-riden-rd6006-dc-power-supply/new/) that mentioned the UniSoft software for the RD6006. Truthfully I was confused about the product because the AliExpress described it as the RD/RK6006 and sometimes they list different names for different models. So I thought it was worth a try. But first, I wanted to make sure I could restore the device to the proper firmware. I found the [vendor firmware](http://www.ruidengkeji.com/rdupdate/firmware/RK60066/) and noticed the latest was v1.09, which matched what my device had (w/bootloader v1.04). I also noticed they described it as model 60066.

I then tried an open source [firmware uploader](https://github.com/tjko/riden-flashtool). At first it didn’t work because it wasn’t a recognized model. So I changed the line

```
supported_models = [60062, 60065, 60121, 60125, 60181, 60241]
```

to

```
supported_models = [60062, 60065, 60066, 60121, 60125, 60181, 60241]
```

And it worked!

![](https://grymoire.wordpress.com/wp-content/uploads/2024/11/pxl_20241110_152226673.jpg)

I then tried to upload the UniSoft firmware. No such luck. No software for me! It’s a different device. The front panel was probably the biggest difference to the software. But I had hoped.

However I kept searching. I found [Voidstarsec](https://voidstarsec.com/hw-hacking-lab/assets/blog/posts/2022/01/17/intro-to-embedded-part-1.html#power-supply-riden-r6006)‘s blog on power supply and read about the [rd6006 python library.](https://github.com/Baldanos/rd6006)

I needed to set up a virtual python environment first

cd ; python -m venv env –system-sitre-packages

activate ~/env/bin/activate

I next needed to install a modbus library as I found out

pip install minimalmodbus

Now get the rd6006 library. I store my git copies in ~/Git

cd ~/Git
gh repo clone Baldanos/rd6006
cd rd6006
python setup.py install –user

I then tested the python code in a file called test.py

from rd6006 import RD6006
r=RD6006(‘/dev/ttyUSB0’)
r.enable=0
r.voltage=3.3
r.enable=1
r.status

I called “python test.py” and the output was

RD6006 or other detected
== Device
Model : 6006.6
SN : 00012522
Firmware: 1.09
Input : 12.17V
Temp : 27°C
TempProb: -73°C
== Output
Voltage : 2.83V
Current : 0.002A
Energy : 0.0Ah
Power : 0.0W
== Settings
Voltage : 3.3V
Current : 6.1A
== Protection
Voltage : 62.0V
Current : 6.2A
== Battery
Capacity: 0.0Ah
Energy : 0.0Wh
== Memories
M0: 5.0V, 6.100A, OVP:62.0V, OCP:6.200A
M1: 5.0V, 6.100A, OVP:62.0V, OCP:6.200A
M2: 5.0V, 6.100A, OVP:62.0V, OCP:6.200A
M3: 5.0V, 6.100A, OVP:62.0V, OCP:6.200A
M4: 5.0V, 6.100A, OVP:62.0V, OCP:6.200A
M5: 5.0V, 6.100A, OVP:62.0V, OCP:6.200A
M6: 5.0V, 6.100A, OVP:62.0V, OCP:6.200A
M7: 5.0V, 6.100A, OVP:62.0V, OCP:6.200A
M8: 5.0V, 6.100A, OVP:62.0V, OCP:6.200A
M9: 5.0V, 6.100A, OVP:62.0V, OCP:6.200A

I don’t have WiFi or BlueTooth, but I was able to get the functionality of a $80 power supply working with a $25 device. And I can control it on my Linux box. Success!

### Share this:

* [Click to share on Facebook (Opens in new window)
  Facebook](https://grymoire.wordpress.com/2024/11/11/a-software-controlled-power-supply-for-25/?share=facebook)
* [Click to share on X (Opens in new window)
  X](https://grymoire.wordpress.com/2024/11/11/a-software-controlled-power-supply-for-25/?share=x)

Like Loading...

### *Related*

This entry was posted in [Uncategorized](https://grymoire.wordpress.com/category/uncategorized/) and tagged [firmware](https://grymoire.wordpress.com/tag/firmware/), [hardware](https://grymoire.wordpress.com/tag/hardware/), [news](https://grymoire.wordpress.com/tag/news/), [python](https://grymoire.wordpress.com/tag/python/), [Technology](https://grymoire.wordpress.com/tag/technology/). Bookmark the [permalink](https://grymoire.wordpress.com/2024/11/11/a-software-controlled-power-supply-for-25/ "Permalink to A software controlled power supply for $25").

[← Compiling GhidraNinja’s Pico Debug’N’Dump](https://grymoire.wordpress.com/2022/01/24/compiling-ghidraninjas-pico-debugndump/)

### Leave a comment [Cancel reply](/2024/11/11/a-software-controlled-power-supply-for-25/#respond)

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

* Search for:
* ### Archives

  + [November 2024](https://grymoire.wordpress.com/2024/11/)
  + [January 2022](https://grymoire.wordpress.com/2022/01/)
  + [December 2020](https://grymoire.wordpress.com/2020/12/)
  + [December 2019](https://grymoire.wordpress.com/2019/12/)
  + [June 2019](https://grymoire.wordpress.com/2019/06/)
  + [January 2018](https://grymoire.wordpress.com/2018/01/)
  + [March 2017](https://grymoire.wordpress.com/2017/03/)
  + [January 2017](https://grymoire.wordpress.com/2017/01/)
  + [February 2016](https://grymoire.wordpress.com/2016/02/)
  + [March 2015](https://grymoire.wordpress.com/2015/03/)
  + [January 2015](https://grymoire.wordpress.com/2015/01/)
  + [December 2014](https://grymoire.wordpress.com/2014/12/)
  + [November 2014](https://grymoire.wordpress.com/2014/11/)
  + [September 2014](https://grymoire.wordpress.com/2014/09/)
  + [July 2014](https://grymoire.wordpress.com/2014/07/)
  + [April 2014](https://grymoire.wordpress.com/2014/04/)
  + [March 2014](https://grymoire.wordpress.com/2014/03/)
  + [February 2014](https://grymoire.wordpress.com/2014/02/)
  + [January 2014](https://grymoire.wordpress.com/2014/01/)
  + [December 2013](https://grymoire.wordpress.com/2013/12/)
  + [No...