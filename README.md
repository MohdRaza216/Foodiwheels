# **Foodiwheels**

Welcome to **Foodiwheels** — an exciting online food ordering platform designed to offer a variety of cuisines at your fingertips. Whether you're looking for a quick bite or planning a feast, Foodiwheels provides a seamless experience for browsing, filtering, and purchasing food items. 

Built with **Django** for the backend and **PostgreSQL** for the database, this project ensures a fast, reliable, and delightful user experience. 

---

## **Key Features**

- **User Authentication**
  - Easy login and signup process.
  - Password reset functionality for secure access.
  
- **Homepage**
  - A visually rich homepage displaying a variety of food items with descriptions.
  - Dynamic and interactive purchase buttons for food items.

- **Filter Options**
  - Filter by preferences (e.g., vegetarian, vegan, etc.) to help users find what suits their needs.

- **Contact Page**
  - A page dedicated to user queries and feedback.

- **User Profile**
  - Users can manage their profiles, including updating their profile picture.

---

## **Tech Stack**

### **Frontend:**
- HTML5
- CSS3
- Bootstrap

### **Backend:**
- Django (Python)

### **Database:**
- PostgreSQL

### **Hosting:**
- **Frontend & Backend**: Vercel

---

## **Deployment**

Foodiwheels is live! Visit the website here:  
👉 **[Foodiwheels on Vercel](https://foodiwheels.vercel.app/)**

---

## **Installation and Setup**

Follow the steps below to get the project running locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/MohdRaza216/foodiwheels.git
   cd foodiwheels
   ```

2. **Create and activate a virtual environment**:
   - For Linux/MacOS:
     ```bash
     python -m venv myvenv
     source myvenv/bin/activate
     ```
   - For Windows:
     ```bash
     python -m venv myvenv
     myvenv\Scripts\activate
     ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the PostgreSQL database**:
   - Ensure PostgreSQL is installed and running on your machine.
   - Create a database for the project in PostgreSQL.
   - Update the `DATABASES` section in `settings.py` with your database credentials.

5. **Apply database migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Start the development server**:
   ```bash
   python manage.py runserver
   ```
   - Visit the application at: `http://127.0.0.1:8000/` to view it locally.

---

## **Usage**

- **Browse food items** on the homepage, which showcases a variety of cuisines.
- **Filter** food items based on dietary preferences (e.g., vegetarian, vegan, etc.).
- **Click on "Purchase"** to add items to your cart for easy checkout.
- **Contact page** for any questions or feedback regarding the platform.
- **Profile management**: Users can update their profiles and change their profile pictures.

---

## **Folder Structure**

Here is an overview of the main folder structure of the project:

```
foodiwheels/
├── myweb/                 # Core Django app files
│   ├── settings.py        # Configuration settings
│   ├── urls.py            # URL routing
│   └── ...
├── templates/             # HTML templates
│   ├── index.html         # Homepage
│   ├── login.html         # User login page
│   └── ...
├── static/                # Static files (CSS, images, JS)
└── README.md              # Project documentation
```

---

## **Contributing**

We welcome contributions to **Foodiwheels**. To contribute:

1. Fork the repository.
2. Create a new branch for your feature/bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m 'Add feature or fix bug'
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Create a pull request with a clear description of your changes.

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## **Contact**

For any inquiries or feedback, feel free to reach out:

- **Email**: [mohdrazamoghul2024@gmail.com](mailto:mohdrazamoghul2024@gmail.com)
- **GitHub**: [MohdRaza216](https://github.com/MohdRaza216)

---

Thank you for visiting **Foodiwheels**! 🍔🍟🍲 Enjoy your meal and happy ordering!
