def criacao_treinamento_modelo():    
    import pandas as pd    
    import numpy as np
    import joblib
    from sklearn.ensemble import RandomForestClassifier    
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import LabelEncoder
    from imblearn import under_sampling, over_sampling
    from imblearn.over_sampling import SMOTE
    from sklearn.preprocessing import MinMaxScaler 

    print('Pacotes carregados')

    df = pd.read_csv('dados_coletados.csv')
    print('Dados carregados')

    # Ajustando Estado_Civil
    df['Estado_Civil'] = df['Estado_Civil'].replace(['NENHUM'], 'OUTRO')
    df['Estado_Civil'] = df['Estado_Civil'].replace(['UNIÃO ESTAVEL'], 'CASADO (A)')

   # Criando faixa etária
    bins = [0, 21, 30, 40, 50, 60, 100]
    labels = ['Até 21 anos', 'De 22 até 30 anos', 'De 31 até 40 anos', 'De 41 até 50 anos', 'De 51 até 60 anos', 'Acima de 60 anos']
    df['Faixa_Etaria'] = pd.cut(df['Idade'], bins=bins, labels=labels)

    # Criando faixa salarial
    bins = [-1, 1000, 2000, 3000, 5000, 10000, 20000, 30000, 9000000]
    labels = ['Até 1k', 'De 1k até 2k', 'De 2k até 3k', 'De 3k até 5k', 'De 5k até 10k anos', 'De 10k até 20k', 'De 20k até 30k', 'Acima de 50k']
    df['Faixa_Salarial'] = pd.cut(df['Valor_Renda'], bins=bins, labels=labels)

    # Preenchendo os valores nulos de QT_Dias_Atraso com a mediana dos dados
    # Obtendo medianda
    df['QT_Dias_Atraso'].median()
    # Preenchando
    df['QT_Dias_Atraso'] = df['QT_Dias_Atraso'].fillna((df['QT_Dias_Atraso'].median()))

    # Criando faixa de dias em atraso
    bins = [-1, 30, 60, 90, 180, 240, 360, 500]
    labels = ['Até 30 dias', 'De 31 até 60 dias', 'De 61 até 90 dias', 'De 91 até 180 dias', 'De 181 até 240 dias', 'De 241 até 360 dias', 'Acima de 360 dias']
    df['Faixa_Dias_Atraso'] = pd.cut(df['QT_Dias_Atraso'], bins=bins, labels=labels)
    
    # Criando faixa de prazo de empréstimo
    bins = [0, 60, 120, 200, 720]
    labels = ['Até 60 meses', 'De 61 até 120 meses', 'De 121 até 200 meses', 'Acima de 200 meses']
    df['Faixa_Prazo_Emprestimo'] = pd.cut(df['Prazo_Emprestimo'], bins=bins, labels=labels)

    # Criando faiza de prazo restante de empréstimo
    bins = [-1, 60, 120, 200, 500]
    labels = ['Até 60 meses', 'De 61 até 120 meses', 'De 121 até 200 meses', 'Acima de 200 meses']
    df['Faixa_Prazo_Restante'] = pd.cut(df['Prazo_Restante'], bins=bins, labels=labels)

    # Criando novo dataframe, apenas com as colunas que vamos utilizar

    # Selecionando colunas
    columns = ['Sexo', 'UF_Cliente', 'Perc_Juros', 
        'VL_Emprestimo', 'VL_Emprestimo_ComJuros', 'QT_Total_Parcelas_Pagas',
        'QT_Total_Parcelas_Pagas_EmDia', 'QT_Total_Parcelas_Pagas_EmAtraso',
        'Qt_Renegociacao', 'Estado_Civil', 'QT_Parcelas_Atraso', 'Saldo_Devedor', 
        'Total_Pago', 'Faixa_Prazo_Restante', 'Faixa_Salarial', 'Faixa_Prazo_Emprestimo', 'Faixa_Etaria', 
        'Faixa_Dias_Atraso', 'Possivel_Fraude']

    df_tratado = pd.DataFrame(df, columns=columns)

    # Carregando variáveis categóricas para OneHotEncoding, exceto a variável target
    categoricas = []
    for i in df_tratado.columns[0:18].tolist():
        if df_tratado.dtypes[i] == 'object' or df_tratado.dtypes[i] == 'category':
            categoricas.append(i)

    # Criando o encoder e aplicando o OneHotEncoder
    lb = LabelEncoder()
    for var in categoricas:
        df_tratado[var] = lb.fit_transform(df_tratado[var])

    # Separando as variáveis em preditoras e target
    PREDITORAS = df_tratado.iloc[:, 0:18]
    TARGET = df_tratado.iloc[:, 18]

    # Fazendo o balanceamento das variáveis
    # Para reproduzir o mesmo resultado
    seed = 100
    # Balanceador SMOTE
    balanceador = SMOTE(random_state = seed)
    # Aplicando o balanceador
    PREDITORAS_RES, TARGET_RES = balanceador.fit_resample(PREDITORAS, TARGET)

    # Divisão entre treino e teste
    X_treino, X_teste, Y_treino, Y_teste = train_test_split(PREDITORAS_RES, TARGET_RES, test_size=0.3, random_state=42)

    # Normalização das variáveis
    normalizador = MinMaxScaler()
    X_treino_normalizado = normalizador.fit_transform(X_treino)

    # Criando o classificador com Random Forest
    clf = RandomForestClassifier(n_estimators=100, criterion='entropy', max_depth=3, max_features='sqrt', min_samples_leaf=2, min_samples_split=2, n_jobs=3)
    
    # Construção e treino do modelo
    clf = clf.fit(X_treino_normalizado, Y_treino) 

    # Salvando modelo
    joblib.dump(clf, 'modelo_treinado_fraude.pk')
    print("Modelo criado e salvo com sucesso!")


def main():
    criacao_treinamento_modelo()    


if __name__ == "__main__":
    main()    

