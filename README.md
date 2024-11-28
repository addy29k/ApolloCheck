# HealthPlus-Visitor-Management-System
A Visitor Management Web App made using Django.

This is a simple web application which can be used for managing meetings and visitor details. It can keep track of all the meetings and can send emails and sms to host and visitor about their meeting details.

Being a web application **It also serves as an organisation's official website** where other people can visit and get more information about the organisation.

#### This project is made by keeping a healthcare organisation in mind. Though it can be modified for any organisation.

#### Why i made it organisation specific?
Well !, as it also acts as an organisation's official website, so i took an example organisation. Also, its always better to explain with examples : )




## Features
- Works as both, Official website and Visitor management system.
- Simple and easy to use GUI.
- Faster load speeds (thanks to Django!).
- Password secured Visitor management dashboard.
- Descriptive dashboard that shows all hosts with their images, details and status.
- Keeps track of all meetings and respective visitor details.
- Emails and SMS notification to both visitor and Host.
- Secure and Easy to **ADD, DELETE or EDIT a Host profile**.



count email id'
    ```
    
- Now go inside the main folder which was cloned (manage.py file will be present there), now open a terminal in that directory and run follwing commands:
    ```
    python manage.py createsuperuser
    # follow further instruction there
    
    - After super user is created 
    python manage.py makemigrations
    python manage.py migrate
    
    python manage.py runserver
    ```
- Now server will start at - http://127.0.0.1:8000/

### Credits :
- HTML mail templates are made on <a href="https://beefree.io/">beefree.io</a>

## Want to contribute or found any bug ?
- Make sure you raise an issue if you find any error or bug.
- If you want to add any feature or want to fix any issue, please make a pull request.
- Contact me at my mail id - shubhamkumar8180323@gmail.com - for any kind of help.

#### Made with ♥ by `Shubham Kumar`
