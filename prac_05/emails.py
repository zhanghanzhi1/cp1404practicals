def main():
    """Get, stored and display users email and name."""
    email_dict = collect_emails()
    print_stored_emails(email_dict)


def collect_emails():
    """Collect emails from the user until a blank email is entered."""
    email_dict = {}
    email = input("Email: ").strip()
    while email != "":
        add_email_to_dict(email_dict, email)
        email = input("Email: ").strip()
    return email_dict


def add_email_to_dict(email_dict, email):
    """Add email and corresponding name to the dictionary."""
    name = extract_name(email)
    confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()
    if confirmation in ('', 'y'):
        email_dict[email] = name
    else:
        name = input("Name: ").strip().title()
        email_dict[email] = name


def extract_name(email):
    """Extract and format the name from the email address."""
    name_part = email.split('@')[0]
    name = name_part.replace('.', ' ').title()
    return name


def print_stored_emails(email_dict):
    """Print all stored emails and names."""
    print("")
    for email, name in email_dict.items():
        print(f"{name} ({email})")


main()
