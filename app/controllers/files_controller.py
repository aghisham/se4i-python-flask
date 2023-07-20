from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import os


files_bp = Blueprint(
    "files_bp", __name__, template_folder="templates", static_folder="static"
)


@files_bp.route("", methods=["POST"])
def upload_file():
    """Upload one or muliple files

    Returns:
        str: message
    """
    try:
        # One file upload
        if request.files["file"]:
            file = request.files["file"]
            file.save(f"{os.getcwd()}/uploads/{secure_filename(file.filename)}")  # type: ignore
            return jsonify({"message": "File Uploaded"})
        # Multiple files upload
        elif request.files["files"]:
            files = request.files["files"]
            for file in files:
                file.save(f"{os.getcwd()}/uploads/{secure_filename(file.filename)}")  # type: ignore
            return jsonify({"message": "Files Uploaded"})
        else:
            return jsonify({"message": "No file was provided"})
    except:
        return jsonify({"message": "File not Uploaded"})


@files_bp.route("/<filename>", methods=["GET"])
def download_file(filename):
    try:
        return jsonify({"path": f"{os.getcwd()}/uploads/{filename}"})
    except:
        return jsonify({"message": "File not found"})
