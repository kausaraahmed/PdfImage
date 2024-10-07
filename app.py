from flask import Flask, request, send_file, render_template
import pymupdf
import io
import zipfile

app = Flask(__name__)


@app.route("/")
def upload_form():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def convert_pdf():
    pdf_file = request.files["file"]
    pdf_data = pdf_file.read()
    doc = pymupdf.open("pdf", pdf_data)
    images = []
    for page in doc:
        pix = page.get_pixmap()
        img_data = pix.tobytes("png")
        images.append(img_data)

    filename = pdf_file.filename.split(".")[0]

    if len(images) > 1:
        zip_io = io.BytesIO()

        # Create the zip file in memory
        with zipfile.ZipFile(
            zip_io, mode="w", compression=zipfile.ZIP_DEFLATED, compresslevel=9
        ) as zip_archive:
            for i, image in enumerate(images):
                zip_archive.writestr(f"{filename}_{i+1}.png", image)

        zip_io.seek(0)

        return send_file(
            zip_io,
            mimetype="application/zip",
            as_attachment=True,
            download_name=f"{filename}.zip",
        )

    else:
        img_io = io.BytesIO(images[0])  # Create a BytesIO object with the image bytes
        img_io.seek(0)  # Move the pointer to the start of the BytesIO object

        return send_file(
            img_io,
            mimetype="image/png",  # Change this to PNG since you're converting to PNG earlier
            as_attachment=True,
            download_name=f"{filename}.png",  # Change this to .png as well
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
