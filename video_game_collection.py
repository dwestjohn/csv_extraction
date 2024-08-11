from flask import Flask, render_template_string, Response
import requests

app = Flask(__name__)

data = [
    {"Name": "Rampage", "Year": 1986, "Publisher": "Nintendo", "Platform": "N", "Currently Owned": "N", "Previously Beaten": "Y", "Looking To Purchase": "Y"},
    {"Name": "Maniac Mansion", "Year": 1987, "Publisher": "Nintendo", "Platform": "N", "Currently Owned": "N", "Previously Beaten": "Y", "Looking To Purchase": "Y"},
    {"Name": "Zombies Ate My Neighbors", "Year": 1993, "Publisher": "Super Nintendo", "Platform": "N", "Currently Owned": "Y", "Previously Beaten": "Y", "Looking To Purchase": "Y"},
    {"Name": "Golden Eye 007", "Year": 1997, "Publisher": "Nintendo 64", "Platform": "Y", "Currently Owned": "Y", "Previously Beaten": "N", "Looking To Purchase": "N"},
    {"Name": "Tony Hawk's Pro Skater 3", "Year": 2002, "Publisher": "Nintendo 64", "Platform": "Y", "Currently Owned": "Y", "Previously Beaten": "Y", "Looking To Purchase": "Y"}
]

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Video Game Collection</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 50px;
        }
        table {
            border-collapse: collapse;
            width: 100%;
            margin-bottom: 20px;
        }
        th, td {
            border: 1px solid #dddddd;
            text-align: left;
            padding: 8px;
        }
        th {
            background-color: #f2f2f2;
        }
        button {
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <h1>Video Game Collection</h1>
    <table>
        <thead>
            <tr>
                <th>Name</th>
                <th>Year</th>
                <th>Publisher</th>
                <th>Platform</th>
                <th>Currently Owned</th>
                <th>Previously Beaten</th>
                <th>Looking To Purchase</th>
            </tr>
        </thead>
        <tbody>
            {% for row in data %}
            <tr>
                <td>{{ row['Name'] }}</td>
                <td>{{ row['Year'] }}</td>
                <td>{{ row['Publisher'] }}</td>
                <td>{{ row['Platform'] }}</td>
                <td>{{ row['Currently Owned'] }}</td>
                <td>{{ row['Previously Beaten'] }}</td>
                <td>{{ row['Looking To Purchase'] }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
    <form action="/extract_csv" method="post">
        <button type="submit">Extract to CSV</button>
    </form>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_template, data=data)

@app.route('/extract_csv', methods=['POST'])
def extract_csv():
    response = requests.post('http://localhost:5001/extract_csv', json=data)
    
    return Response(
    response.content,
    mimetype='text/csv',
    headers={
        "Content-Disposition": "attachment;filename=video_game_collection.csv"
    }
)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)