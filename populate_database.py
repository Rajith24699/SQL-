import sqlite3
import random
from faker import Faker

faker = Faker()
conn = sqlite3.connect('library_management.db')
cursor = conn.cursor()

# Insert data into Books table
genres = ['Fiction', 'Non-fiction', 'Science Fiction', 'Biography', 'Mystery']
for _ in range(200):
    cursor.execute("""
        INSERT INTO books (title, author, genre, isbn, published_year, copies_available, price)
        VALUES (?, ?, ?, ?, ?, ?, ?);
    """, (
        faker.text(max_nb_chars=20),
        faker.name(),
        random.choice(genres),
        faker.isbn13(),
        random.randint(1950, 2023),
        random.randint(1, 20),
        round(random.uniform(5, 100), 2)
    ))

# Insert data into Members table
membership_levels = ['Silver', 'Gold', 'Platinum']
for _ in range(500):
    cursor.execute("""
        INSERT INTO members (name, email, membership_level, membership_years, fines_collected)
        VALUES (?, ?, ?, ?, ?);
    """, (
        faker.name(),
        faker.email(),
        random.choice(membership_levels),
        random.randint(1, 10),
        round(random.uniform(0, 50), 2)
    ))

# Insert data into Transactions table
for _ in range(1000):
    cursor.execute("""
        INSERT INTO transactions (book_id, member_id, borrow_date, return_date, fine_collected)
        VALUES (?, ?, ?, ?, ?);
    """, (
        random.randint(1, 200),
        random.randint(1, 500),
        faker.date_between(start_date='-2y', end_date='today'),
        faker.date_between(start_date='-1y', end_date='today') if random.random() > 0.5 else None,
        round(random.uniform(0, 10), 2)
    ))

conn.commit()
conn.close()
