from flask import request, redirect


def httpHandler(app):
    @app.before_request
    def https_redirect():
        if request.headers.get('X-Forwarded-Proto') == 'http':
            return redirect(request.url.replace('http://', 'https://'), code=301)
