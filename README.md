# EGT309_26S1_test


### Name: Lai Qianhe
### Admin Number: 243106U
### Github Link: https://github.com/roxyalt/EGT_309_Test

#### Q2(a): Documenting Your Python Class:
class ViltVQA is to load images and encode them into values the model can understand
def __init__ is to initialise the process and set the variables for the image processor and image loader and contains the variable for the model. It also loads the model "dandelin/vilt-b32-finetuned-vqa" to the code for later use
def _load_image is to load images from the source and has two vairables, one is the image_source and the other is self which was initialised in def __init__. 
If the image source starts with http:// or https://, it will load the image and output the image. If the image source does not start with http:// or https://, it will still load and output the image.
If there is no image, it will return "Error"
def ask has 3 variables - self, pil_img and question. The function will process the question and the image and output an answer to the question according to the image. The image is encoded to allow the model to understand it before the model processes and outputs an answer.

#### Q2(d) Suggest Improvements to the Code:
Change the class name from ViltVQA to something more recognisable and represents the code like Image_Model. Add documentation throughout the code so that others will be able to understand it. 
Make the code robust so if the model fails, error message will be output. 
#### Q4 Advanced Github features implemented: