create table if not exists entries (
  id integer primary key autoincrement,
  project text not null,
  version integer not null,
  log text not null
);