# Estetist
This is my first project using Python/Django, HTML/CSS, JS and Docker - Website for a cosmetologist who selects cosmetics for customers. I created it to get a diploma from Beetroot Academy in a field of Python Development. It is pet-project, so it is not ready for production. It consist of main like-landing page, form for clients, 
blog with comments, search using postgres tools, translation (ru/uk) and other features like cache and celery for asynchronous sending of emails.

To run code you need docker to be preinstalled.
1. Create .env file inside 'mysite/mysite' directory and add following lines:
  SECRET_KEY = your key with 50 characters length;<br>
  DEBUG = True;<br>
  USER = fill with you data;<br>
  PASSWORD = fill with your data;<br>
  EMAIL_HOST_PASSWORD = fill with your data and change EMAIL_HOST_USER in settings.py or specify EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend';<br>
  GOOGLE_RECAPTCHA_SITE_KEY = fill with your data or delete this line, so captcha will not work in client form;<br>
  GOOGLE_RECAPTCHA_SECRET_KEY = fill with your data or delete this line, so captcha will not work in client form;<br>
  POSTGRES_USER = fill with your data;<br>
  POSTGRES_PASSWORD = fill with your data;<br>
  POSTGRES_DB = fill with your data;<br>
2. Run docker-compose up command;
3. Open in browser http://127.0.0.1:8000/.
