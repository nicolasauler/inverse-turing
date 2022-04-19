import pandas as pd
import matplotlib.pyplot as plt
import protMqtt as mqtt

def atualizaGraf():
    df=pd.read_csv('dados_jogo.csv')

    rodada =''.join(mqtt.rodada)
    novos=pd.DataFrame([[mqtt.ganhou_aux,int(rodada,2)]], columns=['venceu','rodada'])
    df = pd.concat([df,novos],ignore_index=True)

    df.to_csv('dados_jogo.csv',index=False)

    if 1 in df['venceu'].unique():
        vencedores = df['venceu'].value_counts()[1]
    else:
        vencedores = 0

    if 0 in df['venceu'].unique():
        perdedores = df['venceu'].value_counts()[0]
    else:
        perdedores = 0

    venc=[vencedores, perdedores]

    
    px = (1/plt.rcParams['figure.dpi'])

    labels='Replicantes','Humanos'
    fig1, ax1 = plt.subplots(figsize=(200*px,200*px))
    ax1.pie(venc, radius=3,center=(4,4),labels=labels,autopct='%1.1f%%', explode=(0.2,0), shadow=True, textprops={'fontsize': 8})
    ax1.axis('equal')
    fig1.suptitle('Humanos e Replicantes',fontsize=10)
    fig1.savefig('./assets/images/graphVitorias.png',edgecolor=(0,0,0))
    plt.close()

    fig2, ax2 = plt.subplots(figsize=(200*px,200*px))
    rodadas='1','2','3','4','5'
    count = [0,0,0,0,0]

    for i in range(1,6):
        if i in df['rodada'].unique():
            count[i-1]=df['rodada'].value_counts()[i]

    ax2.barh(rodadas,count)
    ax2.tick_params(axis='both', labelsize = 6)
    ax2.set_xlabel('Jogadores',fontsize=6)
    fig2.suptitle('Rodada Final',fontsize=10)
    fig2.savefig('./assets/images/graphRodadas.png',edgecolor=(0,0,0))

    plt.close()