
CREATE TABLE Users (
                id_user SMALLINT AUTO_INCREMENT NOT NULL,
                user_first_name VARCHAR(64) NOT NULL,
                user_last_name VARCHAR(64),
                PRIMARY KEY (id_user)
);


CREATE TABLE TR_Shop (
                id_shop SMALLINT AUTO_INCREMENT NOT NULL,
                shop_name VARCHAR(64) NOT NULL,
                PRIMARY KEY (id_shop)
);


CREATE TABLE TR_Country (
                id_country SMALLINT AUTO_INCREMENT NOT NULL,
                country_name VARCHAR(32) NOT NULL,
                PRIMARY KEY (id_country)
);


CREATE TABLE Products (
                id_product SMALLINT NOT NULL,
                manufacturing_place SMALLINT,
                product_name VARCHAR(64) NOT NULL,
                product_url VARCHAR(256) NOT NULL,
                nutrition_score CHAR(1) NOT NULL,
                PRIMARY KEY (id_product)
);


CREATE TABLE TJ_Products_Shop (
                id_product SMALLINT NOT NULL,
                id_shop SMALLINT NOT NULL,
                PRIMARY KEY (id_product, id_shop)
);


CREATE TABLE TJ_Products_Users (
                id_product SMALLINT NOT NULL,
                id_user SMALLINT NOT NULL,
                PRIMARY KEY (id_product, id_user)
);


CREATE TABLE TR_Category (
                id_category SMALLINT AUTO_INCREMENT NOT NULL,
                category_name VARCHAR(64) NOT NULL,
                PRIMARY KEY (id_category)
);


CREATE TABLE TJ_Products_Category (
                id_product SMALLINT NOT NULL,
                id_category SMALLINT NOT NULL,
                PRIMARY KEY (id_product, id_category)
);


ALTER TABLE TJ_Products_Users ADD CONSTRAINT users_users_favorites_fk
FOREIGN KEY (id_user)
REFERENCES Users (id_user)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE TJ_Products_Shop ADD CONSTRAINT tr_shop_product_shops_fk
FOREIGN KEY (id_shop)
REFERENCES TR_Shop (id_shop)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE Products ADD CONSTRAINT tr_country_products_fk
FOREIGN KEY (manufacturing_place)
REFERENCES TR_Country (id_country)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE TJ_Products_Users ADD CONSTRAINT products_users_favorites_fk
FOREIGN KEY (id_product)
REFERENCES Products (id_product)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE TJ_Products_Shop ADD CONSTRAINT products_product_shops_fk
FOREIGN KEY (id_product)
REFERENCES Products (id_product)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE TJ_Products_Category ADD CONSTRAINT products_product_categories_fk
FOREIGN KEY (id_product)
REFERENCES Products (id_product)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE TJ_Products_Category ADD CONSTRAINT tr_category_product_categories_fk
FOREIGN KEY (id_category)
REFERENCES TR_Category (id_category)
ON DELETE NO ACTION
ON UPDATE NO ACTION;
