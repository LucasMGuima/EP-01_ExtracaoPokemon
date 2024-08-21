import pandas as pd

def remove_conchetes(str: str) -> str:
    return str.split('(')[0]

def count_abilities(str: str) -> int:
    count = str.count('|')
    return count

def tratar_repeticao(str: str) -> str:
    palavras = str.split('|')[0:-1]
    tratado = []
    while len(palavras) > 0:
        temp = palavras.pop()
        if temp not in tratado: 
            tratado.append(temp)

    resp = ""
    for palavra in tratado:
        resp += palavra + "|"
    return resp
    


df_pokemons = pd.read_csv('./dados/file.csv', index_col="pokemon_id")
df_abilities = pd.read_csv('./dados/abilities.csv')

#Remove a parte entre parenteses dos valores nas colunas de peso e altura
df_pokemons['peso'] = df_pokemons['peso'].apply(remove_conchetes)
df_pokemons['altura'] = df_pokemons['altura'].apply(remove_conchetes)

#Tratar abilidades repetidas
abilidades = df_pokemons['abilities']
abilidades = abilidades.apply(tratar_repeticao)
df_pokemons['abilities'] = abilidades

abilities_count = df_pokemons.loc[df_pokemons['abilities'].apply(count_abilities).idxmax()]
print(abilities_count)

#print(df_pokemons.head())
#print(df_abilities.head())