# Cattle+
### Disruptive solutions for enterprise problems
###### A fictional software company

#### About us & the Problem
- We are a group of PUCRS students and we were challenged to create a fictitious software company to solve a problem of a real company. We are a group of 5 students:
  - Augusto Sopelsa Klaic (@AugustoKlaic)
  - Diovane Monteiro
  - Nei Cardoso
  - Henrique Marques
  - Nicolas Curco
  
- We came up with the company **CATTLE+**, we are focus to solve the problem that Vakinha bring to us, that is basically take the information they already have and filter and trsnform that in a more valueable information.

#### Our solution
 - After receiving the proposal we thought about using the info they have and help the users of the web site Vakinha, making the usage and the understanding more easy from the user perspective. Our solution is focused in give power and control to the users over their crowd funding proposals.
 
***The group proposed the following:***
  1. Develop and deliver a backend solution in pyhton;
  2. Using micro-services to facilitate the integration in Vakinha architecture;
  3. Cloud hostage;
  4. User oriented solution;
  
#### Planned Architecture sketch:
![First Architeture sketch(04/19/2019)](https://github.com/AugustoKlaic/IntegradoraII/blob/master/miscelaneous/Arch_prototype.PNG)

#### Actual Architecture:
  -> TO DO

#### How to see DataBase Structure & Infos:
  1. Git clone the project or with you already have cloned just pull the modifications;
  2. Go to the folder that you saved the changes or pulled the changes;
  3. Open/run the index.html file with a browser to navigate through the databse Info;
  
#### DataBase development
  - We received an entire dump file from vakinha to use it as datasource for our software solution. We treat the database as a priority because it might be the most important part to Vakinha. So we focus in solve all databases problems first, and we had some:
  1. How to send the dump file to the AWS EC2 linux;
  2. How we create the database from the dump;
  3. The dump came up with all users from vakinha;
  
- After solving all of this we had setted the databse full operational, and started the development of the SQL scripts:
    <p> Our DBA report: </p>
      First of all, i would like to say that it was a new and different experience having to work with a PostgreSQL database. It was kind hard at some point because i was used to work with SQL Server and Oracle databases, so i had to learn a new type of SQL, the base was similar but with its own universe of writing.
      So we begun to code the SQL scripts, we had to know what our aplicatiom would do, so i had to have a conversation with de developement team and we came to a consensus on what we were going to return from the database. Below are some of the queries we have made.
    
 ##### Showing the remote DB:
 ![example1](https://github.com/AugustoKlaic/IntegradoraII/blob/master/miscelaneous/users_and_tables.png)
 ![example2](https://github.com/AugustoKlaic/IntegradoraII/blob/master/miscelaneous/teste_select1.png)
 
#### API's development
  - After we solved the Database we started developing our solution in python. We made out five endpoints to return the information in JSON format. We choose JSON because it is the most popular nowadays and it is easy to see, understand and map into objects to be used before. The JSON is reusable and we tought it could be the most valuable feature that Vakinha could use with the SQLs scripts. 
  <p>Our devs report: </p>
 
![example3](https://github.com/AugustoKlaic/IntegradoraII/blob/master/miscelaneous/dev_example1.png)

#### Sprints overview Abstract
###### Sprint 1
  - In the first sprint we made a mockup of how our system would look like. We model the interface with the information we thougt would aggregate value to the user. We put some graphics and links just to ilustrate what kind of iformation we wanted. We, from the beginning, have proposed a solution focused in backend, with almost nothing related to frontend. Because we wanted to deliver inteligence to the core business of Vakinha and let them make up the user interface with them UX, UI, design and templates.
  
###### Sprint 2
  - In second sprint we started the database, and focus to resolve it's problems. We created an AWS EC2 cloud to host the database. We use a framework open source to map and classify all the database for us to facilitate our work and the development of the SQL scripts.
  
###### Sprint 3
  - In third sprint we develop all the SQL queries that would return the info from the database, we were already using real data from the vakinha at this point. And started the development of the API's that use those scripts. At this point we hadn't made anything to the frontend. All the endpoints we had made at this point was bringing the response in JSON.
  
###### Sprint 4
  - In the last sprint we finished all the API's and corrected some SQLs that was crashing in some points. We made all this documentation and the presentation for today. Frontend still a mistery KKKK

#### Our sprint planning
|Sprint 1|Sprint 2|Sprint 3|Sprint 4|
|--------|--------|--------|--------|
| 04/03/2019 * 04/17/2019 | 04/17/2019 * 05/15/2019 | 05/15/2019 * 06/12/2019 | 06/12/2019 * 06/26/2019 |
|*`Defining technology for development`* *`Set architecture`* *`Import of data`* *`Screen Mocks`*|*`Beginning of development`* *`Alignment`* *`First set of working APIs`*|*`Development of more complex APIs`* *`Prod test`* *`MVP1`* *`Alignment`*|*`Project development`* *`Final project presentation (final MVP)`*|
|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|
