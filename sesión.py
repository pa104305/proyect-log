# -*- coding:utf-8 -*-
# importamos las variables que almacenan los datos para iniciar sesión
import user1 as dat
# creamos la funcion sesión para que iniciar sesión en el programa
def sesión():
    # imprimimos la bienvenida al usuario
    print("Bienvenido al inicio de sesión")
    # creamos la funcion mail, para solicitar el e-mail y comprobar su existencia
    def mail():
        # solicitamos al usuario ingrese un correo electronico
        e_mail = input("Ingresa un correo electronico para iniciar sesión > ")
        # comparamos el e-mail ingresado con el del archivo de datos
        if e_mail == dat.Input_e_mail:
            # llamamos a la funcion que nos solicita la contraseña
            passwd()
        # en caso de que el correo no coincida se lo notificamos al usuario y volvemos a llamar
        # el mail
        else:
            print("El correo no se ha registrado, vuelve a intentarlo")
            mail()
    # creamos la funcion passwd la cual nos solicita la contraseña
    def passwd():
        # solicitamos al usuario ingrese la contraseña correspondiente
        password = input("Ingrese una contraseña para iniciar sesión > ")
        # comparamos la contraseña ingresada con el del archivo user1.py
        if password == dat.Input_password:
            print("Accediendo...\nInicio de sesion correcto \nBIENVENIDO DE NUEVO " + dat.Input_user_name)
        # en el mismo caso de que la contraseña sea incorrecta lo notificamos al usuario y
        # lo volvemos a intentar
        else:
            print("Contraseña incorrecta, vuelve a intentarlo")
            passwd()
    mail()