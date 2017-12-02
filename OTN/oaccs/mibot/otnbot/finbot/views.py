# -*- coding: utf-8 -*-
# otnbot/finbot/views.py
import json, requests, random, re
from pprint import pprint

from django.views import generic
from django.http.response import HttpResponse

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# A continuacion se puede ver el arreglo de frases, palabras que puede procesar el bot.

comando = {'sucursales': ["""La lista de sucursales, es:.""",
                      """Las sucursales que tenemos, son:  """],
         'que sucursales tienen':      ["""La lista de sucursales, es:.""",
                      """Las sucursales que tenemos, son:  """],
         'q sucursales tienen':      ["""La lista de sucursales, es:.""",
                      """Las sucursales que tenemos, son:  """],
         'que sucursales hay':      ["""La lista de sucursales, es:.""",
                      """Las sucursales que tenemos, son:  """],
         'q sucursales hay':      ["""La lista de sucursales, es:.""",
                      """Las sucursales que tenemos, son:  """],
         'ke sucursales ay':      ["""La lista de sucursales, es:.""",
                      """Las sucursales que tenemos, son:  """],
         'mi numero de folio es 70501': ["""El estado de su solicitud esta en estado de REVISION. """,
                                """La revisión de la solicitud tarda 2 días. Le agradeceremos vistarnos luego de transcurrido la fase de revisión. """],
         'folio 70501':                 ["""El estado de su solicitud esta en estado de REVISION. """,
                                """La revisión de la solicitud tarda 2 días. Le agradeceremos vistarnos luego de transcurrido la fase de revisión. """],
         'claro, es el 70501': ["""El estado de su solicitud esta en estado de REVISION. """,
                                """La revisión de la solicitud tarda 2 días. Le agradeceremos vistarnos luego de transcurrido la fase de revisión. """],
         'folio 7050': [""" Folio inexistente. El folio debe ser de 5 dígitos y está al reverso de tu ticket. """],
         'folio 70501.': [""" Su credito ha sido aprobado. """],
         'hay alguna sucursal cercana a este codigo postal': [""" Tu sucursal mas cercana, es: """],
         'me gustaria saber el status de mi solicitud de credito.': [""" Por supuesto, me indica su número de folio """],
         'me gustaria saber el status de mi solicitud de credito': [""" Por supuesto, me indica su número de folio """],
         'me gustaria saber el estatus de mi solicitud de credito': [""" Por supuesto, me indica su número de folio """],
         'me gustaria saber el estatus de mi solicitud': [""" Por supuesto, me indica su número de folio """],
         'me gustaria saber el status de mi solicitud': [""" Por supuesto, me indica su número de folio """],
         'estatus de mi solicitud': [""" Por supuesto, me indica su número de folio """],
         'estatus solicitud': [""" Por supuesto, me indica su número de folio """],
         'status': [""" Por supuesto, me indica su número de folio """],
         'solicitud': [""" Por supuesto, me indica su número de folio """],
         'alguna sucursal cercana a este codigo postal': [""" Tu sucursal mas cercana, es: """],
         'cual es la sucursal mas cercana a mi codigo postal': [""" Tu sucursal mas cercana, es: """],
         'horarios': [""" Abrimos de 8AM a 10PM en todas las sucursales. Aqui te esperamos.  """],
         'quiero saber el horario de sus sucursales': [""" Abrimos de 8AM a 4PM en todas las sucursales. Aqui te esperamos.  """],
         'a que hora abren': [""" Abrimos de 8AM a 4PM en todas las sucursales. """],
         'a q hora abren': [""" Abrimos de 8AM a 4PM en todas las sucursales. """],
         'pedido': [""" Tu pedido ha sido recibido. Gracias. """],
         'quiero': [""" Tu pedido ha sido recibido. Puedes recogerlo en la sucursal. Gracias. """],
         'oye': [""" Sí. Dime. """],
         'ver': [""" Por el momento no contamos con mas Sucursales en tu ciudad. """],
         '30': [""" Estas muy viejo. """],
         'buena': [""" Estas muy viejo. """],
         'no, gracias': [""" Estamos para servirte. """],
         'hola': [""" Hola. ¿En qué te podemos ayudar, """],
         'mucho': [""" Esperamos poderle servir mejor en el futuro. Si gusta puede contactar a uno de nuestros ejecutivos. """],
         'ola': [""" Hola. ¿En qué te podemos ayudar, """],
         'rechazo': [""" ¿Que fue lo que lo hizo rechazar? """],
         'gracias': [""" Perfecto. Gracias por visitar el asistente en linea. """],
         'conforme, gracias': [""" Perfecto. Gracias por visitar el asistente de seguimiento de crédito. """],
         'hasta luego': [""" Hasta Luego. """],
         'bye': [""" Bye. """],
         'hay existencia o tienen': [""" La existencia de ese medicamento, es: """],
         'quisiera este medicamento': [""" La existencia de ese medicamento, es: """],
         'ellera': ["""El producto que yo manejo.""",
                  """Tiene Hepatitis."""] }

def fbpostmsg(fb_id, rcvdmsg):    
    # Limpia el mensaje enviado desde el chat de FB
    
    print ("=================== RECBIENDO EL MENSAJE DESDE FB ===================================")
    print (str(rcvdmsg))
	# URL de la API de sucursales
    post_msg_farma = 'https://oc-129-144-151-209.compute.oraclecloud.com/developers/apis/spsbank'
    headers = {'x-api-key': '06d35c6d-7a62-4040-9c9d-189321eafaca'}
    resp = requests.get(post_msg_farma)
    pprint(resp.json())

    j = json.loads(resp.text)
    print (j['Branches'][0]['branchID'])

    sucursal = j['Branches'][2]['branchID']
    sucursal1 = j['Branches'][0]['name']
    sucursal2 = j['Branches'][1]['name']
    sucursal3 = j['Branches'][2]['name']
    sucursal1url = j['Branches'][0]['image_url']
    sucursal2url = j['Branches'][1]['image_url']
    sucursal3url = j['Branches'][2]['image_url']
    nombre = j['Branches'][2]['name']
    print (sucursal)
    print (nombre)

    resultado = '\n'
    invresultado = '\n'   
    
    print ("#### MIDE #####")
    print (len(j['Branches']))
    tamano =  len(j['Branches'])
    limite = tamano - 1
    for i in range(0,tamano):
       sucursal = j['Branches'][i]['branchID']
       nombre = j['Branches'][i]['name']
       if i<limite:
          resultado += str(sucursal) + " " + nombre + ",\n"
       else:
          resultado += str(sucursal) + " " + nombre
    
    print (resultado)

    tokens = re.split(':',rcvdmsg.lower())
    print (tokens)
    msg_text = ''
    suc = ''
    bandera = '0'
    for token in tokens:
        if token == 'folio 70501.':
            bandera = '1' 
        if token == 'rechazo':
            bandera = '2'
        if token == 'que sucursales tienen':
            suc = resultado
            bandera = '3'
        if token == 'q sucursales tienen':
            suc = resultado
            bandera = '3'
        if token == 'que sucursales hay':
            suc = resultado
            bandera = '3'
        if token == 'q sucursales hay':
            suc = resultado
            bandera = '3'
        if token == 'ke sucursales ay':
            suc = resultado
            bandera = '3'
        if token == 'sucursales':
            suc = resultado
            bandera = '3'
        if token == 'mucho':
            bandera = '4'
        if token == 'hola':
             print ("&&&&& FBID %%%%%")
             print (fb_id)
             usrdetailsurl = "https://graph.facebook.com/v2.6/%s"%fb_id
             usrdetailsparams = {'fields':'first_name,last_name,profile_pic', 'access_token':'EAABydslxyIQBANCsrDFvo0WehhOD9QNrIVvG30dovKnKmDNEQUy2YAJx4XPaGwyTJI5F4pUmmSCdyZBqWLfo0LPFYQbwSd38mWagy9ZAp9r6PyyYaU0PFF9lzVtda2GeVOZBnMujE3ZAZCpZBmKNVVAUxl2iBueXJyuqhnzrJzIwZDZD'}
             usrdetails = requests.get(usrdetailsurl, params=usrdetailsparams).json()
             nombre = usrdetails['first_name']
             apellido = usrdetails['last_name']
             print (usrdetails)
             print ("$$$$$ USUARIO  $$$$$")
             print (nombre)
             suc = ' ' + str(nombre) + '?'
        if token == 'ola':
             print ("&&&&& FBID %%%%%")
             print (fb_id)
             usrdetailsurl = "https://graph.facebook.com/v2.6/%s"%fb_id
             usrdetailsparams = {'fields':'first_name,last_name,profile_pic', 'access_token':'EAABydslxyIQBANCsrDFvo0WehhOD9QNrIVvG30dovKnKmDNEQUy2YAJx4XPaGwyTJI5F4pUmmSCdyZBqWLfo0LPFYQbwSd38mWagy9ZAp9r6PyyYaU0PFF9lzVtda2GeVOZBnMujE3ZAZCpZBmKNVVAUxl2iBueXJyuqhnzrJzIwZDZD'}
             usrdetails = requests.get(usrdetailsurl, params=usrdetailsparams).json()
             nombre = usrdetails['first_name']
             apellido = usrdetails['last_name']
             print (usrdetails)
             print ("$$$$$ USUARIO  $$$$$")
             print (nombre)
             suc = ' ' + str(nombre) + '?'
        if token == 'pedido':
             print ("####### PEDIDO ########")
             print (tokens[1])
             post_pedido_farma = 'https://private-ec955f-spsbank.apiary-mock.com/spsbank/complain'
             request_ped_msg   = json.dumps({"pedido":{"idSucursal":"1","producto":"aspirina","cantidad":"3"}})
             response_ped_msg  = requests.post(post_pedido_farma, headers={"Content-Type": "application/json"},data=request_ped_msg)
             pprint(response_ped_msg.json()) 
        if token == 'hay alguna sucursal cercana a este codigo postal':
             print ("#######")
             print (tokens[1])
             post_suc_farma = 'https://private-ec955f-spsbank.apiary-mock.com/spsbank/zipcode/' + tokens[1]
             resp_suc = requests.get(post_suc_farma)
             pprint(resp_suc.json()) 
             jsuc = json.loads(resp_suc.text)
             nombre = jsuc['name']
             idsuc = jsuc['branchID']    
             suc = str(idsuc)+ "-" + nombre
        if token == 'alguna sucursal cercana a este codigo postal':
             print ("#######")
             print (tokens[1])
             post_suc_farma = 'https://private-ec955f-spsbank.apiary-mock.com/spsbank/zipcode/' + tokens[1]
             resp_suc = requests.get(post_suc_farma)
             pprint(resp_suc.json())
             jsuc = json.loads(resp_suc.text)
             nombre = jsuc['name']
             idsuc = jsuc['branchID']
             suc = str(idsuc)+ "-" + nombre
        if token == 'cual es la sucursal mas cercana a mi codigo postal':
             print ("#######")
             print (tokens[1])
             post_suc_farma = 'https://private-ec955f-spsbank.apiary-mock.com/spsbank/zipcode/' + tokens[1]
             resp_suc = requests.get(post_suc_farma)
             pprint(resp_suc.json())
             jsuc = json.loads(resp_suc.text)
             nombre = jsuc['name']
             idsuc = jsuc['branchID']
             suc = str(idsuc)+ "-" + nombre
        if token == 'hay existencia o tienen':
             print ("#######")
             print (tokens[1])
             post_suc_farma = 'https://private-952fb9-spspharmacy1.apiary-mock.com/spspharmacy/inventory/' + tokens[1]
             resp_inv = requests.get(post_suc_farma)
             pprint(resp_inv.json()) 
             jinv = json.loads(resp_inv.text)
             for i in range(0,3):
                invsuc = jinv['Branches'][i]['branchID']
                invnombre = jinv['Branches'][i]['name']
                invcantidad = jinv['Branches'][i]['quantity']
                if i<4:
                   invresultado += str(invsuc) + " " + invnombre + " cuenta con: " + invcantidad + " piezas,\n"
                else:
                   invresultado += str(invsuc) + " " + invnombre + " cuenta con: " + invcantidad + " piezas."
             suc = invresultado 
        if token == 'quisiera este medicamento':
             print ("#######")
             print (tokens[1])
             post_suc_farma = 'https://private-952fb9-spspharmacy1.apiary-mock.com/spspharmacy/inventory/' + tokens[1]
             resp_inv = requests.get(post_suc_farma)
             pprint(resp_inv.json())
             jinv = json.loads(resp_inv.text)
             for i in range(0,3):
                invsuc = jinv['Branches'][i]['branchID']
                invnombre = jinv['Branches'][i]['name']
                invcantidad = jinv['Branches'][i]['quantity']
                if i<4:
                   invresultado += str(invsuc) + " " + invnombre + " cuenta con: " + invcantidad + " piezas,\n"
                else:
                   invresultado += str(invsuc) + " " + invnombre + " cuenta con: " + invcantidad + " piezas."
             suc = invresultado
        if token in comando:
            print (token)		
            msg_text = random.choice(comando[token]) + suc
            break
    if not msg_text:
        msg_text = "Disculpa, no entendi lo que me escribiste." 
    postmsgurl = 'https://graph.facebook.com/v2.6/me/messages?access_token=EAABydslxyIQBANCsrDFvo0WehhOD9QNrIVvG30dovKnKmDNEQUy2YAJx4XPaGwyTJI5F4pUmmSCdyZBqWLfo0LPFYQbwSd38mWagy9ZAp9r6PyyYaU0PFF9lzVtda2GeVOZBnMujE3ZAZCpZBmKNVVAUxl2iBueXJyuqhnzrJzIwZDZD' 

    if bandera == '1':
        response_msg = json.dumps({"recipient":{"id":fb_id}, "message":{ "attachment":{ "type":"template", "payload":{ "template_type":"button", "text":msg_text, "buttons":[{"type":"web_url", "url":"http://www.google.com", "title":"Acepto Credito"},{"type":"postback","title":"Rechazo Credito","payload":"rechazo"}]}}}}) 
    if bandera == '0':
        response_msg = json.dumps({"recipient":{"id":fb_id}, "message":{"text":msg_text}})
    if bandera == '2':
        response_msg = json.dumps({"recipient":{"id":fb_id}, "message":{ "attachment":{ "type":"template", "payload":{ "template_type":"button", "text":msg_text, "buttons":[{"type":"web_url", "url":"http://www.google.com", "title":"Mal Trato"},{"type":"postback","title":"Mucho Tiempo","payload":"mucho"}]}}}})
    if bandera == '3':
        response_msg = json.dumps({"recipient":{"id":fb_id}, "message":{"attachment": {"type": "template","payload": {"template_type": "list","elements": [{"title": "Lista de todas nuestras sucursales","image_url": "http://www.elfinanciero.com.mx/files/article_main/uploads/2016/07/15/5788fbbc3d31c.jpg","subtitle": "Ingresa para ver mas informacion","default_action": {"type": "web_url","url": "https://www.bancoinbursa.com","messenger_extensions": "true","webview_height_ratio": "tall","fallback_url": "https://www.bancoinbursa.com"},"buttons": [{"title": "IR","type": "web_url","url": "https://www.google.com","messenger_extensions": "true","webview_height_ratio": "tall","fallback_url": "https://www.bancoinbursa.com"}]},{"title": "Sucursal 1","image_url":sucursal1url,"subtitle":sucursal1,"default_action": {"type": "web_url","url": "https://www.google.com","messenger_extensions": "true","webview_height_ratio": "tall","fallback_url": "https://www.inbursa.com.mx"},"buttons": [{"title": "Revisar su ubicacion","type": "web_url","url": "https://www.tudecide.com/Sucursales/Detalle/41/9/Iztacalco","messenger_extensions": "true","webview_height_ratio": "tall","fallback_url": "https://www.google.com"}]},{"title": "Sucursal 2","image_url":sucursal2url,"subtitle":sucursal2,"default_action": {"type": "web_url","url": "https://www.google.com","messenger_extensions": "true","webview_height_ratio": "tall","fallback_url": "https://www.inbursa.com.mx"},"buttons": [{"title": "Revisar su ubicacion","type": "web_url","url": "https://www.bancoinbursa.com","messenger_extensions": "true","webview_height_ratio": "tall","fallback_url": "https://www.google.com"}]},{"title": "Sucursal 3","image_url":sucursal3url,"subtitle":sucursal3,"default_action": {"type": "web_url","url": "https://www.google.com","messenger_extensions": "true","webview_height_ratio": "tall","fallback_url": "https://www.inbursa.com.mx"},"buttons": [{"title": "Revisar su ubicación","type": "web_url","url": "https://www.tudecide.com/Sucursales/Detalle/41/9/Tlalpan","messenger_extensions": "true","webview_height_ratio": "tall","fallback_url": "https://www.google.com"}]}],"buttons": [{"title": "Ver más...","type": "postback","payload": "ver" }]  }}} })
    if bandera == '4':
        response_msg = json.dumps({"recipient":{"id":fb_id},"message":{"attachment":{"type":"template","payload":{"template_type":"button","text":msg_text,"buttons":[{"type":"phone_number","title":"Llamar a un ejecutivo","payload":"+5215513846357"}]}}} })
    status = requests.post(postmsgurl, headers={"Content-Type": "application/json"},data=response_msg)
    pprint(status.json())

# Aqui se generan las vistas	
class otnbotView(generic.View):
    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == '4318232572':
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Token invalido')
			
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    # Aquí se maneja el mensaje recibido por FB
    def post(self, request, *args, **kwargs):
        # Convierte el texto en un vocabulario entendible por Python
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        print ("==========================  UUUUUU ========================")
        pprint(incoming_message)
        # Se hace un loop por cada mensaje recibido por FB
        # Esto debido a que se pueden recibir multiples mensajes
        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                # Revisa el formato del mensaje
                # Ya que se pueden recibir varios formatos: message, postback, etc
                if 'message' in message:
                    # Lo mandamos a la terminal
                    print ("((((((((((((((((((((( EMPEZANDO )))))))))))))))))))))))))))")
                    pprint(message)
                    # Asumimos que solo viene texto
                    # y que lo demás viene como adjunto
                    fbpostmsg(message['sender']['id'], message['message']['text']) 					
                if 'postback' in message:
                    # Lo manda a la terminal
                    print ("((((((((((((((((((((( EMPEZANDO )))))))))))))))))))))))))))")
                    pprint(message)
                    # Asumimos que solo viene texto
                    # y que lo demás viene como adjunto.
                    fbpostmsg(message['sender']['id'], message['postback']['payload'])
        return HttpResponse()
