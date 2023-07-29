import tkinter as tk
from tkinter import filedialog
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
import requests
from PIL import Image, ImageDraw, ImageFont
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

API_KEY = "c61131d36b754e329847d53e0e127082"
ENDPOINT = "https://sentiment-1.cognitiveservices.azure.com/"
computervision_client = ComputerVisionClient(ENDPOINT, CognitiveServicesCredentials(API_KEY))

TEXT_ANALYTICS_KEY = "c61131d36b754e329847d53e0e127082"
TEXT_ANALYTICS_ENDPOINT = "https://sentiment-1.cognitiveservices.azure.com/"
text_analytics_client = TextAnalyticsClient(endpoint=TEXT_ANALYTICS_ENDPOINT, credential=AzureKeyCredential(TEXT_ANALYTICS_KEY))

def upload_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'rb') as image_file:
            try:
                read_response = computervision_client.read_in_stream(image_file, raw=True)
                read_operation_location = read_response.headers["Operation-Location"]
                operation_id = read_operation_location.split("/")[-1]
                while True:
                    read_result = computervision_client.get_read_result(operation_id)
                    if read_result.status not in ['notStarted', 'running']:
                        break
                if read_result.status == OperationStatusCodes.succeeded:
                    text = ''
                    for text_result in read_result.analyze_result.read_results:
                        for line in text_result.lines:
                            text += line.text + ' '
                            text += '\n'
                    textbox.delete('1.0', tk.END)
                    textbox.insert(tk.END, text)
                    
                # Detect language
                response = text_analytics_client.detect_language([text])
                language = response[0].primary_language.name

                # Display the image
                image = Image.open(file_path)
                image.thumbnail((300, 300))  # Resize the image to fit within the window
                photo = ImageTk.PhotoImage(image)
                image_label.configure(image=photo)
                image_label.image = photo  # Keep a reference to avoid garbage collection issues

                textbox.delete('1.0', tk.END)
                textbox.insert(tk.END, text)
                detected_language_text.delete('1.0', tk.END)  # Clear previous detected language
                detected_language_text.insert(tk.END, f"Detected language: {language}")

            except Exception as e:
                textbox.delete('1.0', tk.END)
                textbox.insert(tk.END, f"Error: {str(e)}")

def clear_text():
    textbox.delete('1.0', tk.END)
    detected_language_text.delete('1.0', tk.END)  # Clear detected language text
    image_label.configure(image='')  # Clear the image when text is cleared

root = tk.Tk()
root.title("Language Lens: Extracting Text and Detecting Language")
root.geometry("700x500")

# Load the background image
background_image = Image.open("bg2.jpg")
background_photo = ImageTk.PhotoImage(background_image)

# Create a Label widget with the image as the background
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Add the title label with custom font and no background color
title_label = tk.Label(root, text="Language Lens: Extracting Text and Detecting Language", font=("times", 24), fg="black",bg="white")
title_label.pack(pady=20)


# Buttons Frame
buttons_frame = tk.Frame(root, bg="white")
buttons_frame.pack(pady=10)

# Upload Button
upload_button = tk.Button(buttons_frame, text="Upload Image", command=upload_image, bg="#4CAF50", fg="white",
                          font=("Helvetica", 14), padx=10, pady=5, relief=tk.RAISED)
upload_button.pack(side=tk.LEFT, padx=10)

# Clear Button
clear_button = tk.Button(buttons_frame, text="Clear Text", command=clear_text, bg="#FF5722", fg="white",
                         font=("Helvetica", 14), padx=10, pady=5, relief=tk.RAISED)
clear_button.pack(side=tk.LEFT, padx=10)

# Image Label
image_label = tk.Label(root, bg="white", bd=3, relief=tk.SUNKEN)
image_label.pack(pady=20)

# Textbox
textbox = tk.Text(root, height=10, width=50, font=("Courier", 12), bg="white", bd=3, relief=tk.SUNKEN)
textbox.pack(pady=10)

# Detected Language Textbox
detected_language_text = tk.Text(root, height=1, width=35, font=("Helvetica", 14), bg="white", bd=3, relief=tk.SUNKEN)
detected_language_text.pack(pady=10)

root.mainloop()
