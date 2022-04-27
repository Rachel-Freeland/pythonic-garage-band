class Band:

    instances = []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.instances.append(self)
        return

    def play_solos(self):
        soloists = []
        for member in self.members:
            soloists.append(member.play_solos())
        return soloists

    @classmethod
    def to_list(cls):
        return cls.instances

class Musician():
    def __init__(self, name="unknown"):
        self.name = name

class Guitarist(Musician):

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def play_solos(self):
        return "face melting guitar solo"

    def get_instrument(self):
        return "guitar"

class Bassist(Musician):

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    def __str__(self):
        return f"My name is {self.name} and I play bass"

    def play_solos(self):
        return "bom bom buh bom"

    def get_instrument(self):
        return "bass"

class Drummer(Musician):

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def play_solos(self):
        return "rattle boom crash"

    def get_instrument(self):
        return "drums"
