import pandas as pd
import matplotlib.pyplot as plt
import protMqtt as mqtt

def atualizaGraf():
    df=pd.read_csv('dados_jogo.csv')

    #rodada =''.join(mqtt.rodada)
    #novos=pd.DataFrame([mqtt.ganhou,int(rodada,2)], columns=['venceu','rodada'])
    #pd.concat(df,novos,ignore_index=True)

    #df.to_csv('dados_jogo.csv')

    if 1 in df['venceu'].unique():
        vencedores = df['venceu'].value_counts()[1]
    else:
        vencedores = 0

    if 0 in df['venceu'].unique():
        perdedores = df['venceu'].value_counts()[0]
    else:
        perdedores = 0

    venc=[vencedores, perdedores]

    px=1/plt.rcParams['figure.dpi']

    labels='Venceram','Perderam'
    fig1, ax1 = plt.subplots(figsize=(200*px,200*px))
    ax1.pie(venc, radius=3,center=(4,4),labels=labels,autopct='%1.1f%%', explode=(0.1,0), shadow=True, textprops={'fontsize': 8})
    ax1.axis('equal')
    fig1.suptitle('Vitórias e Derrotas',fontsize=10)
    fig1.savefig('imagens/graphVitorias.png',edgecolor=(0,0,0))

    fig2, ax2 = plt.subplots(figsize=(200*px,200*px))
    rodadas='1','2','3','4','5'
    count = [0,0,0,0,0]

    for i in range(5):
        if i in df['rodada'].unique():
            count[i]=df['rodada'].value_counts()[i]

    ax2.barh(rodadas,count)
    ax2.tick_params(axis='both', labelsize = 6)
    ax2.set_xlabel('Jogadores',fontsize=6)
    fig2.suptitle('Rodada Final',fontsize=10)
    fig2.savefig('imagens/graphRodadas.png',edgecolor=(0,0,0))

atualizaGraf()