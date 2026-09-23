class Conteudo:
    def __init__(self, titulo, genero):
        self.titulo = titulo
        self.genero = genero

    def exibir_info(self):
        print(f"Título: {self.titulo} | Gênero: {self.genero}")

class Filme(Conteudo):
    def __init__(self, titulo, genero, duracao):
        super().__init__(titulo, genero)
        self.duracao = duracao

    def exibir_info(self):
        print(f"[FILME] {self.titulo} | Gênero: {self.genero} | Duração: {self.duracao} min")

class Serie(Conteudo):
    def __init__(self, titulo, genero, temporadas):
        super().__init__(titulo, genero)
        self.temporadas = temporadas

    def exibir_info(self):
        print(f"[SÉRIE] {self.titulo} | Gênero: {self.genero} | Temporadas: {self.temporadas}")

class Documentario(Conteudo):
    def __init__(self, titulo, genero, tema):
        super().__init__(titulo, genero)
        self.tema = tema

    def exibir_info(self):
        print(f"[DOC] {self.titulo} | Gênero: {self.genero} | Tema: {self.tema}")

class Podcast(Conteudo):
    def __init__(self, titulo, genero, episodios):
        super().__init__(titulo, genero)
        self.episodios = episodios

    def exibir_info(self):
        print(f"[PODCAST] {self.titulo} | Gênero: {self.genero} | Episódios: {self.episodios}")


catalogo = [
    Filme("Interestelar", "Ficcao", 169),
    Filme("Shrek", "Animacao", 90),
    Serie("Stranger Things", "Ficcao", 4),
    Serie("Round 6", "Suspense", 2),
    Documentario("Nosso Planeta", "Natureza", "Vida selvagem"),
    Podcast("Mano a Mano", "Entrevistas", 40)
]

for item in catalogo:
    item.exibir_info()