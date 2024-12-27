# Foodiwheels

Welcome to **Foodiwheels**, an online food ordering platform where you can explore a variety of cuisines, filter based on preferences, and make quick and easy purchases. This project is built using **Django** (backend) and **PostgreSQL** (database), with a vibrant and user-friendly interface for a delightful user experience.

## Features

- **User Authentication**:
  - Login and signup functionality.
  - Password reset support.
- **Homepage**:
  - Displays a variety of food items with descriptions.
  - Interactive purchase buttons for every item.
- **Filters**:
  - Filter options for vegetarian and other preferences.
- **Contact Page**:
  - Users can reach out for queries or feedback.

## Tech Stack

- **Frontend**:
  - HTML5, CSS3, Bootstrap
- **Backend**:
  - Django (Python)
- **Database**:
  - PostgreSQL

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/MohdRaza216/foodiwheels.git
   cd foodiwheels
   ```

2. Create a virtual environment:
   ```bash
   python -m venv myvenv
   source myvenv/bin/activate  # For Windows: myvenv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure the database:
   - Ensure PostgreSQL is installed and running.
   - Create a PostgreSQL database for the project.
   - Update the `DATABASES` section in `settings.py` with your credentials.

5. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```
   Visit `http://127.0.0.1:8000/` to view the website locally.

## Usage

- Browse food items on the homepage.
- Use the filter to view vegetarian or specific categories.
- Click on "Purchase" to add items to your cart.
- Use the contact page for any inquiries.

## Folder Structure

```
foodiwheels/
├── myweb/                 
│   ├── settings.py        
│   ├── urls.py            
│   └── ...
├── templates/             
│   ├── index.html         
│   ├── login.html         
│   └── ...
├── static/                
└── README.md              
```

## Contributing

Contributions are welcome! If you'd like to contribute:
- Fork the repository
- Create a new branch for your feature/fix: `git checkout -b feature-name`
- Commit your changes: `git commit -m 'Add some feature'`
- Push to the branch: `git push origin feature-name`
- Create a pull request

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any inquiries, feel free to reach out:
- Email: mohdrazamoghul2024@gmail.com
- GitHub: [MohdRaza216](https://github.com/MohdRaza216)

---

Thank you for visiting **Foodiwheels**! Bon appétit! 🍔🍟🍲

