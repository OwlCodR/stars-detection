CREATE ROLE star_admin WITH CREATEDB LOGIN PASSWORD 'stars';
CREATE DATABASE star_db OWNER star_admin;

CREATE TABLE sky_2MASS_APASS_01_with_VSX_type (
  id BIGINT PRIMARY KEY,
  angDist double precision,
  RAJ2000 double precision,
  DEJ2000 double precision,
  Jmag real,
  Hmag real,
  Kmag real,
  e_Jmag real,
  e_Hmag real,
  e_Kmag real,
  nobs smallint,
  mobs smallint,
  B-V real,
  e_B-V real,
  Vmag real,
  e_Vmag real,
  Bmag real,
  e_Bmag real,
  gpmag real,
  e_gpmag real,
  rpmag real,
  e_rpmag real,
  ipmag real,
  e_ipmag real,
);

GRANT SELECT, INSERT, DELETE, UPDATE ON sky_2MASS_APASS_01_with_VSX_type TO star_admin;
GRANT ALL ON SEQUENCE sky_2MASS_APASS_01_with_VSX_type_id_seq TO star_admin;