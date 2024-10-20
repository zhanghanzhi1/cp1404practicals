def main():
    """Processing and display Wimbledon data from the file."""
    filename = 'wimbledon.csv'
    champions, countries = read_wimbledon_data(filename)
    champion_count = count_champions(champions)
    display_champion_information(champion_count, countries)


def read_wimbledon_data(filename):
    """Read Wimbledon data from file and return a list of champions and a set of countries."""
    champions = []
    countries = set()

    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)
        for line in in_file:
            parts = line.strip().split(',')
            country, champion = parts[1], parts[2]
            champions.append(champion)
            countries.add(country)

    return champions, countries


def count_champions(champions):
    """Count the number of times each champion has won and return a dictionary."""
    champion_count = {}
    for champion in champions:
        champion_count[champion] = champion_count.get(champion, 0) + 1
    return champion_count


def display_champion_information(champion_count, countries):
    """Display the champion counts and countries in a formatted manner."""
    print("Wimbledon Champions:")
    for champion, count in sorted(champion_count.items()):
        print(f"{champion} {count}")

    sorted_countries = sorted(countries)
    countries_string = ", ".join(sorted_countries)
    print(f"\nThese {len(sorted_countries)} countries have won Wimbledon:\n{countries_string}")


main()
