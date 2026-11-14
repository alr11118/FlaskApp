from app import create_app

app = create_app()

if __name__ == "__main__":
    # Runs the server in debug mode locally
    app.run(debug=True)