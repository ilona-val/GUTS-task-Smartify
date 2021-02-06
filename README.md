# GUTS task: make me sound smarter!

This tool will make your sentences sound smarter!

It can be run as both a command-line script, and as a Flask web application.

![Screenshot](./static/images/screenshot.png)

### Setup

There can be issues on Windows with installing SpaCy. It seems to work best with Anaconda. Good luck...

Firstly, clone the repository to your local computer, and navigate to the project folder.

You can try installing with pip, but may run into issues: `pip install -r requirements.txt`

If you run into these issues, try below:

Open the Anaconda Prompt command line, and type the following commands to create a conda virtual environment:

```
conda create --name smartify
conda activate smartify
```

Navigate to the project directory via `cd` commands, and then, at the project root, type:

```
conda install -c conda-forge spacy -y
pip install -Iv nltk==3.3 spacy-wordnet lemminflect flask
```

spacy-wordnet requires NLTK version 3.3. If you encounter any issues, you can uninstall nltk and reinstall the correct version with:

```
pip uninstall nltk
pip install -Iv nltk==3.3
```

After all that is done, you should be able to run the app.

### Run the app

The first time you run the script, it will take a bit longer as it loads up a spaCy model and the NLTK WordNet dictionary. After that it's quicker. Works best with **longer** sentences.

To run the command line script:
`python smartify_cli.py <input-sentence>`

To run the Flask app, simply type:
`flask run`

The app should be available at localhost:5000
