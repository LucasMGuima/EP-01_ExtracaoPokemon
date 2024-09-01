# EP-01_ExtracaoPokemon

Extração feita do site: https://pokemondb.net/pokedex/all

---
## Iniciando o projeto

Para iniciar o pojeto primeiro precisamos criar um abiente virtual Python, para isso ná raiz do projeto rodados o seguinte comando:
```
    python -m venv env
```
Agora temos a base do nosso ambiente na raiz do projeto, falta apenas as bibliotecas usadas, para isso rodados o comando:
```
    pip install -r requirements.txt
```
Assim o pip ira ler o arquivo *requirements.txt* e instalar todas as bibliotecas necessárias no nosso ambiente.

Nosso projeto esta pronto para rodar agora.

## Coletanto dados

Podemos colletar nossos dados rodando diretamente as spider com a bibliote scrapy, porem qui temos dois scirpts python para a coleto dos dados:
- Coletando Pokemons:

    Para coletar os dados dos pokemons podemos rodar o script *pokemon.py* que ira salvar os dados no arquivo .csv *./dados/pokemons.csv*
    ```
        python pokemon.py
    ```

- Coletando Abilidades:

    Para coletar os dados de abilidades podemos rodar o script *abilities.py* que ira salvar os dados no aquivo .csv *./dados/abilities.csv*
    ```
        python abilities.py
    ```

## Gerar o JSON
Agora que temos os dados coletados, podemos gerar o JSON. Para isso rodamos diretamente o script *main.py*, que ira tratar os dados de ambos os CSVs, removendo dados faltantes e expandindo colunas compactadas durante a extração dos dados.
```
    python main.py
```
Após rodado o comando a cima, será gerado um arquivo com o nome *./pokemons.json*, onde podemons encontrar todos os dados tratados e as informações a mais das abililidades contidas na tabela *abilities.csv*