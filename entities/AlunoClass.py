class Aluno:
    def __init__(self, mat, nom):
        self.mat = mat
        self.nom = nom
    
    @property    
    def getMatAluno(self):
        return self.mat

    @property
    def setMatAluno(self, mat):
        self.mat = mat

    @property
    def getNomAluno(self):
        return self.nom

    @property
    def setNomAluno(self, nom):
        self.nom = nom

    def __str__(self):
        return f'{self.mat} - {self.nom}'