import openai
from get_env import print_env

env = print_env(['app_key'])

# Configurando ambiente
openai.api_key = env['app_key']

# Configurador modelo model_engine 
model  = 'text-davinci-003'

while True:
    print(15*'-')
    prompt = input('Faça sua pergunta: ')
    print('O ChatGPT está processando sua resposta')
    # Gera resposta
    completion = openai.Completion.create(
        engine = model
        ,prompt = prompt
        ,temperature =  0
        ,max_tokens = 1080     
    )

    print(15*'-')
    response = completion.choices[0].text
    print(response)

    fechar = input('Você deseja fazer mais perguntas?')
    if fechar == 'não' or 'nao':
        break