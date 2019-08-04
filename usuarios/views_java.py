# -*- encoding: utf-8 -*-
__author__ = 'brian'

import django.contrib.auth as auth
import django.http as http
from annoying.functions import get_object_or_None


from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import get_object_or_404
import json,httplib
import datetime

from utilidades import Token
from usuarios.models import Tokenregister

from django.contrib.auth.models import User


'''
definicion para conseguir el usuario de django a partir del token
'''
def get_userdjango_by_token(datos):
    token = datos.get('token')
    user_token = get_object_or_None(Tokenregister,token=token)
    if user_token is not None:
        return user_token.user
    else:
        return None


'''
definicion para conseguir el usuario de django a partir del token
'''
def get_userdjango_by_token2(token):

    user_token = get_object_or_None(Tokenregister,token=token)
    if user_token is not None:
        return user_token.user
    else:
        return None

'''
definicion para conseguir el usuario de django a partir del id de usuario
'''
def get_userdjango_by_id(datos):
    userdjango_id = datos.get('usuario_id')
    userdjango = get_object_or_None(User, pk=userdjango_id)
    return userdjango


'''
definicion para conseguir el usuario de django a partir del id de usuario
'''
def get_userdjango_by_id2(userdjango_id):

    userdjango = get_object_or_None(User, pk=userdjango_id)
    return userdjango




'''
definicion para comprobar el usuario
'''
def comprobar_usuario(datos):
    userdjango = get_userdjango_by_id(datos)
    user_token = get_userdjango_by_token(datos)

    if (user_token is not None) and (userdjango is not None):
        if user_token == userdjango:
            return True
        else:
            return False
    else:
        return False


'''
definicion para comprobar el usuario
'''
def comprobar_usuario2(token,userdjango_id):
    userdjango = get_userdjango_by_id2(userdjango_id)
    user_token = get_userdjango_by_token2(token)

    if (user_token is not None) and (userdjango is not None):
        if user_token == userdjango:
            return True
        else:
            return False
    else:
        return False




'''
definicion para logear un usuario desde la aplicación java
'''
@csrf_exempt
def login(request):
    print "Login"
    try:
        try:
            datos= json.loads(request.POST['data'])
            us = datos.get('usuario').lower()
            password = datos.get('password')
        except Exception as e:
            us = request.POST['usuario']
            password =request.POST['password']

        if (us is None and password is None) or (us == "" and password == ""):
            response_data = {'result': 'error', 'message': 'Falta el usuario y el password'}
            return http.HttpResponse(json.dumps(response_data), content_type="application/json")

        if us is None or us == "" :
            response_data = {'result': 'error', 'message': 'Falta el usuario'}
            return http.HttpResponse(json.dumps(response_data), content_type="application/json")

        if password is None or password == "":
            response_data = {'result': 'error', 'message': 'Falta el password'}
            return http.HttpResponse(json.dumps(response_data), content_type="application/json")
        us = us.lower()
        user = auth.authenticate(username=us, password=password)

        if user is not None:
            if user.is_active:
                user_token = get_object_or_None(Tokenregister,user=user)
                if user_token==None:
                    token1 = str(user.id) + "_" + Token.id_generator()
                    tokenform = Tokenregister(token=token1, user=user)
                    tokenform.save()
                    user_token = get_object_or_None(Tokenregister, user=user)
                else:
                    user_token.date = datetime.datetime.now()
                    user_token.token = str(user.id) + "_" + Token.id_generator()
                    user_token.save()

                response_data = {'result': 'ok', 'message': 'Usuario logeado', 'token':user_token.token, 'usuario':user.username,
                                 'nombre': user.first_name,
                                 }

                return http.HttpResponse(json.dumps(response_data), content_type="application/json")

            else:
                response_data = {'result': 'error', 'message': 'Usuario no activo'}
                return http.HttpResponse(json.dumps(response_data), content_type="application/json")
        else:
            response_data = {'result': 'error', 'message': 'Usuario no válido'}
            return http.HttpResponse(json.dumps(response_data), content_type="application/json")

    except Exception as e:
        response_data = {'errorcode': 'U0001', 'result': 'error', 'message': str(e)}

        return http.HttpResponse(json.dumps(response_data), content_type="application/json")

'''
definicion para logear un usuario desde la aplicación java
'''
@csrf_exempt
def logout(request):
    print "Logout"
    try:
        try:
            datos = json.loads(request.POST['data'])
            token = datos.get('token')
            userdjango_id = datos.get('usuario_id')

        except Exception as e:
            token = request.POST['token']
            userdjango_id = request.POST['usuario_id']

        if comprobar_usuario2(token,userdjango_id):
            userdjango = get_userdjango_by_token2(token)

            user_token = get_object_or_None(Tokenregister, user=userdjango)
            if user_token is None:
                response_data = {'result': 'ok', 'message': 'Usuario ya deslogueado'}
            else:

                user_token.delete()
                response_data = {'result': 'ok', 'message': 'Usuario ya deslogueado'}
        else:
            response_data = {'result': 'error', 'message': 'Usuario no logueado'}

        return http.HttpResponse(json.dumps(response_data), content_type="application/json")

    except Exception as e:
        response_data = {'errorcode': 'U0002', 'result': 'error', 'message': str(e)}
        return http.HttpResponse(json.dumps(response_data), content_type="application/json")




'''
definicion para comprobar el token
'''
@csrf_exempt
def comprobar_token(request):
    print "Comprobando token"
    try:
        try:
            datos = json.loads(request.POST['data'])
            token = datos.get('token')
            userdjango_id = datos.get('usuario_id')

        except Exception as e:
            token = request.POST['token']
            userdjango_id = request.POST['usuario_id']

        if token != "" and comprobar_usuario2(token,userdjango_id):
            response_data = {'result': 'ok', 'message': 'Usuario logueado'}

        else:
            response_data = {'result': 'error', 'message': 'Usuario no logueado'}

        return http.HttpResponse(json.dumps(response_data), content_type="application/json")

    except Exception as e:
        response_data = {'errorcode': 'U0003', 'result': 'error', 'message': str(e)}
        return http.HttpResponse(json.dumps(response_data), content_type="application/json")


@csrf_exempt
def get_perfil(request):
    print "buscando perfil"
    try:

        try:
            datos = json.loads(request.POST['data'])
            token = datos.get('token')
            userdjango_id = datos.get('usuario_id')

        except Exception as e:
            token = request.POST['token']
            userdjango_id = request.POST['usuario_id']

        if comprobar_usuario2(token,userdjango_id):
            userdjango = get_userdjango_by_token2(token)

            response_data = {'result': 'ok', 'message': 'Perfil de usuario', 'email': userdjango.email,
                             'nombre': userdjango.first_name}

        else:
            response_data = {'result': 'error', 'message': 'Usuario no logueado'}

        return http.HttpResponse(json.dumps(response_data), content_type="application/json")

    except Exception as e:
        response_data = {'errorcode': 'U0004', 'result': 'error', 'message': 'Error en perfil de usuario: '+str(e)}
        return http.HttpResponse(json.dumps(response_data), content_type="application/json")

'''
metodo para que un usuario pueda ver su perfil, necesario estar loegueado y pasar su id y token
'''
@csrf_exempt
def cambiar_pass(request):
    print "cambiando pass"
    try:
        try:
            datos = json.loads(request.POST['data'])
            token = datos.get('token')
            userdjango_id = datos.get('usuario_id')
            antiguapass = datos.get('antigua')
            nuevapass = datos.get('nueva')

        except Exception as e:
            token = request.POST['token']
            userdjango_id = request.POST['usuario_id']
            antiguapass = request.POST['antigua']
            nuevapass = request.POST['nueva']

        if comprobar_usuario2(token,userdjango_id):
            userdjango = get_userdjango_by_token2(token)
            if userdjango.check_password(antiguapass):
                token = get_object_or_None(Tokenregister,user=userdjango)
                token.delete()
                userdjango.set_password(nuevapass)
                userdjango.save()
                response_data = {'result': 'ok', 'message': 'Password cambiado'}
            else:
                response_data = {'result': 'error', 'message': 'Password antiguo incorrecto'}
        else:
            response_data = {'result': 'error', 'message': 'Usuario no logueado'}

        return http.HttpResponse(json.dumps(response_data), content_type="application/json")

    except Exception as e:
        response_data = {'errorcode': 'U0005', 'result': 'error', 'message': 'Error en perfil de usuario: '+str(e)}
        return http.HttpResponse(json.dumps(response_data), content_type="application/json")

