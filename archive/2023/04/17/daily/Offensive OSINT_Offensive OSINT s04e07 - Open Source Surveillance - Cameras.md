---
title: Offensive OSINT s04e07 - Open Source Surveillance - Cameras
url: https://www.offensiveosint.io/offensive-osint-s04e07-open-source-surveillance-cameras/
source: Offensive OSINT
date: 2023-04-17
fetch_date: 2025-10-04T11:32:08.367391
---

# Offensive OSINT s04e07 - Open Source Surveillance - Cameras

[![Offensive OSINT](https://www.offensiveosint.io/content/images/2020/07/OffensiveOsint-logo-RGB-2.png)](https://www.offensiveosint.io)

* [Home](/)
* [About me](/about-me/)
* [Open Source Surveillance](https://www.os-surveillance.io)
* [kamerka.io](https://www.kamerka.io)
* [Sign up](/signup/)
* [Account](/account/)
* [Sign in](/signin/)
* [Patreon](https://patreon.com/offensiveosint)

##### Search Here

×

## Offensive OSINT s04e07 - Open Source Surveillance - Cameras

* Wojciech

  [![Wojciech](/content/images/size/w100/2023/02/OffensiveOsint-logo-RGB-2.png)](/author/wojciech/)

[Wojciech](/author/wojciech/)
16 Apr 2023 • 12 min read

![Offensive OSINT s04e07 - Open Source Surveillance - Cameras](/content/images/2023/04/paulo-silva-a7Gtlgpeq6w-unsplash.jpg)

In today's episode we have new GUI, vulnerable cameras and how ChatGPT can support Open Source Surveillance.

This is second part of the Open Source Surveillance research that focuses on publicly accessible and Internet exposed cameras.

You can read first part about social media below

[Offensive OSINT s04e06 - Open Source Surveillance - Social media

OSINT researcher doing cyber security art brut

![](https://www.offensiveosint.io/content/images/size/w256h256/2020/07/oo.png)Offensive OSINTWojciech

![](https://www.offensiveosint.io/content/images/2023/02/raphael-lopes-HVibVDQVwbM-unsplash.jpg)](https://www.offensiveosint.io/offensive-osint-s04e06-open-source-surveillance-social-media/)

# Introduction

I've never heard about the case where footage from publicly accessible or internet exposed camera was used in criminal investigation to track bad actor or to identify him by non law enforcement officer, nonetheless it provides additional information and other point of view. In criminal investigations though, it's almost first thing what agents look for in crime scene. Usually, these cameras are privately owned and used for surveillance, so it's impossible to get live or historical footage remotely. However, some devices are directly connected to the Internet and I will talk about how to search for them as well.

Some are completely open i.e. without authentication, which Shodan provides screenshot from, and you can access them remotely and control the device in most cases.

For other ones, it's possible to use default credentials or exploit some old unpatched vulnerability. **This updates provides new types of Internet exposed cameras that are potentially vulnerable.**

# New GUI

First things first, let me present you new interface which was introduced in last update. Design was made by [OSINTTEAM](https://www.osintteam.com/?ref=offensiveosint.io) and I prepared front-end part. Some backend changes had to be performed as well, but at the end it improved not only general look but performance as well.

Moreover, from now you can run multiple modules at once. Just choose ones you are interested in and click Search. Remember that some of them work on radius and some on coordinates range, so zoom in or zoom out to get more accurate results.

![](https://www.offensiveosint.io/content/images/2023/03/port3.png)

From other small improvements, light/dark theme switch button is placed in left bottom corner. **Near Search button, checkbox is located and responsible for checking only new findings. It means, if this checkbox is ticked, it will give you results but if you search for the second time in same place, it won't return anything because there are no new findings**. I implemented it to be up to date with the results and monitor situation on hourly or daily basis gathering only new Tweets or VKontakte photos. Now, let's back to the main topic of the article - publicly accessible cameras in OSINT.

# Public cameras

Usually, publicly accessible cameras are located in most important part of the city like in the centre, beach or crowded places, so it will be OSINT useful only for specific purposes. There are plenty of websites that provide consolidated information about such cameras for whole world.

Most of the large cities has it's own surveillance system and sometimes it's publicly available, so we can grab live stream from cameras.

Currently, there are four types of cameras implemented in Open Source Surveillance.

## Surveillance

This is the type of camera you see most often on the street. It covers entry gates, private properties and similar. They are privately owned and getting remote access is not possible, unless you hack into the network via other techniques and control the camera.

Source for this module is based on overpass API for Open Street Map.

[overpass turbo

A web based data mining tool for OpenStreetMap which runs any kind of Overpass API query and shows the results on an interactive map.

![](https://overpass-turbo.eu/turbo-439087fae60c1d26e3f58f9d3966e20a-favicon-32x32.png)overpass turbo

![](data:image/png;base64...)](https://overpass-turbo.eu/?ref=offensiveosint.io)

I'm not a master of Overpass queries but I didn't have to. The only query I use is quite simple and looks as follow

```
[out:json];( node["man_made"="surveillance"](49.926516143671876,19.777793884277344,50.18605233471432,20.107383728027344););out center meta;>;out skel qt;
```

Basically it means, show me all objects with parameter "man\_made" set to surveillance. You can try it by yourself on overpass-turbe.de.

Returned position is very accurate because it comes from community, everyone can add camera to the Open Street Maps and that's how I grab the data.

This is example of returned data

```
{
    "camera_id":"1303423624",
    "added":"2020-10-26T17:12:35Z",
    "user":"Hydrel",
    "latitude":"48.8497866",
    "longitude":"2.6534938",
    "timestamp":"2020-10-26T17:12:35Z",
    "mount":"building",
    "surveillance":"public",
    "zone":"area",
    "height":"3",
    "source":"survey",
}
```

Beside obvious info, like coordinates and timestamp we have additional data like where the device is mounted, on what height and source of discovery, in some cases it is link where information was found.

## Weather

Weather cameras as the name suggest, are located in locations that allows spectators to see weather in a clear way. Think about hills, skyscrapers or even airports. Open Source Surveillance uses Windy as a main source for this type of cameras.

[https://windy.com](https://www.windy.com/?ref=offensiveosint.io)

Windy has very easy to use API and request looks like this. Number 55 after latitude and longitude means radius in kilometres.

```
https://api.windy.com/api/webcams/v2/list/nearby={lat},{lon},55?show=webcams:location,image,player&key= + WINDY_KEY
```

It returns link to the image stream, title and coordinates.

```
{
    "title":"Hambleton: Thirsk Market Place, Yorkshire",
    "image":"https://images-webcams.windy.com/31/1332072131/current/preview/1332072131.jpg",
    "photo_id":"1332072131",
    "latitude":"54.232829",
    "longitude":"-1.342328",
    "timestamp":"",
}
```

## Traffic

Another source of cameras for OSS is Open Traffic Cam and below is the link to map where you can find around 32 thousands of traffic cameras

[OpenTrafficCamMap](http://otc.armchairresearch.org/map?ref=offensiveosint.io)

This is implemented into the platform via large JSON file with all the necessary data and you can find it here.

[https://raw.githubusercontent.com/AidanWelch/OpenTrafficCamMap/master/cameras/USA.json](https://raw.githubusercontent.com/AidanWelch/OpenTrafficCamMap/master/cameras/USA.json?ref=offensiveosint.io)

Basically, when you choose Traffic cams and click search it iterates over the file and checks if position of the device is located inside your chosen coordinates range.

```
for place in f_json[state][county]:
    lat = place['location']['latitude']
    lon = place['location']['longitude']

    if float(geo2) < float(lat) < float(geo1) and float(geo4) < float(lon) < float(geo3):
    ...Put marker on map...
```

and here is the example response that needs to be parsed and show to the end use...