from flask import Flask, request, jsonify
import csv

app = Flask(__name__)

# Endpoint to accept values as JSON
@app.route('/store_data', methods=['POST'])
def store_data():
    try:
        data = request.get_json()
        a = data['a']
        b = data['b']
        
        # Write data to CSV file
        with open('data.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([a, b])
        
        return "Data stored successfully\n"
    
    except KeyError:
        return "Error: Please provide values for both 'a' and 'b' fields\n", 400

# Endpoint to retrieve data from CSV file
@app.route('/get_data', methods=['GET'])
def get_data():
    try:
        data = []
        with open('data.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append({'a': row[0], 'b': row[1]})
        
        return jsonify(data)
    
    except FileNotFoundError:
        return "No data found\n", 404        

if __name__ == '__main__':
    app.run(debug=True)
