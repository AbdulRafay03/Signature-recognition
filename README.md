# Signature Recognition with YOLOv10

This repository contains code for training and testing a YOLOv10 model for signature recognition. The project includes a sample dataset, a sample weights file, and a GUI built using Tkinter to facilitate training and testing.

## Project Overview

- **Dataset**: 50 images split into 40 training images and 10 validation images.
- **Model**: YOLOv10 trained for 200 epochs.
- **Sample Data**: A sample dataset and corresponding YAML file are provided for replication.
- **Sample Model**: A trained weight file is included for testing.
- **GUI**: A graphical interface allows users to either train a new model or test an existing model.
- **Setup**: A `Setup.ipynb` notebook is provided to help you replicate the work easily.

## Files and Directories

- `Sample Model.pt`: Pre-trained YOLOv10 weights for testing.
- `runs/detect/`: Directory containing the results of model predictions.
- `weights/`: Directory containing weight files generated during training.
- `yolov10/`: YOLOv10 model code.
- `main.py`: Python script for the GUI application.
- `model.py`: Python script containing the model class and training/testing functions.
- `Setup.ipynb`: Jupyter notebook with setup instructions.
- `Sample data/`: Directory containing the sample dataset.

## How to Use

### GUI Application

- **Train a New Model**: Use the GUI to select a YAML file and start training a new YOLOv10 model.
- **Test an Existing Model**: Select a pre-trained weights file to run the model on a test image.

### Setup

1. Clone this repository.
2. Install the required dependencies.
3. Run the `main.py` notebook to replicate the work or set up your environment.
4. Use the GUI to start training or testing the model.

## Acknowledgements

This project is based on the YOLOv10 architecture and uses the Ultralytics library.

