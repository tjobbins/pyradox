import os
import re
import collections
import pyradox.config
import pyradox.txt
import pyradox.worldmap
        
provinceMap = pyradox.worldmap.ProvinceMap()

colormap = {}
for filename, data in pyradox.txt.parseDir(os.path.join(pyradox.config.basedirs['EU4'], 'history', 'provinces'), verbose=False):
    m = re.match('\d+', filename)
    provinceID = int(m.group(0))
    if ('base_tax' in data and data['base_tax'] > 0):
        colormap[provinceID] = (255, 255, 255)

out = provinceMap.generateImage(colormap, defaultLandColor=(63, 63, 63))
out.save('out/blank_map.png')


