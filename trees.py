import numpy as np
from collections import OrderedDict

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