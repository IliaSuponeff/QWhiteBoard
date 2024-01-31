CREATE TABLE IF NOT EXISTS "slides" (
	"id"	INTEGER NOT NULL,
	"album_name"	TEXT NOT NULL,
	"position"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "albums" (
	"id"	INTEGER NOT NULL,
	"shelf_name"	TEXT DEFAULT "",
	"name"	TEXT NOT NULL UNIQUE,
	"create_on"	TEXT NOT NULL,
	"change_on"	TEXT NOT NULL,
	"slide_type"	INTEGER NOT NULL,
	"slide_size"	TEXT NOT NULL,
	"description"	INTEGER NOT NULL,
	"is_archived"	INTEGER NOT NULL DEFAULT 0,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "shelfs" (
	"id"	INTEGER NOT NULL,
	"name"	TEXT NOT NULL,
	"create_on"	TEXT NOT NULL,
	"change_on"	TEXT NOT NULL,
	"description"	TEXT NOT NULL,
	"is_archived"	INTEGER NOT NULL DEFAULT 0,
	PRIMARY KEY("id" AUTOINCREMENT)
);
