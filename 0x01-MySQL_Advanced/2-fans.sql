-- a SQL script that ranks country origins of bands
-- ordered by the number of (non-unique) fans
-- Column names must be: origin and nb_fans
-- Your script can be executed on any database

SELECT DISTINCT `band_name`,
                IFNULL(`split`, 2020) - `formed` as `lifespan`
  FROM `metal_bands` WHERE FIND_IN_SET('Glam rock', style)
  ORDER BY `lifespan` DESC;
--end of script
