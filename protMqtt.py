import paho.mqtt.client as mqtt

#Credenciais
user = "grupo1-bancadaA8"
passwd = "L@Bdygy1A8"
Broker = "labdigi.wiseful.com.br"           
Port = 80                           
KeepAlive = 60

# Quando conectar na rede (Callback de conexao)
def on_connect(client, userdata, flags, rc):
  print("Conectado com codigo " + str(rc))
  client.subscribe(user+"/E0", qos=0)
  print("Conectado com codigo E0")
  client.subscribe(user+"/E1", qos=0)

# Quando receber uma mensagem (Callback de mensagem)
def on_message(client, userdata, msg):
  print(str(msg.topic)+" "+str(msg.payload.decode("utf-8")))
  global pronto
  pronto=0
  if str(msg.topic) == user+"/E0":
    print("Recebi uma mensagem de E0")
    pronto=1
  elif str(msg.topic) == user+"/E1":
    print("Recebi uma mensagem de E1")
  else:
    print("Erro! Mensagem recebida de tópico estranho")

pronto=0
client = mqtt.Client()              
client.on_connect = on_connect      
client.on_message = on_message  

client.username_pw_set(user, passwd)     