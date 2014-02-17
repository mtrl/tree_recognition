import cv2
import numpy as np
from matplotlib import pyplot as plt

maps = ['crop2.jpg', 'crop.jpg']

f = open('coords.txt', 'w+')

for map in maps:
	f.write("----------------\r\nMap: " + map + "\r\n----------------\r\n");
	img_rgb = cv2.imread('images/' + map)
	img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
	template = cv2.imread('images/tree.jpg',0)
	w, h = template.shape[::-1]

	res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
#	res = cv2.matchTemplate(img_gray,template,cv2.TM_SQDIFF)

	threshold = 0.35
	loc = np.where( res >= threshold)
	tree_count = 0
	for pt in zip(*loc[::-1]):
		tree_count += 1
		cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
		f.write("X: " + str(pt[0]) + " Y: " + str(pt[1]) + "\r\n")
		
	print tree_count
	cv2.imwrite('res' + map,img_rgb)
	print "Done " + map
	
f.close()