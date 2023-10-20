# DataDash Application Template

Author: M. W. Hefner

This is the DataDash application template.  Here, you will put a description and introduction to your application.

This application is built using Dash, a Python framework for building interactive web applications. It utilizes the Plotly library for creating data visualizations.

## Table of Contents

- [Before You Begin](#beforeyoubegin)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Before You Begin

Make sure that the RIEEE DataDash administrator has given you the permissions necessary to create a new DataDash application.

## Installation and Getting Started

1. First, clone the repository:

```shell
git clone https://github.com/mwhefner/datadash-application-template.git
```

2. Navigate to the project directory:

```shell
cd datadash-application-template
```

4. Create a python virtual environment (named "venv" in this case, but you can name it whatever you would like):

For windows:

```shell
python -m venv venv
```

For macOS and linux:

```shell
python3 -m venv venv
```

5. Activate the virtual environment:

For windows:

```shell
.\venv\Scripts\activate.bat 
```

For macOS and linux:

```shell
source venv/bin/activate
```

6. Install the required dependencies into the virtual environment:

```shell
pip install -r requirements.txt
```

Note: this step may take a considerable amount of time.

## Running for Local Development

1. Activate the virtual environment:

For windows:

```shell
.\venv\Scripts\activate.bat 
```

For macOS and linux:

```shell
source myenv/bin/activate
```

2. To run the application for local development, execute the following command:

```shell
python application.py
```

Once the application is running, open your web browser and visit `http://localhost:8050` to access the application's interface webpage.

3. Closing the application:

When you're done, exit the virtual environment by using the deactivate command:

```shell
deactivate
```

## Features

Give a detailed description of the application's features.

## License

Add appropriate license information here.
