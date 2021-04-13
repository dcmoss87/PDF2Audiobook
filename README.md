# PDF2Audiobook

## Description

People have various ways that they prefer to learn - whether it's visual, tactile, or aural. This application was created as an alternative to PDF only textbooks and will enable users to have the convenience and portability of an mp3 version of their textbooks.

## Table of Contents

1. [Setup](https://github.com/dcmoss87/PDF2Audiobook#setup)
2. [Usage](https://github.com/dcmoss87/PDF2Audiobook#usage)
3. [Troubleshooting](https://github.com/dcmoss87/PDF2Audiobook#troubleshooting)
4. [Dependencies](https://github.com/dcmoss87/PDF2Audiobook#dependencies)
5. [Author](https://github.com/dcmoss87/PDF2Audiobook#author)
6. [License](https://github.com/dcmoss87/PDF2Audiobook#license)

## Getting Started

This project was developed using [Visual Studio Code on Windows](https://code.visualstudio.com/docs/setup/windows).

An example PDF and audio output has been provided and can be found in the [Documentation](https://github.com/dcmoss87/PDF2Audiobook/tree/main/Documentation) folder.

### Setup

  1. Download the application files from [GitHub](https://github.com/dcmoss87/PDF2Audiobook).

  2. Place PDF file to be converted into the C:\Users\Your_Username subdirectory.

  3. Open the PDF2Audiobook.exe application located in the [dist](https://github.com/dcmoss87/PDF2Audiobook/tree/main/Application%20Files/PDF2Audiobook%20Application/dist) folder of the code download.

  4. Enter the name of the PDF file to convert in the PDF Name field (it is not necessary to put the file extension in the entry field as this will generate an error - example input can be found in the [Usage](https://github.com/dcmoss87/PDF2Audiobook#usage) subsection).

  5. In the Save File Name field, enter a name for the mp3 file that will be generated.

  6. Enter a starting and ending page range (please note that larger page ranges will take longer to convert - see the [Usage](https://github.com/dcmoss87/PDF2Audiobook#usage) and/or [Troubleshooting](https://github.com/dcmoss87/PDF2Audiobook#troubleshooting) subsections for more details).

  7. Select a language from the Language dropdown box.

  8. Click the Convert button.

  9. The Conversion Progress bar will indicate the progress of your conversion.

  10. Once the conversion is complete, the mp3 file will begin to play.

  11. From the application, you may choose to Pause or Resume the mp3 or Exit the program by clicking on the corresponding buttons.

  12. The newly created mp3 file can be found in the dist folder and played independently from the application.
 
### Usage

Place example pictures/gifs here

### Troubleshooting

Place troubleshooting and links to testing information here

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

