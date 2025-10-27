---
title: 智能桌面改造
url: https://blog.upx8.com/3138
source: 黑海洋 - WIKI
date: 2022-12-07
fetch_date: 2025-10-04T00:43:05.124229
---

# 智能桌面改造

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 智能桌面改造

发布时间:
2022-12-06

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
11095

## 前言

一直对改造桌面有想法，于是采购了一片8266正式开始改造。
1.为显示器加了一圈氛围灯，改写代码可实现流光溢彩的效果。
2.电脑实现远程启动，小爱同学启动（局域网网卡唤醒）。

## 代码

//无线局域网音乐律动 远程启动电脑
#define BLINKER\_WIFI
#define BLINKER\_MIOT\_LIGHT
#define BLINKER\_MIOT\_OUTLET
//#define BLINKER\_ESP\_SMARTCONFIG
#define BLINKER\_WITHOUT\_SSL
#include <ESP8266WiFi.h>
#include <WiFiUdp.h>
#include <FastLED.h>
#include <Blinker.h>
char auth[] = "";
char ssid[] = "";
char pswd[] = "";

WiFiUDP Udp;
bool oState = false;

unsigned int localUdpPort = 6001;
char packetBuffer[256];
unsigned long triger\_time;
BlinkerButton Button1("ButtonKey1");
BlinkerButton Button2("ButtonKey2");
BlinkerButton Button3("ButtonKey3");
BlinkerButton Button4("ButtonKey4");
BlinkerButton Button5("ButtonKey5");
BlinkerSlider Slider1("SliderKey");
BlinkerSlider Slider2("SliderKey2");
BlinkerRGB RGBWS2812("RGBKey");
int openState = 2;
unsigned int nowState = 2;
int freq\_flash = 15;
uint8\_t colorR = 250, colorG = 0, colorB = 0, colorW = 250;
bool wsState;
uint8\_t wsMode = BLINKER\_CMD\_MIOT\_DAY;
int brt\_set = 100;

#include <Adafruit\_NeoPixel.h>
#define PIN 5
#define NUMPIXELS 60
int pre\_si = 0;
int drop\_dot = NUMPIXELS - 1;
unsigned long drop\_time;
unsigned long lift\_time;
unsigned long up\_time;
unsigned long down\_time;
Adafruit\_NeoPixel pixels = Adafruit\_NeoPixel(NUMPIXELS, PIN, NEO\_GRB + NEO\_KHZ800);
CRGBArray<NUMPIXELS> leds;
void pixelShow()
{

 pixels.setBrightness(colorW);

 for (int i = 0; i < NUMPIXELS; i++)
 {
 pixels.setPixelColor(i, colorR, colorG, colorB);

 }
 pixels.show();

}
void slider1\_callback(int32\_t value)
{

 Blinker.vibrate();
 BLINKER\_LOG("get slider value: ", value);
 freq\_flash = value;
}
void slider2\_callback(int32\_t value)
{

 Blinker.vibrate();
 BLINKER\_LOG("get slider value: ", value);

}
void ws2812\_callback(uint8\_t r\_value, uint8\_t g\_value, uint8\_t b\_value, uint8\_t bright\_value)
{
 button\_clear();
 BLINKER\_LOG("R value: ", r\_value);
 BLINKER\_LOG("G value: ", g\_value);
 BLINKER\_LOG("B value: ", b\_value);
 BLINKER\_LOG("Rrightness value: ", bright\_value);
 colorR = r\_value;
 colorG = g\_value;
 colorB = b\_value;
 colorW = bright\_value;
 openState = 6;
 //Text1.print("灯光模式：" , "单颜色");
}
void button\_clear()
{
 Button1.print("off");
 Button2.print("off");
 Button3.print("off");
 Button4.print("off");
 Button5.print("off");
 Button1.color("#008000");
 Button2.color("#008000");
 Button3.color("#008000");
 Button4.color("#008000");
 Button5.color("#008000");
}

void button1\_callback(const String & state)
{
 BLINKER\_LOG("get button state: ", state);
 if (state == BLINKER\_CMD\_ON) {
 BLINKER\_LOG("日光模式开启");
 button\_clear();
 Button1.color("#DC143C");
 Button1.print("on");
 openState = 1;
 }
 else if (state == BLINKER\_CMD\_OFF) {
 BLINKER\_LOG("日光模式关闭!");
 button\_clear();
 Button1.color("#008000");
 openState = 0;
 }
}
void button2\_callback(const String & state)
{
 BLINKER\_LOG("get button state: ", state);
 if (state == BLINKER\_CMD\_ON) {
 BLINKER\_LOG("月光模式开启");
 button\_clear();
 Button2.print("on");
 Button2.color("#DC143C");
 openState = 2;
 }
 else if (state == BLINKER\_CMD\_OFF) {
 BLINKER\_LOG("月光模式关闭!");
 button\_clear();
 openState = 0;
 }
}
void button3\_callback(const String & state)
{

 BLINKER\_LOG("get button state: ", state);

 if (state == BLINKER\_CMD\_ON) {
 BLINKER\_LOG("温馨模式开启");
 button\_clear();
 Button3.print("on");
 Button3.color("#DC143C");
 openState = 3;
 brt\_set = colorW;
 }
 else if (state == BLINKER\_CMD\_OFF) {
 BLINKER\_LOG("温馨模式关闭!");
 button\_clear();
 openState = 0;
 }

}
void button4\_callback(const String & state)
{

 BLINKER\_LOG("get button state: ", state);

 if (state == BLINKER\_CMD\_ON) {
 BLINKER\_LOG("电脑模式开启");

 BlinkerMIOT.print();
 pcawaking();

 openState = 4;
 }
 else if (state == BLINKER\_CMD\_OFF) {
 BLINKER\_LOG("电脑模式关闭!");

 BlinkerMIOT.print();
 openState = 0;
 }

}
void button5\_callback(const String & state)
{

 BLINKER\_LOG("get button state: ", state);

 if (state == BLINKER\_CMD\_ON) {
 BLINKER\_LOG("电视模式开启");

 button\_clear();
 Button5.print("on");
 Button5.color("#DC143C");
 openState = 5;
 }
 else if (state == BLINKER\_CMD\_OFF) {
 BLINKER\_LOG("电视模式关闭!");

 button\_clear();
 openState = 0;

 }

}

void dataRead(const String & data)
{
 BLINKER\_LOG("Blinker readString: ", data);

 Blinker.vibrate();

 uint32\_t BlinkerTime = millis();

 Blinker.print("millis", BlinkerTime);
}
uint32\_t getColor()
{

 uint32\_t color = colorR << 16 | colorG << 8 | colorB;

 return color;
}
//小爱同学
void miotPowerState(const String & state)
{
 BLINKER\_LOG("need set power state: ", state);

 if (state == BLINKER\_CMD\_ON) {

 BlinkerMIOT.powerState("on");
 BlinkerMIOT.print();
 wsState = true;
 if (colorW == 0) colorW = 255;
 openState = 6;
 }
 else if (state == BLINKER\_CMD\_OFF) {
 BlinkerMIOT.powerState("off");
 BlinkerMIOT.print();
 wsState = false;
 openState = 0;
 }
}

void miotColor(int32\_t color)
{
 BLINKER\_LOG("need set color: ", color);

 colorR = color >> 16 & 0xFF;
 colorG = color >> 8 & 0xFF;
 colorB = color & 0xFF;

 BLINKER\_LOG("colorR: ", colorR, ", colorG: ", colorG, ", colorB: ", colorB);
 openState = 6;
 BlinkerMIOT.color(color);
 BlinkerMIOT.print();
}

void miotMode(uint8\_t mode)
{
 BLINKER\_LOG("need set mode: ", mode);

 if (mode == BLINKER\_CMD\_MIOT\_DAY) {
 button\_clear();
 Button1.print("on");
 Button1.color("#DC143C");
 openState = 1;

 }
 else if (mode == BLINKER\_CMD\_MIOT\_NIGHT) {
 button\_clear();
 Button2.print("on");
 Button2.color("#DC143C");
 openState = 2;
 }
 else if (mode == BLINKER\_CMD\_MIOT\_COLOR) {
 button\_clear();
 openState = 6;

 }
 else if (mode == BLINKER\_CMD\_MIOT\_WARMTH) {
 button\_clear();
 Button3.print("on");
 Button3.color("#DC143C");
 openState = 3;
 }
 else if (mode == BLINKER\_CMD\_MIOT\_TV) {
 button\_clear();
 Button5.print("on");
 Button5.color("#DC143C");
 openState = 5;
 }
 else if (mode == BLINKER\_CMD\_MIOT\_READING) {
 }
 else if (mode == BLINKER\_CMD\_MIOT\_COMPUTER) {
 pcawaking();
 button\_clear();
 Button1.print("on");
 Button1.color("#DC143C");
 openState = 4;
 }

 wsMode = mode;

 BlinkerMIOT.mode(mode);
 BlinkerMIOT.print();
}

void miotBright(const String & bright)
{
 BLINKER\_LOG("need set brightness: ", bright);

 colorW = bright.toInt();

 BLINKER\_LOG("now set brightness: ", colorW);

 pixelShow();

 BlinkerMIOT.brightness(colorW);
 BlinkerMIOT.print();
 openState = 6;
}

void miotColoTemp(int32\_t colorTemp)
{
 BLINKER\_LOG("need set colorTemperature: ", colorTemp);

 BlinkerMIOT.colorTemp(colorTemp);
 BlinkerMIOT.print();
}

void miotQuery(int32\_t queryCode)
{
 BLINKER\_LOG("MIOT Query codes: ", queryCode);

 switch (queryCode)
 {
 case BLINKER\_CMD\_QUERY\_ALL\_NUMBER :
 BLINKER\_LOG("MIOT Query All");
 BlinkerMIOT.powerState(wsState ? "on" : "off");
 BlinkerMIOT.color(0);
 BlinkerMIOT.mode(0);
 BlinkerMIOT.colorTemp(1000);
 BlinkerMIOT.brightness(1);
 BlinkerMIOT.print();
 break;
 case BLINKER\_CMD\_QUERY\_POWERSTATE\_NUMBER :
 BLINKER\_LOG("MIOT Query Power State");
 BlinkerMIOT.powerState(wsState ? "on" : "off");
 BlinkerMIOT.print();
 break;
 case BLINKER\_CMD\_QUERY\_COLOR\_NUMBER :
 BLINKER\_LOG("MIOT Query Color");
 BlinkerMIOT.color(0);
 BlinkerMIOT.print();
 break;
 case BLINKER\_CMD\_QUERY\_MODE\_NUMBER :
 BLINKER\_LOG("MIOT Query Mode");
 BlinkerMIOT.mode(0);
 BlinkerMIOT.print();
 break;
 case BLINKER\_CMD\_QUERY\_COLORTEMP\_NUMBER :
 BLINKER\_LOG("MIOT Query ColorTemperature");
 BlinkerMIOT.colorTemp(1000);
 BlinkerMIOT.print();
 break;
 case BLINKER\_CMD\_QUERY\_BRIGHTNESS\_NUMBER :
 BLINKER\_LOG("MIOT Query Brightness");
 BlinkerMIOT.brightness(1);
 BlinkerMIOT.print();
 break;
 default :
 BlinkerMIOT.powerState(wsState ? "on" : "off");
 BlinkerMIOT.color(0);
 BlinkerMIOT.mode(0);
 BlinkerMIOT.colorTemp(1000);
 BlinkerMIOT.brightness(1);
 BlinkerMIOT.print();
 break;
 }
}
// 开机
void pcawaking()
{
 int i=0;
 c...