# instagrades
-Steps for running the website:
	-create file settings.py in ./instagrades
	-Copy ./settings.example into settings.py
	-run cmd in the directory of the project
	-run "docker-compose up"
	-the site will run at port 8000

-Dependencies:
   dependency declaration tool:pip
   dependency isolation tool: Docker (no need for virtualenv with docker)
	instructions to add and install a dependency:
			- add in requirements.txt file
			- run pip install -r requirements.txt


-Config: ./instagrades/settings.py

-Build,Run,Release:
	-Backing Services:
		Postgre SQL , mock api (custom made mockapi to return data to mock GUC API) , mockaroo, psycopg2 (adapter for postgres)
		to run, run command
		"docker-compose build && docker-compose up -d" in terminal in project base folder
		then to migrate tables to database: docker-compose run web python manage.py makemigrations
		then: docker-compose run web python manage.py migrate.

		Database image will be running at port 5432

	Docker files: 
		-docker-compose.yml
		-dockerfile
		-requirements.txt


			
