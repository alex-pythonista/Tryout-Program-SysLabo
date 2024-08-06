# Tryout Program: Syslabo Organization Chart Application

### Project requirements (fulfilled requirements are marked as done).
- [x] Please create and provide an application that automatically creates an organizational chart like the one created in "組織図
(Organization chart).xlsx".
- [x] The applications that you create should be simple so that they can be maintained and modified by users other than the
author.
- [x] We would like to have a simple function that allows us to maintain "sys_users" and "cmn_department“, as we would like to
manage the change history, if possible.
- [ ] Since we would like to be able to manage the information of "concurrent duties" that we cannot currently manage, I would
like you to design and propose a way to realize what kind of structure should be used to manage it (implementation is not
required)

### Project Brief
1. The two user xlsx table files, that were provided along the assignement were implemented as a database of the application.
2. Some fields are made optional intentionally, because, either it didn't contributed much on the organization chart render process or didn't contain any data.
3. A relational database is used to store the data.
4. Django Template Engine is used to implement the data rendering from the backend to frontend.

### Video Demonstration
https://github.com/user-attachments/assets/21263d00-a053-4a21-be1b-a6d6c03e4c8e

### How to setup the project

#### Prerequisites
1. Docker and docker compose program has to be installed in the host machine.
2. The program starts with an `entrypoint.sh` file. Windows, by default, cannot run `.sh` files. If you are a windows user, please use `Git bash`.

#### Project setup
1. Create a clone of the project
2. Run `docker compose up --build`. This command will fire up the db and the web application.

### Tech Stack
1. Python
2. Django
3. HTML, CSS, Bootstrap 4.6
4. Docker
5. PostgreSQL

### Scope of improvements

1. A modern frontend framework can be used to improve data rendering and dynamic data input.
2. For an asymmetric data structure like the organization hierarchy, the optimized solution could be a NoSQL database.

### My limitations
Although I have decent proficiency in Django Framework and PostgreSQL database, I lack of frontend development. This application UI can be implemented with dynamic drag-n-drop features along with NoSQL db compatibility like MongoDB. 大変申し訳ありません 😔🙇🏻‍♂️
