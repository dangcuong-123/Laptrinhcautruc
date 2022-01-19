import sqlite3

con = sqlite3.connect('database.db')

cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS products;")
cur.execute('''CREATE TABLE IF NOT EXISTS products (ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                                    name varchar(50) DEFAULT NULL,
                                    detail varchar(3000) DEFAULT NULL, 
                                    brand varchar(50) DEFAULT NULL,
                                    price float DEFAULT NULL, 
                                    category_id INTEGER DEFAULT NULL,   
                                    image varchar(200) DEFAULT NULL,   
                                    size varchar(50) DEFAULT NULL, 
                                    video varchar(200) DEFAULT NULL, 
                                    color varchar(50) DEFAULT NULL, 
                                    quantity int(5) DEFAULT 0);''')

cur.execute("DROP TABLE IF EXISTS category;")
cur.execute('''CREATE TABLE IF NOT EXISTS category (ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                                    name varchar(50) DEFAULT NULL);''')

cur.execute('''INSERT INTO category (ID, name) VALUES
(128, 'sip');''')

cur.execute('''INSERT INTO category (name) VALUES
('quan'),('ao'), ('mu'), ('tui'), ('dam');''')

cur.execute('''INSERT INTO products (ID, name, detail, brand, price, category_id, image, size, video, color, quantity) VALUES
(128, "quan nu xep li", "vai khong cang", "ZARA" , 458000, 129, "https://img.ltwebstatic.com/images3_pi/2021/10/21/16347942624bb0b4f4e3c3b4baa9ae8f05c6fc59bd_thumbnail_900x.webp", "M", NULL, "xam den", 50);''')

cur.execute('''INSERT INTO products (name, detail, brand, price, category_id, image, size, video, color, quantity) VALUES 
("dam pha le kim cuong", "vien la sen, pha le kim cuong",  "DAZY",  565000, 133, "https://img.ltwebstatic.com/images3_pi/2021/12/01/1638325454b376df373da68aee4be6e7e2fee2c811_thumbnail_900x.webp ", "L", NULL, "den", 100), 
("quan short denim", "quan ong rong", "BOUTIQUE", 125000, 129, "https://img.ltwebstatic.com/images3_pi/2021/06/10/1623290444dbe201251a5971ec3055eb6c317eaf82_thumbnail_900x.webp", "M", NULL, "den", 5),
("mu ret kim", "mu tron", NULL, 75000, 131,"https://img.ltwebstatic.com/images3_pi/2021/08/12/162876005536b8730f14bf9e5face7ce21d4cbb6da_thumbnail_900x.webp",NULL, NULL, "den", 100),
("quan nam duong pho", "quan cargo", "SHEIN", 1000000, 129,  "https://img.ltwebstatic.com/images3_pi/2021/09/30/16329788324522175c002148e40e57e032ef26a028_thumbnail_900x.webp", "L", NULL, "den", 43),
("quan nu mau tron thanh lich", "quan ong rong", "DAZY", 180000, 129 ,"https://img.ltwebstatic.com/images3_pi/2021/09/24/1632451449e36e1405a27991d04c76c45a6dde14cb_thumbnail_900x.webp" ,"L", NULL, "den", 100);''')


con.commit()

con.close()