DDL_QUERY =  '''
DROP TABLE IF EXISTS dim_articulo;
CREATE TABLE dim_articulo
(
 sk_articulo INT NOT NULL primary key,
 codigo VARCHAR(50),
 nombre varchar(100),
 timestamp datetime
 )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

 DROP TABLE IF EXISTS dim_persona;
 CREATE TABLE dim_persona
(
 sk_persona INT NOT NULL primary key,
 nombre varchar(100),
 timestamp datetime
 )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS dim_categoria;
 CREATE TABLE dim_categoria
(
 sk_categoria INT NOT NULL primary key,
 nombre varchar(50),
 timestamp datetime
 )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

 DROP TABLE IF EXISTS dim_dates;
 CREATE TABLE IF NOT EXISTS dim_dates (
  date_key bigint NOT NULL,
  full_date date DEFAULT NULL,
  day_of_week bigint DEFAULT NULL,
  day_num_in_month bigint DEFAULT NULL,
  day_num_overall bigint DEFAULT NULL,
  day_name text,
  day_abbrev text,
  weekday_flag text,
  week_num_in_year bigint DEFAULT NULL,
  week_num_overall bigint DEFAULT NULL,
  week_begin_date date DEFAULT NULL,
  week_begin_date_key date DEFAULT NULL,
  month bigint DEFAULT NULL,
  month_num_overall bigint DEFAULT NULL,
  month_name text,
  month_abbrev text,
  quarter bigint DEFAULT NULL,
  year bigint DEFAULT NULL,
  yearmo bigint DEFAULT NULL,
  fiscal_month bigint DEFAULT NULL,
  fiscal_quarter bigint DEFAULT NULL,
  fiscal_year bigint DEFAULT NULL,
  last_day_in_month_flag text,
  same_day_year_ago_date date DEFAULT NULL,
  PRIMARY KEY (date_key)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
 
DROP TABLE IF EXISTS fact_movimientos;
CREATE TABLE IF NOT EXISTS fact_movimientos(
   tipo int NOT NULL,
   date_key bigint NOT NULL,
   sk_articulo int NOT NULL,
   sk_persona int NOT NULL,
   sk_categoria int NOT NULL,
   cantidad int DEFAULT NULL,
   precio decimal(11,2) DEFAULT NULL,
   descuento decimal(11,2) DEFAULT NULL,
   PRIMARY KEY (tipo,date_key,sk_articulo,sk_persona,sk_categoria),
   CONSTRAINT fk_datekey FOREIGN KEY (date_key) REFERENCES dim_dates(date_key),
   CONSTRAINT fk_articulo FOREIGN KEY (sk_articulo) REFERENCES dim_articulo(sk_articulo),
   CONSTRAINT fk_persona FOREIGN KEY (sk_persona) REFERENCES dim_persona(sk_persona),
   CONSTRAINT fk_categoria FOREIGN KEY (sk_categoria) REFERENCES dim_categoria(sk_categoria)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
 
'''
 
 
 
 
 