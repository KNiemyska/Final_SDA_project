# Final_SDA_project
Django Blog

About

The idea was to build some basic bloggin platform. In future this blog will be transformed to platform for renting a climbing gear.
It was made using Python 3.8, Django and SQLite Database. For styling was used Bootstrap.
There is a Home page with Posts from all users. 

User can register and login. After login user:

* has access to profile page, where he can change username, email and change default profile image,
* can create post with describe of adding gear and add picture of a gear,
* can delete or update their gear post.

Every added gear has a detail page. 


Future assumptions:
* unittests,
* equipment rental,
* equipment can be booked,
* access to the location of the equipment (to the user who has currently rented the equipment - his contact details),
* page paginattion,
* contact page.

How to run

Clone This Project (Make Sure You Have Git Installed)

git@github.com:KNiemyska/Final_SDA_project.git


Install Dependencies

pip install -r requirements.txt

Set Database (Make Sure you are in directory same as manage.py)

python manage.py makemigrations
python manage.py migrate

Create SuperUser

python manage.py createsuperuser
