CREATE TABLE vsx_dat_stars (
  id BIGSERIAL PRIMARY KEY,
  oid BIGINT,
  name TEXT,
  v INT,
  radeg DOUBLE PRECISION,
  dedeg DOUBLE PRECISION,
  type TEXT,
  period DOUBLE PRECISION
);

GRANT SELECT, INSERT, DELETE, UPDATE ON vsx_dat_stars TO star_admin;
GRANT ALL ON SEQUENCE vsx_dat_stars_id_seq TO star_admin;


DROP TABLE vsx_dat_stars;

SELECT * FROM vsx_dat_stars;