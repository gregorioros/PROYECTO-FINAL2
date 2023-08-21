import sys

from PySide6.QtWidgets import QApplication
from UI.servicio.persona_principal import PersonaPrincipal
app = QApplication()
vtn_principal = PersonaPrincipal()
vtn_principal.show()
sys.exit(app.exec())
