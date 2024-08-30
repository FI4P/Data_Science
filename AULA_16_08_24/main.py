import pandas as pd
import matplotlib.pyplot as plt;
import seaborn as sb;

endpoint = 'https://drive.google.com/uc?id=126JBR54DaopbBDjcQql12EMqU2gB8e4M'

try:
 
 ##Cria um dataframe com base no arquivo da URL;
 dataFrame = pd.read_excel(endpoint)
 
 #Retorna os registros encontrados na coluna de sexo;
 sexos = dataFrame["sexo"];

 #Renomeia uma coluna para melhor entendimento dos dados;
 #DataFrame precisa receber as colunas renomeadas, caso contrário não terá efeito.
 dataFrame = dataFrame.rename(columns={'salario dos funionarios' : 'salario'});

 
 #Resumo Estatístico das informações contidas na planilha (Somente variaveis quantitativas e não qualitativas).
 #Count - Quantidade de resgistros existentes na planilha
 #Mean  - Média Aritimética dos valores;
 #Std   - Desvio padrão
 #Min   - Menor valor que ocorre entre os registros
 #25%   - 25% são menores ou igual a este valor;
 #50%   - 50% são menores ou igual a este valor;
 #75%   - 75% são menores ou igual a este valor;
 #25%   - Maior valor que ocorre entre os registros;
 resumoEstatistico = dataFrame.describe();
 
 #Resumo estatistico para variáveis categoricas (Variaveis categotias são aquelas qualitativas e nao quantitativas)
 #Geralmente são consideradas variaveis categoricas aquelas que possuem como tipo object, por isso indicamos que desejamos descrever "object"
 #Count - Quantidade de registros existentes para aquela coluna em especifico
 #Unique - Quantidade de categorias distintas existentes na coluna
 # Top - Qual categoria mais aparece na coluna;
 # freq - Com qual frequencia determinada categoria aparece;
 resumoEstatisticoCat = dataFrame.describe(include=["object"]);

 #Descreve de forma organizada todas as categorias existentes na coluna indicada, contabilizando a frequencia em que aparece;
 cargo_count = dataFrame["cargo"].value_counts();


 ################################ Fazendo a análise dos dados ################################

 # 1) Queremos analisar duas empresas, logo precisamos agrupar os valores de acordo com a empresa correspodente.

 informacoes_agrupadas_empresa = dataFrame.groupby('empresa');

 # 2) Tirando a média salarial de cada empresa;

 media_salarial = informacoes_agrupadas_empresa["salario"].mean();
 print("Media Salarial:", media_salarial)

 # 3) Tirando a mediana de cada empresa;

 print("")

 mediana = informacoes_agrupadas_empresa["salario"].median();
 print("Mediana:", mediana)

 print("")

 # 4) Mostrando um resumo dos resultados obtidos por empresa, adicionado do desvio padrão.
 # Aqui estamos agrupando os dados por empresa, e da coluna salario, extraindo a media, mediana e o desvio padrão.
 resultados_empresa = dataFrame.groupby('empresa')["salario"].agg(['mean', 'median', 'std']).reset_index();
 print("Resumo dos dados obtidos em colunas e linhas")
 print(resultados_empresa)
 print("")

 # 5) Agora podemos pegar gerar um resumo estatístico das informações, agrupando por empresa e coluna especifica.
 print("Resumo estatístico dos salarios por empresa")
 resumo_estatistico_empresa = dataFrame.groupby("empresa")["salario"].describe();
 print(resumo_estatistico_empresa)

 # 6) Para deixar ainda melhor, podemos agrupar as informações por cargos e empresa, calculando a média salarial e a mediana, tendo assim uma visão mais estruturada e especifica das informações.
 print("Média Salarial e Mediana: Cargo e Empresa")
 resultados_empresa_cargo = dataFrame.groupby(["cargo", "empresa"])["salario"].agg(["mean", "median"]).reset_index();
 print(resultados_empresa_cargo)
 print("");

# 7) Podemos trazer um resumo estatístico dos salários separados por empresa e cargo.
 print("Resumo estatístico por cargo e empresa")
 resumo_estatistico_empresa_cargo = dataFrame.groupby(['cargo', 'empresa'])["salario"].describe()
 print(resumo_estatistico_empresa_cargo)
 print("")

 # 8) Separando apenas o cargo de estágiario e por empresas
 if "Estagiário" in dataFrame["cargo"].values:
    #Recupera os registros com cargo de estagiário
    estagiarios = dataFrame[dataFrame["cargo"] == "Estagiário"];
    resumo_salario = estagiarios.groupby("empresa")["salario"].describe()
    print("Resumo salarial dos estagiários por empresa")
    print(resumo_salario)



 ################################ Exibindo histograma dos salarios de cada empresa ################################

 # 1) Criando um histograma de salario dos funcionarios para empresa A

 if "Empresa A" in dataFrame["empresa"].values:
     print("Aqui")
     empresas_a = dataFrame[dataFrame["empresa"] == "Empresa A"]
     #Monta o histograma com os registros retornados:
     #Data - Registros para formar o histograma
     # X - Coluna que ficará no eixo X do histograma
     # bins - 
     sb.histplot(data=empresas_a, x='salario', bins=3)
     plt.title('Distribuição Salarial da Empresa A')
     plt.xlabel('Salário')
     plt.ylabel('Número de funcionários')
     plt.show()

#  2) Criando um histograma de salario dos funcionarios para empresa B
 if "Empresa B" in dataFrame["empresa"].values:
    empresas_b = dataFrame[dataFrame["empresa"] == "Empresa B"]
    sb.histplot(data=empresas_b, x="salario", bins=5);
    plt.title("Distribuição Salarial da empresa B")
    plt.xlabel("Salários")
    plt.ylabel("Número de funcionários");
    plt.show()

# 3) Criando um histograma de salario apenas com os estagiários da empresa A
 if "Empresa A" in dataFrame["empresa"].values and "Estagiário" in dataFrame["cargo"].values:
     estagiarios_a = dataFrame[(dataFrame["cargo"] == "Estagiário" ) & (dataFrame["empresa"] == "Empresa A")];
     sb.histplot(data=estagiarios_a, x="salario", bins=3);
     plt.title("Distribuição salarial dos estagiários da Empresa A");
     plt.xlabel("Salários");
     plt.ylabel("Quantidade de estagiários");
     plt.show();

# 3) Criando um histograma de salario apenas com os estagiários da empresa A
 if "Empresa B" in dataFrame["empresa"].values and "Estagiário" in dataFrame["cargo"].values:
   estagiarios_b = dataFrame[(dataFrame["cargo"] == "Estagiário") & (dataFrame["empresa"] == "Empresa B")];
   sb.histplot(data=estagiarios_b, x="salario", bins=3)
   plt.title("Distribuição salarial dos estagiários da Empresa B");
   plt.xlabel("Salários");
   plt.ylabel("Quantidade de estagiários");
   plt.show();

except Exception as error:
    print(error)


################################ Desafio ################################

