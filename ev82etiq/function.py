from PIL import Image
from ipywidgets import interact, fixed
import matplotlib.pyplot as plt


# In[2]:


def imshow(x, height, ratio=False):
    image = Image.open(im)
    w,h = image.size
    
    if ratio: # keep aspect ratio
        #resize
        asp_ratio = (w/h)
        new_width = int(asp_ratio * height)
        resized = image.resize((new_width,height))

    
    # resize image to a square of dimension height*height
    else: 
        resized = image.resize((height, height))
    return resized


# In[3]:


im = '/Users/alex/Dropbox/ev82etiq/data/new.png'
test = imshow(im, 500)
plt.imshow(test)
plt.show()

# In[9]:

#####  UNCOMMENT WHEN RUNNING AS IPYNB

# interact(im_resized, x=fixed(im), height=(100,1000,100), ratio=[True, False])