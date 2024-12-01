import wikipedia


def search_wikipedia():
    while True:
        try:
            title = input("Enter page title: ")
            if not title:  # Check if input is blank to exit the loop
                print("Thank you.")
                break

            # Search for the page with given title and disable autosuggest
            page = wikipedia.page(title, auto_suggest=False)
            print(f"{page.title}\n{page.summary}\n{page.url}\n")

        except wikipedia.exceptions.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options[:5])  # Show the first 5 disambiguation options

        except wikipedia.exceptions.PageError:
            print(f"Page id \"{title}\" does not match any pages. Try another id!")

        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    search_wikipedia()
