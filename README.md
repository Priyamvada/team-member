# team-member
A Team-Member Management Application
Uses Python-Django framework for interfacing with the Database and Django Rest Framework for structuring APIs

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
8. *Create superuser (optional: only if you want to log into Django admin and verify the schema): `python manage.py createsuperuser --email admin@example.com --username admin`*

## Testing the APIs
### Run the server
- After activating the virtual environment and completing the DB setup and migration, run
`python manage.py runserver`.
This will try to run the server on `port: 8000`.
- To run on a custom port, run
`python manage.py runserver 0.0.0.0:<port>`

### Create new Team Member
##### Sample Request
Use a post request as follows
`curl -X POST -H "Content-Type:application/json" http://127.0.0.1:8000/api/team_members/ -d '{"first_name": "David", "last_name": "Jones", "phone_number": "+15101234567", "email": "davidjones@test.com", "role": 0}'`
##### Sample Response
- Returns status code 201 if success, and the entire newly created team member object with id
- Returns status code 400 along with error message, on validation errors such as missing fields, unique constraint violations
```json5
{
   "id":8,
   "first_name":"David",
   "last_name":"Jones",
   "full_name":"David Jones",
   "phone_number":"+15101234567",
   "email":"davidjones@test.com",
   "role":"Admin",
   "created":"2020-12-15 06:04:56 +0000",
   "last_modified":"2020-12-15 06:04:56 +0000"
}
```

### Edit Team Member
##### Sample Request
Note the `id` of the team member to be edited. Eg: 8 from the above example.
Use a PATCH request as follows
`curl -X PATCH -H "Content-Type:application/json" http://127.0.0.1:8000/api/team_members/8/ -d '{"last_name": "Jones II", "role": 1}'`
- Note: the field `role` accepts any of 2 formats - numbers `0` or `1`, or case insensitive words *"admin"* or *"regular"*
- For example, `curl -X PATCH -H "Content-Type:application/json" http://127.0.0.1:8000/api/team_members/8/ -d '{"last_name": "Jones II", "role": "reGuLAr"}'` will also yield the same response as above.
##### Sample Response
- Returns status code 200 if success, and the entire updated team member object
- Returns status code 400 along with error message, on validation errors such as missing fields, unique constraint violations
- Returns status code 404 if the `id` passed is invalid
```json5
{
   "id":8,
   "first_name":"David",
   "last_name":"Jones II",
   "full_name":"David Jones II",
   "phone_number":"+15101234567",
   "email":"davidjones@test.com",
   "role":"Regular",
   "created":"2020-12-15 06:04:56 +0000",
   "last_modified":"2020-12-15 06:38:43 +0000"
}
```

### Delete Team Member
##### Sample Request
Note the `id` of the team member to be edited. Eg: 8 from the above example.
Use a DELETE request as follows
`curl -X DELETE http://127.0.0.1:8000/api/team_members/8/`
##### Sample Response
- Returns status code 204 if success, and empty object `{}` is returned.
- Returns status code 404 if the `id` passed is invalid
```json5
{}
```