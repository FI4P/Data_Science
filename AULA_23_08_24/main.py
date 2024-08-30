import matplotlib.pyplot as plt;
import seaborn as sb;
import pandas as pd;

endpoint = 'https://docs.google.com/spreadsheets/d/1fwHpm487iZ0F1jeRkOAxke7ArFjnCCRXLRPteOgVtNc/export?format=csv'

try:
    dataFrame = pd.read_csv(endpoint);

    # Renomeia os dados para melhor entedimento
    dataFrame = dataFrame.rename(columns={"Gado" : "suinos"})
    dataFrame = dataFrame.rename(columns={"Ganho" : "ganho"})

    #Verificar os tipos de dados e se o python interpreta todos corretamente
    dataFrame["ganho"] = dataFrame["ganho"].str.replace(",", ".");

    # Converte os valores da coluna ganho para numerico, assim o python consegue lidar com todos;
    dataFrame["ganho"] = pd.to_numeric(dataFrame["ganho"]);

    # Resumo estatistico dos dados da planilha
    resumo_estatisico = dataFrame["ganho"].describe()
    print(resumo_estatisico)

    # Respostas # 


    # 1) Criar o histograma
    sb.histplot(data=dataFrame, x="ganho", bins=10)
    plt.title("Histograma da variável de ganho de peso")
    plt.xlabel("Ganho de peso")
    plt.ylabel("Quantidade de suinos")
    plt.show()

    # 2) Quando utilizamos o método describe do panda, é possivel descobrir os quartis dos dados. 

        # 25% - Representa o quartil inferior (Q1). De acordo com os nossos dados, 25% dos ganhos de peso se encontram abaixo ou iguais a 2.04;
        # 50% - Representa o segundo quartil (Q2). De acordo com os nossos dados, 50% dos ganhos de peso se encontram abaixo ou iguais a 2.69;
        # 75% - Representa o quartil superiro (q3). De acordo com os nossos dados, 75% dos ganhos de peso se encontram abaixo ou iguais a 3.39;



    # 3) Você acha que a nova ração é mais eficiente que a tradicional? Justifique.
    # De acordo com a analise de dados feita, é possivel observar que ate o terceiro quartil o ganho de peso da ração dois foi inferior a média mensal da ração um (3.5kg). Com isso, pode se concluir que a ração de numero um é mais eficiente.


    



    




except Exception as error:
    print(error)