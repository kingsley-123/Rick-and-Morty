-- Create schema
CREATE SCHEMA IF NOT EXISTS rickmorty;

-- Create episode table
CREATE TABLE IF NOT EXISTS rickmorty.episode (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    air_date DATE,
    no_of_character INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create location table
CREATE TABLE IF NOT EXISTS rickmorty.location (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    type TEXT,
    dimension TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create character table
CREATE TABLE IF NOT EXISTS rickmorty.character (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    status TEXT,
    species TEXT,
    type TEXT,
    gender TEXT,
    origin TEXT,
    location INT REFERENCES rickmorty.location(id) ON DELETE SET NULL,
    image TEXT,
    episode INT REFERENCES rickmorty.episode(id) ON DELETE SET NULL,
    no_of_episode INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);