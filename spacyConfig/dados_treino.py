# Arquivo: dados_treino.py
# VERSÃO CURADA - Anotações confusas e verbos de estado foram removidos para
# melhorar a consistência e a qualidade do treinamento.

# Formato: (TEXTO_DA_LINHA, [ (PALAVRA_DA_ENTIDADE, "LABEL") ])

DADOS_DE_TREINO = [
    # --- 1. Toda Forma de Poder ---
    ("Eu presto atenção no que eles dizem", [("presto atenção", "ACT"), ("dizem", "ACT")]),
    ("Fidel e Pinochet tiram sarro de você", [("Fidel", "PER"), ("Pinochet", "PER"), ("tiram sarro", "ACT")]),
    ("Que não faz nada", [("faz", "ACT")]),
    ("Você que ama o que faz", [("ama", "ACT"), ("faz", "ACT")]),
    ("E não faz o que ama", [("faz", "ACT"), ("ama", "ACT")]),
    ("Falta, em um domingo azul,", [("domingo", "TEMP")]),
    ("No jornal, da capital", [("jornal", "MIDIA")]),

    # --- 2. Longe Demais das Capitais ---
    ("Um dia desses, eu vou me embora", [("Um dia", "TEMP"), ("vou me embora", "ACT")]),
    ("Um dia desses, eu caio fora", [("Um dia", "TEMP"), ("caio fora", "ACT")]),
    ("Eu 'to vivendo, eu 'to esperando", [("vivendo", "ACT"), ("esperando", "ACT")]),
    ("Eu 'to cansado de esperar", [("esperar", "ACT")]),
    ("Onde a vida corre pra trás", [("corre", "ACT")]),

    # --- 3. A Revolta dos Dândis I ---
    ("Tentando justificar o injustificável", [("justificar", "ACT")]),
    ("Defendendo o seu quintal", [("Defendendo", "ACT")]),
    ("E eu que não fumo, bebi o copo de conhaque", [("bebi", "ACT"), ("conhaque", "PRODUTO")]),
    ("Eu que não bebo, pedi um cigarro", [("pedi", "ACT"), ("cigarro", "PRODUTO")]),
    ("Mas o dândi me disse: 'Rapaz...", [("disse", "ACT")]),

    # --- 4. Infinita Highway ---
    ("Você me faz correr demais", [("correr", "ACT")]),
    ("sabe exatamente onde vai parar", [("parar", "ACT")]),
    ("Nós só precisamos ir", [("ir", "ACT")]),
    ("Nós só queremos viver", [("viver", "ACT")]),
    ("Quando eu vivia e morria na cidade", [("vivia", "ACT"), ("morria", "ACT")]),
    ("E à noite eu acordava banhado em suor", [("noite", "TEMP"), ("acordava", "ACT")]),
    ("Não queremos lembrar o que esquecemos", [("lembrar", "ACT")]),
    ("Um chiclete de menta", [("chiclete de menta", "PRODUTO")]),
    ("Em Porto Alegre ou em Belém", [("Porto Alegre", "LOC"), ("Belém", "LOC")]),
    ("me ajuda, James Dean", [("ajuda", "ACT"), ("James Dean", "PER")]),
    ("um cassete no rádio", [("cassete", "PRODUTO"), ("rádio", "MIDIA")]),

    # --- 5. Terra de Gigantes ---
    ("Eu tenho uma guitarra elétrica", [("guitarra elétrica", "PRODUTO")]),
    ("Antigamente eu sabia exatamente o que fazer", [("Antigamente", "TEMP")]),
    ("Tem uns amigos tocando comigo", [("tocando", "ACT")]),
    ("A juventude é uma banda numa propaganda de refrigerantes", [("propaganda", "MIDIA"), ("refrigerantes", "PRODUTO")]),
    ("As revistas, as revoltas, as conquistas da juventude", [("revistas", "MIDIA")]),

    # --- 6. Até o Fim ---
    ("Não vim até aqui pra desistir agora", [("vim", "ACT"), ("desistir", "ACT"), ("agora", "TEMP")]),
    ("Entendo você, se você quiser ir embora", [("Entendo", "ACT"), ("ir embora", "ACT")]),
    ("nas últimas 24 horas", [("24 horas", "TEMP")]),
    ("Se depender de mim, eu vou até o fim", [("vou", "ACT")]),

    # --- 7. Somos Quem Podemos Ser ---
    ("Um dia me disseram", [("Um dia", "TEMP"), ("disseram", "ACT")]),
    ("Que os ventos às vezes erram a direção", [("erram", "ACT")]),
    ("A chave que abre todas as portas", [("abre", "ACT")]),
    ("Mas a verdade também, às vezes, cura", [("cura", "ACT")]),

    # --- 8. Refrão de Bolero ---
    ("Um beijo de cinema, um amor de almanaque", [("cinema", "MIDIA"), ("almanaque", "MIDIA")]),
    ("Eu que sempre sonhei em ter um Mustang-68", [("sempre", "TEMP"), ("sonhei", "ACT"), ("Mustang-68", "PRODUTO")]),
    ("fazendo cenas de um filme de amor sem fim", [("fazendo", "ACT"), ("filme", "MIDIA")]),
    ("Hoje, eu confesso, meu bem, eu confesso", [("Hoje", "TEMP"), ("confesso", "ACT")]),
    ("um refrão pra dizer o que eu sinto", [("dizer", "ACT")]),

    # --- 9. O Papa é Pop ---
    ("Todo mundo tá relendo o que nunca foi lido", [("relendo", "ACT")]),
    ("Todo mundo tá comprando os mais vendidos", [("comprando", "ACT")]),
    ("O Papa levou um tiro à queima roupa", [("levou um tiro", "ACT")]),
    ("Tá na cara, tá na capa da revista", [("revista", "MIDIA")]),
    ("Os óculos do John ou o olhar do Paul?", [("John", "PER"), ("Paul", "PER")]),

    # --- 10. Era um Garoto Que... ---
    ("Era um garoto que, como eu, amava os Beatles e os Rolling Stones", [("amava", "ACT")]),
    ("Girava o mundo, mas o mundo não lhe era nada demais", [("Girava", "ACT")]),
    ("Cantava as canções que eu cantava", [("Cantava", "ACT")]),
    ("Mas um amigo me falou que ele está vivendo em paz", [("falou", "ACT"), ("vivendo", "ACT")]),
    ("Fazendo rock, o que sempre quis fazer", [("Fazendo", "ACT"), ("fazer", "ACT")]),

    # --- 11. Ando Só ---
    ("Na correnteza do rio, eu, um peixe a nadar", [("nadar", "ACT")]),
    ("No meio da multidão, ando só", [("ando", "ACT")]),
    ("Ando só, como um pássaro voando em pleno ar", [("Ando", "ACT"), ("voando", "ACT")]),
    ("Ando só, como um barco navegando em alto mar", [("Ando", "ACT"), ("navegando", "ACT")]),
    ("Ando só, não sei se sei voltar", [("Ando", "ACT"), ("voltar", "ACT")]),

    # --- 12. Piano Bar ---
    ("O nó que nos une, o abismo que nos separa", [("une", "ACT"), ("separa", "ACT")]),
    ("Eu componho, pra não chorar", [("componho", "ACT"), ("chorar", "ACT")]),

    # --- 13. Ninguém = Ninguém ---
    ("Num carro de aluguel, sem saber pra onde ir", [("ir", "ACT")]),
    ("Procurando abrigo num hotel de beira de estrada", [("Procurando", "ACT")]),

    # --- 14. Parabólica ---
    ("Ela para e fica ali parada", [("para", "ACT"), ("fica", "ACT")]),
    ("Olha um ponto fixo no horizonte", [("Olha", "ACT")]),
    ("Ela abre a porta do seu Opala", [("abre", "ACT"), ("Opala", "PRODUTO")]),
    ("Joga a chave em qualquer canto", [("Joga", "ACT")]),
    ("Deixa a porta aberta", [("Deixa", "ACT")]),
    ("O alarme vai soar", [("soar", "ACT")]),
    ("Que ela não quer mais voltar", [("voltar", "ACT")]),
    ("Girando em torno de si mesma", [("Girando", "ACT")]),

    # --- 15. Pra Ser Sincero ---
    ("Não se sinta capaz de enganar", [("enganar", "ACT")]),
    ("Por ter perdido a calma", [("perdido", "ACT")]),
    ("Por ter vendido a alma ao diabo", [("vendido", "ACT")]),
    ("Talvez a gente se encontre", [("encontre", "ACT")]),

    # --- 16. A Montanha ---
    ("Mais um dia que começa", [("dia", "TEMP"), ("começa", "ACT")]),
    ("Vejo a vida acontecer", [("Vejo", "ACT"), ("acontecer", "ACT")]),
    ("Vejo o sol que me aquece", [("Vejo", "ACT"), ("aquece", "ACT")]),
    ("E eu só quero te encontrar", [("encontrar", "ACT")]),
    ("Subir a montanha, ficar sobre as nuvens", [("Subir", "ACT"), ("ficar", "ACT")]),

    # --- 17. Alucinação ---
    ("Apenas apanhas-te o que era meu", [("apanhas-te", "ACT")]),
    ("E tentas me vender", [("tentas", "ACT"), ("vender", "ACT")]),
    ("Amar como eu amei", [("Amar", "ACT"), ("amei", "ACT")]),
    ("Sonhar como eu sonhei", [("Sonhar", "ACT"), ("sonhei", "ACT")]),

    # --- 18. Eu Que Não Amo Você ---
    ("O meu pente-fino, o meu violão", [("violão", "PRODUTO")]),
    ("O meu coração que bate mais forte lá fora", [("bate", "ACT")]),
    ("A paisagem que não se move", [("move", "ACT")]),
    ("Fico esperando você", [("esperando", "ACT")]),
]

DADOS_DE_VALIDACAO = [
    # --- 19. 3ª do Plural ---
    ("Ela não precisa de ninguém pra dizer o que fazer", [("dizer", "ACT"), ("fazer", "ACT")]),

    # --- 20. Dom Quixote ---
    ("Um dia, sem saber por quê", [("Um dia", "TEMP")]),
    ("Eu saí de casa, eu saí por aí", [("saí", "ACT")]),
    ("Sem pensar em voltar", [("pensar", "ACT"), ("voltar", "ACT")]),
    ("Lutando contra moinhos de vento", [("Lutando", "ACT")]),

    # --- 21. Dançando no Campo Minado ---
    ("Não há mais o que dizer", [("dizer", "ACT")]),
    ("Não há mais o que fazer", [("fazer", "ACT")]),
    ("Nós dançamos no campo minado", [("dançamos", "ACT")]),
    ("E não há mais pra onde correr", [("correr", "ACT")]),

    # --- 22. Vida Real ---
    ("A vida real não tem trilha sonora", [("trilha sonora", "MIDIA")]),
    ("A vida real, a gente inventa", [("inventa", "ACT")]),
    ("Na vida real, a gente se vira", [("vira", "ACT")]),
    ("A cada dia, a cada manhã", [("dia", "TEMP"), ("manhã", "TEMP")]),
]