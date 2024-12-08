
def applicable_pages(rulebook: dict, present_pages: list, rule_target: str):
    ruled_pages = []
    for page in present_pages:
        if page in rulebook.get(rule_target, []):
            ruled_pages.append(page)
    return ruled_pages

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
            print(f"The applicable rules are {applicable_rules}, lets check them.")

            for rule in applicable_rules:
                if rule in glossary.keys():
                    if glossary[rule] < glossary[num]:
                        return False
    return True

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
    if check_rulebook(pages):
        middle_num_index = len(pages)//2 + 1
        vals.append(int(pages[middle_num_index]))

print(sum(vals))



