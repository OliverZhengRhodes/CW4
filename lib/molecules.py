molecules = ["Ammonia", "Aspirin", "Calcium Oxide", "Carbon Dioxide",
             "Cobalt Tetrachloride", "DDT", "Ethanol", "Ethylene",
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
construction, metallurgy, water treatment, and chemical manufacturing.",\
"Carbon dioxide is a colorless, odorless gas naturally present in the Earth's \n\
atmosphere, crucial for photosynthesis and a significant greenhouse gas.",\
"Cobalt tetrachloride, a coordination compound with the chemical formula \n\
[CoCl4]2-, is a versatile chemical used in catalysis, chemical synthesis, \n\
and materials science applications.",\
"DDT, an abbreviation for dichlorodiphenyltrichloroethane, is a \n\
synthetic pesticide historically used for its effectiveness against \n\
insects but later banned due to its persistence in the environment and \n\
potential health risks.",\
"Ethanol, a simple alcohol with the chemical formula C2H5OH, is a \n\
versatile solvent, fuel, and beverage commonly produced through \n\
fermentation and widely used in various industrial, medical, and \n\
recreational applications.",\
"Ethylene, a simple hydrocarbon with the chemical formula C2H4, \n\
is a crucial building block in the petrochemical industry, widely \n\
utilized in the production of plastics, synthetic rubber, and \n\
various organic chemicals.",\
"Morphine, a potent opioid analgesic derived from the opium poppy \n\
plant, is widely used for its effective pain-relieving properties \n\
but also carries a high risk of addiction and dependence.",\
"Penicillin G, a first-generation antibiotic derived from the Penicillium \n\
fungi, revolutionized medicine with its broad-spectrum efficacy against \n\
bacterial infections, marking a milestone in the treatment of various diseases.",\
"Phosphoric acid, a mineral acid with the chemical formula H3PO4, is a \n\
versatile compound widely used in various industries, including food and \n\
beverage production, agriculture, and manufacturing, due to its role as a \n\
pH regulator, flavor enhancer, and key ingredient in fertilizer and \n\
chemical synthesis.",\
"Potassium nitrate, a chemical compound with the formula KNO3, is a \n\
versatile substance used in fertilizers, food preservation, fireworks, \n\
and various industrial applications due to its oxidizing and salting properties.",\
"Progestins, synthetic compounds mimicking the effects of natural \n\
progesterone, are widely used in hormonal contraceptives, hormone \n\
replacement therapy, and the treatment of gynecological disorders.\n\
They are a classs of synthetic hormones and the image is an example.",\
"Sodium chloride, commonly known as table salt, is a ubiquitous compound \n\
essential for human health, culinary preparation, and various \n\
industrial processes.",\
"Sodium hydroxide, commonly known as caustic soda, is a highly versatile \n\
compound integral to various industries for its role in chemical manufacturing, \n\
water treatment, and soap production.",\
"Sodium stearate is a white, odorless powder that serves as a versatile \n\
ingredient in cosmetics, soaps, and personal care products, functioning as \n\
an emulsifier, stabilizer, and cleansing agent due to its surfactant properties.",\
"Silicon dioxide, commonly known as silica, is a versatile compound \n\
found abundantly in nature and used extensively in various industries \n\
for its properties as a filler, abrasive, desiccant, and semiconductor material.",\
"Sulfuric acid, a highly corrosive and versatile chemical compound, is widely \n\
utilized in various industrial processes, from manufacturing fertilizers and \n\
detergents to refining petroleum and producing batteries.",\
"Toluene, a colorless and flammable liquid with a distinct sweet odor, is \n\
widely used as a solvent in various industrial processes and as a precursor in \n\
the production of chemicals such as benzene and xylene.",\
"Urea, a nitrogen-rich compound commonly used as a fertilizer, is an \n\
essential ingredient in agricultural practices and various industrial \n\
applications, including resin production and pharmaceuticals."),
    "melting point":("-77.73","136","2,613","-56.6","N/A","108.5","-114.5","-169.2","254.5","216","N/A","334","Various","800.7","323","250","1,713","10.31","-95","132.7"),
    "boiling point":("-33.34","140","2,850","-78.5","N/A","260","78.5","-103.7","Decomposes before boiling N/A","Decomposes before boiling N/A","N/A","400","Various","1,465","1,388","Decomposes before boiling N/A","2,950","337","110.6","Decomposes before boiling N/A"),
    "hazards":(
#ammonia
"Toxicity: \n\
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
#aspirin
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
#calcium oxide
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
to prevent spontaneous reactions.",\
#carbon dioxide
"Asphyxiation: \n\
Carbon dioxide's ability to displace oxygen poses a significant risk in \n\
confined spaces, where it can accumulate to dangerous levels. Industries \n\
such as breweries, mines, and manufacturing plants are particularly susceptible \n\
to this hazard, emphasizing the importance of proper ventilation and \n\
monitoring systems to prevent suffocation accidents.\n\
Respiratory Issues: \n\
Exposure to elevated levels of carbon dioxide can have immediate health \n\
effects, including headaches, dizziness, and respiratory distress. Prolonged \n\
exposure or sudden spikes in concentration can lead to more severe \n\
conditions such as respiratory acidosis, causing confusion, disorientation, \n\
and potential loss of consciousness. This underscores the necessity of \n\
stringent safety protocols and personal protective equipment in environments \n\
where CO2 is present.\n\
Climate Impact: \n\
As a potent greenhouse gas, carbon dioxide significantly contributes \n\
to global warming and climate change. Its accumulation in the atmosphere, \n\
primarily from human activities such as fossil fuel combustion and \n\
deforestation, is driving unprecedented shifts in weather patterns, \n\
rising sea levels, and ecological disruptions. Addressing carbon emissions \n\
through sustainable practices and renewable energy initiatives is crucial in \n\
mitigating these impacts and safeguarding the planet for future generations.",\
#cobalt tetrachloride
"The ion itself [CoCl4]2- is not commonly isolated, its compound may pose\n\
hazards similar to other cobalt-containing compounds.\n\
Toxicity: \n\
Cobalt compounds can be toxic if ingested, inhaled, or \n\
absorbed through the skin. They may cause symptoms such as nausea, \n\
vomiting, respiratory irritation, and, in severe cases, organ damage.\n\
Allergenic Potential: \n\
Some cobalt compounds have been associated with allergic reactions, \n\
particularly dermatitis, upon skin contact. Sensitization to cobalt can \n\
occur with repeated exposure.\
Environmental Hazard: \n\
If released into the environment, compounds containing the \n\
tetrachlorocobaltate(II) ion may be harmful to aquatic life and \n\
ecosystems. They can persist in the environment and may bioaccumulate \n\
in living organisms, leading to long-term ecological impacts.\n\
Corrosivity: \n\
Depending on the specific compound, tetrachlorocobaltate(II) salts may be \n\
corrosive to skin, eyes, and mucous membranes upon contact. \n\
They can cause burns, irritation, and tissue damage.",\
#ddt
"Toxicity: \n\
DDT is highly toxic to a wide range of organisms, including \n\
humans, and can accumulate in the environment and the food chain, \n\
leading to harmful effects on ecosystems and potential health \n\
risks for humans.\n\
Persistence: \n\
DDT is highly persistent in the environment, remaining active \n\
for long periods after application. This persistence can lead to \n\
bioaccumulation in organisms and long-term ecological impacts.\n\
Bioaccumulation: \n\
DDT and its breakdown products can accumulate in the fatty tissues \n\
of organisms, leading to biomagnification as it moves up the food \n\
chain. This can result in high concentrations of DDT in predators, \n\
posing risks to wildlife and potentially humans through consumption \n\
of contaminated food.\n\
Environmental Contamination: \n\
DDT contamination of soil, water, and air can have detrimental \n\
effects on ecosystems, including toxicity to aquatic life, disruption \n\
of food webs, and degradation of habitat quality.\n\
Endocrine Disruption: \n\
DDT has been shown to disrupt endocrine function in animals, \n\
mimicking or blocking hormones and potentially leading to reproductive \n\
and developmental abnormalities in exposed organisms.\n\
Regulatory Concerns: \n\
Due to its environmental persistence and health hazards, \n\
the use of DDT has been heavily regulated or banned in many countries. \n\
However, it continues to be used in some regions for disease vector control, \n\
raising concerns about human exposure and environmental contamination.",\
#ethanol
"Flammability: \n\
Ethanol is highly flammable, posing a significant fire hazard. \n\
Its vapors can form explosive mixtures with air, and it can ignite \n\
easily when exposed to ignition sources such as open flames, \n\
sparks, or heat.\n\
Health Effects: \n\
Ingestion of ethanol in excessive amounts can lead to alcohol \n\
poisoning, causing symptoms such as nausea, vomiting, impaired \n\
coordination, confusion, respiratory depression, coma, and even \n\
death. Chronic alcohol consumption can also lead to liver damage, \n\
addiction, and other long-term health issues.\n\
Irritant: \n\
Ethanol can irritate the skin, eyes, and respiratory tract upon \n\
contact or inhalation. Prolonged or repeated exposure to ethanol \n\
vapors can cause skin dryness, redness, irritation, as well as eye \n\
irritation and respiratory discomfort.\n\
Toxicity: \n\
While ethanol is metabolized by the body, excessive consumption \n\
can lead to ethanol toxicity, resulting in serious health \n\
complications. Additionally, ingesting denatured ethanol, which \n\
contains added toxic substances to deter consumption, can cause \n\
poisoning and harm.",\
#ethylene
"Flammability: \n\
Ethylene is highly flammable and can form explosive mixtures with \n\
air, posing fire and explosion hazards in the presence of ignition sources.\n\
Asphyxiation: \n\
Ethylene can displace oxygen in confined spaces, leading to an \n\
oxygen-deficient atmosphere and causing asphyxiation if proper \n\
ventilation is not maintained.\n\
Toxicity: \n\
Exposure to high concentrations of ethylene can cause respiratory irritation, \n\
dizziness, headache, and nausea. Prolonged exposure to elevated levels may \n\
result in more severe health effects, including central nervous system \n\
depression and asphyxiation.\n\
Reactivity: \n\
Ethylene may react violently with oxidizing agents, halogens, and strong \n\
acids, leading to the release of hazardous gases, fire, or explosion.\n\
Environmental Impact: \n\
Ethylene emissions contribute to air pollution and the formation of \n\
ground-level ozone, which can have adverse effects on human health \n\
and the environment.",\
#morphine
"Addiction and Dependence: \n\
Morphine use can lead to physical and psychological dependence, \n\
increasing the risk of addiction even when used as prescribed.\n\
Respiratory Depression: \n\
High doses of morphine can cause respiratory depression, potentially \n\
leading to life-threatening breathing difficulties, especially in \n\
individuals with respiratory conditions or when combined with other \n\
central nervous system depressants.\n\
Sedation and Impairment: \n\
Morphine can induce sedation, drowsiness, and impaired cognitive and \n\
motor function, affecting an individual's ability to perform tasks \n\
equiring mental alertness, such as driving or operating machinery.\n\
Constipation: \n\
Morphine use commonly leads to constipation due to its effects on \n\
gastrointestinal motility, necessitating the use of laxatives and careful \n\
monitoring, particularly in patients on long-term therapy.",\
#penicillin g
"Allergic Reactions: \n\
Penicillin G is known to cause allergic reactions, ranging from mild \n\
rashes to severe anaphylaxis, in individuals with penicillin allergy, \n\
which can be life-threatening.\n\
Antibiotic Resistance: \n\
Overuse or misuse of penicillin G can contribute to the development of \n\
antibiotic resistance in bacteria, reducing the drug's effectiveness and \n\
limiting treatment options for bacterial infections.\n\
Secondary Infections: \n\
Penicillin G therapy can disrupt the natural balance of microbial flora \n\
in the body, leading to overgrowth of opportunistic pathogens such as \n\
Clostridium difficile, causing antibiotic-associated diarrhea or other \n\
secondary infections.\n\
Adverse Effects: \n\
Penicillin G can cause various adverse effects, including gastrointestinal \n\
disturbances, allergic reactions, and rare but serious complications such \n\
as neurotoxicity or nephrotoxicity, necessitating careful monitoring \n\
and management during treatment.",\
#phosphoric acid
"Corrosive Properties: \n\
Concentrated phosphoric acid is highly corrosive and can cause severe \n\
burns and tissue damage upon contact with skin, eyes, and \n\
mucous membranes.\n\
Toxicity: \n\
Ingestion or inhalation of phosphoric acid vapors or mists can lead to \n\
respiratory and gastrointestinal irritation, nausea, vomiting, and potential \n\
systemic toxicity.\n\
Reactivity: \n\
Phosphoric acid can react violently with strong bases, oxidizing agents, and \n\
certain metals, potentially leading to the release of hazardous gases or \n\
causing explosions.\n\
Environmental Impact: \n\
Spills or releases of phosphoric acid can contaminate soil, water, and \n\
air, posing risks to aquatic life, ecosystems, and human health through \n\
exposure or contamination of food and water sources.",\
#potassium nitrate
"Oxidizing Agent: \n\
Potassium nitrate is a strong oxidizing agent, capable of causing or \n\
intensifying fires and explosions in the presence of combustible materials.\n\
Toxicity: \n\
Ingestion or inhalation of potassium nitrate dust or mist can cause \n\
irritation to the respiratory tract and gastrointestinal tract, leading to \n\
nausea, vomiting, abdominal pain, and potential systemic toxicity.\n\
Skin and Eye Irritation: \n\
Direct contact with potassium nitrate may cause irritation and burns \n\
to the skin and eyes, particularly in concentrated or prolonged exposures.\n\
Environmental Impact: \n\
Spills or releases of potassium nitrate can contaminate soil, water, and \n\
air, posing risks to aquatic life, ecosystems, and human health through \n\
exposure or contamination of food and water sources.",\
#progestin
"Cardiovascular Risks: \n\
Progestins, especially when used with estrogens, can increase the risk \n\
of cardiovascular events such as blood clots, stroke, and heart attack, \n\
particularly in women who smoke or have existing heart conditions.\n\
Hormonal Side Effects: \n\
Progestin use can lead to various hormonal side effects, including \n\
weight gain, mood changes, depression, breast tenderness, and menstrual \n\
irregularities, affecting overall well-being.\n\
Cancer Risks: \n\
Long-term use of certain progestins has been linked to an increased risk \n\
of breast cancer and potentially other cancers, necessitating careful \n\
monitoring and risk assessment.\n\
Liver Function: \n\
Progestins can impact liver function and may cause liver disorders or \n\
exacerbate pre-existing liver conditions, requiring regular liver function \n\
tests and close monitoring during treatment.",\
#sodium chloride
"Electrolyte Imbalance: \n\
Excessive intake of sodium chloride can lead to electrolyte imbalances, \n\
hypertension, and cardiovascular issues, particularly in individuals \n\
with pre-existing health conditions.\n\
Corrosion: \n\
Sodium chloride, when dissolved in water or present in high concentrations, \n\
can contribute to the corrosion of metals and infrastructure, especially \n\
in coastal areas or regions with de-icing practices.\n\
Environmental Impact: \n\
Runoff from road salt, primarily composed of sodium chloride, \n\
can contaminate freshwater bodies and soil, adversely affecting aquatic \n\
life, vegetation, and soil fertility.\n\
Respiratory Irritation: \n\
Inhalation of sodium chloride dust particles, generated during industrial \n\
processes or road salt application, can irritate the respiratory tract and \n\
worsen existing respiratory conditions in sensitive individuals.",\
#sodium hydroxide
"Corrosive Properties: \n\
Sodium hydroxide is highly corrosive and can cause severe burns to the \n\
skin, eyes, and respiratory tract upon contact, leading to tissue damage \n\
and potential scarring.\n\
Chemical Burns: \n\
Exposure to concentrated sodium hydroxide solutions can result in chemical \n\
burns, which may penetrate deep into tissues and require immediate \n\
medical attention.\n\
Inhalation Risks: \n\
Inhalation of sodium hydroxide dust or mist can irritate the respiratory \n\
tract, causing coughing, shortness of breath, and respiratory distress, \n\
especially in poorly ventilated areas.\n\
Reactivity: \n\
Sodium hydroxide reacts violently with acids, water, and certain metals, \n\
releasing heat and potentially flammable hydrogen gas, which can lead to \n\
fire or explosion hazards in confined spaces or when in contact with \n\
reactive materials.",\
#sodium stearate
"Skin Irritation: \n\
Sodium stearate can cause skin irritation upon prolonged or repeated \n\
contact, particularly in individuals with sensitive skin, leading to \n\
redness, itching, or rash.\n\
Eye Irritation: \n\
Direct contact with sodium stearate powder or solutions can irritate \n\
the eyes, causing redness, tearing, and discomfort, necessitating \n\
immediate rinsing with water and medical attention if symptoms persist.\n\
Ingestion Risks: \n\
Ingestion of large quantities of sodium stearate may lead to \n\
gastrointestinal irritation, nausea, vomiting, and diarrhea, although \n\
accidental ingestion of small amounts is unlikely to cause serious harm.\n\
Respiratory Irritation: \n\
Inhalation of sodium stearate dust or aerosols may irritate the respiratory \n\
tract, leading to coughing, throat irritation, and shortness of breath, \n\
particularly in poorly ventilated areas.",\
#silicon dioxide
"Respiratory Issues: \n\
Inhalation of fine silica dust particles can lead to respiratory issues \n\
such as silicosis, a lung disease characterized by inflammation and scarring \n\
of lung tissue, which can impair breathing and lead to long-term \n\
health problems.\n\
Skin Irritation: \n\
Prolonged or repeated contact with silica dust or solutions can cause \n\
skin irritation, dryness, and dermatitis, particularly in individuals with \n\
sensitive skin or pre-existing skin conditions.\n\
Eye Irritation: \n\
Direct contact with silica dust or solutions may irritate the eyes, causing \n\
redness, tearing, and discomfort, necessitating immediate rinsing with water \n\
and medical attention if symptoms persist.\n\
Chronic Health Effects: \n\
Long-term exposure to silica dust may increase the risk of developing lung \n\
cancer, chronic obstructive pulmonary disease (COPD), and other respiratory \n\
disorders, particularly in occupations with high silica exposure levels such as \n\
mining, construction, and manufacturing.\n\
Carcinogenicity: \n\
Crystalline silica has been classified as a Group 1 carcinogen by the \n\
International Agency for Research on Cancer (IARC), indicating sufficient \n\
evidence of its carcinogenicity in humans, particularly in occupations with high \n\
silica exposure levels such as mining, construction, and manufacturing.",\
#sulfuric acid
"Corrosive Properties: \n\
Sulfuric acid is highly corrosive and can cause severe burns upon contact with \n\
skin, eyes, and respiratory tract, leading to tissue damage and potential \n\
scarring.\n\
Chemical Burns: \n\
Exposure to concentrated sulfuric acid can result in chemical burns, which may \n\
penetrate deep into tissues and require immediate medical attention.\n\
Inhalation Risks: \n\
Inhalation of sulfuric acid vapors or mists can irritate the respiratory \n\
tract, causing coughing, shortness of breath, and respiratory distress, \n\
especially in poorly ventilated areas.\n\
Reactivity: \n\
Sulfuric acid is reactive with water and can release heat, leading to \n\
splattering and potential explosion hazards, particularly when diluted or \n\
mixed with incompatible substances.\n\
Environmental Impact: \n\
Spills or releases of sulfuric acid can contaminate soil, water, and air, \n\
posing risks to aquatic life, ecosystems, and human health through \n\
exposure or ingestion.",\
#toluene
"Health Risks: \n\
Inhalation or skin contact with toluene vapor or liquid can cause headaches, \n\
dizziness, nausea, and irritation to the respiratory tract and skin.\n\
Neurological Effects: \n\
Prolonged exposure to toluene may lead to neurological symptoms such \n\
as confusion, drowsiness, and impairment of coordination and \n\
cognitive functions.\n\
Fire and Explosion: \n\
Toluene is highly flammable and can form explosive mixtures with air, \n\
posing fire and explosion hazards, particularly in confined spaces or \n\
in the presence of ignition sources.\n\
Environmental Impact: \n\
Spills or releases of toluene can contaminate soil, water, and air, posing \n\
risks to ecosystems and human health through exposure or ingestion.\n\
Chronic Health Effects: \n\
Long-term exposure to toluene may lead to respiratory issues, liver and \n\
kidney damage, and adverse effects on the central nervous system, \n\
including memory loss and mood disturbances.",\
#urea
"Health Risks: \n\
Inhalation or skin contact with urea dust or solutions can cause \n\
irritation to the respiratory tract, eyes, and skin, leading to \n\
coughing, redness, and itching.\n\
Ingestion Hazards: \n\
Ingesting large amounts of urea can result in gastrointestinal \n\
disturbances such as nausea, vomiting, and diarrhea.\n\
Environmental Impact: \n\
Excessive use of urea as a fertilizer can lead to nutrient runoff, \n\
contributing to water pollution and eutrophication in aquatic \n\
ecosystems, harming aquatic life.\n\
Combustion Risks: \n\
While urea itself is not highly flammable, it can decompose at high \n\
temperatures to produce ammonia and nitrogen oxides, which are harmful \n\
and can pose combustion risks in confined spaces."),
    "uses":(
#ammonia
"Fertilizer Production: \n\
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
#aspirin
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
#calcium oxide
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
including automotive manufacturing, construction, and machinery production.",\
#carbon dioxide
"Food Preservation: \n\
Carbon dioxide is utilized in food packaging to extend shelf life by \n\
inhibiting microbial growth and oxidation, keeping perishable foods \n\
fresh for longer periods.\n\
Fire Suppression: \n\
In fire extinguishers and suppression systems, carbon dioxide is \n\
employed as a non-conductive and non-corrosive agent to smother fires \n\
by displacing oxygen, effectively extinguishing flames without leaving residue.\n\
Industrial Applications: \n\
Carbon dioxide finds widespread use in industrial processes such as welding, \n\
where it serves as a shielding gas to prevent oxidation during metal fabrication, \n\
and in chemical synthesis for producing compounds like urea and methanol.\n\
Medical Procedures: \n\
In medical procedures such as laparoscopy and cryotherapy, carbon dioxide \n\
is used as a cooling agent or insufflation gas to create pneumoperitoneum, \n\
facilitating minimally invasive surgeries and therapeutic interventions.",\
#cobalt tetrachloride
"Catalysis: \n\
Compounds containing the tetrachlorocobaltate(II) ion serve as catalysts \n\
in various organic synthesis reactions, facilitating processes such as \n\
oxidation, hydrogenation, and cross-coupling reactions, thereby enabling \n\
the efficient production of valuable chemical compounds.\n\
Chemical Synthesis: \n\
Tetrachlorocobaltate(II) complexes are crucial in chemical synthesis as \n\
they act as versatile building blocks for the preparation of other \n\
cobalt-containing compounds. These complexes participate in ligand \n\
exchange, coordination chemistry, and redox reactions, allowing for \n\
the synthesis of diverse chemical structures.\n\
Materials Science: \n\
Cobalt-containing compounds, including those with the \n\
tetrachlorocobaltate(II) ion, are studied for their potential \n\
applications in materials science. They are investigated as \n\
components of magnetic materials, catalyst supports, and \n\
semiconductor devices, contributing to advancements in \n\
technology and innovation.\n\
Analytical Chemistry: \n\
Compounds containing the tetrachlorocobaltate(II) ion are \n\
used in analytical chemistry as reagents or standards for \n\
chemical analysis techniques. They play a role in spectrophotometry, \n\
chromatography, and titration methods, aiding in the accurate \n\
determination of analyte concentrations and the characterization\n\
of chemical compounds.",\
#ddt
"Agricultural Pest Control: \n\
DDT was extensively used in agriculture to control crop pests \n\
such as mosquitoes, flies, and agricultural insects. Its \n\
effectiveness in reducing insect populations helped increase crop \n\
yields and protect agricultural production.\n\
Public Health: \n\
DDT was instrumental in combating vector-borne diseases such as \n\
malaria, typhus, and yellow fever. It was used to control disease-carrying \n\
mosquitoes in public health programs, leading to significant reductions \n\
in disease transmission and mortality rates.\n\
Veterinary Medicine: \n\
DDT was also used in veterinary medicine to control pests such as fleas, \n\
ticks, and lice on livestock and pets. Its use helped prevent the spread \n\
of diseases carried by these parasites and improve animal health.\n\
Household Insect Control: \n\
DDT-based insecticides were commonly used for household pest control, \n\
including the elimination of cockroaches, ants, and other household \n\
insects. Its residual activity made it effective for long-term pest \n\
management in homes and buildings.",\
#ethanol
"Fuel: \n\
Ethanol is commonly blended with gasoline to produce ethanol \n\
fuel (E10, E85), used in vehicles as a renewable and cleaner-burning \n\
alternative to pure gasoline. It is also used as a biofuel in ethanol \n\
distillation plants, contributing to reducing greenhouse gas emissions \n\
and dependence on fossil fuels.\n\
Solvent: \n\
Ethanol serves as a solvent in numerous industries, including \n\
pharmaceuticals, cosmetics, and chemical manufacturing. It is used \n\
to dissolve and extract various compounds, to clean equipment and \n\
surfaces, and as a carrier solvent in formulations such as medications, \n\
perfumes, and household products.\n\
Beverage: \n\
Ethanol is a primary ingredient in alcoholic beverages such as beer, \n\
wine, and spirits. Its consumption is deeply ingrained in cultural and \n\
social practices worldwide, making it a significant economic \n\
commodity in the beverage industry.\n\
Industrial Processes: \n\
Ethanol is utilized in industrial processes such as fermentation, \n\
extraction, and synthesis. It is used as a feedstock for producing \n\
chemicals like ethylene, acetic acid, and ethyl acetate, as well as \n\
in the manufacture of sanitizers, disinfectants, and antiseptics due \n\
to its antimicrobial properties.",\
#ethylene
"Polymer Production: \n\
Ethylene is a primary raw material for the production of polyethylene, \n\
one of the most widely used plastics worldwide. Polyethylene is utilized \n\
in packaging, containers, pipes, construction materials, and numerous other \n\
applications due to its versatility, durability, and low cost.\n\
Chemical Intermediates: \n\
Ethylene is used as a precursor in the synthesis of various organic chemicals \n\
and intermediates, including ethylene oxide, ethylene glycol, vinyl chloride, \n\
and styrene. These chemicals are further processed into products such as antifreeze, \n\
plastics, solvents, and synthetic rubber.\n\
Agrochemicals: \n\
Ethylene is employed in agriculture to stimulate the ripening of fruits, \n\
vegetables, and flowers. It is used in controlled atmospheres and ripening \n\
chambers to accelerate the ripening process, improve fruit quality, and extend \n\
shelf life, benefiting both producers and consumers.\n\
Manufacturing: \n\
Ethylene serves as a feedstock for the production of numerous industrial \n\
chemicals and materials, including ethanol, acetic acid, polyvinyl chloride (PVC), \n\
and polystyrene. These chemicals are used in various industries, including \n\
automotive, construction, electronics, and textiles, contributing to the \n\
manufacturing of diverse products and materials.",\
#morphine
"Pain Management: \n\
Morphine is widely used for the treatment of moderate to severe pain, such \n\
as that caused by surgery, injury, cancer, or other medical conditions. It is \n\
particularly effective in providing relief from acute pain, such as post-operative \n\
pain or pain associated with myocardial infarction.\n\
Palliative Care: \n\
Morphine is an essential medication in palliative care and end-of-life care, \n\
helping to alleviate severe pain and improve the quality of life for patients with \n\
advanced or terminal illnesses, such as cancer or AIDS.\n\
Anesthesia: \n\
Morphine may be used as part of anesthesia during surgical procedures to provide \n\
pain relief and reduce the need for other anesthetic agents. It is often used in \n\
combination with other medications for balanced anesthesia and \n\
post-operative pain management.\n\
Cough Suppression: \n\
Morphine has antitussive properties and may be used in certain \n\
formulations to suppress cough, particularly in cases where other \n\
treatments have been ineffective or when coughing is interfering \n\
with sleep or quality of life.",\
#penicillin g
"Bacterial Infections: \n\
Penicillin G is effective against a wide range of bacterial infections, \n\
including streptococcal infections, pneumococcal infections, syphilis, \n\
meningitis, and other susceptible bacterial diseases, serving as a first-line \n\
treatment for many bacterial infections.\n\
Prophylaxis: \n\
Penicillin G is used prophylactically to prevent bacterial infections in certain \n\
high-risk individuals, such as those undergoing surgery, dental procedures, or \n\
childbirth, as well as in the management of certain medical conditions, such as \n\
rheumatic fever or recurrent streptococcal infections\n\
Syphilis Treatment: \n\
Penicillin G remains the treatment of choice for syphilis, particularly in the \n\
early stages of the disease, where it can effectively cure the infection \n\
and prevent complications.\n\
Prevention of Rheumatic Fever: \n\
Penicillin G is used to prevent recurrent episodes of rheumatic fever in \n\
individuals with a history of acute rheumatic fever or rheumatic heart disease, \n\
helping to reduce the risk of further heart damage.",\
#phosphoric acid
"Food and Beverage Industry: \n\
Phosphoric acid serves as an acidulant and flavoring agent in carbonated \n\
beverages, providing tartness and enhancing flavor profiles in colas and sodas.\n\
Fertilizer Production: \n\
Phosphoric acid is a crucial component in the manufacturing of phosphate \n\
fertilizers, essential for promoting plant growth and improving crop yields \n\
in agriculture.\n\
Metal Surface Treatment: \n\
Phosphoric acid is used in metal surface treatment processes, such as metal \n\
etching and phosphating, to prepare surfaces for painting, coating, or \n\
plating by promoting adhesion and corrosion resistance.\n\
Water Treatment: \n\
Phosphoric acid is utilized in water treatment applications to adjust \n\
pH levels, control alkalinity, and inhibit corrosion in water distribution \n\
systems, ensuring safe and stable drinking water supply.",\
#potassium nitrate
"Fertilizer: \n\
Potassium nitrate is widely used as a source of potassium and nitrogen \n\
in fertilizers, promoting plant growth and enhancing crop yields in agriculture.\n\
Food Preservation: \n\
Potassium nitrate is utilized as a preservative in cured meats, such as \n\
bacon and ham, to prevent bacterial growth and spoilage, extending shelf \n\
life and maintaining product quality.\n\
Pyrotechnics: \n\
Potassium nitrate serves as a key ingredient in the formulation of fireworks \n\
and pyrotechnic compositions, providing oxygen for combustion and \n\
contributing to the vibrant colors and effects of fireworks displays.\n\
Pharmaceuticals: \n\
Potassium nitrate is employed in certain pharmaceutical formulations and \n\
oral hygiene products, such as toothpaste and mouthwash, for its antimicrobial\n\
properties and desensitizing effects on sensitive teeth.\n\
Industrial Applications: \n\
Potassium nitrate is used in various industrial processes, including metallurgy, \n\
glass manufacturing, and electronics, as a flux, oxidizing agent, and \n\
component in chemical synthesis.\n\
Heat Treatment: \n\
Potassium nitrate is utilized in certain heat treatment processes, such as \n\
nitrate hardening, for enhancing the surface hardness and wear resistance \n\
of metals and alloys.",\
#progestin
"Birth Control: \n\
Progestin-only contraceptives, such as the progestin-only pill \n\
(mini-pill), contraceptive implant, and progestin-containing intrauterine \n\
devices (IUDs), are used to prevent pregnancy by inhibiting ovulation, \n\
thickening cervical mucus, and thinning the uterine lining.\n\
Hormone Replacement Therapy (HRT): \n\
Progestins, often combined with estrogen, are used in hormone replacement \n\
therapy to alleviate symptoms of menopause, such as hot flashes, vaginal \n\
dryness, and mood swings, and reduce the risk of osteoporosis and \n\
colorectal cancer.\n\
Treatment of Menstrual Disorders: \n\
Progestins may be prescribed to treat menstrual disorders, such as irregular \n\
or heavy menstrual bleeding, dysmenorrhea (painful periods), and \n\
premenstrual syndrome (PMS), by regulating the menstrual cycle and \n\
reducing menstrual flow.\n\
Endometrial Protection: \n\
In women receiving estrogen therapy for menopausal symptoms, progestins \n\
are used to protect the endometrium (uterine lining) from the \n\
potential risk of endometrial hyperplasia (overgrowth) and cancer \n\
associated with unopposed estrogen use.\n\
Treatment of Endometriosis: \n\
Progestins may be used to alleviate symptoms of endometriosis, a condition \n\
characterized by the presence of endometrial tissue outside the uterus, by \n\
suppressing ovulation, reducing menstrual flow, and relieving pelvic pain.\n\
Breast Cancer Treatment: \n\
Some progestins, such as megestrol acetate, are used in the treatment of \n\
advanced or metastatic breast cancer, either alone or in combination with \n\
other cancer therapies, to slow tumor growth and alleviate symptoms.\n\
Management of Hyperplasia: \n\
Progestins are prescribed to manage endometrial hyperplasia, a condition \n\
characterized by abnormal thickening of the uterine lining, to induce menstrual \n\
bleeding and prevent progression to endometrial cancer.\n\
Androgen Suppression: \n\
Progestins, particularly in high doses, may be used to suppress androgen \n\
(male hormone) production in conditions such as hirsutism \n\
(excessive hair growth) and gender-affirming hormone therapy \n\
for transgender individuals.",\
#sodium chloride
"Culinary: \n\
Sodium chloride is a fundamental ingredient in cooking and food \n\
preservation, enhancing flavor and serving as a key seasoning agent \n\
in various cuisines worldwide.\n\
Food Processing: \n\
Sodium chloride is utilized in food processing to improve texture, \n\
preserve freshness, and extend shelf life in products \n\
such as canned foods, cured meats, and pickled vegetables.\n\
Chemical Industry: \n\
Sodium chloride serves as a feedstock for the production \n\
of various chemicals, including chlorine, sodium hydroxide (caustic soda), \n\
and sodium carbonate (soda ash), essential for manufacturing processes \n\
in industries such as pharmaceuticals, textiles, and plastics.\n\
De-Icing: \n\
Sodium chloride is widely used as a de-icing agent to melt snow and \n\
ice on roads, sidewalks, and runways, improving traction and safety during \n\
winter weather conditions.\n\
Water Treatment: \n\
Sodium chloride is employed in water treatment processes, such as water \n\
softening and disinfection, to remove impurities, adjust pH levels, and prevent \n\
microbial growth in drinking water and wastewater treatment systems.\n\
Healthcare: \n\
Sodium chloride solutions are used in medical settings for various purposes, \n\
including intravenous hydration, wound irrigation, and nasal irrigation, due \n\
to their isotonic properties and compatibility with the human body.\n\
Chemical Reactions: \n\
Sodium chloride is utilized in laboratory settings as a reagent and catalyst \n\
in chemical reactions, including precipitation reactions, redox reactions, \n\
and electrolysis experiments.",\
#sodium hydroxide
"Chemical Manufacturing: \n\
Sodium hydroxide serves as a key raw material in the production of various \n\
chemicals, including soaps, detergents, bleaches, pharmaceuticals, and \n\
synthetic materials such as plastics and textiles.\n\
Water Treatment: \n\
Sodium hydroxide is used in water treatment processes to adjust pH levels, \n\
neutralize acidic wastewater, and remove heavy metals and impurities through \n\
precipitation and coagulation, ensuring safe and clean water for drinking \n\
and industrial purposes.\n\
Paper and Pulp Industry: \n\
Sodium hydroxide is employed in the paper and pulp industry to break down \n\
lignin and cellulose fibers during the pulping process, facilitating the \n\
separation of pulp from wood and improving paper quality and brightness.\n\
Alumina Production: \n\
Sodium hydroxide is utilized in the Bayer process to extract alumina from \n\
bauxite ore, a crucial step in the production of aluminum metal, by dissolving \n\
alumina-bearing minerals and separating them from impurities.\n\
Petroleum Refining: \n\
Sodium hydroxide is used in petroleum refining processes, such as oil and \n\
gas extraction, refining, and petrochemical production, for desulfurization, \n\
neutralization of acidic impurities, and removal of organic contaminants.\n\
Food Processing: \n\
Sodium hydroxide is employed in food processing to regulate pH levels, \n\
control acidity, and neutralize acidic solutions in various food products, \n\
including cocoa processing, vegetable peeling, and poultry scalding.\n\
Cleaning and Degreasing: \n\
Sodium hydroxide is a potent degreaser and cleaning agent, used in industrial \n\
cleaning applications, surface preparation, and oven cleaning, to remove \n\
grease, oil, and organic residues from surfaces and equipment.\n\
Drain and Pipe Maintenance: \n\
Sodium hydroxide is utilized in drain and pipe maintenance products, such as \n\
drain cleaners and pipe degreasers, to dissolve and remove clogs, fats, oils, and \n\
organic matter from plumbing systems.",\
#sodium stearate
"Cosmetics and Personal Care Products: \n\
Sodium stearate serves as a key ingredient in the formulation of cosmetics, \n\
skincare products, and toiletries such as soaps, shampoos, and creams, where it \n\
functions as an emulsifier, stabilizer, and cleansing agent, imparting a smooth \n\
texture and enhancing product stability.\n\
Pharmaceuticals: \n\
Sodium stearate is used in pharmaceutical formulations as an excipient and \n\
tabletbinder to improve the flow properties, compressibility, and \n\
disintegration characteristics of tablets and capsules, facilitating \n\
drug delivery and dosage administration.\n\
Food Additives: \n\
Sodium stearate is utilized as a food additive, primarily as an \n\
emulsifying agent and lubricant in food processing and manufacturing, \n\
where it helps to stabilize emulsions, prevent ingredient separation, \n\
and enhance texture in products such as bakery goods, confectionery, \n\
and processed foods.\n\
Industrial Applications: \n\
Sodium stearate serves as a lubricant, anti-caking agent, and mold \n\
release agent in various industrial processes, including rubber \n\
manufacturing, plastics production, and metalworking, where it facilitates \n\
material handling, processing, and product release.\n\
Surfactants and Detergents: \n\
Sodium stearate is employed as a surfactant and detergent ingredient \n\
in household and industrial cleaning products, laundry detergents, \n\
and dishwashing liquids, where it helps to emulsify and solubilize \n\
oils, grease, and dirt, facilitating their removal from surfaces.\n\
Textile Industry: \n\
Sodium stearate is used in the textile industry as a softening agent \n\
and lubricant in fabric sizing and finishing processes, improving fabric \n\
handle, reducing friction, and enhancing dye absorption and color uniformity.\n\
Rubber and Plastic Production: \n\
Sodium stearate is utilized as a processing aid and stabilizer in the \n\
manufacturing of rubber products, PVC plastics, and polyolefin materials, \n\
where it acts as a lubricant, anti-static agent, and mold release agent, \n\
improving material flow and processing efficiency.",\
#silicon dioxide
"Construction Materials: \n\
Silicon dioxide is a key component in the production of concrete, \n\
mortar, and cementitious materials, where it enhances strength, \n\
durability, and workability.\n\
Glass Manufacturing: \n\
Silicon dioxide is the primary component of glass, providing \n\
structural integrity, transparency, and thermal stability in \n\
various glass products.\n\
Electronics: \n\
Silicon dioxide is used in semiconductor manufacturing as a \n\
substrate material for integrated circuits (ICs) and as an \n\
insulator in electronic components due to its dielectric \n\
properties and thermal stability.\n\
Cosmetics and Personal Care Products: \n\
Silicon dioxide is utilized in cosmetics and personal care items \n\
such as toothpaste and skincare products for its abrasive properties, \n\
thickening capabilities, and oil-absorbing qualities.\n\
Food and Beverage Industry: \n\
Silicon dioxide is approved as a food additive and used in food \n\
processing to prevent caking, improve flow properties, and act as \n\
a clarifying agent in powdered mixes, spices, and beverages.",\
#sulfuric acid
"Chemical Manufacturing: \n\
Sulfuric acid is a key component in the production of various \n\
chemicals, including fertilizers, detergents, pharmaceuticals, \n\
and explosives.\n\
Petroleum Refining: \n\
Sulfuric acid is used in petroleum refining processes to remove \n\
impurities, such as sulfur compounds, from crude oil and petroleum products, \n\
improving their quality and compliance with environmental regulations.\n\
Metal Processing: \n\
Sulfuric acid is utilized in the mining and metallurgical industries for \n\
leaching, extraction, and purification processes, including the production \n\
of copper, zinc, and nickel.\n\
Battery Production: \n\
Sulfuric acid is a crucial component in lead-acid batteries, commonly used \n\
in automobiles, uninterruptible power supplies (UPS), and industrial \n\
applications, where it serves as the electrolyte for energy storage and release.\n\
Textile Industry: \n\
Sulfuric acid is employed in textile processing for dyeing, bleaching, and \n\
finishing operations, where it facilitates color fixation, fiber modification, \n\
and fabric treatment.\n\
Water Treatment: \n\
Sulfuric acid is used in water and wastewater treatment processes to adjust pH \n\
levels, neutralize alkalinity, and remove contaminants such as heavy metals \n\
and organic pollutants.\n\
Pulp and Paper Manufacturing: \n\
Sulfuric acid is utilized in the production of pulp and paper, where it is used \n\
in the pulping process to break down lignin and separate cellulose fibers \n\
from wood.\n\
Cleaning and Descaling: Sulfuric acid is employed in industrial cleaning \n\
applications, such as descaling of boilers, tanks, and equipment, where it \n\
removes mineral deposits and scale buildup through chemical \n\
reaction and dissolution.",\
#toluene
"Solvent: \n\
Toluene serves as a versatile solvent in the production of paints, coatings, \n\
adhesives, and inks, facilitating the dissolution of resins, polymers, \n\
and other organic compounds.\n\
Chemical Manufacturing: \n\
Toluene is a key raw material in the synthesis of various chemicals, \n\
including benzene, xylene, and TNT (trinitrotoluene), used in the production \n\
of plastics, synthetic fibers, and explosives.\n\
Fuel Additive: \n\
Toluene is used as a fuel additive in gasoline to enhance octane ratings \n\
and improve engine performance, particularly in high-performance engines \n\
and racing fuels.\n\
Intermediate in Pharmaceuticals: \n\
Toluene is employed as an intermediate in the synthesis of pharmaceuticals, \n\
including analgesics, antiseptics, and antispasmodics, contributing to the \n\
production of various medicines and healthcare products.\n\
Rubber and Polymer Industry: Toluene is used in the production of \n\
synthetic rubbers, elastomers, and polymers, where it acts as a solvent, \n\
diluent, and reaction medium in polymerization processes.\n\
Cleaning and Degreasing: \n\
Toluene-based solvents are utilized in industrial cleaning applications, \n\
degreasing of machinery, and removal of oil and grease from metal parts, \n\
providing effective cleaning and surface preparation.\n\
Adhesives and Sealants: \n\
Toluene is incorporated into adhesives and sealants formulations to \n\
improve viscosity, adhesion, and drying characteristics, enhancing the \n\
performance and durability of bonded materials.\n\
Laboratory Reagent: \n\
Toluene is used as a laboratory reagent and solvent in chemical research \n\
and analysis, for chromatography, extraction, and synthesis purposes.",\
#urea
"Fertilizer: \n\
Urea is the most commonly used nitrogen fertilizer in agriculture, providing \n\
an essential nutrient that promotes plant growth and increases crop yields.\n\
Chemical Industry: \n\
Urea is used in the production of various chemicals, including \n\
urea-formaldehyde resins and adhesives, which are utilized in \n\
manufacturing particleboard, plywood,and other composite \n\
wood products.\n\
Pharmaceuticals: \n\
Urea is an ingredient in certain pharmaceutical formulations, including \n\
dermatological creams and ointments, where it acts as a keratolytic agent to \n\
treat skin conditions such as dry skin, psoriasis, and eczema.\n\
Animal Feed: Urea is added to animal feed as a non-protein nitrogen source, \n\
aiding in the nutritional supplementation for ruminant animals like cattle and \n\
sheep, which can convert urea into protein through microbial action in \n\
their stomachs.\n\
Automotive Industry: \n\
Urea is a key component in diesel exhaust fluid (DEF), used in selective \n\
catalytic reduction (SCR) systems to reduce nitrogen oxide emissions from \n\
diesel engines, helping vehicles meet stringent environmental regulations.")}
