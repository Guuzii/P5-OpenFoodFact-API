DROP DATABASE IF EXISTS open_food_fact;
CREATE DATABASE open_food_fact;
USE open_food_fact;

CREATE TABLE Categories (
    id_category SMALLINT NOT NULL AUTO_INCREMENT,
    category_name VARCHAR(64),
    PRIMARY KEY (id_category)
);

CREATE TABLE Shops (
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

CREATE TABLE TJ_Products_Categories (
    id_product SMALLINT NOT NULL,
    id_category SMALLINT NOT NULL,
    PRIMARY KEY (id_product, id_category)
);

CREATE TABLE TJ_Products_Shops (
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
    product_name VARCHAR(256) NOT NULL,
    product_url VARCHAR(256) NOT NULL,
    nutrition_score VARCHAR(1),
    PRIMARY KEY (id_product)
);

ALTER TABLE TJ_Products_Categories ADD CONSTRAINT fk_TJ_Products_Category_Products
FOREIGN KEY (id_product)
REFERENCES Products(id_product)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE TJ_Products_Categories ADD CONSTRAINT fk_TJ_Products_Category_TR_Category
FOREIGN KEY (id_category)
REFERENCES Categories(id_category)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE TJ_Products_Shops ADD CONSTRAINT fk_TJ_Products_Shop_Products
FOREIGN KEY (id_product)
REFERENCES Products(id_product)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE TJ_Products_Shops ADD CONSTRAINT fk_TJ_Products_Shop_TR_Shop
FOREIGN KEY (id_shop)
REFERENCES Shops(id_shop)
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

INSERT INTO Users VALUES (NULL, "Default_user", NULL);