# Social Media App (Work in Progress) 📱

Building a Django-based social media platform where users can create profiles, post updates, and interact with others.

## Current Progress
- User authentication and profiles implemented
- Basic post creation and feed functionality
- Database models set up (PostgreSQL ready)
- Frontend templates started

## Planned Features
- Like and comment system
- Follow functionality
- Responsive design
- REST API endpoints (DRF)

## 🛠 Tech Stack
- Django + Python
- PostgreSQL
- HTML, CSS, JavaScript (Bootstrap)

## Progress
## Demo Video

<video src="https://github.com/castle-dot/social-media/raw/main/demo_video.mp4" controls></video>

## How to Run Locally
```bash
git clone https://github.com/castle-dot/social-media.git
cd social-media
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
