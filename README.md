# Teste Data Engineer Contabilizei

### Primeiro passo para a execução do programa é a instalação do Python 2.7. 

Segue o link para download:
  https://www.python.org/downloads/release/python-272/
  
Para seguir os próximos passos certifique-se se o PIP está instalado em seu computador.

    Windows:
    
    http://timmyreilly.azurewebsites.net/python-pip-virtualenv-installation-on-windows/
    
    Linux:
    
    https://www.tecmint.com/install-pip-in-linux/
  
### O ambiente precisa ser preparado para rodar o programa python, para isso você precisa seguir as seguintes instruções:

##### 1) Realizar o clone do projeto no gitHub em uma pasta no seu computador.
        
##### 2) Instalar as bibliotecas necessárias para o projeto utilizando o seguinte comando no diretorio raiz do projeto:


    pip install -r requirements.txt

##### 3) O arquivo principal do projeto é o main.py. Para acessar as funcionalidades é necessário passar 2 parâmetros na execução do arquivo principal, conforme o exemplo:

    
    python main.py --product <PRODUCT> --company_state <COMPANY_STATE>
 
 Exemplos:
 
    python main.py --product water --company_state PR
    
    python main.py --company_state PR
    
    python main.py --product water
  
##### 4) Ao executar o arquivo principal a saída do app será:

    As buscas podem ser encontradas em  c:\0.COMPUTADOR\45.TesteContabilizei\busca_18H_15M_25S

    Busca realizada por water em SP

    Quantidade total de empresas encontradas:  29

    Descricao de todas as empresas localizadas:

    product | company_Id | product_price | company_state

    [u'water'] | 2a79ea27c279e471 | 63.358604 | [u'MG', u'SP']

    [u'water'] | dc6a70712a252123 | 14.865083 | [u'SP']

    [u'water'] | c6036a69be21cb66 | 83.00743 | [u'SP']

    [u'water'] | 4fa7c62536118cc4 | 67.50108 | [u'SP', u'RJ']

    ...

    [u'water'] | 1340ccf24722f02b | 98.81429 | [u'MG', u'SP']


    [u'water'] | 6f3a770e5af1fd4c | 45.493538 | [u'SP']

    [u'water'] | 78f1893678afbeaa | 10.481072 | [u'SP']

    [u'water'] | 28659414dab9eca0 | 21.5459 | [u'PR', u'SP']

    [u'water'] | f6a4f71e72dfe084 | 73.40578 | [u'SP', u'RJ']

    [u'water'] | 09a8a8976abcdfde | 93.41136 | [u'SP', u'BA']
