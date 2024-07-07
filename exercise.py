class Exercise():
    def __init__(self, id: int, name: str, description: str):
        self.id = id
        self.name = name
        self.description = description

    def update(self, name: str, description: str):
        self.name = name
        self.description = description
        return self

    def __repr__(self):
        return f' {self.exercise}'

Bicep_Curl = Exercise(1, 'Bicep Curl', 'Balabala')
