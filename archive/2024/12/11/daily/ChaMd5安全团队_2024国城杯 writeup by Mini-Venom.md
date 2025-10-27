---
title: 2024国城杯 writeup by Mini-Venom
url: https://mp.weixin.qq.com/s?__biz=MzIzMTc1MjExOQ==&mid=2247511732&idx=1&sn=12433157723515b595110acf46a86823&chksm=e89d866cdfea0f7a8e72f11368c52afbc4920a59c6930f8af4bc9b8ebace5d9c0fd4286a4617&scene=58&subscene=0#rd
source: ChaMd5安全团队
date: 2024-12-11
fetch_date: 2025-10-06T19:41:34.286536
---

# 2024国城杯 writeup by Mini-Venom

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PUubqXlrzBR0D90CBDnicrgMuOte9kSPfySR5OEuKdkFYhmHJhusy3Ff1yTzthdoXIHMz1tsBzFGKvaN7uWUicBw/0?wx_fmt=jpeg)

# 2024国城杯 writeup by Mini-Venom

原创

Mini-Venom

ChaMd5安全团队

> > 招新小广告CTF组诚招re、crypto、pwn、misc、合约方向的师傅,长期招新IOT+Car+工控+样本分析多个组招人有意向的师傅请联系邮箱
> >
> > admin@chamd5.org(带上简历和想加入的小组)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBR0D90CBDnicrgMuOte9kSPfOg9NgZWWLt17CbeSgc7PibyVhc9EQxGujbGrjgRiaNibJ0GvRjcBlG7zA/640?wx_fmt=png&from=appmsg)

## misc

### Tr4ffIc\_w1th\_Ste90

解压压缩包得到一个password.pacpng，追踪UDP流，复制原始Hex数据，Cyberchef转一下

然后下载到本地改后缀为.264，VLC打开可以得到压缩包的解压密码：!t15tH3^pAs5W#RD\*f0RFL@9

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBR0D90CBDnicrgMuOte9kSPfrUpZqzYP0vRxZMRTXSEVMGjzwUwO9FnZIgb0s8LnYupaxzCxbI7IDQ/640?wx_fmt=png&from=appmsg)

5ebe4614-5544-4c1a-a7d4-d8240c8196e2

解压压缩包可以得到一张图片和一个加密代码，遛一遛GPT写一个解密代码

```
import numpy as np
import cv2
import sys
import os

def decode(input_image, output_dir, seed_range):
    to_recover = cv2.imread(input_image, cv2.IMREAD_GRAYSCALE)

    if to_recover is None:
        print(f"Error: Unable to load image {input_image}")
        exit(1)

    to_recover_array = np.asarray(to_recover)

    # Loop through all possible seeds in the given range
    for seed in seed_range:
        np.random.seed(seed)

        row_indices = list(range(to_recover_array.shape[0]))
        col_indices = list(range(to_recover_array.shape[1]))

        # Reverse shuffle the row and column indices
        np.random.shuffle(row_indices)
        np.random.shuffle(col_indices)

        row_reverse = np.argsort(row_indices)
        col_reverse = np.argsort(col_indices)

        # Reverse the row and column shuffling
        recovered_image = to_recover_array[row_reverse, :]
        recovered_image = recovered_image[:, col_reverse]

        # Save the decoded image with the current seed as part of the filename
        output_image = os.path.join(output_dir, f"recovered_seed_{seed}.png")
        cv2.imwrite(output_image, recovered_image)
        print(f"Decoded image saved as {output_image}")

        # Add a check here if the result is good enough (e.g., using some similarity measure)
        # For example, you could compare pixel-wise similarity or use image metrics like SSIM
        # If a match is found, you can break the loop and stop further processing

def main():
    if len(sys.argv) != 4:
        print('error! Please provide input image path, output directory, and seed range as command-line arguments.')
        exit(1)

    input_image = sys.argv[1]
    output_dir = sys.argv[2]
    seed_start = int(sys.argv[3].split('-')[0])  # start of seed range
    seed_end = int(sys.argv[3].split('-')[1])    # end of seed range

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    seed_range = range(seed_start, seed_end + 1)
    decode(input_image, output_dir, seed_range)

if __name__ == '__main__':
    main()
```

爆破一下seed就行：python decode.py encoded.png ./recovered\_images 0-1000

然后可以得到一张DataMatrix，在线网站扫码可以得到如下内容

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBR0D90CBDnicrgMuOte9kSPfKzdFLN6x8CQbzBHuXdSmic36DJObmjAZkTBj2iaFUiaGWQr21PMZwrCQw/640?wx_fmt=png&from=appmsg)

dc23c630-04bd-4801-8b70-2f5bb69246a2

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBR0D90CBDnicrgMuOte9kSPfFdRNnEvRWTr6iaelvfkQXfT3BdyqqZJo7ZSFFEicOFsFmeICwtriacj5w/640?wx_fmt=png&from=appmsg)

b7b7fa4a-b602-43ca-801d-01f763d1f679

> I randomly found a word list to encrypt the flag. I only remember that Wikipedia said this word list is similar to the NATO phonetic alphabet.
>
> crumpled chairlift freedom chisel island dashboard crucial kickoff crucial chairlift drifter classroom highchair cranky clamshell edict drainage fallout clamshell chatter chairlift goldfish chopper eyetooth endow chairlift edict eyetooth deadbolt fallout egghead chisel eyetooth cranky crucial deadbolt chatter chisel egghead chisel crumpled eyetooth clamshell deadbolt chatter chopper eyetooth classroom chairlift fallout drainage klaxon

然后找个PGP词汇表解密脚本解密一下即可得到flag

参考链接：https://gryffinbit.top/2020/11/14/%E4%B8%80%E4%BA%9B%E6%9D%82%E4%B9%B1%E7%9A%84%E5%AF%86%E7%A0%81/#PGP%E8%AF%8D%E6%B1%87%E8%A1%A8-%EF%BC%88%E7%94%9F%E7%89%A9%E8%AF%86%E5%88%AB%E8%AF%8D%E6%B1%87%E8%A1%A8%EF%BC%89

```
aaa=[
["00","aardvark","adroitness"],
["01","absurd","adviser"],
["02","accrue","aftermath"],
["03","acme","aggregate"],
["04","adrift","alkali"],
["05","adult","almighty"],
["06","afflict","amulet"],
["07","ahead","amusement"],
["08","aimless","antenna"],
["09","Algol","applicant"],
["0A","allow","Apollo"],
["0B","alone","armistice"],
["0C","ammo","article"],
["0D","ancient","asteroid"],
["0E","apple","Atlantic"],
["0F","artist","atmosphere"],
["10","assume","autopsy"],
["11","Athens","Babylon"],
["12","atlas","backwater"],
["13","Aztec","barbecue"],
["14","baboon","belowground"],
["15","backfield","bifocals"],
["16","backward","bodyguard"],
["17","banjo","bookseller"],
["18","beaming","borderline"],
["19","bedlamp","bottomless"],
["1A","beehive","Bradbury"],
["1B","beeswax","bravado"],
["1C","befriend","Brazilian"],
["1D","Belfast","breakaway"],
["1E","berserk","Burlington"],
["1F","billiard","businessman"],
["20","bison","butterfat"],
["21","blackjack","Camelot"],
["22","blockade","candidate"],
["23","blowtorch","cannonball"],
["24","bluebird","Capricorn"],
["25","bombast","caravan"],
["26","bookshelf","caretaker"],
["27","brackish","celebrate"],
["28","breadline","cellulose"],
["29","breakup","certify"],
["2A","brickyard","chambermaid"],
["2B","briefcase","Cherokee"],
["2C","Burbank","Chicago"],
["2D","button","clergyman"],
["2E","buzzard","coherence"],
["2F","cement","combustion"],
["30","chairlift","commando"],
["31","chatter","company"],
["32","checkup","component"],
["33","chisel","concurrent"],
["34","choking","confidence"],
["35","chopper","conformist"],
["36","Christmas","congregate"],
["37","clamshell","consensus"],
["38","classic","consulting"],
["39","classroom","corporate"],
["3A","cleanup","corrosion"],
["3B","clockwork","councilman"],
["3C","cobra","crossover"],
["3D","commence","crucifix"],
["3E","concert","cumbersome"],
["3F","cowbell","customer"],
["40","crackdown","Dakota"],
["41","cranky","decadence"],
["42","crowfoot","December"],
["43","crucial","decimal"],
["44","crumpled","designing"],
["45","crusade","detector"],
["46","cubic","detergent"],
["47","dashboard","determine"],
["48","deadbolt","dictator"],
["49","deckhand","dinosaur"],
["4A","dogsled","direction"],
["4B","dragnet","disable"],
["4C","drainage","disbelief"],
["4D","dreadful","disruptive"],
["4E","drifter","distortion"],
["4F","dropper","document"],
["50","drumbeat","embezzle"],
["51","drunken","enchanting"],
["52","Dupont","enrollment"],
["53","dwelling","enterprise"],
["54","eating","equation"],
["55","edict","equipment"],
["56","egghead","escapade"],
["57","eightball","Eskimo"],
["58","endorse","everyday"],
["59","endow","examine"],
["5A","enlist","existence"],
["5B","erase","exodus"],
["5C","escape","fascinate"],
["5D","exceed","filament"],
["5E","eyeglass","finicky"],
["5F","eyetooth","forever"],
["60","facial","fortitude"],
["61","fallout","frequency"],
["62","flagpole","gadgetry"],
["63","flatfoot","Galveston"],
["64","flytrap","getaway"],
["65","fracture","glossary"],
["66","framework","gossamer"],
["67","freedom","graduate"],
["68","frighten","gravity"],
["69","gazelle","guitarist"],
["6A","Geiger","hamburger"],
["6B","glitter","Hamilton"],
["6C","glucose","handiwork"],
["6D","goggles","hazardous"],
["6E","goldfish","headwaters"],
["6F","gremlin","hemisphere"],
["70","guidance","hesitate"],
["71","hamlet","hideaway"],
["72","highchair","holiness"],
["73","hockey","hurricane"],
["74","indoors","hydraulic"],
["75","indulge","impartial"],
["76","inverse","impetus"],
["77","involve","inception"],
["78","island","indigo"],
["79","jawbone","inertia"],
["7A","keyboard","infancy"],
["7B","kickoff","inferno"],
["7C","kiwi","informant"],
["7D","klaxon","insincere"],
[...