molecules = ["Ammonia", "Aspirin", "Calcium Oxide", "Carbon Dioxide",
             "Cobalt Tetrachloride", "DDT", "Ethanol", "Ethlyene",
             "Morphine", "Penicilin G", "Phosphoric Acid", "Potassium Nitrate",
             "Progestin", "Sodium Chloride", "Sodium Hydroxide",
             "Sodium Stearate", "Silicon Dioxide", "Sulfuric Acid", "Toluene", "Urea"]
molecule_information = {
    "introduction":("Ammonia is a compound composed of nitrogen and hydrogen atoms, \n\
commonly used in household cleaning products and industrial processes"\
,"Aspirin, also known as acetylsalicylic acid, is a widely used \n\
medication primarily known for its analgesic (pain-relieving), \n\
antipyretic (fever-reducing), and anti-inflammatory properties.",\
"Calcium oxide, also known as quicklime, is a versatile inorganic \n\
compound widely used in various industries for its pivotal roles in \n\
construction, metallurgy, water treatment, and chemical manufacturing.","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"),
    "melting point":("-77.73","136","2,613","a","a","a","a","a","a","a","a","a","a","a","a","a"),
    "boiling point":("-33.34","140","2,850","a","a","a","a","a","a","a","a","a","a","a","a"),
    "hazards":("Toxicity: \n\
Ammonia is toxic when inhaled or ingested in high concentrations. \n\
Inhalation of ammonia vapors can irritate the respiratory tract, leading\n\
to coughing, wheezing, and difficulty breathing. In severe cases, \n\
exposure to high levels of ammonia can cause chemical pneumonitis, \n\
pulmonary edema, and even death.\n\
Corrosive:\n\
Ammonia is corrosive to skin, eyes, and mucous membranes.Direct contact \n\
with concentrated ammonia solutions or vapors can cause irritation, \n\
burns, and tissue damage. Prolonged exposure may lead to chemical \n\
burns and permanent damage to the skin and eyes.\n\
Flammability:\n\
Ammonia is highly flammable in the presence of certain substances, \n\
such as chlorine or fluorine compounds. Mixing ammonia with oxidizing \n\
agents can also result in fire or explosion hazards. Therefore, proper \n\
storage and handling practices are essential to prevent accidental \n\
ignition.\n\
Reactivity: \n\
Ammonia is reactive with various substances, including acids, metals, \n\
and oxidizing agents. It can form explosive or toxic compounds when \n\
mixed with certain chemicals. For example, the reaction between ammonia \n\
and chlorine can produce toxic chloramines, while the \n\
reaction with halogens can form explosive compounds.",\
"Gastrointestinal Side Effects: \n\
One of the most common hazards of aspirin is its potential to \n\
cause gastrointestinal irritation and ulcers. Prolonged use of \n\
aspirin, especially in high doses or for individuals with a history \n\
of gastrointestinal issues, can lead to stomach bleeding, gastritis, \n\
and peptic ulcers.\n\
Increased Bleeding Risk: \n\
Aspirin inhibits the function of platelets, which are blood cells \n\
involved in clotting. While this property makes aspirin useful in \n\
preventing blood clots and reducing the risk of heart attacks and \n\
strokes, it also increases the risk of bleeding, particularly in \n\
individuals undergoing surgery or those with bleeding disorders.\n\
Reye's Syndrome: Aspirin use in children and teenagers with viral \n\
infections, such as influenza or chickenpox, has been associated with \n\
an increased risk of Reye's syndrome. This rare but serious condition \n\
can lead to liver and brain damage, with symptoms including vomiting, \n\
confusion, seizures, and loss of consciousness.\n\
Allergic Reactions: \n\
Some individuals may experience allergic reactions to aspirin, ranging \n\
from mild skin rashes and hives to severe anaphylaxis, which can be \n\
life-threatening. People with known aspirin allergies or hypersensitivity \n\
to nonsteroidal anti-inflammatory drugs (NSAIDs) should avoid aspirin.\n\
Asthma Exacerbation: \n\
Aspirin sensitivity can trigger or worsen asthma symptoms in certain \n\
individuals, leading to asthma attacks, difficulty breathing, and wheezing. \n\
This condition, known as aspirin-exacerbated respiratory disease (AERD), \n\
requires careful avoidance of aspirin and related medications.\n\
Renal Toxicity: \n\
Prolonged or high-dose aspirin use can cause kidney damage and impairment\n\
of renal function, leading to conditions such as acute kidney injury and \n\
interstitial nephritis. Individuals with pre-existing kidney disease or \n\
reduced renal function are particularly susceptible to aspirin-related \n\
renal toxicity.\n\
Overdose and Toxicity: \n\
Accidental or intentional overdose of aspirin can result in salicylate \n\
toxicity, characterized by symptoms such as nausea, vomiting, ringing in \n\
the ears (tinnitus), dizziness, confusion, rapid breathing (hyperventilation), \n\
metabolic acidosis, and in severe cases, seizures, coma, and death.",\
"Corrosive: \n\
Calcium oxide is highly corrosive to the skin, eyes, and respiratory tract. \n\
Contact with the skin or eyes can cause severe burns.\n\
Reactivity: \n\
It reacts vigorously with water to produce heat and can cause severe \n\
burns upon contact.\n\
Inhalation Hazard: \n\
Inhaling calcium oxide dust can irritate the respiratory tract and \n\
cause coughing, shortness of breath, and lung damage.\n\
Environmental Hazard: \n\
Calcium oxide can react with moisture in the air to form calcium \n\
hydroxide, which can be harmful to aquatic life if it enters water bodies.\n\
Fire Hazard: \n\
Calcium oxide is not flammable, but it can react exothermically with \n\
water, releasing heat, which may ignite combustible materials in the vicinity.\n\
Storage Hazard: \n\
It should be stored in a dry area away from moisture and incompatible materials \n\
to prevent spontaneous reactions.","a","a","a","a","a","a","a","a","a","a","a","a"),
    "uses":("Fertilizer Production: \n\
Ammonia is a crucial component in the production of\n\
nitrogen-based fertilizers. It serves as a source of nitrogen for plants, which\n\
is essential for their growth and development. Ammonia is converted \n\
into other nitrogen-containing compounds such as ammonium nitrate,\n\
urea, and ammonium sulfate, which are widely used as \n\
fertilizers in agriculture.\n\
Industrial Chemical Production: \n\
Ammonia is used as a precursor in \n\
the production of various industrial chemicals. It is a key raw \n\
material in the synthesis of nitric acid, which is used in \n\
the manufacture of fertilizers, explosives, and other chemicals. \n\
Additionally, ammonia is used in the production of urea, an \n\
important compound in the manufacture of plastics, adhesives, and textiles.\n\
pH Control: \n\
In various industries, ammonia is used as a pH regulator or \n\
buffer due to its alkaline properties. It can help \n\
adjust the pH of solutions in processes such\n\
as water treatment, chemical manufacturing, and food production.",\
"Pain Relief: \n\
Aspirin is commonly used to relieve mild to moderate pain, including \n\
headaches, toothaches, muscle aches, menstrual cramps, and joint pain \n\
associated with conditions like arthritis.\n\
Fever Reduction: \n\
Aspirin is an effective antipyretic medication, meaning it helps reduce \n\
fever by lowering the body's temperature. It is often used to alleviate \n\
fever associated with infections and inflammatory conditions.\n\
Anti-inflammatory Properties: \n\
Aspirin belongs to a class of medications known as nonsteroidal \n\
anti-inflammatory drugs (NSAIDs). It helps reduce inflammation by \n\
inhibiting the production of prostaglandins, which are substances \n\
involved in the inflammatory response. As a result, aspirin is used to \n\
alleviate inflammation and swelling in conditions like arthritis, \n\
tendonitis, and bursitis.",\
"Construction Industry: \n\
Calcium oxide, commonly known as quicklime, is a crucial ingredient in \n\
cement manufacturing. When mixed with water, it forms calcium hydroxide, \n\
which reacts with atmospheric carbon dioxide to harden into calcium carbonate, \n\
a key component of concrete and mortar used in construction projects worldwide.\n\
Its role in the construction industry underscores its importance in \n\
infrastructure development and urbanization.\n\
Steel Manufacturing: \n\
In the steel industry, calcium oxide serves as a fluxing agent during the \n\
purification of molten iron. It helps remove impurities such as silica, \n\
phosphorus, and sulfur from the iron ore, thereby enhancing the quality of \n\
the final steel product. This process, known as steel desulfurization, is \n\
essential for producing high-quality steel used in various applications, \n\
including automotive manufacturing, construction, and machinery production.","a","a","a","a","a","a","a","a","a","a","a","a")}
molecule_string = ["[Co-2](Cl)(Cl)(Cl)Cl"]

molecule_information1 = ("dfsdfsdfsdfs","dsfsfsdfdsfds\nsdfsdfd","hdsksdhdfkhds hj sdhjshds dh\nsdhfhdshj hads\ns sdhhi9")
#monia is a compound composed of nitrogen and hydrogen atoms, commonly used in household cleaning products and industrial processes
