from .image_utils import ImageText
from PIL import Image
import random
import string
import cv2, shutil
from .directory import TempDir
from .text import Text
from .imagesource import getImage


def TextToVideo(sourceData, vs=0):
	i = 'A'
	color = 'white'
	# TODO: Select font based on Kostya's work
	font = "calibri.ttf"
	backcolor = ['#210f05', '#444441', '#16082d', '#3d091f', '#420000', '#012824', '#332401', '#250130', '#011d30']
	li = Text(sourceData)
	secure_random = random.SystemRandom()
	dir_path = TempDir()
	img_array = []
	for text in range(0, len(li)):
		# TODO: Instead use single overlaid image created by Kostya
		img = ImageText((800, 600), background=secure_random.choice(backcolor))
		img.write_text_box((50, 50), li[text], box_width=700, font_filename=font, font_size=30, color=color, place='justify')
		img.save(dir_path+i+'.png')
		first_image = Image.open(dir_path+i+'.png')
		second_image = Image.open(getImage(li[text]))
		final_check = second_image.resize((700,300), resample=0)
		first_image.paste(final_check, (50, 282))
		first_image.save(dir_path+i+'.png')
		filename = dir_path+i+'.png'
		video_img = cv2.imread(filename)
		height, width, layers = video_img.shape
		size = (width, height)
		img_array.append(video_img)
		i = ''.join(random.choices(string.ascii_uppercase + string.digits))
	# TODO: Figure out how to append audio from Jasper's work
	out = cv2.VideoWriter('project.mp4', cv2.VideoWriter_fourcc(*'mp4v'), vs, size)
	for i in range(len(img_array)):
		out.write(img_array[i])
	out.release()
	shutil.rmtree(dir_path, ignore_errors=True)
	shutil.rmtree('downloads', ignore_errors=True)
