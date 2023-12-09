facts = ['you are a dragon']
rules = ['if you are a dragon and you are rich then you eat humans', 'if you eat humans then you drink blood', 'if you are a dragon then you are rich']

def getAntecedents(rule: str):
  aoi = rule.lower().split('if')[1]
  aoi = aoi.split('then')[0]
  aoi = aoi.split('and')
  aoi = [a.strip() for a in aoi]

  return aoi

def getConsequent(rule):
  aoi = rule.lower().split('if')[1]
  aoi = aoi.split('then')[1]

  return aoi.strip()

while True:
  new_facts = []

  for r in rules:
    antecedents = getAntecedents(r)
    consequent = getConsequent(r)

    if consequent in facts:
      continue

    if all([a in facts for a in antecedents]):
      new_facts.append(consequent)

  if len(new_facts) == 0:
    break

  facts += new_facts

print(*facts, sep='\n')