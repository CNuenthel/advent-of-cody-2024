"""
If you set a dictionary value to 0 then check for the existance of the value directly, it may return unintended results.
i.e:
dict = {"9": 0}

Where 0 is Falsey, but in this case it represents an index where the str value "9" is in a list. If we check if the key "9" has a value like this:

if dict.get("9"):
    ...

if dict.get("9") will return False, since this translates to < if 0 > which is interpreted as false, since 0 is falsey.

This is demonstrated by
if 0:
    print("OK")

So ... uh... if you ever set a key to a value of 0, watch out for this.

"""

"""
Update:
    sigh. f#$% this.
"""

with open("day5_input.txt", "r") as f:
    data = f.read()

rows = data.splitlines()

rules = [row for row in rows if len(row) < 6 and row]
books = [row for row in rows if len(row) > 6]

rulebook = {}


def check_rulebook(book):
    glossary = {val: i for i, val in enumerate(book)}

    for num in book:
        applicable_rules = rulebook.get(num)

        if applicable_rules:

            for rule in applicable_rules:
                if rule in glossary.keys():
                    if glossary[rule] < glossary[num]:
                        glossary[rule], glossary[num] = glossary[num], glossary[rule]

    final_book = ["." for i in range(len(glossary.keys()))]
    for k, v in glossary.items():
        final_book[v] = k

    return final_book


# Map rules to page
for rule in rules:
    k, v = rule.split("|")

    if not rulebook.get(k):
        rulebook[k] = [v]
    else:
        rulebook[k].append(v)

vals = []
for book in books:
    pages = book.split(",")
    ls = check_rulebook(pages)
    middle_num_index = len(pages)//2  # Don't forget index counts up from 0 here
    vals.append(int(pages[middle_num_index]))


print(sum(vals))



