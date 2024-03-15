from random import choice, choices
import time, json
from operator import itemgetter


class Artifact:
    def __init__(self, type, mainstat, mainstat_value, threeliner, substats, level, last_upgrade="", roll_value=0):
        self.type = type
        self.mainstat = mainstat
        self.mainstat_value = mainstat_value
        self.threeliner = threeliner
        self.substats = substats
        self.level = level
        self.last_upgrade = last_upgrade
        self.roll_value = roll_value
        if "Crit RATE%" in self.substats:
            if self.substats["Crit RATE%"] == 23.0:
                self.substats["Crit RATE%"] = 22.9

    def __str__(self):
        val = (self.mainstat_value[0])[self.mainstat_value[1]]

        return f"{val} {self.mainstat} {self.type} (+{self.level})"

    def subs(self):
        sub_stats = {
            sub: round(self.substats[sub], 1)
            if "%" in sub else round(self.substats[sub])
            for sub in self.substats
        }
        return sub_stats

    def print_stats(self):
        print(self)
        for i in self.substats:
            is_percentage = '%' in i
            print(
                f"- {i}: {str(round(self.substats[i], 1)) if is_percentage else round(self.substats[i])}{' (+)' if i == self.last_upgrade else ''}")
        self.last_upgrade = ""
        print()

    def upgrade(self):
        if self.level != 20:
            roll = choice(possible_rolls)
            if self.threeliner:
                self.substats[self.threeliner] = max_rolls[
                                                     self.threeliner] * roll
                self.last_upgrade = self.threeliner
                self.threeliner = 0
            else:
                sub = choice(list(self.substats.keys()))
                self.substats[sub] += max_rolls[sub] * roll
                self.last_upgrade = sub
            self.level += 4
            self.mainstat_value[1] += 1
            self.roll_value += roll * 100

    def cv(self):
        crit_value = 0
        if "Crit DMG%" in self.substats:
            crit_value += round(self.substats["Crit DMG%"], 1)
        if "Crit RATE%" in self.substats:
            crit_value += round(self.substats["Crit RATE%"], 1) * 2
        return round(crit_value, 1)

    def rv(self):
        return int(self.roll_value)


class ArtifactEncoder(json.JSONEncoder):
    def default(self, art):
        return [art.type, art.mainstat, art.mainstat_value, art.threeliner, art.substats, art.level, art.last_upgrade, art.roll_value]


artifact_types = ('Flower', 'Feather', 'Sands', 'Goblet', 'Circlet')
sands_main_stats = ('HP%', 'ATK%', 'DEF%', 'ER%', 'EM')
goblet_main_stats = ('Pyro DMG% Bonus', 'Hydro DMG% Bonus', 'Cryo DMG% Bonus',
                     'Electro DMG% Bonus', 'Anemo DMG% Bonus',
                     'Geo DMG% Bonus', 'Physical DMG% Bonus',
                     'Dendro DMG% Bonus', 'HP%', 'ATK%', 'DEF%', 'EM')
circlet_main_stats = ('HP%', 'ATK%', 'DEF%', 'EM', 'Crit DMG%', 'Crit RATE%',
                      'Healing Bonus')
substats = ('HP', 'ATK', 'DEF', 'HP%', 'ATK%', 'DEF%', 'ER%', 'EM',
            'Crit RATE%', 'Crit DMG%')
flower_stats = (717, 1530, 2342, 3155, 3967, 4780)
feather_stats = (47, 100, 152, 205, 258, 311)
hp_atk_dmg_stats = (7.0, 14.9, 22.8, 30.8, 38.7, 46.6)
def_stats = (8.7, 18.6, 28.6, 38.5, 48.4, 58.3)
em_stats = (28, 60, 91, 123, 155, 187)
er_stats = (7.8, 16.6, 25.4, 34.2, 43.0, 51.8)
healing_bonus_stats = (5.4, 11.5, 17.6, 23.7, 29.8, 35.9)
crit_rate_stats = (4.7, 9.9, 15.2, 20.5, 25.8, 31.1)
crit_dmg_stats = (9.3, 19.9, 30.5, 41.0, 51.6, 62.2)
max_rolls = {
    'HP': 298.75,
    'ATK': 19.4500007629394,
    'DEF': 23.1499996185302,
    'HP%': 5.8335,
    'ATK%': 5.8335,
    'DEF%': 7.28999972343444,
    'EM': 23.3099994659423,
    'ER%': 6.48000016808509,
    'Crit RATE%': 3.88999991118907,
    'Crit DMG%': 7.76999965310096
}
possible_rolls = (0.7, 0.8, 0.9, 1.0)

sands_main_stats_weights = (26.68, 26.66, 26.66, 10.0, 10.0)
goblet_main_stats_weights = (5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 19.25,
                             19.25, 19.0, 2.5)
circlet_main_stats_weights = (22.0, 22.0, 22.0, 4.0, 10.0, 10.0, 10.0)
substats_weights = (6, 6, 6, 4, 4, 4, 4, 4, 3, 3)


def take_input():
    valid_exit = ('exit', "'exit'", '"exit"')
    ok1 = False
    ok2 = False
    print("\nPlease input conditions. Type 'exit' to go back to menu.\nLeave blank to use defaults (1 test, 50 CV).\n")

    while not ok1:
        size = input("Number of tests to run: ")
        if size:
            if size.lower() in valid_exit:
                return 'exit', 0
            try:
                if int(size) > 0:
                    ok1 = True
                else:
                    print("Needs to be positive. Try again.\n")
            except ValueError:
                print("Needs to be an integer. Try again.\n")
        else:
            ok1 = True
            size = 1

    while not ok2:
        cv = input("Desired Crit Value: ")
        if cv:
            if cv.lower() in valid_exit:
                return 0, 'exit'
            try:
                if float(cv) > 0:
                    ok2 = True
                else:
                    print("Needs to be positive. Try again.\n")
            except ValueError:
                print("Needs to be a number. Try again.\n")
        else:
            ok2 = True
            cv = 50

    print(f"Running {int(size)} simulation{'s' if int(size) != 1 else ''}, looking for at least {float(cv)} CV.")
    return size, cv


def create_artifact(source):
    type = choice(artifact_types)
    rv = 0
    if type == 'Flower':
        mainstat = 'HP'
    elif type == 'Feather':
        mainstat = 'ATK'
    elif type == 'Sands':
        mainstat = choices(sands_main_stats,
                           weights=sands_main_stats_weights)[0]
    elif type == 'Goblet':
        mainstat = choices(goblet_main_stats,
                           weights=goblet_main_stats_weights)[0]
    else:
        mainstat = choices(circlet_main_stats,
                           weights=circlet_main_stats_weights)[0]

    if mainstat == 'HP':
        mainstat_value = [flower_stats, 0]
    elif mainstat == 'ATK':
        mainstat_value = [feather_stats, 0]
    elif mainstat in ('Pyro DMG% Bonus', 'Hydro DMG% Bonus', 'Cryo DMG% Bonus',
                     'Electro DMG% Bonus', 'Anemo DMG% Bonus',
                     'Geo DMG% Bonus', 'Physical DMG% Bonus',
                     'Dendro DMG% Bonus', 'HP%', 'ATK%'):
        mainstat_value = [hp_atk_dmg_stats, 0]
    elif mainstat == 'DEF%':
        mainstat_value = [def_stats, 0]
    elif mainstat == 'ER%':
        mainstat_value = [er_stats, 0]
    elif mainstat == 'EM':
        mainstat_value = [em_stats, 0]
    elif mainstat == 'Healing Bonus%':
        mainstat_value = [healing_bonus_stats, 0]
    elif mainstat == 'CRIT Rate%':
        mainstat_value = [crit_rate_stats, 0]
    else:
        mainstat_value = [crit_dmg_stats, 0]

    fourliner_weights = (2, 8) if source == 'domain' else (34, 66)
    fourliner = choices((1, 0), weights=fourliner_weights)[0]
    subs = {}

    subs_pool = list(substats)
    subs_weights = list(substats_weights)
    if mainstat in subs_pool:
        subs_weights.remove(subs_weights[subs_pool.index(mainstat)])
        subs_pool.remove(mainstat)

    for _i in range(3 + fourliner):
        roll = choice(possible_rolls)
        sub = choices(subs_pool, weights=subs_weights)[0]
        subs_weights.remove(subs_weights[subs_pool.index(sub)])
        subs_pool.remove(sub)
        subs[sub] = max_rolls[sub] * roll
        rv += roll * 100

    threeliner = choices(subs_pool,
                         weights=subs_weights)[0] if not fourliner else 0

    return Artifact(type, mainstat, mainstat_value, threeliner, subs, 0, "", rv)


def create_and_roll_artifact(arti_source, highest_cv=0):
    artifact = create_artifact(arti_source)
    if not highest_cv:
        artifact.print_stats()
    for j in range(5):
        artifact.upgrade()
        if not highest_cv:
            artifact.print_stats()
    if highest_cv:
        if artifact.cv() > highest_cv:
            highest_cv = artifact.cv()
            print(f'Day {day}: {artifact.cv()} CV ({artifact}) - {artifact.subs()}')
    return artifact, highest_cv


def upgrade_to_next_tier(artifact):
    if artifact.level == 20:
        print("Artifact already at +20\n")
    else:
        print('Upgrading...\n')
        artifact.upgrade()
        artifact.print_stats()


def upgrade_to_max_tier(artifact, do_we_print=True):
    if artifact.level == 20:
        print("Artifact already at +20\n")
    else:
        print('Upgrading to +20...\n')
        while artifact.level < 20:
            artifact.upgrade()
            if do_we_print:
                artifact.print_stats()
        if not do_we_print:
            artifact.print_stats()


def compare_to_highest_cv(artifact, fastest, slowest, days_list, day_number, cv_want):
    flag_break = False
    if artifact.cv() >= min(54.5, cv_want):
        days_list.append(day_number)
        if fastest[0] == 0 or day_number < fastest[0]:
            fastest = (day_number, artifact)
        if day_number > slowest[0]:
            slowest = (day_number, artifact)
        # print(artifact.subs())
        flag_break = True
    return fastest, slowest, days_list, flag_break


def print_inventory(list_of_artifacts):
    print("Inventory:\n")
    t1 = list_of_artifacts[0].type
    print('-' * 43, f'{t1}{"s" if t1 != "Sands" else ""}', '-' * 43)
    for i in range(len(list_of_artifacts)):
        print(f'{i + 1}) {list_of_artifacts[i]} - {list_of_artifacts[i].subs()}')
        if i + 1 < len(list_of_artifacts):
            t2 = list_of_artifacts[i + 1].type
            if t2 != list_of_artifacts[i].type:
                print('\n' + '-' * 43, f'{t2}{"s" if t2 != "Sands" else ""}', '-' * 43)


def print_controls():
    print('\n' +
          '=' * 27 + ' CONTROLS ' + '=' * 27 + '\n\n'
                                               '---------------- ACTIONS WITH GENERATED ARTIFACT ---------------\n\n'
                                               'a = show generated artifact\n'
                                               '\n'
                                               'a rv = show its roll value\n'
                                               'a cv = show crit value\n'
                                               '+ = upgrade to next tier\n'
                                               '++ = upgrade to +20\n'
                                               '\n'
                                               's = save to inventory\n'
                                               'del = remove from inventory\n'
                                               '\n'
                                               'r = re-roll\n'
                                               'r++ = re-roll and upgrade to +20\n'
                                               '\n'
                                               '-------------------- ACTIONS WITH INVENTORY --------------------\n\n'
                                               'inv = show inventory\n'
                                               'inv cv = show artifact with highest crit value\n'
                                               'inv rv = show inventory with highest roll value\n'
                                               'inv [index] = show artifact from inventory (use index from \'inv\' view)\n'
                                               'inv [index1,index2,...] +/++/cv/rv/del = perform action with artifact in inv\n'
                                               'inv c = clear inventory\n'
                                               '\n'
                                               '------------------------ OTHER COMMANDS -----------------------\n\n'
                                               'domain = change artifact source to domain (default)\n'
                                               'strongbox = change artifact source to strongbox\n'
                                               'source = view current source\n'
                                               '\n'
                                               'exit = go back to menu\n'
                                               '\n'
                                               '================================================================\n'
          )


def print_menu():
    print('\n' + '=' * 29 + " MENU " + '=' * 29 + '\n')
    print("0 = exit the simulator\n"
          "1 = roll artifacts until a certain CV is reached\n"
          "2 = roll one artifact at a time\n")


sort_order_type = {'Flower': 0, 'Feather': 1, 'Sands': 2, 'Goblet': 3, 'Circlet': 4}
sort_order_mainstat = {'ATK': 0,
                       'HP': 1,
                       'Crit DMG%': 2, 'Crit RATE%': 3,
                       'EM': 4,
                       'Pyro DMG% Bonus': 5, 'Hydro DMG% Bonus': 6, 'Cryo DMG% Bonus': 7, 'Electro DMG% Bonus': 8,
                       'Anemo DMG% Bonus': 9, 'Dendro DMG% Bonus': 10, 'Geo DMG% Bonus': 11, 'Physical DMG% Bonus': 12,
                       'ER%': 13,
                       'Healing Bonus': 14,
                       'ATK%': 15,
                       'HP%': 16,
                       'DEF%': 17,
                       }
valid_help = ['help', "'help'", '"help"']
valid_picks = ['0', 'exit', '1', '2']
with open('.\\inventory.txt') as file:
    data = file.read()
artifact_list = json.loads(data)
artifact_list = [Artifact(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]) for i in artifact_list]
while True:
    print_menu()
    while True:
        automate = input('Your pick: ')
        if automate.lower() in valid_picks:
            break
        else:
            print('Commands are 0, 1 or 2\n')
    print("For the list of commands, type 'help'\n" if automate == '2' else "")
    print('=' * 64)
    if automate == "1":
        sample_size, cv_desired = take_input()
        if sample_size == 'exit' or cv_desired == 'exit':
            print("Going back to menu")
            continue
        else:
            sample_size, cv_desired = int(sample_size), float(cv_desired)
        days_it_took_to_reach_50_cv = []
        low = (0, Artifact('this', 'needs', 'to', 'be', 'done', 0))
        high = (0, Artifact('this', 'needs', 'to', 'be', 'done', 0))
        start = time.perf_counter()
        for i in range(sample_size):
            c = 0
            day = 0
            highest = 0.1
            inventory = 0
            flag = False
            print(f'\nSimulation {i + 1}:' if sample_size > 1 else '')
            while not flag:
                day += 1
                # print(f'new day {day}')
                if day % 10000 == 0:
                    print(f'Day {day} - still going')
                resin = 180
                if day % 7 == 1:
                    resin += 60
                while resin:
                    # print('domain run')
                    resin -= 20
                    amount = choices((1, 2), weights=(93, 7))
                    # if amount[0] == 2:
                    #     print('lucky!')
                    inventory += amount[0]
                    for k in range(amount[0]):
                        art, highest = create_and_roll_artifact("domain", highest)
                        low, high, days_it_took_to_reach_50_cv, flag = compare_to_highest_cv(art, low, high,
                                                                                             days_it_took_to_reach_50_cv,
                                                                                             day, cv_desired)
                        if flag:
                            break
                    if flag:
                        break
                else:
                    while inventory >= 3:
                        # print(f'strongbox {inventory}')
                        inventory -= 2
                        art, highest = create_and_roll_artifact("strongbox", highest)
                        low, high, days_it_took_to_reach_50_cv, flag = compare_to_highest_cv(art, low, high,
                                                                                             days_it_took_to_reach_50_cv,
                                                                                             day, cv_desired)
                        if flag:
                            break
                    # print(f'{inventory} left in inventory')

        print()
        days = round(sum(days_it_took_to_reach_50_cv) / sample_size, 2)
        if sample_size > 1:
            print(
                f'Out of {sample_size} simulations, it took an average of {days} days ({round(days / 365.25, 2)} years) to reach {cv_desired} CV.')
            print(f'Fastest - {low[0]} days: {low[1].subs()}')
            print(f'Slowest - {high[0]} days ({round(high[0] / 365.25, 2)} years): {high[1].subs()}')
        else:
            print(f'It took {low[0]} days (or {round(high[0] / 365.25, 2)} years)!')
        end = time.perf_counter()
        run_time = end - start
        to_hours = time.strftime("%T", time.gmtime(run_time))
        decimals = f'{(run_time % 1):.3f}'
        print()
        print(f'The simulation took {to_hours}:{str(decimals)[2:]} ({run_time:.3f} seconds)')
    elif automate == "2":
        source = "domain"
        print()
        art = create_artifact(source)

        art.print_stats()
        while True:
            user_command = input('Command: ').lower()

            if user_command in ('+', 'a+', 'a +'):
                upgrade_to_next_tier(art)
                if art in artifact_list:
                    artifact_list.sort(key=lambda x: (sort_order_type[x.type], sort_order_mainstat[x.mainstat], -x.level))
                    with open(r'.\inventory.txt', 'w') as file:
                        file.write(str(json.dumps(artifact_list, cls=ArtifactEncoder)))
            elif user_command in ('++', 'a++', 'a ++'):
                upgrade_to_max_tier(art)
                if art in artifact_list:
                    artifact_list.sort(key=lambda x: (sort_order_type[x.type], sort_order_mainstat[x.mainstat], -x.level))
                    with open(r'.\inventory.txt', 'w') as file:
                        file.write(str(json.dumps(artifact_list, cls=ArtifactEncoder)))
            elif user_command == 'r':
                print('Re-rolling...\n')
                art = create_artifact(source)
                art.print_stats()

            elif user_command in ('r++', 'r ++'):
                print('Re-rolling and upgrading...\n')
                art, _ = create_and_roll_artifact(source)

            elif user_command in ('s', 'save'):
                if art not in artifact_list:
                    artifact_list.append(art)
                    artifact_list.sort(key=lambda x: (sort_order_type[x.type], sort_order_mainstat[x.mainstat], -x.level))
                    with open(r'.\inventory.txt', 'w') as file:
                        file.write(str(json.dumps(artifact_list, cls=ArtifactEncoder)))
                    print(f'Saved - {len(artifact_list)} artifact{"s" if len(artifact_list) > 1 else ""} in inventory\n')
                else:
                    print('Already saved this artifact\n')

            elif user_command in ('d', 'del', 'delete', 'r', 'rm', 'remove'):
                if art in artifact_list:
                    artifact_list.remove(art)
                    with open(r'.\inventory.txt', 'w') as file:
                        file.write(str(json.dumps(artifact_list, cls=ArtifactEncoder)))
                    print(f'Removed - {len(artifact_list)} artifact{"s" if len(artifact_list) != 1 else ""} in inventory\n')
                else:
                    print('This artifact is not in your inventory\n')

            elif 'inv' in user_command:
                if user_command in ('inv', 'inventory'):
                    if len(artifact_list) == 0:
                        print('Inventory is empty')
                    else:
                        print_inventory(artifact_list)
                    print()

                else:
                    user_command = user_command.split(' ')
                    if len(user_command) == 3:
                        _, indexes, cmd = user_command
                        indexes = indexes.split(',')
                        flag = True
                        for i in indexes:
                            if not i.isnumeric() or int(i) > len(artifact_list) or int(i) == 0:
                                flag = False
                                print(f'Index "{i}" is not valid\n')
                                break
                        if flag:  # if all given indexes are valid
                            indexes = list(map(lambda x: x - 1, map(int, indexes)))  # transform them
                            if len(indexes) > 1:                                     # if there's more than 1 index
                                arti_list = itemgetter(*indexes)(artifact_list)      # make a new list containing all the artifacts in question
                            else:                                        # otherwise, make a list containing 1 artifact
                                arti_list = [artifact_list[indexes[0]]]  # because we need a list object to iterate
                            for art in arti_list:                        # then iterate this list and execute command
                                if cmd == '+':
                                    upgrade_to_next_tier(art)
                                    artifact_list.sort(key=lambda x: (sort_order_type[x.type], sort_order_mainstat[x.mainstat], -x.level))
                                    with open(r'.\inventory.txt', 'w') as file:
                                        file.write(str(json.dumps(artifact_list, cls=ArtifactEncoder)))
                                elif cmd == '++':
                                    upgrade_to_max_tier(art, len(indexes) == 1)
                                    artifact_list.sort(key=lambda x: (sort_order_type[x.type], sort_order_mainstat[x.mainstat], -x.level))
                                    with open(r'.\inventory.txt', 'w') as file:
                                        file.write(str(json.dumps(artifact_list, cls=ArtifactEncoder)))
                                elif cmd == 'rv':
                                    print(f'RV: {art.rv()}%\n')

                                elif cmd == 'cv':
                                    print(f'CV: {art.cv()}\n')

                                elif cmd in ('d', 'del', 'delete', 'r', 'rm', 'remove'):
                                    artifact_list.remove(art)
                                    with open(r'.\inventory.txt', 'w') as file:
                                        file.write(str(json.dumps(artifact_list, cls=ArtifactEncoder)))
                                else:
                                    print('Invalid command\n')

                            if cmd in ('d', 'del', 'delete', 'r', 'rm', 'remove'):
                                print(f'\nArtifact{"s" if len(indexes) > 1 else ""} removed')
                                if len(artifact_list) == 0:
                                    print('Inventory is empty')
                                else:
                                    print_inventory(artifact_list)
                                print()

                    elif len(user_command) == 2:
                        _, cmd = user_command
                        if cmd.isnumeric():
                            cmd = int(cmd)
                            if cmd <= len(artifact_list) and cmd != 0:
                                print()
                                artifact_list[int(cmd) - 1].print_stats()
                            else:
                                print(f'Index "{cmd}" is not valid\n')
                        elif cmd in ('clear', 'clr', 'c'):
                            artifact_list = []
                            with open(r'.\inventory.txt', 'w') as file:
                                file.write(str(json.dumps(artifact_list, cls=ArtifactEncoder)))
                            print('Inventory cleared\n')
                        elif cmd == 'cv':
                            big_cv = max(artifact_list, key=lambda x: x.cv())
                            print(f'{big_cv} - {big_cv.subs()}')
                            print(f'CV: {big_cv.cv()}')
                            print()
                        elif cmd == 'rv':
                            big_rv = max(artifact_list, key=lambda x: x.rv())
                            print(f'{big_rv} - {big_rv.subs()}')
                            print(f'RV: {big_rv.rv()}%')
                            print()
                        else:
                            print('Invalid command\n')
                    else:
                        print('U did something wrong.\nIf you tried inputting multiple indexes, remove spaces between them\n')

            elif user_command == 'domain':
                source = 'domain'
                print('Source set to domain\n')

            elif user_command == 'strongbox':
                source = 'strongbox'
                print('Source set to strongbox\n')

            elif user_command == 'source':
                print(f'Current source: {source}\n')

            elif user_command in ('a rv', 'rv'):
                print(f'RV: {art.rv()}%\n')

            elif user_command in ('a cv', 'cv'):
                print(f'CV: {art.cv()}\n')

            elif user_command in ('artifact', 'a'):
                print()
                art.print_stats()

            elif user_command in ('exit', 'menu', '0'):
                print('Exiting...')
                break

            elif user_command in valid_help:
                print_controls()

            else:
                print("Try 'help'\n")
    else:
        break
print('\nThank you for using Artifact Simulator')
