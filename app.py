from flask import Flask, request, jsonify, render_template_string
import datetime

app = Flask(__name__)

# تسجيل عنوان IP ونوع الجهاز عند الدخول مباشرة
@app.route('/')
def home():
    ip = request.remote_addr  # الحصول على عنوان IP
    user_agent = request.headers.get('User-Agent')  # الحصول على نوع الجهاز
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # تخزين عنوان IP ونوع الجهاز في ملف
    with open('ip_log.txt', 'a') as f:
        f.write(f"IP: {ip}, User Agent: {user_agent}, Timestamp: {timestamp}\n")

    return render_template_string("""
        <!DOCTYPE html>
        <html lang='ar'>
        <head>
            <meta charset='UTF-8'>
            <meta name='viewport' content='width=device-width, initial-scale=1.0'>
            <link href='https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css' rel='stylesheet'>
            <title>تسجيل الجهاز</title>
        </head>
        <body class='bg-light'>
            <div class='container mt-5'>
                <h2 class='text-center'>مرحبا بك!</h2>
                <div class='alert alert-success mt-3'>
                    تم تسجيل عنوان IP الخاص بك ونوع جهازك.
                </div>
            </div>
        </body>
        </html>
    """)

if __name__ == '__main__':
    app.run(debug=True)
