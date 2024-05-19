print("""
here's some statistical information about getting 5-stars and 4-stars based on pity

d   - percentage of all pulls that will end up being your desired item on a specific pity
cum - probability that you will have gotten your desired item by that pity
r   - probability that you will NOT have gotten any item of the respective rarity by that pity
raw - probability of getting your desired item at any given pity (that is, if you got to it)

4-star chances assume that the pull is already not a 5-star
""")


def show_chances(t):
    remaining = 100
    cumulative = 0
    count = 0

    if t == '5-star character':
        hard, soft, base, m = 90, 74, 0.006, 1
    elif t == '5-star weapon':
        hard, soft, base, m = 77, 63, 0.007, 1
    elif t == 'desired 5-star character':
        hard, soft, base, m = 90, 74, 0.006, 1.5
    elif t == 'desired 5-star weapon':
        hard, soft, base, m = 77, 63, 0.007, 127/64
    elif t == '4-star character':
        hard, soft, base, m = 10, 9, 0.051, 1
    elif t == '4-star weapon':
        hard, soft, base, m = 9, 8, 0.06, 1
    elif t == 'on-banner 4-star character':
        hard, soft, base, m = 10, 9, 0.051, 1.5
    elif t == 'on-banner 4-star weapon':
        hard, soft, base, m = 9, 8, 0.06, 5/4

    if "desired" in t:
        desired = "desired "
    elif "on-banner" in t:
        desired = "on-banner "
    else:
        desired = ""

    print(f'\n{t.split()[-1].upper()} BANNER', end=' ')
    print(f'({desired.upper()}{t.split()[-2].upper()})\n')

    for pity in range(1, hard + 1):
        raw = min((max(pity - (soft - 1), 0) * base * 10 + base) / m, 1 / m)  # count raw probability for x pity
        delta = raw * remaining  # count how many wishes will be successful exactly on x pity
        cumulative += delta  # count how many wishes were successful on x pity or before
        count += (raw * m) * remaining / 100 * m * pity  # update counter for average pity
        remaining *= (1 - (raw * m))  # count what percentage of pulls still haven't reached needed rarity
        print(f'p={pity} - d = {delta:.12f}%, cum = {cumulative:.12f}%, '
              f'r = {remaining:.12f}%, raw = {raw * 100:.2f}%')
        # print(100/delta)  # one in how many attempts will stop at this pity
    print(f'\nAverage pity = {count}')
    print(f'{1 / count * 100:.4f}% of all pulls are {t}s on average')


show_chances('5-star character')
print()
show_chances('5-star weapon')
print()
show_chances('desired 5-star character')
print()
show_chances('desired 5-star weapon')
print()
show_chances('4-star character')
print()
show_chances('4-star weapon')
print()
show_chances('on-banner 4-star character')
print()
show_chances('on-banner 4-star weapon')
print()

# This is what the program will output:


# here's some statistical information about getting 5-stars and 4-stars based on pity
#
# d   - percentage of all pulls that will end up being your desired item on a specific pity
# cum - probability that you will have gotten your desired item by that pity
# r   - probability that you will NOT have gotten any item of the respective rarity by that pity
# raw - probability of getting your desired item at any given pity (that is, if you got to it)
#
# 4-star chances assume that the pull is already not a 5-star
#
#
# CHARACTER BANNER (5-STAR)
#
# p=1 - d = 0.600000000000%, cum = 0.600000000000%, r = 99.400000000000%, raw = 0.60%
# p=2 - d = 0.596400000000%, cum = 1.196400000000%, r = 98.803600000000%, raw = 0.60%
# p=3 - d = 0.592821600000%, cum = 1.789221600000%, r = 98.210778400000%, raw = 0.60%
# p=4 - d = 0.589264670400%, cum = 2.378486270400%, r = 97.621513729600%, raw = 0.60%
# p=5 - d = 0.585729082378%, cum = 2.964215352778%, r = 97.035784647222%, raw = 0.60%
# p=6 - d = 0.582214707883%, cum = 3.546430060661%, r = 96.453569939339%, raw = 0.60%
# p=7 - d = 0.578721419636%, cum = 4.125151480297%, r = 95.874848519703%, raw = 0.60%
# p=8 - d = 0.575249091118%, cum = 4.700400571415%, r = 95.299599428585%, raw = 0.60%
# p=9 - d = 0.571797596572%, cum = 5.272198167987%, r = 94.727801832013%, raw = 0.60%
# p=10 - d = 0.568366810992%, cum = 5.840564978979%, r = 94.159435021021%, raw = 0.60%
# p=11 - d = 0.564956610126%, cum = 6.405521589105%, r = 93.594478410895%, raw = 0.60%
# p=12 - d = 0.561566870465%, cum = 6.967088459570%, r = 93.032911540430%, raw = 0.60%
# p=13 - d = 0.558197469243%, cum = 7.525285928813%, r = 92.474714071187%, raw = 0.60%
# p=14 - d = 0.554848284427%, cum = 8.080134213240%, r = 91.919865786760%, raw = 0.60%
# p=15 - d = 0.551519194721%, cum = 8.631653407961%, r = 91.368346592039%, raw = 0.60%
# p=16 - d = 0.548210079552%, cum = 9.179863487513%, r = 90.820136512487%, raw = 0.60%
# p=17 - d = 0.544920819075%, cum = 9.724784306588%, r = 90.275215693412%, raw = 0.60%
# p=18 - d = 0.541651294160%, cum = 10.266435600748%, r = 89.733564399252%, raw = 0.60%
# p=19 - d = 0.538401386396%, cum = 10.804836987144%, r = 89.195163012856%, raw = 0.60%
# p=20 - d = 0.535170978077%, cum = 11.340007965221%, r = 88.659992034779%, raw = 0.60%
# p=21 - d = 0.531959952209%, cum = 11.871967917429%, r = 88.128032082571%, raw = 0.60%
# p=22 - d = 0.528768192495%, cum = 12.400736109925%, r = 87.599263890075%, raw = 0.60%
# p=23 - d = 0.525595583340%, cum = 12.926331693265%, r = 87.073668306735%, raw = 0.60%
# p=24 - d = 0.522442009840%, cum = 13.448773703106%, r = 86.551226296894%, raw = 0.60%
# p=25 - d = 0.519307357781%, cum = 13.968081060887%, r = 86.031918939113%, raw = 0.60%
# p=26 - d = 0.516191513635%, cum = 14.484272574522%, r = 85.515727425478%, raw = 0.60%
# p=27 - d = 0.513094364553%, cum = 14.997366939075%, r = 85.002633060925%, raw = 0.60%
# p=28 - d = 0.510015798366%, cum = 15.507382737440%, r = 84.492617262560%, raw = 0.60%
# p=29 - d = 0.506955703575%, cum = 16.014338441016%, r = 83.985661558984%, raw = 0.60%
# p=30 - d = 0.503913969354%, cum = 16.518252410370%, r = 83.481747589631%, raw = 0.60%
# p=31 - d = 0.500890485538%, cum = 17.019142895907%, r = 82.980857104093%, raw = 0.60%
# p=32 - d = 0.497885142625%, cum = 17.517028038532%, r = 82.482971961468%, raw = 0.60%
# p=33 - d = 0.494897831769%, cum = 18.011925870301%, r = 81.988074129699%, raw = 0.60%
# p=34 - d = 0.491928444778%, cum = 18.503854315079%, r = 81.496145684921%, raw = 0.60%
# p=35 - d = 0.488976874110%, cum = 18.992831189188%, r = 81.007168810812%, raw = 0.60%
# p=36 - d = 0.486043012865%, cum = 19.478874202053%, r = 80.521125797947%, raw = 0.60%
# p=37 - d = 0.483126754788%, cum = 19.962000956841%, r = 80.037999043159%, raw = 0.60%
# p=38 - d = 0.480227994259%, cum = 20.442228951100%, r = 79.557771048900%, raw = 0.60%
# p=39 - d = 0.477346626293%, cum = 20.919575577393%, r = 79.080424422607%, raw = 0.60%
# p=40 - d = 0.474482546536%, cum = 21.394058123929%, r = 78.605941876071%, raw = 0.60%
# p=41 - d = 0.471635651256%, cum = 21.865693775185%, r = 78.134306224815%, raw = 0.60%
# p=42 - d = 0.468805837349%, cum = 22.334499612534%, r = 77.665500387466%, raw = 0.60%
# p=43 - d = 0.465993002325%, cum = 22.800492614859%, r = 77.199507385141%, raw = 0.60%
# p=44 - d = 0.463197044311%, cum = 23.263689659170%, r = 76.736310340830%, raw = 0.60%
# p=45 - d = 0.460417862045%, cum = 23.724107521215%, r = 76.275892478785%, raw = 0.60%
# p=46 - d = 0.457655354873%, cum = 24.181762876088%, r = 75.818237123912%, raw = 0.60%
# p=47 - d = 0.454909422743%, cum = 24.636672298831%, r = 75.363327701169%, raw = 0.60%
# p=48 - d = 0.452179966207%, cum = 25.088852265038%, r = 74.911147734962%, raw = 0.60%
# p=49 - d = 0.449466886410%, cum = 25.538319151448%, r = 74.461680848552%, raw = 0.60%
# p=50 - d = 0.446770085091%, cum = 25.985089236539%, r = 74.014910763461%, raw = 0.60%
# p=51 - d = 0.444089464581%, cum = 26.429178701120%, r = 73.570821298880%, raw = 0.60%
# p=52 - d = 0.441424927793%, cum = 26.870603628913%, r = 73.129396371087%, raw = 0.60%
# p=53 - d = 0.438776378227%, cum = 27.309380007140%, r = 72.690619992860%, raw = 0.60%
# p=54 - d = 0.436143719957%, cum = 27.745523727097%, r = 72.254476272903%, raw = 0.60%
# p=55 - d = 0.433526857637%, cum = 28.179050584734%, r = 71.820949415266%, raw = 0.60%
# p=56 - d = 0.430925696492%, cum = 28.609976281226%, r = 71.390023718774%, raw = 0.60%
# p=57 - d = 0.428340142313%, cum = 29.038316423539%, r = 70.961683576462%, raw = 0.60%
# p=58 - d = 0.425770101459%, cum = 29.464086524997%, r = 70.535913475003%, raw = 0.60%
# p=59 - d = 0.423215480850%, cum = 29.887302005847%, r = 70.112697994153%, raw = 0.60%
# p=60 - d = 0.420676187965%, cum = 30.307978193812%, r = 69.692021806188%, raw = 0.60%
# p=61 - d = 0.418152130837%, cum = 30.726130324649%, r = 69.273869675351%, raw = 0.60%
# p=62 - d = 0.415643218052%, cum = 31.141773542701%, r = 68.858226457299%, raw = 0.60%
# p=63 - d = 0.413149358744%, cum = 31.554922901445%, r = 68.445077098555%, raw = 0.60%
# p=64 - d = 0.410670462591%, cum = 31.965593364037%, r = 68.034406635963%, raw = 0.60%
# p=65 - d = 0.408206439816%, cum = 32.373799803852%, r = 67.626200196148%, raw = 0.60%
# p=66 - d = 0.405757201177%, cum = 32.779557005029%, r = 67.220442994971%, raw = 0.60%
# p=67 - d = 0.403322657970%, cum = 33.182879662999%, r = 66.817120337001%, raw = 0.60%
# p=68 - d = 0.400902722022%, cum = 33.583782385021%, r = 66.416217614979%, raw = 0.60%
# p=69 - d = 0.398497305690%, cum = 33.982279690711%, r = 66.017720309289%, raw = 0.60%
# p=70 - d = 0.396106321856%, cum = 34.378386012567%, r = 65.621613987433%, raw = 0.60%
# p=71 - d = 0.393729683925%, cum = 34.772115696491%, r = 65.227884303509%, raw = 0.60%
# p=72 - d = 0.391367305821%, cum = 35.163483002312%, r = 64.836516997688%, raw = 0.60%
# p=73 - d = 0.389019101986%, cum = 35.552502104298%, r = 64.447497895702%, raw = 0.60%
# p=74 - d = 4.253534861116%, cum = 39.806036965415%, r = 60.193963034585%, raw = 6.60%
# p=75 - d = 7.584439342358%, cum = 47.390476307773%, r = 52.609523692228%, raw = 12.60%
# p=76 - d = 9.785371406754%, cum = 57.175847714527%, r = 42.824152285473%, raw = 18.60%
# p=77 - d = 10.534741462226%, cum = 67.710589176753%, r = 32.289410823247%, raw = 24.60%
# p=78 - d = 9.880559711914%, cum = 77.591148888667%, r = 22.408851111333%, raw = 30.60%
# p=79 - d = 8.201639506748%, cum = 85.792788395415%, r = 14.207211604585%, raw = 36.60%
# p=80 - d = 6.052272143553%, cum = 91.845060538968%, r = 8.154939461032%, raw = 42.60%
# p=81 - d = 3.963300578062%, cum = 95.808361117030%, r = 4.191638882970%, raw = 48.60%
# p=82 - d = 2.288634830102%, cum = 98.096995947131%, r = 1.903004052869%, raw = 54.60%
# p=83 - d = 1.153220456038%, cum = 99.250216403170%, r = 0.749783596830%, raw = 60.60%
# p=84 - d = 0.499355875489%, cum = 99.749572278659%, r = 0.250427721341%, raw = 66.60%
# p=85 - d = 0.181810525694%, cum = 99.931382804353%, r = 0.068617195648%, raw = 72.60%
# p=86 - d = 0.053933115779%, cum = 99.985315920131%, r = 0.014684079869%, raw = 78.60%
# p=87 - d = 0.012422731569%, cum = 99.997738651700%, r = 0.002261348300%, raw = 84.60%
# p=88 - d = 0.002048781560%, cum = 99.999787433260%, r = 0.000212566740%, raw = 90.60%
# p=89 - d = 0.000205339471%, cum = 99.999992772731%, r = 0.000007227269%, raw = 96.60%
# p=90 - d = 0.000007227269%, cum = 100.000000000000%, r = 0.000000000000%, raw = 100.00%
#
# Average pity = 62.297332039631
# 1.6052% of all pulls are 5-star characters on average
#
#
# WEAPON BANNER (5-STAR)
#
# p=1 - d = 0.700000000000%, cum = 0.700000000000%, r = 99.300000000000%, raw = 0.70%
# p=2 - d = 0.695100000000%, cum = 1.395100000000%, r = 98.604900000000%, raw = 0.70%
# p=3 - d = 0.690234300000%, cum = 2.085334300000%, r = 97.914665700000%, raw = 0.70%
# p=4 - d = 0.685402659900%, cum = 2.770736959900%, r = 97.229263040100%, raw = 0.70%
# p=5 - d = 0.680604841281%, cum = 3.451341801181%, r = 96.548658198819%, raw = 0.70%
# p=6 - d = 0.675840607392%, cum = 4.127182408572%, r = 95.872817591428%, raw = 0.70%
# p=7 - d = 0.671109723140%, cum = 4.798292131712%, r = 95.201707868288%, raw = 0.70%
# p=8 - d = 0.666411955078%, cum = 5.464704086790%, r = 94.535295913210%, raw = 0.70%
# p=9 - d = 0.661747071392%, cum = 6.126451158183%, r = 93.873548841817%, raw = 0.70%
# p=10 - d = 0.657114841893%, cum = 6.783566000076%, r = 93.216433999924%, raw = 0.70%
# p=11 - d = 0.652515037999%, cum = 7.436081038075%, r = 92.563918961925%, raw = 0.70%
# p=12 - d = 0.647947432733%, cum = 8.084028470809%, r = 91.915971529191%, raw = 0.70%
# p=13 - d = 0.643411800704%, cum = 8.727440271513%, r = 91.272559728487%, raw = 0.70%
# p=14 - d = 0.638907918099%, cum = 9.366348189612%, r = 90.633651810388%, raw = 0.70%
# p=15 - d = 0.634435562673%, cum = 10.000783752285%, r = 89.999216247715%, raw = 0.70%
# p=16 - d = 0.629994513734%, cum = 10.630778266019%, r = 89.369221733981%, raw = 0.70%
# p=17 - d = 0.625584552138%, cum = 11.256362818157%, r = 88.743637181843%, raw = 0.70%
# p=18 - d = 0.621205460273%, cum = 11.877568278430%, r = 88.122431721570%, raw = 0.70%
# p=19 - d = 0.616857022051%, cum = 12.494425300481%, r = 87.505574699519%, raw = 0.70%
# p=20 - d = 0.612539022897%, cum = 13.106964323377%, r = 86.893035676623%, raw = 0.70%
# p=21 - d = 0.608251249736%, cum = 13.715215573114%, r = 86.284784426886%, raw = 0.70%
# p=22 - d = 0.603993490988%, cum = 14.319209064102%, r = 85.680790935898%, raw = 0.70%
# p=23 - d = 0.599765536551%, cum = 14.918974600653%, r = 85.081025399347%, raw = 0.70%
# p=24 - d = 0.595567177795%, cum = 15.514541778449%, r = 84.485458221551%, raw = 0.70%
# p=25 - d = 0.591398207551%, cum = 16.105939986000%, r = 83.894060014000%, raw = 0.70%
# p=26 - d = 0.587258420098%, cum = 16.693198406098%, r = 83.306801593902%, raw = 0.70%
# p=27 - d = 0.583147611157%, cum = 17.276346017255%, r = 82.723653982745%, raw = 0.70%
# p=28 - d = 0.579065577879%, cum = 17.855411595134%, r = 82.144588404866%, raw = 0.70%
# p=29 - d = 0.575012118834%, cum = 18.430423713968%, r = 81.569576286032%, raw = 0.70%
# p=30 - d = 0.570987034002%, cum = 19.001410747970%, r = 80.998589252030%, raw = 0.70%
# p=31 - d = 0.566990124764%, cum = 19.568400872735%, r = 80.431599127265%, raw = 0.70%
# p=32 - d = 0.563021193891%, cum = 20.131422066625%, r = 79.868577933375%, raw = 0.70%
# p=33 - d = 0.559080045534%, cum = 20.690502112159%, r = 79.309497887841%, raw = 0.70%
# p=34 - d = 0.555166485215%, cum = 21.245668597374%, r = 78.754331402626%, raw = 0.70%
# p=35 - d = 0.551280319818%, cum = 21.796948917192%, r = 78.203051082808%, raw = 0.70%
# p=36 - d = 0.547421357580%, cum = 22.344370274772%, r = 77.655629725228%, raw = 0.70%
# p=37 - d = 0.543589408077%, cum = 22.887959682849%, r = 77.112040317151%, raw = 0.70%
# p=38 - d = 0.539784282220%, cum = 23.427743965069%, r = 76.572256034931%, raw = 0.70%
# p=39 - d = 0.536005792245%, cum = 23.963749757313%, r = 76.036250242687%, raw = 0.70%
# p=40 - d = 0.532253751699%, cum = 24.496003509012%, r = 75.503996490988%, raw = 0.70%
# p=41 - d = 0.528527975437%, cum = 25.024531484449%, r = 74.975468515551%, raw = 0.70%
# p=42 - d = 0.524828279609%, cum = 25.549359764058%, r = 74.450640235942%, raw = 0.70%
# p=43 - d = 0.521154481652%, cum = 26.070514245709%, r = 73.929485754291%, raw = 0.70%
# p=44 - d = 0.517506400280%, cum = 26.588020645989%, r = 73.411979354011%, raw = 0.70%
# p=45 - d = 0.513883855478%, cum = 27.101904501467%, r = 72.898095498533%, raw = 0.70%
# p=46 - d = 0.510286668490%, cum = 27.612191169957%, r = 72.387808830043%, raw = 0.70%
# p=47 - d = 0.506714661810%, cum = 28.118905831767%, r = 71.881094168232%, raw = 0.70%
# p=48 - d = 0.503167659178%, cum = 28.622073490945%, r = 71.377926509055%, raw = 0.70%
# p=49 - d = 0.499645485563%, cum = 29.121718976508%, r = 70.878281023491%, raw = 0.70%
# p=50 - d = 0.496147967164%, cum = 29.617866943673%, r = 70.382133056327%, raw = 0.70%
# p=51 - d = 0.492674931394%, cum = 30.110541875067%, r = 69.889458124933%, raw = 0.70%
# p=52 - d = 0.489226206875%, cum = 30.599768081942%, r = 69.400231918058%, raw = 0.70%
# p=53 - d = 0.485801623426%, cum = 31.085569705368%, r = 68.914430294632%, raw = 0.70%
# p=54 - d = 0.482401012062%, cum = 31.567970717431%, r = 68.432029282569%, raw = 0.70%
# p=55 - d = 0.479024204978%, cum = 32.046994922409%, r = 67.953005077591%, raw = 0.70%
# p=56 - d = 0.475671035543%, cum = 32.522665957952%, r = 67.477334042048%, raw = 0.70%
# p=57 - d = 0.472341338294%, cum = 32.995007296246%, r = 67.004992703754%, raw = 0.70%
# p=58 - d = 0.469034948926%, cum = 33.464042245172%, r = 66.535957754828%, raw = 0.70%
# p=59 - d = 0.465751704284%, cum = 33.929793949456%, r = 66.070206050544%, raw = 0.70%
# p=60 - d = 0.462491442354%, cum = 34.392285391810%, r = 65.607714608190%, raw = 0.70%
# p=61 - d = 0.459254002257%, cum = 34.851539394067%, r = 65.148460605933%, raw = 0.70%
# p=62 - d = 0.456039224242%, cum = 35.307578618309%, r = 64.692421381691%, raw = 0.70%
# p=63 - d = 4.981316446390%, cum = 40.288895064699%, r = 59.711104935301%, raw = 7.70%
# p=64 - d = 8.777532425489%, cum = 49.066427490188%, r = 50.933572509812%, raw = 14.70%
# p=65 - d = 11.052585234629%, cum = 60.119012724817%, r = 39.880987275183%, raw = 21.70%
# p=66 - d = 11.445843347977%, cum = 71.564856072795%, r = 28.435143927205%, raw = 28.70%
# p=67 - d = 10.151346382012%, cum = 81.716202454807%, r = 18.283797545193%, raw = 35.70%
# p=68 - d = 7.807181551797%, cum = 89.523384006604%, r = 10.476615993396%, raw = 42.70%
# p=69 - d = 5.206878148718%, cum = 94.730262155322%, r = 5.269737844678%, raw = 49.70%
# p=70 - d = 2.987941357932%, cum = 97.718203513254%, r = 2.281796486746%, raw = 56.70%
# p=71 - d = 1.453504362057%, cum = 99.171707875311%, r = 0.828292124689%, raw = 63.70%
# p=72 - d = 0.585602532155%, cum = 99.757310407466%, r = 0.242689592534%, raw = 70.70%
# p=73 - d = 0.188569813399%, cum = 99.945880220865%, r = 0.054119779135%, raw = 77.70%
# p=74 - d = 0.045839452927%, cum = 99.991719673792%, r = 0.008280326208%, raw = 84.70%
# p=75 - d = 0.007593059132%, cum = 99.999312732925%, r = 0.000687267075%, raw = 91.70%
# p=76 - d = 0.000678332603%, cum = 99.999991065528%, r = 0.000008934472%, raw = 98.70%
# p=77 - d = 0.000008934472%, cum = 100.000000000000%, r = 0.000000000000%, raw = 100.00%
#
# Average pity = 53.25039058538852
# 1.8779% of all pulls are 5-star weapons on average
#
#
# CHARACTER BANNER (DESIRED 5-STAR)
#
# p=1 - d = 0.400000000000%, cum = 0.400000000000%, r = 99.400000000000%, raw = 0.40%
# p=2 - d = 0.397600000000%, cum = 0.797600000000%, r = 98.803600000000%, raw = 0.40%
# p=3 - d = 0.395214400000%, cum = 1.192814400000%, r = 98.210778400000%, raw = 0.40%
# p=4 - d = 0.392843113600%, cum = 1.585657513600%, r = 97.621513729600%, raw = 0.40%
# p=5 - d = 0.390486054918%, cum = 1.976143568518%, r = 97.035784647222%, raw = 0.40%
# p=6 - d = 0.388143138589%, cum = 2.364286707107%, r = 96.453569939339%, raw = 0.40%
# p=7 - d = 0.385814279757%, cum = 2.750100986865%, r = 95.874848519703%, raw = 0.40%
# p=8 - d = 0.383499394079%, cum = 3.133600380943%, r = 95.299599428585%, raw = 0.40%
# p=9 - d = 0.381198397714%, cum = 3.514798778658%, r = 94.727801832013%, raw = 0.40%
# p=10 - d = 0.378911207328%, cum = 3.893709985986%, r = 94.159435021021%, raw = 0.40%
# p=11 - d = 0.376637740084%, cum = 4.270347726070%, r = 93.594478410895%, raw = 0.40%
# p=12 - d = 0.374377913644%, cum = 4.644725639714%, r = 93.032911540430%, raw = 0.40%
# p=13 - d = 0.372131646162%, cum = 5.016857285875%, r = 92.474714071187%, raw = 0.40%
# p=14 - d = 0.369898856285%, cum = 5.386756142160%, r = 91.919865786760%, raw = 0.40%
# p=15 - d = 0.367679463147%, cum = 5.754435605307%, r = 91.368346592039%, raw = 0.40%
# p=16 - d = 0.365473386368%, cum = 6.119908991675%, r = 90.820136512487%, raw = 0.40%
# p=17 - d = 0.363280546050%, cum = 6.483189537725%, r = 90.275215693412%, raw = 0.40%
# p=18 - d = 0.361100862774%, cum = 6.844290400499%, r = 89.733564399252%, raw = 0.40%
# p=19 - d = 0.358934257597%, cum = 7.203224658096%, r = 89.195163012856%, raw = 0.40%
# p=20 - d = 0.356780652051%, cum = 7.560005310147%, r = 88.659992034779%, raw = 0.40%
# p=21 - d = 0.354639968139%, cum = 7.914645278286%, r = 88.128032082571%, raw = 0.40%
# p=22 - d = 0.352512128330%, cum = 8.267157406617%, r = 87.599263890075%, raw = 0.40%
# p=23 - d = 0.350397055560%, cum = 8.617554462177%, r = 87.073668306735%, raw = 0.40%
# p=24 - d = 0.348294673227%, cum = 8.965849135404%, r = 86.551226296894%, raw = 0.40%
# p=25 - d = 0.346204905188%, cum = 9.312054040591%, r = 86.031918939113%, raw = 0.40%
# p=26 - d = 0.344127675756%, cum = 9.656181716348%, r = 85.515727425478%, raw = 0.40%
# p=27 - d = 0.342062909702%, cum = 9.998244626050%, r = 85.002633060925%, raw = 0.40%
# p=28 - d = 0.340010532244%, cum = 10.338255158293%, r = 84.492617262560%, raw = 0.40%
# p=29 - d = 0.337970469050%, cum = 10.676225627344%, r = 83.985661558984%, raw = 0.40%
# p=30 - d = 0.335942646236%, cum = 11.012168273580%, r = 83.481747589631%, raw = 0.40%
# p=31 - d = 0.333926990359%, cum = 11.346095263938%, r = 82.980857104093%, raw = 0.40%
# p=32 - d = 0.331923428416%, cum = 11.678018692355%, r = 82.482971961468%, raw = 0.40%
# p=33 - d = 0.329931887846%, cum = 12.007950580200%, r = 81.988074129699%, raw = 0.40%
# p=34 - d = 0.327952296519%, cum = 12.335902876719%, r = 81.496145684921%, raw = 0.40%
# p=35 - d = 0.325984582740%, cum = 12.661887459459%, r = 81.007168810812%, raw = 0.40%
# p=36 - d = 0.324028675243%, cum = 12.985916134702%, r = 80.521125797947%, raw = 0.40%
# p=37 - d = 0.322084503192%, cum = 13.308000637894%, r = 80.037999043159%, raw = 0.40%
# p=38 - d = 0.320151996173%, cum = 13.628152634067%, r = 79.557771048900%, raw = 0.40%
# p=39 - d = 0.318231084196%, cum = 13.946383718262%, r = 79.080424422607%, raw = 0.40%
# p=40 - d = 0.316321697690%, cum = 14.262705415953%, r = 78.605941876071%, raw = 0.40%
# p=41 - d = 0.314423767504%, cum = 14.577129183457%, r = 78.134306224815%, raw = 0.40%
# p=42 - d = 0.312537224899%, cum = 14.889666408356%, r = 77.665500387466%, raw = 0.40%
# p=43 - d = 0.310662001550%, cum = 15.200328409906%, r = 77.199507385141%, raw = 0.40%
# p=44 - d = 0.308798029541%, cum = 15.509126439447%, r = 76.736310340830%, raw = 0.40%
# p=45 - d = 0.306945241363%, cum = 15.816071680810%, r = 76.275892478785%, raw = 0.40%
# p=46 - d = 0.305103569915%, cum = 16.121175250725%, r = 75.818237123912%, raw = 0.40%
# p=47 - d = 0.303272948496%, cum = 16.424448199221%, r = 75.363327701169%, raw = 0.40%
# p=48 - d = 0.301453310805%, cum = 16.725901510025%, r = 74.911147734962%, raw = 0.40%
# p=49 - d = 0.299644590940%, cum = 17.025546100965%, r = 74.461680848552%, raw = 0.40%
# p=50 - d = 0.297846723394%, cum = 17.323392824359%, r = 74.014910763461%, raw = 0.40%
# p=51 - d = 0.296059643054%, cum = 17.619452467413%, r = 73.570821298880%, raw = 0.40%
# p=52 - d = 0.294283285196%, cum = 17.913735752609%, r = 73.129396371087%, raw = 0.40%
# p=53 - d = 0.292517585484%, cum = 18.206253338093%, r = 72.690619992860%, raw = 0.40%
# p=54 - d = 0.290762479971%, cum = 18.497015818065%, r = 72.254476272903%, raw = 0.40%
# p=55 - d = 0.289017905092%, cum = 18.786033723156%, r = 71.820949415266%, raw = 0.40%
# p=56 - d = 0.287283797661%, cum = 19.073317520817%, r = 71.390023718774%, raw = 0.40%
# p=57 - d = 0.285560094875%, cum = 19.358877615692%, r = 70.961683576462%, raw = 0.40%
# p=58 - d = 0.283846734306%, cum = 19.642724349998%, r = 70.535913475003%, raw = 0.40%
# p=59 - d = 0.282143653900%, cum = 19.924868003898%, r = 70.112697994153%, raw = 0.40%
# p=60 - d = 0.280450791977%, cum = 20.205318795875%, r = 69.692021806188%, raw = 0.40%
# p=61 - d = 0.278768087225%, cum = 20.484086883100%, r = 69.273869675351%, raw = 0.40%
# p=62 - d = 0.277095478701%, cum = 20.761182361801%, r = 68.858226457299%, raw = 0.40%
# p=63 - d = 0.275432905829%, cum = 21.036615267630%, r = 68.445077098555%, raw = 0.40%
# p=64 - d = 0.273780308394%, cum = 21.310395576024%, r = 68.034406635963%, raw = 0.40%
# p=65 - d = 0.272137626544%, cum = 21.582533202568%, r = 67.626200196148%, raw = 0.40%
# p=66 - d = 0.270504800785%, cum = 21.853038003353%, r = 67.220442994971%, raw = 0.40%
# p=67 - d = 0.268881771980%, cum = 22.121919775333%, r = 66.817120337001%, raw = 0.40%
# p=68 - d = 0.267268481348%, cum = 22.389188256681%, r = 66.416217614979%, raw = 0.40%
# p=69 - d = 0.265664870460%, cum = 22.654853127141%, r = 66.017720309289%, raw = 0.40%
# p=70 - d = 0.264070881237%, cum = 22.918924008378%, r = 65.621613987433%, raw = 0.40%
# p=71 - d = 0.262486455950%, cum = 23.181410464328%, r = 65.227884303509%, raw = 0.40%
# p=72 - d = 0.260911537214%, cum = 23.442322001542%, r = 64.836516997688%, raw = 0.40%
# p=73 - d = 0.259346067991%, cum = 23.701668069532%, r = 64.447497895702%, raw = 0.40%
# p=74 - d = 2.835689907411%, cum = 26.537357976943%, r = 60.193963034585%, raw = 4.40%
# p=75 - d = 5.056292894905%, cum = 31.593650871848%, r = 52.609523692228%, raw = 8.40%
# p=76 - d = 6.523580937836%, cum = 38.117231809685%, r = 42.824152285473%, raw = 12.40%
# p=77 - d = 7.023160974818%, cum = 45.140392784502%, r = 32.289410823247%, raw = 16.40%
# p=78 - d = 6.587039807942%, cum = 51.727432592445%, r = 22.408851111333%, raw = 20.40%
# p=79 - d = 5.467759671165%, cum = 57.195192263610%, r = 14.207211604585%, raw = 24.40%
# p=80 - d = 4.034848095702%, cum = 61.230040359312%, r = 8.154939461032%, raw = 28.40%
# p=81 - d = 2.642200385374%, cum = 63.872240744686%, r = 4.191638882970%, raw = 32.40%
# p=82 - d = 1.525756553401%, cum = 65.397997298088%, r = 1.903004052869%, raw = 36.40%
# p=83 - d = 0.768813637359%, cum = 66.166810935447%, r = 0.749783596830%, raw = 40.40%
# p=84 - d = 0.332903916993%, cum = 66.499714852439%, r = 0.250427721341%, raw = 44.40%
# p=85 - d = 0.121207017129%, cum = 66.620921869568%, r = 0.068617195648%, raw = 48.40%
# p=86 - d = 0.035955410519%, cum = 66.656877280088%, r = 0.014684079869%, raw = 52.40%
# p=87 - d = 0.008281821046%, cum = 66.665159101134%, r = 0.002261348300%, raw = 56.40%
# p=88 - d = 0.001365854373%, cum = 66.666524955507%, r = 0.000212566740%, raw = 60.40%
# p=89 - d = 0.000136892981%, cum = 66.666661848487%, r = 0.000007227269%, raw = 64.40%
# p=90 - d = 0.000004818179%, cum = 66.666666666667%, r = 0.000000000000%, raw = 66.67%
#
# Average pity = 93.4459980594465
# 1.0701% of all pulls are desired 5-star characters on average
#
#
# WEAPON BANNER (DESIRED 5-STAR)
#
# p=1 - d = 0.352755905512%, cum = 0.352755905512%, r = 99.300000000000%, raw = 0.35%
# p=2 - d = 0.350286614173%, cum = 0.703042519685%, r = 98.604900000000%, raw = 0.35%
# p=3 - d = 0.347834607874%, cum = 1.050877127559%, r = 97.914665700000%, raw = 0.35%
# p=4 - d = 0.345399765619%, cum = 1.396276893178%, r = 97.229263040100%, raw = 0.35%
# p=5 - d = 0.342981967260%, cum = 1.739258860438%, r = 96.548658198819%, raw = 0.35%
# p=6 - d = 0.340581093489%, cum = 2.079839953926%, r = 95.872817591428%, raw = 0.35%
# p=7 - d = 0.338197025834%, cum = 2.418036979761%, r = 95.201707868288%, raw = 0.35%
# p=8 - d = 0.335829646653%, cum = 2.753866626414%, r = 94.535295913210%, raw = 0.35%
# p=9 - d = 0.333478839127%, cum = 3.087345465541%, r = 93.873548841817%, raw = 0.35%
# p=10 - d = 0.331144487253%, cum = 3.418489952794%, r = 93.216433999924%, raw = 0.35%
# p=11 - d = 0.328826475842%, cum = 3.747316428636%, r = 92.563918961925%, raw = 0.35%
# p=12 - d = 0.326524690511%, cum = 4.073841119148%, r = 91.915971529191%, raw = 0.35%
# p=13 - d = 0.324239017678%, cum = 4.398080136825%, r = 91.272559728487%, raw = 0.35%
# p=14 - d = 0.321969344554%, cum = 4.720049481379%, r = 90.633651810388%, raw = 0.35%
# p=15 - d = 0.319715559142%, cum = 5.039765040522%, r = 89.999216247715%, raw = 0.35%
# p=16 - d = 0.317477550228%, cum = 5.357242590750%, r = 89.369221733981%, raw = 0.35%
# p=17 - d = 0.315255207377%, cum = 5.672497798126%, r = 88.743637181843%, raw = 0.35%
# p=18 - d = 0.313048420925%, cum = 5.985546219051%, r = 88.122431721570%, raw = 0.35%
# p=19 - d = 0.310857081978%, cum = 6.296403301030%, r = 87.505574699519%, raw = 0.35%
# p=20 - d = 0.308681082405%, cum = 6.605084383434%, r = 86.893035676623%, raw = 0.35%
# p=21 - d = 0.306520314828%, cum = 6.911604698262%, r = 86.284784426886%, raw = 0.35%
# p=22 - d = 0.304374672624%, cum = 7.215979370886%, r = 85.680790935898%, raw = 0.35%
# p=23 - d = 0.302244049916%, cum = 7.518223420802%, r = 85.081025399347%, raw = 0.35%
# p=24 - d = 0.300128341566%, cum = 7.818351762368%, r = 84.485458221551%, raw = 0.35%
# p=25 - d = 0.298027443175%, cum = 8.116379205543%, r = 83.894060014000%, raw = 0.35%
# p=26 - d = 0.295941251073%, cum = 8.412320456616%, r = 83.306801593902%, raw = 0.35%
# p=27 - d = 0.293869662315%, cum = 8.706190118932%, r = 82.723653982745%, raw = 0.35%
# p=28 - d = 0.291812574679%, cum = 8.998002693611%, r = 82.144588404866%, raw = 0.35%
# p=29 - d = 0.289769886657%, cum = 9.287772580267%, r = 81.569576286032%, raw = 0.35%
# p=30 - d = 0.287741497450%, cum = 9.575514077717%, r = 80.998589252030%, raw = 0.35%
# p=31 - d = 0.285727306968%, cum = 9.861241384685%, r = 80.431599127265%, raw = 0.35%
# p=32 - d = 0.283727215819%, cum = 10.144968600504%, r = 79.868577933375%, raw = 0.35%
# p=33 - d = 0.281741125308%, cum = 10.426709725812%, r = 79.309497887841%, raw = 0.35%
# p=34 - d = 0.279768937431%, cum = 10.706478663244%, r = 78.754331402626%, raw = 0.35%
# p=35 - d = 0.277810554869%, cum = 10.984289218113%, r = 78.203051082808%, raw = 0.35%
# p=36 - d = 0.275865880985%, cum = 11.260155099098%, r = 77.655629725228%, raw = 0.35%
# p=37 - d = 0.273934819818%, cum = 11.534089918916%, r = 77.112040317151%, raw = 0.35%
# p=38 - d = 0.272017276079%, cum = 11.806107194995%, r = 76.572256034931%, raw = 0.35%
# p=39 - d = 0.270113155147%, cum = 12.076220350142%, r = 76.036250242687%, raw = 0.35%
# p=40 - d = 0.268222363061%, cum = 12.344442713203%, r = 75.503996490988%, raw = 0.35%
# p=41 - d = 0.266344806519%, cum = 12.610787519722%, r = 74.975468515551%, raw = 0.35%
# p=42 - d = 0.264480392874%, cum = 12.875267912596%, r = 74.450640235942%, raw = 0.35%
# p=43 - d = 0.262629030124%, cum = 13.137896942720%, r = 73.929485754291%, raw = 0.35%
# p=44 - d = 0.260790626913%, cum = 13.398687569632%, r = 73.411979354011%, raw = 0.35%
# p=45 - d = 0.258965092524%, cum = 13.657652662157%, r = 72.898095498533%, raw = 0.35%
# p=46 - d = 0.257152336877%, cum = 13.914804999034%, r = 72.387808830043%, raw = 0.35%
# p=47 - d = 0.255352270519%, cum = 14.170157269552%, r = 71.881094168232%, raw = 0.35%
# p=48 - d = 0.253564804625%, cum = 14.423722074177%, r = 71.377926509055%, raw = 0.35%
# p=49 - d = 0.251789850993%, cum = 14.675511925170%, r = 70.878281023491%, raw = 0.35%
# p=50 - d = 0.250027322036%, cum = 14.925539247205%, r = 70.382133056327%, raw = 0.35%
# p=51 - d = 0.248277130781%, cum = 15.173816377987%, r = 69.889458124933%, raw = 0.35%
# p=52 - d = 0.246539190866%, cum = 15.420355568853%, r = 69.400231918058%, raw = 0.35%
# p=53 - d = 0.244813416530%, cum = 15.665168985382%, r = 68.914430294632%, raw = 0.35%
# p=54 - d = 0.243099722614%, cum = 15.908268707997%, r = 68.432029282569%, raw = 0.35%
# p=55 - d = 0.241398024556%, cum = 16.149666732552%, r = 67.953005077591%, raw = 0.35%
# p=56 - d = 0.239708238384%, cum = 16.389374970936%, r = 67.477334042048%, raw = 0.35%
# p=57 - d = 0.238030280715%, cum = 16.627405251652%, r = 67.004992703754%, raw = 0.35%
# p=58 - d = 0.236364068750%, cum = 16.863769320402%, r = 66.535957754828%, raw = 0.35%
# p=59 - d = 0.234709520269%, cum = 17.098478840671%, r = 66.070206050544%, raw = 0.35%
# p=60 - d = 0.233066553627%, cum = 17.331545394298%, r = 65.607714608190%, raw = 0.35%
# p=61 - d = 0.231435087752%, cum = 17.562980482050%, r = 65.148460605933%, raw = 0.35%
# p=62 - d = 0.229815042137%, cum = 17.792795524187%, r = 64.692421381691%, raw = 0.35%
# p=63 - d = 2.510269705268%, cum = 20.303065229455%, r = 59.711104935301%, raw = 3.88%
# p=64 - d = 4.423323427018%, cum = 24.726388656473%, r = 50.933572509812%, raw = 7.41%
# p=65 - d = 5.569806732412%, cum = 30.296195388884%, r = 39.880987275183%, raw = 10.94%
# p=66 - d = 5.767984049374%, cum = 36.064179438259%, r = 28.435143927205%, raw = 14.46%
# p=67 - d = 5.115639121644%, cum = 41.179818559903%, r = 18.283797545193%, raw = 17.99%
# p=68 - d = 3.934327711142%, cum = 45.114146271045%, r = 10.476615993396%, raw = 21.52%
# p=69 - d = 2.623938594629%, cum = 47.738084865674%, r = 5.269737844678%, raw = 25.05%
# p=70 - d = 1.505734227619%, cum = 49.243819093294%, r = 2.281796486746%, raw = 28.57%
# p=71 - d = 0.732474639147%, cum = 49.976293732440%, r = 0.828292124689%, raw = 32.10%
# p=72 - d = 0.295106787858%, cum = 50.271400520298%, r = 0.242689592534%, raw = 35.63%
# p=73 - d = 0.095027307540%, cum = 50.366427827837%, r = 0.054119779135%, raw = 39.16%
# p=74 - d = 0.023100196751%, cum = 50.389528024588%, r = 0.008280326208%, raw = 42.68%
# p=75 - d = 0.003826423500%, cum = 50.393354448088%, r = 0.000687267075%, raw = 46.21%
# p=76 - d = 0.000341836902%, cum = 50.393696284990%, r = 0.000008934472%, raw = 49.74%
# p=77 - d = 0.000004502411%, cum = 50.393700787402%, r = 0.000000000000%, raw = 50.39%
#
# Average pity = 105.6687438178803
# 0.9464% of all pulls are desired 5-star weapons on average
#
#
# CHARACTER BANNER (4-STAR)
#
# p=1 - d = 5.100000000000%, cum = 5.100000000000%, r = 94.900000000000%, raw = 5.10%
# p=2 - d = 4.839900000000%, cum = 9.939900000000%, r = 90.060100000000%, raw = 5.10%
# p=3 - d = 4.593065100000%, cum = 14.532965100000%, r = 85.467034900000%, raw = 5.10%
# p=4 - d = 4.358818779900%, cum = 18.891783879900%, r = 81.108216120100%, raw = 5.10%
# p=5 - d = 4.136519022125%, cum = 23.028302902025%, r = 76.971697097975%, raw = 5.10%
# p=6 - d = 3.925556551997%, cum = 26.953859454022%, r = 73.046140545978%, raw = 5.10%
# p=7 - d = 3.725353167845%, cum = 30.679212621867%, r = 69.320787378133%, raw = 5.10%
# p=8 - d = 3.535360156285%, cum = 34.214572778151%, r = 65.785427221848%, raw = 5.10%
# p=9 - d = 36.905624671457%, cum = 71.120197449608%, r = 28.879802550391%, raw = 56.10%
# p=10 - d = 28.879802550391%, cum = 100.000000000000%, r = 0.000000000000%, raw = 100.00%
#
# Average pity = 7.655392058144262
# 13.0627% of all pulls are 4-star characters on average
#
#
# WEAPON BANNER (4-STAR)
#
# p=1 - d = 6.000000000000%, cum = 6.000000000000%, r = 94.000000000000%, raw = 6.00%
# p=2 - d = 5.640000000000%, cum = 11.640000000000%, r = 88.360000000000%, raw = 6.00%
# p=3 - d = 5.301600000000%, cum = 16.941600000000%, r = 83.058400000000%, raw = 6.00%
# p=4 - d = 4.983504000000%, cum = 21.925104000000%, r = 78.074896000000%, raw = 6.00%
# p=5 - d = 4.684493760000%, cum = 26.609597760000%, r = 73.390402240000%, raw = 6.00%
# p=6 - d = 4.403424134400%, cum = 31.013021894400%, r = 68.986978105600%, raw = 6.00%
# p=7 - d = 4.139218686336%, cum = 35.152240580736%, r = 64.847759419264%, raw = 6.00%
# p=8 - d = 42.799521216714%, cum = 77.951761797450%, r = 22.048238202550%, raw = 66.00%
# p=9 - d = 22.048238202550%, cum = 100.000000000000%, r = 0.000000000000%, raw = 100.00%
#
# Average pity = 6.7276667396741345
# 14.8640% of all pulls are 4-star weapons on average
#
#
# CHARACTER BANNER (ON-BANNER 4-STAR)
#
# p=1 - d = 3.400000000000%, cum = 3.400000000000%, r = 94.900000000000%, raw = 3.40%
# p=2 - d = 3.226600000000%, cum = 6.626600000000%, r = 90.060100000000%, raw = 3.40%
# p=3 - d = 3.062043400000%, cum = 9.688643400000%, r = 85.467034900000%, raw = 3.40%
# p=4 - d = 2.905879186600%, cum = 12.594522586600%, r = 81.108216120100%, raw = 3.40%
# p=5 - d = 2.757679348083%, cum = 15.352201934683%, r = 76.971697097975%, raw = 3.40%
# p=6 - d = 2.617037701331%, cum = 17.969239636015%, r = 73.046140545978%, raw = 3.40%
# p=7 - d = 2.483568778563%, cum = 20.452808414578%, r = 69.320787378133%, raw = 3.40%
# p=8 - d = 2.356906770857%, cum = 22.809715185434%, r = 65.785427221849%, raw = 3.40%
# p=9 - d = 24.603749780971%, cum = 47.413464966406%, r = 28.879802550391%, raw = 37.40%
# p=10 - d = 19.253201700261%, cum = 66.666666666667%, r = 0.000000000000%, raw = 66.67%
#
# Average pity = 11.4830880872164
# 8.7085% of all pulls are on-banner 4-star characters on average
#
#
# WEAPON BANNER (ON-BANNER 4-STAR)
#
# p=1 - d = 4.800000000000%, cum = 4.800000000000%, r = 94.000000000000%, raw = 4.80%
# p=2 - d = 4.512000000000%, cum = 9.312000000000%, r = 88.360000000000%, raw = 4.80%
# p=3 - d = 4.241280000000%, cum = 13.553280000000%, r = 83.058400000000%, raw = 4.80%
# p=4 - d = 3.986803200000%, cum = 17.540083200000%, r = 78.074896000000%, raw = 4.80%
# p=5 - d = 3.747595008000%, cum = 21.287678208000%, r = 73.390402240000%, raw = 4.80%
# p=6 - d = 3.522739307520%, cum = 24.810417515520%, r = 68.986978105600%, raw = 4.80%
# p=7 - d = 3.311374949069%, cum = 28.121792464589%, r = 64.847759419264%, raw = 4.80%
# p=8 - d = 34.239616973371%, cum = 62.361409437960%, r = 22.048238202550%, raw = 52.80%
# p=9 - d = 17.638590562040%, cum = 80.000000000000%, r = 0.000000000000%, raw = 80.00%
#
# Average pity = 8.409583424592668
# 11.8912% of all pulls are on-banner 4-star weapons on average
