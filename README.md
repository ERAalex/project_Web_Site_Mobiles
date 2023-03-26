
#### E.R.A. - Espinosa Rozov Alexander - python developer.
# Project - Mobile Online Shop

<img src="https://github.com/ERAalex/ERA_Fast_API_course_money/blob/main/api_money_im.webp">
<p>
  <a href="https://www.linkedin.com/in/alexander-espinosa-rozov-b3b270121/"><img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white"></a>
</p>

<br><a href="mailto:erapyth@gmail.com"><img src="https://img.shields.io/badge/-Gmail%20contact%20me-red"></a>
<br><a href="https://t.me/espinosa_python"><img src="https://img.shields.io/badge/-Telegram-blue"></a>

## About the project.

  <a href="#" target="_blank" rel="noreferrer nofollow">
      <img src="https://github.com/ERAalex/PREVIEW_project_site_buisness_card_Maria-/blob/main/website_icons.jpg" >
    </a>

This application is a Fast Api server with the ability to provide the exchange rate of coins on any date. The main idea: <br>

1. FAST API Server.<br>
- use API of https://cbr.ru/development/SXML/ to get new information about exchange rate of coins.<br>
- Check information in database - Mongo DB.<br>
- Save new information on Mongo Db database.<br>

you can make a request  http://127.0.0.1:8000/coin/GBP   where GBP - is a coin of England

2. Vue JS.<br>
- the user can write the name of coin and get information from our Fast Api Server.<br><br>


3. Ready Dockerfile and Docker-compose.yml to RUN Containers.<br> Just type the command: docker-compose up
Container for app + Container for MongoDB <br><br>


Interesting points about API of SBR:<br>
- All information from https://cbr.ru/development/SXML/ we recive not in JSON but as XML so we need to use - import xmltodict as xmltodict <br>
<br>

Intresting points about Mongo db to JSON:<br>
- When we try to pass Mongo Db information as JSON response in Fast API we can recieve problem with '_ id' because it is not just field like int or str, so Fast Api can't serialize this field, the opcion is not use this field, just skip it like: <br>
find_item = collection_name.find_one({'date': f'{date}'}, {'_id': 0}).


RESOLVED  Problem.
When we try make a API request from Vue JS to localhost Fast Api you can get this error: <br>
- fast api from origin 'null' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' <br><br>

You can do:<br>

from fastapi.middleware.cors import CORSMiddleware <br><br>
and add: <br>

origins = ["*"] <br>

app.add_middleware(<br>
    CORSMiddleware,<br>
    allow_origins=origins,<br>
    allow_credentials=True,<br>
    allow_methods=["*"],<br>
    allow_headers=["*"],<br>
)<br>


<br>

## Technologies
Main:<br/>
[![SkillIcons](https://skillicons.dev/icons?i=python)](https://skillicons.dev) PYTHON - REST FRAMEWORK <br/>

Main:<br/>
[![SkillIcons](https://skillicons.dev/icons?i=vue)](https://skillicons.dev) VUE JS <br/>

DATABASES:<br/>
[![SkillIcons](https://skillicons.dev/icons?i=mongo)](https://skillicons.dev) Mongo DB <br/>

Additional tech:<br/>
[![SkillIcons](https://skillicons.dev/icons?i=git)](https://skillicons.dev) GIT <br/>
[![SkillIcons](https://skillicons.dev/icons?i=linux)](https://skillicons.dev) Linux <br/><br/>

[![SkillIcons](https://skillicons.dev/icons?i=html)](https://skillicons.dev) HTML <br/>
[![SkillIcons](https://skillicons.dev/icons?i=css)](https://skillicons.dev) CSS <br/>
<br/><br/>

## The most important projects:
1. <p><a href="https://itespinosa.com/" target="_blank">➡️ Check out my website. You can find a detailed description of the projects</a></p>
2. <p><a href="https://github.com/ERAalex/PREVIEW_project_site_buisness_card_Maria-">➡️ Сommercial project. Flask project. Foreign language teacher website. </a><a href="https://espinosamaria.ru/"> - See on-line website.</a></p>
4. <p><a href="https://github.com/ERAalex/PREVIEW_project_Online_it_school">➡️ Сommercial project. Django project. Online School with personal classrooms of students and teachers.  </a><a href="https://edu.gym205.ru/"> - See online website.</a></p>
5. <p><a href="https://github.com/ERAalex/PREVIEW_project_205_kafedra_website">➡️ Сommercial project. Django project. For goverment school № 205. </a><a href="http://school.gym205.ru/"> - See on-line website.</a></p>
6. <p><a href="https://github.com/ERAalex/project_Web_Site_Mobiles">➡️ Django project Mobile shop, education purpose. Working on it</a></p>
7. <p><a href="https://github.com/ERAalex/Netology_Collective_work">➡️ Collective work. Education purpose. VK-bot</a></p>
8. <p><a href="#">➡️ Control pass, education purpose. Working on it</a></p>
9. <p><a href="https://telegram.me/simon_esp_bot">➡️ Online-school. Telegram Bot (aiogram). Done. You can see it on Telegram @simon_esp_bot. To start print /start and /menu</a></p>





<br/>


<h2>GitHub Stats</h2>

<a href="#">![Github stats](https://github-readme-stats.vercel.app/api?username=ERAalex&theme=blueberry&count_private=true&hide_border=true&line_height=20)</a>
<a href="#">![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=ERAalex&layout=compact&theme=blueberry&count_private=true&hide_border=true)</a>
