# Face Recognition System using streamlit

## Description
This is a simple face matching application built using Streamlit and face_recognition library. It allows users to capture images using a webcam or upload images to check for facial similarity.

This project contains a Python script `main.py` that implements a face recognition system. It takes input from a webcam or an uploaded image, matches it with the camera input, and provides the matching percentage as output. The project uses `OpenCV`, `Streamlit`, and the `face_recognition` library.

## Features

1. Capture reference and destination images using a webcam.
2. Upload images instead of capturing.
3. Perform face recognition to check if two images match.
4. Display similarity score and match results.

## Installation
#### Prerequisites:

Ensure you have Python installed on your system. You can install the required dependencies using the following command:
```sh
pip install streamlit face-recognition cv2
```

#### How to Run:

Run the following command in your terminal to start the Streamlit app:
```sh
streamlit run app.py
```
#### Steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/your-repo.git
    ```
2. Navigate to the project directory:
    ```sh
    cd your-repo
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
## How It Works

1. The user provides a reference image by either capturing an image using the webcam or uploading an image.

2. The user provides a destination image by capturing an image using the webcam.

3. When the Start Matching button is clicked, the app:

- Detects and encodes faces from both images.

- Compares the encoded face data.

- Displays the result indicating whether the faces match, along with a similarity score.

4. If no face is detected in either image, the app notifies the user.


## Usage
Run the `main.py` script:
```sh
streamlit run main.py
```

## Dependencies

- Streamlit: For building the interactive UI.
- face_recognition: For encoding and comparing faces.
- OpenCv: functionalities such as image and video processing, object detection and tracking, facial recognition.
- Numpy: Numerical Operations (Arrays)
- Pillow (PIL): For handling image processing.

## Limitations

- Works best with clear and well-lit images.
- Can only detect one face per image.
- Face recognition accuracy may vary based on image quality and facial expressions.

## Future Enhancements

- Allow destination image upload along with camera capture.
- Improve multiple face detection and matching.
- Optimize face encoding process for better performance.

## Author
Developed by [SowmyaGovula]

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing
1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/fooBar`).
3. Commit your changes (`git commit -am 'Add some fooBar'`).
4. Push to the branch (`git push origin feature/fooBar`).
5. Create a new Pull Request.

## Contact
Your Name - [sowmyagovula@gmail.com](mailto:sowmyagovula@gmail.com)

GitHub Link: [https://github.com/sowmyagovul](https://github.com/sowmyagovula)