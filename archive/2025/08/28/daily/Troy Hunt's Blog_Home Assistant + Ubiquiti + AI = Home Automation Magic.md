---
title: Home Assistant + Ubiquiti + AI = Home Automation Magic
url: https://www.troyhunt.com/home-assistant-ubiquiti-ai-home-automation-magic/
source: Troy Hunt's Blog
date: 2025-08-28
fetch_date: 2025-10-07T00:50:51.741557
---

# Home Assistant + Ubiquiti + AI = Home Automation Magic

* [Home](https://www.troyhunt.com/)
* [Workshops](https://www.troyhunt.com/workshops/)
* [Speaking](https://www.troyhunt.com/speaking/)
* [Media](https://www.troyhunt.com/media/)
* [About](https://www.troyhunt.com/about/)
* [Contact](https://www.troyhunt.com/contact/)
* [Sponsor](https://www.troyhunt.com/sponsorship/)

**Sponsored by:**

# Home Assistant + Ubiquiti + AI = Home Automation Magic

27 August 2025

It seems like every manufacturer of anything electrical that goes in the house wants to be part of the IoT story these days. Further, they all want their own app, which means you have to go to gazillions of bespoke software products to control your things. And they're all - with very few exceptions - terrible:

![](https://www.troyhunt.com/content/images/2025/08/image-4.png)

That's to control the curtains in my office and the master bedroom, but the hubs (you need two, because the range is rubbish) have stopped communicating.

![](https://www.troyhunt.com/content/images/2025/08/image-5.png)

That one is for the spa, but it looks like the service it's meant to authenticate to has disappeared, so now, you can't.

![](https://www.troyhunt.com/content/images/2025/08/image-7.png)

And my most recent favourite, [Advantage Air](https://www.advantageair.com.au/?ref=troyhunt.com), which controls the many tens of thousands of dollars' worth of air conditioning we've just put in. Yes, I'm on the same network, and yes, the touch screen has power and is connected to the network. I know that because it looks like this:

![](https://www.troyhunt.com/content/images/2025/08/IMG_4187.jpg)

That might look like I took the photo in 2013, but no, that's *the current generation app,* complete with Android tablet now fixed to the wall. Fortunately, I can gleefully ignore it as all the entities are now exposed in [Home Assistant](https://www.home-assistant.io/?ref=troyhunt.com) (HA), then persisted into [Apple Home](https://www.apple.com/au/home-app/?ref=troyhunt.com) via [HomeKit Bridge](https://www.home-assistant.io/integrations/homekit/?ref=troyhunt.com), where they appear on our iThings. (Which also means I can replace that tablet with a nice iPad Mini running Apple Home and put the Android into the server rack, where it still needs to act as the controller for the system.)

Anyway, the point is that when you go all in on IoT, you're dealing with a lot of rubbish apps all doing pretty basic stuff: turn things on, turn things off, close things, etc. HA is great as it abstracts away the crappy apps, and now, it also does something much, much cooler than just all this basic functionality...

Start by thinking of the whole IoT ecosystem as simply being triggers and actions. Triggers can be based on explicit activities (such as pushing a button), observable conditions (such as the temperature in a room), schedules, events and a range of other things that can be used to kick off an action. The actions then include closing a garage door, playing an audible announcement on a speaker, pushing an alert to a mobile device and like triggers, many other things as well. That's the obvious stuff, but you can get really creative when you start considering devices like this:

![](https://www.troyhunt.com/content/images/2025/08/SWV_1991996d-1efd-477a-b3c0-2c8a24413546.webp)

That's a [Sonoff IoT water valve](https://sonoff.au/products/sonoff-zigbee-smart-water-valve?ref=troyhunt.com), and yes, it has its own app 🤦‍♂️ But because it's Zigbee-based, it's very easy to incorporate it into HA, which means now, the swag of "actions" at my disposal includes turning on a hose. Cool, but boring if you're just watering the garden. Let's do something more interesting instead:

![](https://www.troyhunt.com/content/images/2025/08/IMG_0116.jpg)

The valve is inline with the hose which is pointing upwards, right above the wall that faces the road and has one of these mounted on it:

![](https://www.troyhunt.com/content/images/2025/08/41TzHkdVbOL._UF894-1000_QL80_.jpg)

That's [a Ubiquiti G4 Pro doorbell](https://ui.com/us/en/physical-security/special-devices/doorbells?ref=troyhunt.com) (full disclosure: Ubiquiti has sent me all the gear I'm using in this post), and to extend the nomenclature used earlier, it has many different events that HA can use as triggers, including a press of the button. Tie it all together and you get this:

Not only does a press of the doorbell trigger the hose on Halloween, it also triggers [Lenny Troll](https://www.soundboard.com/sb/itslenny?ref=troyhunt.com), who's a bit hard to hear, so you gotta lean in *real* close 🤣 C'mon, they offered "trick" as one of the options!

Enough mucking around, let's get to the serious bits and per the title, the AI components. I was reading through [the new features of HA 2025.8](https://www.home-assistant.io/blog/2025/08/06/release-20258/?ref=troyhunt.com) (they do a monthly release in this form), and thought the chicken counter example was pretty awesome. Counting the number of chickens in the coop is a hard problem to solve with traditional sensors, but if you've got a camera that take a decent photo and an AI service to interpret it, suddenly you have some cool options. Which got me thinking about my rubbish bins:

![](https://www.troyhunt.com/content/images/2025/08/bincheck_20250819_111005.jpg)

The red one has to go out on the road by about 07:00 every Tuesday (that's general rubbish), and the yellow one has to go out every other Tuesday (that's recycling). Sometimes, we only remember at the last moment and other times, we remember right as the garbage truck passes by, potentially meaning another fortnight of overstuffing the bin. But I already had [a Ubiquiti G6 Bullet](https://ui.com/us/en/physical-security/bullet?ref=troyhunt.com) pointing at that side of the house (with a privacy blackout configured to avoid recording the neighbours), so now it just takes a simple automation:

```
- id: bin_presence_check
  alias: Bin presence check
  mode: single
  trigger:
    - platform: state
      entity_id: binary_sensor.laundry_side_motion
      to: "off"
      for:
        minutes: 1
  condition:
    - condition: time
      weekday:
        - mon
        - tue
  action:
    - service: ai_task.generate_data
      data:
        task_name: Bin presence check
        instructions: >-
          Look at the image and answer ONLY in JSON with EXACTLY these keys:
          - bin_yellow_present: true if a rubbish bin with a yellow lid is visible, else false
          - bin_red_present: true if a rubbish bin with a red lid is visible, else false
          Do not include any other keys or text.
        structure:
          bin_yellow_present:
            selector:
              boolean:
          bin_red_present:
            selector:
              boolean:
        attachments:
          media_content_id: media-source://camera/camera.laundry_side_medium
          media_content_type: image/jpeg
      response_variable: result
    - service: "input_boolean.turn_{{ 'on' if result.data.bin_yellow_present else 'off' }}"
      target:
        entity_id: input_boolean.yellow_bin_present
    - service: "input_boolean.turn_{{ 'on' if result.data.bin_red_present else 'off' }}"
      target:
        entity_id: input_boolean.red_bin_present
```

Ok, so it's a 40-line automation, but it's also pretty human-readable:

1. When there's motion that's stopped for a minute...
2. And it's a Monday or Tuesday...
3. Create an AI task that requests a JSON response indicating the presence of the yellow and red bin...
4. And attach a snapshot of the camera that's pointing at them...
5. Then set the values of two input booleans

From that, I can then create an alert if the correct bin is still present when it should be out on the road. Amazing! I'd always wanted to do something to this effect but had assumed it would involve sensors on the bins themselves. Not with AI though 😊

And then I started getting carried away. I already had [a Ubiquiti AI LPR](https://ui.com/...