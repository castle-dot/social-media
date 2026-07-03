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
