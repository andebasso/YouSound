YouSound: YouTube Audio Downloader

Overview
YouSound is a Python-based tool that allows users to download audio from YouTube videos. This project utilizes the pytube library to download videos and moviepy to extract audio, providing a simple GUI for ease of use.

Features
Download audio tracks from YouTube videos.
Simple and user-friendly graphical interface.
Allows users to choose download location and file names.
Error handling for download and conversion processes.
Installation
Prerequisites
Python 3.x
pip (Python package installer)
Setup
Clone this repository or download the source code.
Navigate to the project directory and create a virtual environment:
bash
Copy code
python -m venv venv
Activate the virtual environment:
Windows:
bash
Copy code
.\venv\Scripts\activate
macOS/Linux:
bash
Copy code
source venv/bin/activate
Install the required Python packages:
bash
Copy code
pip install -r requirements.txt
Usage
Run the main script:
bash
Copy code
python main.py
Enter the YouTube video URL when prompted in the application window.
Choose the destination folder and specify the desired name for the downloaded audio file.
Click 'Download and Convert' to start the download and conversion process.
Contributing
Contributions to YouSound are welcome! Feel free to fork the repository and submit pull requests.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Thanks to the pytube and moviepy libraries for enabling the core functionality of this tool.
