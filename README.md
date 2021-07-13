# Microsoft-Teams-Clone-Submission | Avil Goel | Netaji Subhas University of Technology | Engage 2021

For running the project on the local machine ( http://127.0.0.1:8000/ ) , follow the given steps:  

1. Open the terminal in your code editor, and enter the command:    
**git clone https://github.com/avilgoel/Microsoft-Teams-Clone-Submission.git**

2. After the cloning of the repository is done, switch the directory to _Microsoft-Teams-Clone-Submission_ by entering:    
**cd Microsoft-Teams-Clone-Submission**

3. Now, install all the modules for the project using:  
**pip install -r requirements.txt**

4. Finally, run the server by entering:  
**python manage.py runserver**

5. This will run the website on the local machine URL- http://127.0.0.1:8000/       

**Video Demo Link:** https://www.youtube.com/watch?v=0usK6DNnAzw   
**Presentation Link:** https://drive.google.com/file/d/1Y9pa...     

**Scrum** methodology under **Agile** framework has been used for developing this project. It relies on incremental development, with each iteration consisting of half-week sprints, where each sprint’s goal is to build the most important feature (mandatory functionality) first and come out with a potentially deliverable product. More features are built into the project in subsequent sprints and are adjusted based on the Microsoft Mentor feedback between sprints.

The project offers six major functionalities:  

**1. Video Conferencing**  
This functionality allows multiple participants to communicate simultaneously, and also enables a single participant to join multiple calls concurrently in different virtual rooms, hence leading to better collaboration and effective exchange of information. For adding real-time communication capabilities, _WebRTC_ has been used due to its cross-platform support, reliable session establishment as well as interoperability. Initiating rooms is achieved through _Web Sockets via Django channels_ because it provides a persistent, low-latency, full-duplex connection and has an active developer community. 

![Screenshot 2021-07-12 12 52 08](https://user-images.githubusercontent.com/70324375/125248730-0ce23580-e312-11eb-8562-60b9a4a81e9f.png)
![Screenshot 2021-07-12 13 03 49](https://user-images.githubusercontent.com/70324375/125248742-11a6e980-e312-11eb-818d-d1cae534761b.png)


**2. Authentication**  
This feature aims to ensure security and privacy for all users. It provides ease-of-use through conventional login/sign-up as well as _Google OAuth_ feature, with _Google captcha_ providing an additional blanket of protection for the user.  

![Screenshot 2021-07-12 12 48 17](https://user-images.githubusercontent.com/70324375/125247061-271b1400-e310-11eb-8e46-fb13eba3efff.png)
![Screenshot 2021-07-12 12 49 16](https://user-images.githubusercontent.com/70324375/125249039-677b9180-e312-11eb-99ff-8987c2494eee.png)

**3. Transcript**  
This functionality aims to ensure accessibility for all. This feature uses _Google Speech-to-Text API_ to produce a meeting transcript, especially beneficial for people with auditory disabilities. It yields high degrees of convenience for participants who might have missed the meeting, by storing the transcripts and making them available for future use. For visually impaired people, the app delivers the option of reading the transcript out loud by an automated voice.       

![Screenshot 2021-07-12 12 57 11](https://user-images.githubusercontent.com/70324375/125249367-ca6d2880-e312-11eb-9f4e-be300ba95ab1.png)
![Screenshot 2021-07-12 13 15 22](https://user-images.githubusercontent.com/70324375/125249982-6434d580-e313-11eb-95d3-273ac156280a.png)

**4. Chat**  
The application provides persistent one-on-one as well as group chat, storing it in _SQLite Database_, and hence making it accessible before, during and after the meeting. The group chat section also displays a list of all the active participants. The one-on-one chat has been implemented using _Web Sockets via Django Channels_.  

![Screenshot 2021-07-12 13 31 01](https://user-images.githubusercontent.com/70324375/125251954-79aaff00-e315-11eb-89b2-d006c190597c.png)
![Screenshot 2021-07-12 13 35 33](https://user-images.githubusercontent.com/70324375/125252654-3d2bd300-e316-11eb-8862-5a2d468f7459.png)

**5. Video and Mic ON/OFF**   
The camera and mic toggle functionalities contribute to the usability of the application, since people might not be comfortable switching on their cameras at all times. 

![Screenshot 2021-07-12 13 38 26](https://user-images.githubusercontent.com/70324375/125252996-91cf4e00-e316-11eb-90a9-8d281fec457a.png)

**6. Invite Users**
The invite feature allows a user to share the meeting link directly through _email_ or _WhatsApp_ to fellow participants, hence furthering the extensibility of the project.  

![Screenshot 2021-07-12 13 41 17](https://user-images.githubusercontent.com/70324375/125253380-f9859900-e316-11eb-8d44-869cc5291121.png)
![Screenshot 2021-07-12 13 52 13](https://user-images.githubusercontent.com/70324375/125254786-6cdbda80-e318-11eb-9747-9b31ebae6ff0.png)











