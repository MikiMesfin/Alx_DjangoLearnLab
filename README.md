# Library Project

A Django-based library management system.

## Setup

1. Clone the repository

```bash
git clone <your-repo-url>
cd LibraryProject
```

2. Create and activate virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run migrations
```bash
python3 manage.py migrate
```

5. Create superuser (optional)
```bash
python3 manage.py createsuperuser
```

6. Run development server
```bash
python3 manage.py runserver
```

## Features
- Book management (CRUD operations)
- ISBN validation
- Publication year validation
- Search functionality
- Admin interface

## Testing
```bash
python3 manage.py test bookshelf.tests
```

## Initialize git and push
```bash
git init
git add .
git commit -m "Initial commit: Library Project setup"
git branch -M main
git remote add origin https://github.com/MikiMesfin/Alx_DjangoLearnLab.git
git push -u origin main
```

Make sure to:
1. Replace `https://github.com/MikiMesfin/Alx_DjangoLearnLab.git` with your actual GitHub repository URL
2. Review the files being committed (using `git status`)
3. Check that no sensitive information (like secret keys) is being pushed
4. Verify all tests pass before pushing

Would you like me to help you with any of these steps?
