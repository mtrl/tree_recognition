import trees
	
maps = ['crop.jpg']

map_image = raw_input("Enter path to map image (Relative to images/ dir): ")
template_image = raw_input("Enter path to template image (Relative to images/ dir): ")
threshold = float(raw_input("Enter matching threshold value (e.g. 0.4): "))
match_overlap = int(raw_input("Enter allowed overlap % (e.g. 70): "))
match_overlap = match_overlap / 100

print "----------"
print "Working..."
print "----------"
trees.match_trees(map_image, template_image, threshold, match_overlap)