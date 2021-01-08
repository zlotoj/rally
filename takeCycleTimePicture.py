from PIL import ImageFont
from PIL import ImageDraw
from PIL import Image
import scrapping
import time

# screenshot = driver.save_screenshot('cycleTime.png')
#
# screenshot=Image.open("cycleTime.png")
# (left, upper, right, lower) = (712, 224, 990, 298)
# im_crop = screenshot.crop((left, upper, right, lower))
# im_crop.save('table.png')
#
# (left, upper, right, lower) = (335, 200, 1570, 950)
# im_crop = screenshot.crop((left, upper, right, lower))
# draw=ImageDraw.Draw(im_crop)
# font = ImageFont.truetype("arial.ttf", 24)
# draw.text((10, 10),"Hello World !",(0,0,0),font=font)
# im_crop.save('graph.png')

def takeScreenshot(name, driver):
    screenshot = driver.save_screenshot('screenshot.png')
    screenshot=Image.open('screenshot.png')

    (left, upper, right, lower) = (712, 224, 990, 298)
    im_crop = screenshot.crop((left, upper, right, lower))
    im_crop.save('statsData\\'+name+'_cycleTimeTable.png')

    (left, upper, right, lower) = (335, 200, 1570, 950)
    im_crop = screenshot.crop((left, upper, right, lower))
    draw=ImageDraw.Draw(im_crop)
    font = ImageFont.truetype("arial.ttf", 16)
    draw.text((10, 10),name,(0,0,0),font=font)
    im_crop.save('statsData\\'+name+'_cycleTimeGraph.png')

if __name__ == "__main__":
    scrapping.init()

    url = 'https://rally1.rallydev.com/#/%s/custom/478931066124'  # template link to copy of dashboard

    driver = scrapping.driver
    scrapping.driver.get(url % '112919413276d')
    time.sleep(5)
    takeScreenshot('sample',driver)