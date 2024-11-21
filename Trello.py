from flask import Flask, Response
import requests

app = Flask(__name__)

@app.route("/")
def trello_proxy():
    trello_url = "https://trello.com/b/JQb3dQsX.html"
    headers = {"Accept-Encoding": "identity"}
    response = requests.get(trello_url, headers=headers)
    return Response(response.content, content_type="text/html")

if __name__ == "__main__":
    app.run()
