---
title: Vehicle-based OSINT Investigations
url: https://digitalinvestigator.blogspot.com/2023/01/vehicle-based-osint-investigations.html
source: Instapaper: Unread
date: 2023-01-16
fetch_date: 2025-10-04T04:00:24.285316
---

# Vehicle-based OSINT Investigations

### Facebook SDK

* [Home](/)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[![Digital Investigator](https://blogger.googleusercontent.com/img/a/AVvXsEjCBXDAFtj3qeFsN0QARpauoOMU-9GGRJMhzK1L_edHwLn3gTy8NtKHApKnUjkKdWPgAEIcdSrosxULEGvjMszmWVhop1V0aiHOOEW8KeeKjSkfEk3bSEuXPRbuGgVQQJlHbfKNju9pNpyZOabgh-Oci700smDybZA3gHWWI5H2Mgy0h08GrB5-FiyV=s150)](https://digitalinvestigator.blogspot.com/)

* [Home](home-icon)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[Home](https://digitalinvestigator.blogspot.com/)[Open Source Intelligence](https://digitalinvestigator.blogspot.com/search/label/Open%20Source%20Intelligence)

# Vehicle-based OSINT Investigations

Joseph Moronwi
January 07, 2023
0

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiQmWzrI7TGiWUNUpaNs4FL4nkIKD2N89wILZu8B1HbY3S7fEFKzBX9ns304AAp1aKPsJbREPMrByBFHzNjATzICCduD6qE9IjuQrXqnqwYFeWDh4MTf6SAFMGq3dxDAxH3fn32r9bKZPCqt-PT2Ag8ESq5h2fxIcqoK3zXmq596yuseiqDmGvzVOBs/w638-h425/pexels-photo-221258.jpeg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiQmWzrI7TGiWUNUpaNs4FL4nkIKD2N89wILZu8B1HbY3S7fEFKzBX9ns304AAp1aKPsJbREPMrByBFHzNjATzICCduD6qE9IjuQrXqnqwYFeWDh4MTf6SAFMGq3dxDAxH3fn32r9bKZPCqt-PT2Ag8ESq5h2fxIcqoK3zXmq596yuseiqDmGvzVOBs/s5184/pexels-photo-221258.jpeg)

In most parts of the world, vehicles such as cars, motorcycles, planes, and ships need to be registered with one or more government offices. This can be done for purposes of tracking ownership in case they are stolen, for tax purposes, or for regulatory reasons. For consumer vehicles such as cars and trucks, registrations contain information about who owns the vehicle, and what country or region it is registered in, may contain the Vehicle Identification Number (VIN), and usually will contain the make, model, and year of the vehicle. With ships and planes, there may be additional data collected.

If
you come across these identifiers in your OSINT assessments, performing
searches on the vehicle registration and identification data can yield
excellent data that you can pivot on.

# Road Vehicles

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh9lBCaCTAWVm5jQe2pPNKwEvB63aoeuU9qg5GVfS9wUOuyajiDmCgWXeEwb_LDIbu92OCD114QHiKDeY_kEOPyi8gzscqc4BQ_Rmpo8lJSLsp_bLHbVHXkBaoTWjpufFYln9ygilHuv00y6NfyyuOO34LaqpA3Z1-rZYfwzz4E0JSOj2ST28wCUfDu/w627-h472/vehicledetails.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh9lBCaCTAWVm5jQe2pPNKwEvB63aoeuU9qg5GVfS9wUOuyajiDmCgWXeEwb_LDIbu92OCD114QHiKDeY_kEOPyi8gzscqc4BQ_Rmpo8lJSLsp_bLHbVHXkBaoTWjpufFYln9ygilHuv00y6NfyyuOO34LaqpA3Z1-rZYfwzz4E0JSOj2ST28wCUfDu/s1148/vehicledetails.jpg)

Vehicle records can be linked to two different unique numbers that exist for all vehicles on the road, VIN and VRM. Utilizing different internet systems, these unique numbers can be searched to bring back details including, vehicle make, vehicle model, the year vehicle was first registered, vehicle color, vehicle taxation status, and more.

## Vehicle Registration Marks

Most of these vehicles, once registered with the local or regional government, get a unique license plate that needs to be displayed. A Vehicle Registration Mark (VRM), is the [registration/ license plate](https://en.wikipedia.org/wiki/Vehicle_registration_plate) that is displayed on every vehicle in the world. A VRM is usually an alphanumeric, although sometimes just numeric, ID that uniquely identifies the vehicle or vehicle owner within the issuing region's vehicle register. We can collect this data and, depending upon where the vehicle is registered, perform a reverse lookup on the plate to find the owner and additional data.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgVmVHXxE7PrSrc6y01Hv3ZkiFCdEx_uECnDpIrG2XCTjjETGzKzm9gr-sKodSpFOGRdNRfl7LWTjqcwCwu56AICtxvUNs0kn9go1kmlUNZmvqeyLGp10YgWhvs-ac0ZldBag4nkx1J3ejfVRfYVNYqAGt4PPUqnY8wrF1EW4JxUssBhFf_1hpiSEEC/w651-h328/license_plates.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgVmVHXxE7PrSrc6y01Hv3ZkiFCdEx_uECnDpIrG2XCTjjETGzKzm9gr-sKodSpFOGRdNRfl7LWTjqcwCwu56AICtxvUNs0kn9go1kmlUNZmvqeyLGp10YgWhvs-ac0ZldBag4nkx1J3ejfVRfYVNYqAGt4PPUqnY8wrF1EW4JxUssBhFf_1hpiSEEC/s1600/license_plates.png)

By far, the easiest place to look up license plates is on a search engine. Looking up a plate such as `6LHW149` in DuckDuckGo shows an excellent link as the top result. Without entering a country or state, DuckDuckGo found a match. Turns out that this California license plate was found on the San Francisco Municipal Transportation Agency's document as a vehicle who's owner over-paid citations.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgIW-hZQbtRbP0z9AqnL2VU2eNrviA94_4XM5J-mbRDd6wOIuvniWnwjtiB3J0cJykCsNXjExk9GB-3b1nj6XJoUlZpIXDE7DBdgRIiprCqJ2wCfbozV2KhG97snCamSIbBhdepHMM7SFzDduePMo2aDynW7bVUgH3tsRkOu38KL6qcobc8kEBDb7tg/w648-h485/duckduckgo.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgIW-hZQbtRbP0z9AqnL2VU2eNrviA94_4XM5J-mbRDd6wOIuvniWnwjtiB3J0cJykCsNXjExk9GB-3b1nj6XJoUlZpIXDE7DBdgRIiprCqJ2wCfbozV2KhG97snCamSIbBhdepHMM7SFzDduePMo2aDynW7bVUgH3tsRkOu38KL6qcobc8kEBDb7tg/s751/duckduckgo.png)

Using search engines can yield valid results, but the best places to find valid data is, in the United States, the state level. In other countries, check who the registering authority for vehicles is and see if they allow searching of records. In the United States, some states allow for license plate look-ups, but it may cost a small fee and may require you to be a private investigator or law enforcement agent. Additionally, some of the commercial-tiered people search engines may show this data, but again there is a cost and restricted access. The following methods will display all publicly available details.

### FAXVIN License Plate Look-up

The [**faxvin service**](https://www.faxvin.com/license-plate-lookup) will resolve a United States license plate to a Vehicle Identification Number (VIN). The site will then allow you to perform additional paid searches based on the VIN.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgzbbPAF6kwJaredbBaEcd6SATZGnbgf6tOr0SVf-82nk-su57hDztzTIRmKXM4qvz8ZYBEF83KfYPmDa2A1SuO-Ou2QjPax4dtIh5uD7L0ishUFYXBS6DKn7ivRGj3CvB46QMErMEp_YdDqujffYHG6Mr7ifJKZcB0uKHWWiQ-e_AoFHUHWibJ5u9G/w651-h330/faxvin.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgzbbPAF6kwJaredbBaEcd6SATZGnbgf6tOr0SVf-82nk-su57hDztzTIRmKXM4qvz8ZYBEF83KfYPmDa2A1SuO-Ou2QjPax4dtIh5uD7L0ishUFYXBS6DKn7ivRGj3CvB46QMErMEp_YdDqujffYHG6Mr7ifJKZcB0uKHWWiQ-e_AoFHUHWibJ5u9G/s980/faxvin.PNG)

In the example above, we searched for the New York license plate GWF8627 and discovered the VIN associated to it.

### Autocheck

One fairly good and free license plate lookup tool for United States vehicles is at **[Autocheck](https://www.autocheck.com/vehiclehistory/?siteID=0)**. Visiting this page brings up search fields where you can enter in a license plate, and the search results should show up. A search for the California license plate 5HUH323 revealed that the plate is registered to a 2004 BMW Z4 car. Note that some result could display the Vehicle Identification Number (VIN) of the vehicle, which
can be used to perform additional searches.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEizh95QcSkLsYQ8EbxQ331TfmWVaw84_L6gPAuJVYKUjg3IFXSou6HcQQzFgLfNlSTS1zgKRyOR_sLTZrCjO982DhayI0s5H_lM_LHxnrlCg7ED_-y8RihcxeDRvbqVNU5d-OnBIFLt1-ZoMV3pZzoCMUy3_0dyXPjZHRKEBNnf7oItNDhsEkE5HgZj/w609-h574/autocheck.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEizh95QcSkLsYQ8EbxQ331TfmWVaw84_L6gPAuJVYKUjg3IFXSou6HcQQzFgLfNlSTS1zgKRyOR_sLTZrCjO982DhayI0s5H_lM_LHxnrlCg7ED_-y8RihcxeDRvbqVNU5d-OnBIFLt1-ZoMV3p...