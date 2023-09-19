from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    date =  request.form['date']
    temperature = request.form['temperature']
    humidity = request.form['humidity']
    ventilator_status = request.form['ventilator_status']
    watering_amount = request.form['watering_amount']
    growth_status = request.form['growth_status']
    store_data(date, temperature, humidity, ventilator_status, watering_amount, growth_status)
    stored_data = read_data_from_csv()
    return 'Data submitted successfully!'

# extra code for training model from the csv file 

def read_data_from_csv():
    data = []
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

def store_data(date, temperature, humidity, ventilator_status, watering_amount, growth_status):
    with open('data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, temperature, humidity, ventilator_status, watering_amount, growth_status])

if __name__ == '__main__':
    app.run()