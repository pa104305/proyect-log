# -*- coding:utf-8 -*-
from itertools import count
# creamos la funcion encargada de crear un nuevo perfil
def create():
    # esta variable abre un archivo python para guardar los datos como variables en el mismo
    # archivo para despues ser utilizado para iniciar sesión
    save = open("user1.py", "w")
    # iniciamos con una segunda funcion encargada de recibir el nombre de usuario
    def user():
        # la funcion "user" nos solicita un nombre de usuario
        user_name = input("Ingresa un nombre de usuario > ")
        # y despues compra la cantidad de letras del nombre de usuario, primero compara si tiene
        # 5 letras o menos se vuelve a solcitar un nombre de usuario
        if len(user_name) < 5:
            print("El nombre de usuario debe tener minimo 5 caracteres...")
            user()
        # si no tiene menos de 5 letras compara si tiene 6 o más letras si es asi prosigue
        # a la siguiente funcion
        elif len(user_name) >= 6:
            print("Nombre de usuario valido, continuando...")
            # en este primer punto sobre escribimos el archivo abierto al principio del codigo
            # con el nombre de usuario indicado y creando una variable que lo contenga
            save.write("\nInput_user_name = \"" + user_name + "\"")
            #llamar a la funcion de correo electronico
            mail()
        # por ultimo nos encontramos con el else en caso de que no cumpla ninguna de las dos
        # sentencias anteriores ira por default a esta
        else:
            print("El nombre de usuario no es valido")
            user()
    # despues generamos la funcion mail en la cual nos solicitara un e-mail, como en cualquier
    # otra plataforma en la que queramos crear una cuenta
    def mail():
        e_mail = input("Ingresa un correo electronico > ")
        # ahora el programa procede a contar los numeros de @ que hay en el input anterior
        arroba = e_mail.count("@")
        com = e_mail.endswith(".com")
        # el if compara si la cantidad de @ es igual a uno si es asi se acepta el e-mail
        if arroba == 1 and com == True:
            print("Correo electronico valido, procediendo...")
            # cuando el e-mail a sido aceptado lo guarda en el archivo abierto al cominenzo en
            # la variable e_mail, para usarlo en el inicio de sesión
            save.write("\nInput_e_mail = \"" +  e_mail + "\"")
            #llamar a la funcion que solicita la contraseña
            passwd()
        else:
            print("e-mail no valido, vuelve a intentarlo")
            mail()

    def passwd():
        password = input("Ingresa una contraseña > ")
        num = password.isdigit()
        al = password.isalpha()
        count = password.count(" ")
        if len(password) >= 8 and count == 0 and num != True and al != True:
            input("Presione enter para crear su cuenta...")
            # aqui pasa lo mismo que al guardar el correo y el nombre de usuario, se guarda
            # cuando la contraseña a sido aceptada
            save.write("\nInput_password = \"" + password + "\"")
            # despues cierra el archivo para que se guarden los datos escritos
            save.close()
            # llamar a la ultima funcion del programa crear
            grettins()
        else:
            print("La contraseña elegida no es segura, vuelve a intentarlo")
            passwd()

    def grettins():
        print("Su cuenta a sido creada con exito\nGracias por crear una cuenta en *inserte nombre de app*")
    user()
    