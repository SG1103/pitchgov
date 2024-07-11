import sqlite3

def clean_image_paths():
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
            
            # Update records where image_path does not start with 'frontend'
            cursor.execute(f'''
                UPDATE {table_name}
                SET image_path = NULL
                WHERE image_path IS NOT NULL AND image_path NOT LIKE 'frontend%'
            ''')
    
    conn.commit()
    conn.close()

# Run this function to clean the image paths
clean_image_paths()
