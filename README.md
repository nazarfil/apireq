
## API backend
  mkdir venv
  virtualenv -p python3 venv/
  source venv/bin/activate

  git clone https://github.com/nazarfil/apireq.git
  cd apireq
  pip install -r requirements.txt

  python manage.py migrate
  pytohn manage.py runserver

Then navigate to localhost:8000/api/

* request/
* request/<category>
* userdata
* userdata/good-security
