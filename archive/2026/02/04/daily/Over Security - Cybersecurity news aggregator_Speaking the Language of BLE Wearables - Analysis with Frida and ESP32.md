---
title: Speaking the Language of BLE Wearables - Analysis with Frida and ESP32
url: https://mandomat.github.io/2026-02-04-speaking-the-language-of-wearables/
source: Over Security - Cybersecurity news aggregator
date: 2026-02-04
fetch_date: 2026-02-05T04:09:56.316009
---

# Speaking the Language of BLE Wearables - Analysis with Frida and ESP32

[Home](https://mandomat.github.io/)

* [About Me](/aboutme)
* Search

[![Navigation bar avatar](/assets/img/avatar-icon.png)](https://mandomat.github.io/)

✕

# Speaking the Language of BLE Wearables - Analysis with Frida and ESP32

## A simple and low-cost way to approach Bluetooth Low Energy security

Posted on February 4, 2026

In this article I want to introduce a simple way to approach BLE hacking, covering a bit of theory and giving a practical, low-cost example so you can start having fun with this protocol right away.

For this experiment we will need:

* A smart band like this one: <https://shorturl.at/qu1KS>
  I have some called M4, some M5, some M7, and it seems there is not much difference between them. The app they use is FitPro and the experiment should work on all associated devices.
* A rooted Android phone
* An ESP32 of any type (in my case I use an ESP32 WROOM like this one: [https://shorturl.at/FOpaM](https://www.aliexpress.com/p/tesla-landing/index.html?scenario=c_ppc_item_bridge&productId=1005006336502350&_immersiveMode=true&withMainCard=true&src=google&aff_platform=true&isdl=y&src=google&albch=shopping&acnt=742-864-1166&isdl=y&slnk=&plac=&mtctp=&albbt=Google_7_shopping&aff_platform=google&aff_short_key=UneMJZVf&gclsrc=aw.ds&&albagn=888888&&ds_e_adid=&ds_e_matchtype=&ds_e_device=c&ds_e_network=x&ds_e_product_group_id=&ds_e_product_id=it1005006336502350&ds_e_product_merchant_id=5087526639&ds_e_product_country=IT&ds_e_product_language=it&ds_e_product_channel=online&ds_e_product_store_id=&ds_url_v=2&albcp=22646554006&albag=&isSmbAutoCall=false&needSmbHouyi=false&gad_source=1&gad_campaignid=22636780545&gbraid=0AAAAA99aYpfGDzz70YukCNiQ1irppw6c3&gclid=Cj0KCQiA-YvMBhDtARIsAHZuUzInptJzF-zH0vpZT2ro3vVRgPQ8mtoZyb1Dfagw3kyCEHd_9yDu1cAaAuKBEALw_wcB) )

# Introduction

Even if this blog post does not aim to fully cover the whole BLE world (<https://www.bluetooth.com/specifications/specs/>), it is important to understand at least the basics, so what we do next actually makes sense.

First of all, let’s clarify that Bluetooth Low Energy is different from Bluetooth Classic:
BLE is designed for **low power communication and small data packets**, usually between devices like sensors, wearables and smartphones.
Bluetooth Classic is designed for **continuous, high-throughput connections**, like audio streaming or file transfers.

In BLE, communication is based on the concept of **services** and **characteristics**, which are exposed by the peripheral device and queried by the client. This creates a modular structure where you can read, write or subscribe to notifications for specific data.

What defines services and characteristics is the **GATT (Generic Attribute Profile)**. This is the protocol that standardizes how data is structured and exchanged between devices.

Alongside GATT, we also have **GAP (Generic Access Profile)**, which defines how devices connect and what role they take.
So in short: GAP is used to establish the connection, and GATT is used to exchange data.

For our experiment, GATT is the most interesting part, because it includes the ability to **read and write data**. And it would be very interesting if we could write data to the smartwatch and make it do “unexpected” things.

![Understanding the Bluetooth GATT Hierarchy](/assets/img/2026-02-04/hierarchy.jpg)

To do this, we will analyze how data is exchanged between the app and the smart band. First we will try to replicate it using `bluetoothctl` on Linux, and then we will implement the same logic on an ESP32 to create a sort of automatic attacker.

# Let’s get into it

The key point is to analyze the app. The steps I describe could also be done using other tools.
If the communication was not encrypted, we could have used a BLE sniffer like an nRF52840 dongle with sniffing firmware.
We could also have used Android’s built-in Bluetooth HCI snoop log to capture and analyze packets.

Today, however, we will use **Frida**, which is a very powerful tool to intercept the execution of apps, on Android and other platforms.

## Initial Frida setup

Download the FitPro app (from the Play Store or other sources).

In my case, I downloaded it online and installed it using `adb install` because I didn’t want to log in with a Google account on my rooted phone. Normally, though, it’s better to use the Play Store to avoid fake or modified apps.

First, we install `frida-tools`.
At this stage, you might run into errors because it is very important that **frida, frida-tools and frida-server all have the exact same version**, and that this version is **compatible with your CPU architecture and Android version**.

In my case, I used a OnePlus 8. With version 17.6.2 (the latest at the time), I had many issues, so I downgraded to 15.2.2, which I had already used in the past and knew worked well.

```
python3 -m venv venv
source venv/bin/activate
pip install frida==15.2.2 frida-tools

frida --version
15.2.2
```

Now we install `frida-server` on Android.
You will need `adb` and developer options enabled on the phone (and root access, as mentioned before).

First, let’s check the CPU architecture:

```
adb shell getprop ro.product.cpu.abi
arm64-v8a
```

Then go to the releases page:
<https://github.com/frida/frida/releases>

And download the correct version for your device, in this case:
`frida-server-15.2.2-android-arm64.xz`

To decompress it:

```
unxz frida-server-15.2.2-android-arm64.xz
```

Then push and start the server:

```
adb root
adb push frida-server-15.2.2-android-arm64 /data/local/tmp/frida-server
adb shell "chmod 755 /data/local/tmp/frida-server"
adb shell "/data/local/tmp/frida-server &"
```

On your PC, we can do a simple smoke test:

```
frida-ps -U
```

If you see a list of processes, everything is working.

## Writing the Frida hook

Now we have Frida working and the FitPro app ready to be analyzed.
The goal here is to **intercept in real time the data that the app sends to the smart band over BLE**, so we can understand *what* is written, *where* it is written, and *in what format*.

In other words, we want to “sit in the middle” between the app and Android’s Bluetooth stack, and watch the Java calls that write to GATT characteristics.

On Android, when an app wants to send data to a BLE device, the flow usually looks like this:

1. The app prepares a byte array with the command.
2. It sets this array on a `BluetoothGattCharacteristic` using `setValue(...)`.
3. It asks the system to send it using `BluetoothGatt.writeCharacteristic(...)`.

By hooking **both** of these points, we get:

* The raw value when it is prepared in memory.
* The exact moment when it is actually sent over the air, with the target characteristic UUID.

This gives us a full view of the proprietary protocol used by the smart band.

Below is the full hook code, with comments:

```
// Check if the Java runtime is available (Frida is attached to a Java-based app)
if (Java.available) {

    // Execute this function inside the Java VM context
    Java.perform(function () {

        // Get references to Android Bluetooth classes
        var BluetoothGatt = Java.use("android.bluetooth.BluetoothGatt");
        var BluetoothGattCharacteristic = Java.use("android.bluetooth.BluetoothGattCharacteristic");

        // Helper function: converts a byte array into a readable hex string
        // Example: [10, 255, 3] -> "0a ff 03"
        function bytesToHex(bytes) {
            var result = [];
            for (var i = 0; i < bytes.length; i++) {
                // Convert signed byte to unsigned
                var b = bytes[i] & 0xff;

                // Convert to hex and pad with leading zero if needed
                result.push(('0' + b.toString(16)).slice(-2));
            }
            return result.join(' ');
        }

        // Hook the writeCharacteristic method to intercept BLE write operations
        BluetoothGatt.writeCharacteristic.implementation = function (ch) {
            try {
                // Get ...