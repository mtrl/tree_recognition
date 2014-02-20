import numpy as np
from collections import OrderedDict
import cv2
import os

def match_trees(map, template_file, match_threshold, overlap_threshold):
	if not os.path.exists('output'):
		os.makedirs('output')
		
	f = open(os.path.join('output', os.path.splitext(template_file)[0] + '_coords.txt'), 'w+')
	methods = ['cv2.TM_CCOEFF_NORMED']
	
	f.write("----------------\r\nMap: " + map + "\r\n----------------\r\n");

	img_rgb = cv2.imread('images/' + map)
	img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
	template = cv2.imread(os.path.join('images', template_file),0)
	w, h = template.shape[::-1]

	res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)

	matches = np.where( res >= match_threshold)
	matches = zip(*matches[::-1])
	matches = remove_overlapping_matches(w, h, matches, overlap_threshold)
	
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
		
	found_image_file = os.path.join('output', os.path.splitext(template_file)[0] + "_" + map)
	cv2.imwrite(found_image_file, img_rgb)
	print "----"	
	print str(tree_count) + " trees found"
	print "Written image file to: " + found_image_file
		
	f.close()

def remove_overlapping_matches(template_width, template_height, matches, overlap_allowed):
	items_to_remove = []
	for idx, match in enumerate(matches):
		if idx not in items_to_remove:
			lower_x_bound = match[0] - (template_width/2 * (1 - overlap_allowed))
			upper_x_bound = match[0] + (template_width/2 * (1 - overlap_allowed))
			lower_y_bound = match[1] - (template_height/2 * (1 - overlap_allowed))
			upper_y_bound = match[1] + (template_height/2 * (1 - overlap_allowed))
			for comp_idx, compare_match in enumerate(matches):
				# Remove items that overlap by the specified amount
				if (
					# if the idx has been flagged to be removed, dont check it
					comp_idx not in items_to_remove and
					comp_idx != idx and
					lower_x_bound <= compare_match[0] <= upper_x_bound and
					lower_y_bound <= compare_match[1] <= upper_y_bound
				):
					# Maybe add something in here to remove the lower threshold matched value
					if comp_idx not in items_to_remove:
						items_to_remove.append(comp_idx)
	matches_cleaned = []
	for idx, match in enumerate(matches):
		if(idx not in items_to_remove):
			matches_cleaned.append(match)
	return matches_cleaned