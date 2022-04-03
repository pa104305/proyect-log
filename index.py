# -*- coding:utf-8 -*-
import crear as nu
import sesión as ss

print("Seleccione:\n  1-. Iniciar sesión \n  2-. Crear cuenta")
log_sign = input("Seleccione 1 o 2 > ")
if log_sign == "1":
    ss.sesión()
elif log_sign == "2":
    nu.create() 
