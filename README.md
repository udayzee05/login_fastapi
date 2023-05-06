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
Insurance Prediction System
├── .github
│ └── workflows
│ ├── .gitkeep
│ └── main.yaml
├── configs
│ └── config.yaml
├── src
│ ├── components
│ │ └── init.py
│ ├── entity
│ │ └── init.py
│ ├── pipeline
│ │ └── init.py
│ ├── logger
│ │ └── init.py
│ ├── init.py
│ ├── config.py
│ ├── exception.py
│ ├── predictor.py
│ └── utils.py
├── main.py
|   app.py
├── requirements.txt
└── setup.py
```
