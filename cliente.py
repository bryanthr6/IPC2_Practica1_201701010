class Cliente:
    def __init__(self, nombre, email, nit):
        self.nombre = nombre
        self.email = email
        self.nit = nit

    # Métodos de acceso como propiedades
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email 

    def get_nit(self):
        return self.nit
    
    def set_nit(self, nit):
        self.nit = nit
