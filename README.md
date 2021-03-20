This project was created to display a dashboard that a user can filter infomation based upon NBA team to see which players actually performed the best or worst during the 2018-2019 NBA season.  For our purposes, we created the following visuals:
  - Pie Chart to display the variability of minutes played for all players per team
  - Scatter Plot to map out each players' Value Over Replacement Player (VORP) vs Usage Rate (USG%).  Here, we wanted to answer the question "Is a player more valuable the more they handle the basketball?"
  - Scatter Plot to map out each players' Turnover Percentage (TO%) vs Usage Rate (USG%).  Here, we wanteed to answer the question "Do players tend to turnover the basketball more the more often they have the ball?"

Steps:
 - Using BeautifulSoup, we scraped Basketball Reference's advanced states webpage for the 2018-2019 NBA season.
 - Using Pandas, we cleaned our data to display only the descriptions for each player and the stats we wanted to identify.
 - After cleaning, we imported our data into a SQL database for easier access
 - After creating a dashboard via HTM and CSS, we used SQLAlchemy and Javascript to create a dropdown menu to dispay all 30 NBA teams and create our three charts based upon a team's information.
 - A Flask app was created so all functions run smoothly together to dispay our working dashboard.

Visual Examples:

![newplot](https://user-images.githubusercontent.com/23372412/111882809-fb090b00-898d-11eb-8d4e-43110839ffaf.png)
![newplot (1)](https://user-images.githubusercontent.com/23372412/111882830-1116cb80-898e-11eb-83f9-c7e1d9b9b44c.png)
![newplot (2)](https://user-images.githubusercontent.com/23372412/111882832-170cac80-898e-11eb-9c77-3095095a17b6.png)
