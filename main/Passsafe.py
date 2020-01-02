from db import PassVault, session


def gui():
    while True:
        # ask the user if they want to set or check passwords
        answer = input('set or check: ')

        # adds passwords to db/ the vault
        # currently can only set one password per session
        # wont save two passwords for same site
        if answer == 'set':

            pass_vault = PassVault(website=input('Website:'), password=input('Password:'))
            session.add(pass_vault)
            session.commit()
            gui()

        # prints list of passwords long with the websites they belong to
        elif answer == 'check':

            x = session.query(PassVault).all()
            for x in x:
                print(x.__dict__)
                continue

        # exits
        elif answer == 'exit':
            break

gui()
