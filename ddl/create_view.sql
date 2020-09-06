CREATE VIEW `urusy-1.co2_view.mh_z19`
AS SELECT CAST(TIMESTAMP_ADD(AcquisitionAt, INTERVAL 9 HOUR) AS DATETIME) AS AcquisitionAt , Co2, Temperature, Tt, Ss, UhUl FROM `urusy-1.co2.mh_z19`
