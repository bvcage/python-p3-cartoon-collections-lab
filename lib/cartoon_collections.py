def roll_call_dwarves(dwarves):
    for n in range(0, len(dwarves)):
        print(f"{n+1}. {dwarves[n]}")

def summon_captain_planet(planeteers):
    # for n in range(0, len(planeteers)):
    #     planeteers[n] = planeteers[n].capitalize() + "!"
    planeteers = [ el.capitalize() + "!" for el in planeteers]
    return planeteers

def long_planeteer_calls(calls):
    has_long = False
    num = 0
    while num < len(calls) and not has_long:
        if len(calls[num]) > 4:
            has_long = True
        num += 1
    return has_long

def find_the_cheese(foods):
    cheeses = ["cheddar", "gouda", "camembert"]
    this_cheese = None
    num = 0
    while this_cheese == None and num < len(foods):
        if foods[num] in cheeses:
            this_cheese = foods[num]
        num += 1
    return this_cheese
