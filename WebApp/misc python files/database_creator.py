import sqlite3

def create_specific_database():
    topics_with_subtopics = {
        'biology': ['ecology'],
        'chemistry': [],
        'physics': []
    }
    
    conn = sqlite3.connect('./WebApp/databases/new_questions_environment.db')
    cursor = conn.cursor()
    
    for topic, subtopics in topics_with_subtopics.items():
        for subtopic in subtopics:
            table_name = f"{topic}_{subtopic}"
            cursor.execute(f'''
                CREATE TABLE IF NOT EXISTS {table_name} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    question TEXT NOT NULL,
                    difficulty INTEGER NOT NULL,
                    type TEXT NOT NULL,
                    correct_answer TEXT NOT NULL,
                    image_path TEXT
                );
            ''')
    
    conn.commit()
    conn.close()

# Run this function to create the new database schema with specified sub-topics and image field
create_specific_database()

def populate_ecology_questions():
    # Existing questions from the provided list
    existing_questions = [
        ("Describe the meaning of the term 'community'.", 1, "Short Answer", "Yes", None),
        ("The organisms in this food web are said to be interdependent. Explain what is meant by this.", 2, "Short Answer", "Yes", "frontend/images/database/The Organisms in the Environment/food web.jpg"),
        ("The information in the image shows some interactions and feeding relationships between different species. However, the image does not represent an entire ecosystem. Explain why.", 2, "Structured", "Yes", "frontend/images/database/The Organisms in the Environment/food web.jpg"),
        ("After a period of drought, there was a reduction in the growth of grass. With reference to the image, explain how this would affect the population of caterpillars.", 3, "Data Response", "Yes", "frontend/images/database/The Organisms in the Environment/food web.jpg"),
        ("Calculate the mean number of lichens found in the quadrats from the west side of the tree.", 2, "Data Response", "Yes", "frontend/images/database/The Organisms in the Environment/quadrant.jpg"),
        ("Give another method that the students could have used to measure the abundance of the lichen.", 2, "Short Answer", "Yes", None),
        ("Give two abiotic factors which would impact the growth of these lichens.", 2, "Short Answer", "Yes", None),
        ("State the meaning of the term 'biodiversity'.", 1, "Short Answer", "Yes", None),
        ("Suggest one adjustment to the method which would help to ensure that the student collected a representative sample.", 2, "Structured", "Yes", None),
        ("Identify which site has the highest biodiversity.", 2, "Data Response", "Yes", None),
        ("Suggest why data could not be collected about these birds using the method from part above.", 2, "Structured", "Yes", "frontend/images/database/The Organisms in the Environment/method.jpg"),
        ("Explain how their presence may have led to the biodiversity seen in the data collected.", 3, "Structured", "Yes", None)
    ]

    new_questions = [
        ("Define the term 'ecosystem'.", 1, "Short Answer", "Yes", None),
        ("Explain the difference between a food chain and a food web.", 1, "Short Answer", "Yes", "/path/to/food_chain_vs_web.jpg"),
        ("Describe two examples of abiotic factors in an ecosystem.", 1, "Short Answer", "Yes", None),
        ("What is the primary source of energy in most ecosystems?", 1, "Short Answer", "Yes", None),
        ("What is the importance of decomposers in an ecosystem?", 2, "Short Answer", "Yes", None),
        ("Explain the process of photosynthesis.", 2, "Short Answer", "Yes", "/path/to/photosynthesis.jpg"),
        ("Describe how energy flows through an ecosystem, starting from producers.", 2, "Short Answer", "Yes", None),
        ("What is the role of keystone species in an ecosystem?", 2, "Short Answer", "Yes", None),
        ("Explain the difference between primary and secondary succession.", 3, "Short Answer", "Yes", None),
        ("Describe the process of eutrophication and its impact on aquatic ecosystems.", 3, "Short Answer", "Yes", None),
        ("Explain the concept of carrying capacity in population ecology.", 3, "Short Answer", "Yes", None),
        ("What are some strategies used by organisms to adapt to their environment?", 3, "Short Answer", "Yes", None),
        ("What is a trophic cascade and how can it impact ecosystems?", 4, "Short Answer", "Yes", None),
        ("Describe the role of apex predators in regulating ecosystem dynamics.", 4, "Short Answer", "Yes", None),
        ("Explain the concept of niche partitioning and its importance in maintaining biodiversity.", 4, "Short Answer", "Yes", None),
        ("What is the significance of biodiversity hotspots and how are they identified?", 4, "Short Answer", "Yes", None),
        ("Discuss the concept of ecological succession in detail, providing examples.", 5, "Short Answer", "Yes", None),
        ("Explain the theory of island biogeography and its relevance to conservation biology.", 5, "Short Answer", "Yes", None),
        ("Describe the process of evolution by natural selection and its role in shaping ecosystems.", 5, "Short Answer", "Yes", None),
        ("What are the major threats to biodiversity and how can they be addressed?", 5, "Short Answer", "Yes", None),
        ("Analyze the impact of climate change on ecosystems and biodiversity.", 6, "Short Answer", "Yes", None),
        ("Discuss the role of habitat fragmentation in species extinction.", 6, "Short Answer", "Yes", None),
        ("Examine the relationship between human population growth and environmental degradation.", 6, "Short Answer", "Yes", None),
        ("Evaluate the effectiveness of different conservation strategies in preserving biodiversity.", 6, "Short Answer", "Yes", None),
        ("Compare and contrast the characteristics of different biomes and their ecological significance.", 7, "Short Answer", "Yes", None),
        ("Assess the ethical considerations in wildlife conservation efforts.", 7, "Short Answer", "Yes", None),
        ("Explain the concept of ecosystem services and their importance to human well-being.", 7, "Short Answer", "Yes", None),
        ("Analyze the role of invasive species in disrupting ecosystems and biodiversity.", 7, "Short Answer", "Yes", None),
        ("Discuss the potential impacts of genetically modified organisms (GMOs) on ecosystems and biodiversity.", 8, "Short Answer", "Yes", None),
        ("Evaluate the role of ecotourism in promoting conservation and sustainable development.", 8, "Short Answer", "Yes", None),
        ("Examine the link between deforestation and loss of biodiversity, and propose solutions.", 8, "Short Answer", "Yes", None),
        ("Assess the challenges and opportunities of implementing international agreements for biodiversity conservation.", 8, "Short Answer", "Yes", None),
        ("Analyze the socio-economic factors influencing conservation efforts and biodiversity management.", 9, "Short Answer", "Yes", None),
        ("Examine the ethical dilemmas associated with conservation biology and environmental policy-making.", 9, "Short Answer", "Yes", None),
        ("Evaluate the effectiveness of global conservation initiatives in preserving biodiversity.", 9, "Short Answer", "Yes", None),
        ("Discuss the role of indigenous knowledge and practices in biodiversity conservation.", 9, "Short Answer", "Yes", None)
    ]

    all_questions = existing_questions + new_questions

    conn = sqlite3.connect('./WebApp/databases/new_questions_environment.db')
    cursor = conn.cursor()

    cursor.executemany('INSERT INTO biology_ecology (question, difficulty, type, correct_answer, image_path) VALUES (?, ?, ?, ?, ?)', all_questions)
    conn.commit()
    conn.close()

# Run this function to populate the ecology sub-topic with questions, including local images
populate_ecology_questions()

