from . import crear_app
from dotenv import load_dotenv

load_dotenv()

app = crear_app()

if __name__ == "__main__":
    app.run(debug=True, port=5000)
