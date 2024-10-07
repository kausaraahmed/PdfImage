from flask import Flask, request, send_file, render_template
from pdf2image import convert_from_bytes
import io
import zipfile

app = Flask(__name__)


@app.route("/")
def upload_form():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def convert_pdf():
    pdf_file = request.files["pdf"]
    images = convert_from_bytes(pdf_file.read())
    filename = pdf_file.filename.split(".")[0]

    if len(images) > 1:
        zip_io = io.BytesIO()

        # Create the zip file in memory
        with zipfile.ZipFile(
            zip_io, mode="w", compression=zipfile.ZIP_DEFLATED, compresslevel=9
        ) as zip_archive:
            for i, image in enumerate(images):
                img_io = io.BytesIO()
                image.save(img_io, "JPEG")
                img_io.seek(0)
                zip_archive.writestr(f"{filename}_{i+1}.jpg", img_io.getvalue())

        zip_io.seek(0)

        return send_file(
            zip_io,
            mimetype="application/zip",
            as_attachment=True,
            download_name=f"{filename}.zip",
        )

    else:
        img_io = io.BytesIO()
        images[0].save(img_io, "JPEG")
        img_io.seek(0)
        return send_file(
            img_io,
            mimetype="image/jpeg",
            as_attachment=True,
            download_name=f"{filename}.jpg",
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
