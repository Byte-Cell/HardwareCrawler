from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_script')
def run_script():
    result = subprocess.run(['python', 'hardware_scraper.py'], capture_output=True, text=True)
    output_lines = result.stdout.splitlines()
    return render_template('output.html', lines=output_lines)

if __name__ == '__main__':
    app.run(debug=True)
