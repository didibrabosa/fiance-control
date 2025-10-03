CREATE TABLE IF NOT EXISTS accounts (
    account_id SERIAL PRIMARY KEY,
    account_name VARCHAR(100) NOT NULL,
    account_status BOOLEAN NOT NULL DEFAULT TRUE,
    balance NUMERIC(10,2) NOT NULL DEFAULT 0.00,
    debt NUMERIC(10,2) NOT NULL DEFAULT 0.00,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NULL
);

CREATE TABLE IF NOT EXISTS goals (
    goal_id SERIAL PRIMARY KEY,
    account_id INTEGER NOT NULL REFERENCES accounts(account_id),
    goal_value NUMERIC(10,2) DEFAULT 0.00,
    current_value NUMERIC(10,2) DEFAULT 0.00
);

CREATE TABLE IF NOT EXISTS categories (
    categorie_id SERIAL PRIMARY KEY,
    categorie_name VARCHAR NOT NULL
);

CREATE TABLE IF NOT EXISTS costs (
    cost_id SERIAL PRIMARY KEY,
    account_id INTEGER NOT NULL REFERENCES accounts(account_id),
    categorie_id INTEGER NOT NULL REFERENCES categories(categorie_id),
    cost_value NUMERIC(10,2) NOT NULL DEFAULT 0.00,
    due_date TIMESTAMP DEFAULT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NULL
);