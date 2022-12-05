# :monocle_face: Estetist :monocle_face:
<h2> Project description </h2>
This is my first project using Python/Django, HTML/CSS, JS and Docker - Fully featured website for a cosmetologist who selects cosmetics for customers. It is a pet-project, so it is not ready for production. 

## <h2>:bookmark_tabs: Features</h2>
* Main like-landing page
* Form for clients
* Blog with comment system
* Search system for blog
* Translation (ru/uk)
* Cache
* Asynchronous sending of emails

## <h2>Technologies</h2>
* Python 3
* Django 4
* JS ES7
* HTML, CSS
* Celery
* Docker
* Postgres 
* Redis

## <h2>:bomb:Instructions for launching the project:bomb:</h2>
<h4>To run this project locally, follow these steps:</h4>
1️⃣ You should install <a href="https://docs.docker.com/get-docker/">Docker</a>

2️⃣ Clone this project
```bash
git clone https://github.com/PavloPolovyi/Estetist
```

3️⃣ Create .env file inside 'mysite/mysite' directory and add following lines:

  SECRET_KEY = your key with 50 characters length
  
  DEBUG = True
  
  USER = fill with you data
  
  PASSWORD = fill with your data
  
  EMAIL_HOST_PASSWORD = fill with your data and change EMAIL_HOST_USER in settings.py or specify EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
  
  GOOGLE_RECAPTCHA_SITE_KEY = fill with your data or delete this line, so captcha will not work in client form
  
  GOOGLE_RECAPTCHA_SECRET_KEY = fill with your data or delete this line, so captcha will not work in client form
  
  POSTGRES_USER = fill with your data
  
  POSTGRES_PASSWORD = fill with your data
  
  POSTGRES_DB = fill with your data
  
  
4️⃣ Run following command:
```bash
docker compose up
```

5️⃣ Open in browser <a href="http://http://localhost:8080/">localhost:8080</a>
