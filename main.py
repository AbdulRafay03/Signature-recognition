import tkinter as tk
from tkinter import filedialog, messagebox
import os
from model import modell
import glob
import sys
import io
from PIL import Image, ImageTk
# Define the main application window
class YOLOApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x500")
        self.root.title("YOLOv10 GUI")
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Select an option:")
        self.label.pack(pady=20)

        self.train_button = tk.Button(self.root, text="Train New Model", command=self.train_model)
        self.train_button.pack(pady=20)

        self.test_button = tk.Button(self.root, text="Test Existing Model", command=self.test_model)
        self.test_button.pack(pady=20)

        self.image_frame = tk.Frame(self.root)
        self.image_frame.pack(pady=40, fill=tk.BOTH, expand=True)


    def train_model(self):
        yaml_file = filedialog.askopenfilename(title="Select YAML file", filetypes=[("YAML files", "*.yaml")])
        if yaml_file:
            # Replace this with your training function call
            messagebox.showinfo("Training", f"Training started with {yaml_file}")
            time = modell.train(yaml_file)
            last_mod = self.get_last_modified_folder('runs/detect')
            self.label2 = tk.Label(self.root, text=f"training time = {time}s \n Results saved in {last_mod} \n Model ready for testing")
            self.label2.pack(pady=20)

        #get the model weights 
    def get_last_modified_folder(self,path):
        folders = glob.glob(f'{path}/*/')
        if not folders:
            return None
        last_modified_folder = max(folders, key=os.path.getmtime)
        return last_modified_folder

    def test_model(self):
        weights_file = filedialog.askopenfilename(title="Select Weights file", filetypes=[("Weights files", "*.pt")])
        if weights_file:
            # Notify the user that testing has started
            messagebox.showinfo("Testing", f"Testing started with {weights_file}")
            
            # Ask the user to select an image file for testing
            image_file = filedialog.askopenfilename(title="Select Image file", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
            
            if image_file:
                modell.test(weights_file, image_file)
            else:
                messagebox.showwarning("No Image Selected", "Please select an image file for testing.")


        self.display_images_from_directory()

    def display_images_from_directory(self):
        dir_path = self.get_last_modified_folder(r'runs\detect')
        if not dir_path:
            print("No directory found.")
            return

        print(f"Displaying images from: {dir_path}")

        # Clear any existing images
        for widget in self.image_frame.winfo_children():
            widget.destroy()

        # Get list of image files
        image_files = [f for f in os.listdir(dir_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

        # Display each image
        for image_file in image_files:
            image_path = os.path.join(dir_path, image_file)
            image = Image.open(image_path)
            image = image.resize((300, 300), Image.LANCZOS)  # Resize to fit in the GUI

            tk_image = ImageTk.PhotoImage(image)

            # Create a Label to display the image
            image_label = tk.Label(self.image_frame, image=tk_image)
            image_label.image = tk_image  # Keep a reference to avoid garbage collection
            image_label.pack(side=tk.LEFT, padx=5, pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    app = YOLOApp(root)
    root.mainloop()
