from VendingMachineImplement import VendingMachineImpl

products = {
    "CANDY": 10,
    "SNACK": 50,
    "NUTS": 90,
    "Coke": 25,
    "Pepsi": 35,
    "Soda": 45,
}
accepted_coins = [1, 2, 5, 10, 25, 50, 100, 200]
balance = 0

VM = VendingMachineImpl(products, accepted_coins, balance)
VM.insert_money(10)
VM.insert_money(25)
VM.insert_money(18)
VM.select_product("CANDY")
VM.insert_money(200)
VM.insert_money(100)
VM.cancel_request()