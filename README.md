# PDF2Audiobook

## Description

People have various ways that they prefer to learn - whether it's visual, tactile, or aural. This application was created as an alternative to PDF only textbooks and will enable users to have the convenience and portability of an mp3 version of their textbooks.

## Table of Contents

1. [Setup](https://github.com/dcmoss87/PDF2Audiobook#setup)
2. [Usage](https://github.com/dcmoss87/PDF2Audiobook#usage)
3. [Dependencies](https://github.com/dcmoss87/PDF2Audiobook#dependencies)
4. [Author](https://github.com/dcmoss87/PDF2Audiobook#author)
5. [License](https://github.com/dcmoss87/PDF2Audiobook#license)

## Getting Started

This project was developed using [Visual Studio Code on Windows](https://code.visualstudio.com/docs/setup/windows).

An example PDF and audio output has been provided and can be found in the [Documentation](https://github.com/dcmoss87/PDF2Audiobook/tree/main/Documentation) folder.

### Setup/Installation

  1. Download the application files from [GitHub](https://github.com/dcmoss87/PDF2Audiobook).

  2. Place PDF file to be converted into the C:\Users\Your_Username subdirectory.

  3. Open the PDF2Audiobook.exe application located in the [dist](https://github.com/dcmoss87/PDF2Audiobook/tree/main/Application%20Files/PDF2Audiobook%20Application/dist)     folder of the code download.
 
### Usage

  1. Enter the name of the PDF file to convert in the PDF Name field (it is not necessary to put the file extension in the entry field as this will generate an error).
    
![PDFNameEntry](https://github.com/dcmoss87/PDF2Audiobook/blob/main/Documentation/Example%20Pictures/PDFNameEntry.PNG)
  
  2. In the Save File Name field, enter a name for the mp3 file that will be generated.

  3. Enter a starting and ending page range (please note that larger page ranges will take longer to convert).

  4. Select a language from the Language dropdown box.

  5. Click the Convert button.

  6. The Conversion Progress bar will indicate the progress of your conversion.

  7. Once the conversion is complete, the mp3 file will begin to play.

  8. From the application, you may choose to Pause or Resume the mp3 or Exit the program by clicking on the corresponding buttons.

  9. The newly created mp3 file can be found in the dist folder and played independently from the application.

## Dependencies

This program utlizes multiple modules including:
- [os](https://docs.python.org/3/library/os.html)
- [gtts](https://pypi.org/project/gTTS/)
- [googletrans](https://pypi.org/project/googletrans/)
- [PyPDF2](https://pypi.org/project/PyPDF2/)
- [pygame](https://pypi.org/project/pygame/)
- [pathlib](https://docs.python.org/3/library/pathlib.html)
- [tkinter](https://docs.python.org/3/library/tkinter.html)
- [threading](https://docs.python.org/3/library/threading.html)

## Author

* **Derek Moss** - [dcmoss87](https://github.com/dcmoss87)

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/dcmoss87/PDF2Audiobook/blob/main/License/LICENSE) file for details.

