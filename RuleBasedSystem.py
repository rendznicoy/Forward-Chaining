rules_filename = "rules.txt"
facts_filename = "facts.txt"

while True:
    print(" [1]Input New Fact\n [2]Input New Rule\n [3]Generate New Facts\n [4]Show Existing Facts\n [5]Show Existing Rules\n [6]Exit Program")

    user_input = input("What would you like to do? ")
    print("\n")
    
    if user_input == "1":
        input_fact = input('Input a Fact: ').lower()
        with open(facts_filename, 'r') as facts_file:
            content = facts_file.read()
        if input_fact in content:
            print('Fact already exists')
        else:
            with open(facts_filename, 'a+', encoding='utf-8') as fact_file:
                fact_file.write(input_fact + '\n')
        f = open(facts_filename, "r")
        print(f.read())

    elif user_input == "2":
        input_rule = input('Input a Rule (e.g, "IF A, THEN B" or "IF A and B, THEN C"): ').lower()
        if input_rule.startswith("if ") and ", then " in input_rule:
            with open(rules_filename, 'r') as rules_file:
               content = rules_file.read()
            if input_rule in content:
                print('Rule already exists')
            else:
                with open(rules_filename, 'a+', encoding='utf-8') as rule_file:
                    rule_file.write(input_rule + '\n')
        else:
            print('Invalid rule input format. Rule must start with "IF " followed by conditions and " THEN ".')
        f = open(rules_filename, "r")
        print(f.read())

    elif user_input == "3":
        with open(facts_filename, "r") as facts_file, open(rules_filename, "r") as rules_file:
            existing_facts = set(fact.strip() for fact in facts_file.readlines())
            existing_rules = [rule.strip() for rule in rules_file.readlines()]

        new_facts = set()
    
        for rule in existing_rules:
            conditions, then_statement = rule.split(", then ") # Antecedent and Consequent Split
            conditions = conditions[3:]  # Remove "IF " from the conditions
            conditions = conditions.split(" and ")
        
            if all(cond.strip() in existing_facts for cond in conditions):
                new_facts.add(then_statement)

        with open(facts_filename, 'a+', encoding='utf-8') as fact_file:
            for fact in new_facts:
                if fact not in existing_facts:
                    fact_file.write(fact + '\n')
                    existing_facts.add(fact)

    elif user_input == "4":
        f = open(facts_filename, "r")
        print(f.read())

    elif user_input == "5":
        f = open(rules_filename, "r")
        print(f.read())

    elif user_input == "6":
        break

    user_decision = input("Would like to run the program again? (Y, N): ").upper()
    if user_decision == "Y":
        continue
    elif user_decision == "N":
        print("Have a great day!")
        break
    else:
        print("Invalid Input. Please select 'Y' or 'N' to continue or exit the program")
