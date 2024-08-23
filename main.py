import pandas as pd
import tools.tratador as tratador

tratamento = tratador.Tratador()

df_pokemons = pd.read_csv('./dados/pokemons.csv', index_col="pokemon_id")
df_abilities = pd.read_csv('./dados/abilities.csv')

#Remove a parte entre parenteses dos valores nas colunas de peso e altura
df_pokemons['peso'] = df_pokemons['peso'].apply(tratamento.remove_conchetes)
df_pokemons['altura'] = df_pokemons['altura'].apply(tratamento.remove_conchetes)

#Tratar abilidades repetidas
abilidades = df_pokemons['abilities']
abilidades = abilidades.apply(tratamento.tratar_repeticao)
df_pokemons['abilities'] = abilidades

#Verifica quem tem mais abilidades
abilities_count = df_pokemons.loc[df_pokemons['abilities'].apply(tratamento.count_abilities).idxmax()]

#Cria X colunas novas, onde X é a quantidade de abilidades de quem tem mais abilidades
qtd = abilities_count['abilities'].count('|')
for num in range(qtd):
    new_columName = f"abilitie {num+1}"
    df_pokemons[new_columName] = ""

#Coloca as abilidades nas novas colunas
for id, pokemon in df_pokemons.iterrows():
    list_abilidade = pokemon['abilities'].split('|')[0:-1]
    count = 1
    for abilitie in list_abilidade:
        pokemon[f'abilitie {count}'] = abilitie
        count += 1
    df_pokemons.loc[id] = pokemon

#Remove a coluna original de abilidades
df_pokemons = df_pokemons.drop('abilities', axis='columns')
print(df_pokemons.head())
#print(df_abilities.head())