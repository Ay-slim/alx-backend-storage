-- My names SQL
DROP INDEX IF EXISTS idx_name_first;
CREATE INDEX IF NOT EXISTS idx_name_first ON names (LEFT(name, 1));
