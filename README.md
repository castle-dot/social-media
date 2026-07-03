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
<img width="1918" height="979" alt="Screenshot 2026-07-02 110034" src="https://github.com/user-attachments/assets/fe94eb04-d787-43de-b57c-07c9da14fce5" />
<img width="1920" height="986" alt="Screenshot (176)" src="https://github.com/user-attachments/assets/f7194968-221e-4ad8-92ce-c7b909c27f57" />



## How to Run Locally
```bash
git clone https://github.com/castle-dot/social-media.git
cd social-media
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
