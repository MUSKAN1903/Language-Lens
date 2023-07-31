# Language-Lens
Extracting Text and Detecting Language from images using MS Azure AI cognitive services

# INTRODUCTION
- In the digital world, images are a common source of data, but the text in them can be hard to extract and use.
- Optical Character Recognition (OCR) technology helps extract text from images. 
- Azure Cognitive Services offers OCR capabilities and other features for image analysis.
- Developers can easily incorporate image text detection and analysis into their applications with Azure Cognitive Services.
- Language detection identifies the language of text within images.
- Azure Cognitive Services offers language detection for multilingual support and more accurate text analysis.

# Azure Cognitive Services
- Azure Cognitive Services is a set of cloud-based services that allow developers to easily integrate artificial intelligence capabilities into their applications.
- It includes a range of services such as speech recognition, image and video analysis, language understanding, and more.
- These services use machine learning algorithms to provide intelligent insights and actions, making applications more powerful and engaging.
- Some of the key features of Azure Cognitive Services include easy integration with popular development tools, scalability, security, and global availability.

# Azure Services Used
### Computer Vision
- This service is used for reading the text from the uploaded image. 
- It provides Optical Character Recognition (OCR) capabilities to extract printed and handwritten text from images
- In our project, we use the Computer Vision API to extract the text from the uploaded image.

### Text Analytics
- This service is used for language identification of the extracted text. 
- It provides natural language processing capabilities to identify the language of a given text.
- In our project, we use the Text Analytics API to detect the language of the extracted text.

### How we get there
- **Input Image**
> * The user uploads an image to the system. 
> * The image should contain text written in any language which is supported by the system.

- **Text Detection**
> * The Computer Vision API is used to perform OCR on an uploaded image.
> * The OCR process extracts text from the image and returns the text as a string. The extracted text is then displayed in a text box on the GUI.

- **Language Identification**
> * The Azure Text Analytics service is used to identify the language of the extracted text.
> * This involves analyzing the text and determining the most likely language it is written in.

## Glimpses

![image](https://github.com/MUSKAN1903/Language-Lens/assets/70433658/f1c5063e-7f41-492a-9254-c2599df1aad5)
![image](https://github.com/MUSKAN1903/Language-Lens/assets/70433658/da29dcbe-9b82-4dc7-9eac-0332a0fdd816)
![image](https://github.com/MUSKAN1903/Language-Lens/assets/70433658/078928ee-3bbf-4d7f-bc99-8589e0727d2e)
![image](https://github.com/MUSKAN1903/Language-Lens/assets/70433658/25b85fab-e9fa-4b6a-ae40-fbd1384c3773)
![image](https://github.com/MUSKAN1903/Language-Lens/assets/70433658/f3a6e6e0-2cde-44f8-81f3-9758282cbfff)

## Future Scope
- Adding a translation feature that can translate the detected language to another language.
- Implementing real-time image text detection using a live camera feed instead of uploading an image.
- Developing a mobile application version of this project to make it more accessible to users on-the-go.
- Expanding the sentiment analysis feature to not only detect the sentiment of the text, but also identify the entities and key phrases present in the text.
- Integrating this project with other applications or services, such as a note-taking app, a cloud storage platform, or a social media site.

## Conclusion
- The project is about building an application that detects and extracts text from an image, identifies the language of the text, and performs sentiment analysis on it. 
- The application uses Azure Cognitive Services such as Computer Vision API and Text Analytics API for these tasks. 
- It can be useful in various industries that deal with text-based data and can improve efficiency by automating text extraction and language identification tasks.


































