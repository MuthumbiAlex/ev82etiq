from distutils.core import setup
from setuptools import find_packages


# In[2]:


setup(name='ev82etiq',
      version='0.1',
      author='alex muthumbi',
      author_email='alex.k.muthumbi@fau.de',
      packages=find_packages(),
      install_requires=['Pillow', 'ipywidgets', 'matplotlib'])
