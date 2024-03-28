# DESENVOLVA UM PROGRAMA QUE O USUÁRIO IRÁ INFORMAR UMA PERGUNTA (UTILIZANDO EXATAMENTE AS PERGUNTAS DO
# QUESTIONÁRIO ANTERIOR) E O SISTEMA DEVERÁ DAR A RESPOSTA.

#1. Qual é o nome completo da protagonista do episódio?
#Joan Taif

#2. Quem dirige a vida de Joan em tempo real para uma série de televisão?
#A interligência artificial.

#3. Qual é o nome do serviço de streaming fictício que parodia a Netflix no episódio?
#Stramberry

#4. Como Joan descobre a existência da série sobre sua vida?
#Quando estava procurando algo para assistir com seu marido.

#5. Qual é a reação inicial de Joan ao descobrir a série e o que ela faz em resposta?
#De ficar em choque ao ver sua vida sendo passada como uma série e tenta arruinar o programa.

#6. Quais são os temas principais explorados neste episódio de Black Mirror?
#A crítica de assinar termos sem ler e de como a inteligiência artifical pode fazer qualquer coisa.

#7. O episódio termina de maneira típica para a série Black Mirror? Explique.
#O episódio termina com a Joan descobrindo que ela era uma variante, mostrando o Plot Twist da série.

while True:

    suaPergunta = input("Faça sua pergunta: ")

    if suaPergunta == "Qual é o nome completo da protagonista do episódio ?":
        print("Joan Taif")
    
    elif suaPergunta == "Quem dirige a vida de Joan em tempo real para uma série de televisão ?":
        print("A Interligência Artificial")

    elif suaPergunta == "Qual é o nome do serviço de streaming fictício que parodia a Netflix no episódio?":
        print("Streamberry")

    elif suaPergunta == "Como Joan descobre a existência da série sobre sua vida ?":
        print("Quando estava procurando algo para assistir com seu marido")

    elif suaPergunta == "Qual é a reação inicial de Joan ao descobrir a série e o que ela faz em resposta ?":
        print("De ficar em choque ao ver sua vida sendo passada como uma série e tenta arruinar o programa")

    elif suaPergunta == "Quais são os temas principais explorados neste episódio de Black Mirror ?":
        print("A crítica de assinar termos sem ler e de como a Inteligiência Artifical pode fazer qualquer coisa")

    elif suaPergunta == "O episódio termina de maneira típica para a série Black Mirror ?":
        print("O episódio termina com a Joan descobrindo que ela era uma variante, mostrando o Plot Twist da série")

    else:
        print("Erro")