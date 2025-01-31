from .image_utils import ImageText
from PIL import Image, ImageDraw, ImageFont
import random
import string
import cv2, shutil
from .directory import TempDir
from .text import Text
from .imagesource import getImage


def TextToVideo(sourceData, vs=0):
	i = 'A'
	color = 'white'
	font = "calibri.ttf"
	backcolor = ['#210f05', '#444441', '#16082d', '#3d091f', '#420000', '#012824', '#332401', '#250130', '#011d30']
	li = Text(sourceData)
	text_position = (50, 50)
	font_size = 150
	font_color = (255, 100, 100)
	secure_random = random.SystemRandom()
	dir_path = TempDir()
	img_array = []
	for text in range(0, len(li)):
		img = ImageText((800, 600), background=secure_random.choice(backcolor))
		img.write_text_box((50, 50), li[text], box_width=700, font_filename=font, font_size=30, color=color, place='justify')
		img.save(dir_path+i+'.png')
		first_image = Image.open(dir_path+i+'.png')
		second_image = Image.open(getImage(li[text]))
		final_check = second_image.resize((700,300), resample=0)
		first_image.paste(final_check, (50, 282))
		first_image.save(dir_path+i+'.png')
		filename = dir_path+i+'.png'
		img = Image.open(filename)
		img = img.resize((1280, 720), resample=0)
		draw = ImageDraw.Draw(img)
		font = ImageFont.truetype(font, font_size)
		draw.text(text_position, li[text], font_color, font=font)
		draw = ImageDraw.Draw(img)
		img.save(filename)
		video_img = cv2.imread(filename)
		height, width, layers = video_img.shape
		size = (width, height)
		img_array.append(video_img)
		i = ''.join(random.choices(string.ascii_uppercase + string.digits))
	out = cv2.VideoWriter('project.mp4', cv2.VideoWriter_fourcc(*'mp4v'), vs, size)
	for i in range(len(img_array)):
		out.write(img_array[i])
	out.release()
	shutil.rmtree(dir_path, ignore_errors=True)
	shutil.rmtree('downloads', ignore_errors=True)
