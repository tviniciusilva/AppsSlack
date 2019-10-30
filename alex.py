#Importando o método random para usar o choice
import random
#Método utilizado para comunicar com o Slac
from slacker import Slacker

#Defininfo uma função
def orderDaily():

    time = ['Bruno', 'Edson', 'Julian', 'Marco', 'Renata', 'Victor', 'Vinicius', 'Rubens']
    time_ordenado = random.choice(time)
    message = 'O escolhido para começar a falar na Daily hoje foi você: %s' % (time_ordenado);
    slack = Slacker('Seu token começando com xxob')
    return slack.chat.post_message('#service-desk', message)
orderDaily()
