# HealthPlus-Visitor-Management-System
A Visitor Management Web App made using Django.

This is a simple web application which can be used for managing meetings and visitor details. It can keep track of all the meetings and can send emails and sms to host and visitor about their meeting details.

Being a web application **It also serves as an organisation's official website** where other people can visit and get more information about the organisation.

#### This project is made by keeping a healthcare organisation in mind. Though it can be modified for any organisation.

#### Why i made it organisation specific?
Well !, as it also acts as an organisation's official website, so i took an example organisation. Also, its always better to explain with examples : )

## Visit deployed website
- Deployed on pythonanywhere : http://healthplus.pythonanywhere.com/


## Features
- Works as both, Official website and Visitor management system.
- Simple and easy to use GUI.
- Faster load speeds (thanks to Django!).
- Password secured Visitor management dashboard.
- Descriptive dashboard that shows all hosts with their images, details and status.
- Keeps track of all meetings and respective visitor details.
- Emails and SMS notification to both visitor and Host.
- Secure and Easy to **ADD, DELETE or EDIT a Host profile**.

## Solution Workflow
- Let a visitor wants to meet a host, he goes to office and checks for that Host on the Dashboard Screen installed for visitors. Dashboard shows information of all Hosts with their current status.
- If the Host is **BUSY** it shows the current visitor details. And if the host is **FREE**, an 'Arrange Meeting' button is shown.
- Visitor clicks on that arrange meeting button and a 'Meeting Form' is opened, visitor fills his/her details in that form and clicks on Check-In button.
- As the Check-In button is clicked, an Email with all deatils of visitor and a Check-out button for that visitor is sent to Host. A SMS is also sent to Host about Visitor's details. Status of the Host is changed to **BUSY** on the dashboard. 
- After the meeting is over, the visitor leaves the office and Host clicks on that 'Check-out' button given inside the mail. As soon as it is clicked, the Host's status is set as **FREE** again and Checkout time is recorded for that meeting. An Email with all the meeting details is sent to the visitor's Email Id.
- Dashboard refreshes itself automatically after 20 seconds and Host is again seen as **FREE** on the dasboard.

## Local Machine development setup
- Clone the repository on your machine 
    ```
    git clone https://github.com/shubhamkumar27/Summergeeks-Visitor-Management-System.git
    ```
    
- Install all dependencies by executing the following command:
    ```
    pip install -r requirements.txt
    ```
    
- You need to make some changes to the settings.py file inside visitor_management folder, go to bottom of the file
    ```
    UPDATE : EMAIL_HOST_USER = "your email id" 
    UPDATE : EMAIL_HOST_PASSWORD = "your email id password"
    ```
    ( Make sure you <a href='https://myaccount.google.com/lesssecureapps'>enable less secure apps</a> in your google account, so that it sends email ! )
   
- Now you need to edit some lines in views.py file inside accounts folder
  - INSIDE email function:
    ```
    UPDATE : sender = 'your email id'
    ```
  - GO to <a href='https://www.way2sms.com/'>way2sms</a>, create your account and genetrate your test apikey and secret key. Now go INSIDE sendsms function:
    ```
    UPDATE : 'apikey':'your api key',
    UPDATE : 'secret':'your secret key',
    UPDATE : 'senderid' : 'your way2sms account email id'
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
