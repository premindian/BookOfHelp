// Comprehensive Social Impact Initiatives Database
// Intelligently processed and deduplicated from comprehensive list

const initiativesData = [
    // EDUCATION INITIATIVES
    {
        title: "Textbook Exchange Network",
        description: "Revolutionary digital marketplace facilitating seamless distribution of used textbooks from senior students to juniors at school level. This comprehensive platform promotes educational resource sharing, significantly reduces educational costs for families, and supports environmental sustainability through systematic reuse initiatives. Features include quality verification, price negotiation, delivery coordination, and impact tracking.",
        category: "education",
        impact: "Reduces education costs by 60%",
        beneficiaries: "10M+ students",
        icon: "book"
    },
    {
        title: "Educational Sponsorship Network",
        description: "Comprehensive education funding platform connecting philanthropic sponsors with deserving children from economically disadvantaged backgrounds. Covers complete educational expenses including school fees, uniforms, books, technology, transportation, and nutritional support with transparent tracking systems and donor recognition programs.",
        category: "education",
        impact: "Universal education access",
        beneficiaries: "50M+ children",
        icon: "graduation-cap"
    },
    {
        title: "School Infrastructure Upgrade",
        description: "Educational infrastructure platform upgrading poor village schools with modern buildings, equipped classrooms, science laboratories, libraries, computer labs, sanitation facilities, and comprehensive infrastructure to create optimal learning environments for quality education delivery.",
        category: "education",
        impact: "Enhanced learning environments",
        beneficiaries: "100M+ students",
        icon: "school"
    },
    {
        title: "Digital Learning Enhancement",
        description: "Education technology platform providing poor school children with comprehensive digital learning kits including educational tablets, e-learning applications, internet access, and digital literacy training for enhanced educational outcomes and future technological readiness.",
        category: "education",
        impact: "Enhanced digital learning",
        beneficiaries: "200M+ students",
        icon: "tablet-alt"
    },
    {
        title: "Rural Digital Knowledge Network",
        description: "Comprehensive educational platform mobilizing unused books, refurbished laptops, tablets, and digital resources from urban areas to establish well-equipped community libraries and learning centers in poor villages for knowledge democratization.",
        category: "education",
        impact: "Rural knowledge access",
        beneficiaries: "100M+ rural learners",
        icon: "wifi"
    },
    {
        title: "Street Children Education Initiative",
        description: "Child welfare platform connecting children found in street situations with volunteer teachers, donors, and comprehensive rehabilitation services including schooling, nutrition, healthcare, uniforms, and family reunification or alternative care arrangements.",
        category: "education",
        impact: "Street children education",
        beneficiaries: "20M+ street children",
        icon: "child"
    },
    {
        title: "Girls Education Empowerment",
        description: "Gender equality platform specifically empowering girls in poor neighborhoods through comprehensive education support, scholarships, mentoring programs, safety measures, leadership training, and advocacy for equal educational opportunities and social advancement.",
        category: "education",
        impact: "Gender equality in education",
        beneficiaries: "100M+ girls",
        icon: "female"
    },
    {
        title: "Higher Education Scholarship Program",
        description: "Educational advancement platform providing comprehensive scholarships for academically excellent students from economically disadvantaged backgrounds. Covers tuition, accommodation, books, living expenses, technology, and mentoring for university and professional courses.",
        category: "education",
        impact: "Higher education access",
        beneficiaries: "25M+ students",
        icon: "university"
    },
    {
        title: "Education Recovery Program",
        description: "Student retention platform encouraging school dropouts to return through comprehensive scholarships, free educational materials, uniforms, nutritional support, counseling services, and addressing root causes of educational abandonment through holistic family support.",
        category: "education",
        impact: "Education retention and recovery",
        beneficiaries: "10M+ students",
        icon: "undo"
    },
    {
        title: "Experiential Learning Tours",
        description: "Educational enrichment platform sponsoring educational picnics, science museum visits, cultural tours, and field trips for village school children, providing hands-on learning experiences, exposure to scientific institutions, and cultural broadening opportunities.",
        category: "education",
        impact: "Experiential learning access",
        beneficiaries: "25M+ students",
        icon: "bus"
    },
    {
        title: "Educational Transportation Support",
        description: "School access platform sponsoring bicycles, transportation vouchers, and safe transit solutions for poor school-going children in rural areas, significantly reducing dropout rates caused by distance barriers and ensuring consistent educational attendance.",
        category: "education",
        impact: "Reduced education dropouts",
        beneficiaries: "25M+ students",
        icon: "bicycle"
    },
    {
        title: "Community Knowledge Centers",
        description: "Educational infrastructure platform building and supporting community libraries with technology resources, internet access, digital literacy programs, and comprehensive book collections for poor neighborhoods, promoting lifelong learning and knowledge access.",
        category: "education",
        impact: "Community knowledge access",
        beneficiaries: "50M+ learners",
        icon: "book-open"
    },
    {
        title: "Free Textbook Sharing Network",
        description: "Educational resource platform where students donate used textbooks to juniors, matching donors with poor students in need, ensuring comprehensive textbook access for all students regardless of economic background.",
        category: "education",
        impact: "Free textbook access",
        beneficiaries: "100M+ students",
        icon: "share-alt"
    },
    {
        title: "Free Tuition Bank",
        description: "Educational support platform connecting poor students with volunteer tutors including college students and professionals, providing free academic coaching and personalized learning support across various subjects and skill levels.",
        category: "education",
        impact: "Free academic support",
        beneficiaries: "50M+ students",
        icon: "chalkboard-teacher"
    },
    {
        title: "Free Exam Coaching Corners",
        description: "Educational enhancement platform establishing exam preparation centers in slum libraries and community spaces for government job aspirants, providing free coaching, study materials, and guidance for competitive examinations.",
        category: "education",
        impact: "Competitive exam success",
        beneficiaries: "10M+ aspirants",
        icon: "clipboard-check"
    },
    {
        title: "Solar Study Lamps Distribution",
        description: "Educational support platform distributing low-cost solar lamps to children in villages without electricity, enabling night-time studying and improving educational outcomes in off-grid communities through sustainable lighting solutions.",
        category: "education",
        impact: "Night study access",
        beneficiaries: "50M+ students",
        icon: "lightbulb"
    },
    {
        title: "School Uniform Distribution",
        description: "Educational support platform coordinating distribution of quality school uniforms to children from poor neighborhoods, ensuring dignified school attendance, reducing stigma, removing economic barriers to education, and improving enrollment rates.",
        category: "education",
        impact: "Dignified education access",
        beneficiaries: "50M+ students",
        icon: "tshirt"
    },

    // HEALTHCARE INITIATIVES
    {
        title: "Academic Stress Management Hub",
        description: "Specialized mental health platform designed for intermediate college students facing severe stress while preparing for engineering and medicine entrance exams. Provides evidence-based stress reduction techniques, peer counseling, academic pressure management, and comprehensive wellness support.",
        category: "healthcare",
        impact: "85% stress reduction in students",
        beneficiaries: "5M+ students",
        icon: "brain"
    },
    {
        title: "Real-Time Medication Tracker",
        description: "Advanced crowdsourced platform enabling users to log and track side effects from medications in real-time. Creates comprehensive database for healthcare providers and patients to make informed treatment decisions and improve drug safety protocols.",
        category: "healthcare",
        impact: "Improved medication safety",
        beneficiaries: "100M+ patients",
        icon: "pills"
    },
    {
        title: "Life-Saving Blood Network",
        description: "Comprehensive blood donation and distribution platform connecting verified blood banks with patients in critical need. Features real-time inventory tracking, donor recognition systems, emergency alerts, blood type matching, and efficient distribution logistics.",
        category: "healthcare",
        impact: "Lives saved daily",
        beneficiaries: "50M+ patients",
        icon: "heartbeat"
    },
    {
        title: "Disease Prevention Network",
        description: "Public health platform distributing mosquito nets, conducting health education, and implementing vector control measures in poor neighborhoods. Prevents vector-borne diseases like malaria, dengue, and chikungunya while improving overall family health.",
        category: "healthcare",
        impact: "Disease prevention coverage",
        beneficiaries: "100M+ people",
        icon: "shield-alt"
    },
    {
        title: "Vision Care Access Program",
        description: "Comprehensive eye health platform organizing mobile eye testing camps, providing free spectacles, conducting cataract surgeries, and ensuring vision correction access for poor communities with early detection of eye diseases.",
        category: "healthcare",
        impact: "Improved vision access",
        beneficiaries: "50M+ people",
        icon: "eye"
    },
    {
        title: "Oral Health Equity Initiative",
        description: "Dental healthcare platform providing free checkups, cleanings, preventive treatments, and basic dental procedures to economically disadvantaged families, preventing serious dental diseases and improving overall health outcomes.",
        category: "healthcare",
        impact: "Oral health for all",
        beneficiaries: "200M+ people",
        icon: "tooth"
    },
    {
        title: "Mobility Independence Program",
        description: "Comprehensive disability support platform providing free motorized and manual wheelchairs, mobility aids, physical therapy, and accessibility modifications to handicapped individuals from poor families, ensuring independence and dignity.",
        category: "healthcare",
        impact: "Mobility independence",
        beneficiaries: "5M+ individuals",
        icon: "wheelchair"
    },
    {
        title: "Hearing Accessibility Network",
        description: "Hearing healthcare platform connecting sponsors with individuals experiencing hearing loss, providing hearing aids, cochlear implants, audiological testing, speech therapy, and ongoing support for comprehensive communication accessibility.",
        category: "healthcare",
        impact: "Communication accessibility",
        beneficiaries: "10M+ individuals",
        icon: "deaf"
    },
    {
        title: "Life-Changing Surgery Program",
        description: "Medical intervention platform connecting children born with cleft conditions to surgical sponsors, covering complete treatment costs including surgery, rehabilitation, speech therapy, dental care, and long-term follow-up care.",
        category: "healthcare",
        impact: "Life-changing surgeries",
        beneficiaries: "100K+ children",
        icon: "user-md"
    },
    {
        title: "Healthcare Crisis Support Fund",
        description: "Emergency financial assistance platform rapidly mobilizing community donations for patient caretakers, covering critical expenses including medical procedures, emergency treatments, and essential support equipment for affected families.",
        category: "healthcare",
        impact: "Crisis support coverage",
        beneficiaries: "10M+ families",
        icon: "ambulance"
    },
    {
        title: "Accident Recovery Assistance",
        description: "Medical support platform helping poor families overcome financial burden and recovery challenges following accidents. Provides medical cost coverage, rehabilitation resources, income replacement, and comprehensive recovery planning assistance.",
        category: "healthcare",
        impact: "Accident recovery support",
        beneficiaries: "2M+ families",
        icon: "band-aid"
    },
    {
        title: "Autism Family Support Hub",
        description: "Specialized platform providing comprehensive support to families affected by autism, including therapy resources, educational materials, respite care, behavior intervention, communication aids, and community support networks.",
        category: "healthcare",
        impact: "Autism family empowerment",
        beneficiaries: "5M+ families",
        icon: "puzzle-piece"
    },
    {
        title: "Cardiac Surgery Access",
        description: "Life-saving medical platform connecting donors with hospitals to fund comprehensive heart operations, cardiac procedures, post-surgery care, and rehabilitation for poor patients, ensuring access to critical cardiac interventions.",
        category: "healthcare",
        impact: "Life-saving cardiac care",
        beneficiaries: "2M+ cardiac patients",
        icon: "heartbeat"
    },
    {
        title: "Kidney Disease Support",
        description: "Renal healthcare platform connecting donors with poor patients requiring kidney transplants, dialysis, and renal care, covering surgery costs, medications, post-transplant care, and long-term medical support.",
        category: "healthcare",
        impact: "Life-saving renal care",
        beneficiaries: "1M+ renal patients",
        icon: "hospital"
    },
    {
        title: "Comprehensive Cancer Care",
        description: "Oncology support platform providing complete cancer treatment funding including chemotherapy, radiation therapy, surgery, medications, palliative care, and family support services through donor contributions and medical partnerships.",
        category: "healthcare",
        impact: "Cancer care accessibility",
        beneficiaries: "5M+ cancer patients",
        icon: "ribbon"
    },
    {
        title: "Prosthetic Rehabilitation Program",
        description: "Medical device platform funding prosthetic limbs, artificial hands, mobility devices, and rehabilitation services for amputees from poor families, restoring functionality, independence, and dignity.",
        category: "healthcare",
        impact: "Restored functionality",
        beneficiaries: "2M+ individuals",
        icon: "hand-paper"
    },
    {
        title: "Burn Victim Rehabilitation",
        description: "Medical care platform tracking poor patients who suffer burns, connecting them with donors to fund surgeries, skin grafts, rehabilitation therapy, and long-term recovery support for comprehensive healing.",
        category: "healthcare",
        impact: "Burn recovery support",
        beneficiaries: "500K+ burn victims",
        icon: "first-aid"
    },
    {
        title: "Infant Care Support Program",
        description: "Child health platform distributing quality diapers, baby care products, hygiene supplies, and parenting resources to economically disadvantaged parents with newborns and toddlers, ensuring infant health and comfort.",
        category: "healthcare",
        impact: "Infant health and comfort",
        beneficiaries: "50M+ infants",
        icon: "baby"
    },
    {
        title: "Rural Mobile Healthcare",
        description: "Healthcare access platform sponsoring regular doctor and nurse visits to underserved villages, providing medical expertise, preventive care, health screenings, treatment services, and medication distribution.",
        category: "healthcare",
        impact: "Rural medical access",
        beneficiaries: "100M+ rural residents",
        icon: "user-md"
    },
    {
        title: "Emergency Medical Response",
        description: "Healthcare emergency platform procuring, maintaining, and operating ambulances with trained drivers and medical equipment for poor neighborhoods, ensuring rapid emergency medical response and transport services.",
        category: "healthcare",
        impact: "Emergency medical access",
        beneficiaries: "200M+ residents",
        icon: "ambulance"
    },
    {
        title: "Community Fitness Revolution",
        description: "Public health platform installing comprehensive open-air gyms, exercise equipment, fitness programs, and wellness activities in poor neighborhoods through donor sponsorship, promoting community health and fitness.",
        category: "healthcare",
        impact: "Community fitness and health",
        beneficiaries: "500M+ residents",
        icon: "dumbbell"
    },
    {
        title: "Farmer Mental Health Initiative",
        description: "Agricultural welfare platform preventing farmer suicides through comprehensive mental health counseling, crisis intervention, emergency financial aid, government scheme connections, and holistic support for agricultural crises.",
        category: "healthcare",
        impact: "Farmer life preservation",
        beneficiaries: "25M+ farmers",
        icon: "heart"
    },
    {
        title: "Rural Emergency Transport",
        description: "Emergency healthcare platform tracking remote villages where ambulances rarely reach, enabling donors to fund specially equipped small vehicles and motorbikes for patient transport to medical facilities.",
        category: "healthcare",
        impact: "Rural emergency medical access",
        beneficiaries: "200M+ rural residents",
        icon: "motorcycle"
    },
    {
        title: "Hospital Infrastructure Upgrade",
        description: "Healthcare infrastructure platform funding comprehensive ICU improvements in government hospitals, providing modern medical equipment, patient cots, electrical systems, and advanced care facilities.",
        category: "healthcare",
        impact: "Enhanced hospital care",
        beneficiaries: "100M+ patients",
        icon: "hospital"
    },
    {
        title: "Supplemental Healthcare Fund",
        description: "Healthcare financing platform providing additional medical funding to poor families beyond government aid, covering emergency treatments, specialized procedures, medications, and comprehensive care.",
        category: "healthcare",
        impact: "Comprehensive medical coverage",
        beneficiaries: "500M+ patients",
        icon: "medical-kit"
    },
    {
        title: "Medicine Redistribution Network",
        description: "Healthcare resource platform systematically collecting unused but non-expired medicines from households, pharmacies, and hospitals, safely redistributing them to poor patients through verified NGOs.",
        category: "healthcare",
        impact: "Medicine accessibility",
        beneficiaries: "1B+ patients",
        icon: "pills"
    },

    // EMPLOYMENT INITIATIVES
    {
        title: "Daily Wage Worker Digital Platform",
        description: "Comprehensive digital ecosystem connecting daily wage workers with task providers across towns and villages, ensuring fairness in wages, transparency in job allocation, and mutual respect through dignified employment networks.",
        category: "employment",
        impact: "Fair wages guaranteed for all",
        beneficiaries: "50M+ workers",
        icon: "hard-hat"
    },
    {
        title: "Street Vendor Quarterly Support",
        description: "Community-driven empowerment program connecting generous donors with street cart vendors, providing quarterly financial assistance, equipment upgrades, hygiene training, and business development support.",
        category: "employment",
        impact: "Quarterly income stability",
        beneficiaries: "5M+ vendors",
        icon: "shopping-cart"
    },
    {
        title: "Auto Driver Welfare Network",
        description: "Community-driven support system providing quarterly financial assistance, vehicle maintenance support, insurance coverage, fuel subsidies, and essential resources to auto-rickshaw drivers from willing donors.",
        category: "employment",
        impact: "Driver family welfare improvement",
        beneficiaries: "2M+ drivers",
        icon: "car"
    },
    {
        title: "Cobbler Business Development Program",
        description: "Comprehensive business transformation platform supporting roadside cobblers in transitioning from temporary setups to permanent small shops with microfinance, location assistance, and business training.",
        category: "employment",
        impact: "Permanent business establishment",
        beneficiaries: "500K+ cobblers",
        icon: "hammer"
    },
    {
        title: "Sustainable Skills Training Program",
        description: "Comprehensive vocational training platform providing 6-month sewing machine operation courses, equipment donation, and business development support to unemployed individuals for sustainable income opportunities.",
        category: "employment",
        impact: "Sustainable skill development",
        beneficiaries: "10M+ trainees",
        icon: "cut"
    },
    {
        title: "Entrepreneurship Equipment Financing",
        description: "Microfinance platform providing push carts, mobile vending equipment, inventory support, and business training to aspiring entrepreneurs, enabling small business creation and economic independence.",
        category: "employment",
        impact: "New business creation",
        beneficiaries: "5M+ entrepreneurs",
        icon: "shopping-cart"
    },
    {
        title: "Fishermen Livelihood Security",
        description: "Seasonal employment platform providing basic living funds, equipment maintenance, boat repairs, and family support to poor fishermen during off-fishing seasons, ensuring year-round income security.",
        category: "employment",
        impact: "Year-round income stability",
        beneficiaries: "3M+ fishermen",
        icon: "fish"
    },
    {
        title: "Traditional Craft Preservation",
        description: "Cultural heritage platform supporting manual handloom weavers with raw materials, modern tools, design innovation, market access, and sustainable income opportunities while preserving traditional textile crafts.",
        category: "employment",
        impact: "Traditional craft preservation",
        beneficiaries: "2M+ artisans",
        icon: "palette"
    },
    {
        title: "Green Employment Initiative",
        description: "Environmental employment platform providing paid opportunities for unemployed youth to clean and beautify poor neighborhoods, creating immediate income while improving community hygiene and environmental conditions.",
        category: "employment",
        impact: "Clean communities + jobs",
        beneficiaries: "10M+ youth",
        icon: "broom"
    },
    {
        title: "Urban Migration Support",
        description: "Employment mobility platform supporting unemployed rural youth with comprehensive 3-month stipends, accommodation assistance, job placement services, and urban adaptation support for city employment.",
        category: "employment",
        impact: "Urban employment opportunities",
        beneficiaries: "5M+ rural youth",
        icon: "city"
    },
    {
        title: "Local Employment Matching",
        description: "Job placement platform organizing comprehensive job fairs, career guidance, skills assessment, employer networking, and immediate employment opportunities for residents of economically disadvantaged neighborhoods.",
        category: "employment",
        impact: "Local employment connections",
        beneficiaries: "25M+ job seekers",
        icon: "handshake"
    },
    {
        title: "Civic Employment Network",
        description: "National development platform supporting youth from poor neighborhoods with meaningful employment in infrastructure development, environmental conservation, education support, and community development sectors.",
        category: "employment",
        impact: "Meaningful civic employment",
        beneficiaries: "15M+ youth",
        icon: "flag"
    },
    {
        title: "Global Artisan Marketplace",
        description: "Economic empowerment platform connecting rural artisans specializing in pottery, bamboo crafts, textiles, and handmade products with city and international buyers, creating sustainable income streams.",
        category: "employment",
        impact: "Global market access",
        beneficiaries: "10M+ artisans",
        icon: "globe"
    },
    {
        title: "Inclusive Employment Platform",
        description: "Comprehensive disability employment platform listing specialized job opportunities designed for physically challenged and visually impaired individuals, with donor-sponsored assistive devices and workplace accommodations.",
        category: "employment",
        impact: "Inclusive employment opportunities",
        beneficiaries: "25M+ disabled individuals",
        icon: "universal-access"
    },
    {
        title: "Multi-Skill Development Center",
        description: "Comprehensive vocational platform providing diverse skill training including plumbing, electrical work, tailoring, mobile repair, computer skills, and AI-based technologies for unemployed youth.",
        category: "employment",
        impact: "Multiple skill development",
        beneficiaries: "50M+ trainees",
        icon: "tools"
    },
    {
        title: "Skills-to-Employment Bridge",
        description: "Employment acceleration platform matching poor unemployed youth with free comprehensive skill workshops in carpentry, tailoring, mobile repair, coding, and emerging technologies for immediate employability.",
        category: "employment",
        impact: "Immediate employability",
        beneficiaries: "100M+ unemployed youth",
        icon: "bridge"
    },
    {
        title: "Migrant Worker Protection",
        description: "Labor rights platform helping stranded or exploited migrant workers connect with help desks for shelter, wage recovery, travel assistance, food support, and legal protection services.",
        category: "employment",
        impact: "Migrant worker protection",
        beneficiaries: "50M+ migrant workers",
        icon: "shield-alt"
    },

    // HOUSING INITIATIVES
    {
        title: "Housing Rehabilitation Initiative",
        description: "Home improvement platform supporting repair, renovation, and reconstruction of substandard housing in economically disadvantaged communities, providing materials, labor coordination, and technical guidance for safe living.",
        category: "housing",
        impact: "Safe housing conditions",
        beneficiaries: "50M+ households",
        icon: "home"
    },
    {
        title: "Housing Upgrade Initiative",
        description: "Housing transformation platform facilitating systematic relocation of families from slums and unsafe areas to improved housing through government and private partnerships, ensuring dignified living conditions.",
        category: "housing",
        impact: "Dignified housing transitions",
        beneficiaries: "100M+ families",
        icon: "building"
    },
    {
        title: "Widow Housing Initiative",
        description: "Housing platform building small donor-funded homes specifically for abandoned or homeless widows, providing safe, dignified shelter and community support for vulnerable women in need of secure accommodation.",
        category: "housing",
        impact: "Widow housing security",
        beneficiaries: "5M+ widows",
        icon: "home"
    },
    {
        title: "Affordable Housing Support",
        description: "Housing development platform connecting donors and NGOs with poor families to fund permanent low-cost houses, ensuring dignified shelter solutions and community development through sustainable housing initiatives.",
        category: "housing",
        impact: "Permanent housing solutions",
        beneficiaries: "200M+ families",
        icon: "building"
    },
    {
        title: "Emergency Shelter Network",
        description: "Crisis housing platform providing immediate shelter solutions for homeless families during emergencies, natural disasters, and crisis situations, ensuring basic human dignity and safety for vulnerable populations.",
        category: "housing",
        impact: "Emergency housing security",
        beneficiaries: "50M+ homeless individuals",
        icon: "home"
    },

    // SOCIAL SUPPORT INITIATIVES
    {
        title: "Inclusive Wedding Support Network",
        description: "Comprehensive matrimonial assistance platform providing support to physically disabled and economically disadvantaged couples for dignified wedding ceremonies, including venue arrangements and accessibility accommodations.",
        category: "social",
        impact: "Dignified celebrations for all",
        beneficiaries: "1M+ couples",
        icon: "heart"
    },
    {
        title: "Sustainable Toy Redistribution Network",
        description: "Environmental and social impact platform collecting, sanitizing, and redistributing quality used toys from affluent families to disadvantaged children, promoting environmental consciousness and childhood development.",
        category: "social",
        impact: "Childhood joy access",
        beneficiaries: "100M+ children",
        icon: "puzzle-piece"
    },
    {
        title: "Community Clothing Exchange Hub",
        description: "Systematic clothing redistribution network using strategically placed smart drop boxes to collect, sort, and distribute quality used clothing from donors to families in need with seasonal coordination.",
        category: "social",
        impact: "Clothing security for all",
        beneficiaries: "500M+ individuals",
        icon: "tshirt"
    },
    {
        title: "NGO Impact Accountability Hub",
        description: "Comprehensive accountability platform tracking, ranking, and evaluating NGOs based on donation transparency, measurable impact metrics, community benefit delivery, and operational efficiency for improved outcomes.",
        category: "social",
        impact: "Enhanced NGO accountability",
        beneficiaries: "Global communities",
        icon: "chart-line"
    },
    {
        title: "Democratic Engagement Platform",
        description: "Advanced civic participation platform enabling citizens to raise local infrastructure, governance, and community issues directly to elected representatives through structured ticketing system for responsive governance.",
        category: "social",
        impact: "Enhanced democratic participation",
        beneficiaries: "1B+ citizens",
        icon: "vote-yea"
    },
    {
        title: "Comprehensive Orphan Care System",
        description: "Holistic support platform for children who have lost parents, coordinating foster care, educational support, healthcare coverage, emotional counseling, and life preparation services with transparent donor tracking.",
        category: "social",
        impact: "Complete child development",
        beneficiaries: "25M+ orphans",
        icon: "child"
    },
    {
        title: "Rural Infrastructure Development Hub",
        description: "Community infrastructure platform systematically documenting rural road conditions, coordinating repair activities, and tracking progress to ensure safe transportation connectivity and rural development.",
        category: "social",
        impact: "Enhanced rural connectivity",
        beneficiaries: "500K+ villages",
        icon: "road"
    },
    {
        title: "Community Energy Access Program",
        description: "Energy security initiative enabling wealthy donors to collectively sponsor electricity bills for poor communities, ensuring consistent power access for households, schools, and healthcare facilities.",
        category: "social",
        impact: "Reliable electricity access",
        beneficiaries: "200M+ households",
        icon: "bolt"
    },
    {
        title: "Cultural Experience Initiative",
        description: "Recreation and education platform organizing lottery-based holiday adventure trips for children from economically disadvantaged backgrounds, providing educational travel experiences and cultural exposure.",
        category: "social",
        impact: "Memorable life experiences",
        beneficiaries: "10M+ children",
        icon: "plane"
    },
    {
        title: "Youth Athletic Development Network",
        description: "Sports empowerment platform providing sporting equipment, shoes, training gear, coaching support, and recreational facilities to underprivileged village youth for holistic development.",
        category: "social",
        impact: "Youth holistic development",
        beneficiaries: "100M+ youth",
        icon: "running"
    },
    {
        title: "Rural Youth Sports Development",
        description: "Athletic empowerment platform sponsoring comprehensive sports equipment, coaching, facilities, and competitive opportunities for rural children, promoting physical fitness and team building.",
        category: "social",
        impact: "Rural youth engagement",
        beneficiaries: "50M+ rural youth",
        icon: "futbol"
    },
    {
        title: "Family Crisis Support Network",
        description: "Emergency assistance platform providing comprehensive support to families who lose their primary income earner, including immediate financial aid, job placement services, and emotional counseling.",
        category: "social",
        impact: "Family crisis recovery",
        beneficiaries: "10M+ families",
        icon: "hands-helping"
    },
    {
        title: "Philanthropic Coordination Network",
        description: "Comprehensive platform supporting various charitable organizations through transparency tools, impact measurement, donation coordination, and healthy competition systems for efficient philanthropy.",
        category: "social",
        impact: "Coordinated philanthropy",
        beneficiaries: "Global communities",
        icon: "network-wired"
    },
    {
        title: "Justice Accessibility Platform",
        description: "Legal aid platform providing free legal support, representation, and advocacy to disadvantaged individuals facing property disputes, labor rights violations, domestic violence, and discrimination.",
        category: "social",
        impact: "Justice accessibility",
        beneficiaries: "500M+ people",
        icon: "balance-scale"
    },
    {
        title: "Dignified Funeral Support",
        description: "End-of-life dignity platform providing financial assistance to poor families facing unexpected funeral costs, ensuring respectful last rites and cultural ceremony support regardless of economic circumstances.",
        category: "social",
        impact: "Dignified final rites",
        beneficiaries: "25M+ families",
        icon: "praying-hands"
    },
    {
        title: "Community Space Development",
        description: "Public amenity platform installing benches, gazebos, and community gathering spaces in parks within poor neighborhoods, creating social interaction hubs and strengthening community bonds.",
        category: "social",
        impact: "Community gathering spaces",
        beneficiaries: "1B+ residents",
        icon: "users"
    },
    {
        title: "Community Safety Lighting",
        description: "Safety infrastructure platform funding comprehensive solar and electric street lighting systems in poorly lit neighborhoods, improving community safety and enabling evening economic activities.",
        category: "social",
        impact: "Enhanced community safety",
        beneficiaries: "500M+ residents",
        icon: "lightbulb"
    },
    {
        title: "Disability Support Network",
        description: "Disability assistance platform providing random financial support, medical aid, assistive devices, and comprehensive services to poor disabled individuals for improved quality of life.",
        category: "social",
        impact: "Comprehensive disability support",
        beneficiaries: "100M+ disabled individuals",
        icon: "wheelchair"
    },
    {
        title: "Youth Sports Competition Network",
        description: "Athletic development platform sponsoring competitive sports events, tournaments, and athletic competitions between schools in poor neighborhoods, promoting healthy competition and talent recognition.",
        category: "social",
        impact: "Youth talent development",
        beneficiaries: "200M+ young athletes",
        icon: "trophy"
    },
    {
        title: "Community Wellness Recreation",
        description: "Social wellness platform sponsoring group recreational trips and activities for residents of poor neighborhoods, providing mental health benefits, community bonding, and stress relief.",
        category: "social",
        impact: "Community mental wellness",
        beneficiaries: "100M+ community members",
        icon: "hiking"
    },
    {
        title: "Climate Relief Support",
        description: "Weather assistance platform providing cooling equipment, fans, and heat relief supplies to poor households with disabled or elderly members, ensuring comfort and preventing heat-related emergencies.",
        category: "social",
        impact: "Climate comfort and health",
        beneficiaries: "50M+ vulnerable individuals",
        icon: "thermometer-half"
    },
    {
        title: "Orphan Childhood Joy Initiative",
        description: "Child welfare platform organizing meaningful birthday celebrations for orphaned children, providing cakes, gifts, party supplies, and emotional support from volunteers and sponsors.",
        category: "social",
        impact: "Childhood celebration and joy",
        beneficiaries: "25M+ orphan children",
        icon: "birthday-cake"
    },
    {
        title: "Vendor Childcare Centers",
        description: "Family support platform creating safe donor-supported daycare centers where street vendors and daily wage laborers can leave their children while working, ensuring child safety.",
        category: "social",
        impact: "Working parent support",
        beneficiaries: "50M+ working parents",
        icon: "baby"
    },
    {
        title: "Elderly Financial Security",
        description: "Senior care platform enabling wealthy donors to 'adopt' elderly poor individuals living without family support, supplementing inadequate government pensions with additional monthly contributions.",
        category: "social",
        impact: "Elderly financial security",
        beneficiaries: "200M+ elderly people",
        icon: "user-friends"
    },
    {
        title: "Widow Empowerment Program",
        description: "Women's welfare platform providing comprehensive support to widows in poor neighborhoods including monthly pensions, vocational training, emotional support groups, and community integration.",
        category: "social",
        impact: "Widow empowerment and rehabilitation",
        beneficiaries: "100M+ widows",
        icon: "female"
    },
    {
        title: "Child Protection and Rehabilitation",
        description: "Child welfare platform comprehensively uplifting child laborers through rescue operations, rehabilitation services, educational enrollment, family economic support, and long-term monitoring.",
        category: "social",
        impact: "Child protection and development",
        beneficiaries: "200M+ children",
        icon: "shield-alt"
    },
    {
        title: "Farmer Widow Support System",
        description: "Specialized welfare platform systematically tracking and supporting widows of farmers who died by suicide, connecting them with donors for monthly sustenance and children's education funding.",
        category: "social",
        impact: "Farmer widow comprehensive care",
        beneficiaries: "25M+ farmer widows",
        icon: "heart"
    },
    {
        title: "Tribal Community Support",
        description: "Cultural preservation platform connecting tribal communities with donors for education, healthcare, clothing, and food support while ensuring cultural sensitivity and preventing exploitation.",
        category: "social",
        impact: "Tribal community support",
        beneficiaries: "100M+ tribal members",
        icon: "users"
    },

    // FOOD & NUTRITION INITIATIVES
    {
        title: "Zero-Waste Food Distribution",
        description: "Comprehensive food waste reduction platform connecting retailers, restaurants, and vendors with surplus fresh produce to orphanages, homeless shelters, and food-insecure families for community nutrition.",
        category: "food",
        impact: "70% waste reduction",
        beneficiaries: "500M+ people",
        icon: "apple-alt"
    },
    {
        title: "Mobile Nutrition Distribution",
        description: "Food security platform establishing comprehensive mobile food delivery services for homeless and underprivileged individuals in areas lacking government food programs, ensuring regular nutritious meal access.",
        category: "food",
        impact: "Regular nutrition access",
        beneficiaries: "100M+ people",
        icon: "truck"
    },
    {
        title: "Community Food Kitchens",
        description: "Nutrition platform establishing community-run kitchens providing free or subsidized daily meals for the poorest sections, funded by donors and managed by local volunteers for sustainable food security.",
        category: "food",
        impact: "Daily nutrition security",
        beneficiaries: "200M+ people",
        icon: "utensils"
    },
    {
        title: "Child Nutrition Programs",
        description: "Specialized nutrition platform ensuring poor children receive daily milk, eggs, fortified foods, and essential nutrients through donor sponsorship, combating malnutrition and supporting healthy development.",
        category: "food",
        impact: "Child malnutrition elimination",
        beneficiaries: "500M+ children",
        icon: "baby"
    },
    {
        title: "School Meal Enhancement",
        description: "Educational nutrition platform providing fortified mid-day meals with added vitamins and minerals for children in underprivileged schools, ensuring nutritious food supports learning and development.",
        category: "food",
        impact: "Enhanced school nutrition",
        beneficiaries: "200M+ students",
        icon: "school"
    },
    {
        title: "Emergency Food Relief",
        description: "Crisis nutrition platform supplying one-month essential grocery packages to families affected by natural disasters, ensuring immediate food security during crisis recovery periods.",
        category: "food",
        impact: "Disaster nutrition support",
        beneficiaries: "100M+ disaster victims",
        icon: "box"
    },

    // WATER & SANITATION INITIATIVES
    {
        title: "Universal Water Security Program",
        description: "Comprehensive water access platform coordinating safe drinking water distribution systems for underserved communities, including infrastructure development, quality monitoring, and sustainable maintenance programs.",
        category: "water",
        impact: "Clean water for all",
        beneficiaries: "1B+ people",
        icon: "tint"
    },
    {
        title: "Sanitation Infrastructure Development",
        description: "Community hygiene platform identifying areas requiring public toilet facilities and mobilizing funding from donors and government sources, improving community health, dignity, and safety.",
        category: "water",
        impact: "Improved sanitation access",
        beneficiaries: "500M+ people",
        icon: "restroom"
    },
    {
        title: "Clean Water Distribution Network",
        description: "Water security platform distributing advanced water filtration systems, purification tablets, and water quality monitoring to poor neighborhoods, ensuring access to safe drinking water.",
        category: "water",
        impact: "Safe drinking water access",
        beneficiaries: "2B+ people",
        icon: "tint"
    },
    {
        title: "Water Infrastructure Security",
        description: "Water access platform providing community water tanks, hand pumps, distribution systems, and maintenance training for underprivileged communities, ensuring reliable water access and health.",
        category: "water",
        impact: "Reliable water access",
        beneficiaries: "1B+ people",
        icon: "faucet"
    },
    {
        title: "Urban Sanitation Transformation",
        description: "Urban health platform systematically identifying slums lacking toilets, drainage, and clean water systems, enabling comprehensive sanitation solutions for community health improvement.",
        category: "water",
        impact: "Urban sanitation access",
        beneficiaries: "1B+ slum residents",
        icon: "shower"
    },
    {
        title: "Drought Crisis Management",
        description: "Water emergency platform managing real-time requests for drinking water in drought-affected villages, coordinating rapid deployment of water tankers and emergency supply systems.",
        category: "water",
        impact: "Drought crisis management",
        beneficiaries: "500M+ drought-affected people",
        icon: "sun"
    },
    {
        title: "Village Water Systems",
        description: "Rural water platform installing community-based rainwater harvesting, bore wells, and water treatment systems in villages, ensuring sustainable water access and management for rural communities.",
        category: "water",
        impact: "Rural water sustainability",
        beneficiaries: "500M+ villagers",
        icon: "tint"
    },

    // AGRICULTURE INITIATIVES
    {
        title: "Quality Seeds Distribution Chain",
        description: "Advanced agricultural supply chain platform ensuring distribution of certified high-quality seeds for paddy, groundnut, millets, and diverse crops to disadvantaged farmers with genetic purity verification.",
        category: "agriculture",
        impact: "40% increase in crop yield",
        beneficiaries: "100M+ farmers",
        icon: "seedling"
    },
    {
        title: "Smart Borewell Feasibility Analyzer",
        description: "AI-powered soil composition and geological analysis platform helping farmers assess optimal borewell drilling locations using satellite imagery, geological surveys, and predictive analytics.",
        category: "agriculture",
        impact: "80% drilling success rate",
        beneficiaries: "50M+ farmers",
        icon: "tint"
    },
    {
        title: "Comprehensive Agricultural Advisory",
        description: "Integrated farm management ecosystem providing soil health assessment, crop planning optimization, plant protection strategies, post-harvest technology guidance, and sustainable farming practices.",
        category: "agriculture",
        impact: "Holistic farm optimization",
        beneficiaries: "200M+ farmers",
        icon: "tractor"
    },
    {
        title: "Community Fertilizer Bank",
        description: "Innovative resource sharing platform creating community-managed fertilizer banks where surplus agricultural inputs are redistributed among farmers, promoting collaborative agriculture.",
        category: "agriculture",
        impact: "30% reduction in farming costs",
        beneficiaries: "150M+ farmers",
        icon: "leaf"
    },
    {
        title: "Agricultural Knowledge Transfer",
        description: "Farm education platform sponsoring agricultural experts and technology specialists to provide comprehensive training to poor farmers on modern techniques and sustainable practices.",
        category: "agriculture",
        impact: "Modern farming knowledge access",
        beneficiaries: "100M+ farmers",
        icon: "chalkboard-teacher"
    },
    {
        title: "Agricultural Crisis Prevention",
        description: "Farm emergency platform providing rapid financial aid, crop insurance, alternative livelihood support, and counseling services to farmers affected by natural disasters.",
        category: "agriculture",
        impact: "Farmer crisis prevention",
        beneficiaries: "200M+ farmers",
        icon: "leaf"
    },
    {
        title: "Farmers' Market Platform",
        description: "Agricultural commerce platform connecting small farmers directly with urban consumers, eliminating middlemen, ensuring fair prices, and providing fresh produce access to cities.",
        category: "agriculture",
        impact: "Fair pricing for farmers",
        beneficiaries: "500M+ farmers and consumers",
        icon: "store"
    },
    {
        title: "Crop Insurance Cooperative",
        description: "Agricultural protection platform providing affordable crop insurance through community-funded schemes, protecting small farmers from weather-related losses and financial devastation.",
        category: "agriculture",
        impact: "Financial protection for farmers",
        beneficiaries: "300M+ farmers",
        icon: "shield-alt"
    },
    {
        title: "Sustainable Farming Network",
        description: "Environmental agriculture platform promoting organic farming, permaculture, and sustainable agricultural practices while connecting eco-conscious farmers with premium markets.",
        category: "agriculture",
        impact: "Sustainable agriculture adoption",
        beneficiaries: "100M+ farmers",
        icon: "leaf"
    },

    // TECHNOLOGY INITIATIVES
    {
        title: "Senior Digital Connectivity",
        description: "Technology accessibility platform distributing smartphones with pre-installed health apps, communication tools, and government service access to elderly citizens for digital inclusion.",
        category: "technology",
        impact: "Digital inclusion for elderly",
        beneficiaries: "100M+ seniors",
        icon: "mobile-alt"
    },
    {
        title: "Solar Energy Access Initiative",
        description: "Renewable energy platform providing comprehensive solar lighting systems to villages without electricity access, enabling children to study after dark and supporting economic activities.",
        category: "technology",
        impact: "Energy access and productivity",
        beneficiaries: "500M+ rural residents",
        icon: "solar-panel"
    },
    {
        title: "Digital Skills Empowerment",
        description: "Technology access platform distributing refurbished laptops, tablets, and digital devices to educated unemployed youth in villages, enabling access to digital job opportunities.",
        category: "technology",
        impact: "Digital skill development",
        beneficiaries: "200M+ rural youth",
        icon: "laptop"
    },
    {
        title: "Poverty Innovation Fund",
        description: "Technology development platform funding individuals and teams working on innovative technical design and implementation of applications specifically focused on poverty alleviation.",
        category: "technology",
        impact: "Innovation for poverty alleviation",
        beneficiaries: "Global poor populations",
        icon: "lightbulb"
    },
    {
        title: "Rural Internet Infrastructure",
        description: "Digital connectivity platform establishing internet access points, Wi-Fi hotspots, and digital literacy centers in rural areas, bridging the digital divide for education and economic opportunities.",
        category: "technology",
        impact: "Rural digital connectivity",
        beneficiaries: "1B+ rural residents",
        icon: "wifi"
    },
    {
        title: "Mobile Technology Training",
        description: "Digital literacy platform providing comprehensive training on smartphones, internet usage, digital payments, and online services for elderly and rural populations.",
        category: "technology",
        impact: "Digital literacy enhancement",
        beneficiaries: "500M+ people",
        icon: "mobile-alt"
    },

    // ENVIRONMENT INITIATIVES
    {
        title: "Village Green Economy Initiative",
        description: "Environmental sustainability platform promoting plastic and paper recycling at village level with comprehensive reward systems, creating economic incentives for environmental protection.",
        category: "environment",
        impact: "Clean villages + income",
        beneficiaries: "100K+ villages",
        icon: "recycle"
    },
    {
        title: "Environmental Restoration Initiative",
        description: "Comprehensive tree planting and ecosystem restoration platform providing resources, funding, training, and coordination for large-scale environmental projects and climate change mitigation.",
        category: "environment",
        impact: "Environmental restoration",
        beneficiaries: "Global environment",
        icon: "tree"
    },
    {
        title: "Plastic-Free Community Program",
        description: "Environmental sustainability platform supporting economically disadvantaged communities in developing and distributing biodegradable alternatives to plastic bags for environmental protection.",
        category: "environment",
        impact: "Plastic pollution reduction",
        beneficiaries: "1B+ communities",
        icon: "leaf"
    },
    {
        title: "Clean Cooking Revolution",
        description: "Environmental health platform connecting poor households with energy-efficient cooking stoves and clean fuel solutions, reducing firewood consumption and indoor air pollution.",
        category: "environment",
        impact: "Clean cooking health",
        beneficiaries: "2B+ households",
        icon: "fire"
    },
    {
        title: "Community Environmental Management",
        description: "Environmental health platform installing comprehensive waste separation systems, recycling facilities, and environmental education in poor neighborhoods for sustainable practices.",
        category: "environment",
        impact: "Clean neighborhood environments",
        beneficiaries: "2B+ residents",
        icon: "trash-alt"
    },
    {
        title: "Carbon Footprint Reduction",
        description: "Climate action platform helping communities reduce carbon emissions through renewable energy adoption, sustainable transportation, and eco-friendly practices with carbon credit incentives.",
        category: "environment",
        impact: "Carbon emission reduction",
        beneficiaries: "Global population",
        icon: "leaf"
    },

    // FINANCIAL SERVICES INITIATIVES
    {
        title: "Transparent Donation Marketplace",
        description: "Revolutionary donation platform with gamified leaderboard system, impact verification, and transparent tracking connecting economically disadvantaged individuals with verified donors.",
        category: "finance",
        impact: "100% transparency",
        beneficiaries: "1B+ people",
        icon: "hand-holding-heart"
    },
    {
        title: "Micro Insurance Protection",
        description: "Financial protection platform providing simple, affordable insurance schemes covering health, accident, crop damage, and livelihood protection where donors cover premiums for ultra-poor families.",
        category: "finance",
        impact: "Financial protection for all",
        beneficiaries: "2B+ poor families",
        icon: "shield-alt"
    },
    {
        title: "Community Banking Network",
        description: "Financial inclusion platform establishing community-owned banks and credit unions in rural areas, providing savings accounts, microloans, and financial services to the unbanked poor.",
        category: "finance",
        impact: "Financial inclusion",
        beneficiaries: "1B+ unbanked people",
        icon: "university"
    },
    {
        title: "Microfinance Cooperatives",
        description: "Financial empowerment platform organizing self-help groups and microfinance cooperatives, providing small loans, savings programs, and financial literacy for economic development.",
        category: "finance",
        impact: "Economic empowerment",
        beneficiaries: "500M+ people",
        icon: "coins"
    },
    {
        title: "Digital Payment Training",
        description: "Financial technology platform teaching digital payment systems, mobile banking, and cashless transactions to street vendors and small business owners for economic modernization.",
        category: "finance",
        impact: "Digital financial literacy",
        beneficiaries: "200M+ vendors",
        icon: "credit-card"
    },
    {
        title: "Emergency Financial Aid",
        description: "Crisis financial platform providing immediate small loans and grants for medical emergencies, natural disasters, and urgent family needs with community-based verification.",
        category: "finance",
        impact: "Emergency financial security",
        beneficiaries: "1B+ families",
        icon: "hand-holding-usd"
    },

    // EMERGENCY AID INITIATIVES
    {
        title: "Weather Emergency Shelters",
        description: "Crisis response platform providing comprehensive emergency shelters for homeless individuals during extreme weather events including heat waves, floods, storms, and winter cold.",
        category: "emergency",
        impact: "Climate emergency protection",
        beneficiaries: "500M+ vulnerable people",
        icon: "home"
    },
    {
        title: "Disaster Recovery Food Support",
        description: "Emergency relief platform rapidly supplying comprehensive one-month essential grocery packages to families affected by natural disasters, ensuring immediate food security during recovery.",
        category: "emergency",
        impact: "Disaster recovery nutrition",
        beneficiaries: "200M+ disaster victims",
        icon: "box"
    },
    {
        title: "Flood Relief Coordination",
        description: "Disaster platform mapping poor families affected by seasonal floods, enabling donors to provide boats, temporary shelters, emergency kits, and coordinated flood response services.",
        category: "emergency",
        impact: "Flood emergency response",
        beneficiaries: "100M+ flood victims",
        icon: "water"
    },
    {
        title: "Homeless Winter Supplies",
        description: "Seasonal support platform distributing blankets, raincoats, and sleeping mats to homeless individuals during harsh weather conditions, providing basic protection and dignity.",
        category: "emergency",
        impact: "Weather protection",
        beneficiaries: "50M+ homeless people",
        icon: "home"
    },
    {
        title: "Emergency Medical Fund",
        description: "Healthcare crisis platform providing immediate financial assistance for medical emergencies, surgeries, and critical treatments for families unable to afford emergency healthcare.",
        category: "emergency",
        impact: "Emergency medical coverage",
        beneficiaries: "1B+ people",
        icon: "ambulance"
    },
    {
        title: "Natural Disaster Response",
        description: "Comprehensive disaster management platform coordinating immediate response, relief supplies, temporary housing, and long-term recovery support for communities affected by natural disasters.",
        category: "emergency",
        impact: "Comprehensive disaster response",
        beneficiaries: "500M+ disaster-prone people",
        icon: "exclamation-triangle"
    },

    // ADDITIONAL UNIQUE INITIATIVES FROM COMPREHENSIVE LIST
    {
        title: "Auto Driver Support Network", 
        description: "Community support system providing quarterly financial assistance and essential resources to auto-rickshaw drivers from willing donors, helping improve their economic stability and family welfare through organized donor matching.",
        category: "employment",
        impact: "Driver family support",
        beneficiaries: "5M+ drivers",
        icon: "car"
    },
    {
        title: "Used Toys Redistribution Network",
        description: "Child welfare platform redistributing used toys (ages 2–5 & 5–9) to disadvantaged children, ensuring quality toy access while promoting environmental sustainability through reuse and proper sanitization protocols.",
        category: "social", 
        impact: "Childhood development access",
        beneficiaries: "200M+ children",
        icon: "puzzle-piece"
    },
    {
        title: "Surplus Fruit Distribution Network",
        description: "Food waste reduction platform distributing surplus fruits from shops and street vendors to disadvantaged families, orphanages, and homeless shelters, ensuring nutritious food access while preventing wastage.",
        category: "food",
        impact: "Nutrition + waste reduction", 
        beneficiaries: "100M+ people",
        icon: "apple-alt"
    },
    {
        title: "Used Clothes Drop Box Network",
        description: "Systematic clothing redistribution platform tracking and distributing used clothes via strategically placed drop boxes, ensuring quality clothing reaches families in need through organized collection and distribution.",
        category: "social",
        impact: "Clothing accessibility",
        beneficiaries: "1B+ people", 
        icon: "tshirt"
    },
    {
        title: "Donation Request Platform",
        description: "Transparent platform enabling poor individuals to request financial assistance while allowing wealthy donors to contribute, featuring comprehensive leaderboards recognizing generous contributors and impact verification.",
        category: "finance",
        impact: "Transparent charitable giving",
        beneficiaries: "2B+ people",
        icon: "hand-holding-heart"
    },
    {
        title: "Ultra-Rich NGO Donation Tracker",
        description: "Accountability platform providing donation logging and leaderboard systems for ultra-rich NGOs, ensuring transparency in charitable giving and promoting competitive philanthropy for maximum social impact.",
        category: "social",
        impact: "NGO transparency enhancement",
        beneficiaries: "Global communities",
        icon: "chart-line"
    },
    {
        title: "Cobbler Permanent Shop Support",
        description: "Business development initiative supporting roadside cobblers in establishing permanent small shops, providing microfinance, location assistance, equipment upgrades, and business training for sustainable livelihoods.", 
        category: "employment",
        impact: "Permanent business establishment",
        beneficiaries: "2M+ cobblers",
        icon: "store"
    },
    {
        title: "Citizen Issue Ticketing System",
        description: "Democratic engagement platform enabling citizens to raise issues directly to MLAs, MLCs, and MPs through structured ticketing system, ensuring government accountability and responsive governance for community development.",
        category: "social", 
        impact: "Enhanced democracy participation",
        beneficiaries: "1.4B+ citizens",
        icon: "vote-yea"
    },
    {
        title: "Patient Caretaker Fund Mobilization",
        description: "Healthcare support platform mobilizing small funds for patient caretakers, covering memorial services, educational books, travel expenses, and sporting goods for families dealing with medical crises.",
        category: "healthcare",
        impact: "Healthcare family support",
        beneficiaries: "50M+ families", 
        icon: "heart"
    },
    {
        title: "Blood Donation Leaderboard Network",
        description: "Life-saving platform receiving donated blood from local banks while maintaining comprehensive leaderboards recognizing blood donors, ensuring efficient blood supply management and donor motivation.",
        category: "healthcare",
        impact: "Blood supply optimization",
        beneficiaries: "500M+ patients",
        icon: "tint"
    },
    {
        title: "Village Plastic Recycling Incentives",
        description: "Environmental platform implementing plastic and paper recycling at village level with incentive systems, creating economic opportunities while promoting environmental protection and waste management.",
        category: "environment",
        impact: "Environmental + economic benefits",
        beneficiaries: "500K+ villages",
        icon: "recycle"
    },
    {
        title: "Village Drinking Water Supply Design",
        description: "Water infrastructure platform designing and implementing safe drinking water supply systems for villages, ensuring sustainable water access through comprehensive planning and community management.",
        category: "water",
        impact: "Sustainable water access",
        beneficiaries: "1B+ villagers",
        icon: "tint"
    },
    {
        title: "Poor Children Education Sponsorship",
        description: "Educational funding platform connecting wealthy sponsors with poor children, featuring donor leaderboards and comprehensive support covering school fees, supplies, and educational needs.",
        category: "education",
        impact: "Education funding access",
        beneficiaries: "500M+ children",
        icon: "graduation-cap"
    },
    {
        title: "Public Toilet Funding Initiative",
        description: "Sanitation platform identifying places needing public toilets, mobilizing funds from wealthy donors, and featuring leaderboards recognizing contributors to improve community hygiene and dignity.",
        category: "water",
        impact: "Improved public sanitation",
        beneficiaries: "2B+ people",
        icon: "restroom"
    },
    {
        title: "Orphaned Children Support Network",
        description: "Comprehensive platform supporting young children who lost both parents, featuring donor leaderboards and providing housing, education, healthcare, and emotional support for complete child development.",
        category: "social",
        impact: "Orphan comprehensive care",
        beneficiaries: "100M+ orphans",
        icon: "child"
    },
    {
        title: "Push Cart Vendor Financing",
        description: "Microfinance platform mobilizing funds to purchase push carts for new vendors, featuring donor leaderboards and providing business training for sustainable entrepreneurship development.",
        category: "employment",
        impact: "New vendor business creation",
        beneficiaries: "10M+ vendors",
        icon: "shopping-cart"
    },
    {
        title: "Rural Road Pothole Tracking",
        description: "Infrastructure platform listing rural road potholes and tracking resolution progress, ensuring improved transportation connectivity and safety for rural communities through systematic monitoring.",
        category: "social", 
        impact: "Rural connectivity improvement",
        beneficiaries: "1B+ rural residents",
        icon: "road"
    },
    {
        title: "Community Electricity Bill Support",
        description: "Energy assistance platform enabling wealthy individuals to collectively pay electricity bills for poor communities, ensuring consistent power access for households and community facilities.",
        category: "social",
        impact: "Energy access for communities",
        beneficiaries: "200M+ households",
        icon: "bolt"
    },
    {
        title: "Fishermen Off-Season Living Fund",
        description: "Seasonal support platform providing basic living funds to poor fishermen during off-season periods, featuring donor leaderboards and ensuring year-round family sustenance and economic stability.",
        category: "employment",
        impact: "Seasonal income security",
        beneficiaries: "50M+ fishermen",
        icon: "fish"
    },
    {
        title: "Cleft Surgery Sponsorship Program",
        description: "Medical intervention platform sponsoring cleft surgery for poor children, connecting donors with patients and providing comprehensive treatment including surgery, rehabilitation, and long-term care.",
        category: "healthcare",
        impact: "Life-changing medical interventions",
        beneficiaries: "500K+ children", 
        icon: "user-md"
    },
    {
        title: "Adventure Trip Lottery for Poor Children",
        description: "Recreation platform organizing lottery-based holiday adventure trips for poor children sponsored by wealthy donors, providing cultural exposure and memorable experiences with donor recognition.",
        category: "social",
        impact: "Childhood enrichment experiences",
        beneficiaries: "25M+ children",
        icon: "plane"
    },
    {
        title: "Cooking Gas Cylinder Sponsorship",
        description: "Energy platform enabling sponsors to provide cooking gas cylinders to poor families, featuring donor leaderboards and promoting clean cooking energy for health and environmental benefits.",
        category: "environment",
        impact: "Clean cooking energy access",
        beneficiaries: "500M+ families",
        icon: "fire"
    },
    {
        title: "School Uniform Distribution Network",
        description: "Educational support platform distributing school uniforms to children from poor neighborhoods, featuring sponsor leaderboards and ensuring dignified school attendance for all students.",
        category: "education",
        impact: "Educational dignity and access",
        beneficiaries: "200M+ students",
        icon: "school"
    },
    {
        title: "Elderly Smartphone Distribution",
        description: "Digital inclusion platform distributing non-smartphones to elderly poor with 1-year subscriptions, featuring sponsor leaderboards and ensuring communication access and emergency connectivity.",
        category: "technology", 
        impact: "Elderly digital inclusion",
        beneficiaries: "200M+ elderly",
        icon: "mobile-alt"
    },
    {
        title: "Village Youth Sports Shoes",
        description: "Athletic development platform distributing sporting shoes to underprivileged village youth, featuring sponsor leaderboards and promoting physical activity and sports participation.",
        category: "social",
        impact: "Youth athletic development",
        beneficiaries: "100M+ youth",
        icon: "running"
    },
    {
        title: "Sewing Machine Training Program", 
        description: "Vocational platform providing 6-month sewing machine training and donating machines to unemployed poor, creating sustainable income opportunities through textile skills development.",
        category: "employment",
        impact: "Sustainable skill-based employment",
        beneficiaries: "50M+ trainees",
        icon: "cut"
    },
    {
        title: "Mosquito Net Distribution Initiative",
        description: "Public health platform distributing mosquito nets to poor neighborhoods, preventing vector-borne diseases and improving sleep quality for enhanced health outcomes.",
        category: "healthcare",
        impact: "Disease prevention coverage",
        beneficiaries: "1B+ people",
        icon: "shield-alt"
    },
    {
        title: "Free Eye Testing and Spectacles",
        description: "Vision care platform providing free eye testing and spectacle donations for poor individuals, featuring sponsor leaderboards and ensuring vision correction access for all.",
        category: "healthcare",
        impact: "Vision accessibility", 
        beneficiaries: "500M+ people",
        icon: "eye"
    },
    {
        title: "Free Dental Care for Poor",
        description: "Oral health platform providing free dental checkups and procedures to poor families, featuring sponsor leaderboards and ensuring comprehensive dental health access.",
        category: "healthcare",
        impact: "Dental health accessibility",
        beneficiaries: "1B+ people",
        icon: "tooth"
    },
    {
        title: "Wheelchair Donation Program",
        description: "Mobility platform providing free wheelchairs (motorized/non-motorized) to handicapped poor individuals, featuring sponsor leaderboards and ensuring mobility independence and dignity.",
        category: "healthcare",
        impact: "Mobility independence",
        beneficiaries: "100M+ disabled individuals",
        icon: "wheelchair"
    },
    {
        title: "Hearing Aid Sponsorship Network",
        description: "Hearing health platform sponsoring hearing aids for disadvantaged individuals with hearing loss, featuring donor leaderboards and ensuring communication accessibility for all.",
        category: "healthcare", 
        impact: "Hearing accessibility",
        beneficiaries: "200M+ people",
        icon: "deaf"
    },
    {
        title: "Rural Sports Equipment Sponsorship",
        description: "Youth development platform sponsoring sports equipment for rural poor children, featuring donor leaderboards and promoting physical activity, teamwork, and healthy development.",
        category: "social",
        impact: "Rural youth development",
        beneficiaries: "200M+ rural children",
        icon: "futbol"
    },
    {
        title: "Breadwinner Loss Family Support",
        description: "Crisis support platform providing assistance to families in poor communities who lose their breadwinner, featuring sponsor leaderboards and comprehensive family rehabilitation services.",
        category: "social",
        impact: "Family crisis recovery",
        beneficiaries: "50M+ families",
        icon: "hands-helping"
    },
    {
        title: "Accident Injury Cost Support",
        description: "Emergency platform supporting poor families affected by accident injuries, featuring sponsor leaderboards and providing medical cost coverage and rehabilitation assistance.",
        category: "healthcare",
        impact: "Accident recovery support", 
        beneficiaries: "25M+ families",
        icon: "band-aid"
    },
    {
        title: "Autism Family Support Network",
        description: "Special needs platform supporting poor families affected by autism, featuring sponsor leaderboards and providing therapy resources, educational support, and family assistance.",
        category: "healthcare",
        impact: "Autism family empowerment",
        beneficiaries: "10M+ families",
        icon: "puzzle-piece"
    },
    {
        title: "Village Education Scholarships",
        description: "Educational platform providing scholarships for bright village poor children for higher education, featuring sponsor leaderboards and comprehensive academic support.",
        category: "education",
        impact: "Higher education access",
        beneficiaries: "100M+ students",
        icon: "university"
    },
    {
        title: "Poor Home Repair Support",
        description: "Housing platform supporting repair of poor homes in backward communities, featuring sponsor leaderboards and providing materials and technical assistance for safe housing.",
        category: "housing", 
        impact: "Safe housing conditions",
        beneficiaries: "500M+ households",
        icon: "home"
    },
    {
        title: "Charity Leaderboard Network",
        description: "Philanthropic platform supporting charities through leaderboard systems across various help networks, promoting transparency and competitive giving for maximum social impact.",
        category: "social",
        impact: "Enhanced charitable coordination",
        beneficiaries: "Global communities",
        icon: "chart-line"
    },
    {
        title: "Legal Support for Disadvantaged",
        description: "Justice platform providing legal support to disadvantaged poor individuals, ensuring access to justice regardless of economic status through volunteer legal professionals.",
        category: "social",
        impact: "Justice accessibility for all",
        beneficiaries: "1B+ people",
        icon: "balance-scale"
    },
    {
        title: "Tree Planting Resource Support",
        description: "Environmental platform supporting tree planting with resources and funds, featuring sponsor leaderboards and promoting environmental restoration and climate change mitigation.",
        category: "environment",
        impact: "Environmental restoration",
        beneficiaries: "Global environment",
        icon: "tree"
    },
    {
        title: "Plastic Bag Alternative Support",
        description: "Environmental platform supporting poor communities working to eradicate plastic bags with degradable alternatives, promoting environmental protection and sustainable business development.",
        category: "environment",
        impact: "Plastic pollution reduction",
        beneficiaries: "2B+ communities", 
        icon: "leaf"
    },
    {
        title: "Funeral Cost Support Network",
        description: "Crisis platform supporting poor families with funeral costs for tragic deaths, featuring sponsor leaderboards and ensuring dignified final rites regardless of economic circumstances.",
        category: "social",
        impact: "Death dignity support",
        beneficiaries: "100M+ families",
        icon: "praying-hands"
    },
    {
        title: "Extra Medical Fund Support",
        description: "Healthcare platform providing extra medical funds to poor apart from government aid, featuring sponsor leaderboards and ensuring comprehensive medical coverage for all.",
        category: "healthcare",
        impact: "Comprehensive medical coverage",
        beneficiaries: "2B+ people",
        icon: "medical-kit"
    },
    {
        title: "Basic Water Filter Distribution",
        description: "Water platform distributing free basic water filters to poor neighborhoods, featuring sponsor leaderboards and ensuring safe drinking water access for community health.",
        category: "water",
        impact: "Safe water access",
        beneficiaries: "2B+ people",
        icon: "tint"
    },
    {
        title: "Government Hospital ICU Upgrades",
        description: "Healthcare infrastructure platform supporting old government hospitals' ICU upgrades with cots, outlets, dustbins, featuring sponsor leaderboards for improved patient care.",
        category: "healthcare",
        impact: "Enhanced hospital infrastructure",
        beneficiaries: "1B+ patients",
        icon: "hospital"
    },
    {
        title: "Prosthetic Device Funding",
        description: "Medical device platform funding prosthetic devices for limb loss patients, featuring sponsor leaderboards and ensuring mobility restoration and independence for disabled individuals.",
        category: "healthcare",
        impact: "Mobility restoration",
        beneficiaries: "50M+ disabled individuals",
        icon: "hand-paper"
    },
    {
        title: "Homeless Weather Protection",
        description: "Crisis platform distributing blankets, raincoats, and sleeping mats to homeless poor, featuring sponsor leaderboards and providing essential weather protection and dignity.",
        category: "emergency",
        impact: "Weather protection for homeless",
        beneficiaries: "200M+ homeless individuals",
        icon: "home"
    },
    {
        title: "Park Bench Installation",
        description: "Community platform installing benches in parks in poor neighborhoods, featuring sponsor leaderboards and creating public spaces for community gathering and recreation.",
        category: "social",
        impact: "Community space development",
        beneficiaries: "1B+ residents",
        icon: "chair"
    },
    {
        title: "Village Solar Light Installation",
        description: "Energy platform providing solar light installation in villages without electricity, featuring sponsor leaderboards and enabling education, safety, and economic activities after dark.",
        category: "technology",
        impact: "Rural energy access",
        beneficiaries: "1B+ rural residents",
        icon: "solar-panel"
    },
    {
        title: "Disaster Grocery Support",
        description: "Emergency platform supplying 1-month essential grocery packages to poor after natural disasters, featuring sponsor leaderboards and ensuring immediate food security during recovery.",
        category: "emergency",
        impact: "Disaster food security",
        beneficiaries: "500M+ disaster victims",
        icon: "box"
    },
    {
        title: "Orphan Birthday Celebrations",
        description: "Child welfare platform celebrating orphan children's birthdays with cakes from orphanages/bakeries, featuring fraud prevention checks and ensuring childhood joy and celebration.",
        category: "social",
        impact: "Childhood celebration access",
        beneficiaries: "100M+ orphan children",
        icon: "birthday-cake"
    },
    {
        title: "Newborn Diaper Distribution",
        description: "Child care platform distributing diapers to economically poor parents for newborns/toddlers, featuring sponsor leaderboards and ensuring infant hygiene and health.",
        category: "healthcare",
        impact: "Infant care support",
        beneficiaries: "200M+ infants",
        icon: "baby"
    },
    {
        title: "Mobile Food Delivery for Homeless",
        description: "Nutrition platform setting up mobile food delivery for homeless/underprivileged in areas lacking government canteens, featuring sponsor leaderboards for regular nutrition access.",
        category: "food",
        impact: "Homeless nutrition security", 
        beneficiaries: "100M+ homeless people",
        icon: "truck"
    },
    {
        title: "Summer Cooling for Disabled Households",
        description: "Climate platform providing summer coolers/fans to poor households with disabled or elderly, featuring sponsor leaderboards and ensuring comfort during extreme weather.",
        category: "social",
        impact: "Climate comfort for vulnerable",
        beneficiaries: "100M+ vulnerable households",
        icon: "thermometer-half"
    },
    {
        title: "Agricultural Expert Education",
        description: "Farm education platform sponsoring agricultural experts to educate poor farmers on new technologies, featuring sponsor leaderboards and promoting modern farming techniques.",
        category: "agriculture",
        impact: "Modern farming education",
        beneficiaries: "500M+ farmers",
        icon: "chalkboard-teacher"
    },
    {
        title: "Mobile Medical Village Visits",
        description: "Healthcare platform sponsoring doctor/nurse visits to poor villages, featuring leaderboards for sponsors and medical professionals, ensuring rural healthcare access.",
        category: "healthcare",
        impact: "Rural healthcare delivery",
        beneficiaries: "1B+ rural residents",
        icon: "user-md"
    },
    {
        title: "Community Picnic Bus Trips",
        description: "Recreation platform sponsoring bus trips for 50 people from poor neighborhoods for picnics, featuring sponsor leaderboards and providing community recreation and mental health benefits.",
        category: "social",
        impact: "Community recreation access",
        beneficiaries: "500M+ community members",
        icon: "bus"
    },
    {
        title: "Neighborhood Cleaning Employment",
        description: "Employment platform paying unemployed youth to clean poor neighborhoods, featuring sponsor and helper leaderboards while creating jobs and improving community hygiene.",
        category: "employment",
        impact: "Employment + community cleaning",
        beneficiaries: "50M+ youth",
        icon: "broom"
    },
    {
        title: "Community Water Tank Installation",
        description: "Water platform providing water tanks/hand pumps for underprivileged communities, featuring sponsor leaderboards and ensuring reliable water access for households.",
        category: "water",
        impact: "Community water access",
        beneficiaries: "2B+ people",
        icon: "faucet"
    },
    {
        title: "Urban Job Search Stipend",
        description: "Employment platform supporting unemployed village youth with 3-month stipend in cities to find jobs, featuring sponsor leaderboards and enabling rural-urban job transition.",
        category: "employment",
        impact: "Rural-urban job transition",
        beneficiaries: "100M+ rural youth", 
        icon: "city"
    },
    {
        title: "Street Lamp Installation",
        description: "Safety platform funding solar/electric street lamps in poorly lit poor neighborhoods, featuring sponsor leaderboards and improving community safety and security.",
        category: "social",
        impact: "Community safety enhancement",
        beneficiaries: "2B+ residents",
        icon: "lightbulb"
    },
    {
        title: "Community Library with Technology",
        description: "Education platform building/supporting community libraries with tech/books for poor neighborhoods, featuring sponsor leaderboards and promoting knowledge access.",
        category: "education",
        impact: "Knowledge access enhancement",
        beneficiaries: "1B+ learners",
        icon: "book-open"
    },
    {
        title: "Crop Damage Quick Aid",
        description: "Agricultural platform providing quick aid to farmers after crop damage from disasters, featuring sponsor leaderboards and preventing farmer debt and suicide.",
        category: "agriculture",
        impact: "Farmer crisis prevention",
        beneficiaries: "500M+ farmers",
        icon: "seedling"
    },
    {
        title: "Slum to Better Housing Relocation",
        description: "Housing platform relocating families in slums/dump yards to better housing via government/private aid, featuring sponsor leaderboards for dignified housing transitions.",
        category: "housing",
        impact: "Housing dignity improvement",
        beneficiaries: "1B+ slum residents",
        icon: "building"
    },
    {
        title: "Random Disability Gift Support",
        description: "Disability platform randomly giving gift cheques to poor disabled individuals, featuring sponsor leaderboards and providing unexpected financial support for essential needs.",
        category: "social",
        impact: "Disability financial support",
        beneficiaries: "500M+ disabled people",
        icon: "gift"
    },
    {
        title: "School Dropout Recovery",
        description: "Education platform encouraging school dropouts to return via scholarships/books/uniforms and counseling, featuring sponsor leaderboards for education recovery.",
        category: "education",
        impact: "Education recovery support",
        beneficiaries: "200M+ dropouts",
        icon: "undo"
    },
    {
        title: "Village School Infrastructure Upgrade",
        description: "Education platform upgrading poor village school infrastructure, featuring sponsor leaderboards and providing modern educational facilities for quality learning.",
        category: "education",
        impact: "Educational infrastructure improvement",
        beneficiaries: "1B+ students",
        icon: "school"
    },
    {
        title: "Village School Educational Tours",
        description: "Education platform sponsoring picnics and science tours for village school kids, featuring sponsor leaderboards and providing experiential learning opportunities.",
        category: "education", 
        impact: "Experiential learning access",
        beneficiaries: "500M+ students",
        icon: "bus"
    },
    {
        title: "Inter-School Sports Events",
        description: "Sports platform sponsoring inter-school sports events in poor neighborhoods, featuring sponsor leaderboards and promoting youth athletic development and competition.",
        category: "social",
        impact: "Youth sports development",
        beneficiaries: "1B+ students",
        icon: "trophy"
    },
    {
        title: "Farmer Suicide Prevention",
        description: "Mental health platform preventing farmer suicides via counseling, emergency aid, government scheme links, featuring sponsor leaderboards for comprehensive farmer support.",
        category: "healthcare",
        impact: "Farmer life preservation",
        beneficiaries: "500M+ farmers",
        icon: "heart"
    },
    {
        title: "Poor Neighborhood Job Fairs",
        description: "Employment platform organizing job fairs in poor neighborhoods, featuring sponsor leaderboards and connecting local residents with employment opportunities.",
        category: "employment",
        impact: "Local employment access",
        beneficiaries: "1B+ job seekers",
        icon: "handshake"
    },
    {
        title: "Community Ambulance Procurement",
        description: "Healthcare platform procuring and funding ambulances with drivers for poor neighborhoods, featuring sponsor leaderboards and ensuring emergency medical response.",
        category: "healthcare",
        impact: "Emergency medical access",
        beneficiaries: "2B+ residents",
        icon: "ambulance"
    },
    {
        title: "Girls Education and Equality",
        description: "Gender platform empowering girls in poor neighborhoods for education and equality, featuring sponsor leaderboards and promoting women's empowerment through education.",
        category: "education",
        impact: "Gender equality in education",
        beneficiaries: "1B+ girls",
        icon: "female"
    },
    {
        title: "Neighborhood Waste Management",
        description: "Environmental platform installing dry/wet dustbins and regular cleanup in poor neighborhoods, featuring sponsor leaderboards for improved community hygiene.",
        category: "environment",
        impact: "Community waste management",
        beneficiaries: "5B+ residents",
        icon: "trash-alt"
    },
    {
        title: "Handloom Weaver Support",
        description: "Craft platform supporting manual handloom weavers with raw materials, tools, and market access, featuring sponsor leaderboards for traditional craft preservation.",
        category: "employment",
        impact: "Traditional craft support",
        beneficiaries: "10M+ weavers",
        icon: "palette"
    },
    {
        title: "Heart Operation Donor Connection",
        description: "Medical platform connecting donors with hospitals to fund heart operations for poor patients, ensuring life-saving cardiac procedures regardless of economic status.",
        category: "healthcare",
        impact: "Life-saving cardiac care",
        beneficiaries: "10M+ cardiac patients",
        icon: "heartbeat"
    },
    {
        title: "Kidney Transplant Donor Connection",
        description: "Medical platform connecting donors with poor patients needing kidney transplants, providing comprehensive renal care and life-saving treatment access.",
        category: "healthcare",
        impact: "Life-saving renal care",
        beneficiaries: "5M+ renal patients",
        icon: "hospital"
    },
    {
        title: "Rural Laptop Distribution",
        description: "Technology platform supporting distribution of refurbished or old laptops and tablets to educated unemployed youth in villages for digital empowerment.",
        category: "technology",
        impact: "Rural digital access",
        beneficiaries: "500M+ rural youth",
        icon: "laptop"
    },
    {
        title: "Child Labor Upliftment",
        description: "Child protection platform uplifting child laborers from poverty and despair through comprehensive rehabilitation, education, and family support services.",
        category: "social",
        impact: "Child labor elimination",
        beneficiaries: "500M+ children",
        icon: "shield-alt"
    },
    {
        title: "Youth Nation-Building Jobs",
        description: "Employment platform supporting youth from poor neighborhoods with nation-building jobs in infrastructure, education, and community development sectors.",
        category: "employment",
        impact: "Civic employment opportunities",
        beneficiaries: "200M+ youth",
        icon: "flag"
    },
    {
        title: "Rural School Bicycle Program",
        description: "Transportation platform sponsoring bicycles for poor school-going children in rural areas, reducing dropout rates due to long-distance travel with sponsor leaderboards.",
        category: "education",
        impact: "Education access improvement",
        beneficiaries: "500M+ rural students",
        icon: "bicycle"
    },
    {
        title: "Rural Artisan Global Market",
        description: "Commerce platform connecting rural artisans (pottery, bamboo, handcrafts) with city and global buyers, enabling income for poor artisans with sponsor leaderboards.",
        category: "employment",
        impact: "Global artisan market access",
        beneficiaries: "100M+ artisans",
        icon: "globe"
    },
    {
        title: "Cancer Treatment Donor Support",
        description: "Oncology platform supporting poor patients needing cancer treatment with donor funding for chemotherapy, radiation, palliative care, and verified hospital partnerships.",
        category: "healthcare",
        impact: "Cancer care accessibility",
        beneficiaries: "50M+ cancer patients",
        icon: "ribbon"
    },
    {
        title: "Energy Efficient Cooking Stoves",
        description: "Environmental platform connecting poor households with energy-efficient cooking stoves, reducing firewood use, indoor pollution, and health issues with sponsor leaderboards.",
        category: "environment",
        impact: "Clean cooking + health",
        beneficiaries: "2B+ households",
        icon: "fire"
    },
    {
        title: "Extreme Weather Safe Shelters",
        description: "Emergency platform providing safe shelters for homeless poor during extreme weather (heat waves, floods, winter cold) with donor-funded temporary housing.",
        category: "emergency",
        impact: "Weather emergency protection",
        beneficiaries: "1B+ vulnerable people",
        icon: "home"
    },
    {
        title: "Widow Support and Training",
        description: "Women's platform supporting widows in poor neighborhoods with monthly pensions, training, and emotional support groups with sponsor recognition leaderboards.",
        category: "social",
        impact: "Widow empowerment",
        beneficiaries: "200M+ widows",
        icon: "female"
    },
    {
        title: "Digital Learning Kit Distribution",
        description: "Education platform providing poor school kids with digital learning kits (educational tablets preloaded with e-learning apps) with sponsor leaderboards.",
        category: "technology",
        impact: "Digital education enhancement",
        beneficiaries: "1B+ students",
        icon: "tablet-alt"
    },
    {
        title: "Multi-Skill Training for Youth",
        description: "Vocational platform enabling skill training (plumbing, electrician, tailoring, mobile repair, website creation using AI) for unemployed youth with donor-funded courses.",
        category: "employment",
        impact: "Multiple skill development",
        beneficiaries: "500M+ youth",
        icon: "tools"
    },
    {
        title: "Open Gym Installation",
        description: "Fitness platform installing open gyms in poor neighborhoods sponsored by wealthy donors, promoting community health and fitness with sponsor leaderboards.",
        category: "healthcare",
        impact: "Community fitness access",
        beneficiaries: "2B+ residents",
        icon: "dumbbell"
    },
    {
        title: "Poverty App Development Funding",
        description: "Technology platform funding people working on technical design and implementation of apps specifically for upliftment of poor with sponsor leaderboards.",
        category: "technology",
        impact: "Poverty-focused innovation",
        beneficiaries: "Global poor population",
        icon: "code"
    }
];