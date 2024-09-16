# QR Code Generator

This is a Flask-based web application that generates customized QR codes. Users can input a URL, choose a color for the QR code, and optionally upload an icon to be placed in the center of the QR code.

## Features

- Generate QR codes from user-provided URLs
- Customize QR code color
- Add custom icons to the center of the QR code
- Default icon if no custom icon is provided

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/qr-code-generator.git
   cd qr-code-generator
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python app.py
   ```

4. Open your web browser and navigate to `http://localhost:5000`

## Usage

1. Enter the URL you want to encode in the QR code
2. Choose a color for the QR code
3. (Optional) Upload an icon image to be placed in the center of the QR code
4. Click "Generate QR Code"
5. The generated QR code will be displayed and can be downloaded

## Dependencies

- Flask
- qrcode
- Pillow (PIL)

## License

This project is licensed under the MIT License - see the LICENSE file for details.