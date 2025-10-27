---
title: Web Hackers vs. The Auto Industry: Critical Vulnerabilities in Ferrari, BMW, Rolls Royce, Porsche, and More
url: https://samcurry.net/web-hackers-vs-the-auto-industry/
source: Over Security - Cybersecurity news aggregator
date: 2023-01-14
fetch_date: 2025-10-04T03:54:54.591611
---

# Web Hackers vs. The Auto Industry: Critical Vulnerabilities in Ferrari, BMW, Rolls Royce, Porsche, and More

[‹ Back](/)

* Findings Summary
* Vulnerability Writeups
* (1) Full Account Takeover on BMW and Rolls Royce via Misconfigured SSO
* (2) Remote Code Execution and Access to Hundreds of Internal Tools on Mercedes-Benz and Rolls Royce via Misconfigured SSO
* (3) Full Account Takeover on Ferrari and Arbitrary Account Creation allows Attacker to Access, Modify, and Delete All Customer Information and Access Administrative CMS Functionality to Manage Ferrari Websites
* (4) SQL Injection and Regex Authorization Bypass on Spireon Systems allows Attacker to Access, Track, and Send Arbitrary Commands to 15 million Telematics systems and Additionally Fully Takeover Fleet Management Systems for Police Departments, Ambulance Services, Truckers, and Many Business Fleet Systems
* (5) Mass Assignment on Reviver allows an Attacker to Remotely Track and Overwrite the Virtual License Plates for All Reviver Customers, Track and Administrate Reviver Fleets, and Access, Modify, and Delete All User Information
* (6) Full Remote Vehicle Access and Full Account Takeover affecting Hyundai and Genesis
* (7) Full Remote Vehicle Access and Full Account Takeover affecting Honda, Nissan, Infiniti, Acura
* (8) Full Vehicle Takeover on Nissan via Mass Assignment
* Credits

[‹ Back](/)

# Web Hackers vs. The Auto Industry: Critical Vulnerabilities in Ferrari, BMW, Rolls Royce, Porsche, and More

Tue Jan 03 2023

![Web Hackers vs. The Auto Industry: Critical Vulnerabilities in Ferrari, BMW, Rolls Royce, Porsche, and More](/images/web-hackers-vs-the-auto-industry/o2WUB2y.png)

During the fall of 2022, a few friends and I took a road trip from Chicago, IL to Washington, DC to attend a cybersecurity conference and (try) to take a break from our usual computer work.

While we were visiting the University of Maryland, we came across a fleet of electric scooters scattered across the campus and couldn't resist poking at the scooter's mobile app. To our surprise, our actions caused the horns and headlights on all of the scooters to turn on and stay on for 15 minutes straight.

When everything eventually settled down, we sent a report over to the scooter manufacturer and became super interested in trying to more ways to make more things honk. We brainstormed for a while, and then realized that nearly every automobile manufactured in the last 5 years had nearly identical functionality. If an attacker were able to find vulnerabilities in the API endpoints that vehicle telematics systems used, they could honk the horn, flash the lights, remotely track, lock/unlock, and start/stop vehicles, completely remotely.

At this point, we started a group chat and all began to work with the goal of finding vulnerabilities affecting the automotive industry. Over the next few months, we found as many car-related vulnerabilities as we could. The following writeup details our work exploring the security of telematic systems, automotive APIs, and the infrastructure that supports it.

## Findings Summary

During our engagement, we found the following vulnerabilities in the companies listed below:

* **Kia, Honda, Infiniti, Nissan, Acura**

  + Fully remote lock, unlock, engine start, engine stop, precision locate, flash headlights, and honk vehicles using only the VIN number
  + Fully remote account takeover and PII disclosure via VIN number (name, phone number, email address, physical address)
  + Ability to lock users out of remotely managing their vehicle, change ownership
    - For Kia's specifically, we could remotely access the 360-view camera and view live images from the car
* **Mercedes-Benz**

  + Access to hundreds of mission-critical internal applications via improperly configured SSO, including…
    - Multiple Github instances behind SSO
    - Company-wide internal chat tool, ability to join nearly any channel
    - SonarQube, Jenkins, misc. build servers
    - Internal cloud deployment services for managing AWS instances
    - Internal Vehicle related APIs
  + Remote Code Execution on multiple systems
  + Memory leaks leading to employee/customer PII disclosure, account access
* **Hyundai, Genesis**

  + Fully remote lock, unlock, engine start, engine stop, precision locate, flash headlights, and honk vehicles using only the victim email address
  + Fully remote account takeover and PII disclosure via victim email address (name, phone number, email address, physical address)
  + Ability to lock users out of remotely managing their vehicle, change ownership
* **BMW, Rolls Royce**

  + Company-wide core SSO vulnerabilities which allowed us to access any employee application as any employee, allowed us to…
    - Access to internal dealer portals where you can query any VIN number to retrieve sales documents for BMW
    - Access any application locked behind SSO on behalf of any employee, including applications used by remote workers and dealerships
* **Ferrari**

  + Full zero-interaction account takeover for any Ferrari customer account
  + IDOR to access all Ferrari customer records
  + Lack of access control allowing an attacker to create, modify, delete employee "back office" administrator user accounts and all user accounts with capabilities to modify Ferrari owned web pages through the CMS system
  + Ability to add HTTP routes on api.ferrari.com (rest-connectors) and view all existing rest-connectors and secrets associated with them (authorization headers)
* **Spireon**

  + Multiple vulnerabilities, including:
    - Full administrator access to a company-wide administration panel with ability to send arbitrary commands to an estimated 15.5 million vehicles (unlock, start engine, disable starter, etc.), read any device location, and flash/update device firmware
    - Remote code execution on core systems for managing user accounts, devices, and fleets. Ability to access and manage all data across all of Spireon
    - Ability to fully takeover any fleet (this would've allowed us to track & shut off starters for police, ambulances, and law enforcement vehicles for a number of different large cities and dispatch commands to those vehicles, e.g. "navigate to this location")
    - Full administrative access to all Spireon products, including the following…
      * GoldStar - <https://www.spireon.com/products/goldstar/>
      * LoJack - <https://www.spireon.com/products/goldstar/lojackgo/>
      * FleetLocate - <https://www.spireon.com/products/fleetlocate-for-fleet-managers/>
      * NSpire - <https://www.spireon.com/spireon-nspire-platform/>
      * Trailer & Asset - <https://www.spireon.com/solutions/trailer-asset-managers/>
    - In total, there were…
      * 15.5 million devices (mostly vehicles)
      * 1.2 million user accounts (end user accounts, fleet managers, etc.)
* **Ford**

  + Full memory disclosure on production vehicle Telematics API discloses
    - Discloses customer PII and access tokens for tracking and executing commands on vehicles
    - Discloses configuration credentials used for internal services related to Telematics
    - Ability to authenticate into customer account and access all PII and perform actions against vehicles
  + Customer account takeover via improper URL parsing, allows an attacker to completely access victim account including vehicle portal
* **Reviver**

  + Full super administrative access to manage all user accounts and vehicles for all Reviver connected vehicles. An attacker could perform the following:
    - Track the physical GPS location and manage the license plate for all Reviver customers (e.g. changing the slogan at the bottom of the license plate to arbitrary text)
    - Update any vehicle status to "STOLEN" which updates the license plate and informs authorities
    - Access all user records, including what vehicles people owned, their physical address, phone number, and email address
    - Access the fleet management functionality for any company, locate and manage all vehicles in a fleet
* **Porsche**

  + Ability to send retrieve vehicle locat...