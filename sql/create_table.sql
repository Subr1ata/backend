create table category (
	id bigserial not null,
	name text,
	parent bigint,
	logo text,
	active bool default true,
	constraint pkey_category primary key (id)
);

create table product (
	id bigserial not null,
	name text,
	category bigint,
	cost int,
	price int,
	star int,
	image bigint,
	description text,
	sales int,
	comment text,
	ship_comment text,
	active bool default true,
	constraint pkey_product primary key (id)
)

create table image (
	id bigserial not null,
	name text,
	url text,
	active bool default true,
	constraint pkey_product primary key (id),
)