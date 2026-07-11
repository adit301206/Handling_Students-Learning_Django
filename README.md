# Student Management System

A Django-based Student Marks and Profile Management application designed for educational institutes. It supports role-based access control (Students vs. Faculty) via both a dynamic Web UI and a RESTful API.

---

## 🚀 Key Features

*   **Student Profiles**: Store and display profile images, student name, roll number, enrollment ID, contact email, and profile URL.
*   **Marks & Performance Tracking**: Calculates and shows total marks, percentages, and grading class (Distinction, First Class, etc.) based on `Python`, `FSD`, and `COA` subject marks.
*   **Role-Based Access Control**:
    *   **Students**: Can view only their own details and grades (must be logged in).
    *   **Faculty (Group)**: Can edit student marks, delete student records, and perform administrative operations.
*   **Django REST Framework API**:
    *   **API Versioning**: Supports `v1` and `v2` endpoints. V2 introduces a custom `grade` field calculation.
    *   **JWT Authentication**: Implemented via `djangorestframework-simplejwt` with a custom token view returning user roles (`faculty` / `student`) directly in the payload.
    *   **Secure Actions**: Dedicated PATCH endpoint (`/api/students/{id}/marks/`) restricted to users in the Faculty group.

---

## 🛠️ Tech Stack

*   **Backend**: Django (v6.0.3)
*   **Database**: SQLite
*   **API**: Django REST Framework (DRF), Simple JWT (JSON Web Token Authentication), DRF Spectacular
*   **Media Handling**: Pillow (for student profile picture uploads)

---

## 📦 Getting Started

### 1. Prerequisites
Ensure you have Python 3 installed.

### 2. Set Up Virtual Environment
Activate the pre-existing virtual environment in the project root:

```bash
# On Windows (PowerShell)
.\env\Scripts\activate

# On Linux/macOS
source env/bin/activate
```

### 3. Install Dependencies
If not already installed, make sure to install the required libraries:
```bash
pip install django djangorestframework djangorestframework-simplejwt pillow drf-spectacular
```

### 4. Database Setup & Migrations
Run the migrations to create the database schemas:
```bash
python manage.py migrate
```

### 5. Configure User Roles
1. Start the Django shell or use the Django Admin panel:
   ```bash
   python manage.py createsuperuser
   ```
2. In the Admin Panel (`http://127.0.0.1:8000/admin/`):
   * Create a new Group named **Faculty**.
   * Assign users who represent teachers/faculty members to this group.
   * Standard student users should not belong to the Faculty group.

### 6. Run the Application
Start the Django development server:
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser.

---

## 🔗 Endpoint Reference

### Web UI Routes

| Route | Method | Description | Access |
| :--- | :--- | :--- | :--- |
| `/` | `GET` | Home page listing students (can filter by enrollment ID using query parameter `?searchEnroll=`) | Public |
| `/detail/<student_id>/` | `GET` | Detailed profile view of a student | Logged-in (Owner or Faculty) |
| `/edit_marks/<student_id>/` | `GET`, `POST` | Edit marks for Python, FSD, and COA | Faculty Only |
| `/delete_student/<student_id>/` | `GET`, `POST` | Delete student profile | Faculty Only |
| `/account/signupaccount/` | `GET`, `POST` | Create a new user account | Public |
| `/account/loginaccount/` | `GET`, `POST` | Sign in | Public |
| `/account/logoutaccount/` | `GET` | Log out | Logged-in |

### REST API Endpoints

| Endpoint | Method | Description | Version | Auth Required |
| :--- | :--- | :--- | :--- | :--- |
| `/api/token/` | `POST` | Obtain JWT Access and Refresh Tokens | - | No |
| `/api/token/refresh/` | `POST` | Refresh existing JWT Access Token | - | No |
| `/api/students/` | `GET` | List all student profiles (v1) | v1 | Yes |
| `/api/v2/students/` | `GET` | List student profiles with grade (v2) | v2 | Yes |
| `/api/students/<id>/` | `GET` | Get detailed information for a student | v1 / v2 | Yes (Owner or Faculty) |
| `/api/students/<id>/marks/` | `PATCH` | Update Python, FSD, or COA marks | v1 / v2 | Yes (Faculty only) |
| `/api-auth/` | - | DRF browsable API login/logout | - | No |

---

## 📂 Project Structure

```text
├── account/               # Account signup, login, and logout views
├── database/              # Main project config (settings, URLs, wsgi)
├── media/                 # Uploaded student profile images
├── student/               # Core student profile model, views, API views, and serializers
├── db.sqlite3             # SQLite database file
├── manage.py              # Django project manager script
└── env/                   # Python virtual environment (ignored in source control)
```
