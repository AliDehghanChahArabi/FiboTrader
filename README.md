# FiboTrader
Stock market analysis, graphical user interface, AlphaVantage API, matplotlib, Fibonacci levels, buy/sell points, Tkinter, GUI, Python project.

This code provides a simple graphical interface for analyzing stock market prices. Users can input their desired stock symbol and API key for the AlphaVantage service, and upon clicking the "Plot Chart" button, they can view a price chart for DAX along with Fibonacci levels and buy/sell points. The program utilizes the Tkinter library for creating the graphical interface and matplotlib for plotting the chart. It fetches historical data from the AlphaVantage API and then plots the price chart along with buy/sell points using Fibonacci levels.

This project utilizes several popular libraries in Python to perform various tasks. Below is a brief description of each library:

1. requests: This library is used to send HTTP requests to websites and receive data in JSON or other formats. In this project, it is used to send requests to the AlphaVantage API to fetch historical stock market data.

2. json: This library allows you to work with JSON data. In this project, JSON data received from the API is parsed and analyzed using this library.

3. matplotlib: This is a powerful library for plotting charts and images in Python. In this project, matplotlib is used to plot the price chart of the DAX stock market, along with Fibonacci levels and buy/sell points.

4. datetime: This library allows you to work with datetime objects such as dates and times. In this project, it is used to convert dates received from the API into a suitable format.

5. numpy: This is a very popular library for numerical operations in Python. In this project, numpy is used to calculate Fibonacci levels.

6. pandas: This library is used for working with structured data such as tables (DataFrames). In this project, pandas is used to convert JSON data to DataFrame and calculate Fibonacci levels.

7. tkinter: This library is used to create a graphical user interface. In this project, tkinter is used to create a simple user interface for entering stock symbols and API keys and displaying the chart.


let's interpret the code step by step:

1. Importing Libraries: The code begins by importing the necessary libraries for the project.

2. Function Definitions:
    - get_stock_data: This function takes a stock symbol and an API key as input parameters, sends a request to the AlphaVantage API to fetch daily stock market data, and returns the response in JSON format.
    - plot_chart: This function is called when the user clicks the "Plot Chart" button. It extracts the stock symbol and API key entered by the user, calls the get_stock_data function to fetch the data, and then uses matplotlib to plot the price chart along with Fibonacci levels and buy/sell points.

3. Creating the GUI:
    - The Tkinter library is used to create a simple graphical user interface (GUI) with two input fields for entering the stock symbol and API key, and a button for plotting the chart.
    - The GUI elements are arranged using the grid layout manager.

4. Plotting the Chart:
    - When the user clicks the "Plot Chart" button, the plot_chart function is called.
    - Inside this function, the stock symbol and API key entered by the user are retrieved from the input fields.
    - The get_stock_data function is called with the stock symbol and API key to fetch the stock market data.
    - The data is then processed and plotted using matplotlib:
        -- The stock prices are plotted on the chart.
        -- Fibonacci levels are calculated based on the highest and lowest prices.
        -- Buy/sell points are identified based on certain conditions (in this case, if the price is above 61.8% of the highest price, it's considered a buy point, and if it's below 38.2% of the lowest price, it's considered a sell point).
        -- The chart is displayed with the Fibonacci levels and buy/sell points highlighted.
        -- Running the GUI: Finally, the mainloop method is called to run the GUI and wait for user interactions.
