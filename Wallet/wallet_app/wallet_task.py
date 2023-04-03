'''from .models import wallet

def create_wallet(data):
    # To create wallet and push data to DB
    print(data)
    wallet_obj = wallet()
    wallet_obj.id = data["id"]
    wallet_obj.name = data["name"]
    print("---------")
    wallet_obj.save()
    print("Test")

def get_wallets():
    # Returns the list of wallets
    objects = wallet.objects.all()
    for i in objects:
        print(i.id)
    print("test2")'''
