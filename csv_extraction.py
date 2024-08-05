from flask import Flask, request, send_file
import pandas as pd
from io import BytesIO

app = Flask(__name__)

@app.route('/extract_csv', methods=['POST'])
def extract_csv():
    data = request.json  
    df = pd.DataFrame(data)
    csv_data = df.to_csv(index=False)
    output = BytesIO()
    output.write(csv_data.encode('utf-8'))
    output.seek(0)  

    return send_file(
        output,
        mimetype='text/csv',
        as_attachment=True,
        download_name='video_game_collection.csv'
    )

if __name__ == '__main__':
    app.run(debug=True, port=5001)  