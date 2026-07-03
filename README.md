📱 Social Media Sandbox

Welcome to the repo! I built this project primarily as a portfolio piece to deepen my understanding of backend architecture, but it quickly evolved into a fun, private sandbox for my friends and me to share updates, terrible memes, and videos.

This isn't just another generic tutorial clone; it features custom logic for mixed-media feeds (handling text-only Twitter-style posts, image galleries, and HTML5 video players dynamically) without relying on heavy external APIs. Everything is rendered beautifully right from the server.
✨ What's Inside?

    Smart Media Feeds: The feed automatically adapts its layout depending on what you post. Text-only posts get a bold, Twitter-style layout, while media posts render sleek image lightboxes or native video players.

    Robust File Handling: Custom logic to separate, validate, and serve user-uploaded images and videos securely.

    The Essentials: User authentication, profiles, dynamic likes, and commenting functionality.

🛠️ The Tech Stack

    Backend: Python & Django

    Database: Django ORM & SQLite (keeping it lightweight and portable!)

    Frontend: HTML5, CSS3, Vanilla JavaScript, and UIkit for the responsive layouts and drop-downs.

    Architecture: Traditional Server-Side Rendering (SSR). No messy third-party APIs here—just clean, native Django template tags doing the heavy lifting.

🚀 Getting Started (Local Setup)

Want to spin this up on your own machine? It’s super straightforward. Follow these steps to get your local server running.

1. Clone the repository
Bash

git clone https://github.com/castle-dot/social-media.git
cd social-media

2. Set up your virtual environment
It is always best to keep your dependencies isolated.
Bash

# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate

3. Install dependencies
(Note: Make sure you have Django and Pillow installed for image handling!)
Bash

pip install -r requirements.txt

4. Run database migrations
This sets up the SQLite database and creates the necessary tables for Users, Posts, etc.
Bash

python manage.py makemigrations
python manage.py migrate

5. Create a Superuser (Optional but recommended)
If you want to access the Django Admin panel to manage posts and users:
Bash

python manage.py createsuperuser

6. Fire it up!
Bash

python manage.py runserver

Navigate to http://127.0.0.1:8000 in your browser, create an account, and start posting!
💡 What I Learned

Building this pushed me to solve real-world problems like handling "orphaned" database records, conditionally rendering front-end UI based on complex backend data states, and managing media files safely in a local environment.
🤝 Contributing

Since this is a personal portfolio piece and a playground for my friends, I'm not actively looking for major pull requests. However, if you spot a bug or have a cool idea for a feature, feel free to open an issue!
