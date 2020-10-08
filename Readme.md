Please ensure you have celery and a broker installed and that it is running 
for the email messaging

Start celery worker:

*celery -A ClinomicTest worker -l info -P threads*

the -l is a lowercase L not an I

Please create a credentials.py file under ClinomicTest and enter:

email = {your email address} \
password = {your email password}

this project uses google smtp for it's email messaging.\
You can change the settings under ClinomicTest.settings.py

Ensure that you have made migrations for the database and migrated the models \
Make migrations :

*python manage.py makemigrations todoapi / reminder*

Migrate models and create database :

*python manage.py migrate*

Ensure that you have the credentials to access the website \
You can do that by creating your own user or logging in if you already have one :

*python manage.py createsuperuser*

Once you have everything setup you can start the server:

*python manage.py runserver*

You can use the interface to navigate through the boards, todos and reminders. \
Use the url provided to get more details and edit specific items you want to change.