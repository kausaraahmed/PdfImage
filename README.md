

# PDF to Image Converter

This project is a Flask web application that enables users to upload PDF files and convert them into images (PNG format). If the uploaded PDF contains multiple pages, the images will be zipped together for easy download.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Upload PDF Files**: Users can upload PDF files through a simple web interface.
- **Convert PDF to Images**: Each page of the PDF is converted into a PNG image.
- **Zip Multiple Images**: For PDFs with multiple pages, images are compressed into a zip file for convenient downloading.
- **Download Images**: Users can download images individually or as a zip file.

## Technologies Used

- **Flask**: A micro web framework for Python.
- **PyMuPDF**: A library for manipulating PDF files and images.
- **HTML/CSS**: For frontend design.
- **Python**: For backend logic.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/kausaraahmed/repo-name.git

   cd repo-name
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install the required packages:**
   ```bash
    pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to `http://127.0.0.1:5000/`.

3. Upload a PDF file and click the submit button to convert it to images.

## Deployment

This application is ready for deployment on platforms like Vercel. Ensure all necessary environment variables are set and configurations are adjusted according to the hosting service's requirements.

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to fork the repository and submit a pull request.

Here’s how you can contribute to this project:

1. **Fork the Repository** (you can also give a star ^_^)


2. **Clone the Forked Repository**:
   ```bash
   git clone https://github.com/yourusername/repo-name.git
   cd repo-name
3. **Do your magic**
4. **Submit PR**

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```
