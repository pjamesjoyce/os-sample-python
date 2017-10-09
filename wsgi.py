from app import app


@app.route("/")
def hello():
    return "Hello Brave New World!"


if __name__ == "__main__":
    app.run()
