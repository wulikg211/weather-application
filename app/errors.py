from flask import jsonify


def errorHandler(app):
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"error": "Bad Request", "message": "The request was invalid."}), 400

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({"error": "Unauthorized", "message": "Authentication is required."}), 401

    @app.errorhandler(403)
    def forbidden(error):
        return jsonify({"error": "Forbidden", "message": "You do not have permission to access this resource."}), 403

    @app.errorhandler(404)
    def page_not_found(e):
        return jsonify({"error": "Resource not found"}), 404

    @app.errorhandler(405)
    def page_not_found(e):
        return jsonify({"error": "Method Not Allowed"}), 405

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({"error": "Internal Server Error", "message": "An internal server error occurred."}), 500

    @app.errorhandler(Exception)
    def handle_exception(e):
        return jsonify({"error": "An unexpected error occurred", "message": str(e)}), 500
