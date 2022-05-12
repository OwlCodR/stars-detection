CREATE TABLE vsx_dat_stars (
  oid BIGINT PRIMARY KEy,
  name TEXT,
  v INT,
  redeg DOUBLE PRECISION,
  dedeg DOUBLE PRECISION,
  type TEXT,
  period DOUBLE PRECISION
);

GRANT SELECT, INSERT, DELETE, UPDATE ON vsx_dat_stars TO star_admin;
GRANT ALL ON SEQUENCE vsx_dat_stars_oid_seq TO star_admin;