# Stock Dashboard Analysis

This Stock Dashboard is a simple yet powerful tool to visualize historical stock data, make stock selections, and generate future stock price predictions using the Alpha Vantage API, Streamlit, Plotly, and the Prophet forecasting model.
![Sample](image.png)
## Overview

1. [Features](#features)
2. [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Setup](#setup)
3. [Usage](#usage)
4. [Built With](#built-with)
5. [Contributing](#contributing)
6. [License](#license)

## Features

- Search for stocks and select from a list of matches.
- Visualize historical stock data using Plotly.
- Generate future stock price predictions with the Prophet forecasting model.

## Getting Started

Follow the steps below to set up and run the Stock Dashboard Analysis:

### Prerequisites

- Python 3.x

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Stock-Dashboard-Analysis.git
cd Stock-Dashboard-Analysis
```
2. Create a virtual enviroment (optional):
```bash
python -m venv venv
source venv/Scripts/ativate
```
3. Install project dependencies:
```bash
pip install -r requirements.txt
```
4. Get your API key from [Alpha Vantage](https://www.alphavantage.co/support/#api-key) and store it in a `.env` file in the project root:
```bash
API_KEY=your_api_key
```
5. Start Streamlit in your terminal with
```bash
streamlit run main.py
```

## Usage

Explore and analyze stock data with ease:

1. **Enter Ticker Symbol:**
   - Type the stock ticker in the sidebar.

2. **Select Stock:**
   - Choose from the suggested matches.

3. **Set Date Range:**
   - Pick start and end dates.

4. **Visualize Data:**
   - See historical stock data in the Plotly graph.

5. **Predict Trends:**
   - Generate future predictions with a single click.

## Built With

- [Streamlit](https://streamlit.io/) - The web framework used to create the interactive dashboard.
- [Plotly](https://plotly.com/python/) - Used for data visualization in the dashboard.
- [Prophet](https://facebook.github.io/prophet/) - A forecasting model for generating future stock price predictions.
- [Alpha Vantage API](https://www.alphavantage.co/) - Provides stock data for analysis.

## Contributing

Contributions are welcome! If you would like to contribute to the project, please follow these steps:

1. **Fork the repository.**
2. **Create a new branch (`git checkout -b feature/new-feature`).**
3. **Make your changes and commit them (`git commit -am 'Add new feature'`).**
4. **Push to the branch (`git push origin feature/new-feature`).**
5. **Open a pull request.**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
