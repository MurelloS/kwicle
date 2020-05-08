# gunicorn по умолчанию ищет объект \'application\'
from app import app as application
# и другие необходимые импорты

if __name__ == "__main__":
    application.run(debug=True, host="0.0.0.0", port=8000)
