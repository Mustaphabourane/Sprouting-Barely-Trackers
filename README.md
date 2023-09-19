# Sprouting Barley Trackers

This is a Flask application designed to track the growth of sprouting barley. The application collects data such as date, temperature, humidity, ventilator status, watering amount, and growth status, and stores it in a CSV file for further analysis.

## How to Use

1. Run the Flask application in your terminal.
2. Open your web browser and navigate to the home page of the application. You should see a form where you can input the data.
3. After submitting the form, the data will be stored in a CSV file and a success message will be displayed.

## Endpoints

- `/`: The home page of the application. Displays a form to input the data.
- `/submit`: The endpoint that handles the form submission. It stores the data in a CSV file and returns a success message.

## Functions

- `home()`: Renders the home page.
- `submit()`: Handles the form submission. It retrieves the data from the form, stores it in a CSV file, and returns a success message.
- `read_data_from_csv()`: Reads the data from the CSV file and returns it as a list of rows.
- `store_data()`: Stores the data in the CSV file.

## Running the Application

To run the application, navigate to the directory containing the application and run the following command:

```bash
python3 apps.py

 

#The application will start and you can access it at
- http://localhost:5000.




Note
- This application is part of the "Sprouting Barely Trackers" project, which is focused on developing an automation project related to tracking sprouting barley.



Please let me know if you need any changes or additions to this README.md file.