# Suicide Text Analysis

This project aims to detect suicidal ideation in textual data using Natural Language Processing (NLP) techniques and machine learning models. By analyzing text data, the system can classify inputs as indicative of potential suicidal thoughts or not, providing a tool for early intervention and support.

## Table of Contents

- [Dataset](#dataset)
- [Model Development](#model-development)
- [Web API](#web-api)
- [Web Interface](#web-interface)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Dataset

The dataset used for this project is sourced from Kaggle:

- **Suicide Watch Dataset**: [https://www.kaggle.com/datasets/nikhileswarkomati/suicide-watch](https://www.kaggle.com/datasets/nikhileswarkomati/suicide-watch)

Additionally, pre-trained GloVe embeddings are utilized:

- **Pickled GloVe Embeddings**: [https://www.kaggle.com/datasets/authman/pickled-glove840b300d-for-10sec-loading](https://www.kaggle.com/datasets/authman/pickled-glove840b300d-for-10sec-loading)

## Model Development

The `model.ipynb` notebook contains the steps for data preprocessing, model training, and evaluation. The process includes:

1. **Data Preprocessing**: Cleaning and preparing the text data for analysis.
2. **Feature Extraction**: Utilizing GloVe embeddings to represent text data.
3. **Model Training**: Implementing machine learning models to classify text as indicative of suicidal ideation or not.
4. **Evaluation**: Assessing model performance using appropriate metrics.

## Web API

An API is developed using Flask to serve the model and provide predictions based on user input. The API can be run using the `api.py` script.

## Web Interface

A simple web interface is provided to interact with the model:

- **HTML**: `index.html`
- **CSS**: `style.css`
- **JavaScript**: `script.js`

This interface allows users to input text and receive model predictions in real-time.

## Setup and Installation

To set up the project locally:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/rajakashyap77/Suicide-text-analysis.git
   ```

2. **Navigate to the project directory**:

   ```bash
   cd Suicide-text-analysis
   ```

3. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Download the necessary datasets** from the links provided above and place them in the project directory.

## Usage

1. **Run the API**:

   ```bash
   python api.py
   ```

   The API will start on `http://127.0.0.1:5000/`.

2. **Access the Web Interface**:

   Open `index.html` in a web browser to interact with the model.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

