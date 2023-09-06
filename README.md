You can clone & create this repo with the following commands -

First, create virtual environment using :
```bash
pip install virtualenv

virtualenv env_name
```
To activate the environment (in Windows) :
```bash
.\env_name\Scripts\activate
```
Now install the dependencies:

```bash
pip install requirements.txt
```
Then, run the server:

```bash
flask run
```
The Flask server will be running on [http://127.0.0.1:5000](http://127.0.0.1:5000)

The API endpoints are - 
```bash
GET - http://127.0.0.1:5000/users - Fetch all the users
GET - http://127.0.0.1:5000/users/<user_id> - Fetch a particular user with the corresponding id
POST - http://127.0.0.1:5000/users - Payload - { "name", "email", "password" } - Create a user
PUT - http://127.0.0.1:5000/users/<user_id> - Payload - { "name", "email", "password" } - Update the data of a particular user
DELETE - http://127.0.0.1:5000/users/<user_id> - Delete the user with the corresponding id
```
