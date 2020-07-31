data= {"districtData":
 {
           "Nicobars":
                  {"notes": "", "active": 0, "confirmed": 0, "deceased": 0, "recovered": 0,
                              "delta": {"confirmed": 0, "deceased": 0, "recovered": 0}
                 },
           "North and Middle Andaman":
                  {"notes": "", "active": 0, "confirmed": 1, "deceased": 0, "recovered": 1,
                                 "delta": {"confirmed": 0, "deceased": 0, "recovered": 0}},
           "South Andaman":
                  {"notes": "", "active": 19, "confirmed": 51, "deceased": 0, "recovered": 32,
                                "delta": {"confirmed": 0, "deceased": 0, "recovered": 0}},
           "Unknown":
                  {"notes": "", "active": 34, "confirmed": 67, "deceased": 0, "recovered": 33,
                                "delta": {"confirmed": 0, "deceased": 0, "recovered": 0}}},
    "statecode": "AN"}


states=[x for x in data]
print(states)
dist=[x for x in data['districtData']]
print(dist)
cases=[x for x in data['districtData']['Nicobars'].items()]
print(cases)
d1=dict(cases)
print(d1)
for x in d1['confirmed']:
    print(x)

