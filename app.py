from flask import Flask, request, redirect, render_template
import os
from encryption import encrypt_file, hash_file
from database import get_connection
from audit import log_action

UPLOAD_FOLDER = "uploads"

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files["file"]

    if file:
        data = file.read()

        encrypted_data = encrypt_file(data)
        file_hash = hash_file(data)

        filename = file.filename
        stored_name = filename + ".enc"

        with open(os.path.join(UPLOAD_FOLDER, stored_name), "wb") as f:
            f.write(encrypted_data)

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO files (filename, stored_name, file_hash) VALUES (%s,%s,%s)",
            (filename, stored_name, file_hash)
        )

        conn.commit()
        cursor.close()
        conn.close()

        log_action("amy", "uploaded file")

    return redirect("/")
    

if __name__ == "__main__":
    app.run(debug=True)
