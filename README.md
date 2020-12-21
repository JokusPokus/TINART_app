# ThisIsNotARealTalkshow

TINART is a student project from the 2020 fall semester at CODE
University of Applied Sciences. It allows the user to simulate an 
interactive political talk show with intelligent agents representing
the rethorical style of selected German politicians.

## Getting started

### Prerequisites

There should be a recent [Python](https://www.python.org/downloads/) version (3.x) installed on your computer. 

Moreover, we recommend using a common web browser like Chrome or Firefox.

### Setting up an environment

First, navigate to the local directory you would like to place the project code in. 
Then, clone the TINART repository.

```s
cd <PATH_TO_DIRECTORY>
git clone https://github.com/JokusPokus/TINART_app.git
```

Create a virtual environment. The first command is only required if the virtualenv package is not yet installed on your machine.

```s
pip install virtualenv
virtualenv venv
```

Activate the virtual environment.

For Linux users:

```s
source venv/bin/activate
```

For Windows users:

```s
.\venv\Scripts\activate
```

Alternatively, you can use your preferred Python IDE and select the venv there. This project was created using [PyCharm](https://www.jetbrains.com/pycharm/).

Next, install all required packages.

```s
pip install -r requirements.txt
```

To run the application locally, you need to 
execute the application file:

```s
python application.py
```

Note that iOS users need to replace the `pip` and `python` commands
with `pip3` and `python3`, respectively.

You may also wish to install the app in your virtual environment. Make sure to navigate to the Nim_AI root directory and execute:

```s
pip install -e .
```

### Language Models
A language model must be provided for each politician that can be selected in the talk show. A politician's language model must be saved in the following directory:

```s
\language_model\gpt2-{}
```

where {} is a placeholder for the politician's name.
For example:

```s
\language_model\gpt2-merkel
```

All models must be consistent with the [AutoModelForCausalLM](https://huggingface.co/transformers/model_doc/auto.html#automodelforcausallm) requirements from the [transformers](https://huggingface.co/transformers/) library.
We recommend using [this repository](https://github.com/JokusPokus/TINART-finetuning) for model fine-tuning. 

## Built with

- Python 3.7.4
- Flask 1.1.2
- Werkzeug 1.0.1

## Authors

- Jakob Schmitt (NLP, Backend)
- Igor Lapinski (Design, Frontend)

