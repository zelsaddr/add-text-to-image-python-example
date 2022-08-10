from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import random

def generate_struct(fname, hashtag1, hashtag2, date):
    font = ImageFont.truetype('./thermal-receipt.ttf', size=34)
    img = Image.open('./sample.jpg')
    draw = ImageDraw.Draw(img)

    draw.text((80, 451), "#"+str(hashtag1), fill=(64,60,59,255), font=font)
    draw.text((240, 451), "#"+str(hashtag2), fill=(64,60,59,255), font=font)
    draw.text((330, 451), "%s/07/2022" % str(date), fill=(64,60,59,255), font=font)
    saved = "./result/%s.jpg" % fname
    img.save(saved)

    print("[+] Generated %s" % saved)



for x in range(0, 100):
    rand = random.randint(1, 99)
    rand_date = random.randint(1, 30)
    hashtag1 = "0" + str(rand) if rand < 10 else str(rand) 
    rand = random.randint(1, 99)
    hashtag2 = "0" + str(rand) if rand < 10 else str(rand) 
    date = "0" + str(rand_date) if rand_date < 10 else str(rand_date)
    fname = "receipt_%s_%s_%s" % (hashtag1, hashtag2, date)
    generate_struct(fname, hashtag1, hashtag2, date)