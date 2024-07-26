SELECT 
  Station AS [Station-A],
  CASE 
    WHEN TotalCount = 0 THEN 0 
    ELSE ROUND((CAST(NoGoodCount AS FLOAT) / TotalCount) * 100, 1) 
  END AS [NG %],
  NoGoodCount AS [NG CNT]
FROM dbo.PCUStationData
WHERE Station IN ('1016', '1020', '1030', '1040', '1048', '1050', '1060', '1070', '1071', '1072', '1080')
ORDER BY 
  CASE Station 
    WHEN '1016' THEN 1
    WHEN '1020' THEN 2
    WHEN '1030' THEN 3
    WHEN '1040' THEN 4
    WHEN '1048' THEN 5
    WHEN '1050' THEN 6
    WHEN '1060' THEN 7
    WHEN '1070' THEN 8
    WHEN '1071' THEN 9
    WHEN '1072' THEN 10
    WHEN '1080' THEN 11
    ELSE 12  -- Just in case there are any unexpected stations
  END;