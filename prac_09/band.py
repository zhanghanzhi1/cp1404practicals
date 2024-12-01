class Band:
    def __init__(self, name):
        self.name = name
        self.musicians = []

    def add_musician(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def __str__(self):
        """String representation of the band showing all members and their instruments."""
        band_representation = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({band_representation})"

    def play(self):
        """Simulate each musician in the band playing their instruments."""
        performances = []
        for musician in self.musicians:
            performance = musician.play()
            performances.append(performance)
        return "\n".join(performances)
