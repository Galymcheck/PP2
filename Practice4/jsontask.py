import json     #is a syntax for storing and exchanging data.

with open("C:/Users/Galam/OneDrive/Документы/VScodes/repositories/PP2/Practice4/sample-data.json", "r") as file:
    data=json.load(file)
print("Interface Status")
print("=" * 80)
print(f"{'DN':53} {'Description':23} {'Speed':10} {'MTU'}")
print("-"*50, " ", "-"*20, " "*2, "-"*6, " "*2, "-"*6)


for item in data["imdata"]:
    attributes=item["l1PhysIf"]["attributes"]

    dn=attributes["dn"]
    descr=attributes["descr"]
    speed=attributes["speed"]
    mtu=attributes["mtu"]

    print(f"{dn:50} {descr:25} {speed:10} {mtu:6}")