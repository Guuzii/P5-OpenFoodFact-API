DROP DATABASE IF EXISTS open_food_fact;
CREATE DATABASE open_food_fact;


USE open_food_fact;

CREATE TABLE TR_Category (
    id_category SMALLINT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
    category_name VARCHAR(64)
)
ENGINE=INNODB;

CREATE TABLE TR_Country (
    id_country SMALLINT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
    country_name VARCHAR(32)
)
ENGINE=INNODB;

CREATE TABLE TR_Shops (
    id_shop SMALLINT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
    shop_name VARCHAR(64)
)
ENGINE=INNODB;

CREATE TABLE Users (
   id_user SMALLINT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
   user_first_name VARCHAR(64) NOT NULL,
   user_last_name VARCHAR(64)
)
ENGINE=INNODB;

CREATE TABLE Products (
    id_product SMALLINT UNSIGNED NOT NULL PRIMARY KEY  AUTO_INCREMENT,
    product_category INT NOT NULL,
    manufacturing_place INT,
    shop INT,
    product_name VARCHAR(64) NOT NULL,
    product_url VARCHAR(256) NOT NULL,
    nutrition_score VARCHAR(1),
    CONSTRAINT fk_Products_TR_Category FOREIGN KEY (product_category) REFERENCES TR_Category(id_category),
    CONSTRAINT fk_Products_TR_Country FOREIGN KEY (manufacturing_place) REFERENCES TR_Country(id_country),
    CONSTRAINT fk_Products_TR_Shops FOREIGN KEY (shop) REFERENCES TR_Shop(id_shop)
)
ENGINE=INNODB;

CREATE TABLE Users_Favorites (
    id_product SMALLINT UNSIGNED NOT NULL,
    id_user SMALLINT UNSIGNED NOT NULL DEFAULT 0,
    PRIMARY KEY (id_product, id_user),
    CONSTRAINT fk_Users_Favorites_Products FOREIGN KEY (id_product) REFERENCES Products(id_product),
    CONSTRAINT fk_Users_Favorites_Users FOREIGN KEY (id_user) REFERENCES Users(id_user)
)
ENGINE=INNODB;

INSERT INTO Users VALUES(0, "Default_user", NULL);