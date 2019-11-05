import telepot # BIBLIOTECA RESPONSAVEL DOS COMANDOS EXISTENTES

bot = telepot.Bot('903074246:AAGSRnjBo_39KVCj-OuxHsWLCGkj3EteSI0') #API DO BOT NO TELEGRAM

id_chat = 915426226 #id chat do ADM do bot

def recebendo(msg): #FUNÇÃO QUE RECEBE A MENSAGEM QUE O BOT RECEBE

    msg_texto = msg['text'] # ARMAZENA A MENSAGEM QUE ENVIARAM AO BOT
    msg_id = msg['chat']['id']  # ARMAZENA O ID DO CHAT DA PESSOA QUE MANDOU MENSAGEM AO BOT

    if msg_texto == '1': # Caso seja 1 a mensagem enviada ele abre a fechadura
        bot.sendMessage(id_chat, "FECHADURA ABERTA!")

    if msg_texto == '2': # Caso 2, envia os dados do banco de dados sobre todas as aberturas da fechadura
        bot.sendMessage(id_chat, "HISTÓRICO!")

    if msg_texto == '3': # Caso 3, captura novamente uma foto
        bot.sendMessage(id_chat, "CAPTURA NOVAMENTE FOTO")

def envia_msg (admin): # função para enviar mensagem ao adm do bot

    # bot.sendPhoto(admin, "FOTO A SER ENVIADA PARA A PESSOA") <- aqui será enviado a foto para o bot

    bot.sendMessage(admin, "INSTRUÇÕES:\n\n"
                           "1- \tABRIR FECHADURA\n\n"
                           "2- \tHISTÓRICO DA FECHADURA\n\n"
                           "3- \tFOTO\n\n") # instruções de como vai funcionar o comando para o bot

envia_msg(id_chat)

telegram = bot.message_loop(recebendo) #loop para ficar recebendo tudo do bot


while True:
        pass






