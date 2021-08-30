from flask import Flask

app = Flask(__name__)

productos = []
@app.route("/")
def inicio():
    #siempre que vamos a responder al client tiene queser por return
    return {
        "message":"Bienvenido a mi API",
        "content": ""
    }
    
    
if __name__ == "__main__":
    app.name(debug=True, port=8000)
