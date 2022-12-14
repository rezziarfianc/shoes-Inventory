import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import controllers.__auth as auth
import controllers.__view as view

auth.form_login()
view.menu()








