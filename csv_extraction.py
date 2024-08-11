# Dependencies for the CSV Extraction
"""
Flask framework, send_file functionality, request variable, pandas packaging for conversion, 
BytesIO for proper encoding output (csv output file).
"""
from flask import Flask, request, send_file
import pandas as pd
from io import BytesIO

# Initialize Flask
app = Flask(__name__)


# extract_csv HTTP POST method
"""
1. requests JSON from client, adds to Pandas dataframe, converts using to_csv(), 
create output with BytestIO(), set pointer with seek.

2. Return the output using send_file with parameters. 
"""
@app.route('/extract_csv', methods=['POST'])
def extract_csv():
    # 1.
    data = request.json  
    df = pd.DataFrame(data)
    csv_data = df.to_csv(index=False)
    output = BytesIO()
    output.write(csv_data.encode('utf-8'))
    output.seek(0)  
    # 2.
    return send_file(
        output,
        mimetype='text/csv',
        as_attachment=True,
        download_name='video_game_collection.csv'
    )

if __name__ == '__main__':
    app.run(debug=True, port=5001)  