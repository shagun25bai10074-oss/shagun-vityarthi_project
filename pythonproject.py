import  random

# Create a fictitious transaction function def create_transaction():
def create_transaction():
    Place = random.choice (["Shop", "Online", "Abroad"])
    Amount = round(random.uniform(1, 1000), 2)
    period = random.choice (["Day", "Night"])
    return {"amount": Amount, "place": Place, "period": period}

# Simple logic to detect fraud
def detect_fraud(trx):
    if trx["amount"] > 750 and trx["place"] == "Abroad" and trx["period"] == "Night":
        return True
    else:
        return False

# For a number in range (8), simulate 8 transactions:
#trx is same to create_transaction()
for number in range(8):
    tx = create_transaction()
print (f"Transaction {number+1}: {tx}")
if detect_fraud(tx):
    print ("Status: Fraud Detected")
else:
    print ("Status: Safe")