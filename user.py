class User:
    def __init__(self, id: int, email: str, first_name: str, last_name: str):
        self.id = id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.active = False

    def update(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        return self
    
    def activate(self):
        self.active = True
        return self

    def __repr__(self):
        return f' {self.first_name}'