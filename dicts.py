sample = { "key":"value",
"number": 1,
"a_list": []
}

print(sample["key"])
print(sample["number"])
print(sample["a_list"])

#test for a key
if "number" in sample:
    print("it exists")
    if sample["number"] ==1:
        print("it's 1")
    else:
        print("nope on number")
else:
    print("no number")

sample["hoobastank"] = "is a band"
print(sample)