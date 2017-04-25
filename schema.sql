drop table if exists links;
    create table links (
    id integer primary key autoincrement,
    course text not null,
    professor text not null,
    http text not null,
    description text not null
);
