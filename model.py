from ultralytics import YOLOv10
import torch
import time
import os

class modell:
    @staticmethod
    def test(model_file_path , test_file_path):
        model = YOLOv10(model_file_path)
        model.predict(test_file_path, save=True)
        
    @staticmethod
    def train(file_path):
        model = YOLOv10()
        yaml_filename = os.path.basename(file_path)
        start_time = time.time()
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        model.train(data=file_path, epochs=200, device=device ) 
        
        training_time = time.time() - start_time
        return training_time
        
    

