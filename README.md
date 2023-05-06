# login_fastapi

'''
[START]
 |
 v
+----------------------------+
| Import Libraries           |
| - os, cv2, glob, np        |
| - enlighten_inference      |
+----------------------------+
 |
 v
+----------------------------+
| Define preprocess class    |
+----------------------------+
 |            |
 |            v
 |  +------------------------+
 |  | __init__ method        |
 |  | - Initialize path      |
 |  | - Initialize model     |
 |  +------------------------+
 |            |
 |            v
 |  +------------------------+
 |  | checkFolder method     |
 |  | - Check/create folders |
 |  +------------------------+
 |            |
 |            v
 |  +------------------------+
 |  | loadImage method       |
 |  | - Read image from path |
 |  +------------------------+
 |            |
 |            v
 |  +------------------------+
 |  | convertScale method    |
 |  | - Adjust image scale   |
 |  +------------------------+
 |            |
 |            v
 |  +------------------------+
 |  | automatic_brightness_  |
 |  | and_contrast method    |
 |  | - Optimize brightness  |
 |  |   and contrast         |
 |  +------------------------+
 |            |
 |            v
 |  +------------------------+
 |  | maskImage method       |
 |  | - Apply mask to image  |
 |  +------------------------+
 |            |
 |            v
 |  +------------------------+
 |  | writeMaskImage method  |
 |  | - Apply inpainting     |
 |  +------------------------+
 |            |
 |            v
 |  +------------------------+
 |  | enlightenGAN method    |
 |  | - Enhance image        |
 |  +------------------------+
 |
 v
[END]

'''
