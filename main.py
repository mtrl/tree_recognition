import cv2
import numpy as np
import trees
from matplotlib import pyplot as plt
	
#maps = ['40216051.jpg']
maps = ['crop.jpg']

f = open('coords.txt', 'w+')

methods = ['cv2.TM_CCOEFF_NORMED']

for map in maps:
	f.write("----------------\r\nMap: " + map + "\r\n----------------\r\n");

	img_rgb = cv2.imread('images/' + map)
	img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
	template = cv2.imread('images/tree.jpg',0)
	w, h = template.shape[::-1]

	res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)

	threshold = 0.35
	matches = np.where( res >= threshold)
	matches = zip(*matches[::-1])
	matches = trees.remove_overlapping_matches(w, h, matches, 0.7)
	
	# remove items from the tuple that are in the same location as existing ones. Keep the one with the higher threshold
	
	tree_count = 0
	for pt in matches:
		tree_count += 1
		cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (255,0,0), 1)
		# find the trunk
		x_trunk_point = (pt[0] + w/2)
		y_trunk_point = (pt[1] + h - 5)
		cv2.rectangle(img_rgb, (x_trunk_point, y_trunk_point) , (x_trunk_point + 1, y_trunk_point + 1), (255,0,0), 1)
		f.write("X: " + str(pt[0]) + " Y: " + str(pt[1]) + "\r\n")
		
print str(tree_count) + " trees found"

cv2.imwrite('found_' + map,img_rgb)
print "Done " + map
	
f.close()

plt.imshow(img_rgb)
plt.show()