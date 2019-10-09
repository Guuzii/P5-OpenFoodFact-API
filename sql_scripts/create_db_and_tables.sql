DROP DATABASE IF EXISTS open_food_fact;
CREATE DATABASE open_food_fact;
USE open_food_fact;

CREATE TABLE TR_Category (
    id_category SMALLINT NOT NULL AUTO_INCREMENT,
    category_name VARCHAR(64),
    PRIMARY KEY (id_category)
);

CREATE TABLE TR_Shops (
    id_shop SMALLINT NOT NULL AUTO_INCREMENT,
    shop_name VARCHAR(64),
    PRIMARY KEY (id_shop)
);

CREATE TABLE Users (
   id_user SMALLINT NOT NULL AUTO_INCREMENT,
   user_first_name VARCHAR(64) NOT NULL,
   user_last_name VARCHAR(64),
   PRIMARY KEY (id_user)
);

CREATE TABLE TR_Country (
    id_country SMALLINT NOT NULL AUTO_INCREMENT,
    country_name VARCHAR(32),
    PRIMARY KEY (id_country)
);

CREATE TABLE TJ_Products_Category (
    id_product SMALLINT NOT NULL,
    id_category SMALLINT NOT NULL,
    PRIMARY KEY (id_product, id_category)
);

CREATE TABLE TJ_Products_Shop (
    id_product SMALLINT NOT NULL,
    id_shop SMALLINT NOT NULL,
    PRIMARY KEY (id_product, id_shop)
);

CREATE TABLE TJ_Products_Users (
    id_product SMALLINT NOT NULL,
    id_user SMALLINT NOT NULL DEFAULT 1,
    PRIMARY KEY (id_product, id_user)
);

CREATE TABLE Products (
    id_product SMALLINT NOT NULL AUTO_INCREMENT,
    manufacturing_place SMALLINT,
    product_name VARCHAR(64) NOT NULL,
    product_url VARCHAR(256) NOT NULL,
    nutrition_score VARCHAR(1),
    PRIMARY KEY (id_product)
);

ALTER TABLE TJ_Products_Category ADD CONSTRAINT fk_TJ_Products_Category_Products
FOREIGN KEY (id_product)
REFERENCES Products(id_product)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE TJ_Products_Category ADD CONSTRAINT fk_TJ_Products_Category_TR_Category
FOREIGN KEY (id_category)
REFERENCES TR_Category(id_category)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE TJ_Products_Shop ADD CONSTRAINT fk_TJ_Products_Shop_Products
FOREIGN KEY (id_product)
REFERENCES Products(id_product)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE TJ_Products_Shop ADD CONSTRAINT fk_TJ_Products_Shop_TR_Shop
FOREIGN KEY (id_shop)
REFERENCES TR_Shops(id_shop)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE TJ_Products_Users ADD CONSTRAINT fk_TJ_Products_Users_Products
FOREIGN KEY (id_product)
REFERENCES Products(id_product)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE TJ_Products_Users ADD CONSTRAINT fk_TJ_Products_Users_Users
FOREIGN KEY (id_user)
REFERENCES Users(id_user)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE Products ADD CONSTRAINT fk_Products_TR_Country 
FOREIGN KEY (manufacturing_place) 
REFERENCES TR_Country(id_country)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

INSERT INTO Users VALUES(1, "Default_user", NULL);