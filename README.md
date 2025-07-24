# Django ERP System 🚀

An Employee Resource Planning (ERP) web application built using Django, Docker, and MySQL — designed for managing employees, projects, staff meetings, and login authentication via OTP. This is a full-stack, internship-level project that includes modern features and a responsive UI.

---

## 🔐 Features

- 🔑 **Secure OTP-based Login System**  
- 👤 **Employee Management**  
  - Add new employees  
  - View employee profile (name, email, DOB, department, and image)  
- 🧑‍💼 **Staff & Project Management**  
  - Add/View Projects  
  - Specify Project Categories  
  - Assign Employees to Projects  
- 📅 **Meeting Management**
  - Schedule and list meetings  
- 🔄 **Login/Logout Functionality**
  - Session-based authentication  
- 🐳 **Dockerized Architecture**
  - Entire project runs inside Docker containers  
  - Uses `Gunicorn`, `Nginx`, and `MySQL`  
- 🛢️ **MySQL Integration**
  - Relational database configured via Docker Compose  
- 🖼️ **Responsive Frontend**
  - Based on open-source [ERP UI Template](https://github.com/kumardigamberjha/CodingIndiaERP/blob/master/website/templates/website/index.html)

---

## 🧰 Tech Stack

| Layer        | Technology           |
|--------------|----------------------|
| Backend      | Django, Python       |
| Frontend     | HTML, CSS, Bootstrap |
| Auth System  | OTP Email Verification |
| Database     | MySQL (Dockerized)   |
| Deployment   | Docker, Docker Compose, Gunicorn |
| Environment  | `.env` file using `python-decouple` |

---

## ⚙️ Installation (Docker)

> Make sure Docker Desktop is installed on your system.

1. Clone this repository  
   ```bash
   git clone https://github.com/abdal2007/django-docker-erp.git
  '''
  Project uses environment variables via python-decouple. Create a .env file in the root directory:
```bash
DJANGO_SECRET_KEY=django_secret-key
DEBUG=True
DB_NAME=Your-database-name
DB_USER=root
DB_PASSWORD=passowrd
DB_HOST=db
DB_PORT=3306

```
Make sure Docker Desktop is installed and running.
```bash
docker-compose up --build
```
Open a new terminal in the same directory and run:
```bash
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```
Access the App:
```bash
http://localhost:8000/

 



