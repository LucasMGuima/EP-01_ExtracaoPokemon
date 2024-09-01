import pandas as pd
import tools.tratador as tratador

tratamento = tratador.Tratador()

def explode_colunas(df: pd.DataFrame, nome_coluna: str, nome_novas_colunas: str) -> pd.DataFrame:
    """
        Explode uma coluna expecifica em varias novas colunas.

        Keyword arguments: \n
        **df** -> DataFrame do pandas que sera operado. \n
        **nome_coluna** -> Nome da coluna a ser explodida. \n
        **nome_novas_colunas** -> Nome que será dado as novas colunas. \n

        Return: \n
        Retorna um DataFrame pandas com as novas colunas e sem a coluna explodida
    """
    #Tratar dados repetidas
    coluna = df[nome_coluna]
    coluna = coluna.apply(tratamento.tratar_repeticao)
    df[nome_coluna] = coluna

    #Verifica quem tem mais entradas na coluna [nome_coluna]
    elemento = df.loc[df[nome_coluna].apply(tratamento.count_abilities).idxmax()]

    #Cria X colunas novas, onde X é a quantidade de abilidades de quem tem mais abilidades
    qtd = elemento[nome_coluna].count('|')
    for num in range(qtd):
        new_columName = f"{nome_novas_colunas} {num+1}"
        df[new_columName] = ""

    #Coloca as abilidades nas novas colunas
    for id, elemento in df.iterrows():
        list = elemento[nome_coluna].split('|')[0:-1]
        count = 1
        for i in list:
            if '#' in i:
                nome = str(i).split('-')[1]
                if nome == elemento['pokemon_name']:
                    continue
            elemento[f'{nome_novas_colunas} {count}'] = i
            count += 1
        df.loc[id] = elemento

    #Remove a coluna original
    df = df.drop(nome_coluna, axis='columns')
    return df

df_pokemons = pd.read_csv('./dados/pokemons.csv', index_col="pokemon_id")
df_abilities = pd.read_csv('./dados/abilities.csv')

#Remove a parte entre parenteses dos valores nas colunas de peso e altura
df_pokemons['peso'] = df_pokemons['peso'].apply(tratamento.remove_conchetes)
df_pokemons['altura'] = df_pokemons['altura'].apply(tratamento.remove_conchetes)

#Explode a coluna de evolucao, colocando cada evolucao em uma coluna separada
df_pokemons = explode_colunas(df_pokemons, 'evolutions', 'evolucao')
#Faz o mesmo com as abilidade
df_pokemons = explode_colunas(df_pokemons, 'abilities', 'abilidade')

df_juncao: pd.DataFrame = pd.DataFrame()

for colum_name in df_pokemons.columns:
    if 'abilidade' in colum_name:
        df_temp = pd.merge(df_pokemons, df_abilities, left_on=colum_name, right_on='nome')
        df_juncao = pd.concat([df_juncao, df_temp])

df_juncao.to_json('pokemons.json', 'records')