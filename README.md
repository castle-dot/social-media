# 📱 Social Media Sandbox

Welcome to the repo! I built this project primarily as a portfolio piece to deepen my understanding of backend architecture, but it quickly evolved into a fun, private sandbox for my friends and me to share updates, terrible memes, and videos. 

This isn't just another generic tutorial clone; it features custom logic for mixed-media feeds (handling text-only Twitter-style posts, image galleries, and HTML5 video players dynamically) without relying on heavy external APIs. Everything is rendered beautifully right from the server.

### ✨ What's Inside?
* **Smart Media Feeds:** The feed automatically adapts its layout depending on what you post. Text-only posts get a bold, Twitter-style layout, while media posts render sleek image lightboxes or native video players.
* **Robust File Handling:** Custom logic to separate, validate, and serve user-uploaded images and videos securely.
* **The Essentials:** User authentication, profiles, dynamic likes, and commenting functionality.

### 🛠️ The Tech Stack
* **Backend:** Python & Django
* **Database:** Django ORM & SQLite (keeping it lightweight and portable!)
* **Frontend:** HTML5, CSS3, Vanilla JavaScript, and UIkit for the responsive layouts and drop-downs. 
* **Architecture:** Traditional Server-Side Rendering (SSR). No messy third-party APIs here—just clean, native Django template tags doing the heavy lifting.

---

### 🚀 Getting Started (Local Setup)

Want to spin this up on your own machine? It’s super straightforward. Follow these steps to get your local server running.

**1. Clone the repository**
```bash
git clone [https://github.com/castle-dot/social-media.git](https://github.com/castle-dot/social-media.git)
cd social-media
