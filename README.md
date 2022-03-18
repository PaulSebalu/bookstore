# Bookstore

#### Installation guidelines
- Clone the repo
- Install dependencies using `pipenv install`
- Create a postgres db
- Create an  ```.env``` file and specify the ```DATABASE_URL```, ```DEBUG``` and ```SECRET_KEY``` values.
- Run migrations to load data in the db
- Invoke interactive shell to run querysets