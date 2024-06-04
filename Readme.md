# Install project

##Step 1 : 
Create env `docker compose build --no-cache`
##Step 2 : 
Generate fake data `docker-compose run web python3 manage.py migrate && docker-compose run web python3 manage.py generate_fake_data -u 1`
##Step 3 : 
Start containers `docker compose up`

#Optional
If you want to run the tests you have to run `docker-compose run web python3 manage.py test`

#Endpoints examples:
Make sure that you add the authorization header Bearer token when you use those endpoints. As a example you can check the End To End tests (glucose/tests.py StudentListTest)
##LevelList 
Endpoint example GET: `http://localhost:8100/api/v1/levels/?limit=10&start=2022-11-13T18:14:21&stop=2022-12-13T18:14:21`
##LevelList by user
Endpoint example GET: `http://localhost:8100/api/v1/levels/1?limit=10&start=2022-11-13T18:14:21&stop=2022-12-13T18:14:21`
##Add new level 
Endpoint example POST: `http://localhost:8100/api/v1/levels/create/`