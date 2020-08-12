# alfred-download-url-from-scihub-workflow

## Features

1. Directly return pdf download url from sci-hub results.
1. **Make use of the external trigger of alfred workflow to cooperate with the google scholar workflow output.**

## Requirements

- Python 3
- [requests-html](https://github.com/psf/requests-html.git)

  To install requests-html, run this in command line

        $ pip3 install requests-html

  Or

        $ pip install requests-html

## Installations

Download the workflow file and import to alfred.

## Setup

You might need to change the python3 executable path in the setting of Script
Filter of the alfred workflow according to your settings.

The current setting is "/usr/local/opt/python@3.8/bin/python3". You should run
"which python3" in terminal to check your python3 executable path.

## Usage

Enter "shd" to trigger the workflow, paste the url of the research paper, done!
You will get the url to download the paper provided from sci-hub.

Holding **shift** will let you open the pdf directly in your browser.

## Acknowledgement

Please support Sci–Hub by donation to them if you are willing to.
