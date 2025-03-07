# back-replaci
Backend of Image Uploader
# Django Project Setup

This README provides instructions to set up and run a Django project with Docker and AWS S3 for media storage.

## Prerequisites
- Python 3.x
- pip
- virtualenv (optional)
- Docker & Docker Compose
- PostgreSQL (if not using SQLite)

## Installation

### 1. Clone the Repository
```sh
git clone <your-repo-url>
cd <your-project-name>
```

### 2. Create and Activate Virtual Environment (Optional)
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Setup Environment Variables
Create a `.env` file in the root directory:
```ini
# Django settings
DEBUG=True
SECRET_KEY=your_secret_key
ALLOWED_HOSTS=*

# Database (PostgreSQL example)
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=db
DB_PORT=5432

# AWS S3 Storage
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
AWS_STORAGE_BUCKET_NAME=your_s3_bucket_name
AWS_S3_REGION_NAME=your_s3_region
AWS_S3_CUSTOM_DOMAIN=https://your_s3_bucket.s3.amazonaws.com

# Docker settings
DOCKER_ENV=True
```

### 5. Apply Migrations
```sh
python manage.py migrate
```

### 6. Create Superuser
```sh
python manage.py createsuperuser
```

### 7. Run Server (Local Development)
```sh
python manage.py runserver
```

## Running with Docker

### 1. Build and Start Docker Containers
```sh
docker-compose up --build
```

### 2. Stop Containers
```sh
docker-compose down
```

### 3. Run Migrations in Docker
```sh
docker-compose exec web python manage.py migrate
```

### 4. Create a Superuser in Docker
```sh
docker-compose exec web python manage.py createsuperuser
```

## Project Structure
```
├── docker-compose.yml
├── Dockerfile
├── .env
├── manage.py
├── requirements.txt
├── app/
│   ├── settings.py
│   ├── urls.py
│   ├── models.py
│   ├── views.py
│   ├── ...
```

## Deployment Notes
- Ensure you configure production settings (`DEBUG=False`)
- Set up **AWS S3** for media file storage
- Use a **WSGI server** like Gunicorn for production
- Set up **Nginx** as a reverse proxy if required

## 📜 License
This project is licensed under the MIT License.

---

## 🔥 Authors
- **[Yash Dixit](https://github.com/Yashdixit2101)**

Happy coding! 🚀


