# Task 1: Add a Member


# import sqlite3

# def add_member(id, name, age, trainer_id):
#     try:
#         conn = sqlite3.connect('gym.db')
#         cursor = conn.cursor()
        
#         # SQL query to add a new member
#         cursor.execute('''
#             INSERT INTO Members (id, name, age, trainer_id) 
#             VALUES (?, ?, ?, ?)
#         ''', (id, name, age, trainer_id))
        
#         conn.commit()
#         print(f"Member {name} added successfully.")
#     except sqlite3.IntegrityError as e:
#         print(f"Error: {e}")
#     finally:
#         conn.close()

# # Example usage
# add_member(1, 'John Doe', 28, 101)


# Task 2: Add a Workout Session


# def add_workout_session(member_id, date, duration_minutes, calories_burned):
#     try:
#         conn = sqlite3.connect('gym.db')
#         cursor = conn.cursor()
        
#         # Check if member exists
#         cursor.execute('SELECT id FROM Members WHERE id = ?', (member_id,))
#         if cursor.fetchone() is None:
#             print(f"Error: Member ID {member_id} does not exist.")
#             return
        
#         # SQL query to add a new workout session
#         cursor.execute('''
#             INSERT INTO WorkoutSessions (member_id, date, duration_minutes, calories_burned) 
#             VALUES (?, ?, ?, ?)
#         ''', (member_id, date, duration_minutes, calories_burned))
        
#         conn.commit()
#         print("Workout session added successfully.")
#     except sqlite3.IntegrityError as e:
#         print(f"Error: {e}")
#     finally:
#         conn.close()

# # Example usage
# add_workout_session(1, '2024-06-01', 60, 500)


# Task 3: Updating Member Information



# def update_member_age(member_id, new_age):
#     try:
#         conn = sqlite3.connect('gym.db')
#         cursor = conn.cursor()
        
#         # Check if member exists
#         cursor.execute('SELECT id FROM Members WHERE id = ?', (member_id,))
#         if cursor.fetchone() is None:
#             print(f"Error: Member ID {member_id} does not exist.")
#             return
        
#         # SQL query to update age
#         cursor.execute('''
#             UPDATE Members 
#             SET age = ? 
#             WHERE id = ?
#         ''', (new_age, member_id))
        
#         conn.commit()
#         print("Member age updated successfully.")
#     except sqlite3.Error as e:
#         print(f"Error: {e}")
#     finally:
#         conn.close()

# # Example usage
# update_member_age(1, 29)


# Task 4: Delete a Workout Session


# def delete_workout_session(session_id):
#     try:
#         conn = sqlite3.connect('gym.db')
#         cursor = conn.cursor()
        
#         # Check if session exists
#         cursor.execute('SELECT id FROM WorkoutSessions WHERE id = ?', (session_id,))
#         if cursor.fetchone() is None:
#             print(f"Error: Session ID {session_id} does not exist.")
#             return
        
#         # SQL query to delete a session
#         cursor.execute('DELETE FROM WorkoutSessions WHERE id = ?', (session_id,))
        
#         conn.commit()
#         print("Workout session deleted successfully.")
#     except sqlite3.Error as e:
#         print(f"Error: {e}")
#     finally:
#         conn.close()

# # Example usage
# delete_workout_session(1)



# Task 1: SQL BETWEEN Usage



# def get_members_in_age_range(start_age, end_age):
#     try:
#         conn = sqlite3.connect('gym.db')
#         cursor = conn.cursor()
        
#         # SQL query using BETWEEN
#         cursor.execute('''
#             SELECT name, age, trainer_id 
#             FROM Members 
#             WHERE age BETWEEN ? AND ?
#         ''', (start_age, end_age))
        
#         results = cursor.fetchall()
#         for row in results:
#             print(row)
            
#         return results
#     except sqlite3.Error as e:
#         print(f"Error: {e}")
#     finally:
#         conn.close()

# # Example usage
# get_members_in_age_range(25, 30)