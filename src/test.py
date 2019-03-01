#%%
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from random import randint

from photo import Photo

#%%
def parseFile(filename):
        f = open(filename,'r')
        lines = f.read().split('\n')
        return lines[1:]

#%%
def output(n, slideshow):
        #slideshow contiene solo gli id
        f = open("output.txt", "w")
        file.write(n)
        for slide in slideshow:
                file.write(s)
        file.close()

def function(set1,set2):
    intersection = len(set1.intersection(set2))
    diff1 = len(set1.difference(set2))
    diff2 = len(set2.difference(set1))
    return min(intersection,diff1,diff2)



#%%
def get_slideshow(slides):
        slideshow = []
        total_points = 0
        bitmask = np.zeros(len(slides))
        last_added = randint(len(slides))
        bitmask[last_added] = 1
        slideshow.append(last_added)
        for i in tqdm(range(len(slides))-1):
                if not (bitmask[i]==0):
                        break
                max_point = 0
                best_index = -1
                for slide in np.nonzero(bitmask - 1):
                        points = function(last_added.tags, slides[slide].tags)
                        if max_point <= points:
                                best_index = slide
                                max_point = points
                bitmask[best_index] = 1
                total_points += max_point
                slideshow.append(best_index)
                last_added=best_index
        return slideshow
                                                                                        
                


#%%
print("ciao")
main_f("ciao")
c
#%%
%load_ext line_profiler

#%%
r = %lprun -r -f main_f main_f('files/medium.in')
r.print_stats()

#%%sesso
