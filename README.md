# Welcome to my Django Portfolio and Blog

If you would like to try this repository, clone it in your own computer (locally).
Once you've cloned the repository, you'll need to install all the requirements before you can run it in your computer.

## Installation Steps:

1. Make sure you are inside **Portfolio2022** directory.

2. If you type **ls** in your Terminal, you should see **manage.py** file. Then, go to next step.

3. Before we install our packages, create a virtual environment:
```
python3 -m venv venv
```

That should create a **venv** folder. You can double check by writing **ls** in your Terminal.

4. Now, activate your **venv** by writing:
```
source venv/bin/activate
```

You'll see that your Terminal changed to add **(venv)** at the beginning.

5. Now, install all everything on the **requirements.txt** file:
```
pip install -r requirements.txt
```

6. Finally, let's run migrations to create your DB:
```
python manage.py makemigrations
python manage.py migrate
```

7. Last step is to run your server so you can see it in port 8000 locally:
```
python manage.py runserver
```

## Have Any Improvements/Suggestions?

If you'd like to help me improve my Portfolio/Blog, feel free to collaborate.