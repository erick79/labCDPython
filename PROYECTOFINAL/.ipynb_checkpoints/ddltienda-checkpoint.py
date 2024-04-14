DDL_QUERY =  '''
CREATE TABLE IF NOT EXISTS rol(
    idrol INT PRIMARY KEY,
    nombre VARCHAR(30),
    descripcion varchar(255),
    estado bit
);
CREATE TABLE IF NOT EXISTS usuario(
    idusuario INT PRIMARY KEY,
    idrol INT,
    nombre VARCHAR(100),
    tipo_documento VARCHAR(20),
    num_documento VARCHAR(20),
    direccion VARCHAR(70),
    telefono VARCHAR(20),
    email VARCHAR(50), 
    clave bytea,
    estado bit,
    CONSTRAINT fk_usuariorol FOREIGN KEY (idrol) REFERENCES rol(idrol)
);

CREATE TABLE IF NOT EXISTS categoria(
    idcategoria INT PRIMARY KEY,
    nombre VARCHAR(50),
    descripcion varchar(255),
    estado bit
);

CREATE TABLE IF NOT EXISTS articulo(
    idarticulo INT PRIMARY KEY,
    idcategoria int,
    codigo varchar(50) UNIQUE,
    nombre VARCHAR(100),
    precio_venta decimal(11,2),
    stock int,
    descripcion varchar(255),
    imagen varchar(20),
    estado bit,
    CONSTRAINT fk_articulocategoria FOREIGN KEY (idcategoria) REFERENCES categoria(idcategoria)
);

CREATE TABLE IF NOT EXISTS persona(
    idpersona INT PRIMARY KEY,
    tipo_persona varchar(20),
    nombre varchar(20),
    tipo_documento varchar(20),
    num_documento varchar(20),
    direccion varchar(70),
    telefono varchar(20),
    email varchar(50)
);


CREATE TABLE IF NOT EXISTS ingreso(
    idingreso INT PRIMARY KEY,
    idproveedor int,
    idusuario int,
    tipo_comprobante varchar(20),
    serie_comprobante VARCHAR(7),
    num_comprobante VARCHAR(10),
    fecha timestamp,
    impuesto decimal(4,2),
    total decimal(11,2),
    estado varchar(20),
    CONSTRAINT fk_ingresopersona FOREIGN KEY (idproveedor) REFERENCES persona(idpersona),
    CONSTRAINT fk_ingresousuario FOREIGN KEY (idusuario) REFERENCES usuario(idusuario)
);


CREATE TABLE IF NOT EXISTS detalle_ingreso(
    iddetalle_ingreso INT PRIMARY KEY,
    idingreso int,
    idarticulo int,
    cantidad int,
    precio decimal(11,2),
    CONSTRAINT fk_detalleingreso FOREIGN KEY (idingreso) REFERENCES ingreso(idingreso),
    CONSTRAINT fk_detallearticulo FOREIGN KEY (idarticulo) REFERENCES articulo(idarticulo)
);



CREATE TABLE IF NOT EXISTS venta(
    idventa INT PRIMARY KEY,
    idcliente int,
    idusuario int,
    tipo_comprobante varchar(20),
    serie_comprobante VARCHAR(7),
    num_comprobante VARCHAR(10),
    fecha timestamp,
    impuesto decimal(4,2),
    total decimal(11,2),
    estado varchar(20),
    CONSTRAINT fk_ventapersona FOREIGN KEY (idcliente) REFERENCES persona(idpersona),
    CONSTRAINT fk_ventausuario FOREIGN KEY (idusuario) REFERENCES usuario(idusuario)
);


CREATE TABLE IF NOT EXISTS detalle_venta(
    iddetalle_venta INT PRIMARY KEY,
    idventa int,
    idarticulo int,
    cantidad int,
    precio decimal(11,2),
    descuento decimal(4,2),
    CONSTRAINT fk_detalledetalleventa2 FOREIGN KEY (idventa) REFERENCES venta(idventa),
    CONSTRAINT fk_detalleventaarticulo2 FOREIGN KEY (idarticulo) REFERENCES articulo(idarticulo)
);

'''