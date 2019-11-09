class Usuarios:

    def __init__(self, nombre, apellido, correo, password):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.password = password
        self.es_activo = 1

    @property
    def nombre(self):
        return self.nombre

    @nombre.setter
    def nombre(self, nombre):
        if 0 < len(nombre) <= 20:
            self.nombre = nombre
        else:
            self.nombre = "null"

    @property
    def apellido(self):
        return self.apellido


    @apellido.setter
    def apellido(self, apellido):
        if 0 < len(apellido) <= 35:
            self.apellido = apellido
        else:
            self.apellido = "null"


    @property
    def correo(self):
        return self.correo

    @correo.setter
    def correo(self, correo):
        if 0 < len(correo) <= 35:
            self.apellido = correo
        else:
            self.apellido = "null"


    @password.setter
    def correo(self, correo):
        if 0 < len(correo) <= 35:
            self.apellido = correo
        else:
            self.apellido = "null"

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, value):
        self._password = value


