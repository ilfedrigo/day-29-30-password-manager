# Password Manager

For days 29 and 30 of my 100 days of programming in Python, I enhanced an old application I had created for generating and managing passwords.

This simple password manager application is built using Python's Tkinter library. It allows users to generate secure passwords, save them along with website details, and retrieve saved passwords when needed. 

The application utilizes a graphical user interface (GUI) for ease of use.

## Features

### Password Generator

The "Generate Password" button triggers a password generation function. The generated password consists of a mix of letters (both uppercase and lowercase), numbers, and symbols to enhance security.

### Save Password

Users can input website details (name, email/username, and password) and save them by clicking the "Add" button. The information is stored in a JSON file named "password.json."

### Search Password

The "Search" button enables users to search for saved passwords by entering the website's name. If the website is found in the database, the associated email/username and password are displayed.

## Usage

1. Run the script.
2. Enter website details (name, email/username, and password).
3. Click "Generate Password" to create a strong password.
4. Click "Add" to save the website details.
5. To retrieve a password, enter the website name and click "Search."

**Note:** Ensure that the "logo.png" file is present in the same directory as the script.

Feel free to customize and enhance the application based on your needs!
