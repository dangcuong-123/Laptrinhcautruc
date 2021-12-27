import sqlite3

con = sqlite3.connect('database.db')

cur = con.cursor()


cur.execute('''CREATE TABLE IF NOT EXISTS products (ID int(5) NOT NULL, 
                                    name varchar(50) DEFAULT NULL,
                                    type varchar(50) DEFAULT NULL,     
                                    price float DEFAULT NULL,     
                                    description varchar(3000) DEFAULT NULL,     
                                    size varchar(50) DEFAULT NULL, 
                                    image varchar(200) DEFAULT NULL, 
                                    video varchar(200) DEFAULT NULL, 
                                    color varchar(50) DEFAULT NULL, 
                                    quantity int(5) DEFAULT 0,     
                                    PRIMARY KEY(ID) );''')
cur.execute("DROP TABLE products;")

cur.execute('''CREATE TABLE IF NOT EXISTS products (ID int(5) NOT NULL, 
                                    name varchar(50) DEFAULT NULL,
                                    type varchar(50) DEFAULT NULL,     
                                    price float DEFAULT NULL,     
                                    description varchar(3000) DEFAULT NULL,     
                                    size varchar(50) DEFAULT NULL, 
                                    image varchar(200) DEFAULT NULL, 
                                    video varchar(200) DEFAULT NULL, 
                                    color varchar(50) DEFAULT NULL, 
                                    quantity int(5) DEFAULT 0,     
                                    PRIMARY KEY(ID) );''')


cur.execute('''INSERT INTO products (ID, name, type, price, description, size, image, video, color, quantity) VALUES 
(124123, "quan nu xep li", "quan tay", 458000, "soi vai khong cang", "M", "https://img.ltwebstatic.com/images3_pi/2021/10/21/16347942624bb0b4f4e3c3b4baa9ae8f05c6fc59bd_thumbnail_900x.webp", NULL, "xam den", 50),
(125123, "dam pha le kim cuong", "dam", 565000, "chat lieu nhung ,tay ao dai", "L", "http://img.ltwebstatic.com/images3_pi/2021/07/31/1627731395dac7229f5c559c11950294f29bdd4780.png", NULL, "den", 26),
(126123, "quan short denim", "quan ong rong", 125000, "hem tho, chat lieu denim/jean","M","https://img.ltwebstatic.com/images3_pi/2021/06/10/1623290444dbe201251a5971ec3055eb6c317eaf82_thumbnail_900x.webp", NULL, "den", 5),
(127123, "mu ret kim", "mu", 75000, "100% Acrylic","freesize","https://img.ltwebstatic.com/images3_pi/2021/08/12/162876005536b8730f14bf9e5face7ce21d4cbb6da_thumbnail_900x.webp",NULL, "den", 100),
(128123, "quan nam duong pho", "quan cargo", 1000000, "80% Polyester, 20% bong", "L", "https://img.ltwebstatic.com/images3_pi/2021/09/30/16329788324522175c002148e40e57e032ef26a028_thumbnail_900x.webp",  NULL, "den", 43),
(129123, "quan nu mau tron thanh lich", "quan ong rong", 180000, "80% Polyester, 15% soi kim loai hoa, 5% bong vai thun","L","https://img.ltwebstatic.com/images3_pi/2021/09/24/1632451449e36e1405a27991d04c76c45a6dde14cb_thumbnail_900x.webp",NULL, "den", 100);''')

cur.execute('''INSERT INTO products(ID, name, type, price, description, size, image, video, color,  quantity) VALUES (195123,"ao ba lo","ao ba lo", 30000, "ngon, bo, re","X","https://shoptretho.com.vn/upload/image/product/20160620/ao-ba-lo-so-sinh-carter-1.jpg", NULL,"den", 11);''')

cur.execute('''INSERT INTO products(ID, name, type, price, description, size, image, video, color,  quantity) VALUES (154123,"ao len giu am","ao len", 80000, "ngon, bo, re","XL","https://sakurafashion.vn/upload/sanpham/large/6351-ao-len-trong-co-don-gian-1.jpg", NULL,"nau", 11);''')

cur.execute('''INSERT INTO products(ID, name, type, price, description, size, image, video, color,  quantity) VALUES (163123,"ao len co lo","ao len", 1200000, "ngon, bo, re","X","https://scontent.webpluscnd.net/photos-df/a-0/1912-1868961-1/ao-len-nu-gu--uniqlo---wl144.png?atk=6f7db80a49ce4c5e7ac5f209ac9806c4", NULL,"den", 11);''')

cur.execute('''INSERT INTO products(ID, name, type, price, description, size, image, video, color,  quantity) VALUES (173123,"ao bong ro","ao ba lo", 120000, "ngon, bo, re","XL","https://chuyendobongro.com/wp-content/uploads/2020/08/%C3%81o-b%C3%B3ng-r%E1%BB%95-c%C3%B3-tay-Jordan-Bull-%C4%90%E1%BB%8F.jpg", NULL,"den", 11);''')

cur.execute('''INSERT INTO products(ID, name, type, price, description, size, image, video, color,  quantity) VALUES (183123,"ao coc","ao phong", 50000, "ngon, bo, re","XL","https://lh3.googleusercontent.com/proxy/M7Qzao6IgZUQSTFtGImNw_2esnXTmDS9WlclmMxiOEOcYqGxhRFf-Dxc0Ad053lLrnnkNLSAgVzILOzDVo1aJCjsULFiJk6JpETRBzvyfHkhNV0hBqfPOqksGUSDK7rk9MaU57HIQdD7nuYWeMV1", NULL,"vang", 11);''')

con.commit()

con.close()
