# ev82etiq
This is a simple python package that once supplied image root, it resizes it.
Two kinds of resize are possible: you can resize and maintain the aspect ration of 
image, or you can resize to a square shape


## Installation and updating
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Toolbox like below. 
Rerun this command to check for and install  updates .
```bash
pip install git+https://github.com/MuthumbiAlex/ev82etiq
```

## Usage
Features:
* function.py ---- main function that takes in 3 inputs:
  * x : 		location of image
  * height: 	what will be the height after resizing
  * ratio: 		do you want to maintain aspect ratio or not


* if code is run as ipynb, you can use interact to choose a slider on size of image (toy example provided), and dropbox with ratio choice

* function.ipynb is added as well ( to test the original .ipynb code written,and not .py since ipywidgets don't work in .py files)

#### Demo of some of the features:
```python
## cd into the directory
## use in jupyter notebook to use interactive from ipywidgets

import ev82etiq
from ev82etiq import function

# location of test image
im = r"data\new.png"

# by default, ratio is false so image is cropped to square
# starting height is 500
interact(im_resized, x=fixed(im), height=(100,1000,100), ratio=[True, False])

```

## License
[MIT](https://choosealicense.com/licenses/mit/)