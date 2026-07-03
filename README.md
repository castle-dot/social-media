# 📱 Social Media Sandbox

Welcome to the repo!

I built this project primarily as a portfolio piece to deepen my understanding of backend architecture, but it quickly evolved into a fun, private sandbox for me and my friends to share updates, terrible memes, and videos.

This isn't just another tutorial clone — it features custom logic for mixed-media feeds (handling text-only Twitter-style posts, image galleries, and HTML5 video players dynamically) without relying on heavy external APIs. Everything is rendered beautifully right from the server.

---

## ✨ What's Inside?

### 🧠 Smart Media Feeds
The feed automatically adapts its layout depending on what you post:
- Text-only posts → clean Twitter-style layout  
- Image posts → responsive lightbox gallery  
- Video posts → native HTML5 video player support  

---

### 📦 Robust File Handling
Custom logic for:
- Separating image/video uploads
- Validating media types
- Securely serving user-uploaded files

---

### 🔑 Core Features
- User authentication system
- User profiles
- Follow system (followers/following)
- Likes and comments
- Dynamic post rendering

---

## 🛠️ Tech Stack

- **Backend:** Python, Django  
- **Database:** SQLite (via Django ORM)  
- **Frontend:** HTML5, CSS3, Vanilla JavaScript, UIkit  
- **Architecture:** Server-Side Rendering (SSR)

No external APIs — just pure Django template rendering and backend logic.

---

## 🚀 Getting Started (Local Setup)

### 1. Clone the repository
```bash
git clone https://github.com/castle-dot/social-media.git
cd social-media

2. Create virtual environment

Windows

python -m venv venv
venv\Scripts\activate

Mac / Linux

python3 -m venv venv
source venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
4. Run migrations
python manage.py makemigrations
python manage.py migrate
5. Create superuser (optional)
python manage.py createsuperuser
6. Run server
python manage.py runserver

Open:

http://127.0.0.1:8000
📸 Screenshots

Replace these with your actual images inside a /screenshots folder.

🏠 Feed Page

👤 Profile Page

➕ Create Post

❤️ Like & Comment System

💡 What I Learned

Building this project pushed me to understand:

Handling relational database edge cases (like orphaned profiles)
Dynamic UI rendering based on backend state
Secure media upload handling in Django
Structuring a full-stack Django application without external APIs
🤝 Contributing

This is mainly a personal portfolio project and sandbox for experimentation.

However, if you:

Find bugs 🐛
Have feature ideas 💡
Or improvements 🚀

Feel free to open an issue or discussion.

⭐ Final Note

This project is part of my learning journey as I grow into backend development and system design using Django.


---

## 📁 Screenshot setup (important)

Create this in your repo:


/screenshots
feed.png
profile.png
create_post.png
interactions.png


Then GitHub will automatically render them.

---

If you want next level polish, I can also help you:
- add a **GitHub banner image**
- make a **demo GIF of the feed scrolling**
- or write a **“portfolio version” README (more recruiter-focused, less casual)**
