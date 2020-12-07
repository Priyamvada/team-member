# team-member
A Team-Member Management Application

### Project Environment Setup
1. Clone the repo `git clone git@github.com:Priyamvada/team_member.git`
2. Install Homebrew (MacOS only. Skip this step if Windows/ Linux user) `ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)`
3. Install Python3 and pip3
    - MacOS: `brew install python3`
    - Windows: Install Python https://phoenixnap.com/kb/how-to-install-python-3-windows
    - Linux: Run `sudo apt-get update` followed by `sudo apt-get -y install python3-pip`
4. Install mysql
    - MacOS: `brew install mysql`
    - Linux: `sudo apt-get install python3-dev default-libmysqlclient-dev build-essential`
5. Navigate to project root `.../team_member`
6. Install pipenv `pip3 install pipenv`
7. Install all dependencies `pipenv install`
8. Activate the project virtual environment `pipenv shell`

### Setup MySQL DB
Ensure there were no failures while installing `mysql` or while installing `mysqlclient` when running `pipenv install`
1. Start the MySQL server: `mysql.server start`
2. Log into MySQL as the root user: `mysql -u root -p`
3. Create database *teammember_db* for this project in the mysql shell: `CREATE DATABASE teammember_db;`
4. Create user *dbadmin* for the database: `create user dbadmin identified by '0000';`
5. Grant all privileges tp *dbadmin* for *teammember_db*: `grant all on teammember_db.* to 'dbadmin'@'%';`
6. Reload the newly granted privileges: `flush privileges;`
7. Run migrations into *teammember_db*: `python manage.py migrate`