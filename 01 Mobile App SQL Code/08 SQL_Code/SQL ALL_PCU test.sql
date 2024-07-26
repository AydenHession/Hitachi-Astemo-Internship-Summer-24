-- Select statement to include Block A and existing stations
SELECT
    Station AS [Station-A],
    ROUND(
        CASE 
            WHEN Station = 'Block A' THEN 
                CAST(SUM(CASE WHEN Station IN ('1020', '1030', '1040', '1048', '1050', '1060', '1070', '1071', '1072', '1080') 
                    THEN NoGoodCount ELSE 0 END) AS FLOAT) / 
                (SELECT TotalCount FROM dbo.PCUStationData WHERE Station = '1016')
            ELSE CAST(NoGoodCount AS FLOAT) / NULLIF(TotalCount, 0)
        END * 100, 1
    ) AS [NG %],
    CASE 
        WHEN Station = 'Block A' THEN 
            SUM(CASE WHEN Station IN ('1020', '1030', '1040', '1048', '1050', '1060', '1070', '1071', '1072', '1080') 
                THEN NoGoodCount ELSE 0 END)
        ELSE NoGoodCount
    END AS [NG CNT]
FROM
    (
        -- Subquery to fetch existing station data
        SELECT 
            Station,
            TotalCount,
            NoGoodCount
        FROM dbo.PCUStationData
        WHERE Station IN ('1016', '1020', '1030', '1040', '1048', '1050', '1060', '1070', '1071', '1072', '1080')
        
        UNION ALL
        
        -- Subquery to add Block A
        SELECT 
            'Block A' AS Station, 
            (SELECT TotalCount FROM dbo.PCUStationData WHERE Station = '1016') AS TotalCount,
            0 AS NoGoodCount -- Placeholder for NoGoodCount to be summed
    ) AS CombinedData
GROUP BY
    Station, TotalCount, NoGoodCount
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
        WHEN 'Block A' THEN 12
        ELSE 13  -- Just in case there are any unexpected stations
    END;
