import paho.mqtt.client as mqtt

#Credenciais
user = "grupo1-bancadaA5"
passwd = "L@Bdygy1A5"
Broker = "labdigi.wiseful.com.br" 
Port = 80                           
KeepAlive = 60

rodada=['0','0','0']
ganhou_aux=0

# Quando conectar na rede (Callback de conexao)
def on_connect(client, userdata, flags, rc):
  print("Conectado com codigo " + str(rc))
  client.subscribe(user+"/S0", qos=0)
  client.subscribe(user+"/S1", qos=0)
  client.subscribe(user+"/S2", qos=0)
  client.subscribe(user+"/S3", qos=0)
  client.subscribe(user+"/S4", qos=0)
  client.subscribe(user+"/S5", qos=0)
  client.subscribe(user+"/S6", qos=0)

# Quando receber uma mensagem (Callback de mensagem)
def on_message(client, userdata, msg):
  print(str(msg.topic)+" "+str(msg.payload.decode("utf-8")))
  global ganhou
  global perdeu
  global audio
  ganhou=0
  perdeu=0
  audio= 0
  if str(msg.topic) == user+"/S5":
    print("Recebi uma mensagem de S5")
    if str(msg.payload.decode("utf-8")) == '1':
      ganhou=1
  elif str(msg.topic) == user+"/S4":
    print("Recebi uma mensagem de S4")
    if str(msg.payload.decode("utf-8")) == '1':
      perdeu=1
  elif str(msg.topic) == user+"/S0":
    rodada[2]= str(msg.payload.decode("utf-8"))
  elif str(msg.topic) == user+"/S1":
    rodada[1]= str(msg.payload.decode("utf-8"))
  elif str(msg.topic) == user+"/S2":
    rodada[0]= str(msg.payload.decode("utf-8"))
  elif str(msg.topic) == user+"/S3":
    if str(msg.payload.decode("utf-8")) == '1':
      audio=1
  else:
    print("Erro! Mensagem recebida de tópico estranho")

ganhou=0
perdeu=0
audio= 0
client = mqtt.Client()              
client.on_connect = on_connect      
client.on_message = on_message  

client.username_pw_set(user, passwd)     
