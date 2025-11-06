from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    version = os.getenv('APP_VERSION', 'v1.0.0')
    hostname = socket.gethostname()
    
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Helm + Cloud Build Demo</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}
            .container {{
                text-align: center;
                background: rgba(255, 255, 255, 0.1);
                padding: 50px;
                border-radius: 20px;
                box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
            }}
            h1 {{ font-size: 3em; margin-bottom: 20px; }}
            .info {{ font-size: 1.2em; margin: 10px 0; }}
            .badge {{ 
                background: rgba(255, 255, 255, 0.2);
                padding: 10px 20px;
                border-radius: 10px;
                display: inline-block;
                margin: 10px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Helm + Cloud Build</h1>
            <div class="info">
                <div class="badge">Version: <strong>{version}</strong></div>
                <div class="badge">Pod: <strong>{hostname}</strong></div>
            </div>
            <p style="margin-top: 30px;">✅ Successfully deployed to GKE!</p>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)