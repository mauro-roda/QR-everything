from flask import Flask, render_template, request
import qrcode

from pathlib import Path

app = Flask(__name__)

@app.route("/")
def main_page():
    #return "<p>Hello, World!</p>"
    #return f"Hello, {escape(name)}!"
    return render_template('index.html')

@app.route("/qr", methods=["GET", "POST"])
def quickQR():
    if request.method != "POST":
        return

    print("Generating QR code with message: ", request.form.get("data"))
    img = qrcode.make(request.form.get("data"))
    type(img) #make image
    img.save("static/qrcode.png") # save image to file
    print("Finished")

    # pngImage = io.BytesIO()
    # pngImage = "data:image/png;base64"
    # pngImage += base64.b64encode(pngImage.getvalue()).decode('utf8')

    #return render_template('index.html', image=img)
    #print(Path(img).absolute())
    return render_template('image.html', image="static/qrcode.png")