# login -fastapi

'''
preprocess_pipeline
|
|-- preprocess.py
|   |
|   |-- __init__(self, path)
|   |-- checkFolder(self)
|   |-- loadImage(self)
|   |-- convertScale(self, alpha, beta)
|   |-- automatic_brightness_and_contrast(self, clip_hist_percent=25)
|   |-- maskImage(self)
|   |-- writeMaskImage(self)
|   |-- enlightenGAN(self)
|
|-- main.py
|-- img
|   |-- input_image.jpg
|
|-- models
|   |-- enlighten_gan.onnx
|
|-- output
|   |-- processed_image.jpg
|
|-- requirements.txt
|-- README.md

'''



## Project Structure

Here is an overview of the project structure:
```

preprocess_pipeline
|
|-- preprocess.py
|   |
|   |-- __init__(self, path)
|   |-- checkFolder(self)
|   |-- loadImage(self)
|   |-- convertScale(self, alpha, beta)
|   |-- automatic_brightness_and_contrast(self, clip_hist_percent=25)
|   |-- maskImage(self)
|   |-- writeMaskImage(self)
|   |-- enlightenGAN(self)
|
|-- main.py
|-- img
|   |-- input_image.jpg
|
|-- models
|   |-- enlighten_gan.onnx
|
|-- output
|   |-- processed_image.jpg
|
|-- requirements.txt
|-- README.md
```
