import numpy as np

def remove_overlapping_matches(template_width, template_height, matches, overlap_allowed):
	f = open("log.txt", "w+")
	matches_array = np.asarray(matches)
	items_to_remove = []
	
	f.write("Template width: " + str(template_width))
	f.write(" Template height: " + str(template_height) + "\r\n")
	
	for idx, match in enumerate(matches_array):
		lower_x_bound = match[0] - (template_width/2 * (1 - overlap_allowed))
		upper_x_bound = match[0] + (template_width/2 * (1 - overlap_allowed))
		lower_y_bound = match[1] - (template_height/2 * (1 - overlap_allowed))
		upper_y_bound = match[1] + (template_height/2 * (1 - overlap_allowed))
		f.write("Index: " + str(idx) + "\r\n")
		f.write("X: " + str(match[0]) + " lower_x_bound: " + str(lower_x_bound) + " upper_x_bound :" + str(upper_x_bound) + "\r\n")
		f.write("Y: " + str(match[1]) + " lower_y_bound: " + str(lower_y_bound) + " upper_y_bound :" + str(upper_y_bound) + "\r\n")
		f.write("--------------\r\n")
		for comp_idx, compare_match in enumerate(matches_array):
			# Remove items that overlap by the specified amount
			if (
				comp_idx != idx and
				lower_x_bound <= compare_match[0] <= upper_x_bound and
				lower_y_bound <= compare_match[1] <= upper_y_bound
			):
				# Maybe add something in here to remove the lower threshold matched value
				#delete compare_match from tuple
				#print "matched"
				print comp_idx
				if comp_idx not in items_to_remove:
					items_to_remove.append(comp_idx)
	'''for idx in items_to_remove:
		matches_array[idx] = (0,0)
	for idx, match in enumerate(matches_array):
		if match == (0,0):'''
	#for x in range(len(matches_array) - 1, -1, -1):
		#print str(x) + " " + str(matches_array[x])
		#matches_array = np.delete(matches_array, (matches_array[x]))
	#print "Now: " + str(len(matches_array))
	print "items_to_remove len " + str(len(items_to_remove))
	f.close()
	return matches