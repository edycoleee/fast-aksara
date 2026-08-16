from fastapi.templating import Jinja2Templates

# Satu instance bersama — global site() ditambahkan dari main.py saat startup
templates = Jinja2Templates(directory="app/templates")
