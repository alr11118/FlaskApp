from flask import Blueprint, jsonify

api_bp = Blueprint("api", __name__)

@api_bp.route("/status")
def status():
    return jsonify({"status": "healthy", "version": "1.0.0"})