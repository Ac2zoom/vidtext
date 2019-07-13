# vidtext
Vidtext is a python library which provides the functionality to convert the text directly into the video. vidtext used the rake_nltk library to tokenization the text. then select the highest score token to make an image according to the token.
## Installation
### Using PIP
`pip install vidtext`
### Directly from the repository
```bash
$ git clone https://github.com/anubhavshakya/vidtext.git
$ cd vidtext
$ python setup.py install
```
## Usage
```python
import vidtext
li = "Text" # Text Content for video
content = vidtext.summary(li) # Return List
vidtext.TextToVideo(content,vs=0.1) # vs to control the speed of video
```
Ensure that `calibri.ttf` is present in the directory from which the script is run.
## Contributing
### Bug Reports and Feature Requests
Please use issue tracker for reporting bugs or feature requests.
### Development
Pull requests are most welcome.