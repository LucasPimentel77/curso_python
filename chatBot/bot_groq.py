from groq import Groq
import json
import requests

def ligar_ar(mensagem):
    print(f'Ligando ar condicionado, {mensagem}')

def desligar_ar(mensagem):
    print(f'Desligando ae condicionado, {mensagem}')

client = Groq(api_key='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')
# client = Groq(api_key=os.getenv("GROQ_API_KEY"))

prompt_do_usuario = input('O que deseja? ')

def processar_mensagem(mensagem):
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": '''
                    Analise a mensagem do usuário para identificar qual é a sua 
                    intenção, e responda com um json no seguinte formato: 
                    {\"intencao\": <numero>, \"resposta\": <texto>}. 
                    No atributo \"intencao\" do JSON, deve haver o número da 
                    intenção, e no atributo \"resposta\", deve haver uma resposta educada para enviar ao usuário. 
                    Caso a intenção seja ligar o ar-condicionado, o número da intenção é 1. 
                    Caso a intenção seja desligar o ar-condicionado, o número da intenção é 2. 
                    Caso o usuário tenha outra intenção, o número é 0. Não dê respostas fora desse formato.
                '''
            },
            {
                "role": "user",
                "content": mensagem
            },
        ],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=False,
        stop=None,
        response_format={'type': 'json_object'}
    )



    resposta_json = completion.choices[0].message.content
    resposta_dados = json.loads(resposta_json)

    return resposta_dados

resposta_dados = processar_mensagem(prompt_do_usuario)
intencao = resposta_dados['intencao']
resposta_ao_usuario = resposta_dados['resposta']

if intencao == 1:
    ligar_ar(resposta_ao_usuario)
elif intencao == 2:
    desligar_ar(resposta_ao_usuario)
else:
    print('COMANDO NÃO RECONHECIDO')
    print(resposta_ao_usuario)
