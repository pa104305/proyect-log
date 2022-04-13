# -*- coding:utf-8 -*-
import crear as nu
import sesión as ss

print("Seleccione:\n  1-. Crear cuenta \n  2-. Iniciar sesión")
log_sign = input("Seleccione 1 o 2 > ")
if log_sign == "1":
    nu.create()     
elif log_sign == "2":
    ss.sesión()
