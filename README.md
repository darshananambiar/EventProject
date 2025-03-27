# Event Scheduler

A dynamic event scheduling system built with Django and Tailwind CSS.

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install Tailwind CSS:
```bash
python manage.py tailwind install
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

6. In a separate terminal, start Tailwind CSS build process:
```bash
python manage.py tailwind start
```

## Features

- Create and manage events with multiple sessions
- Speaker management
- Conflict-free scheduling
- Interactive UI with responsive design
- Real-time schedule optimization 