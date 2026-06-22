from modules.auth import login
from modules.menus import arrancar


user_logado = login()

if user_logado:
  arrancar(user_logado)