create table member(
    m_id varchar(50) primary key,
    name varchar(20) not null,
    phone varchar(20) not null, 
    email varchar(50) UNIQUE,
    type int check(type in (1,2)), -- 1 = normal member, 2 = contract member
    user_status int default 1, -- we still want data even though user delete one's account. 1 = user, 2 = deleted user
    reg_date DATE NOT NULL, -- date that user create account
    billing_date DATE -- NULL if type == 1,
);

create table memberAddress(
    id BIGINT not null auto_increment primary key, #django need this IDK why
    m_id varchar(50),
    address1 varchar(50) not null,
    address2 varchar(50),
    state varchar(2) not null,
    zipcode varchar(15) not null,
    foreign key (m_id) references member(m_id),
    UNIQUE(m_id, address1)
);

create table memberCardInfo(
	id BIGINT not null auto_increment primary key, #django need this... IDK why
    m_id varchar(50),
    card_num varchar(20) not null UNIQUE,
    card_name varchar(30) not null,
    card_exp_month int constraint card01 check(card_exp_month between 1 and 12),
    card_exp_year int constraint card02 check(card_exp_year between 0 and 99),
    foreign key (m_id) references member(m_id),
    balance double not null,
    UNIQUE(m_id, card_num)
);




CREATE TABLE manufacturer(
	manufacturer_id varchar(20) primary key,
	manufacturer_name varchar(100),
	email varchar (30) not null,
	phone_num varchar(20) not null
);

CREATE TABLE product (
    p_id varchar(10) primary key,
    category varchar(30) not null,
    p_name varchar(50) not null,
    wholesale_price double not null,
    instore_price double not null,
    manufacturer_id varchar(20),
    FOREIGN Key (manufacturer_id) REFERENCES manufacturer(manufacturer_id)
);

create table warehouse(
	w_id varchar(10) primary key,
	address1 varchar(20) not null,
	state VARCHAR(2) not null,
	zipcode varchar(15) not null
);

create table store(
    s_id varchar(10) primary KEY,
    address VARCHAR(20) not null,
    state varchar(2) not null,
    zipcode varchar(15) not null
);


CREATE TABLE warehouseReorder(
	w_id varchar(10), 
	manufacturer_id varchar(10),
	p_id varchar(10),
	quantity int default 0, 
	reorderDate date not NULL,
	FOREIGN key (w_id) references warehouse(w_id),
	foreign key (manufacturer_id) references manufacturer(manufacturer_id),
	foreign key (p_id) references product(p_id),
	primary key (w_id, p_id, reorderDate)
);

Create Table storeReorder(
	s_id varchar(10),
	w_id varchar(10),
	p_id varchar(10),
	quantity int default 0,
	reorderDate date not null,
	foreign key (s_id) references store(s_id),
	foreign key (w_id) references warehouse(w_id),
	foreign key (p_id) references product(p_id),
	primary key (s_id, p_id, reorderDate)
);


create table storeINV(
	s_id varchar(10),
	p_id varchar(10),
	quantity int default 0,
	threshold int default 0,
	FOREIGN key (s_id) references store(s_id),
	FOREIGN KEY (p_id) references product(p_id),
	PRIMARY key (s_id, p_id),
	type int check(type in (0,1))
);


create table warehouseINV(
	id BIGINT not null auto_increment primary key,
	w_id varchar(10),
	p_id varchar(10),
	quantity int default 0,
	threshold int default 0,
	foreign key (w_id) references warehouse(w_id),
	foreign key (p_id) references product(p_id),
	UNIQUE (w_id, p_id)
);


create table whCoverage( -- this table illustrates each warehouse's state coverage for shipping
    w_id varchar(10),
    state varchar(10),-- Illinois, Michigan etc...
    FOREIGN key (w_id) references warehouse(w_id),
    primary key(w_id, state)
);

create table whStore( -- This table illustrates each warehouse's store coverage for replenishing
    w_id varchar(10),
    s_id varchar(10),
    primary key(w_id, s_id),
    foreign key (w_id) references warehouse(w_id),
    foreign key (s_id) references store(s_id)
);

CREATE TABLE orderList(
	order_id BIGINT not null auto_increment,
	order_date date not null,
	primary key(order_id)
);


create table ShippingCompany(
	sc_id varchar(20) primary key,
	sc_name varchar(50)
);

create table onlineOrder(
	id BIGINT not null auto_increment primary key,
	order_id BIGINT not null,
	foreign key (order_id) references orderList(order_id),
	
	order_date date not null,	
	
	p_id varchar(10),
	FOREIGN KEY (p_id) REFERENCES product(p_id),
	
	quantity int not null,

	customer_type int CHECK(customer_type in (0, 1, 2)), -- 0: non-member , 1: normal-member, 2:subscript member
	
	m_id varchar(50),

	FOREIGN key (m_id) references member(m_id),
	
	email varchar(30),
	card_info varchar(20) not null,
	
	address1 varchar(50) not null,
	address2 varchar(50),
	state varchar(2) not null,
	zip_code varchar(15) not null,
	
	phone_num BIGINT not null,
	
	recipient_name varchar(30) not null,
	recipient_phone BIGINT not null,
	sc_id varchar(20),
	FOREIGN key (sc_id) references ShippingCompany(sc_id),
	tracking_num varchar(50) not null
);

create table instoreOrder(
	order_id BIGINT not null,
	foreign key (order_id) references orderList(order_id),

	s_id varchar(10), 
	FOREIGN key (s_id) REFERENCES store(s_id),
	
	p_id varchar(10), 
	FOREIGN key (p_id) references product(p_id),
	
	quantity int not null,

	customer_type int CHECK(customer_type in (0,1,2)),
	m_id varchar(50),
	FOREIGN key(m_id) references member (m_id)
);

create table cart(
	id BIGINT not null auto_increment primary key,
	m_id varchar(50) not null,
	foreign key (m_id) references member(m_id),
	
	p_id varchar(10) not null,
	foreign key (p_id) references product(p_id),

	quantity int not null,
	UNIQUE(m_id, p_id)
);

delimiter //
Create Trigger warehouseInit
	after insert on product for each row
	Begin
		declare seq_id INT;
			set seq_id = (select count(*) from product);
		insert into warehouseINV values(seq_id, "w_1", new.p_id, 0, 30);
	end //
delimeter;

INSERT INTO `db`.`product` (`p_id`, `category`, `p_name`, `wholesale_price`, `instore_price`, `manufacturer_id`) VALUES ('p_1', 'computer', 'Galaxy Book', 1000, 1200, 'man_01');
INSERT INTO `db`.`product` (`p_id`, `category`, `p_name`, `wholesale_price`, `instore_price`, `manufacturer_id`) VALUES ('p_2', 'phone', 'galaxy s 22', 1000, 1300, 'man_01');
INSERT INTO `db`.`product` (`p_id`, `category`, `p_name`, `wholesale_price`, `instore_price`, `manufacturer_id`) VALUES ('p_3', 'phone', 'galaxy z flip', 1200, 1400, 'man_01');
INSERT INTO `db`.`product` (`p_id`, `category`, `p_name`, `wholesale_price`, `instore_price`, `manufacturer_id`) VALUES ('p_4', 'tablet', 'galaxy tab', 1300, 1450, 'man_01');
INSERT INTO `db`.`product` (`p_id`, `category`, `p_name`, `wholesale_price`, `instore_price`, `manufacturer_id`) VALUES ('p_5', 'computer', 'macbook air', 800, 1000, 'man_02');
INSERT INTO `db`.`product` (`p_id`, `category`, `p_name`, `wholesale_price`, `instore_price`, `manufacturer_id`) VALUES ('p_6', 'computer', 'macbook pro', 1500, 1700, 'man_02');
INSERT INTO `db`.`product` (`p_id`, `category`, `p_name`, `wholesale_price`, `instore_price`, `manufacturer_id`) VALUES ('p_7', 'computer', 'macbook studio', 2500, 2700, 'man_02');
INSERT INTO `db`.`product` (`p_id`, `category`, `p_name`, `wholesale_price`, `instore_price`, `manufacturer_id`) VALUES ('p_8', 'phone', 'Iphone14', 1300, 1400, 'mann_02');
INSERT INTO `db`.`product` (`p_id`, `category`, `p_name`, `wholesale_price`, `instore_price`, `manufacturer_id`) VALUES ('p_9', 'tablet', 'Ipad', 1500, 1700, 'man_02');
INSERT INTO `db`.`product` (`p_id`, `category`, `p_name`, `wholesale_price`, `instore_price`, `manufacturer_id`) VALUES ('p_10', 'computer', 'dell book', 1100, 1300, 'man_03');
INSERT INTO `db`.`product` (`p_id`, `category`, `p_name`, `wholesale_price`, `instore_price`, `manufacturer_id`) VALUES ('p_11', 'computer ', 'dell book pro', 1600, 1800, 'man_03');
INSERT INTO `db`.`product` (`p_id`, `category`, `p_name`, `wholesale_price`, `instore_price`, `manufacturer_id`) VALUES ('p_12', 'computre', 'Lenovo Carbon', 1700, 1900, 'man_04');
INSERT INTO `db`.`product` (`p_id`, `category`, `p_name`, `wholesale_price`, `instore_price`, `manufacturer_id`) VALUES ('p_13', 'computer', 'Lenovo Think pad', 1400, 2600, 'man_04');
INSERT INTO `db`.`product` (`p_id`, `category`, `p_name`, `wholesale_price`, `instore_price`, `manufacturer_id`) VALUES ('p_14', 'accessory', 'Logitech keyboard', 200, 250, 'man_05');
INSERT INTO `db`.`product` (`p_id`, `category`, `p_name`, `wholesale_price`, `instore_price`, `manufacturer_id`) VALUES ('p_15', 'accessory', 'Logitech keyboard pro', 400, 450, 'man_05');
INSERT INTO `db`.`product` (`p_id`, `category`, `p_name`, `wholesale_price`, `instore_price`, `manufacturer_id`) VALUES ('p_16', 'accessory', 'Logitech mouse', 50, 100, 'man_05');
INSERT INTO `db`.`product` (`p_id`, `category`, `p_name`, `wholesale_price`, `instore_price`, `manufacturer_id`) VALUES ('p_17', 'computer', 'Razer blade 13', 1500, 1700, 'man_06');
INSERT INTO `db`.`product` (`p_id`, `category`, `p_name`, `wholesale_price`, `instore_price`, `manufacturer_id`) VALUES ('p_18', 'computer', 'Razer blade 15', 1700, 1900, 'man_06');
INSERT INTO `db`.`product` (`p_id`, `category`, `p_name`, `wholesale_price`, `instore_price`, `manufacturer_id`) VALUES ('p_19', 'phone', 'google pixel 6', 1200, 1400, 'man_07');
INSERT INTO `db`.`product` (`p_id`, `category`, `p_name`, `wholesale_price`, `instore_price`, `manufacturer_id`) VALUES ('p_20', 'phone', 'google pixel 4a', 700, 900, 'man_07');
INSERT INTO `db`.`product` (`p_id`, `category`, `p_name`, `wholesale_price`, `instore_price`, `manufacturer_id`) VALUES ('p_21', 'phone', 'xperia xi', 1300, 1400, 'man_08');
INSERT INTO `db`.`product` (`p_id`, `category`, `p_name`, `wholesale_price`, `instore_price`, `manufacturer_id`) VALUES ('p_22', 'camera', 'sony xdr cam', 1500, 1700, 'man_08');
INSERT INTO `db`.`product` (`p_id`, `category`, `p_name`, `wholesale_price`, `instore_price`, `manufacturer_id`) VALUES ('p_23', 'camera', 'sony dslr', 2999, 3200, 'man_08');
INSERT INTO `db`.`product` (`p_id`, `category`, `p_name`, `wholesale_price`, `instore_price`, `manufacturer_id`) VALUES ('p_24', 'camera', 'canon pro', 3000, 3300, 'man_09');
INSERT INTO `db`.`product` (`p_id`, `category`, `p_name`, `wholesale_price`, `instore_price`, `manufacturer_id`) VALUES ('p_25', 'camera', 'canon beginner', 1200, 1400, 'man_09');