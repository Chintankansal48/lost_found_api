# Lost & Found API 🏷️🔍

This is a **Django REST framework**-based API that allows users to:

- Report lost and found items.
- Retrieve a list of all lost or found items.
- Match lost items with found items based on name and location.
- Remove items once they are found or returned.
- Authenticate users via **JWT authentication** (Register/Login).

## 🚀 Features

- **User Authentication** (Register & Login using JWT)
- **Report Lost Items**
- **Report Found Items**
- **Retrieve Lists of Lost & Found Items**
- **Match Lost Items with Found Items**
- **Delete Items** Once Resolved

## 🛠️ Installation

### **1️⃣ Clone the Repository**

```sh
git clone https://github.com/yourusername/lost-found-api.git
cd lost-found-api
```

### **2️⃣ Create a Virtual Environment & Activate**

```sh
python -m venv venv
```

- **Mac/Linux:** `source venv/bin/activate`
- **Windows:** `venv\Scripts\activate`

### **3️⃣ Install Dependencies**

```sh
pip install django djangorestframework djangorestframework-simplejwt
```

### **4️⃣ Apply Migrations**

```sh
python manage.py makemigrations
python manage.py migrate
```

### **5️⃣ Create a Superuser (Optional)**

```sh
python manage.py createsuperuser
```

### **6️⃣ Run the Development Server**

```sh
python manage.py runserver
```

## 📌 API Endpoints

| Method     | Endpoint                 | Description                                       |
| ---------- | ------------------------ | ------------------------------------------------- |
| **POST**   | `/api/users/register/`   | Register a new user                               |
| **POST**   | `/api/users/login/`      | Login and get JWT token                           |
| **POST**   | `/api/lost-items/`       | Report a lost item                                |
| **POST**   | `/api/found-items/`      | Report a found item                               |
| **GET**    | `/api/lost-items/`       | Retrieve all lost items                           |
| **GET**    | `/api/found-items/`      | Retrieve all found items                          |
| **GET**    | `/api/match-items/`      | Match lost items with found items                 |
| **DELETE** | `/api/lost-items/{id}/`  | Remove a lost item (Replace `{id}` with item ID)  |
| **DELETE** | `/api/found-items/{id}/` | Remove a found item (Replace `{id}` with item ID) |

## 🔑 Authentication

This API uses **JWT authentication**.

1. **Register a user** using `/api/users/register/`
2. **Login** using `/api/users/login/` to get an `access` token.
3. **Use the Token** in Postman:
   - Add a **Header**: `Authorization: Bearer <your_token>`

## 📝 Project Structure

```
📂 lost_found_api
 ┣ 📂 lostfound
 ┃ ┣ 📄 models.py
 ┃ ┣ 📄 serializers.py
 ┃ ┣ 📄 views.py
 ┃ ┣ 📄 urls.py
 ┣ 📂 users
 ┃ ┣ 📄 models.py
 ┃ ┣ 📄 serializers.py
 ┃ ┣ 📄 views.py
 ┃ ┣ 📄 urls.py
 ┣ 📄 settings.py
 ┣ 📄 urls.py
 ┣ 📄 manage.py
```

## 🌟 Contributing

Feel free to fork this repository and submit pull requests.

## 📝 License

This project is licensed under the MIT License.

