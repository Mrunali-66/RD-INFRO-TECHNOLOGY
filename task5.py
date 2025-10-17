import sqlite3
def create_connection():
    """Create or connect to SQLite database"""
    conn = sqlite3.connect('contacts.db')
    return conn


def create_table(conn):
    """Create contacts table"""
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT
        )
    ''')
    conn.commit()
    print("✅ Table created successfully!")


def insert_contacts(conn):
    """Insert 40 Indian contact entries"""
    cursor = conn.cursor()
    contacts = [
        ('Mrunali Hajare', '9876543210', 'mrunali@example.com'),
        ('Anjali Kadam', '9823456710', 'anju@example.com'),
        ('Aasmita Kale', '9123456780', 'asmita@example.com'),
        ('Rohit Patil', '9890123456', 'rohit.patil@example.com'),
        ('Sneha Joshi', '9876012345', 'sneha.joshi@example.com'),
        ('Aditya Sharma', '9988776655', 'aditya.sharma@example.com'),
        ('Priya Deshmukh', '9812345678', 'priya.deshmukh@example.com'),
        ('Vikas Verma', '9822098765', 'vikas.verma@example.com'),
        ('Kiran Singh', '9701122334', 'kiran.singh@example.com'),
        ('Aarti More', '9856001234', 'aarti.more@example.com'),
        ('Ramesh Iyer', '9911223344', 'ramesh.iyer@example.com'),
        ('Neha Kulkarni', '9787654321', 'neha.kulkarni@example.com'),
        ('Aman Gupta', '9922334455', 'aman.gupta@example.com'),
        ('Divya Nair', '9765432109', 'divya.nair@example.com'),
        ('Rahul Chavan', '9845123678', 'rahul.chavan@example.com'),
        ('Pooja Mehta', '9990011223', 'pooja.mehta@example.com'),
        ('Suresh Kumar', '9800112233', 'suresh.kumar@example.com'),
        ('Manisha Pawar', '9877604321', 'manisha.pawar@example.com'),
        ('Akash Yadav', '9811981198', 'akash.yadav@example.com'),
        ('Komal Reddy', '9900554433', 'komal.reddy@example.com'),
        ('Ravi Jadhav', '9871109876', 'ravi.jadhav@example.com'),
        ('Meena Pillai', '9811122233', 'meena.pillai@example.com'),
        ('Sahil Khan', '9776677885', 'sahil.khan@example.com'),
        ('Kavita Rao', '9823344556', 'kavita.rao@example.com'),
        ('Deepak Sinha', '9888997766', 'deepak.sinha@example.com'),
        ('Chaitali Ghosh', '9871209876', 'chaitali.ghosh@example.com'),
        ('Arjun Mishra', '9834567890', 'arjun.mishra@example.com'),
        ('Shruti Patankar', '9819876543', 'shruti.patankar@example.com'),
        ('Gaurav Jain', '9998887776', 'gaurav.jain@example.com'),
        ('Nikita Patil', '9845632198', 'nikita.patil@example.com'),
        ('Ankit Desai', '9874556677', 'ankit.desai@example.com'),
        ('Payal Bhatt', '9767112233', 'payal.bhatt@example.com'),
        ('Vivek Malhotra', '9811002233', 'vivek.malhotra@example.com'),
        ('Harsha Menon', '9821223344', 'harsha.menon@example.com'),
        ('Shreya Bansal', '9994433221', 'shreya.bansal@example.com'),
        ('Mayur Shetty', '9898776655', 'mayur.shetty@example.com'),
        ('Tanvi Nanda', '9756612345', 'tanvi.nanda@example.com'),
        ('Omkar Pawar', '9811678912', 'omkar.pawar@example.com'),
        ('Ritika Dubey', '9866001122', 'ritika.dubey@example.com'),
        ('Jayesh Patel', '9723456789', 'jayesh.patel@example.com')
    ]

    cursor.executemany('INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)', contacts)
    conn.commit()
    print(f"✅ {len(contacts)} contacts inserted successfully!")


def fetch_contacts(conn):
    """Fetch and display all contacts"""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts")
    rows = cursor.fetchall()

    print("\n📇 CONTACT BOOK:")
    print("-" * 60)
    for row in rows:
        print(f"ID: {row[0]:<2} | Name: {row[1]:<20} | Phone: {row[2]} | Email: {row[3]}")
    print("-" * 60)
    print(f"Total Contacts: {len(rows)}")


def main():
    conn = create_connection()
    create_table(conn)
    insert_contacts(conn)
    fetch_contacts(conn)
    conn.close()
    print("\n🔒 Connection closed successfully!")


if __name__ == "__main__":
    main()
