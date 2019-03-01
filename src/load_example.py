from main import *

input_files = ["input1.txt","input2.txt","input3.txt","input4.txt"]
index = 1
for f in input_files:
    lines = parseFile("../in/"+f)
    photos = []
    for i in range(0,len(lines)):
        photos.append(Photo.from_str(i,lines[i]))
    photos.sort(key = lambda x:len(x.tags))
    # for ph in photos:
    #     print(ph.orientation, ph.tags)

    slides = photoCombiner(photos)
    slideshow, points = get_slideshow(slides)
    output(slideshow,"../out/output"+str(index)+".txt")
    index+=1
    print(check_validity(slideshow,np.array(points)))

#print([slide for slide in slideshow])