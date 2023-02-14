import json
f = open('sample-data.json')

dictionary = json.loads(f.read())

list1 = dictionary['imdata']

print("Interface Status")
print('================================================================================')
print("DN                                                 Description           Speed    MTU ")
print("-------------------------------------------------- --------------------  ------  ------")
for x in (list1):
    print(f'{x["l1PhysIf"]["attributes"]["dn"]}                               {x["l1PhysIf"]["attributes"]["speed"]}  {x["l1PhysIf"]["attributes"]["mtu"]}')