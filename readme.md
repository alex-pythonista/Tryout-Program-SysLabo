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