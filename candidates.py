from pprint import pprint

data = """
1			Benhur Abalos	PFP	Alyansa para sa Bagong Pilipinas	Secretary of the Interior and Local Government (2022–2024)
2			Jerome Adonis	Makabayan	Oposisyon ng Bayan	Secretary general of Kilusang Mayo Uno
3			Wilson Amad	Independent	—	
4			Jocelyn Andamo	Makabayan	Oposisyon ng Bayan	Secretary general of Filipino Nurses United
5			Bam Aquino	KANP	KiBam	Senator (2013–2019)
6			Ronnel Arambulo	Makabayan	Oposisyon ng Bayan	Vice chairperson of Pamalakaya
7			Ernesto Arellano	KKK	—	Founding President of National Confederation of Labor
8			Roberto Ballon	Independent	—	Leader of Kapunungan sa Gagmay'ng Mangingisda sa Concepcion
9			Abigail Binay	NPC	Alyansa para sa Bagong Pilipinas	Mayor of Makati (2016–present)
10			Jimmy Bondoc	PDP	DuterTen	Member of the Board of Directors of Philippine Amusement and Gaming Corporation (2021–2022)
11			Bong Revilla	Lakas	Alyansa para sa Bagong Pilipinas	Incumbent senator (since 2019)
12			Bonifacio Bosita	Independent	Riding-in-tandem Team	Incumbent House representative for 1-Rider Partylist (2022–present)
13			Arlene Brosas	Makabayan	Oposisyon ng Bayan	Incumbent House representative for GABRIELA (since 2016)
14			Roy Cabonegro	DPP	—	
15			Allen Capuyan	PPP	—	Chairperson of the National Commission on Indigenous Peoples (2019–2023)
16			Teodoro Casiño	Makabayan	Oposisyon ng Bayan	House representative for Bayan Muna (2004–2013)
17			France Castro	Makabayan	Oposisyon ng Bayan	Incumbent House representative for ACT Teachers (since 2016)
18			Pia Cayetano	Nacionalista	Alyansa para sa Bagong Pilipinas	Incumbent senator (since 2019)
19			David d'Angelo	Bunyog	—	
20			Angelo de Alban	Independent	—	
21			Leody de Guzman	PLM	—	Chairman of Bukluran ng Manggagawang Pilipino
22			Ronald dela Rosa	PDP	DuterTen	Incumbent senator (since 2019)
23			Mimi Doringo	Makabayan	Oposisyon ng Bayan	Secretary general of Kadamay
24			Arnel Escobal	PM	—	
25			Luke Espiritu	PLM	—	President of Bukluran ng Manggagawang Pilipino
26			Mody Floranda	Makabayan	Oposisyon ng Bayan	Chairperson of PISTON
27			Marc Gamboa	Independent	—	
28			Bong Go	PDP	DuterTen	Incumbent senator (since 2019)
29			Norberto Gonzales	PDSP	—	Secretary of National Defense (2009–2010)
30			Jesus Hinlo Jr.	PDP	DuterTen	Commissioner of the Presidential Anti-Corruption Commission (2022)
31			Gregorio Honasan	Reform PH	—	Secretary of Information and Communications Technology (2019–2021); Senator (2007–2019)
32			Relly Jose Jr.	KBL	—	
33			Panfilo Lacson	Independent	Alyansa para sa Bagong Pilipinas	Senator (2016–2022)
34			Raul Lambino    PDP	DuterTen	Administrator and Chief Executive Officer of the Cagayan Economic Zone Authority (2017–2022)
35			Lito Lapid	NPC	Alyansa para sa Bagong Pilipinas	Incumbent senator (since 2019)
36			Wilbert T. Lee\tAksyon
37			Amirah Lidasan	Makabayan	Oposisyon ng Bayan	Co-chairperson of Sandugo Movement of Moro and Indigenous Peoples for Self-Determination
38			Rodante Marcoleta	Independent	DuterTen	Incumbent House representative for SAGIP Partylist (since 2016)
39			Imee Marcos	Nacionalista	Alyansa para sa Bagong Pilipinas	Incumbent senator (since 2019)
40			Norman Marquez	Independent	—	
41			Eric Martinez	Independent	—	Incumbent House representative from Valenzuela's 2nd district (since 2016)
42			Richard Mata	Independent	DuterTen	
43			Sonny Matula	WPP	—	President of the Federation of Free Workers
44			Liza Maza	Makabayan	Oposisyon ng Bayan	Lead convenor of National Anti-Poverty Commission (2016–2018)
45			Heidi Mendoza	Independent	—	Commissioner of the Commission on Audit (2011–2015)
46			Jose Montemayor Jr.	Independent	—	
47			Subair Mustapha	WPP	—	
48			Jose Olivar	Independent	—	
49			Willie Ong\tAksyon
50			Manny Pacquiao	PFP	Alyansa para sa Bagong Pilipinas	Senator (2016–2022)
51			Francis Pangilinan	Liberal	KiBam	Senator (2016–2022)
52			Ariel Querubin	Nacionalista	Riding-in-tandem Team	Colonel, Philippine Marine Corps
53			Apollo Quiboloy	Independent	DuterTen	
54			Danilo Ramos	Makabayan	Oposisyon ng Bayan	Chairperson of Kilusang Magbubukid ng Pilipinas
55			Willie Revillame	Independent	—	
56			Vic Rodriguez	Independent	DuterTen	Executive Secretary (2022)
57			Nur-Ana Sahidulla	Independent	—	House representative from Sulu's 2nd district (2013–2016)
58			Phillip Salvador	PDP	DuterTen	
59			Tito Sotto	NPC	Alyansa para sa Bagong Pilipinas	Senator (2010–2022; Senate president (2018–2022)
60			Michael Tapado	PM	—	
61			Francis Tolentino	PFP	Alyansa para sa Bagong Pilipinas	Incumbent senator (since 2019)
62			Ben Tulfo	Independent	—	
63			Erwin Tulfo	Lakas	Alyansa para sa Bagong Pilipinas	Incumbent House representative for ACT-CIS Partylist (since 2023)
64			Mar Valbuena	Independent	—	Chairperson of Manibela
65			Leandro Verceles Jr.	Independent	—	Former governor of Catanduanes (2001–2007)
66			Camille Villar	Nacionalista	Alyansa para sa Bagong Pilipinas	Incumbent House representative from Las Piňas (since 2019)
"""

data_lines = data.strip().splitlines()
candidate_rows = [line.split("\t") for line in data_lines]
candidates = [f'{row[3]}' for row in candidate_rows if len(row) > 3]
partylists = list(set([f'{row[4]}' for row in candidate_rows if len(row) > 4]))

candidates_grouped = [candidates[i:i + 3] for i in range(0, len(candidates), 3)]
partylists_grouped = [partylists[i:i + 3] for i in range(0, len(partylists), 3)]

candidates_grouped_name_split = []

for candidate_group in candidates_grouped:
    c_group = []
    for candidate in candidate_group:
        name = candidate.split()
        for name_part in name:
            if len(name_part) > 3:
                c_group.append(name_part)
    candidates_grouped_name_split.append(c_group)

print(candidates)
print("Total candidates:", len(candidates))

print(partylists)
print("Total partylists:", len(partylists))


print(candidates_grouped_name_split)
print(partylists_grouped)
# print(", ".join(candidates))
# print(", ".join(partylists))

"""4Ps
PPP
FPJ Panday Bayanihan
Kabataan[c]
Duterte Youth
ML[d]
PBBM
P3PWD
Murang Kuryente
Bicol Saro
Ipatupad
PATROL
Juan PINOY
ARTE
WIFI
MAAGAP
United Senior Citizens
Epanaw Sambayanan
Ako Padayon
TUCP
ACT Teachers[c]
1PACMAN
TGP
DUMPER PTDA
Anakalusugan
Aksyon Dapat[e]
BHW
Sulong Dignidad
Batang Quiapo
PBA
GILAS
Ako Ilokano Ako
Pamilyang Magsasaka
Click Party
Abante Bisdak
Manila Teachers
PAMANA
Nanay
KM Ngayon Na
Babae Ako
ARISE
Magdalo
APEC
MAGBUBUKID
SSS-GSIS Pensyonado
GABRIELA[c]
Tingog
APAT-DAPAT
Ahon Mahirap
UGB
Akbayan
Agimat
PHILRECA
Kapuso PM
Ilocano Defenders
1-Rider Party-list
TICTOK
(skipped[f])
Bayan Muna[c]
Ang Probinsyano
BANAT
SBP
Buhay
Tulungan Tayo
SAGIP
BTS Bayaning Tsuper
Vendors
ACT-CIS
Aktibong Kaagapay
Asenso Pinoy
Solo Parents
Ang Komadrona
PROMDI
Pusong Pinoy
Kusug Tausug
Damayang Filipino
MPBL
ANGAT
Kalinga
Boses Party-list
Arangkada Pilipino
Aangat Tayo
OFW
BIDA KATAGUMPAY
KAMANGGAGAWA
BFF
Bunyog
AGRI
Senior Citizens
4K
PBP
One Coop
CIBAC
BH - Bagong Henerasyon
1AGILA
EDUAKSYON
Ang Tinig ng Seniors
BG Party-list
Pinoy Ako
H.E.L.P. PILIPINAS
Health Workers
People's Champ
AA-Kasosyo Party
Solid North Party
ABAMIN
TRABAHO
ANGKASangga
TODA Aksyon
Turismo
Abono
ASAP NA
LINGAP
United Frontliners
Kasambahay
Tutok To WIn
Ako OFW
AGAP
1TAHANAN
Coop-NATCCO
KABAYAN
1Munti
PINOY WORKERS
API Party
Ako Bisaya
KAMALAYAN
Ako Tanod
Probinsyano Ako
KABABAIHAN
RAM
ALONA
Ako Bikol
GP (Galing sa Puso)
KAUNLAD PINOY
ABP
CWS
LPGMA
A TEACHER
SWERTE
Gabay
Malasakit@Bayanihan
Akay ni Sol[g]
LUNAS
DIWA
PINUNO
Pamilya Muna
Bagong Pilipinas
Hugpong Federal
Tupad
Lang Kawal
Pamilya Ko
BBM
Heal PH
Abang Lingkod
MAGSASAKA
Maharlika
Uswag Ilonggo
"""